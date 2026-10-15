# Practical 11 | REST API for Model Inference

**Focus:** Flask service, trained-model integration, prediction endpoint, request validation and response measurement.

## Aim

Serve Iris model predictions through HTTP endpoints and verify health, a valid prediction request and an invalid request.

## Requirements

- Python 3.10 or later
- Install this practical's dependencies: `python -m pip install -r requirements.txt`

## Procedure

From this folder:

```powershell
python -m pip install -r requirements.txt
python app.py
```

In a second terminal, send requests as shown in [`requests.md`](./requests.md):

```powershell
curl.exe http://127.0.0.1:8000/health
curl.exe -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"features\":[5.1,3.5,1.4,0.2]}"
curl.exe -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"features\":[1,2]}"
```

## Observed result

The Flask test client returned HTTP `200` for health, HTTP `200` and class `setosa` for the valid prediction, and HTTP `400` for the invalid feature count. Captured response bodies are in [`OUTPUT.txt`](./OUTPUT.txt).

The reported latency is from one in-process test-client request, not a network or load benchmark.

## Conclusion

The API connects a trained classifier to a JSON prediction endpoint and rejects malformed input. A health route supports basic service checks.
