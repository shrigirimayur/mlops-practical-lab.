# Experiment 4 — Data Collection and Processing Pipeline

## Aim
Load, validate, preprocess, engineer features and execute a repeatable data pipeline.

## Requirements
- Python 3.10 or later
- Install this folder's packages with `python -m pip install -r requirements.txt`

## Procedure
1. Open PowerShell in this folder.
2. Install the listed packages and run `python pipeline.py`.
3. Review `data/raw.csv` and the generated `data/processed.csv`.


## Example commands and notes
## Observed result
The pipeline processed 10 sample rows into 8 training rows and 2 test rows, using 2 features. See [`OUTPUT.txt`](./OUTPUT.txt) for the captured command output.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
The demonstration script validates input, splits rows, fits preprocessing on training data, and writes a processed test partition.

## Outcome summary
The script creates sample input data when needed, validates it, fits preprocessing on training data only, and writes the processed test partition.
