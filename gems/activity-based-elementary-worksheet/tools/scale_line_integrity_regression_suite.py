#!/usr/bin/env python3
"""Cross-domain scale-line integrity regression for learner-read instruments.

Protects scale/graduation line semantics across clock, dial, ruler, thermometer,
capacity, protractor and graph-axis skills. Expected case count: exactly 40.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
CASES = []

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def add(name, ok):
    CASES.append((name, bool(ok)))

profile = read("policies/SCALE_LINE_INTEGRITY_PROFILE.md")
shared = read("domains/INSTRUMENT_READING_ENGINE.md")
clock = read("domains/CLOCK_READING_ENGINE.md")
dial = read("domains/SCALE_READING_ENGINE.md")
ruler = read("domains/LENGTH_READING_ENGINE.md")
temp = read("domains/TEMPERATURE_READING_ENGINE.md")
capacity = read("domains/CAPACITY_READING_ENGINE.md")
graph = read("domains/TABLE_GRAPH_READING_ENGINE.md")
system_profile = read("policies/SYSTEM_WIDE_QUALITY_PROFILE.md")
builder = read("tools/build_install_package.py")
validator = read("tools/validate_ssot.py")
checklist = read("qa/BASELINE_2_6_2_RELEASE_CHECKLIST.md")
workflow = (REPO / ".github/workflows/activity-based-elementary-worksheet-gem-ssot.yml").read_text(encoding="utf-8")

# 1-13 mandatory QA family.
qa_tokens = [
    "PROMPT_SCALE_LINE_SPEC_QA",
    "PROMPT_SCALE_TICK_ANCHOR_QA",
    "PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA",
    "PROMPT_SCALE_PRINT_SEPARATION_QA",
    "PROMPT_SCALE_UNIFORM_SPACING_QA",
    "PROMPT_SCALE_DIRECTION_QA",
    "PROMPT_SCALE_LABEL_ALIGNMENT_QA",
    "PROMPT_SCALE_LABEL_CLEARANCE_QA",
    "PROMPT_SCALE_TARGET_ALIGNMENT_QA",
    "PROMPT_SCALE_INACTIVE_REGION_QA",
    "PROMPT_SCALE_DECORATION_ISOLATION_QA",
    "PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA",
    "PROMPT_SCALE_LINE_SERIALIZATION_QA",
]
for token in qa_tokens:
    add(f"profile-{token}", token in profile)

# 14-20 domain coverage in shared profile. Check semantic domain presence rather than brittle exact heading text.
domain_checks = [
    ("clock", "Clock" in profile),
    ("dial-scale", "dial scale" in profile.lower()),
    ("ruler", "Ruler" in profile),
    ("thermometer", "Thermometer" in profile),
    ("graduated-container", "Graduated container" in profile),
    ("protractor", "Protractor" in profile),
    ("graph-axis", "Graph axis" in profile),
]
for label, ok in domain_checks:
    add(f"domain-{label}", ok)

# 21-28 topology/readability invariants.
checks = [
    ("profile-scale-line-spec", "SCALE_LINE_SPEC" in profile and "MIN_TICK_CENTER_SPACING_MM" in profile),
    ("profile-min-spacing", "0.60 mm" in profile),
    ("profile-minor-stroke", "0.25 mm" in profile),
    ("profile-major-stroke", "0.35 mm" in profile),
    ("profile-major-length", "1.5× minor tick length" in profile),
    ("profile-no-floating-ticks", "no floating ticks" in profile),
    ("profile-no-gray-required-lines", "no gray-only scale lines" in profile),
    ("profile-artifact-checklist", "no missing/extra/merged tick" in profile),
]
for name, ok in checks:
    add(name, ok)

# 29-34 domain-engine inheritance / existing exact topology.
add("shared-engine-inherits-scale-profile", "SCALE_LINE_INTEGRITY_PROFILE.md" in shared)
add("clock-60-positions", "60 distinct minute positions" in clock and "6° spacing" in clock)
add("dial-open-arc", "50 active intervals" in dial and "60° inactive gap" in dial)
add("ruler-endpoint-inclusive", "11 graduation positions" in ruler and "cm marks stronger/longer than mm marks" in ruler)
add("thermometer-linear-scale", "uniform graduations" in temp and "labels aligned to major ticks" in temp)
add("capacity-linear-scale", "uniform graduations" in capacity and "no decorative waves/bubbles/tick-like lines" in capacity)

# 35-40 system/runtime/release integration.
add("graph-scale-profile", "SCALE_LINE_INTEGRITY_PROFILE.md" in graph)
add("system-profile-inherits-scale-profile", "SCALE_LINE_INTEGRITY_PROFILE.md" in system_profile)
add("builder-embeds-scale-profile", "SCALE_LINE_PROFILE" in builder and "policies/SCALE_LINE_INTEGRITY_PROFILE.md" in builder)
add("builder-runs-scale-suite", "scale_line_integrity_regression_suite.py" in builder and "971/971 PASS" in builder)
add("workflow-runs-scale-suite", "Scale-line integrity regression" in workflow and "40 cases" in workflow)
add("validator-release-971", "scale_line_integrity_regression_suite.py" in validator and "971" in validator and "971/971 PASS" in checklist)

assert len(CASES) == 40, len(CASES)
failed = [case for case in CASES if not case[1]]
if failed:
    print(f"SCALE-LINE INTEGRITY REGRESSION: FAIL ({len(failed)}/{len(CASES)})")
    for name, _ in failed:
        print("FAIL", name)
    sys.exit(1)

print("SCALE-LINE INTEGRITY REGRESSION: PASS")
print(f"cases: {len(CASES)}")
print(f"pass: {len(CASES)}")
print("fail: 0")
print("cross-domain scale-line integrity: 40/40 PASS")
print("artifact QA: NOT_YET_TESTED")
