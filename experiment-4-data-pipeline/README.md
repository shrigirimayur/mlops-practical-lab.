# Experiment 4 — Automated Data Pipeline

## Aim
Build a small end-to-end pipeline for data generation, validation/cleaning, and feature engineering.

## Pipeline stages
1. **Data source:** `scripts/generate_dataset.py` creates a deterministic sample customer dataset.
2. **Validation and cleaning:** `scripts/preprocess_data.py` checks required columns, unique IDs, valid numeric values, nonnegative values and binary target labels; then sorts and writes clean data.
3. **Feature engineering:** `scripts/engineer_features.py` creates spend-per-visit, high-engagement and age-band features.
4. **Reproducibility:** `dvc.yaml` declares dependencies and outputs so `dvc repro` can rerun only stages affected by changed dependencies.

## Run
```bash
python scripts/generate_dataset.py
python scripts/preprocess_data.py
python scripts/engineer_features.py
```
Or run the entire DVC-managed pipeline with `python scripts/run_dvc_practical.py` after installing requirements.

## Result
Raw, cleaned and engineered CSV files are written beneath `data/`. The scripts stop with an error when key data quality rules fail rather than silently accepting invalid input.
