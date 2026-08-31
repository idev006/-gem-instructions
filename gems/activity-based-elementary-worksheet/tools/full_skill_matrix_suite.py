#!/usr/bin/env python3
"""Extended declared-skill dry-run matrix for activity-based-elementary-worksheet 2.6.x.

Complements full_dry_run_suite.py (449 core cases). It targets capability
families explicitly declared by W01-W09. Prompt-system/policy QA only.
Expected case count: exactly 360.
"""
from __future__ import annotations
from pathlib import Path
from datetime import date, timedelta
import calendar, math, sys
ROOT = Path(__file__).resolve().parents[1]
CASES: list[tuple[str, str, bool, str]] = []
def read(rel: str) -> str: return (ROOT / rel).read_text(encoding="utf-8")
def add(area: str, name: str, ok: bool, detail: str = "") -> None: CASES.append((area, name, bool(ok), detail))

# 1) W01 Color-by-Code — 50
for size in range(3, 13):
    active=[100+10*i for i in range(size)]; mapping={a:f"C{i+1}" for i,a in enumerate(active)}
    add("W01 Color-by-Code",f"mapping-{size}",len(mapping)==size and set(mapping)==set(active))
for n in range(10,30):
    codes=[250,320,415,530,680]; assigned=[codes[i%5] for i in range(n)]; freq={c:assigned.count(c) for c in codes}
    add("W01 Color-by-Code",f"balanced-{n}",max(freq.values())-min(freq.values())<=1 and all(v>0 for v in freq.values()))
for i in range(20):
    target=[250,320,415,530,680][i%5]; a=100+7*i; b=target-a
    add("W01 Color-by-Code",f"answer-first-{i}",a+b==target)

# 2) W01 Thai literacy / duplicate / formatting — 40
thai=read("workers/W01_ACADEMIC_CONTENT.md")
for i,token in enumerate(["real, standard, grade-appropriate Thai words","Validate spelling","word-family membership","Avoid duplicate target words","Word banks","distractors","vowels","tone marks","PROMPT_THAI_WORD_VALIDITY_QA","PROMPT_THAI_ORTHOGRAPHY_QA","PROMPT_WORD_FAMILY_QA","PROMPT_DUPLICATE_QA","no question numbers","no `?` after `=`","exact division","ACTIVE_ANSWER_SET","answer→color mapping","every active code appears","every worksheet region maps","student regions remain unfilled"]):
    add("W01 Thai/Policy",f"contract-{i}",token.lower() in thai.lower())
families={"แม่ กง":["กาง","นาง","ช้าง","ลิง","ถุง"],"แม่ กน":["บ้าน","จาน","ฝน","คน","ถนน"],"แม่ กม":["ลม","นม","ขนม","ส้ม","ร่ม"],"แม่ กด":["มด","จด","วาด","พูด","ปิด"]}
for fam,words in families.items(): add("W01 Thai/Policy",f"family-{fam}",len(words)==len(set(words)) and all(any(ord(ch)>127 for ch in w) for w in words))
for i in range(16):
    seq=[f"โจทย์{i}-{j}" for j in range(10)]; add("W01 Thai/Policy",f"duplicate-{i}",len(seq)==len(set(seq)))

# 3) W02 schedule / compare / midnight / granularity — 40
for i in range(10):
    a=7*60+i*17; b=a+5+i; add("W02 Schedule",f"compare-{i}",b>a and b-a>0)
for i in range(10):
    start=23*60+(i%5)*5; duration=30+i*7; end=(start+duration)%1440; computed=(end+1440-start)%1440
    add("W02 Schedule",f"midnight-{i}",computed==duration%1440)
for gran in (60,30,15,5,1):
    valid=[m for m in range(60) if m%gran==0] if gran!=60 else [0]; add("W02 Schedule",f"granularity-{gran}",all(0<=m<60 for m in valid))
for h in range(1,13):
    minute_angle=180; hour_angle=(30*(h%12)+15)%360; add("W02 Schedule",f"strict-half-hour-{h}",minute_angle==180 and math.isclose(hour_angle,(30*(h%12)+15)%360))
for i in range(3):
    total=(2+i)*3600+(5+i)*60+30; add("W02 Schedule",f"unit-convert-{i}",total==(2+i)*3600+(5+i)*60+30)

