#!/usr/bin/env python3
"""Scale/tick standard governance regression.

Validates that cross-skill scale, tick count, tick hierarchy, label association,
and target alignment standards are present and bound to high-risk skills.

This is prompt/knowledge governance evidence. It does not certify rendered pixels.
Expected case count: exactly 120.
"""
from pathlib import Path
import math, sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
CASES = []

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def add(name, ok, detail=""):
    CASES.append((name, bool(ok), detail))

central = {
    "SCALE_TICK_STANDARD": "policies/SCALE_TICK_STANDARD.md",
    "INSTRUMENT_TICK_HIERARCHY_POLICY": "policies/INSTRUMENT_TICK_HIERARCHY_POLICY.md",
    "CRITICAL_DEFECT_POLICY": "skill-metrics/CRITICAL_DEFECT_POLICY.md",
    "INSTRUMENT_SCALE_DEFECT_TAXONOMY": "qa/INSTRUMENT_SCALE_DEFECT_TAXONOMY.md",
}
central_tokens = {
    "SCALE_TICK_STANDARD": [
        "SCALE_TICK_STANDARD_QA=MANDATORY",
        "EXPECTED_INTERVAL_COUNT",
        "EXPECTED_POSITION_COUNT",
        "EXPECTED_INTERIOR_TICK_COUNT",
        "PROMPT_TICK_LENGTH_HIERARCHY_QA",
        "CRITICAL_SCALE_DEFECT => ARTIFACT_QA=FAIL",
        "0.5 kg midpoint tick",
    ],
    "INSTRUMENT_TICK_HIERARCHY_POLICY": [
        "INSTRUMENT_TICK_HIERARCHY_QA=MANDATORY",
        "MAJOR_TICK_LENGTH_RATIO=1.00",
        "INTERMEDIATE_TICK_LENGTH_RATIO=0.75",
        "MINOR_TICK_LENGTH_RATIO=0.50",
        "0.1 kg",
        "5 mm",
        "ARTIFACT_TICK_HIERARCHY_VISIBLE_QA",
    ],
    "CRITICAL_DEFECT_POLICY": [
        "CRITICAL_ACADEMIC_DEFECT => ARTIFACT_QA=FAIL => CLASSROOM_RELEASE=BLOCKED",
        "missing/extra scale graduation",
        "pointer/hand/ray/liquid endpoint",
        "15:30",
        "1 kg span",
        "1 cm",
        "bar height inconsistent",
    ],
    "INSTRUMENT_SCALE_DEFECT_TAXONOMY": [
        "D1 Missing tick",
        "D2 Extra tick",
        "D3 Wrong interval count",
        "D5 Tick hierarchy failure",
        "D7 Reference origin/center error",
        "D8 Target alignment error",
        "REGRESSION_REQUIRED",
    ],
}

# 4 central documents × (file exists + 7 required tokens) = 32
for name, rel in central.items():
    path = ROOT / rel
    add(f"central-{name}-exists", path.is_file(), rel)
    txt = path.read_text(encoding="utf-8") if path.is_file() else ""
    for token in central_tokens[name]:
        add(f"central-{name}-{token[:28]}", token in txt, token)

skill_packs = {
    "ANALOG_CLOCK": ("skill-metrics/ANALOG_CLOCK_SKILL_METRICS.md", "hour hand"),
    "WEIGHT_SCALE": ("skill-metrics/WEIGHT_SCALE_SKILL_METRICS.md", "0.5 tick"),
    "RULER_LENGTH": ("skill-metrics/RULER_LENGTH_SKILL_METRICS.md", "5 mm"),
    "SPEEDOMETER": ("skill-metrics/SPEEDOMETER_SKILL_METRICS.md", "pointer"),
    "ANGLE_PROTRACTOR": ("skill-metrics/ANGLE_PROTRACTOR_SKILL_METRICS.md", "ray"),
    "TEMPERATURE": ("skill-metrics/TEMPERATURE_SKILL_METRICS.md", "liquid"),
    "CAPACITY": ("skill-metrics/CAPACITY_SKILL_METRICS.md", "meniscus"),
    "DATA_READING": ("skill-metrics/DATA_READING_SKILL_METRICS.md", "axis"),
}
# 8 high-risk skill packs × 6 checks = 48
for skill, (rel, token) in skill_packs.items():
    path = ROOT / rel
    add(f"skill-{skill}-exists", path.is_file(), rel)
    txt = path.read_text(encoding="utf-8") if path.is_file() else ""
    add(f"skill-{skill}-id", f"SKILL_ID={skill}" in txt)
    add(f"skill-{skill}-oracle", "## CANONICAL_ORACLE" in txt)
    add(f"skill-{skill}-artifact", "## ARTIFACT_METRICS" in txt)
    add(f"skill-{skill}-critical", "## CRITICAL_DEFECTS" in txt and "CRITICAL_OVERRIDE=YES" in txt)
    add(f"skill-{skill}-scale-token", token.lower() in txt.lower(), token)

