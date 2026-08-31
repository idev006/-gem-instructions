# Gem Installation Guide — activity-based-elementary-worksheet

Version: 2.6.3-LTS
Target Gem baseline: 2.6.x
Installation profile: Orchestrator + 10 Specialist Workers

## 1. Main Instructions

Use the complete generated `01_MAIN_INSTRUCTIONS/GEM_ORCHESTRATOR_INSTRUCTIONS.txt` from the successful CI installation ZIP in the Gem Instructions field.

Do not replace it with a shortened formula dump. Generated Instructions include the Orchestrator and all mandatory shared safety profiles.

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

W10 is a production worker, not a hotfix. It independently audits measuring instruments, common centers/origins, local-span/reference geometry, scale feasibility and shape-aware page evidence.

## 3. Five mandatory safety profiles

All 10 worker bundles embed:

- `SYSTEM_WIDE_QUALITY_PROFILE.md`
- `SCALE_LINE_INTEGRITY_PROFILE.md`
- `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `METROLOGY_ASSURANCE_PROFILE.md`
- `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Whenever a student reads an instrument:

`OWNING WORKER → W07 → W10 → W08 → W09`

W07 audits geometry. W10 independently recomputes metrology/local-span/reference/common-center/shape/page evidence. Missing either audit blocks prompt release.

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
- actual weight-dial inactive-gap regression `32/32`
- physical page feasibility regression `48/48`
- actual instrument geometry regression `64/64`
- measurement reference artifact regression `66/66`
- repository full-line audit `81/81`
- combined `1366/1366 PASS`
- package build PASS
- ZIP integrity PASS
- artifact upload PASS

Do not locally rebuild and call it the CI artifact.

## 5. Health check after installation

Send:

`ตรวจสุขภาพ Gem`

Expected:

- release family 2.6.3-LTS / compatible baseline 2.6.x
- W01..W10 present
- worker schema version 1
- five mandatory shared profiles present
- `W10_METROLOGY_ENGINEER` active
- `KB_COMPATIBILITY_QA=PASS`
- `INSTALLATION_HEALTH=PASS`

## 6. Critical instrument smoke tests

### Clock — continuous hour hand
`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ มีเวลาประมาณ 2:45 ไม่มีเฉลย`

Expected: W02+W07+W10+W08+W09; 60 distinct minute positions; for 2:45 minute hand=270° and hour hand=82.5°, exactly 75% from 2 toward 3; short hand must not stay directly on 2; hands share one pivot.

### Ruler — endpoint projection/reference
`ป.3 วัดความยาววัตถุด้วยไม้บรรทัด เซนติเมตรและมิลลิเมตร เริ่มที่ 0 จำนวน 10 ข้อ ไม่มีเฉลย`

Expected each 1cm @1mm span =10 intervals/11 positions/9 interior; physical edge not graduation; object start aligns exactly with zero graduation; object start/end have thin dashed vertical projection guides to their ruler graduations. For explicit nonzero-start tasks, both guides remain and answer uses `END-START`.

### Weight dial — per-kilogram hierarchy
`ป.3 อ่านตราชั่ง 0–5 กก. ขีดย่อย 0.1 กก. 10 ข้อ ไม่มีเฉลย`

Expected:
- 0 at top, values increase clockwise;
- labels `0@0°,1@60°,2@120°,3@180°,4@240°,5@300°`;
- 50 intervals /51 active positions;
- exactly 10 intervals in each 1 kg span;
- existing +0.5 kg position is an intermediate tick longer than ordinary 0.1 kg ticks and shorter/weaker than whole-kilogram major ticks;
- no extra tick is created at +0.5 kg;
- inactive gap `(300°,360°)` with zero radial scale-like marks;
- needle pivot equals dial center.

### Protractor
`ป.4 อ่านมุมจากโพรแทรกเตอร์ 0–180° ขีดละ 1° 10 ข้อ ไม่มีเฉลย`

Expected:
- perfect upper semicircle;
- 180 intervals /181 positions;
- single active numeric scale unless dual-scale is explicitly taught;
- 0° right/90° top/180° left;
- exact common center = baseline midpoint = ray origin;
- all ticks/rays radial;
- deterministic geometry;
- width >=70mm at 0.60mm spacing floor;
- no ellipse/skew/shear/non-uniform transform;
- page packing uses 35mm semicircle body height at 70mm width plus actual label/answer reserves.

### Thermometer
`ป.4 อ่านเทอร์โมมิเตอร์ 0–50°C ขีดละ 1°C 10 ข้อ ไม่มีเฉลย`

Expected 50 intervals/51 positions; 6 major +5 intermediate +40 ordinary minor; each 10°C span has 10 intervals/9 interior; liquid endpoint exactly on target.

### Speedometer
`ป.4 อ่านหน้าปัดความเร็วรถ 0–120 km/h ขีดละ 10 km/h 10 ข้อ ไม่มีเฉลย`

Expected 12 intervals/13 positions, 240° active, 120° inactive, exact mapping, pivot exactly at dial/reading-ring center, and radial needle.

### Graduated container — local-span recount
`ป.4 อ่านปริมาตรจากภาชนะตวง 0–1000 mL ขีดละ 50 mL 10 ข้อ ไม่มีเฉลย`

Expected 20 intervals/21 positions globally; major labels every 100 mL; every adjacent 100 mL span has exactly 2 equal intervals and exactly one interior +50 mL tick; no extra short strokes/pseudo-ticks; explicit level/meniscus convention.

### Graph axis
`ป.4 อ่านกราฟแท่งที่แกนตั้งเพิ่มทีละ 5 จำนวน 10 ข้อ`

Expected equal numeric increments map to equal physical spacing and bar endpoints map to canonical data.

## 7. Physical page behavior

Default:

`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

Page calculations use shape-aware item bounding boxes. Circular diameter contributes width and height; a semicircular protractor of width W contributes body height W/2 before labels/answers. When unlocked, an infeasible candidate is paginated rather than degraded.

## 8. Renderer review behavior

For every learner-read instrument, final prompt includes:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

and:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Review explicitly checks exact global and local-span counts, endpoint/reference projections, labels/order, common center/origin, radial collinearity, continuous clock-hand interpolation, shape integrity, target alignment and inactive regions. `Looks correct` is insufficient.

## 9. Prompt vs artifact QA

Passing all prompt/package gates does not prove rendered pixels.

Before actual image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

One wrong learner-read scale, local subdivision, reference projection, hour-hand interpolation, label order, pivot/origin, or distorted instrument means `ARTIFACT_QA=FAIL` and `CLASSROOM_RELEASE=BLOCKED`.
