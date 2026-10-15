# Practical 03 | Dataset Versioning with DVC

**Focus:** data tracking, dataset revisions, artifact storage, Git integration and reproducibility.

## Aim

Track changes to a dataset separately from source code, store its contents in a DVC remote, compare revisions and restore a tracked version.

## Requirements

- Python 3.10 or later
- Git installed
- Install this practical's dependencies: `python -m pip install -r requirements.txt`

## Procedure

From this folder:

```powershell
python -m pip install -r requirements.txt
python run_demo.py
```

The script creates an isolated temporary Git/DVC project, tracks the initial dataset, commits its metadata, changes the dataset, tracks and commits the new revision, pushes both versions to a temporary local remote, deletes the working copy and restores it with `dvc pull`. The assignment repository is not used as the temporary demo repository.

## Observed result

The content hash changed between versions; `dvc pull` restored the six-row second version, and the temporary demo Git working tree was clean. Captured hashes and terminal results are in [`OUTPUT.txt`](./OUTPUT.txt).

**Scope:** the remote is local and temporary, not a shared cloud or team remote. Git stores DVC metadata; DVC stores the dataset contents.

## Conclusion

DVC makes data revisions reproducible alongside Git history. A shared remote is required when collaborators need access to the same data artifacts.