# 5 integration surfaces × 4 checks = 20
integration = {
    "GEM": "GEM_INSTRUCTIONS_PRODUCTION.md",
    "W07": "workers/W07_INSTRUMENT_AUDITOR.md",
    "W09": "workers/W09_QA_RELEASE.md",
    "W10": "workers/W10_METROLOGY_ENGINEER.md",
    "BUILD": "tools/build_install_package.py",
}
for name, rel in integration.items():
    txt = read(rel)
    add(f"integration-{name}-standard-ref", "SCALE_TICK_STANDARD" in txt or "Scale Tick Standard" in txt)
    add(f"integration-{name}-hierarchy-ref", "TICK_HIERARCHY" in txt or "tick hierarchy" in txt.lower())
    add(f"integration-{name}-critical-ref", "CRITICAL_SCALE_DEFECT" in txt or "CRITICAL_ACADEMIC_DEFECT" in txt)
    add(f"integration-{name}-artifact-boundary", "ARTIFACT_QA" in txt or "artifact" in txt.lower())

# 20 canonical math/consistency oracles
add("oracle-clock-minute-angle-30", math.isclose(6 * 30, 180))
add("oracle-clock-hour-3-30", math.isclose(30 * 3 + 0.5 * 30, 105))
add("oracle-clock-hour-2-45", math.isclose(30 * 2 + 0.5 * 45, 82.5))
add("oracle-clock-quarter", math.isclose(0.5 * 15, 7.5))
add("oracle-clock-three-quarter", math.isclose(0.5 * 45, 22.5))
add("oracle-weight-total-intervals", int(round((5 - 0) / 0.1)) == 50)
add("oracle-weight-total-positions", int(round((5 - 0) / 0.1)) + 1 == 51)
add("oracle-weight-per-kg-intervals", int(round(1 / 0.1)) == 10)
add("oracle-weight-per-kg-positions", int(round(1 / 0.1)) + 1 == 11)
add("oracle-weight-interior", int(round(1 / 0.1)) - 1 == 9)
add("oracle-ruler-per-cm-intervals", int(round(10 / 1)) == 10)
add("oracle-ruler-per-cm-positions", int(round(10 / 1)) + 1 == 11)
add("oracle-ruler-5mm-index", 5 == int(10 / 2))
add("oracle-protractor-intervals", int(180 / 1) == 180)
add("oracle-protractor-positions", int(180 / 1) + 1 == 181)
add("oracle-thermometer-intervals", int(50 / 1) == 50)
add("oracle-thermometer-positions", int(50 / 1) + 1 == 51)
add("oracle-capacity-intervals", int(1000 / 50) == 20)
add("oracle-capacity-per-100", int(100 / 50) == 2)
add("oracle-speedometer-positions", int(120 / 10) + 1 == 13)

assert len(CASES) == 120, len(CASES)
failed = [c for c in CASES if not c[1]]
if failed:
    print(f"SCALE TICK STANDARD REGRESSION: FAIL ({len(failed)}/{len(CASES)})")
    for name, _, detail in failed:
        print("FAIL", name, detail)
    sys.exit(1)

print("SCALE TICK STANDARD REGRESSION: PASS")
print("cases: 120")
print("pass: 120")
print("fail: 0")
print("scale/tick count + hierarchy + target alignment governance: 120/120 PASS")
print("artifact QA: NOT_YET_TESTED until rendered worksheet inspection")
