#!/usr/bin/env python3
"""Static SSOT validator for activity-based-elementary-worksheet 2.6.x.

Structural/document-contract validation only. Executable validation is performed
by the additive 971-case release gate. None of these prompt-system checks claims
that downstream worksheet pixels have passed artifact QA.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

WORKERS = {
    "W01_ACADEMIC_CONTENT": "workers/W01_ACADEMIC_CONTENT.md",
    "W02_TIME_CLOCK": "workers/W02_TIME_CLOCK.md",
    "W03_WEIGHT_SCALE": "workers/W03_WEIGHT_SCALE.md",
    "W04_LENGTH_DISTANCE": "workers/W04_LENGTH_DISTANCE.md",
    "W05_TEMPERATURE_CAPACITY_VOLUME": "workers/W05_TEMPERATURE_CAPACITY_VOLUME.md",
    "W06_MONEY_CALENDAR_DATA": "workers/W06_MONEY_CALENDAR_DATA.md",
    "W07_INSTRUMENT_AUDITOR": "workers/W07_INSTRUMENT_AUDITOR.md",
    "W08_LAYOUT_RENDER_THAI": "workers/W08_LAYOUT_RENDER_THAI.md",
    "W09_QA_RELEASE": "workers/W09_QA_RELEASE.md",
}

REQUIRED_FILES = [
    "GEM_INSTRUCTIONS_PRODUCTION.md", "OUTPUT_CONTRACT.md", "ARCHITECTURE.md",
    "KB_ROUTER.md", "KB_MANIFEST.md", "policies/PARAMETER_POLICY.md",
    "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md", "policies/SYSTEM_WIDE_QUALITY_PROFILE.md",
    "policies/SCALE_LINE_INTEGRITY_PROFILE.md", "policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md",
    "domains/DOMAIN_REGISTRY.md", "domains/MEASUREMENT_COVERAGE_P1_P6.md",
    "domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md", "domains/INSTRUMENT_READING_ENGINE.md",
    "domains/SPEEDOMETER_READING_ENGINE.md", "domains/TEMPERATURE_READING_ENGINE.md",
    "domains/CAPACITY_READING_ENGINE.md", "domains/TABLE_GRAPH_READING_ENGINE.md",
    "qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md", "qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md",
    "qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md", "qa/RUNTIME_UAT_CLOCK_REGRESSION_V2_6_X.md",
    "qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md", "qa/BASELINE_2_6_2_RELEASE_CHECKLIST.md",
    "qa/DOMAIN_RELEASE_MATRIX.md", "examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md",
    "tools/full_dry_run_suite.py", "tools/full_skill_matrix_suite.py",
    "tools/runtime_uat_regression_suite.py", "tools/semantic_oracle_regression_suite.py",
    "tools/system_wide_quality_regression_suite.py", "tools/scale_line_integrity_regression_suite.py",
    "tools/instrument_review_speedometer_regression_suite.py", "tools/build_install_package.py",
    *WORKERS.values(),
]

EXPECTED_DOMAINS = {
    "TIME", "TIME_CLOCK", "MEASUREMENT_WEIGHT", "MEASUREMENT_LENGTH",
    "MEASUREMENT_DISTANCE", "MEASUREMENT_SPEEDOMETER", "MEASUREMENT_ANGLE",
    "MEASUREMENT_PERIMETER_AREA", "MEASUREMENT_TEMPERATURE",
    "MEASUREMENT_CAPACITY", "MEASUREMENT_VOLUME",
}

CHECKS = {
    "GEM_INSTRUCTIONS_PRODUCTION.md": [
        "Version: 2.6.2-LTS", "FINAL_IMAGE_GENERATION_PROMPT",
        "INSTRUMENT_REVIEW_REVISE_PROFILE.md", "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON",
        "INTERIOR_POSITIONS_PER_CM_SPAN=9", "speedometer", "ARTIFACT_QA=NOT_YET_TESTED",
    ],
    "OUTPUT_CONTRACT.md": [
        "Version: 2.6.2-LTS", "SCALE_LINE_SPEC_REQUIRED=YES",
        "INSTRUMENT_REVIEW_REVISE_PROTOCOL", "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON",
        "10 intervals", "9 interior positions", "target_angle=(240+2*target_kmh) mod 360",
    ],
    "KB_ROUTER.md": [
        "direct speedometer reading / vehicle speed dial", "W04 + W07 + W08 + W09",
        "INSTRUMENT_REVIEW_REVISE_PROFILE.md", "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON",
    ],
    "KB_MANIFEST.md": [
        "Manifest version: 2.6.2-LTS", "INSTRUMENT_REVIEW_REVISE_PROFILE.md",
        "SPEEDOMETER_READING_ENGINE.md", "exactly nine worker", "INTERIOR_POSITIONS_PER_CM_SPAN=9",
    ],
    "policies/PARAMETER_POLICY.md": [
        "CLOCK_READING_MODE=AUTO|SINGLE|DAY_NIGHT_PAIR",
        "TARGET_MINUTE_MODE=ANY_VALID|MULTIPLE_OF_GRANULARITY|EXACT_MINUTE_SET",
        "TARGET_MINUTE_SET={30}", "ONE_PAGE_LOCK=OFF", "PROTRACTOR_RANGE=0_180|0_360", "DM3", "PI_POLICY",
    ],
    "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md": [
        "CLOCK_READING_MODE=DAY_NIGHT_PAIR", "ONE_CLOCK_TWO_ANSWERS=YES",
        "ANSWER_FIELDS_PER_QUESTION=2", "TARGET_MINUTE_SET={30}", "ONE_PAGE_LOCK=OFF",
        "minute_angle=180°", "do not reduce to only 5-minute ticks",
    ],
    "policies/SYSTEM_WIDE_QUALITY_PROFILE.md": [
        "SYSTEM_INDEPENDENT_ORACLE_QA", "SYSTEM_DIFFICULTY_FIDELITY_QA",
        "PROMPT_RENDER_STATE_SERIALIZATION_QA", "PROMPT_QA_EVIDENCE_CONSISTENCY_QA",
        "SCALE_LINE_INTEGRITY_PROFILE.md",
    ],
    "policies/SCALE_LINE_INTEGRITY_PROFILE.md": [
        "SCALE_LINE_SPEC", "MIN_TICK_CENTER_SPACING_MM", "0.60 mm", "0.25 mm", "0.35 mm",
        "PROMPT_SCALE_TICK_ANCHOR_QA", "PROMPT_SCALE_LINE_SERIALIZATION_QA",
    ],
    "policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md": [
        "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON",
        "PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA", "PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA",
        "PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA", "exactly 9 interior graduation positions",
    ],
    "domains/INSTRUMENT_READING_ENGINE.md": [
        "Version: 1.5.0", "INSTRUMENT_REVIEW_REVISE_PROFILE.md",
        "EXPECTED_INTERIOR_POSITION_COUNT", "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON",
        "canonical 0–120 km/h speedometer",
    ],
    "domains/SPEEDOMETER_READING_ENGINE.md": [
        "OPEN_ARC_BOUNDED", "SPEEDOMETER_ACTIVE_SWEEP_DEG=240", "12 equal minor intervals",
        "13 endpoint-inclusive active positions", "120° inactive/non-scale gap",
        "target_angle=(240 + 2*target_kmh) mod 360", "speed=distance/time",
    ],
    "workers/W04_LENGTH_DISTANCE.md": [
        "direct speedometer reading", "INTERVALS_PER_CM=10", "POSITIONS_PER_CM_SPAN=11",
        "INTERIOR_POSITIONS_PER_CM_SPAN=9", "PHYSICAL_EDGE_IS_GRADUATION=NO",
        "PROMPT_SPEEDOMETER_ANGLE_MAPPING_QA",
    ],
    "workers/W05_TEMPERATURE_CAPACITY_VOLUME.md": [
        "0–50°C @1°C", "50 intervals / 51 positions", "PROMPT_THERMOMETER_INTERVAL_COUNT_QA",
        "renderer self-review",
    ],
    "workers/W07_INSTRUMENT_AUDITOR.md": [
        "PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA", "10 intervals / 11 positions / 9 interior positions",
    ],
    "workers/W08_LAYOUT_RENDER_THAI.md": [
        "INSTRUMENT_REVIEW_REVISE_PROTOCOL", "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON",
        "10 intervals / 11 positions / 9 interior positions",
    ],
    "workers/W09_QA_RELEASE.md": [
        "PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA", "ARTIFACT_QA=FAIL",
        "PROMPT_RULER_SUBDIVISION_COUNT_QA", "PROMPT_SPEEDOMETER_TOPOLOGY_QA",
        "PROMPT_THERMOMETER_INTERVAL_COUNT_QA",
    ],
    "qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md": [
        "CRITICAL_ACADEMIC", "exactly 10 equal intervals", "exactly 11 physical graduation positions",
        "exactly 9 interior positions", "PHYSICAL_EDGE_IS_GRADUATION=NO",
    ],
    "tools/build_install_package.py": [
        "activity-based-elementary-worksheet_Gem_v2.6.2_LTS_9WORKERS_TXT",
        "INSTRUMENT_REVIEW_REVISE_PROFILE.md", "SPEEDOMETER_READING_ENGINE.md",
        "instrument_review_speedometer_regression_suite.py", "971/971 PASS",
    ],
    "tools/full_dry_run_suite.py": ["expected 449", "assert len(CASES) == 449"],
    "tools/full_skill_matrix_suite.py": ["Expected case count: exactly 360", "assert len(CASES)==360,len(CASES)"],
    "tools/runtime_uat_regression_suite.py": ["12/12 PASS", "profile-embedded-main"],
    "tools/semantic_oracle_regression_suite.py": ["Expected case count: exactly 20", "assert len(CASES) == 20"],
    "tools/system_wide_quality_regression_suite.py": ["Expected case count: exactly 30", "assert len(CASES) == 30"],
    "tools/scale_line_integrity_regression_suite.py": ["Expected case count: exactly 40", "assert len(CASES) == 40"],
    "tools/instrument_review_speedometer_regression_suite.py": [
        "Expected case count: exactly 60", "assert len(CASES) == 60", "speedometer-60-angle",
        "thermo-35F-invalid", "ruler-1cm-interior",
    ],
    "qa/BASELINE_2_6_2_RELEASE_CHECKLIST.md": [
        "971/971 PASS", "instrument_review_speedometer_regression_suite.py",
        "NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON",
        "ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md",
    ],
}

EXACT_RELATIONS = [
    ("domains/MEASUREMENT_COVERAGE_P1_P6.md", "10 mm = 1 cm"),
    ("domains/MEASUREMENT_COVERAGE_P1_P6.md", "100 cm = 1 m"),
    ("domains/MEASUREMENT_COVERAGE_P1_P6.md", "1000 m = 1 km"),
    ("domains/MEASUREMENT_COVERAGE_P1_P6.md", "1000 mL = 1 L"),
    ("domains/MEASUREMENT_COVERAGE_P1_P6.md", "1000 cm³ = 1 dm³"),
    ("domains/MEASUREMENT_COVERAGE_P1_P6.md", "1000 dm³ = 1 m³"),
    ("domains/MEASUREMENT_COVERAGE_P1_P6.md", "1 m³ = 1,000,000 cm³"),
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")
    if errors:
        for e in errors: print("FAIL", e)
        return 1

    seen: set[str] = set()
    for wid, rel in WORKERS.items():
        txt = read(rel)
        for required in (f"WORKER_ID={wid}", "BASELINE_COMPATIBILITY=2.6.x", "WORKER_SCHEMA_VERSION=1"):
            if required not in txt:
                errors.append(f"{rel}: missing {required}")
        found = re.findall(r"WORKER_ID=([A-Z0-9_]+)", txt)
        if found:
            if found[0] in seen:
                errors.append(f"duplicate worker id: {found[0]}")
            seen.add(found[0])
    if len(seen) != 9:
        errors.append(f"expected 9 unique worker IDs, got {len(seen)}")

    registry = read("domains/DOMAIN_REGISTRY.md")
    matrix = read("qa/DOMAIN_RELEASE_MATRIX.md")
    for domain in sorted(EXPECTED_DOMAINS):
        if f"| {domain} |" not in registry:
            errors.append(f"registry missing {domain}")
        if f"| {domain} |" not in matrix:
            errors.append(f"release matrix missing {domain}")

    for rel, tokens in CHECKS.items():
        txt = read(rel)
        for expected in tokens:
            if expected not in txt:
                errors.append(f"{rel}: missing token: {expected}")

    for rel, relation in EXACT_RELATIONS:
        if relation not in read(rel):
            errors.append(f"{rel}: missing exact relation: {relation}")

    policy = read("policies/PARAMETER_POLICY.md")
    if "CLOCK_READING_MODE=SINGLE|DAY_NIGHT_PAIR" in policy and "CLOCK_READING_MODE=AUTO|SINGLE|DAY_NIGHT_PAIR" not in policy:
        errors.append("clock mode policy lacks AUTO resolution")
    if "MINUTE_GRANULARITY=30" in read("workers/W02_TIME_CLOCK.md") and "TARGET_MINUTE_SET={30}" not in read("workers/W02_TIME_CLOCK.md"):
        errors.append("half-hour intent not separated from granularity")
    if "PROTRACTOR_RANGE=0_180|0_360" in policy and "CYCLIC_FULL_CIRCLE" not in read("workers/W04_LENGTH_DISTANCE.md"):
        errors.append("0_360 protractor exposed without deterministic full-circle topology")

    # The package builder must ship every mandatory shared profile to every worker.
    builder = read("tools/build_install_package.py")
    for profile in (
        "policies/SYSTEM_WIDE_QUALITY_PROFILE.md",
        "policies/SCALE_LINE_INTEGRITY_PROFILE.md",
        "policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md",
    ):
        if profile not in builder:
            errors.append(f"builder missing mandatory shared profile: {profile}")

    stale = re.compile(r"(?:baseline|Version:|Compatible Gem baseline:)[^\n]*(?:2\.3\.|2\.4\.|2\.5\.)", re.I)
    runtime_files = [
        "GEM_INSTRUCTIONS_PRODUCTION.md", "OUTPUT_CONTRACT.md", "ARCHITECTURE.md",
        "KB_ROUTER.md", "KB_MANIFEST.md", "policies/PARAMETER_POLICY.md",
        "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md", "policies/SYSTEM_WIDE_QUALITY_PROFILE.md",
        "policies/SCALE_LINE_INTEGRITY_PROFILE.md", "policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md",
        "domains/DOMAIN_REGISTRY.md", "domains/INSTRUMENT_READING_ENGINE.md",
        "domains/SPEEDOMETER_READING_ENGINE.md", *WORKERS.values(),
    ]
    for rel in runtime_files:
        if stale.search(read(rel)):
            errors.append(f"{rel}: stale runtime baseline reference")

    if errors:
        print(f"SSOT VALIDATION: FAIL ({len(errors)} issue(s))")
        for e in errors:
            print("FAIL", e)
        return 1

    print("SSOT VALIDATION: PASS")
    print("release family: 2.6.2-LTS / compatible baseline 2.6.x")
    print("workers: 9/9 unique, schema=1")
    print("mandatory runtime profiles: system-wide + scale-line + instrument review-revise")
    print("speedometer deterministic engine: present")
    print("actual ruler extra-tick regression: present")
    print("core dry-run: 449-case executable present")
    print("declared-skill matrix: 360-case executable present")
    print("runtime UAT regression: 12-case executable present")
    print("semantic oracle regression: 20-case executable present")
    print("system-wide quality regression: 30-case executable present")
    print("scale-line integrity regression: 40-case executable present")
    print("instrument review/speedometer regression: 60-case executable present")
    print("combined minimum release gate: 971 cases")
    print("artifact QA: NOT_YET_TESTED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
