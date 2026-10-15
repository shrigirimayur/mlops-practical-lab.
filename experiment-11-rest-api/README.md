# Experiment 11 — REST API for Model Inference

## Aim
Expose a trained demonstration model through a Flask REST API and test valid/invalid requests.

## Requirements
- Python 3.10 or later
- Install this folder's packages with `python -m pip install -r requirements.txt`

## Procedure
1. Open PowerShell in this folder and install the packages.
2. Start the app with `python app.py`.
3. In a second terminal, test the health and prediction endpoints.
4. Send an invalid feature count and confirm the API returns HTTP 400.


## Example commands and notes
```powershell
python -m pip install -r requirements.txt
python app.py
```

Use Postman or cURL for requests in [`requests.md`](./requests.md). The example uses the Iris dataset and expects four numeric features.


## Observed result
The Flask test client returned HTTP 200 for health and a valid Iris prediction, and HTTP 400 for an invalid feature count. The recorded responses and in-process latency are in [`OUTPUT.txt`](./OUTPUT.txt); the latency is not a network benchmark.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
The API validates request fields and returns a prediction response; a health endpoint supports basic service checks.

## Outcome summary
A Flask app trains its demonstration classifier when it starts. The test-client response time is not a network performance benchmark.

## Related files
- [`app.py`](./app.py) contains the Flask application and trained Iris classifier.
- [`requests.md`](./requests.md) contains example health, prediction, and invalid-input requests.
- [Experiment 10](../experiment-10-docker/README.md) packages this API in Docker.