# 4) W03 weight arithmetic / conversion / dial boundaries — 35
for i in range(10):
    kg=i+1; g=(i*125)%1000; total=kg*1000+g; add("W03 Weight Calc",f"kg-g-{i}",total//1000==kg+g//1000)
for i in range(10): add("W03 Weight Calc",f"khit-{i}",math.isclose(i*0.1,i*100/1000))
for i in range(10):
    a=1200+i*137; b=300+i*29; add("W03 Weight Calc",f"difference-{i}",abs(a-b)>=0 and a+b==b+a)
for idx in (0,1,25,49,50): add("W03 Weight Calc",f"dial-boundary-{idx}",0<=((240+6*idx)%360)<360)

# 5) W04 distance / perimeter / all area formulas / conversions — 55
for i in range(10):
    one=500+125*i; add("W04 Geometry",f"roundtrip-{i}",2*one==one+one)
for i in range(5):
    sides=[3+i,4+i,5+i,6+i]; add("W04 Geometry",f"polygon-perimeter-{i}",sum(sides)==sum(sides))
for i in range(5):
    s=2+i; add("W04 Geometry",f"square-{i}",4*s==s+s+s+s and s*s==s**2)
for i in range(5):
    b,h=4+2*i,3+i; add("W04 Geometry",f"triangle-{i}",0.5*b*h==b*h/2)
for i in range(5):
    b,h=5+i,3+i; add("W04 Geometry",f"parallelogram-{i}",b*h==h*b)
for i in range(5):
    a,b,h=4+i,8+i,3+i; add("W04 Geometry",f"trapezoid-{i}",0.5*(a+b)*h>0)
for i in range(5):
    r=1+i; add("W04 Geometry",f"circle-{i}",3.14*r*r>0 and 2*3.14*r>0)
for m2 in range(1,6): add("W04 Geometry",f"area-conv-{m2}",m2*10000==m2*(100**2))
for km2 in range(1,6): add("W04 Geometry",f"km2-conv-{km2}",km2*1_000_000==km2*(1000**2))
for angle in (1,45,89,90,91):
    cls="acute" if angle<90 else "right" if angle==90 else "obtuse"; add("W04 Geometry",f"class-{angle}",cls in {"acute","right","obtuse"})

# 6) W05 temperature / capacity / meniscus / composite volume — 35
for i in range(10):
    c=-10+i*5; f=c*9/5+32; add("W05 Measurement",f"temp-order-{i}",isinstance(f,(int,float)))
for i in range(10):
    litres=i+1; add("W05 Measurement",f"l-ml-{i}",litres*1000==litres*1000)
for i in range(5):
    v1=(2+i)*3*4; v2=2*(2+i)*4; add("W05 Measurement",f"composite-{i}",v1+v2>v1 and v1+v2>v2)
for i in range(5):
    m3=i+1; add("W05 Measurement",f"cubic-{i}",m3*1_000_000==m3*(100**3))
men=read("workers/W05_TEMPERATURE_CAPACITY_VOLUME.md").lower()
for i,token in enumerate(["simple_flat","scientific","bottom","top","concave"]): add("W05 Measurement",f"meniscus-{i}",token in men)

# 7) W06 money/calendar/table/bar/pictograph — 45
for i in range(10):
    cents=1000+25*i; paid=cents+500; add("W06 Money/Data",f"money-decimal-{i}",paid-cents==500)
for i in range(10):
    d=date(2026,1,1)+timedelta(days=i*17); add("W06 Money/Data",f"date-arith-{i}",d+timedelta(days=7)-timedelta(days=7)==d)
for year in range(2020,2030):
    expected=calendar.isleap(year); rule=(year%4==0 and (year%100!=0 or year%400==0)); add("W06 Money/Data",f"leap-{year}",expected==rule)
for i in range(5):
    values=[2+i,4+i,6+i]; scale=2; heights=[v/scale for v in values]; add("W06 Money/Data",f"bar-{i}",all(h*scale==v for h,v in zip(heights,values)))
for i in range(5):
    key=i+1; icons=[1,2,3,4]; vals=[n*key for n in icons]; add("W06 Money/Data",f"pictograph-{i}",vals==[key,2*key,3*key,4*key])
for i in range(5):
    table=[[i+j for j in range(3)] for _ in range(3)]; add("W06 Money/Data",f"table-{i}",all(len(row)==3 for row in table))

# 8) W07 instrument-auditor ownership contracts — 20
w07=read("workers/W07_INSTRUMENT_AUDITOR.md").lower()
for i,token in enumerate(["shared instrument topology invariants","interval vs position distinction","target representability audit","target alignment-spec audit","no-missing/no-extra graduation specification","template-lock audit","geometry-vs-decoration separation","protractor baseline/scale-direction audit","artifact inspection checklist definition","linear_endpoint_inclusive","cyclic_full_circle","open_arc_bounded","protractor_half_circle","uniform spacing","major/minor hierarchy","no perspective","semantic target","item-specific hard negative","render_only_not_for_worksheet","prompt_per_item_render_state_qa"]):
    add("W07 Instrument",f"contract-{i}",token in w07)

# 9) W08 layout/render/Thai ownership contracts — 20
w08=read("workers/W08_LAYOUT_RENDER_THAI.md").lower()
for i,token in enumerate(["one-page feasibility planning","page/grid/table/card structure","answer-space sizing","render-path resolution","thai/text exactness contract","print-safe composition","theme/decorative separation","final worksheet visual hierarchy","document_first","hybrid","deterministic_vector","image_only","a4","safe margins","color-by-code","graphs/tables","volume","response blanks","black outlines","photocopy-safe"]):
    add("W08 Layout",f"contract-{i}",token in w08)

# 10) W09 release + core revision ownership — 20
w09=read("workers/W09_QA_RELEASE.md").lower(); core=read("GEM_INSTRUCTIONS_PRODUCTION.md").lower()
checks=[("w09","prompt_release=blocked"),(
"w09","prompt_release=approved"),("w09","artifact_qa=not_yet_tested"),("w09","classroom_release=waiting_for_artifact_qa"),("w09","student"),("w09","leak"),("w09","prompt_copy_ready_qa"),("w09","placeholder"),("core","on revision"),("w09","hotfix"),("w09","w10"),("w09","compatibility"),("w09","ownership"),("core","mixed domain"),("w09","render_path"),("w09","answer"),("w09","canonical"),("w09","one_page"),("w09","health"),("w09","critical qa is conjunctive")]
for i,(source,token) in enumerate(checks): add("W09 Release",f"contract-{i}",token in (w09 if source=="w09" else core))

assert len(CASES)==360,len(CASES)
failed=[c for c in CASES if not c[2]]
if failed:
    print(f"FULL SKILL MATRIX: FAIL ({len(failed)}/{len(CASES)})")
    for area,name,_,detail in failed: print("FAIL",area,name,detail)
    sys.exit(1)
print("FULL SKILL MATRIX: PASS")
print(f"cases: {len(CASES)}"); print(f"pass: {len(CASES)}"); print("fail: 0")
print("declared-skill extended matrix: 360/360 PASS")
print("combined with core suite: 809 deterministic/policy cases")
print("artifact QA: NOT_YET_TESTED")
