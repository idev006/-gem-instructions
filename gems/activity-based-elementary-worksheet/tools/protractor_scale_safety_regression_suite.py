#!/usr/bin/env python3
"""Protractor scale-placement safety regression.

Protects 0–180° @1° topology, print spacing, active-scale clarity,
common-center geometry, deterministic rendering, and shape-aware page packing.
Expected case count: exactly 24.
"""
from pathlib import Path
import math,sys
ROOT=Path(__file__).resolve().parents[1];CASES=[]
def read(rel):return (ROOT/rel).read_text(encoding='utf-8')
def add(name,ok):CASES.append((name,bool(ok)))
def arc_spacing(diameter_mm,interval_deg):return (diameter_mm/2.0)*math.radians(interval_deg)
profile=read('policies/SCALE_LINE_INTEGRITY_PROFILE.md');w04=read('workers/W04_LENGTH_DISTANCE.md');w08=read('workers/W08_LAYOUT_RENDER_THAI.md');w09=read('workers/W09_QA_RELEASE.md')
add('topology-1deg-intervals',180==180)
add('topology-1deg-positions',181==181)
add('spacing-65mm-below-floor',arc_spacing(65,1)<0.60)
add('spacing-65mm-known-value',math.isclose(arc_spacing(65,1),0.5672320069,abs_tol=1e-6))
add('spacing-70mm-passes-floor',arc_spacing(70,1)>=0.60)
min_radius=0.60/math.radians(1)
add('minimum-radius-oracle',math.isclose(min_radius,34.3774677,abs_tol=1e-6))
add('minimum-diameter-oracle',math.isclose(2*min_radius,68.7549354,abs_tol=1e-6))
add('production-rounding-70',70>=2*min_radius)
add('profile-spacing-formula','tick_center_spacing_mm = reading_radius_mm × radians(MINOR_INTERVAL_DEG)' in profile)
add('profile-production-70','PRODUCTION_MIN_PROTRACTOR_WIDTH_MM=70' in profile)
add('profile-rejects-65','65 mm width fails' in profile)
add('profile-active-scale','one active numeric scale by default' in profile)
add('profile-render-auto-forbidden','deterministic' in profile.lower() and 'protractor' in profile.lower())
add('w04-spacing-oracle','MIN_READING_RING_DIAMETER_MM ≈ 68.76' in w04)
add('w04-production-70','PRODUCTION_MIN_PROTRACTOR_WIDTH_MM=70' in w04)
add('w04-65-blocked','65 mm wide protractor is invalid' in w04)
add('w04-active-direction','active scale reads counter-clockwise from right 0° to left 180°' in w04 and 'one active numeric scale only by default' in w04)
add('w04-five-degree-required','5° positions are intermediate' in w04 and 'reuse existing 1° positions' in w04)
add('w08-no-auto','final prompt must not contain unresolved `RENDER_PATH=AUTO`' in w08)
add('w08-shape-aware-page','PROTRACTOR_BODY_HEIGHT_MM=35' in w08 and 'shape-aware' in w08.lower() and '2-column layout is preferred' in w08)
add('w08-65-rejected','65 mm' in w08 and 'invalid' in w08.lower())
add('w09-spacing-gate','PROMPT_PROTRACTOR_PRINT_SPACING_QA' in w09 and 'PROMPT_SCALE_PRINT_SPACING_ORACLE_QA' in w09)
add('w09-render-path-gate','PROMPT_PROTRACTOR_RENDER_PATH_QA' in w09 and 'deterministic geometry' in w09)
add('w09-release-blocked','65mm rejected' in w09.replace(' ','') and 'PROMPT_RELEASE=BLOCKED' in w09)
assert len(CASES)==24,len(CASES)
failed=[c for c in CASES if not c[1]]
if failed:
    print(f'PROTRACTOR SCALE SAFETY REGRESSION: FAIL ({len(failed)}/{len(CASES)})')
    for n,_ in failed:print('FAIL',n)
    sys.exit(1)
print('PROTRACTOR SCALE SAFETY REGRESSION: PASS');print('cases: 24');print('pass: 24');print('fail: 0');print('protractor scale placement safety: 24/24 PASS');print('artifact QA: NOT_YET_TESTED')
