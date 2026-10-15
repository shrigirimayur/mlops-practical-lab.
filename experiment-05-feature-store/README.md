# Practical 05 | Feature Management with Feast

**Focus:** feature definitions, registration, ingestion, historical retrieval, online retrieval and reuse.

## Aim

Define shared model features in Feast and demonstrate how the same feature definitions support historical training data and online inference.

## Requirements

- Python 3.10 or later
- Install this practical's dependencies: `python -m pip install -r requirements.txt`
- Included sample Parquet data; local Feast provider and SQLite online store.

## Procedure

From this folder:

```powershell
python -m pip install -r requirements.txt
Set-Location feast_repo\feature_repo
python test_workflow.py
```

The workflow applies the repository's feature definitions, retrieves historical features for training and batch scoring, materializes the batch feature view into the local online store, reads online features through direct and service-based requests, then pushes a fresh event and reads the updated online values.

## Observed result

Feast applied the definitions, returned historical features for three drivers and retrieved online values. The push-source feature service initially returns `None` because it has no pushed rows yet; after the script pushes a new event, driver `1001` returns the updated values. The second entity has no pushed update. The complete captured run is in [`OUTPUT.txt`](./OUTPUT.txt).

Feast prints a non-fatal notice that on-demand feature views are experimental. This local workflow completed successfully.

## Implementation files

- [`feature_store.yaml`](./feast_repo/feature_repo/feature_store.yaml): local provider and SQLite configuration.
- [`feature_definitions.py`](./feast_repo/feature_repo/feature_definitions.py): entity, feature views, request-time transformations, feature services and labels.
- [`data/`](./feast_repo/feature_repo/data/): sample offline feature data.

## Conclusion

A feature store centralizes feature definitions and retrieval so training and serving can use consistent feature logic. This practical uses local files and SQLite; it is not a production or shared feature service.
