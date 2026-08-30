# Domain Registry — Activity-Based Elementary Worksheet Generator

Version: 2.6.0-LTS
Status: Canonical SSOT for domain routing and overall maturity
Compatible Gem baseline: 2.6.x

This file is the single source of truth for domain routing and **overall domain maturity**. Specialist Workers own academic rules; this registry owns route names and maturity. If a worker/engine header disagrees with this registry, this registry wins and the mismatch is a governance defect.

| Domain | Question family | Owning worker | Visual auditor | Maturity |
|---|---|---|---|---|
| ACADEMIC_CONTENT | arithmetic/color-by-code/Thai literacy/generic content | W01 | optional | PRODUCTION_CANDIDATE |
| TIME | elapsed time/start-end-duration/schedule | W02 | no | PRODUCTION_CANDIDATE |
| TIME_CLOCK | analog clock reading/day-night | W02 | W07 | PRODUCTION_CANDIDATE |
| MEASUREMENT_WEIGHT | weight arithmetic/conversion/dial reading | W03 | W07 for dial | PRODUCTION_CANDIDATE |
| MEASUREMENT_LENGTH | ruler reading/length arithmetic/conversion | W04 | W07 for ruler | PRODUCTION_CANDIDATE |
| MEASUREMENT_DISTANCE | route/round-trip/multi-segment distance | W04 | optional | PRODUCTION_CANDIDATE |
| MEASUREMENT_TEMPERATURE | thermometer reading/temperature comparison | W05 | W07 for thermometer | PRODUCTION_CANDIDATE |
| MEASUREMENT_CAPACITY | mL/L reading/arithmetic/conversion/meniscus | W05 | W07 for graduated container | PRODUCTION_CANDIDATE |
| MEASUREMENT_VOLUME | rectangular-prism/simple composite volume | W05 | optional | PRODUCTION_CANDIDATE |
| MONEY | shopping/coins/notes/change | W06 | optional | PRODUCTION_CANDIDATE |
| CALENDAR | dates/days/months | W06 | optional | PRODUCTION_CANDIDATE |
| DATA_READING | tables/pictographs/bar graphs | W06 | W07 when exact scale/axis geometry matters | PRODUCTION_CANDIDATE |
| WORD_PROBLEM_GENERIC | real-life word problems without specialized owner | W01 | optional | SUPPORTED_GENERIC |

## Routing examples

- `หาระยะเวลา`, `เวลาเริ่มต้น/สิ้นสุด`, `เวลาเริ่ม + ระยะเวลา` → TIME
- `อ่านนาฬิกาเข็ม` → TIME_CLOCK
- `อ่านตราชั่ง`, `kg/ขีด` → MEASUREMENT_WEIGHT
- `บวก/ลบน้ำหนัก`, `แปลง kg/g` → MEASUREMENT_WEIGHT
- `อ่านไม้บรรทัด`, `cm/mm` → MEASUREMENT_LENGTH
- `บวกความยาว`, `แปลง mm/cm/m/km` → MEASUREMENT_LENGTH
- `ระยะทางไปกลับ`, `ระยะทางรวมหลายช่วง`, `เปรียบเทียบเส้นทาง` → MEASUREMENT_DISTANCE
- `เทอร์โมมิเตอร์` → MEASUREMENT_TEMPERATURE
- `อ่านระดับน้ำ`, `L/mL`, `เมนิสคัส` → MEASUREMENT_CAPACITY
- `ปริมาตรทรงสี่เหลี่ยมมุมฉาก` → MEASUREMENT_VOLUME
- `ซื้อของ`, `เงินทอน` → MONEY
- `วัน เดือน วันที่`, `ปฏิทิน` → CALENDAR
- `ตาราง`, `แผนภูมิรูปภาพ`, `กราฟแท่ง` → DATA_READING

## Measurement family

Formal P1–P6 capability/progression guidance lives in `MEASUREMENT_COVERAGE_P1_P6.md`.

The measurement family includes direct instrument reading and deterministic calculation/conversion. Do not route every measurement word problem to generic content when a specialized measurement worker owns the arithmetic.

## Routing validation

Before prompt release:

1. normalized topic resolves to one primary domain or explicit mixed-domain plan;
2. owning worker is installed and compatible;
3. W07 is selected when learner-read geometry carries academic data;
4. W08/W09 are selected;
5. `KB_ROUTE_QA=PASS`;
6. `KB_COMPATIBILITY_QA=PASS`.

## Maturity rule

`PRODUCTION_HARDENED` requires deterministic academic rules, domain QA, regression evidence and release evidence documented in `qa/DOMAIN_RELEASE_MATRIX.md`.

`PRODUCTION_CANDIDATE` has defined deterministic rules/QA but has not yet met all release-evidence thresholds.

`SUPPORTED_GENERIC` must not claim specialized deterministic guarantees it does not own.

Prompt QA maturity and artifact maturity are separate. A strong prompt-generation rule does not by itself promote a domain.

## Academic maturity vs overall maturity

A domain may have `ACADEMIC_RULES=DETERMINISTIC_MATURE` while overall `DOMAIN_MATURITY=PRODUCTION_CANDIDATE` because rendered-artifact evidence is incomplete.

## Path-specific evidence

Evidence must identify the tested downstream path (`DOCUMENT_FIRST`, `HYBRID`, `DETERMINISTIC_VECTOR`, `IMAGE_ONLY`). Success on one path does not automatically harden all paths.

## Actual-render hardening

Known high-risk families include:

- clock hour-hand interpolation
- canonical dial full-circle substitution
- ruler graduation/start-reference errors
- thermometer between-tick endpoints
- capacity/meniscus read-point ambiguity and target-number leakage

These failures are converted into prompt and artifact regression tests; they do not automatically change maturity status.