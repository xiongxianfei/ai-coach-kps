#!/usr/bin/env python3
"""Domain source alignment and publication declarations; not scholarly or outcome certification."""
from __future__ import annotations
from pathlib import Path
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import validate as v
ALLOWED={'concept':{'definition-paraphrase'},'principle':{'scoped-empirical-finding','methodological-relationship'},'model':{'published-model-subset'},'method':{'published-procedure-summary'}}

def inspect(root=ROOT):
    root=Path(root);errors=[];docs=[]
    for role in sorted(v.CORE|{'reference'}):
        folder='references' if role=='reference' else role+'s'
        for p in sorted((root/folder).glob('*.md')):
            try:d=v.parse(p)
            except (OSError,ValueError,UnicodeError) as exc:errors.append(f'parse:{p.name}:{exc}');continue
            if d.meta.get('type')==role:docs.append(d)
    byid={d.meta.get('id'):d for d in docs}
    for d in docs:
        m=d.meta;typ=m['type'];name=d.path.name
        if typ=='reference':
            for key in ('creator','publication','publication_year','date_basis','accessed','access_extent','source_type','evidence_family'):
                if m.get(key) is None or m.get(key)=='':errors.append('reference-field:'+name+':'+key)
            if not v.section(d,'Nonclaims'):errors.append('reference-nonclaims:'+name)
            continue
        for key in ('canonical_name','version','basis_kind'):
            if not isinstance(m.get(key),str) or not m[key].strip():errors.append('knowledge-field:'+name+':'+key)
        if m.get('evidence_status')!='provisional' or m.get('status')!='draft' or m.get('reviewed') is not None:errors.append('unsupported-promotion:'+name)
        if 'provisional' not in v.section(d,'Evidence status').lower():errors.append('invisible-status:'+name)
        if typ=='practice':
            if m.get('practice_format')!='steps-first-v1':errors.append('practice-format:'+name)
            if m.get('primary_audience')!='independent adult learners':errors.append('audience:'+name)
            if 'KPS' not in m.get('basis_kind',''):errors.append('application-authorship:'+name)
            if 'not recorded' not in v.section(d,'Current practice summary').lower():errors.append('fabricated-practice-record:'+name)
            continue
        align=m.get('source_alignment')
        if not isinstance(align,list) or not align:errors.append('missing-alignment:'+name);continue
        for a in align:
            if not isinstance(a,dict):errors.append('alignment-format:'+name);continue
            ident=a.get('reference');source=byid.get(ident)
            if source is None or source.meta.get('type')!='reference':errors.append('alignment-target:'+name)
            if ident not in m.get('references',[]):errors.append('alignment-dependency:'+name)
            if a.get('relation') not in ALLOWED[typ]:errors.append('alignment-relation:'+name)
            if not isinstance(a.get('locator'),str) or not a['locator'].strip():errors.append('alignment-locator:'+name)
        if not v.section(d,'Source alignment'):errors.append('missing-visible-alignment:'+name)
        if not any('limit' in h.lower() for n,h in d.headings):errors.append('missing-limits:'+name)
    try:
        pub=json.loads((root/'publication.json').read_text())
        if pub.get('based_on_core')!='10.2.0' or pub.get('validated_with')!='9.1.0' or pub.get('kps_language')!='9.x':errors.append('version-boundary')
        if pub.get('scientific_status')!='provisional' or pub.get('independent_review') is not False:errors.append('package-review')
        lock=json.loads((root/'upstream-lock.json').read_text())
        for name,entry in lock['files'].items():
            p=root/name
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=entry['sha256']:errors.append('upstream-digest:'+name)
    except (OSError,KeyError,ValueError) as exc:errors.append('publication-lock:'+str(exc))
    for p in (root/'.github/workflows').glob('*'):
        text=p.read_text()
        if 'contents: write' in text or '--accept-reviewed-summaries' in text:errors.append('unsafe-permanent-ci:'+p.name)
    for part in ('.build','.bootstrap','.coach-build'):
        if (root/part).exists():errors.append('temporary-payload:'+part)
    try:
        claims=json.loads((root/'data/claims.json').read_text());seen=set()
        for c in claims:
            if c['id'] in seen:errors.append('duplicate-claim')
            seen.add(c['id'])
            for key in ('statement','locator','population_context','comparison','outcome','time_horizon','limits','application_inference'):
                if not isinstance(c.get(key),str) or not c[key].strip():errors.append('claim-field:'+c['id']+':'+key)
            for r in c.get('references',[]):
                if r not in byid or byid[r].meta['type']!='reference':errors.append('claim-reference:'+c['id'])
            for ident in c.get('practices',[]):
                if ident not in byid or byid[ident].meta['type']!='practice':errors.append('claim-practice:'+c['id'])
            if not c.get('references') or not c.get('practices'):errors.append('claim-empty-link:'+c['id'])
    except (OSError,ValueError,KeyError,TypeError) as exc:errors.append('claims:'+str(exc))
    return errors

def main():
    errors=inspect()
    print(json.dumps({'ok':not errors,'errors':errors,'scope':'Declared alignment and publication boundaries only; not truth or educational effectiveness.'},indent=2));return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
