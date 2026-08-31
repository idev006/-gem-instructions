#!/usr/bin/env python3
"""Protractor scale-placement safety regression.

Protects the 2026-08-31 UAT finding that a nominally correct 0–180° @1°
protractor can still be academically unsafe when its printed tick ring is too
small or its active scale/render path is ambiguous.

Expected case count: exactly 24.
"""
from pathlib import Path
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
CASES = []

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")

def add(name: str, ok: bool) -> None:
    CASES.append((name, bool(ok)))

def arc_spacing(diameter_mm: float, interval_deg: float) -> float:
    return (diameter_mm / 2.0) * math.radians(interval_deg)

profile = read("policies/SCALE_LINE_INTEGRITY_PROFILE.md")
w04 = read("workers/W04_LENGTH_DISTANCE.md")
w08 = read("workers/W08_LAYOUT_RENDER_THAI.md")
w09 = read("workers/W09_QA_RELEASE.md")

add("topology-1deg-intervals", 180 // 1 == 180)
add("topology-1deg-positions", 180 // 1 + 1 == 181)
add("spacing-65mm-below-floor", arc_spacing(65.0, 1.0) < 0.60)
add("spacing-65mm-known-value", math.isclose(arc_spacing(65.0, 1.0), 0.5672320069, rel_tol=0, abs_tol=1e-6))
add("spacing-70mm-passes-floor", arc_spacing(70.0, 1.0) >= 0.60)
min_radius = 0.60 / math.radians(1.0)
add("minimum-radius-oracle", math.isclose(min_radius, 34.3774677, rel_tol=0, abs_tol=1e-6))
add("minimum-diameter-oracle", math.isclose(2 * min_radius, 68.7549354, rel_tol=0, abs_tol=1e-6))
add("production-rounding-70", 70.0 >= 2 * min_radius and 69.0 >= 2 * min_radius)

add("profile-spacing-formula", "tick_center_spacing_mm = reading_radius_mm × radians(MINOR_INTERVAL_DEG)" in profile)
add("profile-production-70", "PRODUCTION_MIN_PROTRACTOR_WIDTH_MM = 70 mm" in profile)
add("profile-rejects-65", "65 mm diameter protractor fails" in profile)
add("profile-active-scale", "mirrored competing inner scale is forbidden" in profile)
add("profile-render-auto-forbidden", "unresolved `RENDER_PATH=AUTO` is forbidden" in profile)

add("w04-spacing-oracle", "MIN_READING_RING_DIAMETER_MM ≈ 68.76" in w04)
add("w04-production-70", "PRODUCTION_MIN_PROTRACTOR_WIDTH_MM=70" in w04)
add("w04-65-blocked", "65 mm protractor is invalid" in w04)
add("w04-active-direction", "one clearly active 0→180 reading direction" in w04)
add("w04-five-degree-required", "5° intermediate marks are REQUIRED" in w04)

add("w08-no-auto", "final prompt must not contain unresolved `RENDER_PATH=AUTO`" in w08)
add("w08-one-page-block", "PROMPT_ONE_PAGE_FEASIBILITY_QA=FAIL" in w08 and "70 mm" in w08)
add("w08-65-rejected", "65 mm protractor is invalid" in w08)

add("w09-spacing-gate", "PROMPT_PROTRACTOR_PRINT_SPACING_QA" in w09 and "PROMPT_SCALE_PRINT_SPACING_ORACLE_QA" in w09)
add("w09-render-path-gate", "PROMPT_PROTRACTOR_RENDER_PATH_QA" in w09 and "RENDER_PATH=AUTO" in w09)
add("w09-release-blocked", "65 mm protractor therefore fails" in w09 and "PROMPT_RELEASE=BLOCKED" in w09)

assert len(CASES) == 24, len(CASES)
failed = [c for c in CASES if not c[1]]
if failed:
    print(f"PROTRACTOR SCALE SAFETY REGRESSION: FAIL ({len(failed)}/{len(CASES)})")
    for name, _ in failed:
        print("FAIL", name)
    sys.exit(1)

print("PROTRACTOR SCALE SAFETY REGRESSION: PASS")
print(f"cases: {len(CASES)}")
print(f"pass: {len(CASES)}")
print("fail: 0")
print("protractor scale placement safety: 24/24 PASS")
print("artifact QA: NOT_YET_TESTED")
