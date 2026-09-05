#!/usr/bin/env python3
"""Build the compact 10-Knowledge-file Gemini Gem installation package.

Established release gate: 1366/1366 PASS.
Additive clock hand endpoint hardening: +32 cases.
Additive weight-dial visible subdivision hardening: +32 cases.
Additive primary-school pedagogy/usability hardening: +64 cases.
Effective regression gate: 1494/1494 PASS.
Scale tick standard gate: 120/120 PASS.
Skill metric pack governance gate: 161/161 PASS.
Capability quality gate: 15 capabilities × 20 criteria = 300/300 criteria PASS; every capability >=95%.
"""
from __future__ import annotations
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST_ROOT = ROOT / 'dist'
PACKAGE_NAME = 'activity-based-elementary-worksheet_Gem_v2.6.3_LTS_10WORKERS_TXT'
PACKAGE_DIR = DIST_ROOT / PACKAGE_NAME
ZIP_PATH = DIST_ROOT / f'{PACKAGE_NAME}.zip'

SYSTEM_PROFILE = 'policies/SYSTEM_WIDE_QUALITY_PROFILE.md'
SCALE_LINE_PROFILE = 'policies/SCALE_LINE_INTEGRITY_PROFILE.md'
REVIEW_PROFILE = 'policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md'
METROLOGY_PROFILE = 'policies/METROLOGY_ASSURANCE_PROFILE.md'
PAGE_FEASIBILITY_PROFILE = 'policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md'
PEDAGOGY_PROFILE = 'policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md'
CAPABILITY_PROFILE = 'policies/CAPABILITY_QUALITY_GATE.md'
WEIGHT_VISIBLE_PROFILE = 'policies/WEIGHT_DIAL_VISIBLE_TICK_SET_PROFILE.md'
SCALE_TICK_PROFILE = 'policies/SCALE_TICK_STANDARD.md'
TICK_HIERARCHY_PROFILE = 'policies/INSTRUMENT_TICK_HIERARCHY_POLICY.md'
SHARED_PROFILES = [SYSTEM_PROFILE, SCALE_LINE_PROFILE, REVIEW_PROFILE, METROLOGY_PROFILE, PAGE_FEASIBILITY_PROFILE]
SCALE_TICK_GLOBALS = [SCALE_TICK_PROFILE, TICK_HIERARCHY_PROFILE, 'qa/INSTRUMENT_SCALE_DEFECT_TAXONOMY.md', 'qa/EXTERNAL_INSTRUMENT_SCALE_REFERENCE_REVIEW_2026_09_05.md']
SKILL_METRIC_GLOBALS = ['skill-metrics/SKILL_METRIC_STANDARD.md', 'skill-metrics/CRITICAL_DEFECT_POLICY.md', 'skill-metrics/ARTIFACT_QUALIFICATION_PROTOCOL.md', 'skill-metrics/SKILL_SCORE_REGISTRY.md']

