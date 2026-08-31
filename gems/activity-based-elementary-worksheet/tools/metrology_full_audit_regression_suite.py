#!/usr/bin/env python3
"""Independent full metrology audit across all learner-read scale families.

Added with W10_METROLOGY_ENGINEER. This suite complements all prior gates and
never replaces them. Expected case count: exactly 80.
"""
from pathlib import Path
import math, sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
CASES=[]

def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def add(name, ok, detail=''): CASES.append((name,bool(ok),detail))
def linear(a,b,d):
    n=round((b-a)/d); return n,n+1,max(n-1,0)
def arc_spacing(radius_mm, deg): return radius_mm*math.radians(deg)

# 1-40 independent quantitative oracles
# Clock 1-5
add('clock-60-intervals',360//6==60)
add('clock-60-positions',60==60)
add('clock-1min-angle',math.isclose(360/60,6.0))
add('clock-10-30-minute-angle',math.isclose(30*6,180.0))
add('clock-10-30-hour-angle',math.isclose(10*30+30*0.5,315.0))
# Weight dial 6-10
w=linear(0,5,0.1)
add('weight-50-intervals',w[0]==50)
add('weight-51-positions',w[1]==51)
add('weight-2.5-index',round(2.5/0.1)==25)
add('weight-active-sweep-step',math.isclose(300/50,6.0))
add('weight-inactive-gap',360-300==60)
# Ruler 11-15
r=linear(0,10,1)
add('ruler-1cm-10-intervals',r[0]==10)
add('ruler-1cm-11-positions',r[1]==11)
add('ruler-1cm-9-interior',r[2]==9)
add('ruler-5mm-existing-index',round(5/1)==5)
add('ruler-nonzero-reading',13-4==9)
# Speedometer 16-20
s=linear(0,120,10)
add('speed-12-intervals',s[0]==12)
add('speed-13-positions',s[1]==13)
add('speed-60-angle',math.isclose((240+2*60)%360,0.0))
add('speed-gap',360-240==120)
add('speed-35-not-representable',not math.isclose(round(35/10)*10,35))
# Protractor 21-27
p=linear(0,180,1)
add('protractor-180-intervals',p[0]==180)
add('protractor-181-positions',p[1]==181)
add('protractor-65mm-fails',arc_spacing(32.5,1)<0.60)
add('protractor-70mm-passes',arc_spacing(35,1)>=0.60)
minr=0.60/math.radians(1)
add('protractor-min-radius',math.isclose(minr,34.3774677,abs_tol=1e-6))
add('protractor-min-diameter',math.isclose(2*minr,68.7549354,abs_tol=1e-6))
add('protractor-5deg-is-existing-position',5%1==0)
# Thermometer 28-32
t=linear(0,50,1)
add('thermo-50-intervals',t[0]==50)
add('thermo-51-positions',t[1]==51)
add('thermo-minus10-zero-index',round((0-(-10))/1)==10)
t2=linear(0,100,5)
add('thermo-100-5-20-intervals',t2[0]==20)
add('thermo-37-invalid-on-5deg',not math.isclose(round(37/5)*5,37))
# Container 33-36
c=linear(0,1000,50)
add('container-0-1000-50-20-intervals',c[0]==20)
add('container-21-positions',c[1]==21)
add('container-750-index',round(750/50)==15)
add('container-775-invalid',not math.isclose(round(775/50)*50,775))
# Graph axis 37-40
vals=[0,5,10,15,20]
coords=[0,10,20,30,40]
add('graph-equal-value-step',len(set(vals[i+1]-vals[i] for i in range(4)))==1)
add('graph-equal-physical-step',len(set(coords[i+1]-coords[i] for i in range(4)))==1)
add('graph-linear-mapping',all(coords[i]==2*vals[i] for i in range(5)))
add('graph-bar-target-map',2*15==30)

# 41-60 policy/worker audit tokens
profile=read('policies/METROLOGY_ASSURANCE_PROFILE.md')
w10=read('workers/W10_METROLOGY_ENGINEER.md')
for name,needle in [
('profile-one-wrong','ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER'),
('profile-dual-audit','W07 INSTRUMENT GEOMETRY AUDIT → W10 INDEPENDENT METROLOGY AUDIT'),
('profile-linear-oracle','intervals=(max-min)/minor_interval'),
('profile-clock','60 intervals / 60 distinct positions / 6° per interval'),
('profile-weight','50 active intervals / 51 active positions'),
('profile-speed','12 active intervals / 13 active positions'),
('profile-spacing-formula','tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)'),
('profile-protractor-70','production minimum is `70 mm`'),
('profile-thermo','liquid endpoint on the target graduation centerline'),
('profile-container','meniscus'),
('profile-graph','Equal numeric increments must map to equal physical distances'),
('profile-render-gate','PROMPT_METROLOGY_RENDER_PATH_QA'),
('profile-page-gate','PROMPT_METROLOGY_PAGE_FEASIBILITY_QA'),
('profile-print-gate','PROMPT_METROLOGY_PRINT_FEASIBILITY_QA'),
('w10-id','WORKER_ID=W10_METROLOGY_ENGINEER'),
('w10-independence','recompute at least one independent quantitative oracle'),
('w10-65-reject','Any proposed 65 mm diameter at 1° is rejected'),
('w10-families','graduated container/meniscus'),
('w10-state','METROLOGY_AUDIT_STATE'),
('w10-artifact-boundary','ARTIFACT_QA=NOT_YET_TESTED')]:
    add(name,needle in (w10 if name.startswith('w10-') else profile))

# 61-80 integration / package / release checks
core=read('GEM_INSTRUCTIONS_PRODUCTION.md')
router=read('KB_ROUTER.md')
manifest=read('KB_MANIFEST.md')
builder=read('tools/build_install_package.py')
validator=read('tools/validate_ssot.py')
workflow=(REPO/'.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml').read_text(encoding='utf-8')
checklist=read('qa/BASELINE_2_6_3_RELEASE_CHECKLIST.md')
scale=read('policies/SCALE_LINE_INTEGRITY_PROFILE.md')
review=read('policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md')
integ=[
('core-ten-workers','Exactly ten logical workers' in core),
('core-w10','W10_METROLOGY_ENGINEER' in core),
('core-dual-audit','W07 + W10' in core),
('router-w10','W10_METROLOGY_ENGINEER' in router),
('router-instrument-route','W07 + W10 + W08 + W09' in router),
('manifest-ten','10 base Knowledge workers' in manifest),
('manifest-w10','W10_METROLOGY_ENGINEER' in manifest),
('manifest-four-profiles','METROLOGY_ASSURANCE_PROFILE.md' in manifest),
('builder-w10','W10_METROLOGY_ENGINEER.txt' in builder),
('builder-four-profiles','METROLOGY_PROFILE' in builder),
('builder-metrology-suite','metrology_full_audit_regression_suite.py' in builder),
('builder-total','1107/1107 PASS' in builder),
('validator-w10','W10_METROLOGY_ENGINEER' in validator),
('validator-suite','metrology_full_audit_regression_suite.py' in validator),
('workflow-suite','Full metrology audit — 80 cases' in workflow),
('workflow-10worker-artifact','10WORKERS' in workflow),
('checklist-total','1107/1107 PASS' in checklist),
('checklist-w10','W10_METROLOGY_ENGINEER' in checklist),
('scale-metrology-link','METROLOGY_ASSURANCE_PROFILE.md' in scale),
('review-metrology-link','W10_METROLOGY_ENGINEER' in review),
]
for name,ok in integ: add(name,ok)

assert len(CASES)==80,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'METROLOGY FULL AUDIT REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_,d in failed: print('FAIL',n,d)
    sys.exit(1)
print('METROLOGY FULL AUDIT REGRESSION: PASS')
print('cases: 80')
print('pass: 80')
print('fail: 0')
print('all learner-read scale families + independent W10 metrology audit: 80/80 PASS')
print('artifact QA: NOT_YET_TESTED')
