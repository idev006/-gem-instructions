#!/usr/bin/env python3
"""Repository-wide every-line audit for the worksheet Gem.

This gate reads every text/code line under the Gem SSOT plus its GitHub workflow,
then runs 81 semantic/coherence assertions. It is additive and does not replace
any domain regression suite.

Expected semantic case count: exactly 81.
"""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent.parent
TEXT_SUFFIXES={'.md','.py','.yml','.yaml','.json','.txt'}
EXCLUDE_PARTS={'dist','__pycache__','.pytest_cache'}
CASES=[]
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')

# Every-line physical scan.
files=[]; line_count=0; byte_count=0; line_errors=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES: continue
    if any(part in EXCLUDE_PARTS for part in p.parts): continue
    files.append(p)
workflow=REPO/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml'
if workflow.is_file(): files.append(workflow)
for p in files:
    try: text=p.read_text(encoding='utf-8')
    except UnicodeDecodeError as e:
        line_errors.append(f'{p}: utf8 decode failure {e}'); continue
    byte_count+=len(text.encode('utf-8'))
    for n,line in enumerate(text.splitlines(),1):
        line_count+=1
        if '\x00' in line: line_errors.append(f'{p}:{n}: NUL')
        if '\ufffd' in line: line_errors.append(f'{p}:{n}: replacement char')
        if line.startswith('<<<<<<<') or line.startswith('=======') or line.startswith('>>>>>>>'):
            line_errors.append(f'{p}:{n}: merge-conflict marker')
        bad=[c for c in line if ord(c)<32 and c not in '\t']
        if bad: line_errors.append(f'{p}:{n}: control character')
add('all-files-readable',not line_errors,'; '.join(line_errors[:10]))
add('nontrivial-file-count',len(files)>=40,f'files={len(files)}')
add('nontrivial-line-count',line_count>=4000,f'lines={line_count}')
add('nontrivial-byte-count',byte_count>=200000,f'bytes={byte_count}')

# Files required for current architecture. New defect/suite presence is enforced by
# validate_ssot and release-integrity cases below so the 81-case baseline stays additive/stable.
required=[
'GEM_INSTRUCTIONS_PRODUCTION.md','ARCHITECTURE.md','OUTPUT_CONTRACT.md','KB_ROUTER.md','KB_MANIFEST.md','README.md','USER_GUIDE.md','GEM_INSTALLATION_GUIDE.md',
'policies/SYSTEM_WIDE_QUALITY_PROFILE.md','policies/SCALE_LINE_INTEGRITY_PROFILE.md','policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md','policies/METROLOGY_ASSURANCE_PROFILE.md','policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md',
'domains/INSTRUMENT_READING_ENGINE.md','domains/SCALE_READING_ENGINE.md','domains/SPEEDOMETER_READING_ENGINE.md','domains/TEMPERATURE_READING_ENGINE.md',
'workers/W03_WEIGHT_SCALE.md','workers/W04_LENGTH_DISTANCE.md','workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','workers/W07_INSTRUMENT_AUDITOR.md','workers/W08_LAYOUT_RENDER_THAI.md','workers/W09_QA_RELEASE.md','workers/W10_METROLOGY_ENGINEER.md',
'qa/ACTUAL_INSTRUMENT_GEOMETRY_DEFECTS_2026_08_31.md','qa/ACTUAL_WEIGHT_DIAL_INACTIVE_GAP_REGRESSION_2026_08_31.md','qa/CONSOLIDATED_PHYSICAL_PAGE_FEASIBILITY_REGRESSION_2026_08_31.md',
'tools/instrument_geometry_artifact_regression_suite.py','tools/repository_full_line_audit_suite.py']
for i,rel in enumerate(required): add(f'required-{i}',(ROOT/rel).is_file(),rel)

