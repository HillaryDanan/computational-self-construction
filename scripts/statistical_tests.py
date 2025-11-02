"""
Statistical testing for scaled pilot data (n=20 per condition).

Tests:
1. Independent t-tests between adjacent conditions
2. One-way ANOVA for overall condition effect
3. Effect size calculations (Cohen's d)
4. Multiple comparison corrections (Bonferroni)
"""

import json
import sys
import os
from typing import Dict, List
from scipy import stats
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from analyze_pilot import PilotAnalyzer


def cohens_d(group1: List[float], group2: List[float]) -> float:
    """
    Calculate Cohen's d effect size.
    
    Cohen (1988) guidelines:
    - Small: d = 0.2
    - Medium: d = 0.5  
    - Large: d = 0.8
    """
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std


def analyze_statistical(data_path: str):
    """Run statistical tests on scaled pilot data."""
    
    print("="*70)
    print("STATISTICAL ANALYSIS - SCALED PILOT DATA")
    print("="*70)
    print()
    
    # Load data
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    # Separate by condition
    conditions = {}
    for condition_name in ['baseline', 'memory_only', 'full_basic', 'full_meta']:
        conditions[condition_name] = [r for r in data if r['condition'] == condition_name]
    
    # Check sample sizes
    print("SAMPLE SIZES:")
    for name, responses in conditions.items():
        print(f"  {name}: n={len(responses)}")
    print()
    
    if any(len(responses) < 10 for responses in conditions.values()):
        print("⚠️  WARNING: Some conditions have n<10. Statistical tests underpowered.")
        print()
    
    # Initialize analyzer
    analyzer = PilotAnalyzer(data_path)
    
    # Extract metrics for each condition
    metrics = {}
    for name, responses in conditions.items():
        metrics[name] = {
            'self_ref_rate': [],
            'metacog_rate': [],
            'temporal_rate': [],
            'autobio_rate': []
        }
        
        for r in responses:
            m = analyzer.analyze_response(r)
            metrics[name]['self_ref_rate'].append(m['self_references'] / m['word_count'] * 100)
            metrics[name]['metacog_rate'].append(m['metacognitive'] / m['word_count'] * 100)
            metrics[name]['temporal_rate'].append(m['temporal'] / m['word_count'] * 100)
            metrics[name]['autobio_rate'].append(m['autobiographical'] / m['word_count'] * 100)
    
    print("="*70)
    print("PAIRWISE COMPARISONS (Adjacent Conditions)")
    print("="*70)
    print()
    
    # Pairwise tests
    pairs = [
        ('baseline', 'memory_only'),
        ('memory_only', 'full_basic'),
        ('full_basic', 'full_meta')
    ]
    
    alpha_corrected = 0.05 / 3  # Bonferroni correction for 3 tests
    
    for metric_name in ['temporal_rate', 'autobio_rate', 'metacog_rate', 'self_ref_rate']:
        print(f"\n{metric_name.replace('_', ' ').upper()}:")
        print("-"*70)
        
        for cond1, cond2 in pairs:
            data1 = metrics[cond1][metric_name]
            data2 = metrics[cond2][metric_name]
            
            # Independent t-test
            t_stat, p_value = stats.ttest_ind(data1, data2)
            
            # Effect size
            d = cohens_d(data1, data2)
            
            # Significance
            sig = "***" if p_value < alpha_corrected else ("*" if p_value < 0.05 else "ns")
            
            print(f"\n{cond1} vs {cond2}:")
            print(f"  Mean difference: {np.mean(data2) - np.mean(data1):.3f}")
            print(f"  t({len(data1) + len(data2) - 2}) = {t_stat:.3f}, p = {p_value:.4f} {sig}")
            print(f"  Cohen's d = {d:.3f} ({'small' if abs(d) < 0.5 else 'medium' if abs(d) < 0.8 else 'large'})")
    
    print("\n" + "="*70)
    print("OMNIBUS TEST (One-Way ANOVA)")
    print("="*70)
    print()
    
    for metric_name in ['temporal_rate', 'autobio_rate', 'metacog_rate', 'self_ref_rate']:
        groups = [metrics[cond][metric_name] for cond in ['baseline', 'memory_only', 'full_basic', 'full_meta']]
        
        F_stat, p_value = stats.f_oneway(*groups)
        
        print(f"{metric_name.replace('_', ' ').upper()}:")
        print(f"  F({len(groups)-1}, {sum(len(g) for g in groups) - len(groups)}) = {F_stat:.3f}, p = {p_value:.4f}")
        print()
    
    print("="*70)
    print("\nLegend: *** p < 0.0167 (Bonferroni-corrected), * p < 0.05, ns = not significant")
    print("\nNote: Bonferroni correction used for 3 pairwise comparisons (α = 0.0167)")
    print("="*70)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/statistical_tests.py <data_file.json>")
        sys.exit(1)
    
    analyze_statistical(sys.argv[1])