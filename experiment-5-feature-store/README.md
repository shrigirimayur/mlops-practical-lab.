# Experiment 5 — Feature Store Fundamentals

## Aim
Demonstrate feature definitions, ingestion, retrieval and reuse with a simple local SQLite offline feature store.

## Design
- `features` table stores entity ID, feature name, value and event timestamp.
- `feature_store.py` ingests computed features from the Experiment 4 CSV into SQLite.
- Query examples retrieve features for an entity and support repeatable reuse by downstream models.
- This is a teaching demo, not a production feature-store service: no online low-latency serving, access control, distributed consistency or point-in-time joins are implemented.

## Run
```bash
python experiment-5-feature-store/feature_store.py
```

## Online vs offline
- **Offline store:** historical/batch features for training and analytics, commonly stored in data warehouses or object storage.
- **Online store:** low-latency latest feature values for real-time inference.
- Shared definitions and consistent transformation logic help reduce training-serving skew and duplicate feature work.

## Result
The script creates a local SQLite database, inserts the generated customer features, reads them back, and prints the retrieved records.
