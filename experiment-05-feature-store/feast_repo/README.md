# Local Feast feature repository

This repository demonstrates Feast entities, feature views, historical retrieval, materialization, online retrieval, and a stream update with the local provider. It uses the sample Parquet files in `feature_repo/data/`; the registry and SQLite online store are generated locally and are not committed.

## Run the workflow

From the project root:

```powershell
Set-Location experiment-05-feature-store/feast_repo/feature_repo
feast apply
python test_workflow.py
```

The workflow output is recorded in [Experiment 5](../OUTPUT.txt). This local setup is for learning and is not a production feature service or shared store.

See the [Feast quickstart](https://docs.feast.dev/getting-started/quickstart) and [production guide](https://docs.feast.dev/how-to-guides/running-feast-in-production) for further information.