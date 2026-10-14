# Experiment 3 — Dataset Versioning with DVC

## Aim
Track a dataset, store DVC metadata in Git, configure a remote, and compare dataset versions.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. Confirm the project has a Git repository, then initialize DVC from the repository root with `dvc init`.
2. From the repository root, create the sample dataset with `python experiment-03-dvc/create_dataset.py`.
3. Track it with `dvc add experiment-03-dvc/data/students.csv`.
4. Review the generated `.dvc` metadata and the dataset entry added to `.gitignore`; stage and commit both with Git.
5. Configure a local or shared DVC remote, then run `dvc push` and `dvc pull` to verify artifact storage and retrieval.
6. Modify or regenerate the dataset, track and commit the new version, then compare the `.dvc` metadata across Git revisions.
7. Record the remote type and the actual status of each command. A local remote is not cross-machine collaboration.


## Example commands and notes
```bash
python experiment-03-dvc/create_dataset.py
dvc init
dvc add experiment-03-dvc/data/students.csv
git add experiment-03-dvc/data/students.csv.dvc .gitignore .dvc
git commit -m "Track sample dataset with DVC"
dvc status
```

`dvc init` is a one-time repository setup. The sample data path is relative to the repository root. Configure a remote according to its storage provider and keep credentials out of Git; a local DVC remote is not a cloud/shared remote.


## Observed result
The captured DVC demonstration output is in [`OUTPUT.txt`](./OUTPUT.txt). It records a temporary local remote, not a shared cloud remote; the DVC objects are not presented as a persistent hosted remote.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
DVC stores data artifact metadata in the Git workflow and manages data contents in its cache/remote. A local remote is not a shared cloud remote.

## Outcome summary
The folder includes the dataset generator and DVC procedure. Actual remote transfer requires DVC to be installed and configured.

## Related files
- [`create_dataset.py`](./create_dataset.py) creates the five-row sample CSV.
- [`data/`](./data/) is the dataset location for this practical.
