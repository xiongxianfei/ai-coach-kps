#!/usr/bin/env python3
"""Read-only checks of the local planning convention, not learning or prerequisites."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any

SCHEMA = 'two-level-learning-plan-v1'


def inspect_plan(value: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings = ['Structure only: no subject accuracy, learner competence, prerequisite truth or intervention effect is established.']
    counts: dict[str, int] = {}
    if not isinstance(value, dict):
        return {'ok': False, 'errors': ['plan: expected an object'], 'warnings': warnings, 'counts': counts}
    root_fields = {'schema','record_kind','plan_id','version','sources','panorama','goal','goal_map',
                   'prerequisite_hypotheses','learning_stages','learner_agreement','agreement_evidence','revision_log'}
    for k in sorted(root_fields - value.keys()): errors.append(f'plan: missing {k}')
    for k in sorted(value.keys() - root_fields): errors.append(f'plan: unsupported field {k}')
    if value.get('schema') != SCHEMA: errors.append('plan: unsupported schema')
    kind = value.get('record_kind')
    if not isinstance(kind,str) or kind not in {'template','proposed_plan','constructed_example'}: errors.append('plan: invalid record_kind')
    template = kind == 'template'
    if template: warnings.append('Blank/template fields are not a usable completed plan or an observed outcome.')

    def text(x: Any, path: str, optional: bool = False) -> None:
        if optional and x is None: return
        if not isinstance(x, str) or not x.strip(): errors.append(path + ': expected nonempty text')

    def number(x: Any, path: str) -> None:
        if type(x) is not int or x < 1: errors.append(path + ': expected positive integer')

    def obj(x: Any, fields: set[str], path: str) -> dict:
        if not isinstance(x, dict): errors.append(path + ': expected object'); return {}
        for k in sorted(fields - x.keys()): errors.append(path + ': missing ' + k)
        for k in sorted(x.keys() - fields): errors.append(path + ': unsupported field ' + k)
        return x

    def array(x: Any, path: str) -> list:
        if not isinstance(x, list): errors.append(path + ': expected list'); return []
        return x

    def strings(x: Any, path: str, required: bool = False) -> list[str]:
        xs = array(x, path)
        for i, item in enumerate(xs): text(item, f'{path}[{i}]')
        good = [t for t in xs if isinstance(t, str) and t.strip()]
        if len(set(good)) != len(good): errors.append(path + ': duplicate references')
        if required and not good: errors.append(path + ': cannot be empty')
        return good

    def items(x: Any, fields: set[str], path: str, required: bool = False) -> tuple[list[dict], dict[str,dict]]:
        rows = [obj(e, fields, f'{path}[{i}]') for i,e in enumerate(array(x, path))]
        ids: dict[str,dict] = {}
        for i, row in enumerate(rows):
            ident = row.get('id'); text(ident, f'{path}[{i}].id')
            if not isinstance(ident,str) or not ident.strip(): continue
            if ident in ids: errors.append(path + ': duplicate id ' + ident)
            ids[ident] = row
        if required and not rows: errors.append(path + ': cannot be empty')
        return rows, ids

    def refs(xs: Any, ids: dict, path: str, required: bool = False) -> list[str]:
        result = strings(xs, path, required)
        for item in result:
            if item not in ids: errors.append(path + ': unknown id ' + item)
        return result

    text(value.get('plan_id'), 'plan_id', template)
    number(value.get('version'), 'version')
    sources, source_ids = items(value.get('sources'), {'id','citation','locator','access_status'}, 'sources')
    for row in sources:
        text(row.get('citation'),'source.citation');text(row.get('locator'),'source.locator')
        if not isinstance(row.get('access_status'),str) or row.get('access_status') not in {'inspected','uninspected','constructed'}: errors.append('source: invalid access_status')

    def support(row: dict, path: str) -> None:
        state = row.get('source_status')
        if not isinstance(state,str) or state not in {'unverified','source_supported','constructed'}: errors.append(path + ': invalid source_status')
        links = refs(row.get('source_refs'), source_ids, path + '.source_refs', state=='source_supported')
        if state == 'source_supported':
            for ident in links:
                if ident in source_ids and source_ids[ident].get('access_status') != 'inspected':
                    errors.append(path + ': source_supported requires an inspected source declaration')

    panorama = obj(value.get('panorama'),{'subject','orientation_question','boundary','regions','relations','omissions'},'panorama')
    for k in ('subject','orientation_question','boundary'):text(panorama.get(k),'panorama.'+k,template)
    regions, region_ids = items(panorama.get('regions'),{'id','label','purpose','source_refs','source_status'},'panorama.regions',not template)
    for row in regions:
        text(row.get('label'),'region.label');text(row.get('purpose'),'region.purpose');support(row,'region')
    strings(panorama.get('omissions'),'panorama.omissions')

    goal = obj(value.get('goal'),{'capability','context','success_criterion','allowed_resources','panorama_region_ids'},'goal')
    for k in ('capability','context','success_criterion'):text(goal.get(k),'goal.'+k,template)
    strings(goal.get('allowed_resources'),'goal.allowed_resources')
    refs(goal.get('panorama_region_ids'),region_ids,'goal.panorama_region_ids',not template)
    gmap = obj(value.get('goal_map'),{'focus_question','concepts','relations','deferred'},'goal_map')
    text(gmap.get('focus_question'),'goal_map.focus_question',template)
    nodes, node_ids = items(gmap.get('concepts'),{'id','label','panorama_region_ids','source_refs','source_status'},'goal_map.concepts',not template)
    for row in nodes:
        text(row.get('label'),'concept.label');support(row,'concept')
        refs(row.get('panorama_region_ids'),region_ids,'concept.panorama_region_ids',True)
    strings(gmap.get('deferred'),'goal_map.deferred')
    for group, ids, location in [(panorama,region_ids,'panorama'),(gmap,node_ids,'goal_map')]:
        relations = array(group.get('relations'), location+'.relations')
        if location=='goal_map' and not template and not relations:errors.append('goal_map.relations: at least one proposition is required')
        for i, entry in enumerate(relations):
            row=obj(entry,{'source','relation','target','source_status','source_refs'},f'{location}.relations[{i}]')
            text(row.get('relation'),location+'.relation')
            for endpoint in ('source','target'):
                endpoint_value=row.get(endpoint)
                if not isinstance(endpoint_value,str) or endpoint_value not in ids:errors.append(location+'.relation: unknown '+endpoint)
            support(row,location+'.relation')
        # Conceptual cycles are permitted. They are NOT instructional prerequisite edges.

    prereqs, prereq_ids = items(value.get('prerequisite_hypotheses'),{'id','from_concept','to_concept','kind','status','rationale','probe','evidence_refs'},'prerequisite_hypotheses')
    for row in prereqs:
        for k in ('from_concept','to_concept'):
            if not isinstance(row.get(k),str) or row[k] not in node_ids:errors.append('prerequisite: unknown '+k)
        if not isinstance(row.get('kind'),str) or row.get('kind') not in {'required_for_task','helpful','corequisite'}: errors.append('prerequisite: invalid kind')
        if not isinstance(row.get('status'),str) or row.get('status') not in {'proposed','supported','rejected'}: errors.append('prerequisite: invalid status')
        for k in ('rationale','probe'):text(row.get(k),'prerequisite.'+k)
        strings(row.get('evidence_refs'),'prerequisite.evidence_refs',row.get('status')=='supported')

    stage_fields={'id','order','capability','concept_ids','prerequisite_ids','requires_stage_ids','dependency_rationale','activity','allowed_help','check','adaptation_trigger'}
    stages, stage_ids = items(value.get('learning_stages'),stage_fields,'learning_stages',not template)
    edges: dict[str,list[str]] = {}
    orders=[]
    for row in stages:
        number(row.get('order'),'stage.order')
        if type(row.get('order')) is int: orders.append(row['order'])
        for k in ('capability','activity','adaptation_trigger'):text(row.get(k),'stage.'+k)
        refs(row.get('concept_ids'),node_ids,'stage.concept_ids',True)
        for ident in refs(row.get('prerequisite_ids'),prereq_ids,'stage.prerequisite_ids'):
            if ident in prereq_ids and prereq_ids[ident].get('status')=='rejected':errors.append('stage: rejected prerequisite still used')
        deps=refs(row.get('requires_stage_ids'),stage_ids,'stage.requires_stage_ids')
        if isinstance(row.get('id'),str):edges[row['id']]=deps
        text(row.get('dependency_rationale'),'stage.dependency_rationale',not deps)
        strings(row.get('allowed_help'),'stage.allowed_help')
        check=obj(row.get('check'),{'task','criterion','allowed_resources'},'stage.check')
        text(check.get('task'),'check.task');text(check.get('criterion'),'check.criterion');strings(check.get('allowed_resources'),'check.allowed_resources')
        for dep in deps:
            if dep in stage_ids and type(stage_ids[dep].get('order')) is int and type(row.get('order')) is int and stage_ids[dep]['order']>=row['order']:
                errors.append('stage: required predecessor is not earlier in proposed order')
    if sorted(orders)!=list(range(1,len(stages)+1)):errors.append('stages: order must be consecutive and unique')
    pending=set(stage_ids);done=set()
    while pending:
        ready={ident for ident in pending if all(d in done or d not in stage_ids for d in edges.get(ident,[]))}
        if not ready:errors.append('stages: circular required-before dependency');break
        pending-=ready;done|=ready
    agreement=value.get('learner_agreement')
    if not isinstance(agreement,str) or agreement not in {'not_recorded','agreed','needs_revision'}:errors.append('learner_agreement: invalid state')
    text(value.get('agreement_evidence'),'agreement_evidence',agreement!='agreed')
    for i,entry in enumerate(array(value.get('revision_log'),'revision_log')):
        row=obj(entry,{'from_version','to_version','change','reason','basis','evidence_refs','affected_stage_ids'},f'revision_log[{i}]')
        for k in ('from_version','to_version'):number(row.get(k),'revision.'+k)
        if type(row.get('from_version')) is int and type(row.get('to_version')) is int and row['from_version']>=row['to_version']:errors.append('revision: version must increase')
        if type(row.get('to_version')) is int and type(value.get('version')) is int and row['to_version']>value['version']:errors.append('revision: version exceeds current plan')
        for k in ('change','reason'):text(row.get(k),'revision.'+k)
        if not isinstance(row.get('basis'),str) or row.get('basis') not in {'learner_choice','source_review','performance_evidence'}:errors.append('revision: invalid basis')
        strings(row.get('evidence_refs'),'revision.evidence_refs',row.get('basis')=='performance_evidence')
        # Retired stage IDs can appear here; the log preserves rather than deletes history.
        strings(row.get('affected_stage_ids'),'revision.affected_stage_ids')
    counts.update(regions=len(regions),concepts=len(nodes),stages=len(stages),prerequisite_hypotheses=len(prereqs))
    return {'ok':not errors,'errors':errors,'warnings':warnings,'counts':counts}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('record',type=Path);args=parser.parse_args()
    try:result=inspect_plan(json.loads(args.record.read_text(encoding='utf-8')))
    except (OSError,ValueError) as exc:result={'ok':False,'errors':[str(exc)],'warnings':[],'counts':{}}
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['ok'] else 1

if __name__=='__main__':raise SystemExit(main())
