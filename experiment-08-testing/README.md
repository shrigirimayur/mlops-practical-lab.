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

1. Review [`src/validation.py`](../src/validation.py) and [`tests/test_validation.py`](../tests/test_validation.py).
2. From the repository root, run `python -m pytest -v`.
3. Confirm the valid-input and invalid-input cases behave as expected.
4. Add or adapt tests for any new validation rule before changing pipeline behaviour.
5. Record the actual test summary, Python/pytest versions, and any failure diagnosis.

## Test scope

The starter suite contains four tests for a valid frame, an empty frame, a missing target column, and missing target values. It does not yet test every training pipeline or model-output case in the syllabus; document that limitation and extend the tests when those components are added.

## Observation and result

Record the command, actual pass/fail count, and any fixes. Do not copy the illustrative output as if it were captured from your own run. Report success only if pytest exits successfully.

## Expected output format

See [`OUTPUT.txt`](./OUTPUT.txt). It describes an illustrative format, not an execution record.

## Viva questions

1. What is the difference between a unit test and an integration test?
2. Why should invalid inputs be included in a validation test suite?
3. What does a passing test suite prove, and what does it not prove?

## Related files

- Shared implementation: [`src/validation.py`](../src/validation.py)
- Shared tests: [`tests/test_validation.py`](../tests/test_validation.py)
- CI execution: [Experiment 9](../experiment-09-ci/README.md)
