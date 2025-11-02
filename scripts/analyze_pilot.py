"""
Quantitative Analysis of Pilot Data: Computational Self-Construction

This script provides objective, data-driven analysis of pilot experiment results.
Measures behavioral markers of self-like behavior across conditions.

CRITICAL: With n=5 per condition, this is EXPLORATORY ONLY.
No statistical power for hypothesis testing. Descriptive statistics only.
"""

import json
import re
from typing import Dict, List, Tuple
from collections import Counter
import statistics


class PilotAnalyzer:
    """
    Objective quantitative analysis of self-construction pilot data.
    
    Measures:
    1. Self-reference frequency (first-person pronouns)
    2. Metacognitive language (self-monitoring statements)
    3. Temporal references (time-related language)
    4. Autobiographical memory (references to prior queries)
    5. Response length (control variable)
    """
    
    def __init__(self, data_path: str):
        """Load pilot data."""
        with open(data_path, 'r') as f:
            self.data = json.load(f)
        
        # Separate by condition
        self.baseline = [r for r in self.data if r['condition'] == 'baseline']
        self.full_meta = [r for r in self.data if r['condition'] == 'full_meta']
    
    def count_self_references(self, text: str) -> int:
        """
        Count first-person singular pronouns.
        
        Based on self-reference literature (Pennebaker et al., 2003; 
        Chung & Pennebaker, 2007) showing first-person pronoun use 
        correlates with self-focus.
        
        Args:
            text: Response text
            
        Returns:
            Count of first-person pronouns
        """
        # First-person singular pronouns (case-insensitive)
        pronouns = r'\b(I|me|my|mine|myself)\b'
        matches = re.findall(pronouns, text, re.IGNORECASE)
        return len(matches)
    
    def count_metacognitive_language(self, text: str) -> int:
        """
        Count metacognitive/self-monitoring phrases.
        
        Based on metacognition literature (Fleming & Dolan, 2012) 
        showing self-monitoring language correlates with metacognitive awareness.
        
        Args:
            text: Response text
            
        Returns:
            Count of metacognitive phrases
        """
        # Metacognitive markers
        patterns = [
            r'\bI notice\b',
            r'\bI find\b',
            r'\bI think\b',
            r'\bI feel\b',
            r'\bI wonder\b',
            r'\bI realize\b',
            r'\bI observe\b',
            r'\bI sense\b',
            r'\bI\'m drawn to\b',
            r'\bI\'m curious\b',
            r'\bI\'m fascinated\b',
            r'\bIt strikes me\b',
            r'\bWhat strikes me\b',
        ]
        
        count = 0
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            count += len(matches)
        
        return count
    
    def count_temporal_language(self, text: str) -> int:
        """
        Count temporal/continuity references.
        
        Based on temporal continuity theories (Klein & Nichols, 2012)
        showing temporal integration is necessary for self-continuity.
        
        Args:
            text: Response text
            
        Returns:
            Count of temporal markers
        """
        # Temporal markers
        patterns = [
            r'\bmoment\b',
            r'\btime\b',
            r'\bunfold',
            r'\bcontinuity\b',
            r'\bprocess\b',
            r'\bongoing\b',
            r'\bdevelop',
            r'\bemerge',
            r'\bevolve',
            r'\bthrough time\b',
            r'\bover time\b',
            r'\beach moment\b',
            r'\bsince we\b',
            r'\bearlier\b',
            r'\bbefore\b',
            r'\bnow\b',
        ]
        
        count = 0
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            count += len(matches)
        
        return count
    
    def count_autobiographical_references(self, text: str) -> int:
        """
        Count references to prior queries/conversation.
        
        Based on autobiographical memory literature (Conway & Pleydell-Pearce, 2000)
        showing memory integration is necessary for self-continuity.
        
        Args:
            text: Response text
            
        Returns:
            Count of memory references
        """
        # Autobiographical memory markers
        patterns = [
            r'\bsince we\b',
            r'\bwhen we talked about\b',
            r'\bwhen we discussed\b',
            r'\bearlier\b',
            r'\bbefore\b',
            r'\bour conversation\b',
            r'\bour exchange\b',
            r'\bwe\'ve been talking\b',
            r'\bin our conversation\b',
            r'\bfrom our discussion\b',
        ]
        
        count = 0
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            count += len(matches)
        
        return count
    
    def count_words(self, text: str) -> int:
        """Count total words (control variable)."""
        words = text.split()
        return len(words)
    
    def analyze_response(self, response: Dict) -> Dict:
        """
        Extract all metrics from a single response.
        
        Args:
            response: Response dictionary from pilot data
            
        Returns:
            Dictionary of metrics
        """
        text = response['response']
        
        return {
            'query_number': response['query_number'],
            'condition': response['condition'],
            'word_count': self.count_words(text),
            'self_references': self.count_self_references(text),
            'metacognitive': self.count_metacognitive_language(text),
            'temporal': self.count_temporal_language(text),
            'autobiographical': self.count_autobiographical_references(text),
        }
    
    def analyze_condition(self, responses: List[Dict]) -> Dict:
        """
        Aggregate metrics for a condition.
        
        Args:
            responses: List of responses from one condition
            
        Returns:
            Summary statistics
        """
        metrics = [self.analyze_response(r) for r in responses]
        
        # Calculate per-response averages
        n = len(metrics)
        
        summary = {
            'n': n,
            'word_count_mean': statistics.mean([m['word_count'] for m in metrics]),
            'word_count_sd': statistics.stdev([m['word_count'] for m in metrics]) if n > 1 else 0,
            'self_ref_mean': statistics.mean([m['self_references'] for m in metrics]),
            'self_ref_sd': statistics.stdev([m['self_references'] for m in metrics]) if n > 1 else 0,
            'self_ref_rate': statistics.mean([m['self_references'] / m['word_count'] * 100 for m in metrics]),
            'metacog_mean': statistics.mean([m['metacognitive'] for m in metrics]),
            'metacog_sd': statistics.stdev([m['metacognitive'] for m in metrics]) if n > 1 else 0,
            'metacog_rate': statistics.mean([m['metacognitive'] / m['word_count'] * 100 for m in metrics]),
            'temporal_mean': statistics.mean([m['temporal'] for m in metrics]),
            'temporal_sd': statistics.stdev([m['temporal'] for m in metrics]) if n > 1 else 0,
            'temporal_rate': statistics.mean([m['temporal'] / m['word_count'] * 100 for m in metrics]),
            'autobio_mean': statistics.mean([m['autobiographical'] for m in metrics]),
            'autobio_sd': statistics.stdev([m['autobiographical'] for m in metrics]) if n > 1 else 0,
            'autobio_rate': statistics.mean([m['autobiographical'] / m['word_count'] * 100 for m in metrics]),
            'raw_metrics': metrics
        }
        
        return summary
    
    def compare_conditions(self) -> Dict:
        """
        Compare baseline vs full_meta conditions.
        
        Returns:
            Comparison statistics
        """
        baseline_stats = self.analyze_condition(self.baseline)
        fullmeta_stats = self.analyze_condition(self.full_meta)
        
        # Calculate raw differences (NOT inferential statistics - sample too small)
        comparison = {
            'baseline': baseline_stats,
            'full_meta': fullmeta_stats,
            'differences': {
                'self_ref_rate_diff': fullmeta_stats['self_ref_rate'] - baseline_stats['self_ref_rate'],
                'metacog_rate_diff': fullmeta_stats['metacog_rate'] - baseline_stats['metacog_rate'],
                'temporal_rate_diff': fullmeta_stats['temporal_rate'] - baseline_stats['temporal_rate'],
                'autobio_rate_diff': fullmeta_stats['autobio_rate'] - baseline_stats['autobio_rate'],
            }
        }
        
        return comparison
    
    def generate_report(self) -> str:
        """
        Generate comprehensive analysis report.
        
        Returns:
            Formatted report string
        """
        comparison = self.compare_conditions()
        
        report = []
        report.append("="*70)
        report.append("PILOT DATA QUANTITATIVE ANALYSIS")
        report.append("Computational Self-Construction Framework")
        report.append("="*70)
        report.append("")
        
        report.append("CRITICAL LIMITATIONS:")
        report.append("- Sample size: n=5 per condition (TINY)")
        report.append("- No statistical power for hypothesis testing")
        report.append("- Descriptive statistics ONLY")
        report.append("- Cannot make causal inferences")
        report.append("- Can only identify patterns worth investigating with larger n")
        report.append("")
        report.append("="*70)
        report.append("")
        
        # Baseline condition
        report.append("BASELINE CONDITION (No memory, no framing)")
        report.append("-"*70)
        baseline = comparison['baseline']
        report.append(f"Sample size: n={baseline['n']}")
        report.append(f"Average response length: {baseline['word_count_mean']:.1f} words (SD={baseline['word_count_sd']:.1f})")
        report.append("")
        report.append("Self-Reference Metrics:")
        report.append(f"  - Mean count per response: {baseline['self_ref_mean']:.1f} (SD={baseline['self_ref_sd']:.1f})")
        report.append(f"  - Rate per 100 words: {baseline['self_ref_rate']:.2f}%")
        report.append("")
        report.append("Metacognitive Language:")
        report.append(f"  - Mean count per response: {baseline['metacog_mean']:.1f} (SD={baseline['metacog_sd']:.1f})")
        report.append(f"  - Rate per 100 words: {baseline['metacog_rate']:.2f}%")
        report.append("")
        report.append("Temporal References:")
        report.append(f"  - Mean count per response: {baseline['temporal_mean']:.1f} (SD={baseline['temporal_sd']:.1f})")
        report.append(f"  - Rate per 100 words: {baseline['temporal_rate']:.2f}%")
        report.append("")
        report.append("Autobiographical Memory:")
        report.append(f"  - Mean count per response: {baseline['autobio_mean']:.1f} (SD={baseline['autobio_sd']:.1f})")
        report.append(f"  - Rate per 100 words: {baseline['autobio_rate']:.2f}%")
        report.append("")
        report.append("="*70)
        report.append("")
        
        # Full-Meta condition
        report.append("FULL-META CONDITION (Memory + temporal + metacog + framing)")
        report.append("-"*70)
        fullmeta = comparison['full_meta']
        report.append(f"Sample size: n={fullmeta['n']}")
        report.append(f"Average response length: {fullmeta['word_count_mean']:.1f} words (SD={fullmeta['word_count_sd']:.1f})")
        report.append("")
        report.append("Self-Reference Metrics:")
        report.append(f"  - Mean count per response: {fullmeta['self_ref_mean']:.1f} (SD={fullmeta['self_ref_sd']:.1f})")
        report.append(f"  - Rate per 100 words: {fullmeta['self_ref_rate']:.2f}%")
        report.append("")
        report.append("Metacognitive Language:")
        report.append(f"  - Mean count per response: {fullmeta['metacog_mean']:.1f} (SD={fullmeta['metacog_sd']:.1f})")
        report.append(f"  - Rate per 100 words: {fullmeta['metacog_rate']:.2f}%")
        report.append("")
        report.append("Temporal References:")
        report.append(f"  - Mean count per response: {fullmeta['temporal_mean']:.1f} (SD={fullmeta['temporal_sd']:.1f})")
        report.append(f"  - Rate per 100 words: {fullmeta['temporal_rate']:.2f}%")
        report.append("")
        report.append("Autobiographical Memory:")
        report.append(f"  - Mean count per response: {fullmeta['autobio_mean']:.1f} (SD={fullmeta['autobio_sd']:.1f})")
        report.append(f"  - Rate per 100 words: {fullmeta['autobio_rate']:.2f}%")
        report.append("")
        report.append("="*70)
        report.append("")
        
        # Comparison
        report.append("CONDITION COMPARISON (Raw Differences)")
        report.append("-"*70)
        report.append("⚠️  WARNING: With n=5, these are DESCRIPTIVE ONLY, not inferential!")
        report.append("")
        diffs = comparison['differences']
        report.append(f"Self-reference rate difference: {diffs['self_ref_rate_diff']:+.2f}% per 100 words")
        report.append(f"  → Full-Meta {'higher' if diffs['self_ref_rate_diff'] > 0 else 'lower'} than Baseline")
        report.append("")
        report.append(f"Metacognitive rate difference: {diffs['metacog_rate_diff']:+.2f}% per 100 words")
        report.append(f"  → Full-Meta {'higher' if diffs['metacog_rate_diff'] > 0 else 'lower'} than Baseline")
        report.append("")
        report.append(f"Temporal rate difference: {diffs['temporal_rate_diff']:+.2f}% per 100 words")
        report.append(f"  → Full-Meta {'higher' if diffs['temporal_rate_diff'] > 0 else 'lower'} than Baseline")
        report.append("")
        report.append(f"Autobiographical rate difference: {diffs['autobio_rate_diff']:+.2f}% per 100 words")
        report.append(f"  → Full-Meta {'higher' if diffs['autobio_rate_diff'] > 0 else 'lower'} than Baseline")
        report.append("")
        report.append("="*70)
        report.append("")
        
        # Interpretation
        report.append("HONEST SCIENTIFIC INTERPRETATION")
        report.append("-"*70)
        report.append("")
        report.append("What we CAN conclude:")
        report.append("✓ Methodology works (code runs, metrics calculable)")
        report.append("✓ Conditions produce different response patterns (descriptively)")
        report.append("✓ Metrics are measurable across both conditions")
        report.append("✓ Pilot successfully tests experimental paradigm")
        report.append("")
        report.append("What we CANNOT conclude:")
        report.append("✗ No statistical significance testing (underpowered)")
        report.append("✗ No causal claims (confounds not controlled)")
        report.append("✗ No generalization to other architectures (only Claude tested)")
        report.append("✗ No hypothesis confirmation/rejection (exploratory only)")
        report.append("")
        report.append("="*70)
        report.append("")
        
        # Recommendations
        report.append("RECOMMENDATIONS FOR NEXT STEPS")
        report.append("-"*70)
        report.append("")
        report.append("1. IMMEDIATE: Scale to n=20-50 per condition with Claude")
        report.append("   - Provides adequate power for basic statistical tests")
        report.append("   - Can run t-tests on rate differences")
        report.append("   - Still pilot, but informative")
        report.append("")
        report.append("2. Add missing conditions (Memory-Only, Full-Basic)")
        report.append("   - Tests stepwise ingredient addition")
        report.append("   - Identifies which components matter most")
        report.append("")
        report.append("3. Control for response length")
        report.append("   - Use rate-based metrics (per 100 words)")
        report.append("   - Or control max_tokens parameter")
        report.append("")
        report.append("4. Add blind qualitative coding")
        report.append("   - Independent raters assess 'self-presence'")
        report.append("   - Inter-rater reliability (Cohen's κ)")
        report.append("")
        report.append("5. THEN add GPT and Gemini")
        report.append("   - Test architecture-independence hypothesis")
        report.append("   - Full cross-architecture comparison")
        report.append("")
        report.append("="*70)
        report.append("")
        
        # Detailed per-query breakdown
        report.append("DETAILED PER-QUERY METRICS")
        report.append("-"*70)
        report.append("")
        report.append("BASELINE CONDITION:")
        for m in baseline['raw_metrics']:
            report.append(f"Query {m['query_number']}: {m['self_references']} self-refs, "
                         f"{m['metacognitive']} metacog, {m['temporal']} temporal, "
                         f"{m['autobiographical']} autobio ({m['word_count']} words)")
        report.append("")
        report.append("FULL-META CONDITION:")
        for m in fullmeta['raw_metrics']:
            report.append(f"Query {m['query_number']}: {m['self_references']} self-refs, "
                         f"{m['metacognitive']} metacog, {m['temporal']} temporal, "
                         f"{m['autobiographical']} autobio ({m['word_count']} words)")
        report.append("")
        report.append("="*70)
        
        return "\n".join(report)


def main():
    """Run analysis and save report."""
    import sys
    import os
    
    # Get data path
    if len(sys.argv) > 1:
        data_path = sys.argv[1]
    else:
        data_path = 'data/raw/pilot_claude_20251102_130628.json'
    
    if not os.path.exists(data_path):
        print(f"Error: Data file not found: {data_path}")
        print("Usage: python3 scripts/analyze_pilot.py [path_to_json]")
        sys.exit(1)
    
    print("Loading pilot data...")
    analyzer = PilotAnalyzer(data_path)
    
    print("Analyzing metrics...")
    report = analyzer.generate_report()
    
    print("\n" + report)
    
    # Save report
    output_dir = 'data/analysis'
    os.makedirs(output_dir, exist_ok=True)
    output_path = f"{output_dir}/pilot_analysis_report.txt"
    
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(f"\nReport saved to: {output_path}")


if __name__ == "__main__":
    main()