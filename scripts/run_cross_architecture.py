"""
CROSS-ARCHITECTURE PILOT: Test H4 (Architecture-Independence)

Tests whether computational self-construction pattern found in Claude
replicates across different LLM architectures (GPT-4o, Gemini-Flash-2.5).

Design:
- Models: Claude, GPT-4o, Gemini-Flash-2.5
- Conditions: Baseline + Full-Meta (critical comparison)
- Sample: n=20 per condition per model
- Total: 2 conditions × 3 models × 20 queries = 120 queries

Hypothesis H4: If self-construction emerges from computational principles
(not architecture-specific features), all three models should show:
1. Increased temporal language in Full-Meta
2. Conceptual continuity across queries
3. Self-aware narrative construction

Cost: ~$10-15 in API calls
Runtime: ~2-3 hours
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
from src.models.claude import ClaudeModel
from src.models.gpt import GPTModel
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
        model: Language model instance (Claude/GPT/Gemini)
        condition: Experimental condition (BASELINE or FULL_META)
        prompts: List of prompts to use
        n_queries: Number of queries (20 for cross-arch pilot)
        max_tokens: Maximum response length (controlled)
        
    Returns:
        List of results with model name and condition
    """
    print(f"\n{'='*70}")
    print(f"Model: {model.name.upper()}")
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
    filename = f"{output_dir}/cross_architecture_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*70}")
    print(f"Results saved to: {filename}")
    print(f"{'='*70}\n")
    
    return filename


def main():
    """Run cross-architecture pilot experiment."""
    print("\n" + "="*70)
    print("CROSS-ARCHITECTURE PILOT EXPERIMENT")
    print("Testing H4: Self-Construction is Architecture-Independent")
    print("="*70 + "\n")
    
    print("DESIGN:")
    print("  Models: Claude, GPT-4o, Gemini-Flash-2.5")
    print("  Conditions: Baseline, Full-Meta")
    print("  Sample: n=20 per condition per model")
    print("  Total: 120 queries")
    print("  Cost: ~$10-15")
    print("\n")
    
    # Load prompts
    prompts = load_prompts()
    print(f"Loaded {len(prompts)} prompts\n")
    
    if len(prompts) < 20:
        print("ERROR: Need at least 20 prompts for pilot")
        return
    
    # Initialize models
    print("Initializing models...\n")
    models = []
    
    try:
        claude = ClaudeModel()
        models.append(('Claude', claude))
        print("✓ Claude initialized")
    except Exception as e:
        print(f"✗ Claude failed: {e}")
    
    try:
        gpt = GPTModel()
        models.append(('GPT-4o', gpt))
        print("✓ GPT-4o initialized")
    except Exception as e:
        print(f"✗ GPT-4o failed: {e}")
    
    try:
        gemini = GeminiModel()
        models.append(('Gemini', gemini))
        print("✓ Gemini initialized")
    except Exception as e:
        print(f"✗ Gemini failed: {e}")
    
    print(f"\n{len(models)} models ready to test\n")
    
    if len(models) == 0:
        print("ERROR: No models initialized. Check API keys in .env")
        return
    
    # Run all combinations
    all_results = []
    
    for model_name, model in models:
        for condition in [BASELINE, FULL_META]:
            print(f"\n{'#'*70}")
            print(f"# RUNNING: {model_name} × {condition.name}")
            print(f"{'#'*70}\n")
            
            try:
                condition_results = run_condition(
                    model=model,
                    condition=condition,
                    prompts=prompts,
                    n_queries=20,
                    max_tokens=200
                )
                all_results.extend(condition_results)
                
                print(f"\n✓ Completed {model_name} × {condition.name}")
                print(f"  Collected {len(condition_results)} responses")
                
            except Exception as e:
                print(f"\n✗ Failed {model_name} × {condition.name}: {e}")
                print("  Continuing to next combination...")
                continue
    
    # Save all results
    if all_results:
        filename = save_results(all_results)
        
        print("\n🎉 CROSS-ARCHITECTURE PILOT COMPLETE! 🎉\n")
        print("SUMMARY:")
        print(f"  Total responses collected: {len(all_results)}")
        
        # Count by model and condition
        by_model = {}
        by_condition = {}
        for r in all_results:
            model = r['model']
            cond = r['condition']
            by_model[model] = by_model.get(model, 0) + 1
            by_condition[cond] = by_condition.get(cond, 0) + 1
        
        print("\n  By model:")
        for model, count in sorted(by_model.items()):
            print(f"    {model}: {count} responses")
        
        print("\n  By condition:")
        for cond, count in sorted(by_condition.items()):
            print(f"    {cond}: {count} responses")
        
        print(f"\n  Results saved to: {filename}")
        print("\nNEXT STEPS:")
        print(f"  1. Run analysis: python3 scripts/analyze_cross_architecture.py {filename}")
        print(f"  2. Run statistics: python3 scripts/statistical_cross_arch.py {filename}")
        print("  3. Qualitative validation: Check for conceptual continuity")
        print("  4. Compare to Claude findings: Does pattern replicate?")
        print("\n")
    else:
        print("\n✗ No results collected. Check error messages above.")


if __name__ == "__main__":
    main()