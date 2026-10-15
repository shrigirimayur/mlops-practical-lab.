# Practical 07 | Baseline and Hyperparameter Search

**Focus:** baseline evaluation, Grid Search, Random Search, held-out metrics and MLflow run comparison.

## Aim

Compare a default Logistic Regression baseline with tuned candidates on the Breast Cancer Wisconsin dataset, and log each run for repeatable comparison.

## Requirements

- Python 3.10 or later
- Install this practical's dependencies: `python -m pip install -r requirements.txt`

## Procedure

From this folder:

```powershell
python -m pip install -r requirements.txt
python model_selection.py
```

The script uses a stratified train/test split, evaluates the baseline with five-fold F1 cross-validation, checks all four `C` values with Grid Search, and samples two of those values with Random Search. It evaluates each selected estimator on the held-out test set and logs the baseline and both search results and model artifacts to MLflow.

To compare runs in the MLflow UI:

```powershell
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000
```

## Observed result

| Run | CV F1 | Test accuracy | Test F1 |
|---|---:|---:|---:|
| Baseline Logistic Regression (`C=1.0`) | 0.9843 | 0.9825 | 0.9861 |
| Grid Search (`C=0.1`) | 0.9845 | 0.9737 | 0.9793 |
| Random Search (`C=0.1`) | 0.9845 | 0.9737 | 0.9793 |

The three runs and their model artifacts were logged to MLflow. The console output lists the candidate settings evaluated by each search; captured run IDs and metrics are in [`OUTPUT.txt`](./OUTPUT.txt).

**Evaluation note:** the searches were selected using cross-validation. In this run, the baseline scored higher on the held-out test set than the CV-selected searches; that difference is reported rather than hidden. Test metrics were not used to choose hyperparameters.

## Conclusion

Grid Search checks every specified setting while Random Search samples the search space. MLflow makes the baseline and tuned-run comparison inspectable instead of relying on console output alone.
