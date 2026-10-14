# Experiment 12 — Integrated MLOps Workflow

## Aim
Combine source control, data tracking, pipeline execution, experiment tracking, tests, CI, containerization and serving.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. Review the individual experiment instructions and identify which optional services are available.
2. Commit the source and experiment documentation to Git; do not commit credentials or local-only artifacts.
3. Generate and track the sample dataset with DVC, configure a remote, and verify the status and transfer operations.
4. Run the data-processing example and the shared test suite; record their actual outputs.
5. Run the MLflow training script and confirm the run, metrics, and artifact in the configured tracking UI.
6. Push the repository and verify the GitHub Actions run.
7. Build and start the Docker container, then test the API health and prediction endpoints.
8. Complete [`checklist.md`](./checklist.md) based on evidence from your own runs; document unavailable tools and incomplete steps.


## Example commands and notes
Run each command in its experiment guide and from the working directory stated there. The checklist starts unchecked intentionally. Mark an item complete only after verifying the corresponding artifact or external service result.


## Observation
Write what you actually observed. Include tool versions, commands, important values, errors, and how you resolved them.

## Result
State only what you completed and verified. If a tool could not be configured, document the limitation rather than claiming success.

## Output
See the `OUTPUT.txt` file in this experiment folder for the sample/expected output format. Outputs that depend on running an external tool are labelled illustrative and should not be interpreted as proof of execution.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
The integrated workflow demonstrates how source, data, experiment, test, packaging, and serving stages can be connected while retaining traceability.

## Outcome summary
An end-to-end checklist is included. It describes verification criteria; it does not claim that every external integration has been run.

## Related files
- [`checklist.md`](./checklist.md) records verification status.
- [Consolidated practical report](../MLOps_Practical_Lab_Report.md) summarizes the twelve topics.
