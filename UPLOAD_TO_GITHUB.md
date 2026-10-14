# Publish this project to GitHub

These steps create a **dedicated Git repository for this project**. Run every command from the `mlops-practical-lab` directory, not from its parent Desktop directory.

## 1. Create an empty GitHub repository

On GitHub, create a repository for this project. Do not initialize it with a README, license, or `.gitignore`; those files are already in this project. Copy the repository's HTTPS or SSH URL.

## 2. Initialize and review the local repository

In PowerShell, open the project directory and run:

```powershell
Set-Location "C:\path\to\mlops-practical-lab"
git init
git branch -M main
git status --short
```

Before staging, inspect the files and ensure no credentials, private data, `.env` files, local databases, or generated outputs are included.

## 3. Make the initial commit

```powershell
git add .
git status --short
git diff --cached --stat
git diff --cached
git commit -m "Add MLOps practical laboratory experiments"
```

If Git asks you to configure an author identity, set it for this repository:

```powershell
git config user.name "Your Name"
git config user.email "you@example.com"
```

Then repeat the commit command. Repository-local settings do not change your global Git identity.

## 4. Connect and push

Replace the placeholder with the URL copied from your GitHub repository:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git remote -v
git push -u origin main
```

Authenticate using Git Credential Manager or your organization's approved method. Do not put a password or personal access token in the remote URL or commit it to a file.

## 5. Verify the upload

Refresh the GitHub repository page and confirm that all twelve experiment folders, the root README, shared code, tests, and `.github/workflows/ci.yml` are present. Open the **Actions** tab and check the actual CI run status. A workflow configuration or an illustrative output file alone does not prove that CI passed.