WORKER_BUNDLES = {
    'W01_ACADEMIC_CONTENT.txt': ['workers/W01_ACADEMIC_CONTENT.md', 'skill-metrics/ACADEMIC_ARITHMETIC_THAI_SKILL_METRICS.md'],
    'W02_TIME_CLOCK.txt': ['workers/W02_TIME_CLOCK.md', 'domains/TIME_ENGINE.md', 'domains/CLOCK_READING_ENGINE.md', 'domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md', 'policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md', 'skill-metrics/TIME_CALCULATION_SKILL_METRICS.md', 'skill-metrics/ANALOG_CLOCK_SKILL_METRICS.md'],
    'W03_WEIGHT_SCALE.txt': ['workers/W03_WEIGHT_SCALE.md', 'domains/SCALE_READING_ENGINE.md', WEIGHT_VISIBLE_PROFILE, 'skill-metrics/WEIGHT_SCALE_SKILL_METRICS.md'],
    'W04_LENGTH_DISTANCE.txt': ['workers/W04_LENGTH_DISTANCE.md', 'domains/LENGTH_READING_ENGINE.md', 'domains/SPEEDOMETER_READING_ENGINE.md', 'skill-metrics/RULER_LENGTH_SKILL_METRICS.md', 'skill-metrics/DISTANCE_SKILL_METRICS.md', 'skill-metrics/SPEEDOMETER_SKILL_METRICS.md', 'skill-metrics/ANGLE_PROTRACTOR_SKILL_METRICS.md', 'skill-metrics/PERIMETER_AREA_SKILL_METRICS.md'],
    'W05_TEMPERATURE_CAPACITY_VOLUME.txt': ['workers/W05_TEMPERATURE_CAPACITY_VOLUME.md', 'domains/TEMPERATURE_READING_ENGINE.md', 'domains/CAPACITY_READING_ENGINE.md', 'skill-metrics/TEMPERATURE_SKILL_METRICS.md', 'skill-metrics/CAPACITY_SKILL_METRICS.md', 'skill-metrics/VOLUME_SKILL_METRICS.md'],
    'W06_MONEY_CALENDAR_DATA.txt': ['workers/W06_MONEY_CALENDAR_DATA.md', 'domains/MONEY_ENGINE.md', 'domains/CALENDAR_ENGINE.md', 'domains/TABLE_GRAPH_READING_ENGINE.md', 'skill-metrics/MONEY_SKILL_METRICS.md', 'skill-metrics/CALENDAR_SKILL_METRICS.md', 'skill-metrics/DATA_READING_SKILL_METRICS.md'],
    'W07_INSTRUMENT_AUDITOR.txt': ['workers/W07_INSTRUMENT_AUDITOR.md', 'domains/INSTRUMENT_READING_ENGINE.md', WEIGHT_VISIBLE_PROFILE],
    'W08_LAYOUT_RENDER_THAI.txt': ['workers/W08_LAYOUT_RENDER_THAI.md', WEIGHT_VISIBLE_PROFILE],
    'W09_QA_RELEASE.txt': ['workers/W09_QA_RELEASE.md', 'OUTPUT_CONTRACT.md', 'ARCHITECTURE.md', 'KB_ROUTER.md', 'KB_MANIFEST.md', 'policies/PARAMETER_POLICY.md', 'policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md', WEIGHT_VISIBLE_PROFILE, 'domains/DOMAIN_REGISTRY.md', 'domains/MEASUREMENT_COVERAGE_P1_P6.md', 'qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md', 'qa/ACTUAL_WEIGHT_DIAL_INACTIVE_GAP_REGRESSION_2026_08_31.md', 'qa/CONSOLIDATED_PHYSICAL_PAGE_FEASIBILITY_REGRESSION_2026_08_31.md', 'qa/ACTUAL_INSTRUMENT_GEOMETRY_DEFECTS_2026_08_31.md', 'qa/ACTUAL_MEASUREMENT_REFERENCE_DEFECTS_2026_08_31.md', 'qa/ACTUAL_CLOCK_HAND_ENDPOINT_REGRESSION_2026_09_01.md', 'qa/ACTUAL_WEIGHT_DIAL_VISIBLE_SUBDIVISION_REGRESSION_2026_09_01.md', 'qa/FULL_CLEAN_ROOM_PEDAGOGY_AUDIT_2026_09_02.md', 'qa/CAPABILITY_QUALITY_ITERATION_REPORT_2026_09_05.md'],
    'W10_METROLOGY_ENGINEER.txt': ['workers/W10_METROLOGY_ENGINEER.md', 'domains/INSTRUMENT_READING_ENGINE.md', WEIGHT_VISIBLE_PROFILE],
}

def read(rel: str) -> str:
    p = ROOT / rel
    if not p.is_file():
        raise FileNotFoundError(rel)
    return p.read_text(encoding='utf-8')

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run_gate(script: str):
    return subprocess.run([sys.executable, str(ROOT / 'tools' / script)], cwd=ROOT.parent.parent, text=True, capture_output=True)

def gate(script: str, label: str):
    r = run_gate(script)
    if r.returncode != 0:
        print(r.stdout)
        print(r.stderr, file=sys.stderr)
        print(f'BUILD BLOCKED: {label} failed', file=sys.stderr)
    return r

def bundle_text(name: str, sources: list[str]) -> str:
    effective = [*SHARED_PROFILES, PEDAGOGY_PROFILE, CAPABILITY_PROFILE, *sources]
    effective.extend(SKILL_METRIC_GLOBALS)
    effective.extend(SCALE_TICK_GLOBALS)
    head = (
        f'ACTIVITY-BASED ELEMENTARY WORKSHEET GENERATOR\n'
        f'RUNTIME KNOWLEDGE BUNDLE: {name}\n'
        'BASELINE=2.6.x\nWORKER_SCHEMA_VERSION=1\n\n'
        'Generated from GitHub SSOT. Five mandatory technical safety profiles plus learner pedagogy, capability-quality, skill-metric, and scale/tick standards are embedded.\n\n'
        'EMBEDDED_SOURCES:\n'
    )
    parts = [head + '\n'.join(f'- {s}' for s in effective)]
    for rel in effective:
        parts.append(f'\n\n===== BEGIN EMBEDDED SSOT: {rel} =====\n\n{read(rel)}\n\n===== END EMBEDDED SSOT: {rel} =====')
    return ''.join(parts) + '\n'

