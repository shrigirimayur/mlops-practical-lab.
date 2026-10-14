# API test requests

Health:
```bash
curl http://127.0.0.1:8000/health
```

Prediction (four Iris features):
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"features\":[5.1,3.5,1.4,0.2]}"
```

Invalid request:
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"features\":[1,2]}"
```
