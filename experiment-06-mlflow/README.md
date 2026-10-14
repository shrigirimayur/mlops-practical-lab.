# Experiment 6 — MLflow Experiment Tracking

## Aim
Train a model and log parameters, metrics, artifacts and experiment runs.

## Requirements
- Python 3.10 or later
- Dependencies installed from the repository-root `requirements.txt`

## Procedure
1. Install dependencies from `requirements.txt`.
2. From the repository root, run `python experiment-06-mlflow/train.py`.
3. Start the local MLflow UI.
4. Compare run parameters and metrics.
5. Record run IDs and model artifact locations.
6. Use a registry workflow only if supported by your MLflow configuration.


## Example commands and notes
```bash
python experiment-06-mlflow/train.py
mlflow ui --host 127.0.0.1 --port 5000
```

Open `http://127.0.0.1:5000` while the UI process is running. Model registry support depends on the tracking/backend configuration.


## Output
[`OUTPUT.txt`](./OUTPUT.txt) contains the captured MLflow run ID and metrics.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
MLflow associates model parameters, metrics, and artifacts with experiment runs, enabling comparison and traceability.

## Outcome summary
A Random Forest regression run, its metrics, and a model artifact were logged. A model registry was not configured.
