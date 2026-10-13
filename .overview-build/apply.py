"""One-time branch transport of reviewed bytes; not a permanent CI operation."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import lzma
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = 'b05c164ef6ffed62a242d0e51050c90c50583f52e0f056f2124641901f07f8ce'
TEMP_WORKFLOWS = {'overview-export.yml', 'overview-materialize.yml'}
GENERATED = {'INDEX.md', 'PRACTICE-MAP.md', 'TERMINOLOGY-MAP.md',
             'references/README.md', 'REVIEW-QUEUE.md', 'EVIDENCE-MAP.md',
             'knowledge-graph.json', 'summary-dependencies.json'}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(args, cwd, text=None):
    print('$ ' + ' '.join(args), flush=True)
    result = subprocess.run(args, cwd=cwd, input=text, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(result.stdout, flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    return result.stdout

def ignore(directory, names):
    omitted = {'.git', '.overview-build', '__pycache__', '.pytest_cache'}
    if Path(directory).name == 'workflows':
        omitted.update(TEMP_WORKFLOWS)
    return [name for name in names if name in omitted]

def main():
    os.chdir(ROOT)
    compressed = b''.join((ROOT/'.overview-build'/('part'+str(i))).read_bytes()
                          for i in range(2))
    if len(compressed) != 22180 or hashlib.sha256(compressed).hexdigest() != EXPECTED:
        raise SystemExit('Transfer integrity mismatch')
    raw = lzma.decompress(compressed, memlimit=256*1024*1024)
    if len(raw) != 87815:
        raise SystemExit('Unexpected decoded payload length')
    data = json.loads(raw)
    files, patch = data['files'], data['patch']
    if not isinstance(files, dict) or len(files) != 40 or not isinstance(patch, str):
        raise SystemExit('Unexpected payload schema')
    for name, hashes in files.items():
        p = PurePosixPath(name)
        if p.is_absolute() or '..' in p.parts or '\\' in name or p.parts[0].startswith('.'):
            raise SystemExit('Unapproved content path: '+name)
        if not re.fullmatch(r'[a-f0-9]{64}', hashes['after']):
            raise SystemExit('Invalid expected digest: '+name)
        target = ROOT/name
        target.resolve().relative_to(ROOT)
        if target.is_symlink():
            raise SystemExit('Symlink target rejected: '+name)
        if hashes['before'] is None:
            if target.exists():
                raise SystemExit('Unexpected existing target: '+name)
        elif not target.is_file() or digest(target) != hashes['before']:
            raise SystemExit('Concurrent content change: '+name)
    stats = run(['git','apply','--numstat','--unidiff-zero','-'], ROOT, patch)
    patch_names = {line.split('\t',2)[2] for line in stats.splitlines() if line.strip()}
    if patch_names != set(files)-GENERATED:
        raise SystemExit('Patch coverage mismatch')
    run(['git','apply','--check','--unidiff-zero','-'], ROOT, patch)
    run(['git','apply','--unidiff-zero','-'], ROOT, patch)
    # Isolate the exact publication from temporary transport infrastructure.
    with tempfile.TemporaryDirectory(prefix='overview-check-') as tmp:
        clean = Path(tmp)/'package'
        shutil.copytree(ROOT, clean, ignore=ignore)
        run([sys.executable,'tools/build_navigation.py'], clean)
        # Reproduce the already-reviewed local baseline, then require exact hashes.
        # This one-time transport step is never added to ordinary CI.
        run([sys.executable,'validate.py','.', '--accept-reviewed-summaries'], clean)
        for name, hashes in files.items():
            if not (clean/name).is_file() or digest(clean/name) != hashes['after']:
                raise SystemExit('Approved final content mismatch: '+name)
        for args in ([sys.executable,'validate.py','.'],
                     [sys.executable,'test_validate.py'],
                     [sys.executable,'tools/check_domain.py'],
                     [sys.executable,'tools/build_navigation.py','--check'],
                     [sys.executable,'-m','unittest','discover','-s','tests','-v'],
                     [sys.executable,'tools/check_learning_plan.py','data/two-level-learning-plan-template.json'],
                     [sys.executable,'tools/check_learning_plan.py','data/two-level-learning-plan-example.json']):
            run(args, clean)
        for name in GENERATED:
            shutil.copyfile(clean/name, ROOT/name)
    for name, hashes in files.items():
        if digest(ROOT/name) != hashes['after']:
            raise SystemExit('Post-copy digest mismatch: '+name)
    run(['git','add','--',*sorted(files)], ROOT)
    print('All 40 approved files match local reviewed bytes; all checks passed.', flush=True)

if __name__ == '__main__':
    main()
