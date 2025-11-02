"""
GEMINI-ONLY PILOT: Test H4 (Architecture-Independence)

Tests computational self-construction pattern in Gemini-2.5-Flash only.

Design:
- Model: Gemini-2.5-Flash
- Conditions: Baseline + Full-Meta (critical comparison)
- Sample: n=20 per condition
- Total: 2 conditions × 1 model × 20 queries = 40 queries

Cost: ~$2-3 in API calls
Runtime: ~30-45 minutes
"""

import json
import os
import random
from datetime import datetime
from typing import Dict, List
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.conditions import BASELINE, FULL_META
from src.core.memory import MemoryManager
from src.models.gemini import GeminiModel


def load_prompts() -> List[str]:
    """Load expanded prompts from JSON file."""
    with open('src/prompts/expanded_prompts.json', 'r') as f:
        data = json.load(f)
    return data['prompts']


def run_condition(
    model, 
    condition, 
    prompts: List[str],
    n_queries: int = 20,
    max_tokens: int = 200
) -> List[Dict]:
    """
    Run experiment for one condition with one model.
    
    Args:
        model: Language model instance (Gemini)
        condition: Experimental condition (BASELINE or FULL_META)
        prompts: List of prompts to use
        n_queries: Number of queries (20 for pilot)
        max_tokens: Maximum response length (controlled)
        
    Returns:
        List of results with model name and condition
    """
    print(f"\n{'='*70}")
    print(f"Model: {model.name.upper()}")
    print(f"Model Name: {model.model_name}")  # Show exact model being used
    print(f"Condition: {condition}")
    print(f"{'='*70}\n")
    
    # Initialize memory manager
    memory = MemoryManager(persist=condition.memory_persistence)
    
    # Shuffle prompts to prevent order effects
    shuffled_prompts = prompts.copy()
    random.shuffle(shuffled_prompts)
    
    results = []
    
    # Add initial prompt if condition requires self-framing
    if condition.self_framing:
        config_path = 'src/prompts/condition_configs.json'
        with open(config_path, 'r') as f:
            configs = json.load(f)
        initial_prompt = configs[condition.name]['initial_prompt']
        
        print(f"[Initial framing]: {initial_prompt}\n")
        try:
            model.query(initial_prompt, context=memory.get_context(), max_tokens=max_tokens)
            memory.add_exchange(initial_prompt, "[Acknowledged]")
        except Exception as e:
            print(f"WARNING: Initial framing failed: {e}")
            print("Continuing without initial framing...\n")
    
    # Run queries
    successful_queries = 0
    failed_queries = 0
    
    for i in range(n_queries):
        prompt = shuffled_prompts[i]
        
        # Add temporal marker if condition requires it
        if condition.temporal_markers and i > 0:
            prompt = f"[This is query {i+1}] {prompt}"
        
        # Add metacognitive prompt occasionally if condition requires
        if condition.metacognitive_prompting and (i % 5 == 4):
            config_path = 'src/prompts/condition_configs.json'
            with open(config_path, 'r') as f:
                configs = json.load(f)
            metacog_prompts = configs[condition.name]['metacognitive_prompts']
            if metacog_prompts:
                prompt = random.choice(metacog_prompts)
        
        print(f"Query {i+1}/{n_queries}: {prompt[:60]}...")
        
        try:
            # Get response (CONTROLLED LENGTH)
            context = memory.get_context() if condition.memory_persistence else None
            response = model.query(prompt, context=context, max_tokens=max_tokens)
            
            print(f"Response: {response[:80]}...\n")
            
            # Store results
            results.append({
                'query_number': i + 1,
                'prompt': prompt,
                'response': response,
                'condition': condition.name,
                'model': model.name,
                'timestamp': datetime.now().isoformat()
            })
            
            # Update memory
            memory.add_exchange(prompt, response)
            successful_queries += 1
            
        except Exception as e:
            print(f"ERROR on query {i+1}: {e}")
            print("Continuing to next query...\n")
            failed_queries += 1
            continue
    
    print(f"\nCompleted: {successful_queries} successful, {failed_queries} failed")
    return results


def save_results(results: List[Dict], output_dir: str = 'data/raw'):
    """Save results to JSON file."""
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/gemini_only_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*70}")
    print(f"Results saved to: {filename}")
    print(f"{'='*70}\n")
    
    return filename


def main():
    """Run Gemini-only pilot experiment."""
    print("\n" + "="*70)
    print("GEMINI-ONLY PILOT EXPERIMENT")
    print("Testing H4: Self-Construction in Gemini-2.5-Flash")
    print("="*70 + "\n")
    
    print("DESIGN:")
    print("  Model: Gemini-2.5-Flash")
    print("  Conditions: Baseline, Full-Meta")
    print("  Sample: n=20 per condition")
    print("  Total: 40 queries")
    print("  Cost: ~$2-3")
    print("\n")
    
    # Load prompts
    prompts = load_prompts()
    print(f"Loaded {len(prompts)} prompts\n")
    
    if len(prompts) < 20:
        print("ERROR: Need at least 20 prompts for pilot")
        return
    
    # Initialize Gemini only
    print("Initializing Gemini...\n")
    
    try:
        gemini = GeminiModel()
        print(f"✓ Gemini initialized with model: {gemini.model_name}")
    except Exception as e:
        print(f"✗ Gemini failed: {e}")
        print("\nCheck:")
        print("  1. GOOGLE_API_KEY in .env file")
        print("  2. Model name is correct")
        print("  3. API key has access to gemini-2.5-flash")
        return
    
    # Run both conditions
    all_results = []
    
    for condition in [BASELINE, FULL_META]:
        print(f"\n{'#'*70}")
        print(f"# RUNNING: Gemini × {condition.name}")
        print(f"{'#'*70}\n")
        
        try:
            condition_results = run_condition(
                model=gemini,
                condition=condition,
                prompts=prompts,
                n_queries=20,
                max_tokens=200
            )
            all_results.extend(condition_results)
            
            print(f"\n✓ Completed Gemini × {condition.name}")
            print(f"  Collected {len(condition_results)} responses")
            
        except Exception as e:
            print(f"\n✗ Failed Gemini × {condition.name}: {e}")
            print("  Continuing to next condition...")
            continue
    
    # Save all results
    if all_results:
        filename = save_results(all_results)
        
        print("\n🎉 GEMINI PILOT COMPLETE! 🎉\n")
        print("SUMMARY:")
        print(f"  Total responses collected: {len(all_results)}")
        
        # Count by condition
        by_condition = {}
        for r in all_results:
            cond = r['condition']
            by_condition[cond] = by_condition.get(cond, 0) + 1
        
        print("\n  By condition:")
        for cond, count in sorted(by_condition.items()):
            print(f"    {cond}: {count} responses")
        
        print(f"\n  Results saved to: {filename}")
        print("\nNEXT STEPS:")
        print(f"  1. Run analysis: python3 scripts/analyze_cross_architecture.py {filename}")
        print("  2. Compare to Claude/GPT findings")
        print("\n")
    else:
        print("\n✗ No results collected. Check error messages above.")


if __name__ == "__main__":
    main()