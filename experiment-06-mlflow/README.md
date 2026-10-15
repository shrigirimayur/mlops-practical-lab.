# Experiment 6 — MLflow Experiment Tracking

## Aim
Train a model and log parameters, metrics, artifacts and experiment runs.

## Requirements

- Python 3.10 or later
- Install the packages in this folder's `requirements.txt`

## Procedure
1. Open PowerShell in this folder and install its dependencies.
2. Run `python train.py`. It compares two candidates by five-fold cross-validation R2.
3. Review the logged parameters, test metrics, model artifacts, and registered model.
4. Start the local MLflow UI from this same folder.


## Example commands and notes
```bash
python -m pip install -r requirements.txt
python train.py
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000
```

Open `http://127.0.0.1:5000` while the UI is running. The SQLite tracking/registry database and model artifacts are written in this experiment folder. The best cross-validation run is registered and assigned the `champion` alias.

## Output
[`OUTPUT.txt`](./OUTPUT.txt) contains the captured MLflow run ID and metrics.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
MLflow associates model parameters, metrics, and artifacts with runs. The script selects the best candidate using training-only cross-validation, evaluates the selected candidate on the held-out test set, and registers that candidate.

## Outcome summary
Two Random Forest candidates are logged, compared, and the best candidate is registered locally.
