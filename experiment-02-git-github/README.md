# Practical 02 | Git Version Control and Collaboration

**Focus:** repository setup, commits, branching, merging, conflict resolution and remote collaboration.

## Aim

Use Git to maintain a clear history of an ML project and safely integrate work from separate branches.

## Requirements

- Git installed and available in the terminal.
- Optional: a GitHub or GitLab account and an empty remote repository for online collaboration.

## Procedure

1. Open this folder in a terminal and verify `git --version`.
2. Read [`commands.txt`](./commands.txt) for the core repository, commit and branch commands.
3. Run the repeatable conflict exercise in an isolated temporary repository:

   ```powershell
   .\run_demo.ps1
   ```

4. For online collaboration, create a feature branch in your own GitHub/GitLab project, push it with `git push -u origin <branch>`, and open a pull/merge request. Do not use this step to overwrite another person's repository.

Example inspection commands:

```powershell
git status
git log --oneline --graph --decorate
git branch
git remote -v
```

## Observed result

The recorded demonstration created a feature branch and a main-branch change, produced a content conflict, resolved it, and finished with a clean local repository. See [`OUTPUT.txt`](./OUTPUT.txt). The script creates and removes a temporary repository; it does not alter the submitted repository.

## Conclusion

Commits preserve checkpoints, branches isolate changes, and merges bring work together. A remote is needed for collaboration across machines; the captured conflict exercise itself was local.
