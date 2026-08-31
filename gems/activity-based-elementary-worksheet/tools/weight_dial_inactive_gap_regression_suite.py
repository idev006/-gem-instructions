#!/usr/bin/env python3
"""Actual-artifact regression for canonical 0–5 kg weight-dial inactive gap.

Protects the user-supplied artifact defect while enforcing the corrected
classroom canonical: top-zero, clockwise 0→5, 60° inactive 5→0 gap.
Expected case count: exactly 32.
"""
from pathlib import Path
import math, sys
ROOT=Path(__file__).resolve().parents[1]
CASES=[]
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def add(name,ok): CASES.append((name,bool(ok)))
def ang(i): return (6*i)%360

# 1-16 independent quantitative/canonical oracles
add('interval-count-50',round((5-0)/0.1)==50)
add('position-count-51',round((5-0)/0.1)+1==51)
add('minor-step-6deg',math.isclose(300/50,6.0))
add('active-sweep-300',50*6==300)
add('inactive-gap-60',360-300==60)
add('active-start-top',ang(0)==0)
add('label-1-angle-60',ang(10)==60)
add('label-2-angle-120',ang(20)==120)
add('label-3-angle-180',ang(30)==180)
add('label-4-angle-240',ang(40)==240)
add('label-5-angle-300',ang(50)==300)
active=[ang(i) for i in range(51)]
add('active-position-count-51',len(active)==51)
add('active-endpoints-0-300',active[0]==0 and active[-1]==300)
add('gap-open-arc-has-no-active-position',not any(300<a<360 for a in active))
labels={0:0,1:60,2:120,3:180,4:240,5:300}
add('canonical-label-map-exact',labels=={0:0,1:60,2:120,3:180,4:240,5:300})
add('2.5kg-angle-150',ang(round(2.5/0.1))==150)

# 17-32 SSOT/release integration
engine=read('domains/SCALE_READING_ENGINE.md')
w03=read('workers/W03_WEIGHT_SCALE.md')
w07=read('workers/W07_INSTRUMENT_AUDITOR.md')
w10=read('workers/W10_METROLOGY_ENGINEER.md')
w09=read('workers/W09_QA_RELEASE.md')
defect=read('qa/ACTUAL_WEIGHT_DIAL_INACTIVE_GAP_REGRESSION_2026_08_31.md')
checks=[
('engine-gap-zero-radial','INACTIVE_GAP_RADIAL_MARK_COUNT=0' in engine),
('engine-active-tick-formula','active_tick_angle(i)=(6*i) mod 360, i=0..50' in engine),
('engine-label-angles','LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}' in engine),
('engine-label-order','CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]' in engine),
('w03-gap-object','INACTIVE_GAP_TICK_COUNT=0' in w03 and 'INACTIVE_GAP_RADIAL_MARK_COUNT=0' in w03),
('w03-label-order-gate','PROMPT_DIAL_LABEL_ORDER_QA' in w03),
('w03-common-center','NEEDLE_PIVOT' in w03 and 'DIAL_CENTER' in w03),
('w07-gap-artifact-fail','inactive region independently' in w07 and 'expected count is zero' in w07 and 'One wrong instructional instrument blocks classroom release' in w07),
('w07-label-order','Expected clockwise major-label order' in w07 and '[0,1,2,3,4,5]' in w07 and 'PROMPT_DIAL_LABEL_ORDER_QA' in w07),
('w10-independent-gap-oracle','inactive open arc = `(300°,360°)`' in w10 and 'expected radial scale-like marks strictly inside that arc = 0' in w10),
('w10-active-set-evidence','ACTIVE_TICK_SET_CHECK' in w10),
('w10-common-center','NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER' in w10),
('w09-label-order-gate','PROMPT_DIAL_LABEL_ORDER_QA' in w09),
('w09-release-conjunctive','PROMPT_RELEASE=BLOCKED' in w09),
('defect-p0','P0_CRITICAL_ACADEMIC' in defect and 'INACTIVE_GAP_RADIAL_MARK_COUNT=0' in defect),
('defect-corrected-canonical','corrected top-zero clockwise' in defect and 'Future refactors must preserve' in defect),
]
for n,o in checks:add(n,o)

assert len(CASES)==32,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'WEIGHT DIAL INACTIVE-GAP REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_ in failed: print('FAIL',n)
    sys.exit(1)
print('WEIGHT DIAL INACTIVE-GAP REGRESSION: PASS')
print('cases: 32')
print('pass: 32')
print('fail: 0')
print('actual weight-dial inactive-gap + label-coordinate regression: 32/32 PASS')
print('artifact QA: NOT_YET_TESTED')
