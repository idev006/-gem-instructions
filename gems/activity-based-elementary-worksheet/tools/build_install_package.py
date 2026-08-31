#!/usr/bin/env python3
"""Build the compact 10-Knowledge-file Gemini Gem installation package.

Release gate: 449 core + 360 skill + 12 runtime UAT + 20 semantic oracle +
30 system-wide + 40 scale-line + 60 instrument-review/speedometer +
24 protractor-safety + 80 full-metrology = 1075 cases.
"""
from __future__ import annotations
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, zipfile

ROOT=Path(__file__).resolve().parents[1]
DIST_ROOT=ROOT/'dist'
PACKAGE_NAME='activity-based-elementary-worksheet_Gem_v2.6.3_LTS_10WORKERS_TXT'
PACKAGE_DIR=DIST_ROOT/PACKAGE_NAME
ZIP_PATH=DIST_ROOT/f'{PACKAGE_NAME}.zip'

SYSTEM_PROFILE='policies/SYSTEM_WIDE_QUALITY_PROFILE.md'
SCALE_LINE_PROFILE='policies/SCALE_LINE_INTEGRITY_PROFILE.md'
REVIEW_PROFILE='policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md'
METROLOGY_PROFILE='policies/METROLOGY_ASSURANCE_PROFILE.md'
SHARED_PROFILES=[SYSTEM_PROFILE,SCALE_LINE_PROFILE,REVIEW_PROFILE,METROLOGY_PROFILE]

WORKER_BUNDLES={
'W01_ACADEMIC_CONTENT.txt':['workers/W01_ACADEMIC_CONTENT.md'],
'W02_TIME_CLOCK.txt':['workers/W02_TIME_CLOCK.md','domains/TIME_ENGINE.md','domains/CLOCK_READING_ENGINE.md','domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md','policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md'],
'W03_WEIGHT_SCALE.txt':['workers/W03_WEIGHT_SCALE.md','domains/SCALE_READING_ENGINE.md'],
'W04_LENGTH_DISTANCE.txt':['workers/W04_LENGTH_DISTANCE.md','domains/LENGTH_READING_ENGINE.md','domains/SPEEDOMETER_READING_ENGINE.md'],
'W05_TEMPERATURE_CAPACITY_VOLUME.txt':['workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','domains/TEMPERATURE_READING_ENGINE.md','domains/CAPACITY_READING_ENGINE.md'],
'W06_MONEY_CALENDAR_DATA.txt':['workers/W06_MONEY_CALENDAR_DATA.md','domains/MONEY_ENGINE.md','domains/CALENDAR_ENGINE.md','domains/TABLE_GRAPH_READING_ENGINE.md'],
'W07_INSTRUMENT_AUDITOR.txt':['workers/W07_INSTRUMENT_AUDITOR.md','domains/INSTRUMENT_READING_ENGINE.md'],
'W08_LAYOUT_RENDER_THAI.txt':['workers/W08_LAYOUT_RENDER_THAI.md'],
'W09_QA_RELEASE.txt':['workers/W09_QA_RELEASE.md','OUTPUT_CONTRACT.md','ARCHITECTURE.md','KB_ROUTER.md','KB_MANIFEST.md','policies/PARAMETER_POLICY.md','domains/DOMAIN_REGISTRY.md','domains/MEASUREMENT_COVERAGE_P1_P6.md','qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md'],
'W10_METROLOGY_ENGINEER.txt':['workers/W10_METROLOGY_ENGINEER.md','domains/INSTRUMENT_READING_ENGINE.md'],
}

def read(rel):
    p=ROOT/rel
    if not p.is_file(): raise FileNotFoundError(rel)
    return p.read_text(encoding='utf-8')

