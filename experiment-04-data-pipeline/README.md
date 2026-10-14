# Experiment 4 — Data Collection and Processing Pipeline

## Aim
Load, validate, preprocess, engineer features and execute a repeatable data pipeline.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. Review `pipeline.py`.
2. Run the script from the repository root.
3. Check generated output and validation messages.
4. Test missing target and empty input cases.
5. Record actual row counts and feature count.


## Example commands and notes
```bash
python experiment-04-data-pipeline/pipeline.py
```

The script uses a small generated sample dataset so the basic workflow can be tested. Replace it with the dataset required by your course if needed.


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
The demonstration script validates input, splits rows, fits preprocessing on training data, and writes a processed test partition.

## Outcome summary
A runnable data pipeline is included. Output row counts are printed at runtime and depend on the selected input data.
