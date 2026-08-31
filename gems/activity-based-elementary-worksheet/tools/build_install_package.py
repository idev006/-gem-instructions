#!/usr/bin/env python3
"""Build the compact 9-Knowledge-file Gemini Gem installation package.

Run from repository root:
    python gems/activity-based-elementary-worksheet/tools/build_install_package.py

The package is DERIVED from GitHub SSOT. Do not hand-maintain a competing ZIP.
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
PACKAGE_NAME = "activity-based-elementary-worksheet_Gem_v2.6.0_LTS_9WORKERS_TXT"
PACKAGE_DIR = DIST_ROOT / PACKAGE_NAME
ZIP_PATH = DIST_ROOT / f"{PACKAGE_NAME}.zip"

WORKER_BUNDLES: dict[str, list[str]] = {
    "W01_ACADEMIC_CONTENT.txt": [
        "workers/W01_ACADEMIC_CONTENT.md",
    ],
    "W02_TIME_CLOCK.txt": [
        "workers/W02_TIME_CLOCK.md",
        "domains/TIME_ENGINE.md",
        "domains/CLOCK_READING_ENGINE.md",
        "domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md",
    ],
    "W03_WEIGHT_SCALE.txt": [
        "workers/W03_WEIGHT_SCALE.md",
        "domains/SCALE_READING_ENGINE.md",
    ],
    "W04_LENGTH_DISTANCE.txt": [
        "workers/W04_LENGTH_DISTANCE.md",
        "domains/LENGTH_READING_ENGINE.md",
    ],
    "W05_TEMPERATURE_CAPACITY_VOLUME.txt": [
        "workers/W05_TEMPERATURE_CAPACITY_VOLUME.md",
        "domains/TEMPERATURE_READING_ENGINE.md",
        "domains/CAPACITY_READING_ENGINE.md",
    ],
    "W06_MONEY_CALENDAR_DATA.txt": [
        "workers/W06_MONEY_CALENDAR_DATA.md",
        "domains/MONEY_ENGINE.md",
        "domains/CALENDAR_ENGINE.md",
        "domains/TABLE_GRAPH_READING_ENGINE.md",
    ],
    "W07_INSTRUMENT_AUDITOR.txt": [
        "workers/W07_INSTRUMENT_AUDITOR.md",
        "domains/INSTRUMENT_READING_ENGINE.md",
    ],
    "W08_LAYOUT_RENDER_THAI.txt": [
        "workers/W08_LAYOUT_RENDER_THAI.md",
    ],
    "W09_QA_RELEASE.txt": [
        "workers/W09_QA_RELEASE.md",
        "OUTPUT_CONTRACT.md",
        "ARCHITECTURE.md",
        "KB_ROUTER.md",
        "KB_MANIFEST.md",
        "policies/PARAMETER_POLICY.md",
        "domains/DOMAIN_REGISTRY.md",
        "domains/MEASUREMENT_COVERAGE_P1_P6.md",
        "qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md",
        "qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md",
        "qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md",
        "qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md",
        "qa/BASELINE_2_6_0_RELEASE_CHECKLIST.md",
        "qa/DOMAIN_RELEASE_MATRIX.md",
    ],
}


def read(rel: str) -> str:
    p = ROOT / rel
    if not p.is_file():
        raise FileNotFoundError(rel)
    return p.read_text(encoding="utf-8")


def bundle_text(worker_name: str, sources: list[str]) -> str:
    header = f"""ACTIVITY-BASED ELEMENTARY WORKSHEET GENERATOR\nRUNTIME KNOWLEDGE BUNDLE: {worker_name}\nBASELINE=2.6.x\nWORKER_SCHEMA_VERSION=1\n\nIMPORTANT RUNTIME PACKAGING NOTE\nThis TXT file is generated from GitHub SSOT. Repository path references inside the text are provenance/logical references, not missing runtime dependencies. Supporting SSOT listed below is embedded in this same Knowledge bundle.\n\nEMBEDDED_SOURCES:\n"""
    header += "\n".join(f"- {s}" for s in sources)
    sections = [header]
    for rel in sources:
        sections.append(f"\n\n===== BEGIN EMBEDDED SSOT: {rel} =====\n\n{read(rel)}\n\n===== END EMBEDDED SSOT: {rel} =====")
    return "".join(sections) + "\n"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    validator = ROOT / "tools" / "validate_ssot.py"
    result = subprocess.run([sys.executable, str(validator)], cwd=ROOT.parent.parent, text=True, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        print("BUILD BLOCKED: SSOT validation failed", file=sys.stderr)
        return 1

    if PACKAGE_DIR.exists():
        shutil.rmtree(PACKAGE_DIR)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()

    instructions_dir = PACKAGE_DIR / "01_MAIN_INSTRUCTIONS"
    knowledge_dir = PACKAGE_DIR / "02_UPLOAD_9_WORKER_KNOWLEDGE_TXT"
    guide_dir = PACKAGE_DIR / "03_GUIDE"
    instructions_dir.mkdir(parents=True)
    knowledge_dir.mkdir(parents=True)
    guide_dir.mkdir(parents=True)

    compact_note = """COMPACT RUNTIME PROFILE\nThe 9 uploaded Knowledge TXT files are generated bundles. Supporting repository SSOT (registry, policies, domain engines, QA) is embedded inside the appropriate worker bundle, especially W09. Repository filenames referenced below are logical provenance and do not need separate Gemini Knowledge uploads.\n\n"""
    (instructions_dir / "GEM_ORCHESTRATOR_INSTRUCTIONS.txt").write_text(
        compact_note + read("GEM_INSTRUCTIONS_PRODUCTION.md"), encoding="utf-8"
    )

    for out_name, sources in WORKER_BUNDLES.items():
        (knowledge_dir / out_name).write_text(bundle_text(out_name, sources), encoding="utf-8")

    if len(list(knowledge_dir.glob("*.txt"))) != 9:
        raise RuntimeError("Knowledge bundle count must equal 9")

    install_guide = read("GEM_INSTALLATION_GUIDE.md")
    (PACKAGE_DIR / "INSTALL_ME_FIRST.txt").write_text(install_guide, encoding="utf-8")
    (guide_dir / "GEM_INSTALLATION_GUIDE.txt").write_text(install_guide, encoding="utf-8")
    (guide_dir / "MEASUREMENT_COMMAND_CATALOG_P1_P6.txt").write_text(
        read("examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md"), encoding="utf-8"
    )
    (guide_dir / "CLOCK_DAY_NIGHT_SINGLE_FACE_COMMANDS.txt").write_text(
        read("examples/CLOCK_DAY_NIGHT_SINGLE_FACE_COMMANDS.md"), encoding="utf-8"
    )
    (guide_dir / "SSOT_VALIDATION_REPORT.txt").write_text(result.stdout, encoding="utf-8")

    manifest = []
    for path in sorted(PACKAGE_DIR.rglob("*")):
        if path.is_file():
            manifest.append({
                "path": str(path.relative_to(PACKAGE_DIR)),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            })
    (PACKAGE_DIR / "BUNDLE_MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in sorted(PACKAGE_DIR.rglob("*")):
            if path.is_file():
                z.write(path, arcname=str(PACKAGE_DIR.name / path.relative_to(PACKAGE_DIR)))

    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        bad = z.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP integrity failure: {bad}")

    print(result.stdout.strip())
    print("PACKAGE BUILD: PASS")
    print("Knowledge files: 9")
    print(f"ZIP: {ZIP_PATH}")
    print(f"ZIP SHA256: {sha256(ZIP_PATH)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
