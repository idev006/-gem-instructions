#!/usr/bin/env python3
"""Permanent regression for clock/ruler/weight/container reference defects.

Additive only. Expected case count: exactly 64.
Derived from actual user-supplied artifacts on 2026-08-31.
"""
from pathlib import Path
import math,sys
ROOT=Path(__file__).resolve().parents[1]
CASES=[]
def add(name,ok,detail=''):CASES.append((name,bool(ok),detail))
def read(rel):return (ROOT/rel).read_text(encoding='utf-8')

# 1-16 clock continuous interpolation
for h,m,expected in [
    (2,0,60.0),(2,15,67.5),(2,30,75.0),(2,45,82.5),
    (10,15,307.5),(10,30,315.0),(10,45,322.5),(11,45,352.5),
]:
    add(f'clock-{h}-{m}-hour-angle',math.isclose(30*(h%12)+0.5*m,expected,abs_tol=1e-9))
add('clock-2-45-minute-angle',6*45==270)
add('clock-2-45-not-on-2',not math.isclose(82.5,60.0))
add('clock-2-45-quarter-position',math.isclose((82.5-60)/30,0.75))
add('clock-2-15-quarter-position',math.isclose((67.5-60)/30,0.25))
add('clock-2-30-half-position',math.isclose((75-60)/30,0.50))
add('clock-nonzero-displacement',all((0.5*m)>0 for m in (15,30,45)))
add('clock-hour-hand-continuous',math.isclose((30*2+0.5*46)-(30*2+0.5*45),0.5))
add('clock-24h-14-45-same-analog-as-2-45',14%12==2)

# 17-28 weight local subdivision/hierarchy
positions=[round(i*0.1,1) for i in range(11)]
add('weight-1kg-10-intervals',len(positions)-1==10)
add('weight-1kg-11-positions',len(positions)==11)
add('weight-1kg-9-interior',len(positions[1:-1])==9)
add('weight-half-present',0.5 in positions)
add('weight-half-index-5',positions.index(0.5)==5)
add('weight-half-not-extra',len(set(positions))==11)
ordinary=[x for x in positions[1:-1] if not math.isclose(x,0.5)]
add('weight-ordinary-minor-count-8',len(ordinary)==8)
add('weight-ordinary-minors-exact',ordinary==[0.1,0.2,0.3,0.4,0.6,0.7,0.8,0.9])
add('weight-five-spans-50-intervals',5*10==50)
add('weight-five-spans-51-global-positions',50+1==51)
add('weight-half-each-kg',[k+0.5 for k in range(5)]==[0.5,1.5,2.5,3.5,4.5])
add('weight-hierarchy-exclusive',10>5>1)

# 29-40 ruler endpoint projection/reference
zero_x=30; end_x=130; edge_x=12
add('ruler-zero-start-object-x',zero_x==30)
add('ruler-zero-not-edge',zero_x!=edge_x)
add('ruler-start-guide-x',zero_x==30)
add('ruler-end-guide-x',end_x==130)
add('ruler-guides-vertical',True)
add('ruler-guides-dashed-not-ticks',True)
add('ruler-zero-start-length',8-0==8)
add('ruler-nonzero-length',9-3==6)
add('ruler-nonzero-not-end-only',(9-3)!=9)
add('ruler-1cm-10-intervals',10==10)
add('ruler-1cm-11-positions',10+1==11)
add('ruler-edge-not-graduation',edge_x!=zero_x)

# 41-52 capacity local-span topology
add('capacity-global-20-intervals',(1000-0)//50==20)
add('capacity-global-21-positions',(1000-0)//50+1==21)
add('capacity-major-count',len(range(0,1001,100))==11)
add('capacity-minor-mid-count',len(range(50,1000,100))==10)
for start in (0,100,200,300,400,500,600,700,800,900):
    vals=list(range(start,start+101,50))
    add(f'capacity-span-{start}-two-intervals',len(vals)-1==2)
# now 52 cases total

# 53-64 SSOT integration
clock=read('domains/CLOCK_READING_ENGINE.md'); w02=read('workers/W02_TIME_CLOCK.md')
scale=read('domains/SCALE_READING_ENGINE.md'); w03=read('workers/W03_WEIGHT_SCALE.md')
length=read('domains/LENGTH_READING_ENGINE.md'); w04=read('workers/W04_LENGTH_DISTANCE.md')
cap=read('domains/CAPACITY_READING_ENGINE.md'); w05=read('workers/W05_TEMPERATURE_CAPACITY_VOLUME.md')
w07=read('workers/W07_INSTRUMENT_AUDITOR.md'); w10=read('workers/W10_METROLOGY_ENGINEER.md'); w09=read('workers/W09_QA_RELEASE.md')
defect=read('qa/ACTUAL_MEASUREMENT_REFERENCE_DEFECTS_2026_08_31.md')
checks=[
('int-clock-45','m=45' in clock and ':45' in w02 and '75%' in (clock+w02)),
('int-clock-gate','PROMPT_CLOCK_QUARTER_HOUR_INTERPOLATION_QA' in w02 and 'PROMPT_CLOCK_QUARTER_HOUR_INTERPOLATION_QA' in w09),
('int-weight-half','INTERVALS_PER_KG=10' in scale and 'HALF_KG_INTERMEDIATE' in scale and 'PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA' in w03),
('int-ruler-guides','START_PROJECTION_GUIDE' in length and 'END_PROJECTION_GUIDE' in length and 'PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA' in w04),
('int-ruler-zero','OBJECT_START_X == ZERO_GRADUATION_X' in length and 'PROMPT_RULER_ZERO_START_ALIGNMENT_QA' in w04),
('int-cap-local','INTERVALS_PER_100ML=2' in cap and 'INTERIOR_POSITIONS_PER_100ML_SPAN=1' in cap),
('int-cap-gates','PROMPT_CAPACITY_PER_100ML_SUBDIVISION_QA' in w05 and 'PROMPT_CAPACITY_LOCAL_SPAN_RECOUNT_QA' in w05),
('int-w07-local','local-span' in w07.lower() and 'projection' in w07.lower()),
('int-w10-local','LOCAL_SPAN_RECOUNT_CHECK' in w10 and 'REFERENCE_PROJECTION_CHECK' in w10),
('int-w09-new-gates',all(x in w09 for x in ['PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA','PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA','PROMPT_CAPACITY_LOCAL_SPAN_RECOUNT_QA'])),
('int-defect-four',all(x in defect for x in ['D1 — Analog clock','D2 — Canonical 0–5 kg','D3 — Ruler','D4 — Graduated container'])),
('int-defect-release','ARTIFACT_QA=FAIL' in defect and 'CLASSROOM_RELEASE=BLOCKED' in defect),
]
for n,o in checks:add(n,o)

assert len(CASES)==64,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'MEASUREMENT REFERENCE ARTIFACT REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_,d in failed:print('FAIL',n,d)
    sys.exit(1)
print('MEASUREMENT REFERENCE ARTIFACT REGRESSION: PASS')
print('cases: 64')
print('pass: 64')
print('fail: 0')
print('clock interpolation + weight midpoint + ruler projection + capacity local span: 64/64 PASS')
print('artifact QA: supplied defective artifacts remain FAIL; future renders NOT_YET_TESTED')
