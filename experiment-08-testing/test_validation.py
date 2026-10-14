import pandas as pd
import pytest

from validation import validate_frame


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
