#!/usr/bin/env python3
"""Full GEM + all-skills clean-room audit regression — exactly 180 cases.

Checks every declared skill plus cross-skill architecture/integration drift.
Prompt/Knowledge gate only. Rendered Artifact QA remains separate.
"""
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent.parent
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
CASES=[]
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))

PACKS={
'ACADEMIC_ARITHMETIC_THAI':('W01_ACADEMIC_CONTENT','skill-metrics/ACADEMIC_ARITHMETIC_THAI_SKILL_METRICS.md'),
'TIME_CALCULATION':('W02_TIME_CLOCK','skill-metrics/TIME_CALCULATION_SKILL_METRICS.md'),
'ANALOG_CLOCK':('W02_TIME_CLOCK','skill-metrics/ANALOG_CLOCK_SKILL_METRICS.md'),
'WEIGHT_SCALE':('W03_WEIGHT_SCALE','skill-metrics/WEIGHT_SCALE_SKILL_METRICS.md'),
'RULER_LENGTH':('W04_LENGTH_DISTANCE','skill-metrics/RULER_LENGTH_SKILL_METRICS.md'),
'DISTANCE':('W04_LENGTH_DISTANCE','skill-metrics/DISTANCE_SKILL_METRICS.md'),
'SPEEDOMETER':('W04_LENGTH_DISTANCE','skill-metrics/SPEEDOMETER_SKILL_METRICS.md'),
'ANGLE_PROTRACTOR':('W04_LENGTH_DISTANCE','skill-metrics/ANGLE_PROTRACTOR_SKILL_METRICS.md'),
'PERIMETER_AREA':('W04_LENGTH_DISTANCE','skill-metrics/PERIMETER_AREA_SKILL_METRICS.md'),
'TEMPERATURE':('W05_TEMPERATURE_CAPACITY_VOLUME','skill-metrics/TEMPERATURE_SKILL_METRICS.md'),
'CAPACITY':('W05_TEMPERATURE_CAPACITY_VOLUME','skill-metrics/CAPACITY_SKILL_METRICS.md'),
'VOLUME':('W05_TEMPERATURE_CAPACITY_VOLUME','skill-metrics/VOLUME_SKILL_METRICS.md'),
'MONEY':('W06_MONEY_CALENDAR_DATA','skill-metrics/MONEY_SKILL_METRICS.md'),
'CALENDAR':('W06_MONEY_CALENDAR_DATA','skill-metrics/CALENDAR_SKILL_METRICS.md'),
'DATA_READING':('W06_MONEY_CALENDAR_DATA','skill-metrics/DATA_READING_SKILL_METRICS.md'),
}

# 120 structural checks: 15 skills x 8
required=['## CANONICAL_ORACLE','## PROMPT_METRICS','## ARTIFACT_METRICS','## CRITICAL_DEFECTS','## REPAIR_PROTOCOL','## RUNTIME_INVARIANT']
for skill,(owner,rel) in PACKS.items():
    txt=read(rel)
    add(f'{skill}-id',f'SKILL_ID={skill}' in txt)
    add(f'{skill}-owner',f'OWNER={owner}' in txt)
    for token in required:
        add(f'{skill}-{token[3:18]}',token in txt)
assert len(CASES)==120,len(CASES)

# 15 routing/owner checks => 135
router=read('KB_ROUTER.md')
for skill,(owner,rel) in PACKS.items():
    add(f'route-{skill}',skill in router and owner.split('_')[0] in router)
assert len(CASES)==135,len(CASES)

# 15 canonical-state checks => 150
for skill,(owner,rel) in PACKS.items():
    txt=read(rel)
    add(f'canonical-state-{skill}','CANONICAL_STATE_REQUIRED=YES' in txt)
assert len(CASES)==150,len(CASES)

