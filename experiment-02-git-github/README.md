# Experiment 2 — Git and GitHub Version Control

## Aim
Install/configure Git, create commits and branches, merge changes, resolve a merge conflict, and share the repository.

## Requirements
- Git

## Procedure
1. Open PowerShell in this folder and run `git --version`.
2. Configure `user.name` and `user.email` for a practice repository.
3. Follow the commands in [`commands.txt`](./commands.txt) to initialize, commit, branch, merge, and inspect history.
4. Create and resolve a controlled conflict only in a disposable repository.
5. To demonstrate remote collaboration, configure your own GitHub remote and push your branch.

Git does not require Python packages. Configure `user.name` and `user.email` in the practice repository; use `--global` only if you want those settings on every repository.

## Example commands
```bash
git --version
git config user.name "Your Name"
git config user.email "you@example.com"
git init
git status
git add .
git commit -m "Add project files"
git switch -c feature/docs
git switch main
git merge --no-ff feature/docs
git log --oneline
git remote -v
```

## Captured run

[`OUTPUT.txt`](./OUTPUT.txt) records the actual branch, merge, conflict, and resolution operations performed in a disposable local Git repository.

## Result

The feature branch and main branch contained conflicting edits; Git reported a content conflict, which was resolved and committed. The final history contained both lines of work and a merge commit.

## Viva questions
1. What problem does this tool or workflow solve?
2. What is one limitation or failure mode?
3. How can the result be reproduced?


## Concept summary
Commits capture checkpoints, branches isolate work, and merges integrate changes. Conflicts are resolved by editing the final file and committing it.

## Outcome summary
Git branch, merge, and conflict resolution were demonstrated locally in a disposable repository. A GitHub remote is optional and is not represented as part of the local conflict demonstration.
