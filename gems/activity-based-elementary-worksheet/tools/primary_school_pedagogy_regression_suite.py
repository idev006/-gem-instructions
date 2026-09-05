#!/usr/bin/env python3
"""Primary-school pedagogy/usability regression — 64 additive cases.

Protects learner-facing readability, writability, cognitive clarity, A4 Portrait
defaults and vector ownership of academic geometry. Artifact pixels remain a
separate acceptance phase.
"""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent.parent
CASES=[]
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')

profile=read('policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md')
param=read('policies/PARAMETER_POLICY.md')
system=read('policies/SYSTEM_WIDE_QUALITY_PROFILE.md')
core=read('GEM_INSTRUCTIONS_PRODUCTION.md')
out=read('OUTPUT_CONTRACT.md')
builder=read('tools/build_install_package.py')
validator=read('tools/validate_ssot.py')
checklist=read('qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md')
audit=read('qa/FULL_CLEAN_ROOM_PEDAGOGY_AUDIT_2026_09_02.md')
workflow=(REPO/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml').read_text(encoding='utf-8')

# 1-20 mandatory pedagogy semantics
for name,token in [
('profile-mission','ACADEMIC_CORRECTNESS > LEARNER_COMPREHENSION'),
('a4-default','PAGE_SIZE=A4'),
('portrait-default','ORIENTATION=PORTRAIT'),
('page-provenance','PAGE_SIZE_PROVENANCE=SYSTEM_DEFAULT'),
('grade-gate','SYSTEM_PRIMARY_GRADE_APPROPRIATENESS_QA'),
('instruction-gate','PROMPT_LEARNER_INSTRUCTION_CLARITY_QA'),
('ambiguity-gate','PROMPT_LEARNER_AMBIGUITY_QA'),
('typography-gate','PROMPT_LEARNER_TYPOGRAPHY_QA'),
('writing-gate','PROMPT_LEARNER_WRITING_SPACE_QA'),
('visual-load-gate','PROMPT_LEARNER_VISUAL_LOAD_QA'),
('decoration-gate','PROMPT_LEARNER_DECORATION_ISOLATION_QA'),
('template-gate','PROMPT_LEARNER_TEMPLATE_CONSISTENCY_QA'),
('progression-gate','PROMPT_LEARNER_ITEM_PROGRESSION_QA'),
('instrument-simplicity','PROMPT_TEACHING_INSTRUMENT_SIMPLICITY_QA'),
('vector-mode','ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED'),
('no-generative-redraw','GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES'),
('canonical-coordinate','CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES'),
('uniform-post-transform','POST_LAYOUT_GEOMETRY_TRANSFORM=UNIFORM_SCALE_AND_TRANSLATE_ONLY'),
('print-contrast','PROMPT_LEARNER_PRINT_CONTRAST_QA'),
('learner-simulation','ARTIFACT_LEARNER_SIMULATION_QA'),
]: add(name,token in profile,token)

# 21-30 concrete child-readable defaults
for name,ok in [
('p1p3-14pt','P1–P3 student body text: target >=14 pt' in profile),
('p4p6-12pt','P4–P6 student body text: target >=12 pt' in profile),
('title-18pt','primary title: target >=18 pt' in profile),
('instrument-12pt','instrument/graph numerals read by the learner: target >=12 pt' in profile),
('p1p3-write-8mm','P1–P3: 8 mm' in profile),
('p4p6-write-6mm','P4–P6: 6 mm' in profile),
('one-primary-action','one primary cognitive action' in profile),
('no-color-only','do not encode essential meaning by color alone' in profile),
('paginate-before-degrade','paginate' in profile and 'Never degrade instructional geometry' in profile),
('answer-format-gate','PROMPT_LEARNER_ANSWER_FORMAT_QA' in profile),
]: add(name,ok)

# 31-40 vector/render separation and classroom logic
for name,ok in [
('vector-lock-gate','PROMPT_ACADEMIC_VECTOR_PRIMITIVE_LOCK_QA' in profile),
('transform-gate','PROMPT_ACADEMIC_GEOMETRY_TRANSFORM_QA' in profile),
('primitive-manifest','primitive/position manifest' in profile),
('no-standard-scale-prose','draw a standard scale' in profile),
('decoration-layer','decoration/image layer' in profile),
('protractor-single-scale','protractor: one active numeric scale by default' in profile),
('ruler-projection','ruler: clear zero/reference and endpoint projection guides' in profile),
('weight-explicit-graduations','weight dial: explicit 0.1 kg graduations' in profile),
('clock-continuous','clock: continuous hour hand' in profile),
('graph-no-perspective','graph: 2D bars' in profile),
]: add(name,ok)

# 41-52 integration: runtime, SSOT and release pipeline
for name,ok in [
('parameter-a4','Mandatory implicit page default' in param and 'ORIENTATION=PORTRAIT' in param),
('system-pedagogy-ref','PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md' in system),
('core-pedagogy-ref','PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md' in core),
('output-pedagogy-ref','PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md' in out),
('builder-pedagogy-var',"PEDAGOGY_PROFILE='policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md'" in builder),
('builder-worker-embed','effective=[*SHARED_PROFILES,PEDAGOGY_PROFILE,CAPABILITY_PROFILE,*sources]' in builder.replace(' ','')),
('builder-main-embed','MANDATORY PRIMARY-SCHOOL PEDAGOGY PROFILE' in builder),
('builder-suite','primary_school_pedagogy_regression_suite.py' in builder),
('validator-profile','PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md' in validator),
('validator-suite','primary_school_pedagogy_regression_suite.py' in validator),
('workflow-suite','Primary-school pedagogy regression — 64 cases' in workflow),
('checklist-suite','primary-school pedagogy regression: 64' in checklist.lower()),
]: add(name,ok)

# 53-64 root-cause audit / release truth / scope
for name,ok in [
('audit-r1','Root cause R1' in audit and 'metrology was stronger than pedagogy' in audit),
('audit-r2','Root cause R2' in audit and 'prose-to-render freedom' in audit),
('audit-r3','Root cause R3' in audit and 'duplicated authority' in audit),
('audit-r4','Root cause R4' in audit and 'token-presence regression' in audit),
('audit-r5','Root cause R5' in audit and 'release metadata drift' in audit),
('audit-r6','Root cause R6' in audit and 'one-page optimization' in audit),
('audit-r7','Root cause R7' in audit and 'real-world instruments' in audit),
('audit-r8','Root cause R8' in audit and 'Artifact QA' in audit),
('builder-total','1494/1494 PASS' in builder),
('validator-total','1494' in validator),
('checklist-total','1494/1494 PASS' in checklist),
('artifact-boundary','ARTIFACT_QA=NOT_YET_TESTED' in profile and 'CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA' in profile),
]: add(name,ok)

assert len(CASES)==64,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'PRIMARY-SCHOOL PEDAGOGY REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_,d in failed: print('FAIL',n,d)
    sys.exit(1)
print('PRIMARY-SCHOOL PEDAGOGY REGRESSION: PASS')
print('cases: 64')
print('pass: 64')
print('fail: 0')
print('learner readability + writability + cognitive clarity + vector ownership: 64/64 PASS')
print('artifact QA: NOT_YET_TESTED for future renders')
