# Domain Registry — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
Status: Canonical SSOT for domain routing and overall maturity
Compatible Gem baseline: 2.6.x

This file is the single source of truth for domain routing and overall domain maturity. Specialist workers own academic rules; this registry owns route names and maturity. If a worker/engine header disagrees with this registry, this registry wins and the mismatch is a governance defect.

| Domain | Question family | Owning worker | Visual auditor | Maturity |
|---|---|---|---|---|
| ACADEMIC_CONTENT | arithmetic/color-by-code/Thai literacy/generic content | W01 | optional | PRODUCTION_CANDIDATE |
| TIME | elapsed time/start-end-duration/time-unit conversion/schedule | W02 | no | PRODUCTION_CANDIDATE |
| TIME_CLOCK | analog clock reading/day-night | W02 | W07 | PRODUCTION_CANDIDATE |
| MEASUREMENT_WEIGHT | weight arithmetic/conversion/dial reading | W03 | W07 for dial | PRODUCTION_CANDIDATE |
| MEASUREMENT_LENGTH | ruler reading/length arithmetic/conversion | W04 | W07 for ruler | PRODUCTION_CANDIDATE |
| MEASUREMENT_DISTANCE | route/round-trip/multi-segment distance | W04 | optional | PRODUCTION_CANDIDATE |
| MEASUREMENT_SPEEDOMETER | direct vehicle speedometer reading in km/h | W04 | W07 | PRODUCTION_CANDIDATE |
| MEASUREMENT_ANGLE | angle classification/protractor reading/construction prompts | W04 | W07 for protractor | PRODUCTION_CANDIDATE |
| MEASUREMENT_PERIMETER_AREA | perimeter/area/circle measurement and squared-unit conversion | W04 | optional; W07 when learner-read geometry is encoded | PRODUCTION_CANDIDATE |
| MEASUREMENT_TEMPERATURE | thermometer reading/temperature comparison/change | W05 | W07 for thermometer | PRODUCTION_CANDIDATE |
| MEASUREMENT_CAPACITY | mL/L reading/arithmetic/conversion/meniscus | W05 | W07 for graduated container | PRODUCTION_CANDIDATE |
| MEASUREMENT_VOLUME | rectangular-prism/simple composite volume/cubic-unit conversion | W05 | optional | PRODUCTION_CANDIDATE |
| MONEY | shopping/coins/notes/change | W06 | optional | PRODUCTION_CANDIDATE |
| CALENDAR | dates/days/months | W06 | optional | PRODUCTION_CANDIDATE |
| DATA_READING | tables/pictographs/bar graphs | W06 | W07 when exact scale/axis geometry matters | PRODUCTION_CANDIDATE |
| WORD_PROBLEM_GENERIC | real-life word problems without specialized owner | W01 | optional | SUPPORTED_GENERIC |

## Routing examples

- `หาระยะเวลา`, `เวลาเริ่มต้น/สิ้นสุด`, `แปลงชั่วโมง นาที วินาที` → TIME
- `อ่านนาฬิกาเข็ม` → TIME_CLOCK
- `อ่านตราชั่ง`, `kg/ขีด`, `แปลง kg/g` → MEASUREMENT_WEIGHT
- `อ่านไม้บรรทัด`, `cm/mm`, `บวกความยาว`, `แปลง mm/cm/m/km` → MEASUREMENT_LENGTH
- `ระยะทางไปกลับ`, `ระยะทางรวมหลายช่วง`, `เปรียบเทียบเส้นทาง` → MEASUREMENT_DISTANCE
- `อ่านหน้าปัดความเร็วรถ`, `อ่านมาตรวัดความเร็ว`, `speedometer reading` → MEASUREMENT_SPEEDOMETER
- `อ่านมุมจากโพรแทรกเตอร์`, `จำแนกมุม` → MEASUREMENT_ANGLE
- `รอบรูป`, `พื้นที่`, `พื้นที่วงกลม`, `แปลงหน่วยพื้นที่` → MEASUREMENT_PERIMETER_AREA
- `เทอร์โมมิเตอร์`, `อ่านอุณหภูมิ` → MEASUREMENT_TEMPERATURE
- `อ่านระดับน้ำ`, `L/mL`, `เมนิสคัส` → MEASUREMENT_CAPACITY
- `ปริมาตรทรงสี่เหลี่ยมมุมฉาก`, `แปลง cm³/dm³/m³` → MEASUREMENT_VOLUME
- `ซื้อของ`, `เงินทอน` → MONEY
- `วัน เดือน วันที่`, `ปฏิทิน` → CALENDAR
- `ตาราง`, `แผนภูมิรูปภาพ`, `กราฟแท่ง` → DATA_READING

## Measurement family

Formal P1–P6 capability/progression guidance lives in `MEASUREMENT_COVERAGE_P1_P6.md`.

The measurement family includes direct instrument reading and deterministic calculation/conversion. Do not route specialized measurement problems to generic content when W02–W06 owns the rule.

Direct speedometer reading is supported by `SPEEDOMETER_READING_ENGINE.md`. This does **not** automatically enable speed/rate calculation from distance/time. Do not silently infer `speed=distance/time` from a speedometer-reading request.

## Learner-read instrument architecture

Every learner-read instrument/axis must inherit:

- `domains/INSTRUMENT_READING_ENGINE.md`
- `policies/SCALE_LINE_INTEGRITY_PROFILE.md` when graduations/ticks/axis intervals are read
- `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`

Required route includes W07 + W10 + W08 + W09.

The renderer-side self-review loop is a prevention layer only; actual pixel correctness remains artifact QA.

## Routing validation

Before prompt release:

1. normalized topic resolves to one primary domain or explicit mixed-domain plan;
2. owning worker is installed and compatible;
3. W07 is selected when learner-read geometry carries academic data;
4. W10 independently audits metrology/common-center/page feasibility for learner-read geometry;
5. W08/W09 are selected;
6. mandatory shared instrument profiles are available when applicable;
7. `KB_ROUTE_QA=PASS`;
8. `KB_COMPATIBILITY_QA=PASS`.

## Maturity rule

`PRODUCTION_HARDENED` requires deterministic academic rules, domain QA, regression evidence and release evidence documented in `qa/DOMAIN_RELEASE_MATRIX.md`.

`PRODUCTION_CANDIDATE` has deterministic rules/QA but has not yet met all artifact-evidence thresholds.

`SUPPORTED_GENERIC` must not claim specialized deterministic guarantees it does not own.

Prompt maturity and artifact maturity are separate. A strong prompt rule or renderer self-review instruction does not by itself prove classroom-ready pixels.

## Actual-render hardening

Known high-risk families include:

- clock hour-hand interpolation / minute-mark count
- canonical dial full-circle substitution / gap ticks
- ruler extra/missing graduation, border-as-tick and start-reference errors
- speedometer active-arc/needle/extra-tick errors
- protractor baseline/inner-outer scale ambiguity
- thermometer between-tick endpoints, wrong graduation count/direction
- capacity/meniscus read-point ambiguity and target-number leakage
- graph-axis scale distortion

These failures are converted into permanent prompt and artifact regressions. One wrong learner-read scale blocks classroom release.


## All-skills runtime invariant

Every routed skill inherits `policies/ALL_SKILLS_RUNTIME_INVARIANT_PROFILE.md`.

Canonical state is owned by the specialist worker. Downstream audit/layout/release layers may reject or constrain output but may not redefine the academic oracle.
