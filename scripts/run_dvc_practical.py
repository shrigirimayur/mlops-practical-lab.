"""Initialize and run the real DVC pipeline. Requires the DVC CLI installed."""
from pathlib import Path
import shutil, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
def run(args, check=True):
    print('\n$ ' + ' '.join(args), flush=True)
    return subprocess.run(args, cwd=ROOT, check=check, text=True)
if shutil.which('dvc') is None:
    print('ERROR: DVC CLI was not found. Install dependencies first:', file=sys.stderr)
    print('  python -m pip install -r requirements.txt', file=sys.stderr)
    print('Then reopen the terminal and run: python scripts/run_dvc_practical.py', file=sys.stderr)
    sys.exit(2)
# Ensure generated source data exists before DVC starts its stages.
run([sys.executable, 'scripts/generate_dataset.py'])
if not (ROOT / '.git').exists():
    run(['git', 'init'])
if not (ROOT / '.dvc').exists():
    run(['dvc', 'init'])
# A local remote makes the experiment self-contained and does not require cloud credentials.
run(['dvc', 'remote', 'add', '-d', 'localstorage', '.dvc/storage'], check=False)
run(['dvc', 'repro'])
run(['dvc', 'status'])
run(['dvc', 'dag'])
run(['dvc', 'push'])
print('\nPASS: DVC pipeline completed. The commands above are actual DVC CLI output.')
print('Note: to version DVC metadata in Git, run: git add .dvc/config dvc.yaml dvc.lock .gitignore && git commit -m "Track data pipeline with DVC"')
