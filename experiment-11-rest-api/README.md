# Experiment 11 — REST API for Model Inference

## Aim
Expose a trained demonstration model through a Flask REST API and test valid/invalid requests.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. From the repository root, start the app with `python experiment-11-rest-api/app.py`.
2. Test `/health`.
3. Send a JSON POST request to `/predict`.
4. Test malformed input and incorrect feature counts.
5. Record response body and latency from your actual run.


## Example commands and notes
```bash
python experiment-11-rest-api/app.py
curl http://127.0.0.1:8000/health
```

Use Postman or cURL for `/predict`. The included example uses the Iris dataset and expects four numeric features.


## Observed result
The Flask test client returned HTTP 200 for health and a valid Iris prediction, and HTTP 400 for an invalid feature count. The recorded responses and in-process latency are in [`OUTPUT.txt`](./OUTPUT.txt); the latency is not a network benchmark.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
The API validates request fields and returns a prediction response; a health endpoint supports basic service checks.

## Outcome summary
A Flask app and request examples are included. Response values and latency are generated at runtime.

## Related files
- [`app.py`](./app.py) contains the Flask application and trained Iris classifier.
- [`requests.md`](./requests.md) contains example health, prediction, and invalid-input requests.
- [Experiment 10](../experiment-10-docker/README.md) packages this API in Docker.
