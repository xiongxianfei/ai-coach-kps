"""One-time exact-file transfer and validation; not part of the published KPS."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import lzma
import os
import shutil
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PIN = '9432f1ee86f641d01444038cc81b7efa596b75dc'
COMPRESSED = 'a1b15ea0776fcbb8ae9925b81d8cf3c1fdaac94900d293c94a7e56c64974f31a'
RAW = '9d7c7d9bbc13f85bbe67866c5de67e9ef83cf044f50ff38e11ee669bc1f3a60e'
UPSTREAM_FILES = {'AUTHORING.md', 'TEMPLATES.md', 'LICENSE', 'validate.py', 'test_validate.py'}
ROOT_FILES = {'README.md', 'AGENTS.md', 'ALIGNMENT.md', 'CHANGELOG.md', 'CHECKS.md', 'COMPATIBILITY.md', 'CONTRIBUTING.md', 'DIAGRAMS.md', 'EVIDENCE-MAP.md', 'INDEX.md', 'NAVIGATION.md', 'NOTICE.md', 'PRACTICE-MAP.md', 'RECORDS.md', 'REVIEW-QUEUE.md', 'REVIEW.md', 'SCOPE.md', 'TERMINOLOGY-MAP.md', 'WORKED-EXAMPLE.md', 'publication.json', 'upstream-lock.json', 'knowledge-graph.json', 'summary-dependencies.json', '.gitignore'}
FOLDERS = {'concepts','principles','models','methods','practices','references','tools','tests','data'}
if os.environ.get('GITHUB_REPOSITORY') != 'xiongxianfei/ai-coach-kps' or os.environ.get('GITHUB_REF') != 'refs/heads/feat/adult-learning-coaching':
    raise SystemExit('Refusing to materialize outside the authorized implementation branch')
os.chdir(ROOT)
blob = b''.join((ROOT/'.coach-build'/f'part{i}').read_bytes() for i in range(6))
if hashlib.sha256(blob).hexdigest() != COMPRESSED:
    raise SystemExit('Compressed transfer digest mismatch')
raw = lzma.decompress(blob)
if hashlib.sha256(raw).hexdigest() != RAW:
    raise SystemExit('Authored content digest mismatch')
files = json.loads(raw.decode('utf-8'))
if not isinstance(files, dict) or len(files) != 66:
    raise SystemExit('Unexpected payload file inventory')
for name, text in files.items():
    p = PurePosixPath(name)
    if not isinstance(text, str) or p.is_absolute() or '..' in p.parts or '\\' in name:
        raise SystemExit('Invalid payload entry')
    allowed = (len(p.parts) == 1 and name in ROOT_FILES) or (p.parts[0] in FOLDERS) or name == '.github/pull_request_template.md'
    if not allowed or '.git' in p.parts or '__pycache__' in p.parts:
        raise SystemExit('Unexpected payload path: '+name)
for name, text in files.items():
    path = ROOT/name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode('utf-8'))
print('Transferred 66 authored files with both SHA256 checks verified', flush=True)
lock = json.loads((ROOT/'upstream-lock.json').read_text(encoding='utf-8'))
if lock['commit'] != PIN or set(lock['files']) != UPSTREAM_FILES:
    raise SystemExit('Unexpected upstream declaration')
for name in sorted(UPSTREAM_FILES):
    url = f'https://raw.githubusercontent.com/xiongxianfei/knowledge-practice-system/{PIN}/{name}'
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read()
    expected = lock['files'][name]
    git_digest = hashlib.sha1(b'blob '+str(len(data)).encode('ascii')+b'\0'+data).hexdigest()
    if hashlib.sha256(data).hexdigest() != expected['sha256'] or git_digest != expected['git_blob_sha1']:
        raise SystemExit('Pinned upstream file integrity failure: '+name)
    (ROOT/name).write_bytes(data)
    print('Verified unchanged upstream file: '+name, flush=True)
# Test the intended clean publication tree, not temporary transport files.
# Workflow deletions here are NOT staged by the bot; the connector removes them later.
shutil.rmtree(ROOT/'.coach-build')
for name in ('source-snapshot.yml','materialize.yml'):
    (ROOT/'.github/workflows'/name).unlink(missing_ok=True)
commands = [
    ['python3','validate.py','.'],
    ['python3','test_validate.py'],
    ['python3','tools/check_domain.py'],
    ['python3','tools/build_navigation.py','--check'],
    ['python3','-m','unittest','discover','-s','tests','-v'],
    ['python3','tools/check_record.py','data/session-record-template.json'],
]
for command in commands:
    print('$ '+' '.join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)
print('All remote checks passed on exact authored content. No learner effectiveness is established.', flush=True)
