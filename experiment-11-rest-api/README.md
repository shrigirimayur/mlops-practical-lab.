# Experiment 11 — REST API for Model Inference

## Aim
Expose a trained demonstration model through a Flask REST API and test valid/invalid requests.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. Start the app with `python app.py`.
2. Test `/health`.
3. Send a JSON POST request to `/predict`.
4. Test malformed input and incorrect feature counts.
5. Record response body and latency from your actual run.


## Example commands and notes
```bash
python app.py
curl http://127.0.0.1:8000/health
```

Use Postman or cURL for `/predict`. The included example uses the Iris dataset and expects four numeric features.


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
The API validates request fields and returns a prediction response; a health endpoint supports basic service checks.

## Outcome summary
A Flask app and request examples are included. Response values and latency are generated at runtime.
