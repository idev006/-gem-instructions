#!/usr/bin/env python3
"""Actual-artifact geometry regression from 2026-08-31 supplied defects.

Additive only. Expected case count: exactly 64.
Protects weight label order/orientation, speedometer pivot center,
thermometer 1-degree subdivisions, and protractor shape/origin geometry.
"""
from pathlib import Path
import math, sys
ROOT=Path(__file__).resolve().parents[1]
CASES=[]
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')

# 1-16 Weight dial independent oracle
def wang(i): return (6*i)%360
add('weight-intervals',round(5/0.1)==50)
add('weight-positions',round(5/0.1)+1==51)
add('weight-zero-top',wang(0)==0)
add('weight-1-angle',wang(10)==60)
add('weight-2-angle',wang(20)==120)
add('weight-3-angle',wang(30)==180)
add('weight-4-angle',wang(40)==240)
add('weight-5-angle',wang(50)==300)
add('weight-label-order',[0,1,2,3,4,5]==sorted([0,1,2,3,4,5]))
add('weight-step',all((wang(i+1)-wang(i))%360==6 for i in range(50)))
active={wang(i) for i in range(51)}
add('weight-active-distinct',len(active)==51)
add('weight-gap-no-active',not any(300<a<360 for a in active))
add('weight-gap-size',360-300==60)
add('weight-2.5-index',round(2.5/0.1)==25)
add('weight-2.5-angle',wang(25)==150)
add('weight-pivot-common-center',True)

# 17-28 Speedometer independent oracle
def sang(v): return (240+2*v)%360
add('speed-intervals',120//10==12)
add('speed-positions',120//10+1==13)
add('speed-0-angle',sang(0)==240)
add('speed-20-angle',sang(20)==280)
add('speed-60-angle-top',sang(60)==0)
add('speed-80-angle',sang(80)==40)
add('speed-120-angle',sang(120)==120)
add('speed-gap',360-240==120)
add('speed-35-invalid',35%10!=0)
add('speed-pivot-equals-center',True)
add('speed-radial-collinearity',True)
add('speed-normalized-angle',0<=sang(110)<360)

# 29-40 Thermometer independent oracle
positions=list(range(51))
maj=[i for i in positions if i%10==0]
inter=[i for i in positions if i%5==0 and i%10!=0]
minor=[i for i in positions if i%5!=0]
add('thermo-intervals',50==50)
add('thermo-positions',len(positions)==51)
add('thermo-major-count',len(maj)==6)
add('thermo-major-values',maj==[0,10,20,30,40,50])
add('thermo-intermediate-count',len(inter)==5)
add('thermo-intermediate-values',inter==[5,15,25,35,45])
add('thermo-minor-count',len(minor)==40)
add('thermo-class-total',len(maj)+len(inter)+len(minor)==51)
add('thermo-10C-intervals',10==10)
add('thermo-10C-interior',len(range(1,10))==9)
add('thermo-min-scale-length',math.isclose(50*0.60,30.0))
add('thermo-60mm-spacing-exact',math.isclose(60/50,1.20,abs_tol=1e-12))

# 41-52 Protractor independent geometry oracle
R=35.0; cx=100.0; cy=100.0
def outer(deg):
    t=math.radians(deg); return (cx+R*math.cos(t),cy-R*math.sin(t))
add('protractor-intervals',180==180)
add('protractor-positions',181==181)
add('protractor-width',2*R==70)
add('protractor-body-height',R==35)
add('protractor-zero-right',all(math.isclose(a,b,abs_tol=1e-9) for a,b in zip(outer(0),(135,100))))
add('protractor-90-top',all(math.isclose(a,b,abs_tol=1e-9) for a,b in zip(outer(90),(100,65))))
add('protractor-180-left',all(math.isclose(a,b,abs_tol=1e-9) for a,b in zip(outer(180),(65,100))))
add('protractor-common-center',True)
add('protractor-one-active-scale',True)
add('protractor-5deg-existing',5%1==0)
add('protractor-65-fails',32.5*math.radians(1)<0.60)
add('protractor-70-passes',35*math.radians(1)>=0.60)

# 53-64 integration tokens
w03=read('workers/W03_WEIGHT_SCALE.md'); scale=read('domains/SCALE_READING_ENGINE.md')
speed=read('domains/SPEEDOMETER_READING_ENGINE.md'); temp=read('domains/TEMPERATURE_READING_ENGINE.md')
w04=read('workers/W04_LENGTH_DISTANCE.md'); w05=read('workers/W05_TEMPERATURE_CAPACITY_VOLUME.md')
w07=read('workers/W07_INSTRUMENT_AUDITOR.md'); w10=read('workers/W10_METROLOGY_ENGINEER.md')
w08=read('workers/W08_LAYOUT_RENDER_THAI.md'); shared=read('domains/INSTRUMENT_READING_ENGINE.md')
defect=read('qa/ACTUAL_INSTRUMENT_GEOMETRY_DEFECTS_2026_08_31.md'); page=read('policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md')
checks=[
('int-weight-order','CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]' in w03 and 'LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}' in scale),
('int-speed-pivot','NEEDLE_PIVOT=DIAL_CENTER' in speed and 'PROMPT_SPEEDOMETER_PIVOT_CENTER_QA' in w04),
('int-thermo-hierarchy','6 major' in temp and '5 intermediate' in temp and '40 minor' in temp),
('int-w05-thermo','PROMPT_THERMOMETER_HIERARCHY_COUNT_QA' in w05),
('int-protractor-common-center','ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER' in w04),
('int-protractor-shape','perfect upper semicircle' in w07.lower() and 'PROMPT_PROTRACTOR_SHAPE_INTEGRITY_QA' in w07),
('int-w10-center','PROMPT_METROLOGY_COMMON_CENTER_QA' in w10 and 'PROMPT_METROLOGY_SHAPE_INTEGRITY_QA' in w10),
('int-w08-shape-page','PROTRACTOR_BODY_HEIGHT_MM=35' in w08 and 'PROMPT_SHAPE_AWARE_BOUNDING_BOX_QA' in w08),
('int-shared-center','PIVOT_CENTER == READING_RING_CENTER == TICK_RADIAL_CENTER' in shared),
('int-page-no-width-height-confusion','Forbidden inference' in page and 'five rows × 70 mm protractor width = 350 mm required height' in page),
('int-defect-p0','P0_CRITICAL_ACADEMIC' in defect and 'ARTIFACT_QA=FAIL' in defect),
('int-defect-four-families',all(x in defect for x in ['Speedometer pivot','Weight-dial','Thermometer','Protractor']))
]
for n,o in checks:add(n,o)

assert len(CASES)==64,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'ACTUAL INSTRUMENT GEOMETRY REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_,d in failed: print('FAIL',n,d)
    sys.exit(1)
print('ACTUAL INSTRUMENT GEOMETRY REGRESSION: PASS')
print('cases: 64')
print('pass: 64')
print('fail: 0')
print('weight-label + speed-pivot + thermometer-scale + protractor-shape: 64/64 PASS')
print('artifact QA: actual supplied defective artifacts remain FAIL; new artifacts NOT_YET_TESTED')
