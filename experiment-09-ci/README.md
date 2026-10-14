# Experiment 9 — Continuous Integration with GitHub Actions

## Aim
Create a CI workflow that installs dependencies and runs automated tests on pushes and pull requests.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. Review `.github/workflows/ci.yml`.
2. Commit and push the workflow to GitHub.
3. Open the repository Actions tab.
4. Inspect each step and save the actual run URL.
5. Fix any dependency or test failure and rerun.


## Example commands and notes
Expected workflow stages (illustrative): checkout → set up Python → install dependencies → run pytest. The actual status is only known after a real GitHub Actions run.


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
CI automates checkout, dependency installation, and tests on configured repository events.

## Outcome summary
The GitHub Actions workflow file is included. Its actual status becomes available after a real workflow run.
