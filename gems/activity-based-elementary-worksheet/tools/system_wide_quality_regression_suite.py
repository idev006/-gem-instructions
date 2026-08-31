#!/usr/bin/env python3
"""System-wide cross-worker quality regression for baseline 2.6.x.

This suite protects architecture-level guarantees shared by W01-W09. It does not
replace domain suites. Expected case count: exactly 30.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CASES = []

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def add(name, ok, detail=""):
    CASES.append((name, bool(ok), detail))

profile = read("policies/SYSTEM_WIDE_QUALITY_PROFILE.md")
core = read("GEM_INSTRUCTIONS_PRODUCTION.md")
out = read("OUTPUT_CONTRACT.md")
w08 = read("workers/W08_LAYOUT_RENDER_THAI.md")
w09 = read("workers/W09_QA_RELEASE.md")
builder = read("tools/build_install_package.py")

workers = [
    "W01_ACADEMIC_CONTENT", "W02_TIME_CLOCK", "W03_WEIGHT_SCALE",
    "W04_LENGTH_DISTANCE", "W05_TEMPERATURE_CAPACITY_VOLUME",
    "W06_MONEY_CALENDAR_DATA", "W07_INSTRUMENT_AUDITOR",
    "W08_LAYOUT_RENDER_THAI", "W09_QA_RELEASE",
]

# 1-9: every base worker remains structurally contract-compatible.
for wid in workers:
    txt = read(f"workers/{wid}.md")
    add(f"worker-contract-{wid}",
        f"WORKER_ID={wid}" in txt and "## ACCEPTS" in txt and "## OWNS" in txt
        and "## RETURNS" in txt and "## MUST_NOT_DECIDE" in txt and "## QA" in txt)

# 10-21: shared profile contains every system-wide protection family.
profile_tokens = [
    "SYSTEM_OWNERSHIP_INTEGRITY_QA",
    "SYSTEM_PARAMETER_PROVENANCE_QA",
    "SYSTEM_INDEPENDENT_ORACLE_QA",
    "SYSTEM_ITEM_COUNT_QA",
    "SYSTEM_DIFFICULTY_FIDELITY_QA",
    "SYSTEM_TARGET_DISTRIBUTION_QA",
    "SYSTEM_VISIBILITY_ISOLATION_QA",
    "PROMPT_RENDER_STATE_SERIALIZATION_QA",
    "PROMPT_PAGE_POLICY_WORDING_QA",
    "SYSTEM_FINAL_PROMPT_SELF_CONTAINED_QA",
    "PROMPT_QA_EVIDENCE_CONSISTENCY_QA",
    "SYSTEM_PHASE_BOUNDARY_QA",
]
for token in profile_tokens:
    add(f"profile-{token}", token in profile)

# 22-30: integration/runtime/package protections.
checks = [
    ("core-inherits-profile", "SYSTEM_WIDE_QUALITY_PROFILE.md" in core),
    ("core-atomic-state", "PROMPT_RENDER_STATE_SERIALIZATION_QA" in core),
    ("output-atomic-state", "PROMPT_RENDER_STATE_SERIALIZATION_QA" in out),
    ("output-page-wording", "PROMPT_PAGE_POLICY_WORDING_QA" in out),
    ("w08-atomic-serializer", "PROMPT_RENDER_STATE_SERIALIZATION_QA" in w08),
    ("w08-page-wording", "PROMPT_PAGE_POLICY_WORDING_QA" in w08),
    ("w09-evidence-consistency", "PROMPT_QA_EVIDENCE_CONSISTENCY_QA" in w09),
    ("w09-difficulty-fidelity", "SYSTEM_DIFFICULTY_FIDELITY_QA" in w09),
    ("builder-shared-profile", "SYSTEM_WIDE_QUALITY_PROFILE.md" in builder),
]
for name, ok in checks:
    add(name, ok)

assert len(CASES) == 30, len(CASES)
failed = [c for c in CASES if not c[1]]
if failed:
    print(f"SYSTEM-WIDE QUALITY REGRESSION: FAIL ({len(failed)}/{len(CASES)})")
    for name, _, detail in failed:
        print("FAIL", name, detail)
    sys.exit(1)

print("SYSTEM-WIDE QUALITY REGRESSION: PASS")
print(f"cases: {len(CASES)}")
print(f"pass: {len(CASES)}")
print("fail: 0")
print("cross-worker architecture quality: 30/30 PASS")
print("artifact QA: NOT_YET_TESTED")
