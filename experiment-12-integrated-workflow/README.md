# Experiment 12 — Integrated MLOps Workflow

## Aim
Combine source control, data tracking, pipeline execution, experiment tracking, tests, CI, containerization and serving.

## Requirements
- Python 3.10 or later
- Git and dependencies installed from the repository-root `requirements.txt`
- Optional external tools as noted in the relevant experiments

## Procedure
1. Follow Experiments 2–11 to connect version control, data, features, training, testing, CI, packaging, and serving.
2. Compare the recorded metrics and command results; identify which components use local demonstration infrastructure.
3. Distinguish completed local integrations from unavailable infrastructure, such as a Docker daemon.
4. Review the actual end-to-end summary in [`OUTPUT.txt`](./OUTPUT.txt).


## Integrated result

The captured results show the successful local demonstrations and CI run, and explicitly identify infrastructure that was not available in the execution environment.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
The integrated workflow demonstrates how source, data, experiment, test, packaging, and serving stages can be connected while retaining traceability.

## Outcome summary
The local workflow links all twelve practicals. A Docker image was not built when Docker was unavailable; the report does not claim an unverified container deployment.

## Related files
- [Consolidated practical report](../reports/MLOps_Practical_Lab_Report.md) summarizes the twelve topics and the verified results.
