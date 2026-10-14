# Experiment 2 — Git and GitHub Collaboration

## Aim
Practice repository setup, commits, branching, merging, history, conflict resolution and remote collaboration.

## Commands (run in a separate practice folder or this project after reviewing files)
```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git init
git status
git add README.md
git commit -m "Initial commit"
git switch -c feature/documentation
# edit a file, then:
git add README.md
git commit -m "Update documentation"
git switch main
git merge feature/documentation
git log --oneline --graph --all
```
If the default branch is named `master`, replace `main` with `master` or rename it using `git branch -M main`.

## Safe merge-conflict exercise
Create a temporary repo, make two branches edit the same line, merge one branch into the other, inspect `git status`, resolve conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), then `git add` and `git commit`. Do not intentionally break the submitted project files.

## GitHub collaboration
Create an empty GitHub repository, add its URL with `git remote add origin YOUR_REPOSITORY_URL`, then push your branch. Never put passwords or access tokens in source files.

## Result
Git is checked by `verify_environment.py`. Actual merge and remote push results depend on running the commands in your own Git environment and account; they are not claimed as completed here.
