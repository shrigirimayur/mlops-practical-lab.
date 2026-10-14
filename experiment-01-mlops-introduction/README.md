# Experiment 1 — Introduction to MLOps

## Aim
Compare software development, DevOps and MLOps; explain lifecycle, components, production challenges and tool choices.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. Read the comparison in this README and identify the model/data artifacts that must be versioned.
2. Draw the lifecycle from problem definition through monitoring and retraining.
3. Map each stage to tools in the table below.
4. Review the Mermaid lifecycle diagram in [`mlops-lifecycle.mmd`](./mlops-lifecycle.mmd).


## Example commands and notes
| Stage | Example tools | Purpose |
|---|---|---|
| Source versioning | Git/GitHub | Track code |
| Data versioning | DVC | Track datasets |
| Experiment tracking | MLflow | Compare runs |
| Feature management | Feast | Reuse features |
| Testing/CI | pytest/GitHub Actions | Automated checks |
| Packaging/serving | Docker/Flask | Deployment |


## Observed result
The lifecycle demonstration ran successfully. The captured terminal output is in [`OUTPUT.txt`](./OUTPUT.txt); the lifecycle diagram is a conceptual workflow reference.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
The lifecycle reference identifies data, code, feature, model, and monitoring responsibilities across the ML lifecycle.

## Outcome summary
The workflow diagram and tool comparison provide a structured overview of an MLOps system.
