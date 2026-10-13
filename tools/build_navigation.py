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
    return '---\nlanguage: "KPS 9.x"\npackage_version: "0.2.0"\nstatus: "draft"\n---\n\n# '+title+'\n\n## Key takeaway\n\n'+take+'\n\n## Summary\n\nGenerated view of canonical package declarations. It is a navigation and review aid, not evidence of scientific validity or learner outcomes.\n'
def collect(root):
    out=[];refs=[]
    for role in ROLES:
        for p in sorted((root/(role+'s')).glob('*.md')):
            d=v.parse(p)
            if d.meta.get('type')==role:out.append((p.relative_to(root).as_posix(),d))
    for p in sorted((root/'references').glob('*.md')):
        d=v.parse(p)
        if d.meta.get('type')=='reference':refs.append((p.relative_to(root).as_posix(),d))
    return out,refs

def generate(root=ROOT):
    root=Path(root);docs,refs=collect(root);byid={d.meta['id']:(p,d) for p,d in docs+refs}
    def name(d):return d.meta.get('canonical_name',next(h for n,h in d.headings if n==1))
    index=opener('Knowledge index','Enter through a Practice; consult academic objects for deeper meaning and source scope.')
    for role in ROLES:
        index+='\n## '+role.capitalize()+'s\n\n'
        for p,d in docs:
            if d.meta['type']==role:index+=f'- [{name(d)}]({p}) — provisional.\n'
    index+='\n## Other views\n\n[Practice map](PRACTICE-MAP.md), [evidence map](EVIDENCE-MAP.md), [terminology map](TERMINOLOGY-MAP.md), [source register](references/README.md), and [review queue](REVIEW-QUEUE.md).\n'
    pm=opener('Practice map','Choose a recurring adult learning task rather than a compulsory sequence through the whole library.')
    for p,d in docs:
        if d.meta['type']!='practice':continue
        pm+='\n## '+next(h for n,h in d.headings if n==1)+'\n\n'
        pm+='[Open this Practice]('+p+'). Original KPS application; effectiveness not established.\n\n'
        for i,h in enumerate(d.meta['stage_titles'],1):pm+=f'{i}. [{h}]({p}#{v.slug(h)})\n'
    tm=opener('Academic terminology map','Names correspond to inspected academic meaning; original application sequences remain in Practices.')
    tm+='\n## Canonical library\n\n| File | Canonical name | Role | Source relationship and locator |\n|---|---|---|---|\n'
    for p,d in docs:
        if d.meta['type']=='practice':basis='KPS application synthesis; not a published intervention'
        else:
            a=d.meta['source_alignment'][0];rp,rd=byid[a['reference']]
            basis=f"[{rd.meta['creator']}]({rp}) — {a['relation']}; {a['locator']}"
        tm+=f'| [{p}]({p}) | {name(d)} | {d.meta["type"]} | {basis} |\n'
    tm+='\n## Meaning boundaries\n\nA canonical name does not certify paraphrase faithfulness or effectiveness. Pieschl\'s calibration article is not attributed to Schraw; no generic loop is labeled Zimmerman\'s model. The published-model-subset relationship is an explicit domain adaptation for academic frameworks, not a standards conformance claim.\n'
    sr=opener('Source register','Every source record identifies what was inspected and what the source does not establish.')
    sr+='\n## Publications\n\n'
    for p,d in refs:sr+=f'- [{d.meta["publication"]}]({Path(p).name}) — {d.meta["access_extent"]}\n'
    sr+='\n## Rights and applicability\n\nNo external full texts, figures, audio, datasets or private learner results are bundled. General educational research and studies of particular AI systems have different application limits. Multiple records of a publication are not independent experiments. See [source review](../REVIEW.md).\n'
    rq=opener('Review queue','Source inspection, authoring review and independent validation remain separate.')
    rq+='\n## Knowledge objects\n\n| Object | Current status | Next review need |\n|---|---|---|\n'
    for p,d in docs:
        need='Consented adult usability and outcome evaluation; source-to-AI adaptation review' if d.meta['type']=='practice' else 'Independent source-faithfulness and scope review'
        rq+=f'| [{name(d)}]({p}) | provisional | {need} |\n'
    rq+='\n## Source access priorities\n\n'
    for p,d in refs:
        if 'abstract' in d.meta['access_extent'].lower():rq+=f'- [{d.meta["creator"]}]({p}) — read missing full procedures/arguments before strengthening the current claim.\n'
    rq+='\n## No automatic promotion\n\nFile integrity, source identity and completed plans are not expert approval or actual learning. All authored knowledge remains provisional in this release.\n'
    claims=json.loads((root/'data/claims.json').read_text(encoding='utf-8'))
    evidence=opener('Evidence to Practice map','A source-supported premise and an AI coaching application are different claims.')
    evidence+='\n## Scope\n\nBounded claim records connect selected research with authored Practice decisions. This is a targeted map, not a systematic review, pooled effect-size analysis or causal model.\n'
    for c in claims:
        title=c['id'].split(':')[-1].replace('-',' ').title()
        rp,rd=byid[c['references'][0]]
        evidence+=f"\n## {title}\n\n**Source premise:** {c['statement']}\n\n[Source record]({rp}) — {c['locator']}.\n\n**Population and context:** {c['population_context']}  \n**Comparison:** {c['comparison']}  \n**Outcome and timing:** {c['outcome']}; {c['time_horizon']}.\n\n**Limit:** {c['limits']}\n\n**Authored application, not a demonstrated effect:** {c['application_inference']}\n"
    evidence+='\n## Data and review\n\n[Machine-readable claim bridge](data/claims.json). Each inference remains provisional. Different populations and designs must not be flattened into an unconditional claim about all AI learning.\n'
    graph={'format':1,'meaning':'Declared documentation dependencies, not a causal or mental-processing model.','nodes':[{'id':d.meta['id'],'path':p,'type':d.meta['type']} for p,d in docs+refs],'edges':[]}
    for p,d in docs+refs:
        for relation in v.RELATIONS:
            for target in d.meta.get(relation,[]):graph['edges'].append({'source':d.meta['id'],'relationship':relation,'target':target})
    return {'INDEX.md':index,'PRACTICE-MAP.md':pm,'TERMINOLOGY-MAP.md':tm,'references/README.md':sr,'REVIEW-QUEUE.md':rq,'EVIDENCE-MAP.md':evidence,'knowledge-graph.json':json.dumps(graph,ensure_ascii=False,indent=2)+'\n'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();stale=[]
    for name,text in generate().items():
        p=ROOT/name
        if args.check:
            if not p.exists() or p.read_text(encoding='utf-8')!=text:stale.append(name)
        else:p.write_text(text,encoding='utf-8')
    if stale:print('Stale navigation: '+', '.join(stale));return 1
    print('Navigation '+('checked' if args.check else 'written'));return 0
if __name__=='__main__':raise SystemExit(main())
