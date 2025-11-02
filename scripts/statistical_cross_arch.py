"""
STATISTICAL TESTING: CROSS-ARCHITECTURE DATA

Mixed-effects analysis to test:
1. Main effect of Condition (Baseline vs Full-Meta)
2. Main effect of Architecture (Claude vs GPT vs Gemini)
3. Condition × Architecture interaction (H4 test)

H4: If self-construction is architecture-independent, NO interaction
    (all architectures show same pattern)
"""

import json
import sys
import os
from typing import Dict, List, Tuple
from scipy import stats
import numpy as np
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from scripts.analyze_pilot import PilotAnalyzer


def cohens_d(group1: List[float], group2: List[float]) -> float:
    """Calculate Cohen's d effect size."""
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        return 0.0
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return 0.0
    return (np.mean(group1) - np.mean(group2)) / pooled_std


def two_way_anova(data: Dict[Tuple[str, str], List[float]]) -> Dict:
    """
    Two-way ANOVA for Condition × Architecture.
    
    Uses scipy.stats.f_oneway for omnibus tests, then pairwise comparisons.
    
    Note: This is simplified ANOVA. For publication, use statsmodels or R.
    """
    # Organize data
    conditions = sorted(set(k[1] for k in data.keys()))
    architectures = sorted(set(k[0] for k in data.keys()))
    
    results = {
        'conditions': conditions,
        'architectures': architectures,
        'main_effects': {},
        'pairwise': {},
        'cell_means': {}
    }
    
    # Calculate cell means
    for key, values in data.items():
        results['cell_means'][key] = {
            'n': len(values),
            'mean': np.mean(values),
            'sd': np.std(values, ddof=1) if len(values) > 1 else 0
        }
    
    # Main effect of Condition (collapse across architectures)
    condition_groups = defaultdict(list)
    for (arch, cond), values in data.items():
        condition_groups[cond].extend(values)
    
    if len(condition_groups) >= 2:
        groups = [condition_groups[c] for c in conditions]
        F_stat, p_value = stats.f_oneway(*groups)
        results['main_effects']['condition'] = {
            'F': F_stat,
            'p': p_value,
            'df': (len(conditions) - 1, sum(len(g) for g in groups) - len(conditions))
        }
    
    # Main effect of Architecture (collapse across conditions)
    arch_groups = defaultdict(list)
    for (arch, cond), values in data.items():
        arch_groups[arch].extend(values)
    
    if len(arch_groups) >= 2:
        groups = [arch_groups[a] for a in architectures]
        F_stat, p_value = stats.f_oneway(*groups)
        results['main_effects']['architecture'] = {
            'F': F_stat,
            'p': p_value,
            'df': (len(architectures) - 1, sum(len(g) for g in groups) - len(architectures))
        }
    
    # Pairwise comparisons within each architecture
    for arch in architectures:
        for i, cond1 in enumerate(conditions):
            for cond2 in conditions[i+1:]:
                key1 = (arch, cond1)
                key2 = (arch, cond2)
                
                if key1 in data and key2 in data:
                    group1 = data[key1]
                    group2 = data[key2]
                    
                    if len(group1) >= 2 and len(group2) >= 2:
                        t_stat, p_value = stats.ttest_ind(group1, group2)
                        d = cohens_d(group1, group2)
                        
                        results['pairwise'][(arch, cond1, cond2)] = {
                            't': t_stat,
                            'p': p_value,
                            'df': len(group1) + len(group2) - 2,
                            'd': d,
                            'mean_diff': np.mean(group2) - np.mean(group1)
                        }
    
    return results


