# MLOps Practical Laboratory — Consolidated Report

**Department:** Computer Engineering

**Experiments:** 01–12
**Execution environment:** Windows, Python 3.14.7

## Summary of verified results

| No. | Practical | Verified result |
|---:|---|---|
| 01 | MLOps lifecycle | Ran the lifecycle demonstration and reviewed the Mermaid diagram. |
| 02 | Git and GitHub | Created branches, produced and resolved a merge conflict, and verified the final local history. |
| 03 | DVC | Tracked a five-row dataset; pushed and pulled it using an isolated local DVC remote. |
| 04 | Data pipeline | Processed 10 rows into 8 training and 2 test rows with 2 features. |
| 05 | Feature store | Applied Feast definitions, retrieved historical and online features, and demonstrated a stream update using the local SQLite provider. |
| 06 | MLflow | Logged a Random Forest regression run, metrics, and a model artifact. |
| 07 | Model selection | Ran Grid Search and Random Search; both selected `C=0.1` with test F1 `0.9793`. |
| 08 | Automated tests | All 4 validation tests passed locally. |
| 09 | Continuous integration | GitHub Actions Python CI run #2 passed on commit `4e68f60`; [view run](https://github.com/shrigirimayur/mlops-practical-lab./actions/runs/38623459566). |
| 10 | Docker | Docker CLI was unavailable; no image build or container run is claimed. |
| 11 | Model API | Flask test client returned HTTP 200 for health and valid prediction requests, and HTTP 400 for invalid features. |
| 12 | Integrated workflow | Local demonstrations and CI results are summarized; the Docker limitation remains explicit. |

## Experiment 6 — MLflow metrics

**Run ID:** `86196a77bfd44613acda9a39a20a6499`

**Model:** RandomForestRegressor (`n_estimators=100`, `max_depth=6`, `random_state=42`)

| Metric | Value |
|---|---:|
| MAE | 43.53563736129633 |
| MSE | 2878.820810419161 |
| R2 | 0.45663677692410665 |

## Experiment 7 — model comparison

| Search | Best parameter | CV F1 | Test accuracy | Test F1 |
|---|---|---:|---:|---:|
| Grid Search | `model__C=0.1` | 0.9845 | 0.9737 | 0.9793 |
| Random Search | `model__C=0.1` | 0.9845 | 0.9737 | 0.9793 |

## Reproducibility and limitations

- Detailed captured outputs and commands are stored in each experiment's `OUTPUT.txt`.
- Experiment 3 used a temporary local DVC remote. It demonstrates data tracking and transfer but is not a shared cloud remote.
- Experiment 5 used Feast's local provider, sample Parquet files, a local registry, and a SQLite online store. It is not a production feature service.
- Experiment 9's GitHub Actions run passed on the pushed code revision; the run link and commit are recorded in its experiment output.
- Experiment 10 is not complete as a container build: Docker was not installed/available in the execution environment.
- Experiment 11 latency came from one in-process Flask test-client request and is not a network performance benchmark.
- Sample data and metric values are from the scripts in this repository. Re-run in the target course environment if machine-specific execution is required.

## References

- [Git](https://git-scm.com/doc)
- [DVC](https://dvc.org/doc)
- [Feast](https://docs.feast.dev/)
- [MLflow](https://mlflow.org/docs/latest/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [pytest](https://docs.pytest.org/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Docker](https://docs.docker.com/)
- [Flask](https://flask.palletsprojects.com/)
