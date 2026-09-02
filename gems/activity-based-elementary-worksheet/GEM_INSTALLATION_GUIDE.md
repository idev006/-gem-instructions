# Gem Installation Guide — activity-based-elementary-worksheet

Version: 2.6.3-LTS
Target Gem baseline: 2.6.x
Installation profile: Orchestrator + 10 Specialist Workers

## 1. Main Instructions

Use the complete generated `01_MAIN_INSTRUCTIONS/GEM_ORCHESTRATOR_INSTRUCTIONS.txt` from the successful CI installation ZIP in the Gem Instructions field.

Do not replace it with a shortened formula dump. Generated Instructions include the Orchestrator, all mandatory technical safety profiles, primary-school pedagogy profile and current actual-defect evidence.

## 2. Knowledge upload — exactly 10 base files

Upload every `.txt` from `02_UPLOAD_10_WORKER_KNOWLEDGE_TXT`:

1. `W01_ACADEMIC_CONTENT.txt`
2. `W02_TIME_CLOCK.txt`
3. `W03_WEIGHT_SCALE.txt`
4. `W04_LENGTH_DISTANCE.txt`
5. `W05_TEMPERATURE_CAPACITY_VOLUME.txt`
6. `W06_MONEY_CALENDAR_DATA.txt`
7. `W07_INSTRUMENT_AUDITOR.txt`
8. `W08_LAYOUT_RENDER_THAI.txt`
9. `W09_QA_RELEASE.txt`
10. `W10_METROLOGY_ENGINEER.txt`

W10 independently audits measuring instruments, common centers/origins, local-span/reference geometry, scale feasibility and shape-aware page evidence.

## 3. Mandatory runtime safety knowledge

Every worker bundle embeds five technical safety profiles:
- `SYSTEM_WIDE_QUALITY_PROFILE.md`
- `SCALE_LINE_INTEGRITY_PROFILE.md`
- `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `METROLOGY_ASSURANCE_PROFILE.md`
- `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Every bundle also embeds:
- `PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`

Whenever a student reads an instrument:
`OWNING WORKER → W07 → W10 → W08 → W09`

`NO WORKER MAY SELF-CERTIFY ITS OWN HIGH-RISK OUTPUT.`

## 4. Release artifact eligibility

Install only a ZIP whose exact GitHub Actions source commit passed:

- SSOT validation
- core dry-run `449/449`
- declared-skill matrix `360/360`
- runtime UAT `12/12`
- semantic oracle `20/20`
- system-wide quality `30/30`
- scale-line integrity `40/40`
- instrument review/speedometer `60/60`
- protractor scale safety `24/24`
- full metrology audit `80/80`
- actual weight-dial inactive-gap `32/32`
- physical page feasibility `48/48`
- actual instrument geometry `64/64`
- measurement reference artifact `66/66`
- clock hand endpoint `32/32`
- weight dial visible subdivision `32/32`
- primary-school pedagogy/usability `64/64`
- repository full-line audit `81/81`
- combined effective `1494/1494 PASS`
- package build PASS
- ZIP integrity PASS
- artifact upload PASS

Do not locally rebuild and label it as the CI artifact.

## 5. Health check after installation

Send:
`ตรวจสุขภาพ Gem`

Expected:
- release family2.6.3-LTS / compatible baseline2.6.x
- W01..W10 present
- worker schema1
- five mandatory technical shared profiles present
- mandatory primary-school pedagogy profile present
- `W10_METROLOGY_ENGINEER` active
- `KB_COMPATIBILITY_QA=PASS`
- `INSTALLATION_HEALTH=PASS`

## 6. Primary learner defaults

Without explicit safe override:
- A4 Portrait on every page;
- `ONE_PAGE_LOCK=OFF` and pagination allowed when needed;
- P1–P3 body text target >=14pt;
- P4–P6 body text target >=12pt;
- title target >=18pt;
- learner-read numerals target >=12pt;
- response clear height P1–P3 >=8mm, P4–P6 >=6mm;
- concise grade-appropriate directions;
- one clear response zone per item;
- no essential meaning by color alone;
- no decoration competing with academic data.

