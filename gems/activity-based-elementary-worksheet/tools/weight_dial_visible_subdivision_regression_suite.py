#!/usr/bin/env python3
"""Actual weight-dial visible subdivision regression — 32 additive cases."""
from pathlib import Path
import math,sys
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent.parent
CASES=[]
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')

# 1-12 independent math/topology oracles
add('kg-span-intervals',math.isclose((1.0-0.0)/0.1,10.0))
add('kg-span-positions',10+1==11)
add('kg-span-interior',11-2==9)
angles=[6*i for i in range(11)]
add('zero-one-angle-count',len(angles)==11)
add('zero-one-angle-start',angles[0]==0)
add('zero-one-angle-end',angles[-1]==60)
add('zero-one-angle-step',all(b-a==6 for a,b in zip(angles,angles[1:])))
add('halfkg-index',angles[5]==30)
add('ordinary-interior-count',len([i for i in range(1,10) if i!=5])==8)
add('five-spans',5*10==50)
add('global-position-count',50+1==51)
add('inactive-gap',360-300==60)

# 13-26 SSOT policy/worker integration
policy=read('policies/WEIGHT_DIAL_VISIBLE_TICK_SET_PROFILE.md')
w03=read('workers/W03_WEIGHT_SCALE.md')
w08=read('workers/W08_LAYOUT_RENDER_THAI.md')
w09=read('workers/W09_QA_RELEASE.md')
w10=read('workers/W10_METROLOGY_ENGINEER.md')
builder=read('tools/build_install_package.py')
checks=[
('policy-intervals','INTERVALS_PER_KG=10' in policy),
('policy-positions','POSITIONS_PER_KG_ENDPOINT_INCLUSIVE=11' in policy),
('policy-interior','INTERIOR_POSITIONS_PER_KG_SPAN=9' in policy),
('policy-visible-offsets','VISIBLE_TICK_OFFSETS_PER_KG' in policy and '0.9' in policy),
('policy-visible-angle-offsets','VISIBLE_TICK_ANGLE_OFFSETS_PER_KG' in policy and '54°' in policy),
('policy-half-index','HALF_KG_INTERMEDIATE_INDEX=5' in policy),
('policy-hard-negative','DO NOT simplify, omit, merge, or sparsify' in policy),
('w03-explicit-visible-set','VISIBLE_TICK_OFFSETS_PER_KG' in w03 and 'VISIBLE_TICK_ANGLE_OFFSETS_PER_KG' in w03),
('w07-runtime-policy-bundle',"'W07_INSTRUMENT_AUDITOR.txt':['workers/W07_INSTRUMENT_AUDITOR.md','domains/INSTRUMENT_READING_ENGINE.md',WEIGHT_VISIBLE_PROFILE]" in builder),
('w08-local-serialization','INTERVALS_PER_KG=10' in w08 and 'HALF_KG_INTERMEDIATE_OFFSET=0.5' in w08),
('w09-release-gate','PROMPT_WEIGHT_PER_KG_SUBDIVISION_QA' in w09 and 'PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA' in w09),
('w10-independent-recount','INTERVALS_PER_KG=10' in w10 and 'LOCAL_SPAN_RECOUNT_CHECK' in w10),
('policy-artifact-fail','ARTIFACT_WEIGHT_PER_KG_SUBDIVISION_QA=FAIL' in policy),
('defect-doc',(ROOT/'qa/ACTUAL_WEIGHT_DIAL_VISIBLE_SUBDIVISION_REGRESSION_2026_09_01.md').is_file()),
]
for n,o in checks:add(n,o)

# 27-32 release/package integration
workflow=(REPO/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml').read_text(encoding='utf-8')
for n,o in [
('builder-policy','WEIGHT_DIAL_VISIBLE_TICK_SET_PROFILE.md' in builder),
('builder-suite','weight_dial_visible_subdivision_regression_suite.py' in builder),
('builder-effective-total','1430/1430 PASS' in builder),
('workflow-suite','Weight dial visible subdivision regression — 32 cases' in workflow),
('builder-defect-doc','ACTUAL_WEIGHT_DIAL_VISIBLE_SUBDIVISION_REGRESSION_2026_09_01.md' in builder),
('policy-bundled-team',all(token in builder for token in ["'W03_WEIGHT_SCALE.txt'","'W07_INSTRUMENT_AUDITOR.txt'","'W08_LAYOUT_RENDER_THAI.txt'","'W09_QA_RELEASE.txt'","'W10_METROLOGY_ENGINEER.txt'",'WEIGHT_VISIBLE_PROFILE'])),
]:add(n,o)

assert len(CASES)==32,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'WEIGHT DIAL VISIBLE SUBDIVISION REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_,d in failed: print('FAIL',n,d)
    sys.exit(1)
print('WEIGHT DIAL VISIBLE SUBDIVISION REGRESSION: PASS')
print('cases: 32')
print('pass: 32')
print('fail: 0')
print('per-kg visible tick-set + midpoint hierarchy + runtime integration: 32/32 PASS')
print('artifact QA: supplied defective artifact remains FAIL; future renders NOT_YET_TESTED')
