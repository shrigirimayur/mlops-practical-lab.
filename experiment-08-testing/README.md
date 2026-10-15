# Practical 08 | Testing an ML Workflow

**Focus:** unit tests for data validation, training-pipeline behavior and prediction outputs.

## Aim

Use automated tests to check both accepted and invalid data, exercise a small training pipeline, and verify its predictions have the expected shape and values.

## Requirements

- Python 3.10 or later
- Install this practical's dependencies: `python -m pip install -r requirements.txt`

## Procedure

From this folder:

```powershell
python -m pip install -r requirements.txt
python -m pytest -v
```

The suite covers valid input, empty input, a missing target, missing target values, successful training and prediction, prediction row-count validation, and missing prediction values.

## Observed result

All **7 tests passed** in the recorded run. The command and test summary are captured in [`OUTPUT.txt`](./OUTPUT.txt).

## Files

- [`validation.py`](./validation.py): validation and training-pipeline functions.
- [`test_validation.py`](./test_validation.py): automated test cases.

## Conclusion

The tests catch specific data and model-output regressions. They are unit-level checks; they do not validate external stores, the complete API, or deployment.
