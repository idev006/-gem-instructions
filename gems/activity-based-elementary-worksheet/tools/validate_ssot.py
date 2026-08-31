#!/usr/bin/env python3
"""Static SSOT validator for activity-based-elementary-worksheet 2.6.x.

Structural/document-contract validation only. Executable prompt-system validation
is performed by the 449-case core suite, 360-case declared-skill matrix,
12-case runtime UAT regression suite, and 20-case semantic-oracle suite.
None of these claims artifact pixels pass.
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
    "GEM_INSTRUCTIONS_PRODUCTION.md",
    "OUTPUT_CONTRACT.md",
    "ARCHITECTURE.md",
    "KB_ROUTER.md",
    "KB_MANIFEST.md",
    "policies/PARAMETER_POLICY.md",
    "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md",
    "domains/DOMAIN_REGISTRY.md",
    "domains/MEASUREMENT_COVERAGE_P1_P6.md",
    "domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md",
    "qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md",
    "qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md",
    "qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md",
    "qa/RUNTIME_UAT_CLOCK_REGRESSION_V2_6_X.md",
    "qa/BASELINE_2_6_0_RELEASE_CHECKLIST.md",
    "qa/DOMAIN_RELEASE_MATRIX.md",
    "examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md",
    "tools/full_dry_run_suite.py",
    "tools/full_skill_matrix_suite.py",
    "tools/runtime_uat_regression_suite.py",
    "tools/semantic_oracle_regression_suite.py",
    "tools/build_install_package.py",
    *WORKERS.values(),
]

EXPECTED_DOMAINS = {
    "TIME", "TIME_CLOCK", "MEASUREMENT_WEIGHT", "MEASUREMENT_LENGTH",
    "MEASUREMENT_DISTANCE", "MEASUREMENT_ANGLE", "MEASUREMENT_PERIMETER_AREA",
    "MEASUREMENT_TEMPERATURE", "MEASUREMENT_CAPACITY", "MEASUREMENT_VOLUME",
}

CHECKS = {
    "GEM_INSTRUCTIONS_PRODUCTION.md": [
        "Orchestrator", "W02_TIME_CLOCK", "FINAL_IMAGE_GENERATION_PROMPT",
        "ARTIFACT_QA=NOT_YET_TESTED", "RENDER_ONLY_NOT_FOR_WORKSHEET",
        "ONE_PAGE_LOCK=OFF",
    ],
    "policies/PARAMETER_POLICY.md": [
        "CLOCK_READING_MODE=AUTO|SINGLE|DAY_NIGHT_PAIR",
        "TARGET_MINUTE_MODE=ANY_VALID|MULTIPLE_OF_GRANULARITY|EXACT_MINUTE_SET",
        "TARGET_MINUTE_SET={30}", "ONE_PAGE_LOCK=OFF",
        "PROTRACTOR_RANGE=0_180|0_360", "DM3", "PI_POLICY",
    ],
    "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md": [
        "CLOCK_READING_MODE=DAY_NIGHT_PAIR", "ONE_CLOCK_TWO_ANSWERS=YES",
        "ANSWER_FIELDS_PER_QUESTION=2", "TARGET_MINUTE_SET={30}",
        "ONE_PAGE_LOCK=OFF", "minute_angle=180°",
        "do not reduce to only 5-minute ticks",
    ],
    "tools/build_install_package.py": [
        "MANDATORY RUNTIME PROFILE: THAI P3 ANALOG CLOCK",
        "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md",
        "qa/RUNTIME_UAT_CLOCK_REGRESSION_V2_6_X.md",
        "semantic_oracle_regression_suite.py",
        "841/841 PASS",
    ],
    "workers/W02_TIME_CLOCK.md": [
        "Thai Grade 3 analog-clock reading", "TARGET_MINUTE_SET={30}",
        "กลางวัน = h12+12", "กลางคืน = h12+12",
        "PROMPT_PER_ITEM_RENDER_STATE_QA", "PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA",
    ],
    "domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md": [
        "01:30 → กลางวัน 13:30 | กลางคืน 01:30",
        "06:30 → กลางวัน 06:30 | กลางคืน 18:30",
        "12:15 → กลางวัน 12:15 | กลางคืน 00:15",
        "TARGET_MINUTE_SET={30}", "ONE_PAGE_LOCK=OFF",
    ],
    "workers/W04_LENGTH_DISTANCE.md": [
        "CYCLIC_FULL_CIRCLE", "360 equal intervals / 360 distinct positions",
        "no duplicated 0°/360° physical mark",
    ],
    "workers/W09_QA_RELEASE.md": [
        "Critical QA is conjunctive", "PROMPT_RELEASE=BLOCKED",
        "PROMPT_PAGE_LOCK_PROVENANCE_QA", "PROMPT_HALF_HOUR_INTENT_QA",
        "PROMPT_DAY_NIGHT_MAPPING_QA", "PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA",
    ],
    "qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md": [
        "DN-01 — Thai P3 AUTO mode", "DN-10 — strict half-hour intent",
        "DN-13 — numeric angles mandatory", "DN-17 — page-lock provenance",
        "DN-19 — false-PASS prevention",
    ],
    "qa/RUNTIME_UAT_CLOCK_REGRESSION_V2_6_X.md": [
        "UAT-01", "UAT-03", "UAT-05", "UAT-06", "UAT-10", "821/821 PASS",
    ],
    "tools/full_dry_run_suite.py": ["expected 449", "assert len(CASES) == 449"],
    "tools/full_skill_matrix_suite.py": ["Expected case count: exactly 360", "assert len(CASES)==360,len(CASES)"],
    "tools/runtime_uat_regression_suite.py": ["12/12 PASS", "profile-embedded-main"],
    "tools/semantic_oracle_regression_suite.py": ["Expected case count: exactly 20", "assert len(CASES) == 20"],
    "qa/BASELINE_2_6_0_RELEASE_CHECKLIST.md": ["841/841 PASS", "semantic_oracle_regression_suite.py"],
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
        for token in (f"WORKER_ID={wid}", "BASELINE_COMPATIBILITY=2.6.x", "WORKER_SCHEMA_VERSION=1"):
            if token not in txt: errors.append(f"{rel}: missing {token}")
        found = re.findall(r"WORKER_ID=([A-Z0-9_]+)", txt)
        if found:
            if found[0] in seen: errors.append(f"duplicate worker id: {found[0]}")
            seen.add(found[0])
    if len(seen) != 9: errors.append(f"expected 9 unique worker IDs, got {len(seen)}")

    registry, matrix = read("domains/DOMAIN_REGISTRY.md"), read("qa/DOMAIN_RELEASE_MATRIX.md")
    for domain in sorted(EXPECTED_DOMAINS):
        if f"| {domain} |" not in registry: errors.append(f"registry missing {domain}")
        if f"| {domain} |" not in matrix: errors.append(f"release matrix missing {domain}")

    for rel, tokens in CHECKS.items():
        txt = read(rel)
        for token in tokens:
            if token not in txt: errors.append(f"{rel}: missing token: {token}")

    for rel, relation in EXACT_RELATIONS:
        if relation not in read(rel): errors.append(f"{rel}: missing exact relation: {relation}")

    policy = read("policies/PARAMETER_POLICY.md")
    if "CLOCK_READING_MODE=SINGLE|DAY_NIGHT_PAIR" in policy and "CLOCK_READING_MODE=AUTO|SINGLE|DAY_NIGHT_PAIR" not in policy:
        errors.append("clock mode policy lacks AUTO resolution")
    if "MINUTE_GRANULARITY=30" in read("workers/W02_TIME_CLOCK.md") and "TARGET_MINUTE_SET={30}" not in read("workers/W02_TIME_CLOCK.md"):
        errors.append("half-hour intent not separated from granularity")
    if "PROTRACTOR_RANGE=0_180|0_360" in policy and "CYCLIC_FULL_CIRCLE" not in read("workers/W04_LENGTH_DISTANCE.md"):
        errors.append("0_360 protractor exposed without deterministic full-circle topology")

    stale = re.compile(r"(?:baseline|Version:|Compatible Gem baseline:)[^\n]*(?:2\.3\.|2\.4\.|2\.5\.)", re.I)
    for rel in ["GEM_INSTRUCTIONS_PRODUCTION.md", "OUTPUT_CONTRACT.md", "ARCHITECTURE.md", "KB_ROUTER.md", "KB_MANIFEST.md", "policies/PARAMETER_POLICY.md", "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md", "domains/DOMAIN_REGISTRY.md", *WORKERS.values()]:
        if stale.search(read(rel)): errors.append(f"{rel}: stale runtime baseline reference")

    if errors:
        print(f"SSOT VALIDATION: FAIL ({len(errors)} issue(s))")
        for e in errors: print("FAIL", e)
        return 1

    print("SSOT VALIDATION: PASS")
    print("baseline: 2.6.x")
    print("workers: 9/9 unique, schema=1")
    print("Thai P3 clock runtime profile + UAT regression: present")
    print("generated runtime profile embedding: present")
    print("core dry-run: 449-case executable present")
    print("declared-skill matrix: 360-case executable present")
    print("runtime UAT regression: 12-case executable present")
    print("semantic oracle regression: 20-case executable present")
    print("combined minimum release gate: 841 cases")
    print("artifact QA: NOT_YET_TESTED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
