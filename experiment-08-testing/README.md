# Experiment 8 — Automated Testing

## Aim

Use automated tests to check data-validation behaviour and understand how tests protect an ML workflow from regressions.

## Learning objectives

- Run tests with pytest from this experiment folder.
- Distinguish valid input from expected validation failures.
- Interpret test results and identify what the current test suite does—and does not—cover.

## Requirements

- Python 3.10 or later
- Install the packages in this folder's `requirements.txt`

## Procedure

1. Open PowerShell in this folder and install its dependencies.
2. Run `python -m pytest -v`.
3. Confirm the valid-input and invalid-input cases behave as expected.
4. Add or adapt tests for any new validation rule before changing pipeline behavior.
5. Record the actual test summary, Python/pytest versions, and any failure diagnosis.

## Test scope

The suite checks input validation, trains a small model pipeline, and verifies prediction row counts and missing values. These are focused unit tests, not a complete test suite for every MLOps tool in the repository.

## Captured result

The actual command, Python/pytest versions, and test results are recorded in [`OUTPUT.txt`](./OUTPUT.txt).

## Viva questions

1. What is the difference between a unit test and an integration test?
2. Why should invalid inputs be included in a validation test suite?
3. What does a passing test suite prove, and what does it not prove?

## Related files

- Validation implementation: [`validation.py`](./validation.py)
- Tests: [`test_validation.py`](./test_validation.py)
- CI execution: [Experiment 9](../experiment-09-ci/README.md)
