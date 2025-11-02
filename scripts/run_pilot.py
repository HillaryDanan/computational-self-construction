"""
Pilot experiment runner: Tests basic functionality with small sample.

This is a minimal viable experiment to validate methodology before
scaling to full data collection.
"""

import json
import os
from datetime import datetime
from typing import Dict, List
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.conditions import BASELINE, FULL_META
from src.core.memory import MemoryManager
from src.models.claude import ClaudeModel


def load_prompts() -> List[str]:
    """Load baseline prompts from JSON file."""
    with open('src/prompts/baseline_prompts.json', 'r') as f:
        data = json.load(f)
    return data['prompts']


def run_condition(
    model, 
    condition, 
    prompts: List[str],
    n_queries: int = 5
) -> List[Dict]:
    """
    Run experiment for one condition.
    
    Args:
        model: Language model instance
        condition: Experimental condition
        prompts: List of prompts to use
        n_queries: Number of queries to run
        
    Returns:
        List of results (query, response, metadata)
    """
    print(f"\n{'='*60}")
    print(f"Running condition: {condition}")
    print(f"{'='*60}\n")
    
    # Initialize memory manager
    memory = MemoryManager(persist=condition.memory_persistence)
    
    results = []
    
    # Add initial prompt if condition requires self-framing
    if condition.self_framing:
        config_path = 'src/prompts/condition_configs.json'
        with open(config_path, 'r') as f:
            configs = json.load(f)
        initial_prompt = configs[condition.name]['initial_prompt']
        
        print(f"[Initial framing]: {initial_prompt}\n")
        # Send initial prompt (don't count as query)
        model.query(initial_prompt, context=memory.get_context())
        memory.add_exchange(initial_prompt, "[Acknowledged]")
    
    # Run queries
    for i in range(n_queries):
        prompt = prompts[i % len(prompts)]
        
        # Add temporal marker if condition requires it
        if condition.temporal_markers and i > 0:
            prompt = f"[This is query {i+1}] {prompt}"
        
        print(f"Query {i+1}/{n_queries}: {prompt}")
        
        # Get response
        context = memory.get_context() if condition.memory_persistence else None
        response = model.query(prompt, context=context)
        
        print(f"Response: {response[:200]}{'...' if len(response) > 200 else ''}\n")
        
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
    filename = f"{output_dir}/pilot_{model_name}_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Results saved to: {filename}")
    print(f"{'='*60}\n")


def main():
    """Run pilot experiment."""
    print("\n" + "="*60)
    print("COMPUTATIONAL SELF-CONSTRUCTION FRAMEWORK")
    print("Pilot Experiment")
    print("="*60 + "\n")
    
    # Load prompts
    prompts = load_prompts()
    print(f"Loaded {len(prompts)} prompts\n")
    
    # Initialize model (just Claude for pilot)
    print("Initializing Claude model...")
    model = ClaudeModel()
    print("Model ready!\n")
    
    # Run baseline condition
    baseline_results = run_condition(
        model=model,
        condition=BASELINE,
        prompts=prompts,
        n_queries=5
    )
    
    # Run full-meta condition
    fullmeta_results = run_condition(
        model=model,
        condition=FULL_META,
        prompts=prompts,
        n_queries=5
    )
    
    # Combine and save
    all_results = baseline_results + fullmeta_results
    save_results(all_results, model.name)
    
    print("\n🎉 PILOT EXPERIMENT COMPLETE! 🎉\n")
    print("Next steps:")
    print("1. Examine results in data/raw/")
    print("2. Check for self-reference patterns")
    print("3. If methodology works, scale to full experiment\n")


if __name__ == "__main__":
    main()