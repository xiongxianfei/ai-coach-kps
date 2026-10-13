"""Apply the exact locally reviewed master Practice patch on its feature branch only."""
from pathlib import Path
import base64
import hashlib
import lzma
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BASE_TREE = '9200b901cadcd01258ebb78198b28bb99c12756f'
EXPECTED_TREE = '87ecd47ee80b376f2b56c1788f285d0b47f708b8'
COMPRESSED_SHA = 'ad8e2d835b1b9d9b2b94a39b120a2f3f799e371aa043ba4960e9029266db00a2'
PATCH_SHA = '461de1d8ce3d61dd865f09e121d48922c08d3f777d403ec4c84d4050650cfadf'

def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)

def output(*args):
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()

if output('git', 'rev-parse', 'HEAD^' + '^{tree}') != BASE_TREE:
    raise SystemExit('The staging commit is not based on the reviewed source tree.')
if output('git', 'status', '--porcelain'):
    raise SystemExit('Refusing to overwrite an unexpected dirty checkout.')
parts = sorted((ROOT / '.master-build').glob('part-*.b64'))
if [p.name for p in parts] != [f'part-{i}.b64' for i in range(1, 6)]:
    raise SystemExit('Incomplete or unexpected transfer parts.')
packed = base64.b64decode(''.join(p.read_text(encoding='utf-8') for p in parts), validate=True)
if hashlib.sha256(packed).hexdigest() != COMPRESSED_SHA:
    raise SystemExit('Compressed source integrity check failed.')
patch = lzma.decompress(packed)
if hashlib.sha256(patch).hexdigest() != PATCH_SHA:
    raise SystemExit('Decompressed source integrity check failed.')
with tempfile.TemporaryDirectory(prefix='kps-master-') as td:
    p = Path(td) / 'source.patch'
    p.write_bytes(patch)
    run('git', 'apply', '--check', str(p))
    run('git', 'apply', '--index', str(p))
# Remove all transfer infrastructure before running the permanent publication checks.
run('git', 'rm', '-r', '--', '.master-build', '.github/workflows/master-materialize.yml')
run('python3', 'tools/build_navigation.py')
# This stages already locally reviewed summaries. The exact resulting tree must match
# the approved local tree; no new source/summary is silently accepted here or in CI.
run('python3', 'validate.py', '.', '--accept-reviewed-summaries')
run('git', 'add', '-A')
actual_tree = output('git', 'write-tree')
if actual_tree != EXPECTED_TREE:
    raise SystemExit(f'Approved tree mismatch: expected {EXPECTED_TREE}; actual {actual_tree}')
for command in [
    ('python3', 'validate.py', '.'),
    ('python3', 'test_validate.py'),
    ('python3', 'tools/check_domain.py'),
    ('python3', 'tools/build_navigation.py', '--check'),
    ('python3', '-m', 'unittest', 'discover', '-s', 'tests', '-v'),
]:
    run(*command)
if output('git', 'write-tree') != EXPECTED_TREE or output('git', 'diff', '--name-only'):
    raise SystemExit('A check changed the approved files.')
print('Verified final source tree:', EXPECTED_TREE)
print('Structural and declaration tests only; no coaching efficacy or learner result claimed.')
