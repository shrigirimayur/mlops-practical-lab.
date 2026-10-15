# Experiment 7 — Baseline Model and Hyperparameter Search

## Aim
Compare baseline, Grid Search and Random Search using suitable validation and test metrics.

## Requirements
- Python 3.10 or later
- Install this folder's packages with `python -m pip install -r requirements.txt`

## Procedure
1. Open PowerShell in this folder, install the packages, and run `python model_selection.py`.
2. Compare cross-validation and held-out test metrics.
3. Explain why tuning should not use the test set.
4. Record best parameters and the chosen metric.


## Example commands and notes
## Observed result
Both searches selected `model__C=0.1`; the captured held-out test F1 was `0.9793` (accuracy `0.9737`). See [`OUTPUT.txt`](./OUTPUT.txt) for the full recorded run.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
Grid Search evaluates the specified combinations, while Random Search samples the search space. Test data is reserved for final evaluation.

## Outcome summary
The script compares both search methods on the same training split and uses a held-out test split only for final evaluation.
