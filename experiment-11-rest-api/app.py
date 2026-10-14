from time import perf_counter

from flask import Flask, jsonify, request
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
data = load_iris()
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(data.data, data.target)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/predict")
def predict():
    start = perf_counter()
    body = request.get_json(silent=True)
    if not isinstance(body, dict) or "features" not in body:
        return jsonify({"error": "JSON body must contain 'features'"}), 400
    features = body["features"]
    if not isinstance(features, list) or len(features) != 4:
        return jsonify({"error": "features must be a list of four numbers"}), 400
    try:
        values = [float(value) for value in features]
    except (TypeError, ValueError):
        return jsonify({"error": "all features must be numeric"}), 400
    prediction = int(model.predict([values])[0])
    latency_ms = (perf_counter() - start) * 1000
    return jsonify(
        {
            "prediction": prediction,
            "class_name": str(data.target_names[prediction]),
            "probabilities": model.predict_proba([values])[0].tolist(),
            "latency_ms": round(latency_ms, 3),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
