# Practical 09 | Continuous Integration with GitHub Actions

**Focus:** automated dependency installation, test execution and CI result reporting.

## Aim

Run the Experiment 9 test suite automatically when code is pushed or a pull request targets `main`.

## Requirements

- A GitHub repository with GitHub Actions enabled.
- The dependencies listed in this practical's `requirements.txt`.

## Procedure

1. Review the repository workflow at [`../.github/workflows/ci.yml`](../.github/workflows/ci.yml).
2. Push a change to `main` or open a pull request targeting `main`.
3. In GitHub, open **Actions** and inspect the `MLOps Practical CI` run.
4. The workflow installs this folder's dependencies and runs this folder's pytest suite.

To reproduce the CI commands locally, from this folder run:

```powershell
python -m pip install -r requirements.txt
python -m pytest -v
```

## Observed result

The recorded local run passed **7 tests**; see [`OUTPUT.txt`](./OUTPUT.txt). The workflow is now located at the repository root, where GitHub discovers workflow files. A green local run is not evidence of a successful GitHub-hosted run; check the Actions page for the run associated with the submitted commit.

## Conclusion

CI repeats the test command in a clean runner and provides a visible pass/fail result for repository changes. It verifies the configured tests, not model quality or Docker deployment.
