import shutil, subprocess
print('Git executable:', shutil.which('git') or 'NOT FOUND')
if shutil.which('git'):
    r = subprocess.run(['git','--version'], text=True, capture_output=True)
    print(r.stdout.strip() or r.stderr.strip())
    print('PASS: Git command can be invoked')
else:
    print('ACTION REQUIRED: install Git from https://git-scm.com/downloads')