def sha256(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def run_gate(script): return subprocess.run([sys.executable,str(ROOT/'tools'/script)],cwd=ROOT.parent.parent,text=True,capture_output=True)
def gate(script,label):
    r=run_gate(script)
    if r.returncode!=0:
        print(r.stdout); print(r.stderr,file=sys.stderr); print(f'BUILD BLOCKED: {label} failed',file=sys.stderr)
    return r

def bundle_text(name,sources):
    effective_sources=[*SHARED_PROFILES,*sources]
    head=(f'ACTIVITY-BASED ELEMENTARY WORKSHEET GENERATOR\nRUNTIME KNOWLEDGE BUNDLE: {name}\n'
          'BASELINE=2.6.x\nWORKER_SCHEMA_VERSION=1\n\n'
          'Generated from GitHub SSOT. System quality, scale-line integrity, review-revise and independent metrology profiles are embedded.\n\nEMBEDDED_SOURCES:\n')
    head+='\n'.join(f'- {s}' for s in effective_sources)
    parts=[head]
    for rel in effective_sources:
        parts.append(f'\n\n===== BEGIN EMBEDDED SSOT: {rel} =====\n\n{read(rel)}\n\n===== END EMBEDDED SSOT: {rel} =====')
    return ''.join(parts)+'\n'

def main():
    gates=[
      ('validate_ssot.py','SSOT validation'),
      ('full_dry_run_suite.py','449-case core dry-run'),
      ('full_skill_matrix_suite.py','360-case declared-skill matrix'),
      ('runtime_uat_regression_suite.py','12-case runtime UAT'),
      ('semantic_oracle_regression_suite.py','20-case semantic oracle'),
      ('system_wide_quality_regression_suite.py','30-case system-wide quality'),
      ('scale_line_integrity_regression_suite.py','40-case scale-line integrity'),
      ('instrument_review_speedometer_regression_suite.py','60-case instrument review/speedometer'),
      ('protractor_scale_safety_regression_suite.py','24-case protractor scale safety'),
      ('metrology_full_audit_regression_suite.py','80-case full metrology audit'),
    ]
    results=[]
    for script,label in gates:
        r=gate(script,label); results.append(r)
        if r.returncode!=0: return 1

    if PACKAGE_DIR.exists(): shutil.rmtree(PACKAGE_DIR)
    if ZIP_PATH.exists(): ZIP_PATH.unlink()
    inst=PACKAGE_DIR/'01_MAIN_INSTRUCTIONS'; know=PACKAGE_DIR/'02_UPLOAD_10_WORKER_KNOWLEDGE_TXT'; guide=PACKAGE_DIR/'03_GUIDE'
    inst.mkdir(parents=True); know.mkdir(parents=True); guide.mkdir(parents=True)

    compact=('COMPACT RUNTIME PROFILE\nBuilt only after 1075/1075 PASS. Exactly 10 base worker Knowledge files.\n\n')
    main_text=(compact+read('GEM_INSTRUCTIONS_PRODUCTION.md')+
      '\n\n===== MANDATORY SYSTEM-WIDE QUALITY PROFILE =====\n\n'+read(SYSTEM_PROFILE)+
      '\n\n===== MANDATORY SCALE-LINE INTEGRITY PROFILE =====\n\n'+read(SCALE_LINE_PROFILE)+
      '\n\n===== MANDATORY INSTRUMENT REVIEW-REVISE PROFILE =====\n\n'+read(REVIEW_PROFILE)+
      '\n\n===== MANDATORY METROLOGY ASSURANCE PROFILE =====\n\n'+read(METROLOGY_PROFILE)+
      '\n\n===== MANDATORY RUNTIME PROFILE: THAI P3 ANALOG CLOCK =====\n\n'+read('policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md'))
    (inst/'GEM_ORCHESTRATOR_INSTRUCTIONS.txt').write_text(main_text,encoding='utf-8')

    for out,sources in WORKER_BUNDLES.items(): (know/out).write_text(bundle_text(out,sources),encoding='utf-8')
    if len(list(know.glob('*.txt')))!=10: raise RuntimeError('Knowledge bundle count must equal 10')

    install=read('GEM_INSTALLATION_GUIDE.md')
    (PACKAGE_DIR/'INSTALL_ME_FIRST.txt').write_text(install,encoding='utf-8')
    (guide/'GEM_INSTALLATION_GUIDE.txt').write_text(install,encoding='utf-8')
    report_names=['SSOT_VALIDATION_REPORT.txt','FULL_DRY_RUN_449_REPORT.txt','FULL_SKILL_MATRIX_360_REPORT.txt','RUNTIME_UAT_REGRESSION_12_REPORT.txt','SEMANTIC_ORACLE_REGRESSION_20_REPORT.txt','SYSTEM_WIDE_QUALITY_REGRESSION_30_REPORT.txt','SCALE_LINE_INTEGRITY_REGRESSION_40_REPORT.txt','INSTRUMENT_REVIEW_SPEEDOMETER_REGRESSION_60_REPORT.txt','PROTRACTOR_SCALE_SAFETY_REGRESSION_24_REPORT.txt','METROLOGY_FULL_AUDIT_REGRESSION_80_REPORT.txt']
    for name,r in zip(report_names,results): (guide/name).write_text(r.stdout,encoding='utf-8')

    manifest=[]
    for p in sorted(PACKAGE_DIR.rglob('*')):
        if p.is_file(): manifest.append({'path':str(p.relative_to(PACKAGE_DIR)),'bytes':p.stat().st_size,'sha256':sha256(p)})
    (PACKAGE_DIR/'BUNDLE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    with zipfile.ZipFile(ZIP_PATH,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(PACKAGE_DIR.rglob('*')):
            if p.is_file(): z.write(p,arcname=str(PACKAGE_DIR.name/p.relative_to(PACKAGE_DIR)))
    with zipfile.ZipFile(ZIP_PATH,'r') as z:
        bad=z.testzip()
        if bad: raise RuntimeError(f'ZIP integrity failure: {bad}')

    for r in results: print(r.stdout.strip())
    print('COMBINED DRY-RUN: 1075/1075 PASS')
    print('PACKAGE BUILD: PASS')
    print('Knowledge files: 10')
    print(f'ZIP: {ZIP_PATH}')
    print(f'ZIP SHA256: {sha256(ZIP_PATH)}')
    return 0

if __name__=='__main__': raise SystemExit(main())
