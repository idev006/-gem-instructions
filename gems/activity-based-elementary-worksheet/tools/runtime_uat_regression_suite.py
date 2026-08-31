#!/usr/bin/env python3
"""Runtime UAT-derived regression checks for known installed-Gem failures.

These checks encode failures observed from real Gem output so future packages
cannot omit the corresponding top-level runtime instructions.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
profile = (ROOT / "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md").read_text(encoding="utf-8")
builder = (ROOT / "tools/build_install_package.py").read_text(encoding="utf-8")
w02 = (ROOT / "workers/W02_TIME_CLOCK.md").read_text(encoding="utf-8")
w09 = (ROOT / "workers/W09_QA_RELEASE.md").read_text(encoding="utf-8")

checks = [
    ("thai-p3-auto-day-night", "CLOCK_READING_MODE=DAY_NIGHT_PAIR" in profile),
    ("one-clock-two-answers", "ONE_CLOCK_TWO_ANSWERS=YES" in profile and "ANSWER_FIELDS_PER_QUESTION=2" in profile),
    ("two-visible-blanks", "กลางวัน ........ น. | กลางคืน ........ น." in profile),
    ("strict-half-hour-set", "TARGET_MINUTE_SET={30}" in profile),
    ("page-lock-default-off", "ONE_PAGE_LOCK=OFF" in profile),
    ("page-lock-explicit-only", "explicitly requests a one-page lock" in profile),
    ("numeric-minute-angle", "minute_angle=180°" in profile),
    ("numeric-hour-angle", "hour_angle=(30*(h mod 12)+15) mod 360" in profile),
    ("no-topology-degradation", "do not reduce to only 5-minute ticks" in profile),
    ("profile-embedded-main", "MANDATORY RUNTIME PROFILE: THAI P3 ANALOG CLOCK" in builder),
    ("profile-embedded-w02-w09", builder.count("policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md") >= 3),
    ("w02-w09-consistent", "Thai Grade 3 analog-clock reading" in w02 and "Thai Grade 3 analog-clock requests" in w09),
]

failed = [name for name, ok in checks if not ok]
if failed:
    print(f"RUNTIME UAT REGRESSION: FAIL ({len(failed)}/{len(checks)})")
    for name in failed: print("FAIL", name)
    sys.exit(1)

print("RUNTIME UAT REGRESSION: PASS")
print(f"cases: {len(checks)}")
print(f"pass: {len(checks)}")
print("fail: 0")
print("known installed-Gem clock regressions: 12/12 PASS")
print("artifact QA: NOT_YET_TESTED")
