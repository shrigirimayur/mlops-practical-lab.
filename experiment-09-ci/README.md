# Experiment 9 — Continuous Integration with GitHub Actions

## Aim

Automate dependency installation and the Experiment 8 test suite when changes are pushed or a pull request targets `main`.

## Workflow

The canonical workflow is [`../.github/workflows/ci.yml`](../.github/workflows/ci.yml). It checks out the repository, sets up Python 3.11, installs `requirements.txt`, and runs:

```bash
python -m pytest -v experiment-08-testing
```

## Captured result

[`OUTPUT.txt`](./OUTPUT.txt) identifies the actual GitHub Actions run for the published revision. Open the run to inspect the job and individual steps.

## Result

GitHub Actions executes the same tests used locally and retains the run logs with the commit. A successful CI job verifies this test command in the runner environment; it does not prove model quality or Docker deployment.

## Viva questions

1. What events trigger this workflow?
2. Why should the same test command run locally and in CI?
3. What does a green CI job establish—and what does it not establish?
