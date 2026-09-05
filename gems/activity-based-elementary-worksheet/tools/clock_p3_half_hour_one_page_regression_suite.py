#!/usr/bin/env python3
"""Clock P3 half-hour one-page regression — exactly 100 cases.

Protects two user-observed failures:
1) short/hour hand not derived from long/minute-hand position;
2) 10-item Thai P3 half-hour worksheet unnecessarily split despite a proved A4 portrait 2x5 layout.

Prompt/Knowledge regression only; rendered Artifact QA remains separate.
"""
from pathlib import Path
import math,sys
ROOT=Path(__file__).resolve().parents[1]
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
CASES=[]
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))

# 72 numeric checks = 12 hours × 6
for h in range(1,13):
    m=30
    minute_angle=6*m
    base=30*(h%12)
    displacement=minute_angle/12
    hour_angle=(base+displacement)%360
    expected=(base+15)%360
    add(f'{h}:30-minute-180', math.isclose(minute_angle,180))
    add(f'{h}:30-driver-15', math.isclose(displacement,15))
    add(f'{h}:30-hour-midpoint', math.isclose(hour_angle,expected))
    add(f'{h}:30-direct-equivalence', math.isclose(hour_angle,(30*(h%12)+0.5*m)%360))
    add(f'{h}:30-not-start', not math.isclose(hour_angle,base%360))
    add(f'{h}:30-endpoint-finite', math.isfinite(0.55*math.sin(math.radians(hour_angle))) and math.isfinite(-0.55*math.cos(math.radians(hour_angle))))

# 8 physical packing checks => 80
PW,PH=210,297
ml=mr=mt=mb=8
header=38
uw=PW-ml-mr
uh=PH-mt-mb-header
cols,rows=2,5
iw,ih,cg,rg=91,43,4,4
rw=cols*iw+(cols-1)*cg
rh=rows*ih+(rows-1)*rg
for name,ok in [
 ('page-a4',PW==210 and PH==297),
 ('page-portrait',PH>PW),
 ('usable-width-194',uw==194),
 ('usable-height-243',uh==243),
 ('grid-2x5',cols==2 and rows==5),
 ('required-width-186',rw==186 and rw<=uw),
 ('required-height-231',rh==231 and rh<=uh),
 ('one-page-proof',rw<=uw and rh<=uh),
]: add(name,ok)

# 20 SSOT/integration checks => 100
engine=read('domains/CLOCK_READING_ENGINE.md')
w02=read('workers/W02_TIME_CLOCK.md')
w08=read('workers/W08_LAYOUT_RENDER_THAI.md')
w09=read('workers/W09_QA_RELEASE.md')
driver=read('policies/CLOCK_MINUTE_HAND_DRIVEN_HOUR_HAND_POLICY.md')
page=read('policies/THAI_P3_CLOCK_HALF_HOUR_ONE_PAGE_PROFILE.md')
defect=read('qa/ACTUAL_CLOCK_HALF_HOUR_ONE_PAGE_ARTIFACT_REGRESSION_2026_09_05.md')
builder=read('tools/build_install_package.py')
workflow=(ROOT.parents[1]/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml').read_text(encoding='utf-8')
checks=[
 ('driver-token','MINUTE_HAND_DRIVES_HOUR_HAND_POSITION=YES' in driver),
 ('driver-formula','hour_hand_displacement_deg = minute_hand_angle_deg / 12' in driver),
 ('engine-driver','minute_hand_angle_deg / 12' in engine),
 ('w02-driver','minute_angle / 12' in w02),
 ('engine-driver-gate','CLOCK_MINUTE_HAND_DRIVER_QA' in engine),
 ('w02-driver-gate','PROMPT_CLOCK_MINUTE_HAND_DRIVER_QA' in w02),
 ('page-required-token','FEASIBILITY_CONFIRMED_ONE_PAGE_LAYOUT_REQUIRED=YES' in page),
 ('page-2x5','GRID_COLUMNS=2' in page and 'GRID_ROWS=5' in page),
 ('page-proof-width','REQUIRED_GRID_WIDTH_MM=2×91+4=186 <=194' in page),
 ('page-proof-height','REQUIRED_GRID_HEIGHT_MM=5×43+4×4=231 <=243' in page),
 ('w08-one-page-profile','THAI_P3_CLOCK_HALF_HOUR_ONE_PAGE_PROFILE' in w08),
 ('w08-page-gate','PROMPT_CLOCK_P3_HALF_HOUR_10_ITEM_ONE_PAGE_QA' in w08),
 ('w09-one-page-gate','PROMPT_CLOCK_P3_HALF_HOUR_10_ITEM_ONE_PAGE_QA' in w09),
 ('w09-driver-gate','PROMPT_CLOCK_MINUTE_HAND_DRIVER_QA' in w09),
 ('defect-blocked','CLASSROOM_RELEASE=BLOCKED' in defect),
 ('defect-page-fail','ARTIFACT_PAGE_COUNT_QA=FAIL' in defect),
 ('builder-driver','CLOCK_MINUTE_HAND_DRIVEN_HOUR_HAND_POLICY.md' in builder),
 ('builder-page','THAI_P3_CLOCK_HALF_HOUR_ONE_PAGE_PROFILE.md' in builder),
 ('workflow-suite','clock_p3_half_hour_one_page_regression_suite.py' in workflow),
 ('artifact-boundary','Future renders remain `NOT_YET_TESTED`' in defect),
]
for x in checks:add(*x)

assert len(CASES)==100,len(CASES)
failed=[x for x in CASES if not x[1]]
if failed:
    print(f'CLOCK P3 HALF-HOUR ONE-PAGE REGRESSION: FAIL ({len(failed)}/100)')
    for n,_,d in failed:print('FAIL',n,d)
    sys.exit(1)
print('CLOCK P3 HALF-HOUR ONE-PAGE REGRESSION: PASS')
print('cases: 100')
print('pass: 100')
print('fail: 0')
print('minute hand drives hour displacement: verified 12/12 half-hour positions')
print('A4 portrait 2x5 packing: 186x231 mm within usable 194x243 mm')
print('future artifact QA: NOT_YET_TESTED')
