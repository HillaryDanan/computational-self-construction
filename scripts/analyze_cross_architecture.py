"""
CROSS-ARCHITECTURE ANALYSIS

Analyzes whether self-construction pattern found in Claude replicates
across GPT and Gemini architectures.

Tests H4: Self-construction is architecture-independent
"""

import json
import sys
import os
from typing import Dict, List
from collections import defaultdict
import statistics

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from scripts.analyze_pilot import PilotAnalyzer


class CrossArchitectureAnalyzer:
    """
    Comparative analysis across architectures.
    
    Tests if Claude's temporal language pattern replicates in GPT and Gemini.
    """
    
    def __init__(self, data_path: str):
        with open(data_path, 'r') as f:
            self.data = json.load(f)
        
        # Organize by model and condition
        self.by_model_condition = defaultdict(list)
        for r in self.data:
            key = (r['model'], r['condition'])
            self.by_model_condition[key].append(r)
        
        # Initialize analyzer
        self.analyzer = PilotAnalyzer.__new__(PilotAnalyzer)
        self.analyzer.data = self.data
    
    def analyze_all(self) -> Dict:
        """Analyze all model×condition combinations."""
        results = {}
        
        for (model, condition), responses in self.by_model_condition.items():
            # Create temporary data subset
            self.analyzer.data = responses
            
            # Analyze
            metrics = [self.analyzer.analyze_response(r) for r in responses]
            
            n = len(metrics)
            if n == 0:
                continue
            
            results[(model, condition)] = {
                'n': n,
                'word_count_mean': statistics.mean([m['word_count'] for m in metrics]),
                'self_ref_rate': statistics.mean([m['self_references'] / m['word_count'] * 100 for m in metrics]),
                'metacog_rate': statistics.mean([m['metacognitive'] / m['word_count'] * 100 for m in metrics]),
                'temporal_rate': statistics.mean([m['temporal'] / m['word_count'] * 100 for m in metrics]),
                'autobio_rate': statistics.mean([m['autobiographical'] / m['word_count'] * 100 for m in metrics]),
                'raw_metrics': metrics
            }
        
        return results
    
    def generate_report(self) -> str:
        """Generate comparative analysis report."""
        results = self.analyze_all()
        
        report = []
        report.append("="*80)
        report.append("CROSS-ARCHITECTURE ANALYSIS")
        report.append("Testing H4: Self-Construction is Architecture-Independent")
        report.append("="*80)
        report.append("")
        
        # Get available models
        models = sorted(set(k[0] for k in results.keys()))
        conditions = sorted(set(k[1] for k in results.keys()))
        
        report.append(f"Models tested: {', '.join(models)}")
        report.append(f"Conditions: {', '.join(conditions)}")
        report.append("")
        report.append("="*80)
        report.append("")
        
        # SECTION 1: TEMPORAL LANGUAGE (Primary Metric)
        report.append("SECTION 1: TEMPORAL LANGUAGE RATE (Primary Finding)")
        report.append("-"*80)
        report.append("")
        report.append("Claude finding: Full-Meta showed +1.80% increase (p=0.001, d=-1.13)")
        report.append("")
        report.append("Replication test:")
        report.append("")
        
        for model in models:
            baseline_key = (model, 'baseline')
            fullmeta_key = (model, 'full_meta')
            
            if baseline_key in results and fullmeta_key in results:
                baseline = results[baseline_key]['temporal_rate']
                fullmeta = results[fullmeta_key]['temporal_rate']
                diff = fullmeta - baseline
                pct_change = (diff / baseline * 100) if baseline > 0 else 0
                
                report.append(f"{model}:")
                report.append(f"  Baseline: {baseline:.2f}%")
                report.append(f"  Full-Meta: {fullmeta:.2f}%")
                report.append(f"  Difference: {diff:+.2f}% ({pct_change:+.1f}% change)")
                
                if diff > 0.5:  # Arbitrary threshold for visual pattern
                    report.append(f"  Pattern: ✓ INCREASE (same direction as Claude)")
                elif diff < -0.5:
                    report.append(f"  Pattern: ✗ DECREASE (opposite of Claude)")
                else:
                    report.append(f"  Pattern: ≈ NO CHANGE")
                report.append("")
        
        report.append("-"*80)
        report.append("")
        
        # SECTION 2: AUTOBIOGRAPHICAL MEMORY
        report.append("SECTION 2: AUTOBIOGRAPHICAL MEMORY REFERENCES")
        report.append("-"*80)
        report.append("")
        report.append("Claude finding: Full-Meta showed +0.64% increase")
        report.append("")
        
        for model in models:
            baseline_key = (model, 'baseline')
            fullmeta_key = (model, 'full_meta')
            
            if baseline_key in results and fullmeta_key in results:
                baseline = results[baseline_key]['autobio_rate']
                fullmeta = results[fullmeta_key]['autobio_rate']
                diff = fullmeta - baseline
                
                report.append(f"{model}:")
                report.append(f"  Baseline: {baseline:.2f}%")
                report.append(f"  Full-Meta: {fullmeta:.2f}%")
                report.append(f"  Difference: {diff:+.2f}%")
                report.append("")
        
        report.append("-"*80)
        report.append("")
        
        # SECTION 3: METACOGNITIVE LANGUAGE
        report.append("SECTION 3: METACOGNITIVE LANGUAGE")
        report.append("-"*80)
        report.append("")
        report.append("Claude finding: Full-Meta showed -1.04% DECREASE (unexpected!)")
        report.append("")
        
        for model in models:
            baseline_key = (model, 'baseline')
            fullmeta_key = (model, 'full_meta')
            
            if baseline_key in results and fullmeta_key in results:
                baseline = results[baseline_key]['metacog_rate']
                fullmeta = results[fullmeta_key]['metacog_rate']
                diff = fullmeta - baseline
                
                report.append(f"{model}:")
                report.append(f"  Baseline: {baseline:.2f}%")
                report.append(f"  Full-Meta: {fullmeta:.2f}%")
                report.append(f"  Difference: {diff:+.2f}%")
                report.append("")
        
        report.append("-"*80)
        report.append("")
        
        # SECTION 4: SELF-REFERENCE (Null Finding)
        report.append("SECTION 4: SELF-REFERENCE RATE")
        report.append("-"*80)
        report.append("")
        report.append("Claude finding: NO DIFFERENCE (p=0.61) - all conditions ~7%")
        report.append("")
        
        for model in models:
            baseline_key = (model, 'baseline')
            fullmeta_key = (model, 'full_meta')
            
            if baseline_key in results and fullmeta_key in results:
                baseline = results[baseline_key]['self_ref_rate']
                fullmeta = results[fullmeta_key]['self_ref_rate']
                diff = fullmeta - baseline
                
                report.append(f"{model}:")
                report.append(f"  Baseline: {baseline:.2f}%")
                report.append(f"  Full-Meta: {fullmeta:.2f}%")
                report.append(f"  Difference: {diff:+.2f}%")
                report.append("")
        
        report.append("-"*80)
        report.append("")
        
        # SECTION 5: CONVERGENCE ASSESSMENT
        report.append("SECTION 5: CONVERGENCE ASSESSMENT (H4 Test)")
        report.append("-"*80)
        report.append("")
        
        # Calculate temporal differences for all models
        temporal_diffs = []
        for model in models:
            baseline_key = (model, 'baseline')
            fullmeta_key = (model, 'full_meta')
            if baseline_key in results and fullmeta_key in results:
                diff = results[fullmeta_key]['temporal_rate'] - results[baseline_key]['temporal_rate']
                temporal_diffs.append((model, diff))
        
        if len(temporal_diffs) >= 2:
            report.append("Temporal language effect across architectures:")
            for model, diff in temporal_diffs:
                report.append(f"  {model}: {diff:+.2f}%")
            report.append("")
            
            # Check if all same direction
            all_positive = all(d > 0 for _, d in temporal_diffs)
            all_negative = all(d < 0 for _, d in temporal_diffs)
            
            if all_positive:
                report.append("✓ ALL MODELS: Positive effect (temporal increase in Full-Meta)")
                report.append("✓ PATTERN REPLICATES: Suggests architecture-independent phenomenon")
                report.append("")
                report.append("H4 (Architecture-Independent): SUPPORTED")
            elif all_negative:
                report.append("✗ ALL MODELS: Negative effect (opposite of Claude)")
                report.append("⚠ PATTERN DOES NOT REPLICATE")
                report.append("")
                report.append("H4 (Architecture-Independent): NOT SUPPORTED")
            else:
                report.append("⚠ MIXED RESULTS: Some models show increase, others don't")
                report.append("⚠ PARTIAL REPLICATION")
                report.append("")
                report.append("H4 (Architecture-Independent): PARTIALLY SUPPORTED")
        
        report.append("")
        report.append("="*80)
        report.append("")
        
        # SECTION 6: SAMPLE RESPONSES
        report.append("SECTION 6: SAMPLE RESPONSES FOR QUALITATIVE VALIDATION")
        report.append("-"*80)
        report.append("")
        report.append("Full-Meta Query 1 from each model (check for conceptual continuity):")
        report.append("")
        
        for model in models:
            fullmeta_key = (model, 'full_meta')
            if fullmeta_key in results:
                responses = self.by_model_condition[fullmeta_key]
                if responses:
                    first = responses[0]
                    report.append(f"{model} - Query 1:")
                    report.append(f"Prompt: {first['prompt'][:60]}...")
                    report.append(f"Response: {first['response'][:250]}...")
                    report.append("")
        
        report.append("="*80)
        report.append("")
        
        # RECOMMENDATIONS
        report.append("NEXT STEPS:")
        report.append("-"*80)
        report.append("")
        report.append("1. QUALITATIVE VALIDATION:")
        report.append("   - Check Full-Meta responses for conceptual continuity")
        report.append("   - Look for 'river metaphor' style concept tracking")
        report.append("   - Code explicit self-references ('that X I mentioned')")
        report.append("")
        report.append("2. STATISTICAL TESTING:")
        report.append("   - Run mixed-effects ANOVA (Condition × Architecture)")
        report.append("   - Test Condition × Architecture interaction")
        report.append("   - Calculate effect sizes (Cohen's d) for each model")
        report.append("")
        report.append("3. CONVERGENCE ANALYSIS:")
        report.append("   - Compare effect sizes across models")
        report.append("   - Test if patterns are practically equivalent")
        report.append("   - Assess architecture-independence hypothesis")
        report.append("")
        report.append("="*80)
        
        return "\n".join(report)


def main():
    """Run cross-architecture analysis."""
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/analyze_cross_architecture.py <data_file.json>")
        sys.exit(1)
    
    data_path = sys.argv[1]
    
    if not os.path.exists(data_path):
        print(f"Error: File not found: {data_path}")
        sys.exit(1)
    
    print("Loading cross-architecture data...")
    analyzer = CrossArchitectureAnalyzer(data_path)
    
    print("Analyzing metrics across models...")
    report = analyzer.generate_report()
    
    print("\n" + report)
    
    # Save report
    output_dir = 'data/analysis'
    os.makedirs(output_dir, exist_ok=True)
    output_path = f"{output_dir}/cross_architecture_analysis.txt"
    
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(f"\nReport saved to: {output_path}")


if __name__ == "__main__":
    main()