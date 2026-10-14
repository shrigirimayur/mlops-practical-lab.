# Experiment 2 — Git and GitHub Version Control

## Aim
Install/configure Git, create commits and branches, merge changes, resolve a merge conflict, and share the repository.

## Requirements
- Git

## Procedure
1. Verify `git --version`.
2. Configure `user.name` and `user.email` for this repository or globally.
3. Run `git init`, `git add`, and `git commit` in a new project repository.
4. Create a feature branch, edit a file, commit, and merge it.
5. Create and resolve a controlled conflict in a disposable test repository; do not create a conflict in your submitted project.
6. Push to the GitHub repository and confirm the commit appears remotely.

For repository-only identity configuration, run `git config user.name "Your Name"` and `git config user.email "you@example.com"` from the repository root. Use `--global` only if you intend to use that identity for all repositories on this computer.

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

Set a repository-specific identity with `git config user.name` and `git config user.email`. Avoid `--global` if you only want to configure this repository. GitHub authentication should use Git Credential Manager or another approved credential helper.


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
Git branch/merge/conflict behaviour is demonstrated locally. Remote collaboration requires a GitHub account and authenticated remote.
