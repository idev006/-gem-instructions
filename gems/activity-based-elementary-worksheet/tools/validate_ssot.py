#!/usr/bin/env python3
"""Static SSOT validator for activity-based-elementary-worksheet 2.6.3-LTS.

Prompt/package coherence only. Effective additive release gate: 1494 cases.
Artifact pixels remain NOT_YET_TESTED until separately inspected.
"""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]; REPO=ROOT.parent.parent
WORKERS={'W01_ACADEMIC_CONTENT':'workers/W01_ACADEMIC_CONTENT.md','W02_TIME_CLOCK':'workers/W02_TIME_CLOCK.md','W03_WEIGHT_SCALE':'workers/W03_WEIGHT_SCALE.md','W04_LENGTH_DISTANCE':'workers/W04_LENGTH_DISTANCE.md','W05_TEMPERATURE_CAPACITY_VOLUME':'workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','W06_MONEY_CALENDAR_DATA':'workers/W06_MONEY_CALENDAR_DATA.md','W07_INSTRUMENT_AUDITOR':'workers/W07_INSTRUMENT_AUDITOR.md','W08_LAYOUT_RENDER_THAI':'workers/W08_LAYOUT_RENDER_THAI.md','W09_QA_RELEASE':'workers/W09_QA_RELEASE.md','W10_METROLOGY_ENGINEER':'workers/W10_METROLOGY_ENGINEER.md'}
SUITES=[('tools/full_dry_run_suite.py','449'),('tools/full_skill_matrix_suite.py','360'),('tools/runtime_uat_regression_suite.py','12'),('tools/semantic_oracle_regression_suite.py','20'),('tools/system_wide_quality_regression_suite.py','30'),('tools/scale_line_integrity_regression_suite.py','40'),('tools/instrument_review_speedometer_regression_suite.py','60'),('tools/protractor_scale_safety_regression_suite.py','24'),('tools/metrology_full_audit_regression_suite.py','80'),('tools/weight_dial_inactive_gap_regression_suite.py','32'),('tools/physical_page_feasibility_regression_suite.py','48'),('tools/instrument_geometry_artifact_regression_suite.py','64'),('tools/measurement_reference_artifact_regression_suite.py','66'),('tools/clock_hand_endpoint_regression_suite.py','32'),('tools/weight_dial_visible_subdivision_regression_suite.py','32'),('tools/primary_school_pedagogy_regression_suite.py','64'),('tools/repository_full_line_audit_suite.py','81')]
REQUIRED_FILES=['GEM_INSTRUCTIONS_PRODUCTION.md','OUTPUT_CONTRACT.md','ARCHITECTURE.md','KB_ROUTER.md','KB_MANIFEST.md','README.md','USER_GUIDE.md','GEM_INSTALLATION_GUIDE.md','policies/PARAMETER_POLICY.md','policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md','policies/SYSTEM_WIDE_QUALITY_PROFILE.md','policies/SCALE_LINE_INTEGRITY_PROFILE.md','policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md','policies/METROLOGY_ASSURANCE_PROFILE.md','policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md','policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md','policies/CAPABILITY_QUALITY_GATE.md','policies/WEIGHT_DIAL_VISIBLE_TICK_SET_PROFILE.md','domains/DOMAIN_REGISTRY.md','domains/MEASUREMENT_COVERAGE_P1_P6.md','domains/INSTRUMENT_READING_ENGINE.md','domains/CLOCK_READING_ENGINE.md','domains/SCALE_READING_ENGINE.md','domains/LENGTH_READING_ENGINE.md','domains/SPEEDOMETER_READING_ENGINE.md','domains/TEMPERATURE_READING_ENGINE.md','domains/CAPACITY_READING_ENGINE.md','domains/TABLE_GRAPH_READING_ENGINE.md','qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md','qa/ACTUAL_WEIGHT_DIAL_INACTIVE_GAP_REGRESSION_2026_08_31.md','qa/CONSOLIDATED_PHYSICAL_PAGE_FEASIBILITY_REGRESSION_2026_08_31.md','qa/ACTUAL_INSTRUMENT_GEOMETRY_DEFECTS_2026_08_31.md','qa/ACTUAL_MEASUREMENT_REFERENCE_DEFECTS_2026_08_31.md','qa/ACTUAL_CLOCK_HAND_ENDPOINT_REGRESSION_2026_09_01.md','qa/ACTUAL_WEIGHT_DIAL_VISIBLE_SUBDIVISION_REGRESSION_2026_09_01.md','qa/FULL_CLEAN_ROOM_PEDAGOGY_AUDIT_2026_09_02.md','qa/CAPABILITY_QUALITY_ITERATION_REPORT_2026_09_05.md','qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md','qa/DOMAIN_RELEASE_MATRIX.md','tools/build_install_package.py','tools/capability_quality_scorecard.py',*[x[0] for x in SUITES],*WORKERS.values()]
SKILL_METRIC_REQUIRED=["skill-metrics/SKILL_METRIC_STANDARD.md","skill-metrics/CRITICAL_DEFECT_POLICY.md","skill-metrics/ARTIFACT_QUALIFICATION_PROTOCOL.md","skill-metrics/SKILL_SCORE_REGISTRY.md","skill-metrics/ACADEMIC_ARITHMETIC_THAI_SKILL_METRICS.md","skill-metrics/TIME_CALCULATION_SKILL_METRICS.md","skill-metrics/ANALOG_CLOCK_SKILL_METRICS.md","skill-metrics/WEIGHT_SCALE_SKILL_METRICS.md","skill-metrics/RULER_LENGTH_SKILL_METRICS.md","skill-metrics/DISTANCE_SKILL_METRICS.md","skill-metrics/SPEEDOMETER_SKILL_METRICS.md","skill-metrics/ANGLE_PROTRACTOR_SKILL_METRICS.md","skill-metrics/PERIMETER_AREA_SKILL_METRICS.md","skill-metrics/TEMPERATURE_SKILL_METRICS.md","skill-metrics/CAPACITY_SKILL_METRICS.md","skill-metrics/VOLUME_SKILL_METRICS.md","skill-metrics/MONEY_SKILL_METRICS.md","skill-metrics/CALENDAR_SKILL_METRICS.md","skill-metrics/DATA_READING_SKILL_METRICS.md","tools/skill_metric_pack_regression_suite.py"]
REQUIRED_FILES.extend(SKILL_METRIC_REQUIRED)
def read(rel):return (ROOT/rel).read_text(encoding='utf-8')
def need(errors,rel,*tokens):
    txt=read(rel)
    for t in tokens:
        if t not in txt:errors.append(f'{rel}: missing token: {t}')
