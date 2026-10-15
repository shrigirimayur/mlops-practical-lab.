# Experiment 9 — Continuous Integration with GitHub Actions

## Aim

Automate dependency installation and the Experiment 8 test suite when changes are pushed or a pull request targets `main`.

## Workflow

The workflow file, dependencies, and validation test suite are included in this folder. GitHub Actions only discovers workflow files under `.github/workflows` at the root of a GitHub repository. To run this practical as its own GitHub repository, place the contents of this folder at the repository root and copy `ci.yml` to `.github/workflows/ci.yml`. Then the workflow installs `requirements.txt` and runs the included tests:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## Captured result

[`OUTPUT.txt`](./OUTPUT.txt) records the local seven-test run and a prior successful GitHub Actions run. The workflow source stays in this experiment folder so the practical is self-contained; GitHub does not auto-run this nested workflow in the assignment repository.

## Result

GitHub Actions installs the specified dependencies and runs the included tests on pushes and pull requests. Passing CI verifies the configured tests in the runner environment; it does not prove model quality or Docker deployment.

## Viva questions

1. What events trigger this workflow?
2. Why should the same test command run locally and in CI?
3. What does a green CI job establish—and what does it not establish?
