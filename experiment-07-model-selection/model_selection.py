from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MLFLOW_DISABLE_AGENT_HINT", "1")

import mlflow
import mlflow.sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    cross_val_score,
    train_test_split,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

HERE = Path(__file__).resolve().parent


def build_pipeline() -> Pipeline:
    return Pipeline(
        [
            ("scale", StandardScaler()),
            ("model", LogisticRegression(max_iter=3000)),
        ]
    )


def main() -> None:
    tracking_uri = f"sqlite:///{(HERE / 'mlflow.db').as_posix()}"
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment("breast-cancer-model-search")

    data = load_breast_cancer(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        data.data,
        data.target,
        test_size=0.2,
        random_state=42,
        stratify=data.target,
    )
    search_space = {"model__C": [0.01, 0.1, 1.0, 10.0]}

    baseline = build_pipeline()
    baseline_cv_f1 = float(
        cross_val_score(baseline, X_train, y_train, cv=5, scoring="f1").mean()
    )
    baseline.fit(X_train, y_train)
    baseline_predictions = baseline.predict(X_test)
    baseline_metrics = {
        "cv_f1": baseline_cv_f1,
        "test_accuracy": accuracy_score(y_test, baseline_predictions),
        "test_f1": f1_score(y_test, baseline_predictions),
    }
    with mlflow.start_run(run_name="baseline-logistic-regression") as run:
        mlflow.log_params({"model_type": "LogisticRegression", "C": 1.0})
        mlflow.log_metrics(baseline_metrics)
        mlflow.sklearn.log_model(baseline, name="model")
        baseline_run_id = run.info.run_id

    searches = [
        (
            "Grid Search",
            GridSearchCV(
                build_pipeline(),
                search_space,
                cv=5,
                scoring="f1",
                n_jobs=-1,
            ),
        ),
        (
            "Random Search",
            RandomizedSearchCV(
                build_pipeline(),
                search_space,
                n_iter=2,
                cv=5,
                scoring="f1",
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ]

    print("Baseline Logistic Regression")
    print(f"Run ID: {baseline_run_id}")
    print(f"CV F1: {baseline_metrics['cv_f1']:.4f}")
    print(f"Test accuracy: {baseline_metrics['test_accuracy']:.4f}")
    print(f"Test F1: {baseline_metrics['test_f1']:.4f}")

    for name, search in searches:
        search.fit(X_train, y_train)
        predictions = search.predict(X_test)
        metrics = {
            "cv_f1": float(search.best_score_),
            "test_accuracy": accuracy_score(y_test, predictions),
            "test_f1": f1_score(y_test, predictions),
        }
        with mlflow.start_run(run_name=name.lower().replace(" ", "-")) as run:
            mlflow.log_params(
                {
                    "model_type": "LogisticRegression",
                    "search_method": name,
                    **search.best_params_,
                }
            )
            mlflow.log_metrics(metrics)
            mlflow.sklearn.log_model(search.best_estimator_, name="model")
            run_id = run.info.run_id

        print(f"\n{name}")
        print(f"Run ID: {run_id}")
        print(f"Tested parameters: {search.cv_results_['params']}")
        print(f"Best parameters: {search.best_params_}")
        print(f"CV F1: {metrics['cv_f1']:.4f}")
        print(f"Test accuracy: {metrics['test_accuracy']:.4f}")
        print(f"Test F1: {metrics['test_f1']:.4f}")

    print("\nMLflow tracking database: mlflow.db (local to this experiment folder)")
    print("All three runs are available in the 'breast-cancer-model-search' experiment.")


if __name__ == "__main__":
    main()
