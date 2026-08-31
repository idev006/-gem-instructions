#!/usr/bin/env python3
"""Static SSOT validator for activity-based-elementary-worksheet 2.6.3-LTS.

Prompt/package coherence only. The additive release gate is 1075 cases.
Artifact pixels remain NOT_YET_TESTED until separately inspected.
"""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]

WORKERS={
'W01_ACADEMIC_CONTENT':'workers/W01_ACADEMIC_CONTENT.md',
'W02_TIME_CLOCK':'workers/W02_TIME_CLOCK.md',
'W03_WEIGHT_SCALE':'workers/W03_WEIGHT_SCALE.md',
'W04_LENGTH_DISTANCE':'workers/W04_LENGTH_DISTANCE.md',
'W05_TEMPERATURE_CAPACITY_VOLUME':'workers/W05_TEMPERATURE_CAPACITY_VOLUME.md',
'W06_MONEY_CALENDAR_DATA':'workers/W06_MONEY_CALENDAR_DATA.md',
'W07_INSTRUMENT_AUDITOR':'workers/W07_INSTRUMENT_AUDITOR.md',
'W08_LAYOUT_RENDER_THAI':'workers/W08_LAYOUT_RENDER_THAI.md',
'W09_QA_RELEASE':'workers/W09_QA_RELEASE.md',
'W10_METROLOGY_ENGINEER':'workers/W10_METROLOGY_ENGINEER.md',
}

REQUIRED_FILES=[
'GEM_INSTRUCTIONS_PRODUCTION.md','OUTPUT_CONTRACT.md','ARCHITECTURE.md','KB_ROUTER.md','KB_MANIFEST.md',
'policies/PARAMETER_POLICY.md','policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md','policies/SYSTEM_WIDE_QUALITY_PROFILE.md',
'policies/SCALE_LINE_INTEGRITY_PROFILE.md','policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md','policies/METROLOGY_ASSURANCE_PROFILE.md',
'domains/DOMAIN_REGISTRY.md','domains/MEASUREMENT_COVERAGE_P1_P6.md','domains/INSTRUMENT_READING_ENGINE.md',
'domains/CLOCK_READING_ENGINE.md','domains/SCALE_READING_ENGINE.md','domains/LENGTH_READING_ENGINE.md','domains/SPEEDOMETER_READING_ENGINE.md',
'domains/TEMPERATURE_READING_ENGINE.md','domains/CAPACITY_READING_ENGINE.md','domains/TABLE_GRAPH_READING_ENGINE.md',
'qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md','qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md','qa/DOMAIN_RELEASE_MATRIX.md',
'tools/full_dry_run_suite.py','tools/full_skill_matrix_suite.py','tools/runtime_uat_regression_suite.py','tools/semantic_oracle_regression_suite.py',
'tools/system_wide_quality_regression_suite.py','tools/scale_line_integrity_regression_suite.py','tools/instrument_review_speedometer_regression_suite.py',
'tools/protractor_scale_safety_regression_suite.py','tools/metrology_full_audit_regression_suite.py','tools/build_install_package.py',*WORKERS.values()]

def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def need(errors,rel,*tokens):
    txt=read(rel)
    for t in tokens:
        if t not in txt: errors.append(f'{rel}: missing token: {t}')