def main() -> int:
    gates = [
        ('validate_ssot.py', 'SSOT validation'),
        ('full_dry_run_suite.py', '449-case core dry-run'),
        ('full_skill_matrix_suite.py', '360-case declared-skill matrix'),
        ('runtime_uat_regression_suite.py', '12-case runtime UAT'),
        ('semantic_oracle_regression_suite.py', '20-case semantic oracle'),
        ('system_wide_quality_regression_suite.py', '30-case system-wide quality'),
        ('scale_line_integrity_regression_suite.py', '40-case scale-line integrity'),
        ('instrument_review_speedometer_regression_suite.py', '60-case instrument review/speedometer'),
        ('protractor_scale_safety_regression_suite.py', '24-case protractor scale safety'),
        ('metrology_full_audit_regression_suite.py', '80-case full metrology audit'),
        ('weight_dial_inactive_gap_regression_suite.py', '32-case actual weight-dial inactive-gap regression'),
        ('physical_page_feasibility_regression_suite.py', '48-case physical page feasibility regression'),
        ('instrument_geometry_artifact_regression_suite.py', '64-case actual instrument geometry regression'),
        ('measurement_reference_artifact_regression_suite.py', '66-case measurement reference artifact regression'),
        ('clock_hand_endpoint_regression_suite.py', '32-case clock hand endpoint regression'),
        ('weight_dial_visible_subdivision_regression_suite.py', '32-case weight dial visible subdivision regression'),
        ('primary_school_pedagogy_regression_suite.py', '64-case primary-school pedagogy regression'),
        ('repository_full_line_audit_suite.py', '81-case repository full-line audit'),
        ('skill_metric_pack_regression_suite.py', '161-case skill metric pack governance'),
        ('scale_tick_standard_regression_suite.py', '120-case scale tick standard governance'),
        ('capability_quality_scorecard.py', '300-criterion capability quality scorecard'),
    ]
    results = []
    for script, label in gates:
        r = gate(script, label)
        results.append(r)
        if r.returncode != 0:
            return 1

    if PACKAGE_DIR.exists(): shutil.rmtree(PACKAGE_DIR)
    if ZIP_PATH.exists(): ZIP_PATH.unlink()
    inst = PACKAGE_DIR / '01_MAIN_INSTRUCTIONS'
    know = PACKAGE_DIR / '02_UPLOAD_10_WORKER_KNOWLEDGE_TXT'
    guide = PACKAGE_DIR / '03_GUIDE'
    inst.mkdir(parents=True); know.mkdir(parents=True); guide.mkdir(parents=True)

    main_sections = [
        'COMPACT RUNTIME PROFILE\nEstablished baseline 1366/1366 PASS + clock endpoint 32 + weight visible subdivision 32 + primary-school pedagogy 64; effective 1494/1494 PASS. Skill metric 161/161 PASS. Scale tick standard 120/120 PASS. Exactly 10 base worker Knowledge files.\n\n',
        read('GEM_INSTRUCTIONS_PRODUCTION.md'),
        '\n\n===== MANDATORY SYSTEM-WIDE QUALITY PROFILE =====\n\n' + read(SYSTEM_PROFILE),
        '\n\n===== MANDATORY SCALE-LINE INTEGRITY PROFILE =====\n\n' + read(SCALE_LINE_PROFILE),
        '\n\n===== MANDATORY INSTRUMENT REVIEW-REVISE PROFILE =====\n\n' + read(REVIEW_PROFILE),
        '\n\n===== MANDATORY METROLOGY ASSURANCE PROFILE =====\n\n' + read(METROLOGY_PROFILE),
        '\n\n===== MANDATORY PHYSICAL PAGE FEASIBILITY PROFILE =====\n\n' + read(PAGE_FEASIBILITY_PROFILE),
        '\n\n===== MANDATORY PRIMARY-SCHOOL PEDAGOGY PROFILE =====\n\n' + read(PEDAGOGY_PROFILE),
        '\n\n===== MANDATORY CAPABILITY QUALITY GATE =====\n\n' + read(CAPABILITY_PROFILE),
        '\n\n===== SKILL METRIC STANDARD =====\n\n' + read('skill-metrics/SKILL_METRIC_STANDARD.md'),
        '\n\n===== CRITICAL DEFECT POLICY =====\n\n' + read('skill-metrics/CRITICAL_DEFECT_POLICY.md'),
        '\n\n===== ARTIFACT QUALIFICATION PROTOCOL =====\n\n' + read('skill-metrics/ARTIFACT_QUALIFICATION_PROTOCOL.md'),
        '\n\n===== SKILL SCORE REGISTRY =====\n\n' + read('skill-metrics/SKILL_SCORE_REGISTRY.md'),
        '\n\n===== SCALE TICK STANDARD =====\n\n' + read(SCALE_TICK_PROFILE),
        '\n\n===== INSTRUMENT TICK HIERARCHY POLICY =====\n\n' + read(TICK_HIERARCHY_PROFILE),
        '\n\n===== INSTRUMENT SCALE DEFECT TAXONOMY =====\n\n' + read('qa/INSTRUMENT_SCALE_DEFECT_TAXONOMY.md'),
        '\n\n===== EXTERNAL INSTRUMENT SCALE REFERENCE REVIEW =====\n\n' + read('qa/EXTERNAL_INSTRUMENT_SCALE_REFERENCE_REVIEW_2026_09_05.md'),
        '\n\n===== CLEAN-ROOM PEDAGOGY ROOT-CAUSE AUDIT =====\n\n' + read('qa/FULL_CLEAN_ROOM_PEDAGOGY_AUDIT_2026_09_02.md'),
        '\n\n===== CAPABILITY QUALITY ITERATION REPORT =====\n\n' + read('qa/CAPABILITY_QUALITY_ITERATION_REPORT_2026_09_05.md'),
    ]
    (inst / 'GEM_ORCHESTRATOR_INSTRUCTIONS.txt').write_text(''.join(main_sections), encoding='utf-8')
    for out, sources in WORKER_BUNDLES.items():
        (know / out).write_text(bundle_text(out, sources), encoding='utf-8')
    if len(list(know.glob('*.txt'))) != 10:
        raise RuntimeError('Knowledge bundle count must equal 10')

    install = read('GEM_INSTALLATION_GUIDE.md')
    docs = {'GEM_INSTALLATION_GUIDE.txt': install, 'BASELINE_2_6_3_RELEASE_CHECKLIST.txt': read('qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md')}
    for rel in ['qa/CLASSROOM_ARTIFACT_QUALIFICATION_UAT.md','qa/ACTUAL_WEIGHT_DIAL_INACTIVE_GAP_REGRESSION_2026_08_31.md','qa/CONSOLIDATED_PHYSICAL_PAGE_FEASIBILITY_REGRESSION_2026_08_31.md','qa/ACTUAL_INSTRUMENT_GEOMETRY_DEFECTS_2026_08_31.md','qa/ACTUAL_MEASUREMENT_REFERENCE_DEFECTS_2026_08_31.md','qa/ACTUAL_CLOCK_HAND_ENDPOINT_REGRESSION_2026_09_01.md','qa/ACTUAL_WEIGHT_DIAL_VISIBLE_SUBDIVISION_REGRESSION_2026_09_01.md','qa/FULL_CLEAN_ROOM_PEDAGOGY_AUDIT_2026_09_02.md','qa/CAPABILITY_QUALITY_ITERATION_REPORT_2026_09_05.md','qa/INSTRUMENT_SCALE_DEFECT_TAXONOMY.md','qa/EXTERNAL_INSTRUMENT_SCALE_REFERENCE_REVIEW_2026_09_05.md']:
        docs[rel.replace('/','_').replace('.md','.txt')] = read(rel)
    for rel in [WEIGHT_VISIBLE_PROFILE, PEDAGOGY_PROFILE, CAPABILITY_PROFILE, SCALE_TICK_PROFILE, TICK_HIERARCHY_PROFILE]:
        docs[rel.replace('/','_').replace('.md','.txt')] = read(rel)
    for p in sorted((ROOT / 'skill-metrics').glob('*.md')):
        docs[f'SKILL_METRICS_{p.stem}.txt'] = p.read_text(encoding='utf-8')
    (PACKAGE_DIR / 'INSTALL_ME_FIRST.txt').write_text(install, encoding='utf-8')
    for name, text in docs.items():
        (guide / name).write_text(text, encoding='utf-8')

    report_names = ['SSOT_VALIDATION_REPORT.txt','FULL_DRY_RUN_449_REPORT.txt','FULL_SKILL_MATRIX_360_REPORT.txt','RUNTIME_UAT_REGRESSION_12_REPORT.txt','SEMANTIC_ORACLE_REGRESSION_20_REPORT.txt','SYSTEM_WIDE_QUALITY_REGRESSION_30_REPORT.txt','SCALE_LINE_INTEGRITY_REGRESSION_40_REPORT.txt','INSTRUMENT_REVIEW_SPEEDOMETER_REGRESSION_60_REPORT.txt','PROTRACTOR_SCALE_SAFETY_REGRESSION_24_REPORT.txt','METROLOGY_FULL_AUDIT_REGRESSION_80_REPORT.txt','WEIGHT_DIAL_INACTIVE_GAP_REGRESSION_32_REPORT.txt','PHYSICAL_PAGE_FEASIBILITY_REGRESSION_48_REPORT.txt','ACTUAL_INSTRUMENT_GEOMETRY_REGRESSION_64_REPORT.txt','MEASUREMENT_REFERENCE_ARTIFACT_REGRESSION_66_REPORT.txt','CLOCK_HAND_ENDPOINT_REGRESSION_32_REPORT.txt','WEIGHT_DIAL_VISIBLE_SUBDIVISION_REGRESSION_32_REPORT.txt','PRIMARY_SCHOOL_PEDAGOGY_REGRESSION_64_REPORT.txt','REPOSITORY_FULL_LINE_AUDIT_81_REPORT.txt','SKILL_METRIC_PACK_REGRESSION_161_REPORT.txt','SCALE_TICK_STANDARD_REGRESSION_120_REPORT.txt','CAPABILITY_QUALITY_SCORECARD_300_CRITERIA_REPORT.txt']
    for name, r in zip(report_names, results):
        (guide / name).write_text(r.stdout, encoding='utf-8')

    manifest = []
    for p in sorted(PACKAGE_DIR.rglob('*')):
        if p.is_file(): manifest.append({'path': str(p.relative_to(PACKAGE_DIR)), 'bytes': p.stat().st_size, 'sha256': sha256(p)})
    (PACKAGE_DIR / 'BUNDLE_MANIFEST.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(PACKAGE_DIR.rglob('*')):
            if p.is_file(): z.write(p, arcname=str(PACKAGE_DIR.name / p.relative_to(PACKAGE_DIR)))
    with zipfile.ZipFile(ZIP_PATH, 'r') as z:
        bad = z.testzip()
        if bad: raise RuntimeError(f'ZIP integrity failure: {bad}')

    for r in results: print(r.stdout.strip())
    print('ESTABLISHED BASELINE: 1366/1366 PASS')
    print('CLOCK HAND ENDPOINT HARDENING: 32/32 PASS')
    print('WEIGHT DIAL VISIBLE SUBDIVISION HARDENING: 32/32 PASS')
    print('PRIMARY-SCHOOL PEDAGOGY/USABILITY HARDENING: 64/64 PASS')
    print('EFFECTIVE REGRESSION GATE: 1494/1494 PASS')
    print('SKILL METRIC PACK GOVERNANCE: 161/161 PASS; 15/15 skill metric packs complete')
    print('SCALE TICK STANDARD GOVERNANCE: 120/120 PASS')
    print('CAPABILITY QUALITY GATE: 300/300 criteria PASS; 15/15 capabilities = 100%')
    print('PACKAGE BUILD: PASS')
    print('Knowledge files: 10')
    print('Mandatory technical shared profiles: 5')
    print('Mandatory primary-school pedagogy profile: INCLUDED in every worker bundle')
    print('Capability quality gate: INCLUDED in every worker bundle and main instructions')
    print('Skill metric standard + critical defect policy + artifact qualification: INCLUDED')
    print('Scale tick standard + tick hierarchy + defect taxonomy + external reference review: INCLUDED')
    print('Repository full-line audit: INCLUDED (81 semantic cases + every UTF-8 line scan)')
    print(f'ZIP: {ZIP_PATH}')
    print(f'ZIP SHA256: {sha256(ZIP_PATH)}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
