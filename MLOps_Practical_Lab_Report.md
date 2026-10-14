# MLOps Practical Laboratory Report
**Department of Computer Engineering**  
**Subject:** Machine Learning Operations (MLOps)  
**Practical Record:** Experiments 1–12

## Introduction
MLOps applies software engineering and operational practices to the machine-learning lifecycle. It supports repeatable data preparation, experiment tracking, model evaluation, testing, packaging, deployment, and monitoring. This practical record describes twelve MLOps topics and provides example procedures, starter implementations, observations, and outcomes.

**Interpretation note:** This repository is a prepared practical package. Text labelled *illustrative* describes expected behaviour or a demonstration format; it is not a claim that external services, Docker, Feast, DVC remotes, or GitHub Actions were executed in the author's environment.

## Experiment 1 — Introduction to MLOps
**Aim:** Understand MLOps, compare Software Development, DevOps, and MLOps, and document an ML lifecycle.

**Theory:** Software development builds and maintains software. DevOps automates collaboration and delivery. MLOps adds data, feature, model, and experiment management because model behaviour depends on both code and changing data.

**Workflow:** Problem definition → data collection → validation → preprocessing and features → training → evaluation → versioning and packaging → deployment → monitoring → retraining or rollback.

**Tools:** Git/GitHub for source control; DVC for dataset tracking; MLflow for experiments; Feast for feature management; pytest and GitHub Actions for testing/CI; Docker for packaging; Flask for inference APIs.

**Observation:** The MLOps lifecycle requires traceability across code, datasets, parameters, metrics, model artifacts, and deployments. Production risks include data leakage, drift, inconsistent training/serving features, and dependency conflicts.

**Outcome:** A lifecycle and tool-mapping reference is included in `experiment-01-mlops-introduction/README.md`. The workflow diagram is supplied as text and can be rendered from the included Mermaid file.

## Experiment 2 — Git and GitHub Version Control
**Aim:** Learn repository creation, commits, branches, merges, conflict resolution, and remote collaboration.

**Procedure:** Check the Git version, configure identity, initialize a repository, stage files, commit changes, create a feature branch, merge changes, and inspect history. A controlled conflict can be resolved by editing conflict markers and committing the final file. The repository README contains the push commands.

**Illustrative command/output format:**
```text
$ git log --oneline
<commit-id> Add initial practical files
<commit-id> Add project README

$ git status
On branch main
nothing to commit, working tree clean
```
Commit IDs and status above are examples; actual values depend on the user's Git history.

**Observation:** Commits create checkpoints, branches isolate work, and merges combine histories. A merge conflict requires a deliberate decision about the final content.

**Outcome:** The repository contains a Git command checklist and collaboration procedure. A real remote push requires the owner to connect their own GitHub repository.

## Experiment 3 — Dataset Versioning with DVC
**Aim:** Track dataset versions separately from ordinary source files and integrate DVC metadata with Git.

**Procedure:** Install DVC, initialize it inside a Git repository, create or add a dataset, run `dvc add`, commit the `.dvc` metadata, configure a remote, and verify status/push/pull operations.

**Illustrative output format:**
```text
$ dvc status
Data and pipelines are up to date.
```
This message is only an example of a successful status check, not an execution record.

**Observation:** Git stores source code and DVC metadata, while DVC manages the contents of tracked data artifacts. A local remote demonstrates the concept but does not provide cross-computer sharing.

**Outcome:** The DVC procedure and sample dataset generator are included. A shared remote must be configured separately if cross-machine artifact transfer is required.

## Experiment 4 — Data Processing Pipeline
**Aim:** Load, validate, split, preprocess, and save data through a repeatable pipeline.

**Procedure:** Run `python experiment-04-data-pipeline/pipeline.py`. The script creates a small demonstration CSV when no input file exists, validates the target column, splits data, fits imputation/scaling on training data, and saves a processed test partition.

**Illustrative output format:**
```text
Created demonstration input data.
Input rows: 10
Training rows: 8
Test rows: 2
Processed feature count: 2
Saved test partition: ...
```
File paths vary by operating system.

**Observation:** Validation detects missing required fields. Fitting transformations on training data helps prevent test-set leakage.

**Outcome:** A runnable demonstration pipeline is included. Its output is generated when the script is run; the values above describe the expected shape of the demo rather than a captured terminal session.

## Experiment 5 — Feature Store and Feast
**Aim:** Understand reusable features and the difference between offline and online retrieval.

**Theory:** Offline stores support historical feature retrieval for training; online stores support low-latency serving. Feature stores help share feature definitions and reduce training-serving skew.

**Procedure:** The package includes a small SQLite teaching demo at `experiment-05-feature-store/feature_store_demo.py`. Run it with Python to inspect reusable feature rows. This demo explains the concept but is not a Feast deployment. To demonstrate Feast itself, install a compatible version, initialize a repository, register feature definitions, materialize data, and test retrieval using the official documentation.

**Illustrative output format:**
```text
Feature rows retrieved: 3
(1, 20, 100)
(2, 25, 500)
(3, 31, 900)
Note: SQLite demo only; Feast must be configured separately.
```

**Observation:** A feature repository can centralize definitions. Actual Feast behaviour depends on its provider, configuration, timestamps, and installed version.

**Outcome:** The SQLite feature-store concept demo is included; Feast integration is documented as a separate setup because it requires version- and provider-specific configuration.

## Experiment 6 — MLflow Experiment Tracking
**Aim:** Train a model and track parameters, metrics, and model artifacts.

**Procedure:** Run `python experiment-06-mlflow/train.py`, then start `mlflow ui --host 127.0.0.1 --port 5000`. Open the local UI and inspect the experiment and run. The script uses a public scikit-learn diabetes dataset and logs a Random Forest regression run.

