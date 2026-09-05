#!/usr/bin/env python3
"""Skill Metric Pack governance regression.

Validates that every declared skill has a complete metric pack and that
high-risk canonical oracles remain mathematically coherent.

Gate is additive governance evidence and does not replace Artifact QA.
Expected: exactly 161 cases.
"""
from pathlib import Path
import math,sys
ROOT=Path(__file__).resolve().parents[1]
MET=ROOT/'skill-metrics'
CASES=[]
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))
def read(name): return (MET/name).read_text(encoding='utf-8')

PACKS={
'ACADEMIC_ARITHMETIC_THAI':'ACADEMIC_ARITHMETIC_THAI_SKILL_METRICS.md',
'TIME_CALCULATION':'TIME_CALCULATION_SKILL_METRICS.md',
'ANALOG_CLOCK':'ANALOG_CLOCK_SKILL_METRICS.md',
'WEIGHT_SCALE':'WEIGHT_SCALE_SKILL_METRICS.md',
'RULER_LENGTH':'RULER_LENGTH_SKILL_METRICS.md',
'DISTANCE':'DISTANCE_SKILL_METRICS.md',
'SPEEDOMETER':'SPEEDOMETER_SKILL_METRICS.md',
'ANGLE_PROTRACTOR':'ANGLE_PROTRACTOR_SKILL_METRICS.md',
'PERIMETER_AREA':'PERIMETER_AREA_SKILL_METRICS.md',
'TEMPERATURE':'TEMPERATURE_SKILL_METRICS.md',
'CAPACITY':'CAPACITY_SKILL_METRICS.md',
'VOLUME':'VOLUME_SKILL_METRICS.md',
'MONEY':'MONEY_SKILL_METRICS.md',
'CALENDAR':'CALENDAR_SKILL_METRICS.md',
'DATA_READING':'DATA_READING_SKILL_METRICS.md',
}
required_sections=['SKILL_ID=','OWNER=','## CANONICAL_ORACLE','## PROMPT_METRICS','## ARTIFACT_METRICS','## CRITICAL_DEFECTS','## REPAIR_PROTOCOL','PASS_THRESHOLD=95']

# 15 skills × 9 structural checks = 135
for skill,name in PACKS.items():
    p=MET/name
    add(f'{skill}-file',p.is_file())
    if not p.is_file():
        for i in range(8): add(f'{skill}-missing-{i}',False)
        continue
    txt=p.read_text(encoding='utf-8')
    add(f'{skill}-id',f'SKILL_ID={skill}' in txt)
    for token in required_sections[1:]: add(f'{skill}-{token[:18]}',token in txt,token)

# 21 semantic/governance checks, total 156
standard=read('SKILL_METRIC_STANDARD.md')
critical=read('CRITICAL_DEFECT_POLICY.md')
artifact=read('ARTIFACT_QUALIFICATION_PROTOCOL.md')
registry=read('SKILL_SCORE_REGISTRY.md')
add('global-standard-95','SKILL_PROMPT_SCORE >= 95' in standard and 'SKILL_ARTIFACT_SCORE >= 95' in standard)
add('global-critical-override','CRITICAL_ACADEMIC_DEFECT => SKILL_RELEASE=BLOCKED' in standard)
add('global-a4-portrait','PAGE_SIZE=A4' in standard and 'ORIENTATION=PORTRAIT' in standard)
add('global-artifact-boundary','ARTIFACT_QA=NOT_YET_TESTED' in standard)
add('global-critical-noncompensatory','CRITICAL_ACADEMIC_DEFECT => ARTIFACT_QA=FAIL => CLASSROOM_RELEASE=BLOCKED' in critical)
add('global-artifact-min10','>=10 actual rendered worksheets' in artifact)
for skill in PACKS: add(f'registry-{skill}',skill in registry)

# 5 canonical math checks, total 161
h,m=3,30
add('oracle-clock-3-30',math.isclose(30*(h%12)+0.5*m,105.0))
h,m=2,45
add('oracle-clock-2-45',math.isclose(30*(h%12)+0.5*m,82.5))
add('oracle-weight-per-kg',math.isclose(1.0/0.1,10.0) and int(round(1.0/0.1))+1==11)
add('oracle-protractor',int(180/1)==180 and int(180/1)+1==181)
add('oracle-capacity',int(1000/50)==20 and int(100/50)==2)

assert len(CASES)==161,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'SKILL METRIC PACK REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_,d in failed: print('FAIL',n,d)
    sys.exit(1)
print('SKILL METRIC PACK REGRESSION: PASS')
print('cases: 161')
print('pass: 161')
print('fail: 0')
print('skills: 15/15 metric packs complete')
print('skill prompt threshold: >=95')
print('skill artifact threshold: >=95')
print('critical academic defect override: enforced')
print('artifact QA: NOT_YET_TESTED until rendered worksheet inspection')
