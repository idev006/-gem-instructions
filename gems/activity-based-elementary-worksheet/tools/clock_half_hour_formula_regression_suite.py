#!/usr/bin/env python3
"""Clock half-hour formula regression.

Guards the common artifact failure where the minute hand points to 6 for :30,
but the short/hour hand is visually snapped to the starting hour numeral instead
of being exactly halfway to the next numeral.

This validates the formula oracle and required SSOT tokens. It does not replace
actual rendered Artifact QA.
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

clock = read('domains/CLOCK_READING_ENGINE.md')
metric = read('skill-metrics/ANALOG_CLOCK_SKILL_METRICS.md')
defect = read('qa/ACTUAL_CLOCK_HALF_HOUR_FORMULA_ARTIFACT_REGRESSION_2026_09_05.md')

# 12 SSOT/documentation checks, total 72
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

assert len(CASES) == 72, len(CASES)
failed = [c for c in CASES if not c[1]]
if failed:
    print(f'CLOCK HALF-HOUR FORMULA REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n, _, d in failed:
        print('FAIL', n, d)
    sys.exit(1)
print('CLOCK HALF-HOUR FORMULA REGRESSION: PASS')
print('cases: 72')
print('pass: 72')
print('fail: 0')
print('half-hour formula oracle: 12/12 hours verified')
print('15:30 oracle: minute=180°, hour=105°, hour hand halfway between 3 and 4')
print('artifact QA: supplied defective artifact remains FAIL; future renders NOT_YET_TESTED')
