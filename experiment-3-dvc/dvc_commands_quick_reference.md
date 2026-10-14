# DVC command quick reference

```bash
python -m pip install -r requirements.txt
git init
dvc init
dvc remote add -d localstorage .dvc/storage
dvc repro
dvc dag
dvc status
dvc push
dvc pull
```

`dvc init` is run only once per repository. The included runner performs initialization/configuration where possible. If `dvc remote add` reports that `localstorage` already exists, inspect `dvc remote list` and continue with the configured remote. For Git metadata, use `git status`, then commit `.dvc/config`, `dvc.yaml`, `dvc.lock`, and any `.dvc` pointer files that DVC creates. Do not commit `.dvc/cache`.