# Aggregate current authoritative text for stale-contract scans.
current_paths=[
'GEM_INSTRUCTIONS_PRODUCTION.md','ARCHITECTURE.md','OUTPUT_CONTRACT.md','KB_ROUTER.md','KB_MANIFEST.md','README.md','USER_GUIDE.md','GEM_INSTALLATION_GUIDE.md',
'workers/W02_TIME_CLOCK.md','workers/W03_WEIGHT_SCALE.md','workers/W04_LENGTH_DISTANCE.md','workers/W05_TEMPERATURE_CAPACITY_VOLUME.md','workers/W07_INSTRUMENT_AUDITOR.md','workers/W08_LAYOUT_RENDER_THAI.md','workers/W09_QA_RELEASE.md','workers/W10_METROLOGY_ENGINEER.md',
'policies/SCALE_LINE_INTEGRITY_PROFILE.md','policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md','policies/METROLOGY_ASSURANCE_PROFILE.md','policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md',
'domains/INSTRUMENT_READING_ENGINE.md','domains/CLOCK_READING_ENGINE.md','domains/SCALE_READING_ENGINE.md','domains/LENGTH_READING_ENGINE.md','domains/SPEEDOMETER_READING_ENGINE.md','domains/TEMPERATURE_READING_ENGINE.md','domains/CAPACITY_READING_ENGINE.md']
auth='\n'.join(read(p) for p in current_paths).lower()

# Stale/unsafe authoritative phrases must be gone.
for name,needle in [
('no-nine-workers','nine specialist workers'),
('no-knowledge-9','knowledge 9'),
('no-slot10-reserved','slot 10 is intentionally reserved'),
('no-old-weight-label-map','label_angles={0:240°'),
('no-old-weight-formula','active_tick_angle(i)=(240+6*i)'),
('no-protractor-width-as-height','five rows of 70 mm protractors require at least 350 mm'),
('no-four-mandatory-profiles','four mandatory shared profiles'),
]: add(name,needle not in auth,needle)

# OUTPUT_MODE vs RENDER_PATH is context-sensitive: a forbidden example is allowed only
# when the same line explicitly marks it as invalid/prohibited. Positive misuse is not.
bad_output_mode_lines=[]
negative_markers=('never','invalid','forbidden','must not','do not','not ','category error','reject','wrong','≠')
for rel in current_paths:
    for line_no,line in enumerate(read(rel).splitlines(),1):
        low=line.lower()
        if 'output_mode=deterministic_vector' in low and not any(m in low for m in negative_markers):
            bad_output_mode_lines.append(f'{rel}:{line_no}:{line.strip()}')
add('no-output-mode-render-path-confusion',not bad_output_mode_lines,'; '.join(bad_output_mode_lines[:5]))

