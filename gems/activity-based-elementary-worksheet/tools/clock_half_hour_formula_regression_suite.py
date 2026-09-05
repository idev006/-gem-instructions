#!/usr/bin/env python3
"""Clock half-hour formula regression.

Guards the common artifact failure where the minute hand points to 6 for :30,
but the short/hour hand is visually snapped to the starting hour numeral instead
of being exactly halfway to the next numeral.

This validates the formula oracle, the minute-hand-driven displacement model,
and required SSOT tokens. It does not replace actual rendered Artifact QA.
"""
from pathlib import Path
import math, sys

ROOT = Path(__file__).resolve().parents[1]

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding='utf-8')

CASES = []
def add(name: str, ok: bool, detail: str = ''):
    CASES.append((name, bool(ok), detail))

# Formula oracle for all 12 half-hour positions: 12 * 5 = 60 checks
for h in range(1, 13):
    m = 30
    hour_mod = h % 12
    minute_angle = 6 * m
    hour_angle = 30 * hour_mod + 0.5 * m
    start_angle = 30 * hour_mod
    next_angle = (start_angle + 30) % 360
    expected_mid = (start_angle + 15) % 360
    add(f'{h}:30-minute-angle', math.isclose(minute_angle, 180.0), f'{minute_angle}')
    add(f'{h}:30-hour-midpoint-angle', math.isclose(hour_angle % 360, expected_mid), f'{hour_angle} vs {expected_mid}')
    add(f'{h}:30-hour-displacement', math.isclose((hour_angle - start_angle) % 360, 15.0), f'{hour_angle-start_angle}')
    add(f'{h}:30-not-snapped-start', not math.isclose(hour_angle % 360, start_angle % 360), f'{hour_angle} vs {start_angle}')
    add(f'{h}:30-not-snapped-next', not math.isclose(hour_angle % 360, next_angle % 360), f'{hour_angle} vs {next_angle}')

# Minute-hand-driven oracle: 12 * 1 = 12 checks.
# This directly encodes the user's correction: the long/minute hand is the input
# that determines short/hour-hand displacement.
for h in range(1, 13):
    m = 30
    minute_angle = 6 * m
    hour_sector_base = 30 * (h % 12)
    hour_displacement = minute_angle / 12
    driven_hour_angle = hour_sector_base + hour_displacement
    direct_formula_hour_angle = 30 * (h % 12) + 0.5 * m
    add(
        f'{h}:30-minute-hand-drives-hour-hand',
        math.isclose(driven_hour_angle % 360, direct_formula_hour_angle % 360)
        and math.isclose(hour_displacement, 15.0),
        f'driven={driven_hour_angle}, direct={direct_formula_hour_angle}, displacement={hour_displacement}'
    )

clock = read('domains/CLOCK_READING_ENGINE.md')
w02 = read('workers/W02_TIME_CLOCK.md')
metric = read('skill-metrics/ANALOG_CLOCK_SKILL_METRICS.md')
defect = read('qa/ACTUAL_CLOCK_HALF_HOUR_FORMULA_ARTIFACT_REGRESSION_2026_09_05.md')
minute_driver = read('policies/CLOCK_MINUTE_HAND_DRIVEN_HOUR_HAND_POLICY.md')

# 12 existing SSOT/documentation checks
required = [
    ('engine-minute-formula', 'minute_hand_angle_deg = 6*m' in clock),
    ('engine-hour-formula', 'hour_hand_angle_deg = 30*(h mod 12) + 0.5*m' in clock),
    ('engine-halfway-rule', 'm=30' in clock and 'exactly halfway' in clock),
    ('engine-anti-snap', 'DO NOT snap/approximate/reposition' in clock),
    ('engine-endpoint', 'hour_endpoint' in clock and 'sin' in clock and 'cos' in clock),
    ('qa-gate-half-hour', 'HALF_HOUR_MIDPOINT_QA' in clock),
    ('metric-half-hour-critical', 'snap' in metric.lower() and 'wrong minute hand' in metric.lower()),
    ('defect-critical', 'Status: CRITICAL_ACADEMIC' in defect),
    ('defect-1530', '3:30 / 15:30' in defect and '105°' in defect),
    ('defect-1230', '12:30 / 00:30' in defect and '15°' in defect),
    ('defect-release-block', 'CLASSROOM_RELEASE=BLOCKED' in defect),
    ('defect-artifact-boundary', 'does not by itself certify future rendered worksheets' in defect),
]
for name, ok in required:
    add(name, ok)

# 12 minute-hand-driver SSOT checks; total 84
minute_driver_required = [
    ('policy-minute-driver-token', 'MINUTE_HAND_DRIVES_HOUR_HAND_POSITION=YES' in minute_driver),
    ('policy-compute-minute-first', 'Compute in this order' in minute_driver and 'minute_hand_angle_deg = 6*M' in minute_driver),
    ('policy-displacement-from-minute-angle', 'hour_hand_displacement_deg = minute_hand_angle_deg / 12' in minute_driver),
    ('policy-equivalent-formula', 'hour_hand_angle_deg = 30*(H mod 12) + 0.5*M' in minute_driver),
    ('policy-1530-example', '15:30 / 3:30' in minute_driver and 'hour_hand_angle_deg = 90+15 = 105°' in minute_driver),
    ('policy-hard-negative-not-hour-alone', 'Do not place the hour hand by choosing the nearest hour numeral' in minute_driver),
    ('policy-no-300-plus-minute', 'Do not treat `3:30` as `3:00` plus a minute hand' in minute_driver),
    ('policy-qa-gate', 'PROMPT_CLOCK_MINUTE_HAND_DRIVER_QA' in minute_driver),
    ('w02-minute-driver-compatible', 'minute_angle=6*m' in w02 and 'hour_angle=30*(h mod 12)+0.5*m' in w02),
    ('w02-displacement-compatible', 'HOUR_DISPLACEMENT_FROM_START_HOUR_DEG = 0.5*m' in w02),
    ('engine-displacement-compatible', 'abs(hour_hand_angle_deg - 30*(h mod 12)) = 0.5*m' in clock),
    ('engine-artifact-block-compatible', 'CRITICAL_ACADEMIC' in clock and 'blocks release' in clock),
]
for name, ok in minute_driver_required:
    add(name, ok)

assert len(CASES) == 96, len(CASES)
failed = [c for c in CASES if not c[1]]
if failed:
    print(f'CLOCK HALF-HOUR FORMULA REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n, _, d in failed:
        print('FAIL', n, d)
    sys.exit(1)
print('CLOCK HALF-HOUR FORMULA REGRESSION: PASS')
print('cases: 96')
print('pass: 96')
print('fail: 0')
print('half-hour formula oracle: 12/12 hours verified')
print('minute-hand-driven oracle: hour displacement = minute_angle / 12')
print('15:30 oracle: minute=180°, hour=105°, hour hand halfway between 3 and 4')
print('artifact QA: supplied defective artifact remains FAIL; future renders NOT_YET_TESTED')
