import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def main():
    data = load_diabetes(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )
    mlflow.set_experiment("mlops-practical")
    with mlflow.start_run(run_name="random-forest-baseline"):
        model = RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42)
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        metrics = {
            "mae": mean_absolute_error(y_test, pred),
            "mse": mean_squared_error(y_test, pred),
            "r2": r2_score(y_test, pred),
        }
        mlflow.log_params({"model_type": "RandomForestRegressor", "n_estimators": 100, "max_depth": 6})
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(
            model,
            name="model",
            skops_trusted_types=["sklearn.tree._tree.Tree"],
        )
        print("Logged MLflow run:", mlflow.active_run().info.run_id)
        print("Metrics:", metrics)

if __name__ == "__main__":
    main()