# Positive cross-file invariants.
core=read('GEM_INSTRUCTIONS_PRODUCTION.md'); arch=read('ARCHITECTURE.md'); out=read('OUTPUT_CONTRACT.md')
manifest=read('KB_MANIFEST.md'); router=read('KB_ROUTER.md'); install=read('GEM_INSTALLATION_GUIDE.md')
readme=read('README.md'); guide=read('USER_GUIDE.md')
w09=read('workers/W09_QA_RELEASE.md'); w10=read('workers/W10_METROLOGY_ENGINEER.md')
scale=read('domains/SCALE_READING_ENGINE.md'); speed=read('domains/SPEEDOMETER_READING_ENGINE.md'); temp=read('domains/TEMPERATURE_READING_ENGINE.md')
w04=read('workers/W04_LENGTH_DISTANCE.md'); phys=read('policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md')
positives=[
('core-ten','Exactly ten logical workers' in core),
('core-physical-profile','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in core),
('arch-ten','ten logical Specialist Workers' in arch),
('arch-physical-profile','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in arch),
('out-five-profiles','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in out),
('manifest-five','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in manifest and 'five mandatory' in manifest.lower()),
('router-physical','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in router),
('install-ten','W10_METROLOGY_ENGINEER' in install and '10' in install),
('install-five','PHYSICAL_PAGE_FEASIBILITY_PROFILE' in install or 'physical page' in install.lower()),
('readme-current','Version: 2.6.3-LTS' in readme and 'W10_METROLOGY_ENGINEER' in readme),
('guide-current','Version: 2.6.3-LTS' in guide and 'W10' in guide),
('w09-physical','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in w09),
('w09-common-center','PROMPT_METROLOGY_COMMON_CENTER_QA' in w09),
('w10-weight-order','CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]' in w10),
('weight-top-zero','LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}' in scale),
('speed-common-center','NEEDLE_PIVOT=DIAL_CENTER' in speed),
('thermo-hierarchy','6 major' in temp and '5 intermediate' in temp and '40 minor' in temp),
('protractor-perfect','perfect' in w04.lower() and 'undistorted upper semicircle' in w04.lower() and 'every graduation is radial from the same center' in w04.lower()),
('protractor-body-height','PROTRACTOR_BODY_HEIGHT_MM = PROTRACTOR_BODY_WIDTH_MM/2' in w04),
('physical-shape-aware','PROMPT_SHAPE_AWARE_BOUNDING_BOX_QA' in phys),
]
for n,o in positives:add(n,o)

# Worker contract structural checks: all ten IDs, required sections.
workers=['W01_ACADEMIC_CONTENT','W02_TIME_CLOCK','W03_WEIGHT_SCALE','W04_LENGTH_DISTANCE','W05_TEMPERATURE_CAPACITY_VOLUME','W06_MONEY_CALENDAR_DATA','W07_INSTRUMENT_AUDITOR','W08_LAYOUT_RENDER_THAI','W09_QA_RELEASE','W10_METROLOGY_ENGINEER']
for wid in workers:
    txt=read(f'workers/{wid}.md')
    add(f'worker-{wid}',all(t in txt for t in [f'WORKER_ID={wid}','BASELINE_COMPATIBILITY=2.6.x','WORKER_SCHEMA_VERSION=1','## ACCEPTS','## OWNS','## RETURNS','## MUST_NOT_DECIDE']))

# 4 physical scan + 29 required + 8 stale + 20 positive + 10 workers = 71.
# Add 10 release-integrity cases => 81.
builder=read('tools/build_install_package.py'); validator=read('tools/validate_ssot.py'); checklist=read('qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md')
workflow_text=workflow.read_text(encoding='utf-8')
release_checks=[
('builder-geometry64','instrument_geometry_artifact_regression_suite.py' in builder and 'measurement_reference_artifact_regression_suite.py' in builder),
('builder-line81','repository_full_line_audit_suite.py' in builder),
('validator-geometry64','instrument_geometry_artifact_regression_suite.py' in validator and 'measurement_reference_artifact_regression_suite.py' in validator),
('validator-line81','repository_full_line_audit_suite.py' in validator),
('workflow-geometry64','Actual instrument geometry regression — 64 cases' in workflow_text and 'Measurement reference artifact regression — 64 cases' in workflow_text),
('workflow-line81','Repository full-line audit — 81 semantic cases' in workflow_text),
('checklist-geometry64','actual instrument geometry regression: 64' in checklist.lower() and 'measurement reference artifact regression: 64' in checklist.lower()),
('checklist-line81','repository full-line audit: 81' in checklist.lower()),
('release-total-1364',all('1364/1364 PASS' in x for x in [builder,checklist,install,readme])),
('five-profile-packaging','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in builder and 'Mandatory shared profiles: 5' in builder),
]
for n,o in release_checks:add(n,o)

assert len(CASES)==81,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed or line_errors:
    print(f'REPOSITORY FULL LINE AUDIT: FAIL ({len(failed)} semantic failures, {len(line_errors)} line errors)')
    for n,_,d in failed: print('FAIL',n,d)
    for e in line_errors[:20]: print('LINE_FAIL',e)
    print(f'files_scanned: {len(files)}')
    print(f'lines_scanned: {line_count}')
    print(f'bytes_scanned: {byte_count}')
    sys.exit(1)
print('REPOSITORY FULL LINE AUDIT: PASS')
print(f'files_scanned: {len(files)}')
print(f'lines_scanned: {line_count}')
print(f'bytes_scanned: {byte_count}')
print('semantic_cases: 81/81 PASS')
print('scope: every UTF-8 text/code line under Gem SSOT + workflow')
print('artifact QA: NOT_YET_TESTED for future renders')
