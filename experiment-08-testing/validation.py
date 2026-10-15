import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def validate_frame(frame: pd.DataFrame, target: str) -> None:
    if frame.empty:
        raise ValueError("Dataset is empty")
    if frame.columns.duplicated().any():
        raise ValueError("Duplicate columns")
    if target not in frame.columns:
        raise ValueError("Target column missing")
    if frame[target].isna().any():
        raise ValueError("Target has missing values")


def train_model(frame: pd.DataFrame, target: str) -> tuple[Pipeline, pd.Series]:
    validate_frame(frame, target)
    features = frame.drop(columns=target)
    labels = frame[target]
    model = Pipeline(
        [
            ("scale", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )
    model.fit(features, labels)
    predictions = pd.Series(model.predict(features), index=frame.index)
    validate_model_output(predictions, expected_rows=len(frame))
    return model, predictions


def validate_model_output(predictions: pd.Series, expected_rows: int) -> None:
    if len(predictions) != expected_rows:
        raise ValueError("Model output row count does not match input")
    if predictions.isna().any():
        raise ValueError("Model output contains missing values")
