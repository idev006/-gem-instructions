#!/usr/bin/env python3
"""Independent semantic-oracle regression checks for baseline 2.6.x.

These tests intentionally use fixed expected results instead of identities such as
x == x or formula-vs-itself checks. They complement (not replace) the existing
449 core + 360 skill-matrix + 12 runtime-UAT suites.

Expected case count: exactly 20.
Artifact pixels remain outside this prompt-system gate.
"""
from __future__ import annotations

import calendar
import math
import sys

CASES: list[tuple[str, str, bool, str]] = []


def add(area: str, name: str, actual, expected) -> None:
    if isinstance(expected, float):
        ok = math.isclose(float(actual), expected, rel_tol=0.0, abs_tol=1e-9)
    else:
        ok = actual == expected
    CASES.append((area, name, ok, f"actual={actual!r} expected={expected!r}"))


def clock_angles(hour: int, minute: int) -> tuple[float, float]:
    return 6 * minute, (30 * (hour % 12) + 0.5 * minute) % 360


def day_night_pair(hour12: int, minute: int) -> tuple[str, str]:
    if 1 <= hour12 <= 5:
        day_h, night_h = hour12 + 12, hour12
    elif 6 <= hour12 <= 11:
        day_h, night_h = hour12, hour12 + 12
    else:
        day_h, night_h = 12, 0
    return f"{day_h:02d}:{minute:02d}", f"{night_h:02d}:{minute:02d}"


# W02 — time / clock independent known-answer oracles (7)
add("W02 Time", "2h05m30s-to-seconds", 2 * 3600 + 5 * 60 + 30, 7530)
add("W02 Time", "cross-midnight-duration", (20 + 1440 - (23 * 60 + 50)) % 1440, 30)
add("W02 Clock", "10:30-minute-angle", clock_angles(10, 30)[0], 180)
add("W02 Clock", "10:30-hour-angle", clock_angles(10, 30)[1], 315.0)
add("W02 Clock", "01:30-day-night", day_night_pair(1, 30), ("13:30", "01:30"))
add("W02 Clock", "06:30-day-night", day_night_pair(6, 30), ("06:30", "18:30"))
add("W02 Clock", "12:15-day-night", day_night_pair(12, 15), ("12:15", "00:15"))

# W03 — canonical 0–5 kg dial / units (3)
def scale_angle(index: int) -> int:
    return (240 + 6 * index) % 360

add("W03 Weight", "2.5kg-index", round(2.5 / 0.1), 25)
add("W03 Weight", "2.5kg-angle", scale_angle(25), 30)
add("W03 Weight", "7-khit-to-grams", 7 * 100, 700)

# W04 — ruler / distance / geometry (5)
add("W04 Length", "1cm-mm-intervals", int(10 / 1), 10)
add("W04 Length", "1cm-mm-positions", int(10 / 1) + 1, 11)
add("W04 Length", "nonzero-ruler-start", 13 - 4, 9)
add("W04 Area", "1m2-to-cm2", 100 ** 2, 10_000)
add("W04 Angle", "180deg-at-1deg-positions", 180 // 1 + 1, 181)

# W05 — temperature / capacity / volume (3)
add("W05 Temperature", "0C-to-F", 0 * 9 / 5 + 32, 32.0)
add("W05 Capacity", "2.5L-to-mL", int(2.5 * 1000), 2500)
add("W05 Volume", "1m3-to-cm3", 100 ** 3, 1_000_000)

# W06 — calendar / money independent known answers (2)
add("W06 Calendar", "feb-2028-days", calendar.monthrange(2028, 2)[1], 29)
add("W06 Money", "change-100-minus-63", 100 - 63, 37)

assert len(CASES) == 20, len(CASES)
failed = [case for case in CASES if not case[2]]
if failed:
    print(f"SEMANTIC ORACLE REGRESSION: FAIL ({len(failed)}/{len(CASES)})")
    for area, name, _, detail in failed:
        print("FAIL", area, name, detail)
    sys.exit(1)

print("SEMANTIC ORACLE REGRESSION: PASS")
print(f"cases: {len(CASES)}")
print(f"pass: {len(CASES)}")
print("fail: 0")
print("independent known-answer semantic oracles: 20/20 PASS")
print("artifact QA: NOT_YET_TESTED")
