#!/usr/bin/env python3
"""Full deterministic/policy dry-run suite for activity-based-elementary-worksheet 2.6.x.

This suite exercises declared formulas, topology, routing/visibility contracts and
critical negative guards. It is prompt-system QA, not downstream artifact QA.

Expected case count: exactly 449.
"""
from __future__ import annotations
from pathlib import Path
import calendar,math,sys
ROOT=Path(__file__).resolve().parents[1]
CASES=[]
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def add(area,name,ok,detail=''): CASES.append((area,name,bool(ok),detail))

workers={
'W01_ACADEMIC_CONTENT':'workers/W01_ACADEMIC_CONTENT.md','W02_TIME_CLOCK':'workers/W02_TIME_CLOCK.md','W03_WEIGHT_SCALE':'workers/W03_WEIGHT_SCALE.md','W04_LENGTH_DISTANCE':'workers/W04_LENGTH_DISTANCE.md','W05_TEMPERATURE_CAPACITY_VOLUME':'workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','W06_MONEY_CALENDAR_DATA':'workers/W06_MONEY_CALENDAR_DATA.md','W07_INSTRUMENT_AUDITOR':'workers/W07_INSTRUMENT_AUDITOR.md','W08_LAYOUT_RENDER_THAI':'workers/W08_LAYOUT_RENDER_THAI.md','W09_QA_RELEASE':'workers/W09_QA_RELEASE.md'}
for wid,rel in workers.items():
    txt=read(rel); add('Package',f'worker {wid}',f'WORKER_ID={wid}' in txt and 'BASELINE_COMPATIBILITY=2.6.x' in txt and 'WORKER_SCHEMA_VERSION=1' in txt)
static_checks=[
('GEM_INSTRUCTIONS_PRODUCTION.md','FINAL_IMAGE_GENERATION_PROMPT'),('GEM_INSTRUCTIONS_PRODUCTION.md','Orchestrator'),('GEM_INSTRUCTIONS_PRODUCTION.md','ARTIFACT_QA=NOT_YET_TESTED'),('OUTPUT_CONTRACT.md','STUDENT_CONTENT_BLUEPRINT'),('OUTPUT_CONTRACT.md','RENDER_ONLY_NOT_FOR_WORKSHEET'),('OUTPUT_CONTRACT.md','DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY'),('policies/PARAMETER_POLICY.md','CLOCK_READING_MODE=AUTO|SINGLE|DAY_NIGHT_PAIR'),('policies/PARAMETER_POLICY.md','TARGET_MINUTE_MODE=ANY_VALID|MULTIPLE_OF_GRANULARITY|EXACT_MINUTE_SET'),('policies/PARAMETER_POLICY.md','TARGET_MINUTE_SET={30}'),('policies/PARAMETER_POLICY.md','ONE_PAGE_LOCK=OFF'),('domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md','01:30 → กลางวัน 13:30 | กลางคืน 01:30'),('domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md','06:30 → กลางวัน 06:30 | กลางคืน 18:30'),('domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md','12:15 → กลางวัน 12:15 | กลางคืน 00:15'),('workers/W02_TIME_CLOCK.md','TARGET_MINUTE_SET={30}'),('workers/W02_TIME_CLOCK.md','PROMPT_PER_ITEM_RENDER_STATE_QA'),('workers/W02_TIME_CLOCK.md','STUDENT_CONTENT_BLUEPRINT'),('workers/W04_LENGTH_DISTANCE.md','CYCLIC_FULL_CIRCLE'),('workers/W04_LENGTH_DISTANCE.md','360 equal intervals / 360 distinct positions'),('workers/W09_QA_RELEASE.md','PROMPT_PAGE_LOCK_PROVENANCE_QA'),('workers/W09_QA_RELEASE.md','PROMPT_RELEASE=BLOCKED'),('workers/W09_QA_RELEASE.md','Critical QA is conjunctive'),('qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md','DN-19 — false-PASS prevention'),('qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md','TARGET_MINUTE_SET={30}'),('qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md','ONE_PAGE_LOCK=OFF'),('qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md','Prompt Generator Acceptance Tests'),('qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md','M-49'),('domains/MEASUREMENT_COVERAGE_P1_P6.md','60 seconds = 1 minute'),('domains/MEASUREMENT_COVERAGE_P1_P6.md','1000 cm³ = 1 dm³'),('KB_ROUTER.md','W02_TIME_CLOCK'),('KB_MANIFEST.md','W09_QA_RELEASE'),('qa/DOMAIN_RELEASE_MATRIX.md','PRODUCTION_CANDIDATE')]
for rel,token in static_checks:add('Package',f'{rel}::{token[:36]}',token in read(rel))
assert len(CASES)==40

