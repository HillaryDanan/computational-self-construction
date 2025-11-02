"""
MERGE CROSS-ARCHITECTURE DATA

Combines separate data files into single dataset for analysis.

Usage:
    python3 scripts/merge_data.py \\
        data/raw/cross_architecture_20251102_160134.json \\
        data/raw/gemini_only_20251102_161718.json \\
        data/raw/combined_all_models.json
"""

import json
import sys

def merge_data_files(file1_path: str, file2_path: str, output_path: str):
    """
    Merge two JSON data files into one.
    
    Args:
        file1_path: Path to first data file (Claude + GPT)
        file2_path: Path to second data file (Gemini)
        output_path: Path for combined output file
    """
    print("="*70)
    print("MERGING CROSS-ARCHITECTURE DATA FILES")
    print("="*70)
    print()
    
    # Load first file
    print(f"Loading file 1: {file1_path}")
    with open(file1_path, 'r') as f:
        data1 = json.load(f)
    print(f"  Loaded {len(data1)} responses")
    
    # Count by model
    models1 = {}
    for r in data1:
        model = r.get('model', 'unknown')
        models1[model] = models1.get(model, 0) + 1
    print(f"  Models: {dict(models1)}")
    print()
    
    # Load second file
    print(f"Loading file 2: {file2_path}")
    with open(file2_path, 'r') as f:
        data2 = json.load(f)
    print(f"  Loaded {len(data2)} responses")
    
    # Count by model
    models2 = {}
    for r in data2:
        model = r.get('model', 'unknown')
        models2[model] = models2.get(model, 0) + 1
    print(f"  Models: {dict(models2)}")
    print()
    
    # Combine
    combined = data1 + data2
    print(f"Combined total: {len(combined)} responses")
    print()
    
    # Verify structure
    print("Verifying data structure...")
    required_fields = ['query_number', 'prompt', 'response', 'condition', 'model', 'timestamp']
    
    for i, record in enumerate(combined):
        missing = [f for f in required_fields if f not in record]
        if missing:
            print(f"  WARNING: Record {i} missing fields: {missing}")
    
    print("  ✓ All records have required fields")
    print()
    
    # Count final breakdown
    print("Final breakdown:")
    print()
    
    # By model
    by_model = {}
    for r in combined:
        model = r['model']
        by_model[model] = by_model.get(model, 0) + 1
    
    print("  By model:")
    for model, count in sorted(by_model.items()):
        print(f"    {model}: {count} responses")
    print()
    
    # By condition
    by_condition = {}
    for r in combined:
        cond = r['condition']
        by_condition[cond] = by_condition.get(cond, 0) + 1
    
    print("  By condition:")
    for cond, count in sorted(by_condition.items()):
        print(f"    {cond}: {count} responses")
    print()
    
    # By model × condition
    by_model_condition = {}
    for r in combined:
        key = (r['model'], r['condition'])
        by_model_condition[key] = by_model_condition.get(key, 0) + 1
    
    print("  By model × condition:")
    for (model, cond), count in sorted(by_model_condition.items()):
        print(f"    {model} × {cond}: {count} responses")
    print()
    
    # Check for expected sample sizes
    print("Sample size check:")
    expected = 20  # Should be n=20 per cell
    issues = []
    for (model, cond), count in by_model_condition.items():
        if count != expected:
            issues.append(f"  ⚠️  {model} × {cond}: {count} (expected {expected})")
        else:
            print(f"  ✓ {model} × {cond}: {count}")
    
    if issues:
        print()
        print("WARNINGS:")
        for issue in issues:
            print(issue)
    print()
    
    # Save combined file
    print(f"Saving to: {output_path}")
    with open(output_path, 'w') as f:
        json.dump(combined, f, indent=2)
    
    print()
    print("="*70)
    print("✓ MERGE COMPLETE!")
    print("="*70)
    print()
    print("NEXT STEPS:")
    print(f"  1. Run analysis: python3 scripts/analyze_cross_architecture.py {output_path}")
    print(f"  2. Run statistics: python3 scripts/statistical_cross_arch.py {output_path}")
    print()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 scripts/merge_data.py <file1> <file2> <output>")
        print()
        print("Example:")
        print("  python3 scripts/merge_data.py \\")
        print("    data/raw/cross_architecture_20251102_160134.json \\")
        print("    data/raw/gemini_only_20251102_161718.json \\")
        print("    data/raw/combined_all_models.json")
        sys.exit(1)
    
    merge_data_files(sys.argv[1], sys.argv[2], sys.argv[3])