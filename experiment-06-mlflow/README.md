# Experiment 6 — MLflow Experiment Tracking

## Aim
Train a model and log parameters, metrics, artifacts and experiment runs.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. Install dependencies from `requirements.txt`.
2. Run `train.py`.
3. Start the local MLflow UI.
4. Compare run parameters and metrics.
5. Record run IDs and model artifact locations.
6. Use a registry workflow only if supported by your MLflow configuration.


## Example commands and notes
```bash
python experiment-06-mlflow/train.py
mlflow ui --host 127.0.0.1 --port 5000
```

Open `http://127.0.0.1:5000` while the UI process is running. Model registry support depends on the tracking/backend configuration.


## Observation
Write what you actually observed. Include tool versions, commands, important values, errors, and how you resolved them.

## Result
State only what you completed and verified. If a tool could not be configured, document the limitation rather than claiming success.

## Output
See the `OUTPUT.txt` file in this experiment folder for the sample/expected output format. Outputs that depend on running an external tool are labelled illustrative and should not be interpreted as proof of execution.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
MLflow associates model parameters, metrics, and artifacts with experiment runs, enabling comparison and traceability.

## Outcome summary
A training script is included. Actual run IDs and metric values are produced at runtime; registry support depends on backend configuration.
