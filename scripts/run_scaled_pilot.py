"""
Scaled Pilot Experiment: n=20 per condition, all 4 conditions.

Controls for response length, uses expanded prompt set,
provides adequate statistical power.
"""

import json
import os
import random
from datetime import datetime
from typing import Dict, List
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.conditions import BASELINE, MEMORY_ONLY, FULL_BASIC, FULL_META
from src.core.memory import MemoryManager
from src.models.claude import ClaudeModel


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
    max_tokens: int = 200  # CONTROLLED LENGTH
) -> List[Dict]:
    """
    Run scaled experiment for one condition.
    
    Args:
        model: Language model instance
        condition: Experimental condition
        prompts: List of prompts to use
        n_queries: Number of queries (default 20 for scaled pilot)
        max_tokens: Maximum response length (controls length confound)
        
    Returns:
        List of results
    """
    print(f"\n{'='*70}")
    print(f"Running condition: {condition}")
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
        model.query(initial_prompt, context=memory.get_context(), max_tokens=max_tokens)
        memory.add_exchange(initial_prompt, "[Acknowledged]")
    
    # Run queries
    for i in range(n_queries):
        prompt = shuffled_prompts[i]
        
        # Add temporal marker if condition requires it
        if condition.temporal_markers and i > 0:
            prompt = f"[This is query {i+1}] {prompt}"
        
        # Add metacognitive prompt occasionally if condition requires
        if condition.metacognitive_prompting and (i % 5 == 4):  # Every 5th query
            config_path = 'src/prompts/condition_configs.json'
            with open(config_path, 'r') as f:
                configs = json.load(f)
            metacog_prompts = configs[condition.name]['metacognitive_prompts']
            if metacog_prompts:
                prompt = random.choice(metacog_prompts)
        
        print(f"Query {i+1}/{n_queries}: {prompt[:60]}...")
        
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
            'timestamp': datetime.now().isoformat()
        })
        
        # Update memory
        memory.add_exchange(prompt, response)
    
    return results


def save_results(results: List[Dict], model_name: str, output_dir: str = 'data/raw'):
    """Save results to JSON file."""
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/scaled_pilot_{model_name}_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*70}")
    print(f"Results saved to: {filename}")
    print(f"{'='*70}\n")


def main():
    """Run scaled pilot experiment."""
    print("\n" + "="*70)
    print("COMPUTATIONAL SELF-CONSTRUCTION FRAMEWORK")
    print("Scaled Pilot Experiment: n=20 per condition")
    print("="*70 + "\n")
    
    # Load prompts
    prompts = load_prompts()
    print(f"Loaded {len(prompts)} prompts\n")
    
    if len(prompts) < 20:
        print("ERROR: Need at least 20 prompts for scaled pilot")
        return
    
    # Initialize model
    print("Initializing Claude model...")
    model = ClaudeModel()
    print("Model ready!\n")
    
    # Run all 4 conditions
    all_results = []
    
    for condition in [BASELINE, MEMORY_ONLY, FULL_BASIC, FULL_META]:
        condition_results = run_condition(
            model=model,
            condition=condition,
            prompts=prompts,
            n_queries=20,  # Scaled sample size
            max_tokens=200  # Controlled length
        )
        all_results.extend(condition_results)
    
    # Save
    save_results(all_results, model.name)
    
    print("\n🎉 SCALED PILOT COMPLETE! 🎉\n")
    print("Results:")
    print(f"- Total queries: {len(all_results)}")
    print(f"- Conditions tested: 4 (Baseline, Memory-Only, Full-Basic, Full-Meta)")
    print(f"- Queries per condition: 20")
    print(f"- Response length: Controlled (max_tokens=200)")
    print("\nNext steps:")
    print("1. Run analysis: python3 scripts/analyze_pilot.py data/raw/scaled_pilot_*.json")
    print("2. Run statistics: python3 scripts/statistical_tests.py data/raw/scaled_pilot_*.json")
    print("3. If results replicate → proceed to cross-architecture study")
    print("4. If results don't replicate → revise methodology\n")


if __name__ == "__main__":
    main()