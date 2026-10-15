# Practical 06 | Experiment Tracking with MLflow

**Focus:** model training, parameter and metric logging, artifact tracking, run comparison and model registration.

## Aim

Compare two Random Forest regressors, select one by cross-validation on training data, evaluate it on held-out data, and register the selected model in MLflow.

## Requirements

- Python 3.10 or later
- Install this practical's dependencies: `python -m pip install -r requirements.txt`

## Procedure

From this folder:

```powershell
python -m pip install -r requirements.txt
python train.py
```

To inspect the experiment UI in another terminal:

```powershell
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000
```

Open `http://127.0.0.1:5000`. The SQLite tracking database and model artifacts are local to this practical.

## Observed result

The script logged two candidate runs and selected the model with the higher five-fold cross-validation R². The selected model achieved CV R² `0.4037` and held-out test R² `0.4549`; MLflow registered it as `mlops-practical-diabetes` version `1` and assigned the `champion` alias. Run IDs and additional metrics are in [`OUTPUT.txt`](./OUTPUT.txt).

## Conclusion

MLflow preserves parameters, metrics and model artifacts for comparison. The candidate was selected using cross-validation; the held-out test set was reserved for final evaluation.
