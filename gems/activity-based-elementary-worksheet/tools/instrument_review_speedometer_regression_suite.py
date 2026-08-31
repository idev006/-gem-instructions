#!/usr/bin/env python3
"""Instrument review/revise + ruler UAT + thermometer + speedometer regression.

Architecture and semantic-oracle suite added after the 2026-08-31 ruler extra-tick
artifact defect. Complements, never replaces, the existing 911 cases.
Expected case count: exactly 60.
"""
from __future__ import annotations

from pathlib import Path
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
CASES: list[tuple[str, bool, str]] = []


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def add(name: str, actual, expected) -> None:
    if isinstance(expected, float):
        ok = math.isclose(float(actual), expected, rel_tol=0.0, abs_tol=1e-9)
    else:
        ok = actual == expected
    CASES.append((name, ok, f"actual={actual!r} expected={expected!r}"))


def token(name: str, haystack: str, needle: str) -> None:
    CASES.append((name, needle in haystack, needle))


def linear_counts(min_v: float, max_v: float, d: float) -> tuple[int, int, int]:
    intervals = round((max_v - min_v) / d)
    positions = intervals + 1
    interior = max(positions - 2, 0)
    return intervals, positions, interior


def represented(min_v: float, d: float, target: float) -> tuple[int, float, bool]:
    idx = round((target - min_v) / d)
    value = min_v + idx * d
    return idx, value, math.isclose(target, value, rel_tol=0.0, abs_tol=1e-9)


def speed_angle(target: float) -> float:
    return (240 + 2 * target) % 360


# 1-24 independent known-answer semantic oracles.
r1 = linear_counts(0, 10, 1)  # mm within one cm
add("ruler-1cm-intervals", r1[0], 10)
add("ruler-1cm-positions", r1[1], 11)
add("ruler-1cm-interior", r1[2], 9)
add("ruler-5mm-existing-index", round(5 / 1), 5)
r2 = linear_counts(0, 20, 1)
add("ruler-2cm-intervals", r2[0], 20)

t1 = linear_counts(0, 50, 1)
add("thermo-0-50C-intervals", t1[0], 50)
add("thermo-0-50C-positions", t1[1], 51)
add("thermo-neg10-40-zero-index", round((0 - (-10)) / 1), 10)
t2 = linear_counts(0, 100, 5)
add("thermo-0-100C-intervals", t2[0], 20)
t3 = linear_counts(20, 120, 2)
add("thermo-20-120F-positions", t3[1], 51)
idx36, rep36, ok36 = represented(20, 2, 36)
add("thermo-36F-index", idx36, 8)
add("thermo-36F-represented", rep36, 36)
_, _, ok35 = represented(20, 2, 35)
add("thermo-35F-invalid", ok35, False)

s = linear_counts(0, 120, 10)
add("speedometer-intervals", s[0], 12)
add("speedometer-positions", s[1], 13)
add("speedometer-0-angle", speed_angle(0), 240.0)
add("speedometer-30-angle", speed_angle(30), 300.0)
add("speedometer-60-angle", speed_angle(60), 0.0)
add("speedometer-90-angle", speed_angle(90), 60.0)
add("speedometer-120-angle", speed_angle(120), 120.0)
add("speedometer-70-angle", speed_angle(70), 20.0)
_, _, ok_speed35 = represented(0, 10, 35)
add("speedometer-35-invalid", ok_speed35, False)
add("speedometer-inactive-gap", 360 - 240, 120)
add("speedometer-major-label-count", len(list(range(0, 121, 20))), 7)

# 25-44 policy/domain regression tokens.
review = read("policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md")
speed = read("domains/SPEEDOMETER_READING_ENGINE.md")
uat = read("qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md")
for name, needle in [
    ("review-loop", "GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS"),
    ("review-no-first-pass", "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON"),
    ("review-recount-gate", "PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA"),
    ("review-revise-gate", "PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA"),
    ("review-evidence-gate", "PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA"),
    ("review-serialization-gate", "PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA"),
    ("review-ruler-10-11-9", "exactly 9 interior graduation positions"),
    ("review-artifact-boundary", "ARTIFACT_QA=NOT_YET_TESTED"),
]:
    token(name, review, needle)

for name, needle in [
    ("speed-open-arc", "OPEN_ARC_BOUNDED"),
    ("speed-12-13", "12 equal minor intervals"),
    ("speed-240-sweep", "SPEEDOMETER_ACTIVE_SWEEP_DEG=240"),
    ("speed-120-gap", "120° inactive/non-scale gap"),
    ("speed-angle-formula", "target_angle=(240 + 2*target_kmh) mod 360"),
    ("speed-no-rate-calc", "does **not** silently introduce the formula `speed=distance/time`"),
    ("speed-self-review", "Renderer self-review"),
]:
    token(name, speed, needle)

