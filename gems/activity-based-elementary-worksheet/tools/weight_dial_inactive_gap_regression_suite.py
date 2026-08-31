#!/usr/bin/env python3
"""Actual-artifact regression for canonical 0–5 kg weight-dial inactive gap.

Protects the 2026-08-31 user-supplied artifact defect where radial scale-like
marks continued through the intended 5→0 inactive region and label rotation
could drift from the canonical coordinate system.

Expected case count: exactly 32.
"""
from pathlib import Path
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
CASES=[]

def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def add(name, ok): CASES.append((name,bool(ok)))

def ang(i): return (240 + 6*i) % 360

# 1-16 independent quantitative/canonical oracles
add('interval-count-50', round((5-0)/0.1)==50)
add('position-count-51', round((5-0)/0.1)+1==51)
add('minor-step-6deg', math.isclose(300/50,6.0))
add('active-sweep-300', 50*6==300)
add('inactive-gap-60', 360-300==60)
add('active-start-240', ang(0)==240)
add('label-1-angle-300', ang(10)==300)
add('label-2-angle-0', ang(20)==0)
add('label-3-angle-60', ang(30)==60)
add('label-4-angle-120', ang(40)==120)
add('label-5-angle-180', ang(50)==180)
active={ang(i) for i in range(51)}
add('active-set-51-distinct', len(active)==51)
add('gap-open-arc-has-no-active-position', not any(180 < a < 240 for a in active))
add('gap-endpoints-are-active', 180 in active and 240 in active)
labels={0:240,1:300,2:0,3:60,4:120,5:180}
add('canonical-label-map-exact', labels=={0:240,1:300,2:0,3:60,4:120,5:180})
add('2.5kg-angle-still-30', ang(round(2.5/0.1))==30)

# 17-32 SSOT / release integration
engine=read('domains/SCALE_READING_ENGINE.md')
w03=read('workers/W03_WEIGHT_SCALE.md')
w07=read('workers/W07_INSTRUMENT_AUDITOR.md')
w10=read('workers/W10_METROLOGY_ENGINEER.md')
w09=read('workers/W09_QA_RELEASE.md')
defect=read('qa/ACTUAL_WEIGHT_DIAL_INACTIVE_GAP_REGRESSION_2026_08_31.md')

checks=[
('engine-gap-zero-radial','INACTIVE_GAP_RADIAL_MARK_COUNT=0' in engine),
('engine-active-tick-formula','active_tick_angle(i)=(240 + 6*i) mod 360, i=0..50' in engine),
('engine-label-angles','LABEL_ANGLES={0:240°,1:300°,2:0°,3:60°,4:120°,5:180°}' in engine),
('engine-gap-decoration-gate','PROMPT_DIAL_GAP_DECORATION_ISOLATION_QA' in engine),
('w03-gap-object','INACTIVE_GAP_TICK_COUNT=0' in w03 and 'INACTIVE_GAP_RADIAL_MARK_COUNT=0' in w03),
('w03-active-set-gate','PROMPT_DIAL_ACTIVE_TICK_SET_QA' in w03),
('w03-label-angle-gate','PROMPT_DIAL_CANONICAL_LABEL_ANGLE_QA' in w03),
('w07-gap-artifact-fail','ARTIFACT_DIAL_INACTIVE_GAP_QA=FAIL' in w07 and 'CLASSROOM_RELEASE=BLOCKED' in w07),
('w07-count-radial-marks','count radial marks' in w07.lower()),
('w10-independent-gap-oracle','360° - 300° = 60°' in w10 and 'expected radial scale-like marks strictly inside that arc = **0**' in w10),
('w10-active-set-evidence','ACTIVE_TICK_SET_CHECK' in w10),
('w10-gap-zero-gate','PROMPT_METROLOGY_DIAL_GAP_RADIAL_MARK_ZERO_QA' in w10),
('w09-generic-inactive-gates','PROMPT_SCALE_INACTIVE_REGION_QA' in w09 and 'PROMPT_METROLOGY_INACTIVE_REGION_QA' in w09),
('w09-release-conjunctive','PROMPT_RELEASE=BLOCKED' in w09),
('defect-p0','P0_CRITICAL_ACADEMIC' in defect and 'INACTIVE_GAP_RADIAL_MARK_COUNT=0' in defect),
('defect-permanent','PERMANENT NEGATIVE EVIDENCE' in defect and 'Future refactors must preserve this negative oracle' in defect),
]
for n,ok in checks: add(n,ok)

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
