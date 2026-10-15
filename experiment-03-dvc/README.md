# Experiment 3 — Dataset Versioning with DVC

## Aim
Track a dataset, store DVC metadata in Git, configure a remote, and compare dataset versions.

## Requirements
- Python 3.10 or later
- Git and DVC installed
- Install this folder's packages with `python -m pip install -r requirements.txt`

## Procedure
1. Run `python run_demo.py` from this folder. It creates a temporary Git/DVC project and a local remote.
2. Review the generated `.dvc` metadata, push/pull output, and hash comparison printed by the script.
3. Read [`create_dataset.py`](./create_dataset.py) to see the five-row source dataset.
## Observed result
The captured DVC demonstration output is in [`OUTPUT.txt`](./OUTPUT.txt). It records a temporary local remote, not a shared cloud remote. Running the script again makes a new isolated project and does not change this assignment's Git repository.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
DVC stores data artifact metadata in the Git workflow and manages data contents in its cache/remote. A local remote is not a shared cloud remote.

## Outcome summary
Dataset tracking, DVC metadata versioning, local push/pull, and data-hash comparison are demonstrated end to end.