**Illustrative metric format:**
```text
Experiment: mlops-practical
Run name: random-forest-baseline
Parameters: n_estimators=100, max_depth=6
Metrics: MAE=<value>, MSE=<value>, R2=<value>
```

**Observation:** MLflow associates parameters, metrics, and artifacts with a run ID, making experiments easier to compare and reproduce.

**Outcome:** A runnable training script is included. The actual run ID and metric values are generated by MLflow when executed; model registry support depends on the configured tracking backend and MLflow version.

## Experiment 7 — Baseline Model and Hyperparameter Search
**Aim:** Compare Grid Search and Random Search with cross-validation and held-out test metrics.

**Procedure:** Run `python experiment-07-model-selection/model_selection.py`. The script uses the breast-cancer dataset, a StandardScaler/LogisticRegression pipeline, and F1 as the tuning score. It reports best parameters, cross-validation F1, test accuracy, and test F1.

**Result table format:**

| Method | Best parameters | CV F1 | Test accuracy | Test F1 |
|---|---|---:|---:|---:|
| Grid Search | Printed by script | Printed by script | Printed by script | Printed by script |
| Random Search | Printed by script | Printed by script | Printed by script | Printed by script |

**Observation:** Grid Search evaluates each listed parameter combination. Random Search samples combinations. The held-out test set should not be used to choose hyperparameters.

**Outcome:** The comparison script is included and computes metrics at runtime. The table intentionally refers to the program's output instead of inventing numerical scores.

## Experiment 8 — Testing Data and ML Pipelines
**Aim:** Test data-validation functions with valid and invalid inputs.

**Procedure:** From the repository root, run `python -m pytest -v`. Tests cover a valid frame, an empty frame, a missing target column, and missing target values.

**Illustrative output format:**
```text
tests/test_validation.py::test_valid_frame PASSED
tests/test_validation.py::test_empty_frame PASSED
tests/test_validation.py::test_missing_target PASSED
tests/test_validation.py::test_missing_target_value PASSED
4 passed
```
This is a sample format. Actual output is determined by the test run and installed dependencies.

**Observation:** Unit tests make data-validation behaviour repeatable and help catch regressions when code changes.

**Outcome:** Four starter unit tests are included in `tests/test_validation.py`.

## Experiment 9 — Continuous Integration with GitHub Actions
**Aim:** Automate dependency installation and test execution on pushes and pull requests.

**Procedure:** The repository includes `.github/workflows/ci.yml`. After pushing it to GitHub, open the Actions tab and inspect the actual workflow run.

**Illustrative workflow stages:** Checkout → set up Python → install requirements → run pytest.

**Observation:** CI provides repeatable checks and fast feedback. A passing test workflow does not, by itself, establish model quality or production readiness.

**Outcome:** A workflow configuration is included. Its status is only known after GitHub executes it on the repository.

## Experiment 10 — Docker Containerization
**Aim:** Package an ML API and its dependencies into a Docker image.

**Procedure:** With Docker installed and running, execute `docker build -t mlops-practical:1.0 .`, then run `docker run --rm -p 8000:8000 mlops-practical:1.0`. Test the health endpoint in another terminal.

**Illustrative command format:**
```text
$ docker images
REPOSITORY         TAG     IMAGE ID      SIZE
mlops-practical    1.0     <image-id>    <size>
```

**Observation:** An image packages application files and dependencies. A container is a running instance of an image. Port mapping makes the container's service available on the host.

**Outcome:** The Dockerfile and `.dockerignore` are included. A successful build and image ID can only be reported after running Docker.

## Experiment 11 — REST API for Model Inference
**Aim:** Serve model predictions through HTTP endpoints and validate requests.

**Procedure:** Start the app with `python app.py`. Test `GET /health` and `POST /predict` using cURL or Postman. The prediction endpoint expects four numeric Iris features.

**Illustrative health response:**
```json
{"status": "ok"}
```

**Illustrative prediction response shape:**
```json
{
  "prediction": 0,
  "class_name": "setosa",
  "probabilities": [0.98, 0.01, 0.01],
  "latency_ms": 2.5
}
```
The prediction, probabilities, and latency are example values only; the live app computes its own response.

**Observation:** Input validation prevents malformed requests from reaching the model. Latency depends on machine load, server state, and request conditions.

**Outcome:** A Flask API and request examples are included. Real response values are generated when the app is run.

## Experiment 12 — Integrated MLOps Workflow
**Aim:** Connect source control, data tracking, processing, experiment tracking, testing, CI, packaging, and model serving.

**Workflow:** Git → DVC → data validation/preprocessing → feature management → model training and MLflow → automated tests/CI → Docker → REST API → monitoring.

**Observation:** Integration improves traceability and repeatability, but each service must be configured and checked. Tool configuration alone does not prove a successful end-to-end run.

**Outcome:** The repository includes an integration checklist and links to all experiment folders. The complete workflow is described, with execution requirements documented for services that need an external runtime.

## Overall conclusion
This practical package covers the core concepts and example implementations used in an MLOps workflow: source control, data versioning, data processing, feature management, experiment tracking, model selection, testing, continuous integration, containerization, and API serving. The code and configuration files provide a consistent starting point. Example outputs are marked as illustrative; external-tool execution status should be reported only after actual verification.

## References
- Git: https://git-scm.com/doc
- GitHub: https://docs.github.com/en/repositories
- DVC: https://dvc.org/doc
- Feast: https://docs.feast.dev/
- MLflow: https://mlflow.org/docs/latest/
- scikit-learn: https://scikit-learn.org/stable/
- pytest: https://docs.pytest.org/
- GitHub Actions: https://docs.github.com/en/actions
- Docker: https://docs.docker.com/
- Flask: https://flask.palletsprojects.com/
