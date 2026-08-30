# Domain Registry — Activity-Based Elementary Worksheet Generator

Version: 2.2.1
Status: Canonical SSOT for domain routing and maturity

This file is the single source of truth for domain routing and **overall domain maturity**. If an engine header disagrees with this registry, the registry wins and the mismatch is a release-blocking governance defect that must be repaired.

| Domain | Question family | Engine | Maturity |
|---|---|---|---|
| TIME | elapsed time / start-end-duration transformations | `TIME_ENGINE.md` | PRODUCTION_HARDENED |
| MEASUREMENT_WEIGHT | dial scale reading | `SCALE_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| TIME_CLOCK | analog clock reading, including one-clock day/night paired reading | `CLOCK_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| MEASUREMENT_LENGTH | ruler/length reading | `LENGTH_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| MEASUREMENT_TEMPERATURE | thermometer reading | `TEMPERATURE_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| MEASUREMENT_CAPACITY | graduated container reading | `CAPACITY_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| MONEY | shopping/coins/notes/change | `MONEY_ENGINE.md` | PRODUCTION_CANDIDATE |
| CALENDAR | dates/days/months | `CALENDAR_ENGINE.md` | PRODUCTION_CANDIDATE |
| DATA_READING | tables/pictographs/bar graphs | `TABLE_GRAPH_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| WORD_PROBLEM_GENERIC | real-life word problems | core only | SUPPORTED_GENERIC |

## Routing examples

- `การหาระยะเวลา`, `เวลาเริ่มต้น/สิ้นสุด`, `เวลาเริ่ม + ระยะเวลา`, `เวลาสิ้นสุด - ระยะเวลา` → TIME
- `การอ่านตราชั่ง`, `กิโลกรัมและขีด` → MEASUREMENT_WEIGHT
- `อ่านนาฬิกาเข็ม` → TIME_CLOCK
- `อ่านนาฬิกากลางวันและกลางคืนจากหน้าปัดเดียว` → TIME_CLOCK with `CLOCK_READING_MODE=DAY_NIGHT_PAIR`
- `อ่านไม้บรรทัด`, `เซนติเมตร/มิลลิเมตร` → MEASUREMENT_LENGTH
- `อ่านอุณหภูมิ`, `เทอร์โมมิเตอร์` → MEASUREMENT_TEMPERATURE
- `อ่านระดับน้ำ`, `ลิตร/มิลลิลิตร` → MEASUREMENT_CAPACITY
- `ซื้อของ`, `รวมเงิน`, `เงินทอน` → MONEY
- `วัน เดือน วันที่`, `ปฏิทิน` → CALENDAR
- `อ่านตาราง`, `แผนภูมิรูปภาพ`, `กราฟแท่ง` → DATA_READING

## Maturity rule

`PRODUCTION_HARDENED` requires deterministic generation/validation, domain-specific QA, regression evidence, and the evidence threshold in `qa/DOMAIN_RELEASE_MATRIX.md`.

`PRODUCTION_CANDIDATE` has deterministic rules and QA design but still requires broader actual-render regression before promotion.

`SUPPORTED_GENERIC` may use the core pipeline but must not claim domain-specific deterministic guarantees that do not exist.

The Gem MUST include the maturity status in QA whenever the domain is not hardened.

## Path-specific evidence rule

Overall maturity is not the same as render-path evidence. A candidate domain may have a strong deterministic-vector/overlay path while a generative-only path remains weak. The QA report may state path-specific evidence, but MUST NOT upgrade the overall maturity unless the promotion rule is satisfied.

## Scale-reading note

`MEASUREMENT_WEIGHT` was deliberately returned to `PRODUCTION_CANDIDATE` after real rendered examples exposed systemic dial defects. The deterministic-overlay path now has strong evidence, but the overall domain remains candidate until the release matrix promotion rule is met. Engine headers and teacher-facing reports must not call the overall domain hardened.
