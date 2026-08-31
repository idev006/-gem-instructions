# Gem Installation Guide — activity-based-elementary-worksheet

Version: 2.6.3-LTS
Target Gem baseline: 2.6.x
Installation profile: Orchestrator + 10 Specialist Workers

## 1. Main Instructions

Use the complete generated `01_MAIN_INSTRUCTIONS/GEM_ORCHESTRATOR_INSTRUCTIONS.txt` from the CI installation ZIP in the Gem Instructions field.

Do not replace it with a shortened formula dump. The generated Instructions include the Orchestrator and all mandatory shared safety profiles.

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

W10 is a production worker, not a hotfix. It independently audits measuring instruments and scale feasibility.

## 3. Mandatory safety architecture

All 10 worker bundles embed:

- `SYSTEM_WIDE_QUALITY_PROFILE.md`
- `SCALE_LINE_INTEGRITY_PROFILE.md`
- `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `METROLOGY_ASSURANCE_PROFILE.md`

Whenever a student reads an instrument:

`OWNING WORKER → W07 → W10 → W08 → W09`

W07 audits geometry. W10 independently recomputes metrology evidence. Missing either audit blocks prompt release.

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
- combined `1075/1075 PASS`
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
- four mandatory shared profiles present
- `W10_METROLOGY_ENGINEER` active
- `KB_COMPATIBILITY_QA=PASS`
- `INSTALLATION_HEALTH=PASS`

## 6. Critical instrument smoke tests

### Clock
`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ไม่มีเฉลย`

Expected learner-read route includes W02 + W07 + W10 + W08 + W09. Full minute face = 60 distinct positions. 10:30 = minute 180°, hour 315°.

### Ruler
`ป.3 อ่านไม้บรรทัด เซนติเมตรและมิลลิเมตร 10 ข้อ ไม่มีเฉลย`

Expected: each 1 cm @1 mm span = 10 intervals / 11 positions / 9 interior positions; physical edge is not a graduation.

### Nonzero ruler start
`ป.4 วัดความยาวจากไม้บรรทัดโดยวัตถุไม่ได้เริ่มที่ 0 จำนวน 10 ข้อ`

Expected `length=end-start`.

### Weight dial
`ป.3 อ่านตราชั่ง 0–5 กก. ขีดย่อย 0.1 กก. 10 ข้อ ไม่มีเฉลย`

Expected canonical 50 active intervals / 51 active positions and no value ticks in the inactive gap.

### Protractor
`ป.4 อ่านมุมจากโพรแทรกเตอร์ 0–180° ขีดละ 1° 10 ข้อ ไม่มีเฉลย`

Expected:
- 180 intervals / 181 positions;
- exact origin/baseline/direction;
- deterministic instrument geometry;
- `tick_center_spacing_mm = reading_radius_mm × radians(1°)`;
- at 0.60 mm spacing floor, production width >=70 mm;
- 65 mm is rejected;
- one clearly active reading scale unless dual-scale reading is explicitly taught.

### Thermometer
`ป.4 อ่านเทอร์โมมิเตอร์ 0–50°C ขีดละ 1°C 10 ข้อ ไม่มีเฉลย`

Expected 50 intervals / 51 positions; liquid endpoint exactly on target graduation.

### Speedometer
`ป.4 อ่านหน้าปัดความเร็วรถ 0–120 km/h ขีดละ 10 km/h 10 ข้อ ไม่มีเฉลย`

Expected 12 intervals / 13 positions, 240° active arc, 120° inactive gap and exact needle mapping.

### Graduated container
`ป.4 อ่านปริมาตรจากภาชนะตวง 0–1000 mL ขีดละ 50 mL 10 ข้อ ไม่มีเฉลย`

Expected 20 intervals / 21 positions and explicit level/meniscus convention.

### Graph axis
`ป.4 อ่านกราฟแท่งที่แกนตั้งเพิ่มทีละ 5 จำนวน 10 ข้อ`

Expected equal numeric increments map to equal physical spacing and bar endpoints map exactly to canonical data.

## 7. Renderer review behavior

For every learner-read instrument, the final prompt must include:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

and a review/revise loop:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

A vague `looks correct` review is not sufficient.

## 8. Prompt vs artifact QA

Passing all prompt/package gates does not prove rendered pixels.

Before actual image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

One wrong learner-read scale in an actual worksheet means `ARTIFACT_QA=FAIL` and `CLASSROOM_RELEASE=BLOCKED`.