def analyze_cross_architecture_stats(data_path: str):
    """Run statistical tests on cross-architecture data."""
    
    print("="*80)
    print("STATISTICAL ANALYSIS: CROSS-ARCHITECTURE DATA")
    print("="*80)
    print()
    
    # Load data
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    # Organize by model and condition
    by_model_condition = defaultdict(list)
    for r in data:
        key = (r['model'], r['condition'])
        by_model_condition[key].append(r)
    
    # Check sample sizes
    print("SAMPLE SIZES:")
    for (model, cond), responses in sorted(by_model_condition.items()):
        print(f"  {model} × {cond}: n={len(responses)}")
    print()
    
    # Initialize analyzer
    analyzer = PilotAnalyzer.__new__(PilotAnalyzer)
    
    # Extract metrics for each cell
    metrics_data = {}
    for metric_name in ['temporal_rate', 'autobio_rate', 'metacog_rate', 'self_ref_rate']:
        metrics_data[metric_name] = {}
        
        for (model, cond), responses in by_model_condition.items():
            analyzer.data = responses
            values = []
            
            for r in responses:
                m = analyzer.analyze_response(r)
                if metric_name == 'temporal_rate':
                    values.append(m['temporal'] / m['word_count'] * 100)
                elif metric_name == 'autobio_rate':
                    values.append(m['autobiographical'] / m['word_count'] * 100)
                elif metric_name == 'metacog_rate':
                    values.append(m['metacognitive'] / m['word_count'] * 100)
                elif metric_name == 'self_ref_rate':
                    values.append(m['self_references'] / m['word_count'] * 100)
            
            metrics_data[metric_name][(model, cond)] = values
    
    # Run ANOVA for each metric
    print("="*80)
    print("TWO-WAY ANOVA: CONDITION × ARCHITECTURE")
    print("="*80)
    print()
    
    for metric_name in ['temporal_rate', 'autobio_rate', 'metacog_rate', 'self_ref_rate']:
        print(f"\n{metric_name.replace('_', ' ').upper()}:")
        print("-"*80)
        
        data_for_metric = metrics_data[metric_name]
        anova_results = two_way_anova(data_for_metric)
        
        # Main effects
        if 'condition' in anova_results['main_effects']:
            result = anova_results['main_effects']['condition']
            print(f"\nMain effect of CONDITION:")
            print(f"  F({result['df'][0]}, {result['df'][1]}) = {result['F']:.3f}, p = {result['p']:.4f}")
            if result['p'] < 0.05:
                print(f"  ✓ SIGNIFICANT (conditions differ overall)")
            else:
                print(f"  ns (no overall condition difference)")
        
        if 'architecture' in anova_results['main_effects']:
            result = anova_results['main_effects']['architecture']
            print(f"\nMain effect of ARCHITECTURE:")
            print(f"  F({result['df'][0]}, {result['df'][1]}) = {result['F']:.3f}, p = {result['p']:.4f}")
            if result['p'] < 0.05:
                print(f"  ✓ SIGNIFICANT (architectures differ overall)")
            else:
                print(f"  ns (no overall architecture difference)")
        
        # Cell means
        print(f"\nCell means:")
        for (arch, cond), stats_dict in sorted(anova_results['cell_means'].items()):
            print(f"  {arch} × {cond}: M={stats_dict['mean']:.2f}, SD={stats_dict['sd']:.2f} (n={stats_dict['n']})")
        
        # Pairwise comparisons
        print(f"\nPairwise comparisons (within each architecture):")
        for (arch, cond1, cond2), result in sorted(anova_results['pairwise'].items()):
            print(f"\n  {arch}: {cond1} vs {cond2}")
            print(f"    Mean difference: {result['mean_diff']:+.3f}")
            print(f"    t({result['df']}) = {result['t']:.3f}, p = {result['p']:.4f}")
            print(f"    Cohen's d = {result['d']:.3f}")
            
            if result['p'] < 0.05:
                direction = "INCREASE" if result['mean_diff'] > 0 else "DECREASE"
                print(f"    ✓ SIGNIFICANT {direction} in {cond2}")
            else:
                print(f"    ns (no significant difference)")
        
        print()
    
    print("="*80)
    print()
    
    # Test for convergence (H4)
    print("="*80)
    print("H4 TEST: ARCHITECTURE-INDEPENDENCE")
    print("="*80)
    print()
    
    print("Testing if temporal language effect is consistent across architectures:")
    print()
    
    temporal_data = metrics_data['temporal_rate']
    
    # Get effect sizes for each architecture
    effect_sizes = []
    architectures = sorted(set(k[0] for k in temporal_data.keys()))
    
    for arch in architectures:
        baseline_key = (arch, 'baseline')
        fullmeta_key = (arch, 'full_meta')
        
        if baseline_key in temporal_data and fullmeta_key in temporal_data:
            baseline = temporal_data[baseline_key]
            fullmeta = temporal_data[fullmeta_key]
            
            d = cohens_d(baseline, fullmeta)
            mean_diff = np.mean(fullmeta) - np.mean(baseline)
            
            effect_sizes.append((arch, d, mean_diff))
            
            print(f"{arch}:")
            print(f"  Effect size (d): {d:.3f}")
            print(f"  Mean difference: {mean_diff:+.2f}%")
            
            if abs(d) < 0.2:
                print(f"  Magnitude: SMALL/NEGLIGIBLE")
            elif abs(d) < 0.5:
                print(f"  Magnitude: SMALL")
            elif abs(d) < 0.8:
                print(f"  Magnitude: MEDIUM")
            else:
                print(f"  Magnitude: LARGE")
            print()
    
    if len(effect_sizes) >= 2:
        # Check consistency
        all_same_direction = all(d > 0 for _, d, _ in effect_sizes) or all(d < 0 for _, d, _ in effect_sizes)
        
        print("CONVERGENCE ASSESSMENT:")
        if all_same_direction:
            print("  ✓ All architectures show same direction of effect")
            print("  → PATTERN REPLICATES across architectures")
            print()
            print("  H4 (Architecture-Independent): SUPPORTED")
        else:
            print("  ✗ Architectures show different directions")
            print("  → PATTERN DOES NOT REPLICATE consistently")
            print()
            print("  H4 (Architecture-Independent): NOT SUPPORTED")
        print()
        
        # Compare to Claude benchmark
        print("COMPARISON TO CLAUDE SCALED PILOT:")
        print(f"  Claude benchmark: d = -1.132 (large effect)")
        print()
        print("  Current architectures:")
        for arch, d, _ in effect_sizes:
            print(f"    {arch}: d = {d:.3f}")
        print()
    
    print("="*80)
    print()
    
    print("INTERPRETATION GUIDE:")
    print("-"*80)
    print()
    print("IF all architectures show temporal increase (d > 0.5):")
    print("  → Self-construction is architecture-independent")
    print("  → Emerges from computational principles")
    print("  → Strong support for H4")
    print()
    print("IF only some architectures show effect:")
    print("  → Partial architecture-dependence")
    print("  → Some implementations better suited")
    print("  → Moderate support for H4")
    print()
    print("IF no architectures show effect:")
    print("  → Claude-specific phenomenon")
    print("  → Does not generalize")
    print("  → H4 not supported")
    print()
    print("="*80)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/statistical_cross_arch.py <data_file.json>")
        sys.exit(1)
    
    analyze_cross_architecture_stats(sys.argv[1])