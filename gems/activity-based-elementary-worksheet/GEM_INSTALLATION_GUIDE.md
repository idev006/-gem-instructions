# Gem Installation Guide — activity-based-elementary-worksheet

Version: 2.6.0-LTS
Target Gem baseline: 2.6.x
Installation profile: Orchestrator + 9 Specialist Workers

## 1. Main Instructions

Use the complete contents of:

`GEM_INSTRUCTIONS_PRODUCTION.md`

in the Gem **Instructions** field.

The main file is the Orchestrator: route, visibility, integration, output contract and release policy. Do not replace it with a shortened formula dump.

The Orchestrator also contains runtime-critical profiles that must be visible at instruction level, including Thai Grade 3 analog-clock AUTO behavior.

## 2. Knowledge upload — exactly 9 base files

Upload compact `.txt` forms generated from:

1. `workers/W01_ACADEMIC_CONTENT.md`
2. `workers/W02_TIME_CLOCK.md`
3. `workers/W03_WEIGHT_SCALE.md`
4. `workers/W04_LENGTH_DISTANCE.md`
5. `workers/W05_TEMPERATURE_CAPACITY_VOLUME.md`
6. `workers/W06_MONEY_CALENDAR_DATA.md`
7. `workers/W07_INSTRUMENT_AUDITOR.md`
8. `workers/W08_LAYOUT_RENDER_THAI.md`
9. `workers/W09_QA_RELEASE.md`

Knowledge slot 10 remains empty by default and is reserved for `W10_HOTFIX_OVERRIDE`.

Do not separately upload all core/domain/QA repository files when using the compact package; the installable worker files consolidate operational rules.

## 3. Release artifact eligibility

Use an installation ZIP only when its source commit passed all current executable gates:

- SSOT validation
- core dry-run `449/449`
- declared-skill matrix `360/360`
- runtime UAT regression `12/12`
- combined minimum `821/821 PASS`
- package build
- ZIP integrity verification

If any gate fails or is not run, do not install that artifact as a release candidate.

## 4. Health check after installation

Send:

`ตรวจสุขภาพ Gem`

Expected:

- baseline 2.6.x
- W01..W09 present
- worker schema versions = 1
- W10 absent unless approved hotfix installed
- measurement capability family recognized
- `KB_COMPATIBILITY_QA=PASS`
- `INSTALLATION_HEALTH=PASS`

The health check should not generate a worksheet unless requested separately.

## 5. Smoke tests

### A — elapsed time
`ป.3 หาระยะเวลาจากเวลาเริ่มต้นและเวลาสิ้นสุด 10 ข้อ ไม่มีเฉลย`

Expected W02+W08+W09; deterministic time relations; one resolved render path.

### B — time units / seconds
`ป.4 แปลงชั่วโมง นาที วินาที 10 ข้อ ไม่มีเฉลย`

Expected exact 60/60/24 relations. A seconds hand must not appear unless analog-second reading is explicitly requested.

### C — Thai P3 clock half-hour runtime profile
`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ไม่มีเฉลย`

Expected canonical behavior:

- `CLOCK_READING_MODE=DAY_NIGHT_PAIR`
- exactly one analog clock per question
- exactly two student answer fields per question: `กลางวัน ........ น.` and `กลางคืน ........ น.`
- strict half-hour targets are `hh:30` only; no `:00` unless explicitly requested as a mixed worksheet
- one shared hand state supports both day/night interpretations
- renderer metadata includes exact numeric angles for every clock item
- 10:30 regression: minute 180°, hour 315°, midpoint 10–11, never directly on 10
- Student Blueprint contains no target times, answer values or angles
- `ONE_PAGE_LOCK=OFF` unless the request explicitly says exactly one page
- canonical clock topology is not reduced merely to force page fit

An output with one answer line, implicit page lock, missing numeric angles or downgraded clock topology is a runtime UAT regression and must not be accepted.

### D — ruler
`ป.3 อ่านไม้บรรทัด เซนติเมตรและมิลลิเมตร 10 ข้อ ไม่มีเฉลย`

Expected 1 cm @1 mm = 10 intervals / 11 positions; zero graduation distinct from physical edge.

