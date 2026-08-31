#!/usr/bin/env python3
"""System-wide cross-worker quality regression for baseline 2.6.x.

This suite protects architecture-level guarantees shared by the original W01-W09
contracts. W10 is covered by the additive metrology suite. Expected case count: exactly 30.
"""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; CASES=[]
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))
profile=read('policies/SYSTEM_WIDE_QUALITY_PROFILE.md'); builder=read('tools/build_install_package.py')
workflow=(ROOT.parent.parent/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml').read_text(encoding='utf-8')
workers=['W01_ACADEMIC_CONTENT','W02_TIME_CLOCK','W03_WEIGHT_SCALE','W04_LENGTH_DISTANCE','W05_TEMPERATURE_CAPACITY_VOLUME','W06_MONEY_CALENDAR_DATA','W07_INSTRUMENT_AUDITOR','W08_LAYOUT_RENDER_THAI','W09_QA_RELEASE']
for wid in workers:
    txt=read(f'workers/{wid}.md'); has_qa='_QA`' in txt or 'QA is conjunctive' in txt
    add(f'worker-contract-{wid}',f'WORKER_ID={wid}' in txt and '## ACCEPTS' in txt and '## OWNS' in txt and '## RETURNS' in txt and '## MUST_NOT_DECIDE' in txt and has_qa)
for token in ['SYSTEM_OWNERSHIP_INTEGRITY_QA','SYSTEM_PARAMETER_PROVENANCE_QA','SYSTEM_INDEPENDENT_ORACLE_QA','SYSTEM_ITEM_COUNT_QA','SYSTEM_DIFFICULTY_FIDELITY_QA','SYSTEM_TARGET_DISTRIBUTION_QA','SYSTEM_VISIBILITY_ISOLATION_QA','PROMPT_RENDER_STATE_SERIALIZATION_QA','PROMPT_PAGE_POLICY_WORDING_QA','SYSTEM_FINAL_PROMPT_SELF_CONTAINED_QA','PROMPT_QA_EVIDENCE_CONSISTENCY_QA','SYSTEM_PHASE_BOUNDARY_QA']:
    add(f'profile-{token}',token in profile)
checks=[
('builder-shared-profile-path','policies/SYSTEM_WIDE_QUALITY_PROFILE.md' in builder),
('builder-shared-profile-main','MANDATORY SYSTEM-WIDE QUALITY PROFILE' in builder),
('builder-shared-profile-workers','SHARED_PROFILES' in builder and 'effective_sources=[*SHARED_PROFILES,*sources]' in builder.replace(' ','')),
('builder-system-gate','system_wide_quality_regression_suite.py' in builder),
('builder-current-total','1075/1075 PASS' in builder),
('workflow-system-gate','System-wide quality regression' in workflow),
('workflow-30-cases','30 cases' in workflow),
('profile-atomic-block','Atomic renderer-state serialization' in profile),
('profile-no-hard-page-drift','ONE_PAGE_LOCK=OFF' in profile and 'Hard one-page wording is forbidden' in profile),]
for n,o in checks:add(n,o)
assert len(CASES)==30,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'SYSTEM-WIDE QUALITY REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    [print('FAIL',n,d) for n,_,d in failed]; sys.exit(1)
print('SYSTEM-WIDE QUALITY REGRESSION: PASS'); print('cases: 30'); print('pass: 30'); print('fail: 0'); print('cross-worker architecture quality: 30/30 PASS'); print('artifact QA: NOT_YET_TESTED')