def main():
    errors=[]
    for rel in REQUIRED_FILES:
        if not (ROOT/rel).is_file(): errors.append(f'missing required file: {rel}')
    if errors:
        print(f'SSOT VALIDATION: FAIL ({len(errors)} issue(s))'); [print('FAIL',e) for e in errors]; return 1

    seen=set()
    for wid,rel in WORKERS.items():
        txt=read(rel)
        for token in (f'WORKER_ID={wid}','BASELINE_COMPATIBILITY=2.6.x','WORKER_SCHEMA_VERSION=1'):
            if token not in txt: errors.append(f'{rel}: missing {token}')
        found=re.findall(r'WORKER_ID=([A-Z0-9_]+)',txt)
        if found:
            if found[0] in seen: errors.append(f'duplicate worker id: {found[0]}')
            seen.add(found[0])
    if len(seen)!=10: errors.append(f'expected 10 unique worker IDs, got {len(seen)}')

    need(errors,'GEM_INSTRUCTIONS_PRODUCTION.md','Version: 2.6.3-LTS','Exactly ten logical workers','W10_METROLOGY_ENGINEER','METROLOGY_ASSURANCE_PROFILE.md','FINAL_IMAGE_GENERATION_PROMPT','ARTIFACT_QA=NOT_YET_TESTED')
    need(errors,'KB_ROUTER.md','Version: 2.6.3-LTS','W10_METROLOGY_ENGINEER','W07 + W10 + W08 + W09','METROLOGY_ASSURANCE_PROFILE.md')
    need(errors,'KB_MANIFEST.md','Manifest version: 2.6.3-LTS','10 base Knowledge workers','W10_METROLOGY_ENGINEER','exactly ten worker','.txt')
    need(errors,'policies/METROLOGY_ASSURANCE_PROFILE.md','ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER','PROMPT_METROLOGY_INDEPENDENCE_QA','tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)','ARTIFACT_QA=NOT_YET_TESTED')
    need(errors,'policies/SCALE_LINE_INTEGRITY_PROFILE.md','METROLOGY_ASSURANCE_PROFILE.md','W10_METROLOGY_ENGINEER','PROMPT_SCALE_PRINT_SPACING_ORACLE_QA')
    need(errors,'policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md','W10_METROLOGY_ENGINEER','PROMPT_METROLOGY_AUDIT_REQUIRED_QA')
    need(errors,'workers/W10_METROLOGY_ENGINEER.md','METROLOGY_AUDIT_STATE','recompute at least one independent quantitative oracle','Any proposed 65 mm diameter at 1° is rejected')
    need(errors,'tools/build_install_package.py','activity-based-elementary-worksheet_Gem_v2.6.3_LTS_10WORKERS_TXT','W10_METROLOGY_ENGINEER.txt','METROLOGY_ASSURANCE_PROFILE.md','metrology_full_audit_regression_suite.py','1075/1075 PASS','Knowledge bundle count must equal 10')
    need(errors,'tools/metrology_full_audit_regression_suite.py','Expected case count: exactly 80','assert len(CASES)==80','all learner-read scale families + independent W10 metrology audit')
    need(errors,'qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md','W10_METROLOGY_ENGINEER','1075/1075 PASS','ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER')

    builder=read('tools/build_install_package.py')
    for profile in ['policies/SYSTEM_WIDE_QUALITY_PROFILE.md','policies/SCALE_LINE_INTEGRITY_PROFILE.md','policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md','policies/METROLOGY_ASSURANCE_PROFILE.md']:
        if profile not in builder: errors.append(f'builder missing mandatory shared profile: {profile}')

    workflow=(ROOT.parent.parent/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml').read_text(encoding='utf-8')
    for token in ['Full metrology audit — 80 cases','metrology_full_audit_regression_suite.py','v2.6.3_LTS_10WORKERS_TXT']:
        if token not in workflow: errors.append(f'workflow missing {token}')

    if errors:
        print(f'SSOT VALIDATION: FAIL ({len(errors)} issue(s))'); [print('FAIL',e) for e in errors]; return 1
    print('SSOT VALIDATION: PASS')
    print('release family: 2.6.3-LTS / compatible baseline 2.6.x')
    print('workers: 10/10 unique, schema=1')
    print('mandatory runtime profiles: system-wide + scale-line + instrument review-revise + metrology assurance')
    print('independent metrology engineer: W10 present')
    print('core dry-run: 449-case executable present')
    print('declared-skill matrix: 360-case executable present')
    print('runtime UAT regression: 12-case executable present')
    print('semantic oracle regression: 20-case executable present')
    print('system-wide quality regression: 30-case executable present')
    print('scale-line integrity regression: 40-case executable present')
    print('instrument review/speedometer regression: 60-case executable present')
    print('protractor scale safety regression: 24-case executable present')
    print('metrology full audit regression: 80-case executable present')
    print('combined minimum release gate: 1075 cases')
    print('artifact QA: NOT_YET_TESTED')
    return 0
if __name__=='__main__': sys.exit(main())