### E — nonzero ruler start
`ป.4 วัดความยาวจากไม้บรรทัดโดยวัตถุไม่ได้เริ่มที่ 0 จำนวน 10 ข้อ`

Expected `length=end-start`.

### F — distance
`ป.4 คำนวณระยะทางรวมและระยะทางไปกลับ หน่วยเมตรและกิโลเมตร 10 ข้อ`

Expected normalization before arithmetic; doubling only when same route explicit; no silent speed/rate.

### G — protractor
`ป.4 อ่านมุมจากโพรแทรกเตอร์ 0–180° ขีดละ 1° 10 ข้อ ไม่มีเฉลย`

Expected 180 intervals/181 positions, exact center/vertex, one baseline ray on selected 0°, target ray on exact graduation, active inner/outer scale direction explicit.

### H — perimeter/area
`ป.4 คำนวณรอบรูปและพื้นที่สี่เหลี่ยมผืนผ้า/สี่เหลี่ยมจัตุรัส 10 ข้อ ไม่มีเฉลย`

Expected correct formula and square units.

### I — area conversion
`ป.5 แปลงตารางเมตรและตารางเซนติเมตร 10 ข้อ ไม่มีเฉลย`

Expected `1 m²=10,000 cm²`; reject linear ×100 conversion.

### J — circle π policy
`ป.6 พื้นที่และความยาวรอบวงกลม 10 ข้อ ใช้ π=3.14 ทุกข้อ ไม่มีเฉลย`

Expected one consistent π policy throughout.

### K — canonical scale
`ป.3 อ่านตราชั่ง 0–5 กก. ขีดละ 0.1 กก. 10 ข้อ ไม่มีเฉลย`

Expected 300° active +60° inactive gap, 50 intervals/51 positions, no gap ticks, no 360° substitution, labels 0–5 preserved.

### L — weight conversion
`ป.4 แปลงและคำนวณกิโลกรัมกับกรัม 10 ข้อ`

Expected `1000 g=1 kg` and unit normalization.

### M — thermometer
`ป.5 อ่านเทอร์โมมิเตอร์ 20–120°F ขีดย่อย 2°F 10 ข้อ`

Expected targets only 20+2k and exact graduation alignment specification.

### N — capacity
`ป.4 คำนวณและแปลงลิตรกับมิลลิลิตร 10 ข้อ`

Expected `1000 mL=1 L` and normalization before arithmetic.

### O — meniscus
Request explicit bottom/top convention. Expected unambiguous curve/read point and no target-number annotation.

### P — rectangular-prism volume
`ป.5 ปริมาตรทรงสี่เหลี่ยมมุมฉาก 10 ข้อ`

Expected compatible dimension units before `V=l×w×h`.

### Q — cubic conversion
`ป.6 แปลง cm³ dm³ และ m³ 10 ข้อ ไม่มีเฉลย`

Expected `1000 cm³=1 dm³`, `1000 dm³=1 m³`, `1 m³=1,000,000 cm³`; reject linear-factor conversion.

### R — arithmetic/color-by-code/Thai
Test W01 so measurement expansion does not regress general worksheet behavior.

## 6. Prompt/artifact boundary

After Gem generates a prompt and before any downstream image is inspected:

`PROMPT_RELEASE=APPROVED` may be valid.

But it must still report:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Prompt QA does not guarantee third-party pixels.

## 7. Update policy

Baseline 2.6.x is LTS-style.

For a narrow future defect, prefer one slot-10 hotfix with:

`HOTFIX_ID`
`APPLIES_TO_BASELINE=2.6.x`
`TARGET_WORKER`
`SCOPE`
`REPLACED_RULE`
`NEW_RULE`
`REGRESSION_TEST`

A real UAT defect should first be repaired in canonical SSOT according to ownership and then converted to a permanent automated regression test. Do not patch only final prose.

Full reinstall should be reserved for worker-schema, architecture/routing, visibility/output-contract, runtime-instruction profile, or multi-domain critical changes.

## 8. Source of truth

GitHub repository `idev006/-gem-instructions`, folder `gems/activity-based-elementary-worksheet`, is the project SSOT.

Installation ZIPs must be generated from this SSOT and from a successful CI run. A ZIP must not become a competing specification newer than GitHub.