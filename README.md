# MLOps Practical Laboratory

**Department of Computer Engineering · Practical Experiments 01–12**

This repository is the practical record for a twelve-part MLOps laboratory. Open an experiment below for its objective, procedure, implementation, captured output, and result.

## Experiments

| No. | Experiment | Open |
|---:|---|---|
| 01 | Introduction to MLOps and lifecycle | [Experiment 01](./experiment-01-mlops-introduction/README.md) |
| 02 | Git, GitHub, branching, and collaboration | [Experiment 02](./experiment-02-git-github/README.md) |
| 03 | Dataset versioning with DVC | [Experiment 03](./experiment-03-dvc/README.md) |
| 04 | Data validation and processing pipeline | [Experiment 04](./experiment-04-data-pipeline/README.md) |
| 05 | Feature management and feature-store concepts | [Experiment 05](./experiment-05-feature-store/README.md) |
| 06 | Model training and experiment tracking with MLflow | [Experiment 06](./experiment-06-mlflow/README.md) |
| 07 | Baseline model and hyperparameter search | [Experiment 07](./experiment-07-model-selection/README.md) |
| 08 | Unit testing for data validation | [Experiment 08](./experiment-08-testing/README.md) |
| 09 | Continuous integration with GitHub Actions | [Experiment 09](./experiment-09-ci/README.md) |
| 10 | Containerization with Docker | [Experiment 10](./experiment-10-docker/README.md) |
| 11 | REST API model serving | [Experiment 11](./experiment-11-rest-api/README.md) |
| 12 | Integrated MLOps workflow and results | [Experiment 12](./experiment-12-integrated-workflow/README.md) |

## Run the Python practicals

Python 3.10 or later is recommended. From the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v experiment-08-testing
```

The experiment-specific READMEs explain how to run each practical. Docker requires Docker Engine/Desktop to be installed and running.

## Repository files

- `requirements.txt` installs the Python dependencies used by the examples and tests.
- `.gitignore` excludes local environments, caches, generated datasets, model runs, and secrets from Git. It is standard repository configuration, not an experiment deliverable.
- `.github/workflows/ci.yml` runs the automated tests on GitHub Actions.
- [`reports/MLOps_Practical_Lab_Report.md`](./reports/MLOps_Practical_Lab_Report.md) is the consolidated practical report.

Each practical's `OUTPUT.txt` contains results captured from actual commands. Where a tool was unavailable, the output records that limitation instead of presenting sample text as a successful run.

## Academic integrity and reproducibility

Use the captured outputs as a record of these repository runs. Re-run them in your own environment if your course requires individually witnessed or machine-specific execution. Do not present an unavailable integration (such as Docker on a machine without Docker Engine) as completed.
