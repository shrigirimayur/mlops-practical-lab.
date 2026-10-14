import pandas as pd


def validate_frame(frame: pd.DataFrame, target: str) -> None:
    if frame.empty:
        raise ValueError("Dataset is empty")
    if frame.columns.duplicated().any():
        raise ValueError("Duplicate columns")
    if target not in frame.columns:
        raise ValueError("Target column missing")
    if frame[target].isna().any():
        raise ValueError("Target has missing values")
