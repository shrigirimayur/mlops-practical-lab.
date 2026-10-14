# MLOps Practical Laboratory

**Department of Computer Engineering · Experiments 01–12**

A hands-on laboratory repository covering the machine-learning operations lifecycle: source and data versioning, data pipelines, feature management, experiment tracking, model selection, testing, CI, containers, and model serving.

> **Execution and evidence:** This repository contains runnable examples, reference procedures, and illustrative output formats. An included script or expected output is not evidence that a tool or external service has run. Record your own commands, versions, results, screenshots, and limitations in the relevant experiment before submitting.

## Experiments

| No. | Practical | Folder |
| --- | --- | --- |
| 01 | Introduction to MLOps and lifecycle workflow | [experiment-01-mlops-introduction](./experiment-01-mlops-introduction/) |
| 02 | Git, GitHub, branching, merging, and collaboration | [experiment-02-git-github](./experiment-02-git-github/) |
| 03 | Dataset versioning and reproducibility with DVC | [experiment-03-dvc](./experiment-03-dvc/) |
| 04 | Data collection, validation, and processing pipeline | [experiment-04-data-pipeline](./experiment-04-data-pipeline/) |
| 05 | Feature stores and reusable features | [experiment-05-feature-store](./experiment-05-feature-store/) |
| 06 | Experiment tracking and model artifacts with MLflow | [experiment-06-mlflow](./experiment-06-mlflow/) |
| 07 | Baseline models and hyperparameter search | [experiment-07-model-selection](./experiment-07-model-selection/) |
| 08 | Automated testing for data and ML components | [experiment-08-testing](./experiment-08-testing/) |
| 09 | Continuous integration with GitHub Actions | [experiment-09-ci](./experiment-09-ci/) |
| 10 | Containerization with Docker | [experiment-10-docker](./experiment-10-docker/) |
| 11 | REST API model serving with Flask | [experiment-11-rest-api](./experiment-11-rest-api/) |
| 12 | Integrated end-to-end MLOps workflow | [experiment-12-integrated-workflow](./experiment-12-integrated-workflow/) |

Each experiment folder contains its own `README.md` with the aim, procedure, commands or implementation notes, observation prompts, result guidance, and an `OUTPUT.txt` reference where applicable.

## Repository layout

```text
.
├── .github/workflows/ci.yml       # Automated test workflow
├── evidence/                      # Optional genuine screenshots/logs
├── experiment-01-.../             # Experiment instructions and assets
├── ...                            # Experiments 02–11
├── experiment-12-.../             # Integration checklist and instructions
├── sample_outputs/                # Clearly labelled illustrative examples
├── src/                           # Shared data validation code
├── tests/                         # Shared automated tests
├── app.py                         # Flask prediction API (Experiments 10–11)
├── Dockerfile                     # Container definition (Experiment 10)
├── MLOps_Practical_Lab_Report.md  # Consolidated report reference
└── requirements.txt               # Python dependencies for examples/tests
```

The executable API, Dockerfile, CI workflow, and shared tests are intentionally kept at repository level and linked from the experiment instructions. This avoids maintaining duplicate copies of shared files.

## Getting started

### Requirements

- Python 3.10 or later
- Git
- Optional tools for the corresponding practicals: DVC, Feast, MLflow, Docker Desktop/Engine, and a GitHub account

### Create an environment and install dependencies

Run these commands from the repository root.

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Verify the shared examples

```bash
python -m pytest -v
python experiment-01-mlops-introduction/workflow_demo.py
python experiment-03-dvc/create_dataset.py
python experiment-04-data-pipeline/pipeline.py
python experiment-05-feature-store/feature_store_demo.py
python experiment-07-model-selection/model_selection.py
```

The first and third commands above create local data/artifacts. Check each experiment guide before running commands that initialize a repository, create a DVC remote, start a service, or build a container. MLflow and Docker steps are documented in Experiments 6 and 10.

## Recording results

For each experiment:

1. Read its README and confirm the prerequisites.
2. Run the commands in order from the stated working directory.
3. Record the command, tool/version, actual output, observations, and conclusion.
4. Save only genuine screenshots or logs in `evidence/` and identify their experiment.
5. Mark external integrations complete only after verifying them (for example, a DVC transfer, a visible MLflow run, a passing Actions run, or a working Docker container).

See [REPORT_COMPLETION_GUIDE.md](./REPORT_COMPLETION_GUIDE.md) for a suggested report format. Examples in [sample_outputs](./sample_outputs/) and experiment `OUTPUT.txt` files are illustrative, not execution records.

## Continuous integration

The workflow at [.github/workflows/ci.yml](./.github/workflows/ci.yml) installs the project requirements and runs `python -m pytest -v` on pushes and pull requests targeting `main`. A workflow file is not evidence of a successful run; check the repository's **Actions** tab after pushing.

## Publish to GitHub

Create or choose a dedicated, empty GitHub repository for this project. From this project directory, initialize and push the repository using the instructions in [UPLOAD_TO_GITHUB.md](./UPLOAD_TO_GITHUB.md). Do not run Git commands from the parent Desktop folder.

## Safety and data

- Never commit credentials, access tokens, passwords, `.env` files, private datasets, or personal information.
- Inspect `git status` and the staged diff before every commit.
- Use the provided synthetic/sample data for demonstrations unless you have permission to use another dataset.
- Avoid committing generated caches, local MLflow runs, or local-only DVC configuration.

## References

- [Git documentation](https://git-scm.com/doc)
- [GitHub documentation](https://docs.github.com/en/repositories)
- [DVC documentation](https://dvc.org/doc)
- [Feast documentation](https://docs.feast.dev/)
- [MLflow documentation](https://mlflow.org/docs/latest/)
- [scikit-learn documentation](https://scikit-learn.org/stable/)
- [pytest documentation](https://docs.pytest.org/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [Docker documentation](https://docs.docker.com/)
- [Flask documentation](https://flask.palletsprojects.com/)
