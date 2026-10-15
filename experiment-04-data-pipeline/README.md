# Practical 04 | Data Preparation Pipeline

**Focus:** data input, validation, preprocessing, feature preparation and repeatable pipeline execution.

## Aim

Build and run a small end-to-end pipeline that checks a dataset, separates features and target, splits training and test rows, fits preprocessing on training data and saves the processed test partition.

## Requirements

- Python 3.10 or later
- Install this practical's dependencies: `python -m pip install -r requirements.txt`

## Pipeline stages

| Stage | Demonstration |
|---|---|
| Data collection | Read the included `data/raw.csv` sample |
| Validation | Check that input is non-empty and contains a target column |
| Split | Keep a reproducible 80% training / 20% test split |
| Preprocessing | Fit median imputation and standard scaling on training data; transform the test data |
| Output | Save the processed test partition as `data/processed.csv` |

The source dataset is a small classroom example, not a real-world student record.

## Procedure

From this folder:

```powershell
python -m pip install -r requirements.txt
python pipeline.py
```

Inspect `data/raw.csv` before running. The script recreates `data/processed.csv` on each run; the generated file is intentionally ignored by Git.

## Observed result

The captured run processed 10 rows into 8 training rows and 2 test rows, with 2 input features. See [`OUTPUT.txt`](./OUTPUT.txt).

## Conclusion

Fitting preprocessing only on the training split avoids leaking test-set statistics into training. A single command executes the pipeline stages consistently.
