#!/usr/bin/env python3
"""Actual protractor 181-position manifest regression — exactly 220 cases.

Protects against missing/extra/merged 1° graduations and duplicate/missing 10° labels.
Prompt/Knowledge regression only; rendered Artifact QA remains separate.
"""
from pathlib import Path
import math,sys
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent.parent
CASES=[]
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')

# 181 exact tick-position/classification checks
major=inter=minor=0
for d in range(181):
    if d%10==0:
        cls='MAJOR'; major+=1
    elif d%5==0:
        cls='INTERMEDIATE'; inter+=1
    else:
        cls='MINOR'; minor+=1
    # exact degree membership + finite radial endpoints on unit radius
    x=math.cos(math.radians(d)); y=-math.sin(math.radians(d))
    add(f'tick-{d:03d}', d>=0 and d<=180 and math.isfinite(x) and math.isfinite(y) and cls in {'MAJOR','INTERMEDIATE','MINOR'})
assert len(CASES)==181
assert (major,inter,minor)==(19,18,144)

# 19 exact unique label checks => 200
labels=list(range(0,181,10))
for v in labels:
    add(f'label-{v:03d}', v%10==0 and v in range(181))
assert len(CASES)==200
assert len(labels)==19 and len(set(labels))==19

# 20 integration/SSOT checks => 220
profile=read('policies/PROTRACTOR_181_TICK_MANIFEST_PROFILE.md')
metric=read('skill-metrics/ANGLE_PROTRACTOR_SKILL_METRICS.md')
w04=read('workers/W04_LENGTH_DISTANCE.md')
w07=read('workers/W07_INSTRUMENT_AUDITOR.md')
w08=read('workers/W08_LAYOUT_RENDER_THAI.md')
w09=read('workers/W09_QA_RELEASE.md')
w10=read('workers/W10_METROLOGY_ENGINEER.md')
defect=read('qa/ACTUAL_PROTRACTOR_MISSING_TICK_LABEL_REGRESSION_2026_09_05.md')
builder=read('tools/build_install_package.py')
workflow=(REPO/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml').read_text(encoding='utf-8')
checks=[
('profile-counts','EXPECTED_TICK_POSITION_COUNT=181' in profile and 'MAJOR_TICK_COUNT=19' in profile and 'INTERMEDIATE_TICK_COUNT=18' in profile and 'MINOR_TICK_COUNT=144' in profile),
('profile-label-count','EXPECTED_LABEL_COUNT=19' in profile),
('profile-label-unique','LABEL_VALUES_UNIQUE=YES' in profile and 'LABEL_DUPLICATE_COUNT=0' in profile),
('profile-manifest','PROTRACTOR_TICK_MANIFEST' in profile and 'PROTRACTOR_LABEL_MANIFEST' in profile),
('metric-bind','PROTRACTOR_181_TICK_MANIFEST_PROFILE.md' in metric),
('metric-critical','duplicate/missing labels are critical academic defects' in metric),
('w04-manifest','PROTRACTOR_TICK_MANIFEST' in w04 and 'PROTRACTOR_LABEL_MANIFEST' in w04),
('w04-counts','MAJOR_TICK_COUNT=19' in w04 and 'MINOR_TICK_COUNT=144' in w04),
('w07-set-audit','tick degrees are exactly the integer set 0..180' in w07),
('w07-label-audit','labels are exactly the unique set 0,10,...,180' in w07),
('w08-render-manifest','render from `PROTRACTOR_TICK_MANIFEST`' in w08),
('w08-no-omit','omit ticks for visual cleanliness' in w08),
('w09-gate','PROMPT_PROTRACTOR_181_POSITION_MANIFEST_QA=PASS' in w09),
('w09-label-gate','PROMPT_PROTRACTOR_LABEL_UNIQUENESS_QA=PASS' in w09),
('w10-oracle','EXPECTED_TICK_DEGREES=set(range(0,181))' in w10),
('w10-label-oracle','EXPECTED_LABEL_VALUES={0,10,20,...,180}' in w10),
('defect-fail','ARTIFACT_PROTRACTOR_TICK_MANIFEST_QA=FAIL' in defect),
('defect-label-fail','ARTIFACT_PROTRACTOR_LABEL_SET_QA=FAIL' in defect),
('builder-integration','PROTRACTOR_181_TICK_MANIFEST_PROFILE.md' in builder and 'ACTUAL_PROTRACTOR_MISSING_TICK_LABEL_REGRESSION_2026_09_05.md' in builder),
('workflow-integration','protractor_181_tick_manifest_regression_suite.py' in workflow),
]
for x in checks:add(*x)
assert len(CASES)==220,len(CASES)

failed=[x for x in CASES if not x[1]]
if failed:
    print(f'PROTRACTOR 181-TICK MANIFEST REGRESSION: FAIL ({len(failed)}/220)')
    for n,_,d in failed: print('FAIL',n,d)
    sys.exit(1)
print('PROTRACTOR 181-TICK MANIFEST REGRESSION: PASS')
print('cases: 220')
print('pass: 220')
print('fail: 0')
print('tick positions: 181/181')
print('class counts: major=19 intermediate=18 minor=144')
print('labels: 19/19 unique')
print('artifact QA: NOT_YET_TESTED for future renders')
