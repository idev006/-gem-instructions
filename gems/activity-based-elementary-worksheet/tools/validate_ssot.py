#!/usr/bin/env python3
"""Static SSOT validator for activity-based-elementary-worksheet 2.6.x.

Run from repository root:
    python gems/activity-based-elementary-worksheet/tools/validate_ssot.py

This validates structural/document-contract consistency only. It does not claim
that downstream rendered worksheet artifacts have passed visual QA.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "2.6"

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
    "domains/DOMAIN_REGISTRY.md",
    "domains/MEASUREMENT_COVERAGE_P1_P6.md",
    "qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md",
    "qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md",
    "qa/BASELINE_2_6_0_RELEASE_CHECKLIST.md",
    "qa/DOMAIN_RELEASE_MATRIX.md",
    "examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md",
    *WORKERS.values(),
]

EXPECTED_DOMAINS = {
    "TIME",
    "TIME_CLOCK",
    "MEASUREMENT_WEIGHT",
    "MEASUREMENT_LENGTH",
    "MEASUREMENT_DISTANCE",
    "MEASUREMENT_ANGLE",
    "MEASUREMENT_PERIMETER_AREA",
    "MEASUREMENT_TEMPERATURE",
    "MEASUREMENT_CAPACITY",
    "MEASUREMENT_VOLUME",
}

CHECK_TOKENS = {
    "GEM_INSTRUCTIONS_PRODUCTION.md": [
        "Orchestrator",
        "W04_LENGTH_DISTANCE",
        "angle/protractor",
        "perimeter",
        "cm³/dm³/m³",
        "ARTIFACT_QA=NOT_YET_TESTED",
        "RENDER_ONLY_NOT_FOR_WORKSHEET",
    ],
    "KB_ROUTER.md": [
        "angle/protractor",
        "perimeter/area",
        "time-unit conversion",
        "cubic-unit conversion",
    ],
    "policies/PARAMETER_POLICY.md": [
        "TIME_PRECISION=HOUR|MINUTE|SECOND",
        "ANGLE_TASK_TYPE",
        "AREA_TASK_TYPE",
        "DM3",
        "PI_POLICY",
    ],
    "domains/MEASUREMENT_COVERAGE_P1_P6.md": [
        "ANGLE / PROTRACTOR",
        "PERIMETER",
        "AREA",
        "SOLID VOLUME",
        "60 seconds = 1 minute",
    ],
    "qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md": [
        "M-39",
        "M-41",
        "M-46",
        "M-49",
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


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(errors, f"missing required file: {rel}")

    if errors:
        for e in errors:
            print("FAIL", e)
        return 1

    # Worker identity/schema/baseline.
    seen_ids: set[str] = set()
    for worker_id, rel in WORKERS.items():
        text = read(rel)
        if f"WORKER_ID={worker_id}" not in text:
            fail(errors, f"{rel}: wrong/missing WORKER_ID={worker_id}")
        if "BASELINE_COMPATIBILITY=2.6.x" not in text:
            fail(errors, f"{rel}: missing baseline compatibility 2.6.x")
        if "WORKER_SCHEMA_VERSION=1" not in text:
            fail(errors, f"{rel}: missing worker schema 1")
        found = re.findall(r"WORKER_ID=([A-Z0-9_]+)", text)
        if found:
            if found[0] in seen_ids:
                fail(errors, f"duplicate worker id: {found[0]}")
            seen_ids.add(found[0])

    if len(seen_ids) != 9:
        fail(errors, f"expected 9 unique base worker IDs, got {len(seen_ids)}")

    # Domain registry and release matrix must contain the same formal measurement domains.
    registry = read("domains/DOMAIN_REGISTRY.md")
    matrix = read("qa/DOMAIN_RELEASE_MATRIX.md")
    for domain in sorted(EXPECTED_DOMAINS):
        if f"| {domain} |" not in registry:
            fail(errors, f"DOMAIN_REGISTRY missing {domain}")
        if f"| {domain} |" not in matrix:
            fail(errors, f"DOMAIN_RELEASE_MATRIX missing {domain}")

    # Core known tokens.
    for rel, tokens in CHECK_TOKENS.items():
        text = read(rel)
        for token in tokens:
            if token not in text:
                fail(errors, f"{rel}: missing required token: {token}")

    # Exact measurement relations.
    for rel, relation in EXACT_RELATIONS:
        if relation not in read(rel):
            fail(errors, f"{rel}: missing exact relation: {relation}")

    # Single render-path contract and prompt/artifact phase contract.
    core = read("GEM_INSTRUCTIONS_PRODUCTION.md")
    if "DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY" not in core:
        fail(errors, "core: resolved render-path enum missing")
    if "ARTIFACT_QA=NOT_YET_TESTED" not in core:
        fail(errors, "core: prompt/artifact phase boundary missing")

    # Runtime canonical files must not declare stale 2.3/2.4/2.5 baselines.
    runtime_files = [
        "GEM_INSTRUCTIONS_PRODUCTION.md",
        "OUTPUT_CONTRACT.md",
        "ARCHITECTURE.md",
        "KB_ROUTER.md",
        "KB_MANIFEST.md",
        "policies/PARAMETER_POLICY.md",
        "domains/DOMAIN_REGISTRY.md",
        *WORKERS.values(),
    ]
    stale_pattern = re.compile(r"(?:baseline|Version:|Compatible Gem baseline:)[^\n]*(?:2\.3\.|2\.4\.|2\.5\.)", re.I)
    for rel in runtime_files:
        if stale_pattern.search(read(rel)):
            fail(errors, f"{rel}: stale runtime baseline reference detected")

    # Student visibility / renderer metadata terminology.
    output = read("OUTPUT_CONTRACT.md")
    for token in ["RENDER_ONLY_NOT_FOR_WORKSHEET", "STUDENT_VISIBLE_WORKSHEET", "ARTIFACT_QA=NOT_YET_TESTED"]:
        if token not in output:
            fail(errors, f"OUTPUT_CONTRACT missing {token}")

    if errors:
        print(f"SSOT VALIDATION: FAIL ({len(errors)} issue(s))")
        for e in errors:
            print("FAIL", e)
        return 1

    print("SSOT VALIDATION: PASS")
    print("baseline: 2.6.x")
    print("workers: 9/9 unique, schema=1")
    print("measurement domains: registry/matrix aligned")
    print("visibility/render-path/phase contracts: present")
    print("measurement relations/regression tokens: present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