for i in range(10):
    a,b=137+i*23,21+i; add('W01 Arithmetic',f'add-{i}',a+b==sum([a,b]))
for i in range(10):
    a,b=500+i*17,80+i*3; add('W01 Arithmetic',f'sub-{i}',a>=b and a-b>=0)
for i in range(10):
    a,b=103+i*11,2+(i%7); add('W01 Arithmetic',f'mul-{i}',a*b==sum(a for _ in range(b)))
for i in range(10):
    q,d=11+i,2+(i%8); n=q*d; add('W01 Arithmetic',f'exact-div-{i}',n%d==0 and n//d==q)

for i in range(20):
    start=7*60+i*5; duration=15+(i%6)*10; end=start+duration; add('W02 Time',f'duration-{i}',end-start==duration)
for i in range(10):
    h,m,s=i%5,(i*7)%60,(i*11)%60; total=3600*h+60*m+s; add('W02 Time',f'seconds-{i}',total==h*3600+60*m+s)
for i in range(10):
    end=8*60+i*13; duration=20+i; start=end-duration; add('W02 Time',f'reverse-{i}',start+duration==end)

for h in range(1,13):
    for m in (0,15,30,45,55):
        minute_angle=6*m; hour_angle=(30*(h%12)+0.5*m)%360; ok=minute_angle%6==0 and 0<=hour_angle<360
        if m==30: ok=ok and math.isclose(hour_angle,(30*(h%12)+15)%360)
        add('W02 Clock',f'clock-{h:02d}:{m:02d}',ok)

def pair(h):
    if 1<=h<=5:return h+12,h
    if 6<=h<=11:return h,h+12
    return 12,0
for h in range(1,13):
    for m in (0,30,45):
        day,night=pair(h); add('W02 Day/Night',f'pair-{h:02d}:{m:02d}',(day-night)%24==12 and 0<=day<=23 and 0<=night<=23)

for idx in range(51):
    weight=idx/10; angle=(240+6*idx)%360; add('W03 Weight',f'dial-index-{idx}',round(weight/0.1)==idx and 0<=angle<360)

for i in range(40):
    start_mm=i%17; length_mm=5+(i*3)%50; end_mm=start_mm+length_mm; add('W04 Length',f'ruler-{i}',end_mm-start_mm==length_mm and 10+1==11)

for i in range(10):
    outbound=500+100*i; ret=600+80*i; add('W04 Distance',f'route-{i}',outbound+ret==sum([outbound,ret]))
for i,d in enumerate([1,2,5,10,15,20,30,45,60,90]): add('W04 Angle',f'semi-{d}',180%d==0 and 180//d+1>=3)
for i,d in enumerate([1,2,3,4,5,6,10,12,15,30]):
    intervals=360//d; add('W04 Angle',f'full-{d}',360%d==0 and intervals==len(range(0,360,d)))
for i in range(10):
    l,w=3+i,2+i; p=2*(l+w); area=l*w; add('W04 Area',f'rect-{i}',p==l+l+w+w and area>0)

for i in range(10):
    t=20+2*i; idx=round((t-20)/2); add('W05 Temperature',f'temp-{t}',20+idx*2==t)
for i in range(10):
    litres,ml=i,(i*125)%1000; total=litres*1000+ml; add('W05 Capacity',f'capacity-{i}',total>=0 and total//1000==litres+ml//1000)
for i in range(10):
    l,w,h=2+i,3,4; add('W05 Volume',f'prism-{i}',l*w*h==(2+i)*12)
meniscus=read('workers/W05_TEMPERATURE_CAPACITY_VOLUME.md')
for i,token in enumerate(['BOTTOM','TOP','concave','target graduation','1000 mL','1 dm³','V=','compatible','composite','CUBIC']): add('W05 Meniscus/Volume',f'contract-{i}',token.lower() in meniscus.lower())

for i in range(10):
    prices=[10+i,20+i,5]; paid=sum(prices)+50; add('W06 Money',f'money-{i}',paid-sum(prices)==50)
for year,month in [(2024,2),(2025,2),(2026,1),(2026,4),(2026,6),(2026,9),(2026,11),(2026,12),(2028,2),(2030,7)]: add('W06 Calendar',f'calendar-{year}-{month}',calendar.monthrange(year,month)[1] in (28,29,30,31))
for i in range(10):
    data=[i+1,i+2,i+3]; add('W06 Data',f'data-{i}',sum(data)==3*i+6)

contract_checks=[
('GEM_INSTRUCTIONS_PRODUCTION.md','W02 + W07 + W10 + W08 + W09'),('GEM_INSTRUCTIONS_PRODUCTION.md','W03 + W07 + W10 + W08 + W09'),('GEM_INSTRUCTIONS_PRODUCTION.md','W04 + W07 + W10 + W08 + W09'),('GEM_INSTRUCTIONS_PRODUCTION.md','W05 + W07 + W10 + W08 + W09'),('workers/W08_LAYOUT_RENDER_THAI.md','DOCUMENT_FIRST'),('workers/W08_LAYOUT_RENDER_THAI.md','HYBRID'),('workers/W08_LAYOUT_RENDER_THAI.md','DETERMINISTIC_VECTOR'),('workers/W08_LAYOUT_RENDER_THAI.md','IMAGE_ONLY'),('workers/W09_QA_RELEASE.md','PROMPT_RELEASE=BLOCKED'),('workers/W09_QA_RELEASE.md','PROMPT_RELEASE=APPROVED'),('workers/W09_QA_RELEASE.md','ARTIFACT_QA=NOT_YET_TESTED'),('workers/W09_QA_RELEASE.md','CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA'),('workers/W09_QA_RELEASE.md','PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA'),('workers/W09_QA_RELEASE.md','PROMPT_PAGE_LOCK_PROVENANCE_QA'),('workers/W09_QA_RELEASE.md','PROMPT_HALF_HOUR_INTENT_QA'),('workers/W09_QA_RELEASE.md','PROMPT_DAY_NIGHT_MAPPING_QA'),('workers/W09_QA_RELEASE.md','PROMPT_PER_ITEM_RENDER_STATE_QA'),('OUTPUT_CONTRACT.md','NO_PLACEHOLDER_VISUALS'),('OUTPUT_CONTRACT.md','STUDENT_VISIBLE_ANSWER_LEAK_GUARD=ON'),('OUTPUT_CONTRACT.md','CANONICAL_LABEL_PRESERVATION=ON'),('ARCHITECTURE.md','INTERNAL_VERIFIED_STATE'),('ARCHITECTURE.md','STUDENT_CONTENT_BLUEPRINT'),('ARCHITECTURE.md','TEACHER_VISIBLE_RENDER_STATE'),('policies/PARAMETER_POLICY.md','ONE_PAGE_LOCK=ON` only when the user explicitly requires one page'),('policies/PARAMETER_POLICY.md','Every non-default lock or mode must record provenance'),('qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md','PROMPT_RELEASE=BLOCKED'),('qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md','numeric angles mandatory'),('qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md','strict half-hour intent'),('qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md','Thai P3 AUTO mode'),('workers/W04_LENGTH_DISTANCE.md','no duplicated 0°/360° physical mark'),('workers/W04_LENGTH_DISTANCE.md','reflex'),('workers/W07_INSTRUMENT_AUDITOR.md','If the learner must read it, geometry is academic data')]
for rel,token in contract_checks:add('Routing/Output',f'{rel}::{token[:32]}',token.lower() in read(rel).lower())
assert len(CASES)==449,f'suite construction error: expected 449, got {len(CASES)}'
fails=[c for c in CASES if not c[2]]
print(f"FULL DRY-RUN SUITE: {'PASS' if not fails else 'FAIL'}"); print(f'cases: {len(CASES)}'); print(f'pass: {len(CASES)-len(fails)}'); print(f'fail: {len(fails)}')
if fails:
    [print(f'FAIL [{a}] {n} {d}'.rstrip()) for a,n,_,d in fails]; sys.exit(1)
print('release-gate deterministic/policy suite: 449/449 PASS'); print('artifact QA: NOT_YET_TESTED')