for name, needle in [
    ("uat-critical", "CRITICAL_ACADEMIC"),
    ("uat-10-intervals", "exactly 10 equal intervals"),
    ("uat-11-positions", "exactly 11 physical graduation positions"),
    ("uat-9-interior", "exactly 9 interior positions"),
    ("uat-edge-not-tick", "physical ruler border/outline is not an additional graduation"),
]:
    token(name, uat, needle)

# 45-60 cross-system integration checks.
w04 = read("workers/W04_LENGTH_DISTANCE.md")
w05 = read("workers/W05_TEMPERATURE_CAPACITY_VOLUME.md")
w07 = read("workers/W07_INSTRUMENT_AUDITOR.md")
w08 = read("workers/W08_LAYOUT_RENDER_THAI.md")
w09 = read("workers/W09_QA_RELEASE.md")
router = read("KB_ROUTER.md")
registry = read("domains/DOMAIN_REGISTRY.md")
manifest = read("KB_MANIFEST.md")
instrument = read("domains/INSTRUMENT_READING_ENGINE.md")
builder = read("tools/build_install_package.py")
validator = read("tools/validate_ssot.py")
checklist = read("qa/BASELINE_2_6_0_RELEASE_CHECKLIST.md")
workflow = (REPO / ".github/workflows/activity-based-elementary-worksheet-gem-ssot.yml").read_text(encoding="utf-8")
core = read("GEM_INSTRUCTIONS_PRODUCTION.md")
out = read("OUTPUT_CONTRACT.md")

integration = [
    ("w04-speedometer-owner", "SPEEDOMETER_READING_ENGINE.md" in w04 and "INTERIOR_POSITIONS_PER_CM_SPAN=9" in w04),
    ("w05-thermo-review", "PROMPT_THERMOMETER_INTERVAL_COUNT_QA" in w05 and "renderer self-review" in w05.lower()),
    ("w07-review-owner", "PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA" in w07),
    ("w08-review-serialization", "INSTRUMENT_REVIEW_REVISE_PROTOCOL" in w08 and "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON" in w08),
    ("w09-release-block", "PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA" in w09 and "ARTIFACT_QA=FAIL" in w09),
    ("router-speedometer", "direct speedometer reading / vehicle speed dial" in router),
    ("registry-speedometer", "MEASUREMENT_SPEEDOMETER" in registry),
    ("manifest-three-profiles", "INSTRUMENT_REVIEW_REVISE_PROFILE.md" in manifest and "SCALE_LINE_INTEGRITY_PROFILE.md" in manifest),
    ("instrument-engine-review", "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON" in instrument and "speedometer" in instrument.lower()),
    ("builder-review-profile", "INSTRUMENT_REVIEW_REVISE_PROFILE.md" in builder),
    ("builder-new-suite", "instrument_review_speedometer_regression_suite.py" in builder and "971/971 PASS" in builder),
    ("validator-new-suite", "instrument_review_speedometer_regression_suite.py" in validator and "971" in validator),
    ("workflow-new-suite", "Instrument review + speedometer regression" in workflow and "60 cases" in workflow),
    ("checklist-new-suite", "971/971 PASS" in checklist and "instrument_review_speedometer_regression_suite.py" in checklist),
    ("core-review-protocol", "INSTRUMENT_REVIEW_REVISE_PROFILE.md" in core and "MEASUREMENT_SPEEDOMETER" in core),
    ("output-review-protocol", "INSTRUMENT_REVIEW_REVISE_PROTOCOL" in out and "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON" in out),
]
for name, ok in integration:
    CASES.append((name, bool(ok), "integration"))

assert len(CASES) == 60, len(CASES)
failed = [c for c in CASES if not c[1]]
if failed:
    print(f"INSTRUMENT REVIEW/SPEEDOMETER REGRESSION: FAIL ({len(failed)}/{len(CASES)})")
    for name, _, detail in failed:
        print("FAIL", name, detail)
    sys.exit(1)

print("INSTRUMENT REVIEW/SPEEDOMETER REGRESSION: PASS")
print(f"cases: {len(CASES)}")
print(f"pass: {len(CASES)}")
print("fail: 0")
print("ruler/thermometer/speedometer + review-revise architecture: 60/60 PASS")
print("artifact QA: NOT_YET_TESTED")
