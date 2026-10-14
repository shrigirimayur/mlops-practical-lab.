# Experiment 2 — Git and GitHub Version Control

## Aim
Install/configure Git, create commits and branches, merge changes, resolve a merge conflict, and share the repository.

## Requirements
- Python 3.10+ for Python examples
- Relevant tool listed in the procedure
- Work from the repository root unless stated otherwise

## Procedure
1. Verify `git --version`.
2. Configure `user.name` and `user.email` for this repository or globally.
3. Run `git init`, `git add`, and `git commit`.
4. Create a feature branch, edit a file, commit, and merge.
5. Create a controlled conflict in a test file and resolve it.
6. Push to a GitHub repository you own.

For repository-only identity configuration, run `git config user.name "Your Name"` and `git config user.email "you@example.com"` from the repository root. Use `--global` only if you intend to use that identity for all repositories on this computer.

## Example commands and notes
```bash
git --version
git config user.name "Your Name"
git config user.email "you@example.com"
git init
git status
git add .
git commit -m "Add initial practical files"
git switch -c feature/docs
git switch main
git merge feature/docs
git log --oneline
git remote -v
```

Run Git operations from the project root. To publish this project as its own repository, follow [`UPLOAD_TO_GITHUB.md`](../UPLOAD_TO_GITHUB.md) and use a dedicated GitHub repository; do not initialize Git from a parent folder that contains unrelated files.


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
Commits capture checkpoints, branches isolate work, and merges integrate changes. Conflicts are resolved by editing the final file and committing it.

## Outcome summary
The Git procedure and command checklist are documented. Remote operations require the user's own GitHub repository and credentials.
