import pandas as pd
import pytest

from validation import train_model, validate_frame, validate_model_output


def test_valid_frame():
    validate_frame(pd.DataFrame({"x": [1, 2], "target": [0, 1]}), "target")


def test_empty_frame():
    with pytest.raises(ValueError, match="empty"):
        validate_frame(pd.DataFrame(), "target")


def test_missing_target():
    with pytest.raises(ValueError, match="missing"):
        validate_frame(pd.DataFrame({"x": [1, 2]}), "target")


def test_missing_target_value():
    frame = pd.DataFrame({"x": [1, 2], "target": [0, None]})
    with pytest.raises(ValueError, match="missing values"):
        validate_frame(frame, "target")


def test_training_pipeline_returns_complete_predictions():
    frame = pd.DataFrame(
        {
            "x1": [0, 1, 2, 3, 4, 5],
            "x2": [5, 4, 3, 2, 1, 0],
            "target": [0, 0, 0, 1, 1, 1],
        }
    )
    model, predictions = train_model(frame, "target")
    assert len(predictions) == len(frame)
    assert set(predictions).issubset({0, 1})
    assert len(model.predict(frame[["x1", "x2"]])) == len(frame)


def test_model_output_row_count_must_match_input():
    with pytest.raises(ValueError, match="row count"):
        validate_model_output(pd.Series([0]), expected_rows=2)


def test_model_output_cannot_contain_missing_values():
    with pytest.raises(ValueError, match="missing values"):
        validate_model_output(pd.Series([0, None]), expected_rows=2)
