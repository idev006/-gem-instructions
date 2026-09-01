#!/usr/bin/env python3
"""Permanent regression for analog-clock hand endpoint geometry.

Derived from actual rendered artifact defect on 2026-09-01.
Additive only. Expected case count: exactly 32.
"""
from pathlib import Path
import math,sys
ROOT=Path(__file__).resolve().parents[1]
CASES=[]
def add(name,ok,detail=''):CASES.append((name,bool(ok),detail))
def read(rel):return (ROOT/rel).read_text(encoding='utf-8')
def hour_angle(h,m):return (30*(h%12)+0.5*m)%360
def minute_angle(m):return (6*m)%360
def endpoint(theta,length):
    r=math.radians(theta)
    return (length*math.sin(r),-length*math.cos(r))
def close(a,b,tol=1e-9):return math.isclose(a,b,abs_tol=tol,rel_tol=0)

# 1-18 numeric geometry checkpoints
samples=[
    (1,15,37.5),(3,30,105.0),(9,30,285.0),(2,45,82.5),(8,45,262.5),(11,45,352.5)
]
for h,m,expected in samples:
    add(f'angle-{h:02d}-{m:02d}',close(hour_angle(h,m),expected),f'{hour_angle(h,m)}')
for h,m,_ in samples:
    whole=(30*(h%12))%360
    add(f'anti-snap-{h:02d}-{m:02d}',not close(hour_angle(h,m),whole),f'whole={whole} actual={hour_angle(h,m)}')
for h,m,_ in [(3,30,105.0),(9,30,285.0),(2,45,82.5)]:
    x,y=endpoint(hour_angle(h,m),0.55)
    mag=math.hypot(x,y)
    add(f'endpoint-radius-{h:02d}-{m:02d}',close(mag,0.55),f'mag={mag}')
add('minute-30-angle',close(minute_angle(30),180.0))
add('minute-45-angle',close(minute_angle(45),270.0))
add('minute-length',close(math.hypot(*endpoint(180,0.78)),0.78))

# 19-24 relational displacement checkpoints
for m,expected in [(15,7.5),(30,15.0),(45,22.5)]:
    add(f'displacement-{m}',close(0.5*m,expected))
add('half-sector-ratio',close((hour_angle(3,30)-90)/30,0.5))
add('quarter-sector-ratio',close((hour_angle(1,15)-30)/30,0.25))
add('three-quarter-sector-ratio',close((hour_angle(2,45)-60)/30,0.75))

# 25-32 SSOT integration
engine=read('domains/CLOCK_READING_ENGINE.md')
w02=read('workers/W02_TIME_CLOCK.md')
review=read('policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md')
defect=read('qa/ACTUAL_CLOCK_HAND_ENDPOINT_REGRESSION_2026_09_01.md')
checks=[
('engine-vector','minute_endpoint' in engine and 'hour_endpoint' in engine and '0.78' in engine and '0.55' in engine),
('engine-anti-snap','Anti-snap oracle' in engine and '0.5*m' in engine),
('engine-required-fields','MINUTE_ENDPOINT_NORMALIZED' in engine and 'HOUR_ENDPOINT_NORMALIZED' in engine),
('w02-vector','MINUTE_ENDPOINT_NORMALIZED' in w02 and 'HOUR_ENDPOINT_NORMALIZED' in w02),
('w02-gates','PROMPT_CLOCK_VECTOR_ENDPOINT_QA' in w02 and 'PROMPT_CLOCK_ANTI_SNAP_QA' in w02),
('shared-review','deterministic vector geometry' in review.lower() and '3:30 must be 105°' in review),
('defect-status','CRITICAL_ACADEMIC' in defect and 'ARTIFACT_CLOCK_HAND_ENDPOINT_QA=FAIL' in defect),
('defect-blocks','CLASSROOM_RELEASE=BLOCKED' in defect),
]
for n,o in checks:add(n,o)

assert len(CASES)==32,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'CLOCK HAND ENDPOINT REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_,d in failed:print('FAIL',n,d)
    sys.exit(1)
print('CLOCK HAND ENDPOINT REGRESSION: PASS')
print('cases: 32')
print('pass: 32')
print('fail: 0')
print('continuous angle + deterministic endpoint + anti-snap geometry: 32/32 PASS')
print('artifact QA: supplied defective clock artifact remains FAIL; future renders NOT_YET_TESTED')
