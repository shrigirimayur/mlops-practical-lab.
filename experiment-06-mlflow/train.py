import os
from pathlib import Path

os.environ.setdefault("MLFLOW_DISABLE_AGENT_HINT", "1")

import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split
from mlflow.tracking import MlflowClient

HERE = Path(__file__).resolve().parent
MODEL_NAME = "mlops-practical-diabetes"


def main():
    tracking_uri = f"sqlite:///{(HERE / 'mlflow.db').as_posix()}"
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_registry_uri(tracking_uri)
    data = load_diabetes(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )
    mlflow.set_experiment("mlops-practical")

    candidates = []
    for n_estimators, max_depth in [(50, 4), (100, 6)]:
        model = RandomForestRegressor(
            n_estimators=n_estimators, max_depth=max_depth, random_state=42
        )
        cv_r2 = float(
            cross_val_score(
                model, X_train, y_train, cv=5, scoring="r2", n_jobs=-1
            ).mean()
        )
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        metrics = {
            "mae": mean_absolute_error(y_test, pred),
            "mse": mean_squared_error(y_test, pred),
            "r2": r2_score(y_test, pred),
            "cv_r2": cv_r2,
        }
        with mlflow.start_run(run_name=f"random-forest-{n_estimators}-{max_depth}"):
            mlflow.log_params(
                {
                    "model_type": "RandomForestRegressor",
                    "n_estimators": n_estimators,
                    "max_depth": max_depth,
                }
            )
            mlflow.log_metrics(metrics)
            model_info = mlflow.sklearn.log_model(
                model,
                name="model",
                skops_trusted_types=["sklearn.tree._tree.Tree"],
            )
            candidates.append(
                (
                    cv_r2,
                    mlflow.active_run().info.run_id,
                    metrics,
                    n_estimators,
                    max_depth,
                    model_info.model_uri,
                )
            )

    (
        best_cv_r2,
        best_run_id,
        best_metrics,
        best_estimators,
        best_depth,
        best_model_uri,
    ) = max(
        candidates, key=lambda candidate: candidate[0]
    )
    registered_model = mlflow.register_model(best_model_uri, MODEL_NAME)
    MlflowClient().set_registered_model_alias(
        MODEL_NAME, "champion", registered_model.version
    )
    print("Candidate runs:")
    for cv_r2, run_id, metrics, n_estimators, max_depth, _ in candidates:
        print(
            f"  run={run_id} n_estimators={n_estimators} max_depth={max_depth} "
            f"CV R2={cv_r2:.4f} test R2={metrics['r2']:.4f}"
        )
    print(f"Selected run: {best_run_id}")
    print(f"Selection metric (5-fold CV R2): {best_cv_r2:.4f}")
    print(f"Selected parameters: n_estimators={best_estimators}, max_depth={best_depth}")
    print(f"Selected test metrics: {best_metrics}")
    print(f"Registered model: {MODEL_NAME}, version {registered_model.version}")
    print(f"Champion alias: {MODEL_NAME}@champion")
    print("Tracking database: mlflow.db (local to this experiment folder)")

if __name__ == "__main__":
    main()