def main():
    errors=[]
    for rel in REQUIRED_FILES:
        if not (ROOT/rel).is_file():errors.append(f'missing required file: {rel}')
    workflow=REPO/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml'
    if not workflow.is_file():errors.append('missing GitHub workflow')
    if errors:
        print(f'SSOT VALIDATION: FAIL ({len(errors)} issue(s))');[print('FAIL',e) for e in errors];return 1
    seen=set()
    for wid,rel in WORKERS.items():
        txt=read(rel)
        for token in (f'WORKER_ID={wid}','BASELINE_COMPATIBILITY=2.6.x','WORKER_SCHEMA_VERSION=1'):
            if token not in txt:errors.append(f'{rel}: missing {token}')
        ids=re.findall(r'WORKER_ID=([A-Z0-9_]+)',txt)
        if not ids:errors.append(f'{rel}: worker id not found')
        elif ids[0] in seen:errors.append(f'duplicate worker id: {ids[0]}')
        else:seen.add(ids[0])
    if len(seen)!=10:errors.append(f'expected 10 unique worker IDs, got {len(seen)}')
    need(errors,'GEM_INSTRUCTIONS_PRODUCTION.md','Version: 2.6.3-LTS','Exactly ten logical workers','PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md','ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED','PROMPT_LEARNER_TYPOGRAPHY_QA','ARTIFACT_QA=NOT_YET_TESTED')
    need(errors,'KB_MANIFEST.md','10 base Knowledge workers','PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md','repository full-line regression')
    need(errors,'policies/PARAMETER_POLICY.md','Mandatory implicit page default','PAGE_SIZE=A4','ORIENTATION=PORTRAIT')
    need(errors,'skill-metrics/SKILL_METRIC_STANDARD.md','PASS_THRESHOLD=95','CRITICAL_ACADEMIC_DEFECT','PAGE_SIZE=A4','ORIENTATION=PORTRAIT')
    need(errors,'skill-metrics/CRITICAL_DEFECT_POLICY.md','CRITICAL_ACADEMIC_DEFECT => ARTIFACT_QA=FAIL => CLASSROOM_RELEASE=BLOCKED')
    need(errors,'skill-metrics/ARTIFACT_QUALIFICATION_PROTOCOL.md','>=10 actual rendered worksheets','ITEM_COUNT_INSPECTED')
    need(errors,'skill-metrics/SKILL_SCORE_REGISTRY.md','ANALOG_CLOCK','WEIGHT_SCALE','RULER_LENGTH','TEMPERATURE','CAPACITY')
    need(errors,'policies/CAPABILITY_QUALITY_GATE.md','OVERALL_CAPABILITY_SCORE >= 95%','EVERY_CAPABILITY_SCORE >= 95%','CAPABILITY_QUALITY_GATE=PASS')
    need(errors,'policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md','SYSTEM_PRIMARY_GRADE_APPROPRIATENESS_QA','PROMPT_LEARNER_TYPOGRAPHY_QA','PROMPT_LEARNER_WRITING_SPACE_QA','ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED','ARTIFACT_LEARNER_SIMULATION_QA')
    need(errors,'workers/W02_TIME_CLOCK.md','PROMPT_CLOCK_QUARTER_HOUR_INTERPOLATION_QA','14:45 / 2:45','82.5°')
    need(errors,'domains/SCALE_READING_ENGINE.md','LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}','CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]','active_tick_angle(i)=(6*i) mod 360','NEEDLE_PIVOT=DIAL_CENTER','INTERVALS_PER_KG=10','HALF_KG_INTERMEDIATE_OFFSET=0.5')
    need(errors,'workers/W03_WEIGHT_SCALE.md','PROMPT_WEIGHT_PER_KG_SUBDIVISION_QA','PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA','VISIBLE_TICK_OFFSETS_PER_KG')
    need(errors,'policies/WEIGHT_DIAL_VISIBLE_TICK_SET_PROFILE.md','INTERVALS_PER_KG=10','HALF_KG_INTERMEDIATE_INDEX=5','DO NOT simplify, omit, merge, or sparsify')
    need(errors,'domains/LENGTH_READING_ENGINE.md','START_PROJECTION_GUIDE_X','END_PROJECTION_GUIDE_X','OBJECT_START_X == ZERO_GRADUATION_X')
    need(errors,'workers/W04_LENGTH_DISTANCE.md','PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA','PROMPT_RULER_ZERO_START_ALIGNMENT_QA','perfect, undistorted upper semicircle','ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == PROTRACTOR_CENTER','one active numeric scale only by default','PROTRACTOR_BODY_HEIGHT_MM = PROTRACTOR_BODY_WIDTH_MM/2')
    need(errors,'domains/SPEEDOMETER_READING_ENGINE.md','NEEDLE_PIVOT','DIAL_CENTER','READING_RING_CENTER')
    need(errors,'domains/TEMPERATURE_READING_ENGINE.md','exactly 6 major positions','exactly 5 intermediate positions','exactly 40 minor positions','exactly 10 equal intervals','exactly 9 interior graduation positions')
    need(errors,'domains/CAPACITY_READING_ENGINE.md','INTERVALS_PER_100ML=2','INTERIOR_POSITIONS_PER_100ML_SPAN=1','LOCAL_SPAN_RECOUNT_REQUIRED=YES')
    need(errors,'workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','PROMPT_CAPACITY_PER_100ML_SUBDIVISION_QA','PROMPT_CAPACITY_LOCAL_SPAN_RECOUNT_QA','PROMPT_CAPACITY_MAJOR_MINOR_HIERARCHY_QA')
    need(errors,'workers/W07_INSTRUMENT_AUDITOR.md','PROMPT_LOCAL_SPAN_RECOUNT_QA','PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA','INTERVALS_PER_100ML=2','HALF_KG_INTERMEDIATE_OFFSET=0.5')
    need(errors,'workers/W08_LAYOUT_RENDER_THAI.md','PROTRACTOR_BODY_HEIGHT_MM=35','shape-aware','2-column layout is preferred','Never emit `OUTPUT_MODE=DETERMINISTIC_VECTOR`','START_PROJECTION_GUIDE_X','INTERVALS_PER_100ML=2','HALF_KG_INTERMEDIATE_OFFSET=0.5')
    need(errors,'workers/W10_METROLOGY_ENGINEER.md','COMMON_CENTER_CHECK','RADIAL_COLLINEARITY_CHECK','semicircle body height is `R=W/2`','CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]','LOCAL_SPAN_RECOUNT_CHECK','REFERENCE_PROJECTION_CHECK')
    need(errors,'workers/W09_QA_RELEASE.md','PROMPT_SPEEDOMETER_PIVOT_CENTER_QA','PROMPT_DIAL_LABEL_ORDER_QA','PROMPT_THERMOMETER_HIERARCHY_COUNT_QA','PROMPT_PROTRACTOR_SHAPE_INTEGRITY_QA','PROMPT_CLOCK_QUARTER_HOUR_INTERPOLATION_QA','PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA','PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA','PROMPT_CAPACITY_LOCAL_SPAN_RECOUNT_QA')
    need(errors,'qa/ACTUAL_INSTRUMENT_GEOMETRY_DEFECTS_2026_08_31.md','speedometer','thermometer','protractor','weight')
    need(errors,'qa/ACTUAL_MEASUREMENT_REFERENCE_DEFECTS_2026_08_31.md','D1 — Analog clock','D2 — Canonical 0–5 kg','D3 — Ruler','D4 — Graduated container','ARTIFACT_QA=FAIL')
    need(errors,'qa/ACTUAL_CLOCK_HAND_ENDPOINT_REGRESSION_2026_09_01.md','3:30','9:30','ARTIFACT_QA')
    need(errors,'qa/ACTUAL_WEIGHT_DIAL_VISIBLE_SUBDIVISION_REGRESSION_2026_09_01.md','10 intervals','0.5 kg','ARTIFACT_QA')
    need(errors,'qa/FULL_CLEAN_ROOM_PEDAGOGY_AUDIT_2026_09_02.md','Root cause R1','Root cause R8','ARTIFACT_LEARNER_SIMULATION_QA')
    need(errors,'qa/CAPABILITY_QUALITY_ITERATION_REPORT_2026_09_05.md','OVERALL_CAPABILITY_SCORE=100.00%','CAPABILITY_QUALITY_GATE=PASS')
    need(errors,'qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md','1494/1494 PASS','300/300 SCORED CRITERIA PASS','15/15 CAPABILITIES >=95%','clock hand endpoint regression: 32','weight dial visible subdivision regression: 32','primary-school pedagogy regression: 64','repository full-line audit: 81')
    builder=read('tools/build_install_package.py')
    for token in ['activity-based-elementary-worksheet_Gem_v2.6.3_LTS_10WORKERS_TXT','W10_METROLOGY_ENGINEER.txt','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md','PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md','clock_hand_endpoint_regression_suite.py','weight_dial_visible_subdivision_regression_suite.py','primary_school_pedagogy_regression_suite.py','repository_full_line_audit_suite.py','skill_metric_pack_regression_suite.py','SKILL_METRIC_GLOBALS','capability_quality_scorecard.py','CAPABILITY_QUALITY_GATE','1494/1494 PASS','Knowledge bundle count must equal 10','ACTUAL_MEASUREMENT_REFERENCE_DEFECTS_2026_08_31.md','FULL_CLEAN_ROOM_PEDAGOGY_AUDIT_2026_09_02.md']:
        if token not in builder:errors.append(f'builder missing token: {token}')
    for rel,marker in SUITES:
        if marker not in read(rel):errors.append(f'{rel}: case marker missing: {marker}')
    wtxt=workflow.read_text(encoding='utf-8')
    for token in ['Full metrology audit — 80 cases','Actual weight-dial inactive-gap regression — 32 cases','Physical page feasibility regression — 48 cases','Actual instrument geometry regression — 64 cases','Measurement reference artifact regression — 66 cases','Clock hand endpoint regression — 32 cases','Weight dial visible subdivision regression — 32 cases','Primary-school pedagogy regression — 64 cases','Repository full-line audit — 81 semantic cases','clock_hand_endpoint_regression_suite.py','weight_dial_visible_subdivision_regression_suite.py','primary_school_pedagogy_regression_suite.py','repository_full_line_audit_suite.py','Skill metric pack governance — 161 cases','skill_metric_pack_regression_suite.py','Capability quality scorecard — every capability >=95%','capability_quality_scorecard.py','v2.6.3_LTS_10WORKERS_TXT']:
        if token not in wtxt:errors.append(f'workflow missing {token}')
    current='\n'.join(read(x) for x in ['GEM_INSTRUCTIONS_PRODUCTION.md','domains/SCALE_READING_ENGINE.md','domains/LENGTH_READING_ENGINE.md','domains/CAPACITY_READING_ENGINE.md','workers/W02_TIME_CLOCK.md','workers/W03_WEIGHT_SCALE.md','workers/W04_LENGTH_DISTANCE.md','workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','workers/W07_INSTRUMENT_AUDITOR.md','workers/W08_LAYOUT_RENDER_THAI.md','workers/W09_QA_RELEASE.md','workers/W10_METROLOGY_ENGINEER.md','policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md','policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md','qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md'])
    for stale in ['LABEL_ANGLES={0:240°,1:300°,2:0°,3:60°,4:120°,5:180°}','active_tick_angle(i)=(240+6*i)','five rows of 70 mm protractors require at least 350 mm']:
        if stale in current:errors.append(f'stale canonical statement remains: {stale}')
    if errors:
        print(f'SSOT VALIDATION: FAIL ({len(errors)} issue(s))');[print('FAIL',e) for e in errors];return 1
    print('SSOT VALIDATION: PASS');print('release family: 2.6.3-LTS / compatible baseline 2.6.x');print('workers: 10/10 unique, schema=1');print('mandatory technical runtime profiles: 5');print('mandatory primary-school pedagogy profile: present');print('clock endpoint regression: 32-case executable present');print('weight visible subdivision regression: 32-case executable present');print('primary-school pedagogy regression: 64-case executable present');print('repository full-line audit: 81-case executable present');print('skill metric packs: 15/15 + 161-case governance suite present');print('capability quality scorecard: 300 criteria / 15 capabilities present');print('effective regression gate: 1494 cases + mandatory capability score gate');print('artifact QA: NOT_YET_TESTED');return 0
if __name__=='__main__':sys.exit(main())
