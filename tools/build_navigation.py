#!/usr/bin/env python3
"""Generate reader and provenance views from canonical files; never refresh dependency hashes."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import validate as v
ROLES=['practice','concept','principle','model','method']
def opener(title,take):
    return '---\nlanguage: "KPS 9.x"\npackage_version: "0.4.0"\nstatus: "draft"\n---\n\n# '+title+'\n\n## Key takeaway\n\n'+take+'\n\n## Summary\n\nGenerated view of canonical package declarations. It is a navigation and review aid, not evidence of scientific validity or learner outcomes.\n'
def collect(root):
    out=[];refs=[]
    for role in ROLES:
        for p in sorted((root/(role+'s')).glob('*.md')):
            d=v.parse(p)
            if d.meta.get('type')==role:out.append((p.relative_to(root).as_posix(),d))
    for p in sorted((root/'references').glob('*.md')):
        d=v.parse(p)
        if d.meta.get('type')=='reference':refs.append((p.relative_to(root).as_posix(),d))
    primary=json.loads((root/'publication.json').read_text(encoding='utf-8')).get('primary_practice')
    # Place the explicitly selected master first while preserving role/path order
    # for all other objects. Source meanings do not depend on display position.
    out.sort(key=lambda item: (0 if item[1].meta.get('id')==primary else 1))
    return out,refs

def generate(root=ROOT):
    root=Path(root);docs,refs=collect(root)
    def name(d):return d.meta.get('canonical_name',next(h for n,h in d.headings if n==1))
    index=opener('Knowledge index','Enter through a Practice; consult academic objects for deeper meaning and source scope.')
    for role in ROLES:
        index+='\n## '+role.capitalize()+'s\n\n'
        for p,d in docs:
            if d.meta['type']!=role:continue
            summary=' '.join(v.section(d,'Key takeaway').split())
            index+=f'- [{name(d)}](../{p}) — {summary}\n'
            if role=='practice':
                label='Self-contained master entry' if d.meta.get('orchestration_role')=='master' else 'Independent specialist entry'
                index+=f'  {label}; original KPS application, effectiveness not established.\n'
                for h in d.meta['stage_titles']:
                    index+=f'  - [{h}](../{p}#{v.slug(h)})\n'
    index+='\n## Sources and review\n\n[Source register](../references/README.md) records inspection limits. [Claim records](../data/claims.json) distinguish research premises from AI application inferences. References and owning knowledge documents state remaining inspection and explanation gaps. All authored knowledge remains provisional.\n'
    sr=opener('Source register','Every source record identifies what was inspected and what the source does not establish.')
    sr+='\n## Publications\n\n'
    for p,d in refs:sr+=f'- [{d.meta["publication"]}]({Path(p).name}) — {d.meta["access_extent"]}\n'
    sr+='\n## Rights and applicability\n\nNo external full texts, figures, audio, datasets or private learner results are bundled. General educational research and studies of particular AI systems have different application limits. Multiple records of a publication are not independent experiments. Consult each Reference for its inspection scope and applicability limits.\n'
    return {'docs/INDEX.md':index,'references/README.md':sr}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();stale=[]
    for name,text in generate().items():
        p=ROOT/name
        if not args.check:p.parent.mkdir(parents=True,exist_ok=True)
        if args.check:
            if not p.exists() or p.read_text(encoding='utf-8')!=text:stale.append(name)
        else:p.write_text(text,encoding='utf-8')
    if stale:print('Stale navigation: '+', '.join(stale));return 1
    print('Navigation '+('checked' if args.check else 'written'));return 0
if __name__=='__main__':raise SystemExit(main())
