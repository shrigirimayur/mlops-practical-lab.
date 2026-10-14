# Experiment 3 — Data Version Control (DVC)

## Aim
Use DVC to define a reproducible pipeline and track generated data artifacts without placing large data files directly in Git history.

## Why the earlier local Python run was not DVC
A Python script can create a CSV, but that alone does not execute DVC. DVC is a separate command-line application. A genuine demonstration must show commands such as `dvc --version`, `dvc repro`, `dvc status`, `dvc dag`, and `dvc push` executing successfully. This project includes a runner for those real commands; it does not manufacture their output.

## Procedure
From the project root:
```bash
python -m pip install -r requirements.txt
python scripts/run_dvc_practical.py
```
The runner initializes DVC, configures a local directory as the DVC remote, executes the stages in `dvc.yaml`, displays status and DAG, then pushes tracked outputs to the local remote. The first run may ask Git to be initialized; run `git init` in the project root first if required.

## What to show the teacher
1. `dvc --version` — proves the CLI is installed.
2. `dvc dag` — shows the pipeline dependency graph.
3. `dvc repro` — executes/reuses stages according to dependency changes.
4. `dvc status` — checks whether outputs are up to date.
5. `dvc push` — sends cached artifacts to the configured remote.
6. `dvc.yaml` and `dvc.lock` — declarative stages and locked stage details.

## Local remote vs cloud remote
This practical configures `.dvc/storage` as a local remote so it works without cloud credentials. It demonstrates DVC mechanics, but it is not an off-device backup. For team collaboration, configure a shared remote (for example an organization-approved S3/GDrive/Azure/SSH target) and ensure all collaborators have access.

## Expected outcome
A successful real run produces `.dvc/`, `dvc.lock`, tracked outputs and DVC CLI output. The evidence folder deliberately does not contain a fabricated DVC success log.