# 30 cross-system checks => 180
registry=read('domains/DOMAIN_REGISTRY.md')
output=read('OUTPUT_CONTRACT.md')
runtime=read('policies/ALL_SKILLS_RUNTIME_INVARIANT_PROFILE.md')
clock=read('domains/CLOCK_READING_ENGINE.md')
clock_driver=read('policies/CLOCK_MINUTE_HAND_DRIVEN_HOUR_HAND_POLICY.md')
clock_page=read('policies/THAI_P3_CLOCK_HALF_HOUR_ONE_PAGE_PROFILE.md')
weight=read('skill-metrics/WEIGHT_SCALE_SKILL_METRICS.md')
ruler=read('skill-metrics/RULER_LENGTH_SKILL_METRICS.md')
speed=read('skill-metrics/SPEEDOMETER_SKILL_METRICS.md')
pro=read('skill-metrics/ANGLE_PROTRACTOR_SKILL_METRICS.md')
temp=read('skill-metrics/TEMPERATURE_SKILL_METRICS.md')
cap=read('skill-metrics/CAPACITY_SKILL_METRICS.md')
data=read('skill-metrics/DATA_READING_SKILL_METRICS.md')
w09=read('workers/W09_QA_RELEASE.md')
audit=read('qa/FULL_GEM_ALL_SKILLS_CLEAN_ROOM_AUDIT_2026_09_05.md')
workflow=(REPO/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml').read_text(encoding='utf-8')
builder=read('tools/build_install_package.py')

cross=[
('registry-version','Version: 2.6.3-LTS' in registry),
('registry-w10-route','Required route includes W07 + W10 + W08 + W09.' in registry),
('registry-runtime-profile','ALL_SKILLS_RUNTIME_INVARIANT_PROFILE.md' in registry),
('router-runtime-profile','ALL_SKILLS_RUNTIME_INVARIANT_PROFILE.md' in router),
('output-runtime-profile','ALL_SKILLS_RUNTIME_INVARIANT_PROFILE.md' in output),
('runtime-chain','CANONICAL_STATE -> INDEPENDENT_VERIFY -> STUDENT_VIEW_DERIVATION -> LAYOUT -> RELEASE' in runtime),
('runtime-instrument-chain','OWNER -> W07 -> W10 -> W08 -> W09' in runtime),
('runtime-a4','Default page is A4 Portrait' in runtime),
('runtime-critical','CRITICAL_ACADEMIC_DEFECT=YES' in runtime),
('output-proved-page','FEASIBILITY_CONFIRMED_ONE_PAGE_LAYOUT_REQUIRED=YES' in output),
('clock-minute-driver','minute_hand_angle_deg / 12' in clock),
('clock-driver-policy','MINUTE_HAND_DRIVES_HOUR_HAND_POSITION=YES' in clock_driver),
('clock-page-2x5','GRID_COLUMNS=2' in clock_page and 'GRID_ROWS=5' in clock_page),
('clock-page-width','REQUIRED_GRID_WIDTH_MM=2×91+4=186 <=194' in clock_page),
('clock-page-height','REQUIRED_GRID_HEIGHT_MM=5×43+4×4=231 <=243' in clock_page),
('weight-midpoint','major > 0.5 kg intermediate > ordinary 0.1 kg minor' in weight),
('ruler-zero','Physical border is never silently promoted to a graduation' in ruler),
('speed-hierarchy','20 km/h major hierarchy' in speed),
('protractor-hierarchy','10° major > 5° intermediate > 1° minor' in pro),
('temperature-hierarchy','Major 10°C > intermediate 5°C > minor 1°C' in temp),
('capacity-local','no decorative pseudo-ticks' in cap),
('data-axis','Numeric axes inherit scale/tick integrity' in data),
('w09-minute-driver','PROMPT_CLOCK_MINUTE_HAND_DRIVER_QA' in w09),
('w09-one-page','PROMPT_CLOCK_P3_HALF_HOUR_10_ITEM_ONE_PAGE_QA' in w09),
('audit-f1','F1 — Registry version drift' in audit),
('audit-f5','F5 — Skill metric packs lacked a uniform runtime-state declaration' in audit),
('workflow-self','all_skills_clean_room_audit_suite.py' in workflow),
('builder-self','all_skills_clean_room_audit_suite.py' in builder),
('artifact-boundary','ARTIFACT_QA=NOT_YET_TESTED' in runtime),
('multi-skill-no-average','Multi-skill worksheets require every active skill to pass independently' in runtime),
]
for x in cross:add(*x)
assert len(CASES)==180,len(CASES)

failed=[x for x in CASES if not x[1]]
if failed:
    print(f'ALL-SKILLS CLEAN-ROOM AUDIT: FAIL ({len(failed)}/180)')
    for n,_,d in failed: print('FAIL',n,d)
    sys.exit(1)
print('ALL-SKILLS CLEAN-ROOM AUDIT: PASS')
print('cases: 180')
print('pass: 180')
print('fail: 0')
print('skills: 15/15 canonical-state runtime packs verified')
print('learner-read chain: OWNER -> W07 -> W10 -> W08 -> W09')
print('prompt/knowledge audit: PASS')
print('artifact QA: NOT_YET_TESTED')
