# Experiment 8 — Automated Testing

## Aim

Use automated tests to check data-validation behaviour and understand how tests protect an ML workflow from regressions.

## Learning objectives

- Run tests with pytest from the repository root.
- Distinguish valid input from expected validation failures.
- Interpret test results and identify what the current test suite does—and does not—cover.

## Requirements

- Python 3.10 or later
- Project dependencies installed from the repository-root `requirements.txt`

## Procedure

1. Review [`validation.py`](./validation.py) and [`test_validation.py`](./test_validation.py).
2. From the repository root, run `python -m pytest -v experiment-08-testing`.
3. Confirm the valid-input and invalid-input cases behave as expected.
4. Add or adapt tests for any new validation rule before changing pipeline behaviour.
5. Record the actual test summary, Python/pytest versions, and any failure diagnosis.

## Test scope

The suite contains four tests for a valid frame, an empty frame, a missing target column, and missing target values. It does not test every training pipeline or model-output case; additional practicals should add tests for their own behaviours.

## Captured result

The actual command, Python/pytest versions, and test results are recorded in [`OUTPUT.txt`](./OUTPUT.txt).

## Expected output format

See [`OUTPUT.txt`](./OUTPUT.txt) for the captured test run.

## Viva questions

1. What is the difference between a unit test and an integration test?
2. Why should invalid inputs be included in a validation test suite?
3. What does a passing test suite prove, and what does it not prove?

## Related files

- Validation implementation: [`validation.py`](./validation.py)
- Tests: [`test_validation.py`](./test_validation.py)
- CI execution: [Experiment 9](../experiment-09-ci/README.md)
