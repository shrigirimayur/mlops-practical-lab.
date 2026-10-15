# Experiment 1 — Introduction to MLOps

## Aim
Compare software development, DevOps and MLOps; explain lifecycle, components, production challenges and tool choices.

## Procedure
1. Run `python workflow_demo.py` from this folder.
2. Review the lifecycle diagram in [`mlops-lifecycle.mmd`](./mlops-lifecycle.mmd).
3. Connect each lifecycle stage to the tools listed below.

| Stage | Example tool | Purpose |
|---|---|---|
| Source versioning | Git | Track code changes |
| Data versioning | DVC | Track datasets |
| Experiment tracking | MLflow | Compare model runs |
| Feature management | Feast | Reuse model features |
| Testing and CI | pytest, GitHub Actions | Detect regressions |
| Packaging and serving | Docker, Flask | Deploy predictions |

| Approach | Main artifact | Typical change | Operations focus |
|---|---|---|---|
| Software development | Source code | Feature or bug fix | Build and release software |
| DevOps | Code and infrastructure | Application release | Automate integration, delivery, and service operations |
| MLOps | Code, data, features, and model | Code, data, or model update | Reproducibility, deployment, monitoring, and retraining |

Production ML systems can experience changing data distributions, training-serving skew, non-reproducible experiments, weak model/data lineage, delayed ground truth, and increased compute needs. MLOps tools solve different parts of these problems; no single tool covers the entire lifecycle.

The lifecycle diagram connects problem definition, data preparation, training/evaluation, deployment, monitoring, and retraining.

## Observed result
The lifecycle demonstration ran successfully. The captured terminal output is in [`OUTPUT.txt`](./OUTPUT.txt); the lifecycle diagram is a conceptual workflow reference.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
The lifecycle reference identifies data, code, feature, model, and monitoring responsibilities across the ML lifecycle.

## Outcome summary
The output lists six lifecycle stages. No third-party Python package is required.
