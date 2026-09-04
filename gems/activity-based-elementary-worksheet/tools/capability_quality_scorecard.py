#!/usr/bin/env python3
"""Capability-by-capability quality score gate.

Uniform 20-criterion rubric, 5 points each.
Target: every capability >=95 and overall >=95.
This evaluates SSOT/instruction/knowledge readiness, not rendered pixels.
"""
from pathlib import Path
import sys,re,math
ROOT=Path(__file__).resolve().parents[1]
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def has(text,*tokens): return all(t.lower() in text.lower() for t in tokens)
def anyhas(text,*tokens): return any(t.lower() in text.lower() for t in tokens)

ped=read('policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md')
router=read('KB_ROUTER.md'); registry=read('domains/DOMAIN_REGISTRY.md')
examples=read('examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md')+'\n'+read('examples/USAGE_EXAMPLES.md')+'\n'+read('examples/MULTI_DOMAIN_EXAMPLES.md')
qa=read('qa/ACCEPTANCE_TESTS.md')+'\n'+read('qa/DOMAIN_RELEASE_MATRIX.md')
skills=read('tools/full_skill_matrix_suite.py')

CAPS={
'ACADEMIC_ARITHMETIC_THAI':('workers/W01_ACADEMIC_CONTENT.md',None,'W01_ACADEMIC_CONTENT'),
'TIME_CALCULATION':('domains/TIME_ENGINE.md','workers/W02_TIME_CLOCK.md','W02_TIME_CLOCK'),
'ANALOG_CLOCK':('domains/CLOCK_READING_ENGINE.md','workers/W02_TIME_CLOCK.md','W02_TIME_CLOCK'),
'WEIGHT_SCALE':('domains/SCALE_READING_ENGINE.md','workers/W03_WEIGHT_SCALE.md','W03_WEIGHT_SCALE'),
'RULER_LENGTH':('domains/LENGTH_READING_ENGINE.md','workers/W04_LENGTH_DISTANCE.md','W04_LENGTH_DISTANCE'),
'DISTANCE':('workers/W04_LENGTH_DISTANCE.md','domains/MEASUREMENT_COVERAGE_P1_P6.md','W04_LENGTH_DISTANCE'),
'SPEEDOMETER':('domains/SPEEDOMETER_READING_ENGINE.md','workers/W04_LENGTH_DISTANCE.md','W04_LENGTH_DISTANCE'),
'ANGLE_PROTRACTOR':('workers/W04_LENGTH_DISTANCE.md','policies/SCALE_LINE_INTEGRITY_PROFILE.md','W04_LENGTH_DISTANCE'),
'PERIMETER_AREA':('workers/W04_LENGTH_DISTANCE.md','domains/MEASUREMENT_COVERAGE_P1_P6.md','W04_LENGTH_DISTANCE'),
'TEMPERATURE':('domains/TEMPERATURE_READING_ENGINE.md','workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','W05_TEMPERATURE_CAPACITY_VOLUME'),
'CAPACITY':('domains/CAPACITY_READING_ENGINE.md','workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','W05_TEMPERATURE_CAPACITY_VOLUME'),
'VOLUME':('workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','domains/MEASUREMENT_COVERAGE_P1_P6.md','W05_TEMPERATURE_CAPACITY_VOLUME'),
'MONEY':('domains/MONEY_ENGINE.md','workers/W06_MONEY_CALENDAR_DATA.md','W06_MONEY_CALENDAR_DATA'),
'CALENDAR':('domains/CALENDAR_ENGINE.md','workers/W06_MONEY_CALENDAR_DATA.md','W06_MONEY_CALENDAR_DATA'),
'DATA_READING':('domains/TABLE_GRAPH_READING_ENGINE.md','workers/W06_MONEY_CALENDAR_DATA.md','W06_MONEY_CALENDAR_DATA'),
}

scope_terms=['scope','supports','owns']
verify_terms=['independent','recompute','verify','validate']
failure_terms=['block','fail','critical','wrong','invalid']
grade_terms=['grade','p1','p2','p3','ป.']
student_terms=['student','learner','answer format','visible']
difficulty_terms=['difficulty','complexity','grade']
render_terms=['render','vector','document_first','deterministic']
qa_terms=['qa','prompt_']
negative_terms=['do not','must not','hard negative','forbid','never']
repair_terms=['review','revise','repair','regenerate','recheck','failure']
example_terms=['example','canonical','เช่น']

scores={}
details={}
for cap,(p1,p2,owner) in CAPS.items():
    d1=read(p1); d2=read(p2) if p2 else ''
    text=d1+'\n'+d2
    checks=[]
    checks.append(anyhas(text,*scope_terms)) # A1
    checks.append(anyhas(text,'formula','=', 'canonical','exact')) # A2
    checks.append(anyhas(text,'representab','valid','target','answer')) # A3
    checks.append(anyhas(text,*verify_terms)) # A4
    checks.append(anyhas(text,*failure_terms)) # A5
    checks.append(anyhas(text,*grade_terms)) # B1
    checks.append(anyhas(text,*student_terms)) # B2
    checks.append(anyhas(text,*difficulty_terms) or has(ped,'difficulty')) # B3
    checks.append(has(ped,'typography') and has(ped,'writing')) # B4
    checks.append(anyhas(text,'state','canonical','dataset','target')) # C1
    checks.append(anyhas(text,'mapping','geometry','align','grid','position','visual')) # C2
    checks.append(anyhas(text,'decoration','decorative','perspective','competing','ambiguous')) # C3
    checks.append(anyhas(text,*render_terms) or has(ped,'VECTOR_PRIMITIVE_LOCKED')) # C4
    checks.append(anyhas(text,*qa_terms)) # D1
    checks.append(anyhas(text,*negative_terms)) # D2
    checks.append(anyhas(text,*repair_terms)) # D3
    checks.append(owner.lower() in skills.lower() or cap.split('_')[0].lower() in qa.lower()) # D4
    checks.append(owner.lower() in router.lower() or owner.lower() in registry.lower()) # D5
    checks.append(cap.split('_')[0].lower() in examples.lower() or anyhas(text,*example_terms)) # E1
    checks.append(anyhas(text,'teacher','worksheet','output','returns')) # E2
    assert len(checks)==20
    passed=sum(checks); score=passed*5
    scores[cap]=score
    details[cap]=[i+1 for i,v in enumerate(checks) if not v]

overall=sum(scores.values())/len(scores)
print('CAPABILITY QUALITY SCORECARD')
for cap in CAPS:
    print(f'{cap}: {scores[cap]:.0f}% missing={details[cap]}')
print(f'OVERALL_CAPABILITY_SCORE: {overall:.2f}%')
print('ARTIFACT_QA: NOT_YET_TESTED')
failed=[c for c,s in scores.items() if s<95]
if overall<95 or failed:
    print('CAPABILITY_QUALITY_GATE: FAIL')
    if failed: print('BELOW_95:', ', '.join(failed))
    sys.exit(1)
print('CAPABILITY_QUALITY_GATE: PASS')
print('EVERY_CAPABILITY_SCORE >=95: YES')
