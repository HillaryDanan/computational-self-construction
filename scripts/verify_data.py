"""
VERIFY DATA COMPATIBILITY

Checks if data files have correct format for analysis scripts.

Usage:
    python3 scripts/verify_data.py <data_file.json>
"""

import json
import sys

def verify_data_format(data_path: str):
    """Check if data file is compatible with analysis scripts."""
    
    print("="*70)
    print("DATA FORMAT VERIFICATION")
    print("="*70)
    print()
    
    print(f"Loading: {data_path}")
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    print(f"Total records: {len(data)}")
    print()
    
    # Check structure
    required_fields = ['query_number', 'prompt', 'response', 'condition', 'model', 'timestamp']
    
    print("Checking required fields...")
    all_good = True
    for i, record in enumerate(data[:5]):  # Check first 5
        missing = [f for f in required_fields if f not in record]
        if missing:
            print(f"  ✗ Record {i} missing: {missing}")
            all_good = False
        else:
            print(f"  ✓ Record {i} has all fields")
    
    if len(data) > 5:
        print(f"  ... (checked first 5 of {len(data)} records)")
    print()
    
    if not all_good:
        print("❌ DATA FORMAT ERROR: Missing required fields")
        return False
    
    # Check values
    print("Checking field values...")
    
    models = set()
    conditions = set()
    
    for record in data:
        models.add(record.get('model', 'unknown'))
        conditions.add(record.get('condition', 'unknown'))
    
    print(f"  Models found: {sorted(models)}")
    print(f"  Conditions found: {sorted(conditions)}")
    print()
    
    # Expected values
    expected_models = {'claude', 'gpt', 'gemini'}
    expected_conditions = {'baseline', 'full_meta'}
    
    if 'unknown' in models:
        print("  ⚠️  WARNING: Some records have 'unknown' model")
    if 'unknown' in conditions:
        print("  ⚠️  WARNING: Some records have 'unknown' condition")
    
    if models <= expected_models and conditions <= expected_conditions:
        print("  ✓ All values are expected")
    else:
        unexpected_models = models - expected_models
        unexpected_conditions = conditions - expected_conditions
        if unexpected_models:
            print(f"  ⚠️  Unexpected models: {unexpected_models}")
        if unexpected_conditions:
            print(f"  ⚠️  Unexpected conditions: {unexpected_conditions}")
    print()
    
    # Check sample sizes
    print("Checking sample sizes...")
    by_model_condition = {}
    for r in data:
        key = (r['model'], r['condition'])
        by_model_condition[key] = by_model_condition.get(key, 0) + 1
    
    expected_n = 20
    balanced = True
    
    for (model, cond), count in sorted(by_model_condition.items()):
        if count == expected_n:
            print(f"  ✓ {model} × {cond}: n={count}")
        else:
            print(f"  ⚠️  {model} × {cond}: n={count} (expected {expected_n})")
            balanced = False
    print()
    
    if not balanced:
        print("  ⚠️  WARNING: Unbalanced design (some cells != 20)")
        print("  This is OK, but may affect statistical power")
    else:
        print("  ✓ Balanced design (all cells = 20)")
    print()
    
    # Check response text
    print("Checking response text...")
    empty_responses = 0
    for record in data:
        if not record.get('response') or len(record['response'].strip()) == 0:
            empty_responses += 1
    
    if empty_responses > 0:
        print(f"  ⚠️  {empty_responses} empty responses found")
    else:
        print(f"  ✓ All responses have text")
    print()
    
    # Final verdict
    print("="*70)
    if all_good and empty_responses == 0:
        print("✓ DATA FORMAT VERIFIED - READY FOR ANALYSIS")
        print()
        print("You can now run:")
        print(f"  python3 scripts/analyze_cross_architecture.py {data_path}")
        print(f"  python3 scripts/statistical_cross_arch.py {data_path}")
    else:
        print("⚠️  DATA HAS WARNINGS - Review issues above")
    print("="*70)
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/verify_data.py <data_file.json>")
        sys.exit(1)
    
    verify_data_format(sys.argv[1])