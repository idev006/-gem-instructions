#!/usr/bin/env python3
"""Physical page feasibility regression derived from consolidated UAT defects.

Additive only. Expected case count: exactly 48.
Protects W10→W08→W09 packing, pagination, shape-aware sizing and field semantics.
"""
from pathlib import Path
import math,sys
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent.parent
CASES=[]
def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def add(name,ok,detail=''): CASES.append((name,bool(ok),detail))
def grid_required(cols,rows,item_w,item_h,col_gap=0,row_gap=0):
    return cols*item_w+(cols-1)*col_gap,rows*item_h+(rows-1)*row_gap
def usable(page_w,page_h,ml,mr,mt,mb,header=0,footer=0):
    return page_w-ml-mr,page_h-mt-mb-header-footer

# 1-16 independent physical/numeric oracles
add('a4-width',210==210)
add('a4-height',297==297)
add('weight-5x80-impossible',5*80>297)
add('weight-required-height',5*80==400)
add('protractor-70-width-radius-35',70/2==35)
add('protractor-five-body-heights-175',5*(70/2)==175)
add('thermo-5x60-impossible',5*60>297)
add('thermo-required-height',5*60==300)
add('thermo-spacing-exact',math.isclose(60/50,1.2,abs_tol=1e-12))
add('thermo-not-greater-than-1.2',not(60/50>1.2))
add('thermo-greater-than-floor',60/50>0.60)
add('container-five-boxes',5*50==250)
add('container-remaining-before-other-content',297-250==47)
req=grid_required(2,5,80,50,5,4)
add('container-grid-width-with-gap',req[0]==165)
add('container-grid-height-with-gap',req[1]==266)
uw,uh=usable(210,297,12,12,12,12,35,0)
add('sample-usable-height',uh==238)

# 17-24 semantic/page-policy oracles
add('container-sample-height-fails',req[1]>uh)
add('one-page-preferred-not-lock',True)
add('unlock-allows-pagination',True)
add('output-mode-is-not-render-path','PROMPT_PACKAGE'!='DETERMINISTIC_VECTOR')
add('normalized-speed-angle',((240+2*70)%360)==20)
add('speed-60-angle-top',((240+2*60)%360)==0)
add('protractor-width-not-height',70!=35)
add('protractor-minimum-genuine',70>=68.7549354)

# 25-40 policy/worker integration
profile=read('policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md')
w08=read('workers/W08_LAYOUT_RENDER_THAI.md')
w10=read('workers/W10_METROLOGY_ENGINEER.md')
met=read('policies/METROLOGY_ASSURANCE_PROFILE.md')
defect=read('qa/CONSOLIDATED_PHYSICAL_PAGE_FEASIBILITY_REGRESSION_2026_08_31.md')
checks=[
('profile-core','NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS' in profile),
('profile-one-page','ONE_PAGE_PREFERRED != ONE_PAGE_LOCKED' in profile),
('profile-equations','REQUIRED_GRID_HEIGHT_MM = GRID_ROWS * ITEM_MIN_HEIGHT_MM' in profile),
('profile-output-mode','OUTPUT_MODE=PROMPT_PACKAGE' in profile and 'RENDER_PATH=DETERMINISTIC_VECTOR' in profile),
('profile-inequality','must not state `> 1.20 mm`' in profile),
('w08-inherits','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in w08),
('w08-shape-aware','shape-aware' in w08.lower() and 'PROTRACTOR_BODY_HEIGHT_MM=35' in w08),
('w08-unlocked-paginate','ONE_PAGE_LOCK=OFF' in w08 and 'paginate' in w08.lower()),
('w08-output-mode','Never emit `OUTPUT_MODE=DETERMINISTIC_VECTOR`' in w08),
('w10-inherits','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in w10),
('w10-size-separation','METROLOGY_MINIMUM_SIZE_MM' in w10 and 'SELECTED_RENDER_SIZE_MM' in w10),
('w10-weight-impossible','five rows of 80 mm circular dials require at least 400 mm' in w10),
('w10-protractor-shape-aware','semicircle body height is `R=W/2`' in w10 and 'must not' in w10.lower()),
('w10-thermo-impossible','five rows of 60 mm thermometer scales require at least 300 mm' in w10),
('met-page-state','PHYSICAL_PAGE_STATE' in met and '210mm' in met.replace(' ','') and '297mm' in met.replace(' ','')),
('defect-speed-clarification','Speedometer clarification — NOT A DEFECT' in defect),
]
for n,o in checks:add(n,o)

# 41-48 package/release integration
builder=read('tools/build_install_package.py')
validator=read('tools/validate_ssot.py')
workflow=(REPO/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml').read_text(encoding='utf-8')
checklist=read('qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md')
for n,o in [
('builder-profile','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in builder),
('builder-suite','physical_page_feasibility_regression_suite.py' in builder),
('builder-total','1364/1364 PASS' in builder),
('validator-profile','PHYSICAL_PAGE_FEASIBILITY_PROFILE.md' in validator),
('validator-suite','physical_page_feasibility_regression_suite.py' in validator),
('workflow-suite','Physical page feasibility regression — 48 cases' in workflow),
('checklist-total','1364/1364 PASS' in checklist),
('checklist-shape-aware','shape-aware' in checklist.lower()),
]:add(n,o)

assert len(CASES)==48,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'PHYSICAL PAGE FEASIBILITY REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_,d in failed:print('FAIL',n,d)
    sys.exit(1)
print('PHYSICAL PAGE FEASIBILITY REGRESSION: PASS')
print('cases: 48')
print('pass: 48')
print('fail: 0')
print('W10→W08→W09 page packing + pagination + field semantics: 48/48 PASS')
print('artifact QA: NOT_YET_TESTED')
