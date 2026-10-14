"""Run Python-based demonstrations; this intentionally does not claim to run DVC."""
from pathlib import Path
import subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
commands = [
    ('Experiment 1: MLOps workflow', [sys.executable, 'experiment-1-mlops-introduction/workflow_demo.py']),
    ('Experiment 2: Git environment check', [sys.executable, 'experiment-2-git-github/verify_environment.py']),
    ('Experiment 3: dataset generation', [sys.executable, 'scripts/generate_dataset.py']),
    ('Experiment 4: preprocessing', [sys.executable, 'scripts/preprocess_data.py']),
    ('Experiment 4: feature engineering', [sys.executable, 'scripts/engineer_features.py']),
    ('Experiment 5: feature store', [sys.executable, 'experiment-5-feature-store/feature_store.py']),
]
all_ok = True
for label, cmd in commands:
    print(f'\n===== {label} =====', flush=True)
    result = subprocess.run(cmd, cwd=ROOT, text=True)
    if result.returncode:
        all_ok = False
        print(f'FAILED (exit {result.returncode})', flush=True)
    else:
        print('PASS', flush=True)
print('\nPython experiment status:', 'PASS' if all_ok else 'FAIL')
sys.exit(0 if all_ok else 1)
