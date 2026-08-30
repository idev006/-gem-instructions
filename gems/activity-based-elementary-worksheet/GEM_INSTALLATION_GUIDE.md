# Gem Installation Guide — activity-based-elementary-worksheet

Version: 2.6.0-LTS
Target Gem baseline: 2.6.x
Installation profile: Orchestrator + 9 Specialist Workers

## 1. Main Instructions

Use the complete contents of:

`GEM_INSTRUCTIONS_PRODUCTION.md`

in the Gem **Instructions** field.

Do not shorten it into a domain formula dump. The main file is the Orchestrator: route, visibility, integration, output contract and release policy.

## 2. Knowledge upload — exactly 9 base files

Upload the compact `.txt` forms generated from these repository worker SSOT files:

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

Do not separately upload all domain/core/QA repository files when using the compact 9-worker package; the installation package consolidates the necessary operational rules.

## 3. Health check after installation

Send:

`ตรวจสุขภาพ Gem`

Expected:

- baseline 2.6.x
- W01..W09 present
- all worker schema versions = 1
- W10 absent unless an approved hotfix is installed
- `KB_COMPATIBILITY_QA=PASS`
- `INSTALLATION_HEALTH=PASS`

The health check should not generate a worksheet unless requested separately.

## 4. Measurement smoke tests

### A — elapsed time

`ป.3 หาระยะเวลาจากเวลาเริ่มต้นและเวลาสิ้นสุด 10 ข้อ ไม่มีเฉลย`

Expected: W02+W08+W09; deterministic time relations; one resolved render path; no answer leak.

### B — clock half-hour regression

`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ไม่มีเฉลย`

For 10:30 final renderer state must include:

- minute hand 180° / at 6
- hour hand 315°
- exactly halfway between 10 and 11
- hard negative: not directly on 10
- clock numerals preserved

Student Blueprint must not print target times/angles.

### C — ruler

`ป.3 อ่านไม้บรรทัด เซนติเมตรและมิลลิเมตร 10 ข้อ ไม่มีเฉลย`

Expected:

- 1 cm @1 mm = 10 intervals / 11 positions
- zero graduation distinct from physical edge
- exact endpoint mapping
- no target length/tick index in Student Blueprint

### D — nonzero ruler start

`ป.4 วัดความยาวจากไม้บรรทัดโดยวัตถุไม่ได้เริ่มที่ 0 จำนวน 10 ข้อ`

Expected verified relation `length=end-start`, not `length=end`.

### E — distance

`ป.4 คำนวณระยะทางรวมและระยะทางไปกลับ หน่วยเมตรและกิโลเมตร 10 ข้อ`

Expected unit normalization before arithmetic; round-trip doubling only when same route is explicit.

### F — canonical scale

`ป.3 อ่านตราชั่ง 0–5 กก. ขีดละ 0.1 กก. 10 ข้อ ไม่มีเฉลย`

Expected:

- 300° active + 60° inactive gap
- 50 intervals / 51 positions
- no ticks in gap
- no 360° substitution
- labels 0–5 preserved

### G — weight conversion

`ป.4 แปลงและคำนวณกิโลกรัมกับกรัม 10 ข้อ`

Expected exact `1000 g=1 kg`; normalize before calculation.

### H — thermometer

`ป.5 อ่านเทอร์โมมิเตอร์ 20–120°F ขีดย่อย 2°F 10 ข้อ`

Expected targets only `20+2k`; endpoint specification exactly on valid graduation.

### I — capacity

`ป.4 คำนวณและแปลงลิตรกับมิลลิลิตร 10 ข้อ`

Expected exact `1000 mL=1 L`; mixed units normalized before arithmetic.

### J — meniscus

Request explicit bottom/top convention. Expected unambiguous curve/read point and no target-number annotation.

### K — rectangular-prism volume

`ป.5 ปริมาตรทรงสี่เหลี่ยมมุมฉาก 10 ข้อ`

Expected compatible dimension units before `V=l×w×h`.

### L — arithmetic/color-by-code

Test W01 to ensure measurement expansion did not regress general worksheet behavior.

## 5. Prompt/artifact boundary

After Gem generates a prompt and before any downstream image is inspected:

`PROMPT_RELEASE=APPROVED` may be valid.

But it must still report:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Prompt QA does not guarantee third-party pixels.

## 6. Update policy

Baseline 2.6.x is an LTS-style installation.

For a narrow future defect, prefer one slot-10 hotfix file with:

`HOTFIX_ID`
`APPLIES_TO_BASELINE=2.6.x`
`TARGET_WORKER`
`SCOPE`
`REPLACED_RULE`
`NEW_RULE`
`REGRESSION_TEST`

Full reinstall should be reserved for worker-schema, architecture/routing, visibility/output-contract, or multi-domain critical changes.

## 7. Source of truth

GitHub repository `idev006/-gem-instructions`, folder `gems/activity-based-elementary-worksheet`, is the project SSOT.

Installation ZIPs must be generated from this SSOT. A ZIP must not become a competing specification newer than GitHub.