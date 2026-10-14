# MLOps Practical Lab Report

**Student:** ____________________  
**Class / Roll No.:** ____________________  
**Subject:** MLOps  
**Date:** ____________________

## Experiment 1 — Introduction to MLOps
**Aim:** Study the MLOps lifecycle, distinguish software development, DevOps and MLOps, identify production challenges and draw the lifecycle workflow.

**Key learning:** MLOps connects data and model lifecycle management with software engineering and operations. Reproducibility, versioning, automated validation/deployment and production monitoring are central.

**Result:** Workflow demonstration included. Run `python experiment-1-mlops-introduction/workflow_demo.py` to display the stages.

## Experiment 2 — Git and GitHub
**Aim:** Practice repository initialization, commits, branches, merges, history and collaboration.

**Commands practiced:** `git init`, `git add`, `git commit`, `git switch -c`, `git merge`, `git log --oneline --graph --all`, remote configuration and push.

**Result:** Instructions and environment check included. Record actual merge-conflict resolution and GitHub push output after completing them in your own repository.

## Experiment 3 — DVC
**Aim:** Track data artifacts and make ML pipeline stages reproducible using DVC.

**Procedure:** Install requirements, run `python scripts/run_dvc_practical.py`, and inspect `dvc.yaml`, `dvc.lock`, `dvc dag`, `dvc status`, `dvc repro`, and `dvc push`.

**Result:** The project contains a real executable DVC pipeline definition and runner. DVC success is not claimed until the commands execute on the student's machine. Attach the actual terminal output after running.

## Experiment 4 — Data preprocessing and feature engineering pipeline
**Aim:** Generate a sample dataset, validate and clean it, then calculate reusable features.

**Validation:** Required schema, unique customer IDs, numeric values, valid age range, nonnegative spend/visits and binary target.

**Features:** Spend per visit, high-engagement indicator and age band.

**Result:** Python stages are included and can be run directly or through DVC.

## Experiment 5 — Feature store
**Aim:** Demonstrate feature ingestion and retrieval using a local SQLite database.

**Procedure:** Run `python experiment-5-feature-store/feature_store.py`. The program inserts three feature values per customer and retrieves the values for one example entity.

**Result:** A small offline feature-store demonstration is included. It is not represented as a production online feature store.

## Overall conclusion
The five experiments demonstrate MLOps concepts, source control practices, data/version pipeline design, preprocessing and feature reuse. Python demonstrations and DVC CLI operations are separate: the DVC experiment must be run with the DVC CLI, and its actual output should be captured as evidence.

## Submission checklist
- [ ] Run Python experiments successfully.
- [ ] Run DVC setup and confirm `dvc repro`, `dvc status`, `dvc dag`, `dvc push`.
- [ ] Complete a Git branch/merge and a safe conflict-resolution exercise.
- [ ] Push the project files to your own GitHub repository.
- [ ] Add actual terminal screenshots/output requested by the teacher.