## 7. Academic geometry mode

For learner-read geometry the generated prompt must carry:
`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES`
`CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES`
`POST_LAYOUT_GEOMETRY_TRANSFORM=UNIFORM_SCALE_AND_TRANSLATE_ONLY`

Free-form image generation can decorate around the instrument but cannot redraw academic ticks, labels, hands, pointers, rays, axes or reading levels.

## 8. Critical smoke tests

### Clock — continuous/vector hour hand
`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นครึ่งชั่วโมง ไม่มีเฉลย`

Expected: for every :30 item the minute hand is at 6 and the short hand is exactly halfway to the next numeral. 3:30=105°, not90°; 9:30=285°, not270°. Exact vector endpoints are included in renderer-only state.

### Ruler — endpoint projection/reference
`ป.3 วัดความยาววัตถุด้วยไม้บรรทัด เซนติเมตรและมิลลิเมตร เริ่มที่ 0 จำนวน 10 ข้อ ไม่มีเฉลย`

Expected 1cm @1mm=10 intervals/11 positions/9 interior; edge not graduation; object start aligns zero; dashed vertical start/end projection guides.

### Weight dial — visible per-kilogram grammar
`ป.3 อ่านตราชั่ง 0–5 กก. ขีดย่อย 0.1 กก. 10 ข้อ ไม่มีเฉลย`

Expected:
- 0 top, values increase clockwise;
- 50 intervals /51 active positions;
- each whole-kilogram span has exactly10 equal intervals,11 endpoint positions,9 interior marks;
- +0.5kg is the existing fifth interval and visually longer than ordinary minor marks;
- explicit visible tick position set serialized;
- inactive gap clean;
- pivot=center.

### Protractor
`ป.4 อ่านมุมจากโพรแทรกเตอร์ 0–180° ขีดละ 1° 10 ข้อ ไม่มีเฉลย`

Expected perfect upper semicircle,180/181,single active numeric scale unless dual-scale is the lesson,common center/ray origin,radial ticks,deterministic vector geometry,width>=70mm,no distortion.

### Thermometer
`ป.4 อ่านเทอร์โมมิเตอร์ 0–50°C ขีดละ 1°C 10 ข้อ ไม่มีเฉลย`

Expected50/51,6 major+5 intermediate+40 ordinary minor,10 intervals per10°C,liquid endpoint exact.

### Speedometer
`ป.4 อ่านหน้าปัดความเร็วรถ 0–120 km/h ขีดละ 10 km/h 10 ข้อ ไม่มีเฉลย`

Expected12/13,240° active,120° inactive,exact mapping,pivot=center,radial needle.

### Graduated container
`ป.4 อ่านปริมาตรจากภาชนะตวง 0–1000 mL ขีดละ 50 mL 10 ข้อ ไม่มีเฉลย`

Expected20/21 globally; each100mL span exactly2 intervals and one interior +50mL tick; no extra pseudo-ticks.

### Graph axis
`ป.4 อ่านกราฟแท่งที่แกนตั้งเพิ่มทีละ 5 จำนวน 10 ข้อ`

Expected canonical data-first 2D graph, equal numeric increments equal physical spacing, exact bar endpoints and complete content/page packing proof.

## 9. Physical page behavior

Implicit default:
`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

Page calculations use shape-aware item boxes. Physical fit is conjunctive with learner typography/writing-space rules. When unlocked, an unsafe or over-dense candidate is paginated rather than degraded.

## 10. Renderer review behavior

For every learner-read instrument:
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Review explicitly checks primitive manifest/global+local counts, references, labels/order, common center/origin, radial collinearity, continuous clock motion, shape integrity, target alignment and inactive regions.

## 11. Prompt vs artifact QA

Passing all prompt/package gates does not prove rendered pixels.

Before image inspection:
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Artifact QA includes `ARTIFACT_LEARNER_SIMULATION_QA`: a child must be able to identify what to read, what evidence to use and where to write, and derive the answer from visible information alone.

Any wrong scale, unreadable required content, ambiguous reference, wrong hand/pivot or distorted instrument blocks classroom release.
