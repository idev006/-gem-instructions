#!/usr/bin/env python3
"""Build the compact 9-Knowledge-file Gemini Gem installation package.

Package is derived from GitHub SSOT. Build is blocked unless static SSOT
validation and every release suite passes:
449 core + 360 skill + 12 runtime-UAT + 20 semantic-oracle + 30 system-wide
+ 40 scale-line + 60 instrument-review/speedometer + 24 protractor-scale = 995 cases total.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST_ROOT = ROOT / "dist"
PACKAGE_NAME = "activity-based-elementary-worksheet_Gem_v2.6.2_LTS_9WORKERS_TXT"
PACKAGE_DIR = DIST_ROOT / PACKAGE_NAME
ZIP_PATH = DIST_ROOT / f"{PACKAGE_NAME}.zip"

SYSTEM_PROFILE = "policies/SYSTEM_WIDE_QUALITY_PROFILE.md"
SCALE_LINE_PROFILE = "policies/SCALE_LINE_INTEGRITY_PROFILE.md"
REVIEW_PROFILE = "policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md"
SHARED_PROFILES = [SYSTEM_PROFILE, SCALE_LINE_PROFILE, REVIEW_PROFILE]

WORKER_BUNDLES: dict[str, list[str]] = {
    "W01_ACADEMIC_CONTENT.txt": ["workers/W01_ACADEMIC_CONTENT.md"],
    "W02_TIME_CLOCK.txt": [
        "workers/W02_TIME_CLOCK.md", "domains/TIME_ENGINE.md", "domains/CLOCK_READING_ENGINE.md",
        "domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md", "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md",
    ],
    "W03_WEIGHT_SCALE.txt": ["workers/W03_WEIGHT_SCALE.md", "domains/SCALE_READING_ENGINE.md"],
    "W04_LENGTH_DISTANCE.txt": [
        "workers/W04_LENGTH_DISTANCE.md", "domains/LENGTH_READING_ENGINE.md", "domains/SPEEDOMETER_READING_ENGINE.md",
    ],
    "W05_TEMPERATURE_CAPACITY_VOLUME.txt": [
        "workers/W05_TEMPERATURE_CAPACITY_VOLUME.md", "domains/TEMPERATURE_READING_ENGINE.md", "domains/CAPACITY_READING_ENGINE.md",
    ],
    "W06_MONEY_CALENDAR_DATA.txt": [
        "workers/W06_MONEY_CALENDAR_DATA.md", "domains/MONEY_ENGINE.md", "domains/CALENDAR_ENGINE.md", "domains/TABLE_GRAPH_READING_ENGINE.md",
    ],
    "W07_INSTRUMENT_AUDITOR.txt": ["workers/W07_INSTRUMENT_AUDITOR.md", "domains/INSTRUMENT_READING_ENGINE.md"],
    "W08_LAYOUT_RENDER_THAI.txt": ["workers/W08_LAYOUT_RENDER_THAI.md"],
    "W09_QA_RELEASE.txt": [
        "workers/W09_QA_RELEASE.md", "OUTPUT_CONTRACT.md", "ARCHITECTURE.md", "KB_ROUTER.md", "KB_MANIFEST.md",
        "policies/PARAMETER_POLICY.md", "policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md",
        "domains/DOMAIN_REGISTRY.md", "domains/MEASUREMENT_COVERAGE_P1_P6.md",
        "qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md", "qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md",
        "qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md", "qa/RUNTIME_UAT_CLOCK_REGRESSION_V2_6_X.md",
        "qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md", "qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md",
        "qa/BASELINE_2_6_2_RELEASE_CHECKLIST.md", "qa/DOMAIN_RELEASE_MATRIX.md",
    ],
}


def read(rel: str) -> str:
    p = ROOT / rel
    if not p.is_file():
        raise FileNotFoundError(rel)
    return p.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_gate(script: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(ROOT / "tools" / script)], cwd=ROOT.parent.parent, text=True, capture_output=True)


def bundle_text(worker_name: str, sources: list[str]) -> str:
    effective_sources = [*SHARED_PROFILES, *sources]
    header = (
        f"ACTIVITY-BASED ELEMENTARY WORKSHEET GENERATOR\nRUNTIME KNOWLEDGE BUNDLE: {worker_name}\n"
        "BASELINE=2.6.x\nWORKER_SCHEMA_VERSION=1\n\nIMPORTANT RUNTIME PACKAGING NOTE\n"
        "Generated from GitHub SSOT. Mandatory system-wide quality, scale-line integrity, and instrument review-revise profiles are embedded before worker/domain SSOT.\n\nEMBEDDED_SOURCES:\n"
    )
    header += "\n".join(f"- {s}" for s in effective_sources)
    sections = [header]
    for rel in effective_sources:
        sections.append(f"\n\n===== BEGIN EMBEDDED SSOT: {rel} =====\n\n{read(rel)}\n\n===== END EMBEDDED SSOT: {rel} =====")
    return "".join(sections) + "\n"


def gate(script: str, label: str) -> subprocess.CompletedProcess[str]:
    result = run_gate(script)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        print(f"BUILD BLOCKED: {label} failed", file=sys.stderr)
    return result


def main() -> int:
    validation = gate("validate_ssot.py", "SSOT validation")
    if validation.returncode != 0: return 1
    core = gate("full_dry_run_suite.py", "449-case core dry-run")
    if core.returncode != 0: return 1
    skill = gate("full_skill_matrix_suite.py", "360-case declared-skill matrix")
    if skill.returncode != 0: return 1
    uat = gate("runtime_uat_regression_suite.py", "12-case runtime UAT regression")
    if uat.returncode != 0: return 1
    semantic = gate("semantic_oracle_regression_suite.py", "20-case semantic-oracle regression")
    if semantic.returncode != 0: return 1
    system_quality = gate("system_wide_quality_regression_suite.py", "30-case system-wide quality regression")
    if system_quality.returncode != 0: return 1
    scale_line = gate("scale_line_integrity_regression_suite.py", "40-case scale-line integrity regression")
    if scale_line.returncode != 0: return 1
    instrument_review = gate("instrument_review_speedometer_regression_suite.py", "60-case instrument review/speedometer regression")
    if instrument_review.returncode != 0: return 1
    protractor_scale = gate("protractor_scale_safety_regression_suite.py", "24-case protractor scale safety regression")
    if protractor_scale.returncode != 0: return 1

    if PACKAGE_DIR.exists(): shutil.rmtree(PACKAGE_DIR)
    if ZIP_PATH.exists(): ZIP_PATH.unlink()
    instructions_dir = PACKAGE_DIR / "01_MAIN_INSTRUCTIONS"
    knowledge_dir = PACKAGE_DIR / "02_UPLOAD_9_WORKER_KNOWLEDGE_TXT"
    guide_dir = PACKAGE_DIR / "03_GUIDE"
    instructions_dir.mkdir(parents=True); knowledge_dir.mkdir(parents=True); guide_dir.mkdir(parents=True)

    compact_note = (
        "COMPACT RUNTIME PROFILE\n"
        "The 9 Knowledge TXT files are generated bundles with all mandatory shared safety profiles embedded.\n"
        "Built only after SSOT validation + 449 core + 360 skill + 12 runtime-UAT + 20 semantic-oracle + 30 system-wide + 40 scale-line + 60 instrument-review/speedometer + 24 protractor-scale = 995/995 PASS.\n\n"
    )
    main_instructions = (
        compact_note
        + read("GEM_INSTRUCTIONS_PRODUCTION.md")
        + "\n\n===== MANDATORY SYSTEM-WIDE QUALITY PROFILE =====\n\n" + read(SYSTEM_PROFILE)
        + "\n\n===== MANDATORY SCALE-LINE INTEGRITY PROFILE =====\n\n" + read(SCALE_LINE_PROFILE)
        + "\n\n===== MANDATORY INSTRUMENT REVIEW-REVISE PROFILE =====\n\n" + read(REVIEW_PROFILE)
        + "\n\n===== MANDATORY RUNTIME PROFILE: THAI P3 ANALOG CLOCK =====\n\n" + read("policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md")
    )
    (instructions_dir / "GEM_ORCHESTRATOR_INSTRUCTIONS.txt").write_text(main_instructions, encoding="utf-8")

    for out_name, sources in WORKER_BUNDLES.items():
        (knowledge_dir / out_name).write_text(bundle_text(out_name, sources), encoding="utf-8")
    if len(list(knowledge_dir.glob("*.txt"))) != 9:
        raise RuntimeError("Knowledge bundle count must equal 9")

    install_guide = read("GEM_INSTALLATION_GUIDE.md")
    (PACKAGE_DIR / "INSTALL_ME_FIRST.txt").write_text(install_guide, encoding="utf-8")
    (guide_dir / "GEM_INSTALLATION_GUIDE.txt").write_text(install_guide, encoding="utf-8")
    (guide_dir / "MEASUREMENT_COMMAND_CATALOG_P1_P6.txt").write_text(read("examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md"), encoding="utf-8")
    (guide_dir / "CLOCK_DAY_NIGHT_SINGLE_FACE_COMMANDS.txt").write_text(read("examples/CLOCK_DAY_NIGHT_SINGLE_FACE_COMMANDS.md"), encoding="utf-8")
    (guide_dir / "SSOT_VALIDATION_REPORT.txt").write_text(validation.stdout, encoding="utf-8")
    (guide_dir / "FULL_DRY_RUN_449_REPORT.txt").write_text(core.stdout, encoding="utf-8")
    (guide_dir / "FULL_SKILL_MATRIX_360_REPORT.txt").write_text(skill.stdout, encoding="utf-8")
    (guide_dir / "RUNTIME_UAT_REGRESSION_12_REPORT.txt").write_text(uat.stdout, encoding="utf-8")
    (guide_dir / "SEMANTIC_ORACLE_REGRESSION_20_REPORT.txt").write_text(semantic.stdout, encoding="utf-8")
    (guide_dir / "SYSTEM_WIDE_QUALITY_REGRESSION_30_REPORT.txt").write_text(system_quality.stdout, encoding="utf-8")
    (guide_dir / "SCALE_LINE_INTEGRITY_REGRESSION_40_REPORT.txt").write_text(scale_line.stdout, encoding="utf-8")
    (guide_dir / "INSTRUMENT_REVIEW_SPEEDOMETER_REGRESSION_60_REPORT.txt").write_text(instrument_review.stdout, encoding="utf-8")
    (guide_dir / "PROTRACTOR_SCALE_SAFETY_REGRESSION_24_REPORT.txt").write_text(protractor_scale.stdout, encoding="utf-8")
    (guide_dir / "ACTUAL_RULER_EXTRA_TICK_REGRESSION.txt").write_text(read("qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md"), encoding="utf-8")

    manifest = []
    for path in sorted(PACKAGE_DIR.rglob("*")):
        if path.is_file():
            manifest.append({"path": str(path.relative_to(PACKAGE_DIR)), "bytes": path.stat().st_size, "sha256": sha256(path)})
    (PACKAGE_DIR / "BUNDLE_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in sorted(PACKAGE_DIR.rglob("*")):
            if path.is_file():
                z.write(path, arcname=str(PACKAGE_DIR.name / path.relative_to(PACKAGE_DIR)))
    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        bad = z.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP integrity failure: {bad}")

    for result in (validation, core, skill, uat, semantic, system_quality, scale_line, instrument_review, protractor_scale):
        print(result.stdout.strip())
    print("COMBINED DRY-RUN: 995/995 PASS")
    print("PACKAGE BUILD: PASS")
    print("Knowledge files: 9")
    print(f"ZIP: {ZIP_PATH}")
    print(f"ZIP SHA256: {sha256(ZIP_PATH)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
