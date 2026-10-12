#!/usr/bin/env python3
"""Check declarations in a private learning record; never score learning or infer mastery."""
from __future__ import annotations
import argparse
from datetime import datetime
import json
from pathlib import Path

STATES={'planned','not_attempted','observed'}
PHASES={'baseline','practice','immediate_check','delayed_check','transfer_check'}
HELP={'none','hint','partial_solution','full_solution','unknown'}
BASES={'none','ai_only','source_checked','deterministic_check','human_review'}
JUDGMENTS={'not_evaluated','meets','does_not_meet','uncertain'}

def nonempty(x): return isinstance(x,str) and bool(x.strip())
def inspect_record(record):
    errors=[]; warnings=[]
    counts={x:0 for x in ('planned','not_attempted','observed','declared_independent','unchecked')}
    if not isinstance(record,dict):
        return {'ok':False,'errors':['record must be an object'],'warnings':[], 'scope':'declarations only'}
    if record.get('schema_version')!=1: errors.append('schema_version must be 1')
    if record.get('record_kind') not in {'blank_template','constructed_example','personal_observation'}:errors.append('record_kind must identify provenance')
    if record.get('mastery_decision') is not None: errors.append('mastery_decision is not supported by this record checker')
    attempts=record.get('attempts')
    if not isinstance(attempts,list): attempts=[];errors.append('attempts must be a list')
    seen=set()
    for i,a in enumerate(attempts):
        p=f'attempt {i+1}: '
        if not isinstance(a,dict):errors.append(p+'must be an object');continue
        ident=a.get('attempt_id')
        if not nonempty(ident) or ident in seen:errors.append(p+'missing or duplicate attempt_id')
        else:seen.add(ident)
        state=a.get('state'); phase=a.get('phase'); help_=a.get('answer_help'); basis=a.get('verification_basis');judgment=a.get('criterion_judgment')
        if state not in STATES:errors.append(p+'invalid state')
        else:counts[state]+=1
        if phase not in PHASES:errors.append(p+'invalid phase')
        if help_ not in HELP:errors.append(p+'invalid answer_help')
        if basis not in BASES:errors.append(p+'invalid verification_basis')
        if judgment not in JUDGMENTS:errors.append(p+'invalid criterion_judgment')
        for field in ('claimed_independent','verified'):
            if type(a.get(field)) is not bool:errors.append(p+field+' must be boolean')
        if a.get('answer_visible_during_attempt') is not None and type(a['answer_visible_during_attempt']) is not bool:errors.append(p+'answer visibility must be boolean or null')
        if a.get('same_item_seen_before') is not None and type(a['same_item_seen_before']) is not bool:errors.append(p+'prior exposure must be boolean or null')
        accommodations=a.get('access_accommodations')
        if not isinstance(accommodations,list) or any(not nonempty(x) for x in accommodations):errors.append(p+'access_accommodations must be a text list')
        if state=='observed':
            if not nonempty(a.get('original_response')):errors.append(p+'an observed response must be preserved')
            date=a.get('attempted_at')
            try:
                dt=datetime.fromisoformat(date.replace('Z','+00:00')) if isinstance(date,str) else None
                if dt is None or dt.tzinfo is None:raise ValueError('missing timezone')
            except (ValueError,TypeError):errors.append(p+'observed attempt needs an actual ISO timestamp with timezone')
            if not nonempty(record.get('task')) or not nonempty(record.get('criterion')):errors.append(p+'observed attempt needs task and criterion')
            if record.get('record_kind')=='blank_template':errors.append(p+'blank_template cannot contain observed results')
            if not a.get('verified'):counts['unchecked']+=1
        else:
            if a.get('original_response') is not None or judgment not in {None,'not_evaluated'} or a.get('verified') or a.get('feedback') is not None or a.get('revised_response') is not None:
                errors.append(p+'an unobserved or unattempted event cannot contain a performance result')
            if a.get('claimed_independent'):errors.append(p+'an unobserved event cannot be claimed independent evidence')
        if a.get('claimed_independent'):
            if help_!='none' or a.get('answer_visible_during_attempt') is not False:
                errors.append(p+'independence conflicts with help or unknown answer visibility')
            elif state=='observed':counts['declared_independent']+=1
        if a.get('verified'):
            if state!='observed' or basis not in {'source_checked','deterministic_check','human_review'} or not nonempty(a.get('verification_locator')):
                errors.append(p+'verified requires an observed result and an explicit non-AI-only verification basis')
            if judgment=='not_evaluated':errors.append(p+'verified result cannot be not_evaluated')
        elif basis=='ai_only' and state=='observed':warnings.append(p+'AI-only judgment remains unverified')
        delay=a.get('delay_days')
        if delay is not None and (type(delay) not in (int,float) or not 0<=delay<float('inf')):errors.append(p+'delay_days must be finite nonnegative or null')
        if phase=='delayed_check' and state=='observed':
            if delay is None:warnings.append(p+'actual delay unknown; timing-based retention inference is not established')
            elif isinstance(delay,(int,float)) and delay<=0:errors.append(p+'a declared delayed check needs positive actual delay')
        if phase=='transfer_check' and state=='observed' and not nonempty(a.get('context_change')):warnings.append(p+'context change unspecified; transfer interpretation remains open')
        if state=='observed' and a.get('same_item_seen_before') is None:warnings.append(p+'prior item exposure unknown')
    return {'ok':not errors,'errors':errors,'warnings':warnings,'counts':counts,'scope':'Record declarations only; not truth, correctness, clinical diagnosis, learner competence or causal effectiveness.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('record',type=Path);args=ap.parse_args()
    try:result=inspect_record(json.loads(args.record.read_text(encoding='utf-8')))
    except (OSError,UnicodeError,json.JSONDecodeError) as exc:
        print(json.dumps({'ok':False,'errors':[str(exc)],'scope':'file parsing only'}));return 2
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['ok'] else 1
if __name__=='__main__':raise SystemExit(main())
