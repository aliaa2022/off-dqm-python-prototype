# Open Food Facts – Data Quality Python Prototype

This prototype explores how existing Perl data quality checks from the Open Food Facts server could be migrated into Python.

The goal is to understand how the current validation logic works and experiment with a Python-based validation pipeline.

## Implemented Checks

1. **value-over-105**

Detects nutrients that exceed plausible limits per 100g or 100ml.

Example:

fat = 120 → en:nutrition-user-as-sold-100g-value-over-105-fat

---

2. **saturated-fat-greater-than-fat**

Detects inconsistencies where saturated fat exceeds total fat.

Example:

fat = 10  
saturated-fat = 12

→ en:nutrition-user-as-sold-100g-saturated-fat-greater-than-fat

---

## Architecture

Dataset → Python validation checks → error tags

Each nutrition set produces a result structure:

{
"errors": [],
"warnings": []
}


## Files

checks.py  
Contains helper functions and validation checks.

runner.py  
Loads dataset and executes checks.

dataset.json  
Small dataset used for testing.

## Next Steps

- Add more rules from `DataQualityFood.pm`
- Run checks on real Open Food Facts JSONL data
- Compare results with Perl implementation
