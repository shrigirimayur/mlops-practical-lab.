# Experiment 5 — Feature Store and Feast

## Aim
Understand offline/online stores, define reusable features, register them, and retrieve feature values.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. Run the included SQLite demonstration from the repository root: `python experiment-05-feature-store/feature_store_demo.py`.
2. Review the feature-store concepts and distinguish this teaching example from a Feast deployment.
3. Check the current Feast quickstart and install a compatible version.
4. Initialize a feature repository.
5. Define an entity, feature view, event timestamp, and data source.
6. Apply definitions and test offline and online retrieval.
7. Record the provider and actual command output.


## Example commands and notes
```bash
python -m pip install feast
feast --version
feast init feature_repo
```

Feast commands/configuration depend on version and provider. The code in this folder is a local SQLite teaching example for the feature-store concept, not proof that Feast was configured.


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
Feature stores promote reusable feature definitions; offline retrieval is for historical training data and online retrieval is for low-latency serving.

## Outcome summary
A SQLite feature-store concept demo is included. It is explicitly distinct from a configured Feast deployment.

## Related files
- [`feature_store_demo.py`](./feature_store_demo.py) demonstrates simple local feature storage using SQLite.
- The generated SQLite database is a local artifact and is excluded from Git.
