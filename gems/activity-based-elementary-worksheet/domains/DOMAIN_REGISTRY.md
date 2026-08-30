# Domain Registry — Activity-Based Elementary Worksheet Generator

Version: 2.0.1

This file is the single source of truth for domain routing and maturity.

| Domain | Question family | Engine | Maturity |
|---|---|---|---|
| TIME | elapsed time | `TIME_ENGINE.md` | PRODUCTION_HARDENED |
| MEASUREMENT_WEIGHT | dial scale reading | `SCALE_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| TIME_CLOCK | analog clock reading | `CLOCK_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| MEASUREMENT_LENGTH | ruler/length reading | `LENGTH_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| MEASUREMENT_TEMPERATURE | thermometer reading | `TEMPERATURE_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| MEASUREMENT_CAPACITY | graduated container reading | `CAPACITY_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| MONEY | shopping/coins/notes/change | `MONEY_ENGINE.md` | PRODUCTION_CANDIDATE |
| CALENDAR | dates/days/months | `CALENDAR_ENGINE.md` | PRODUCTION_CANDIDATE |
| DATA_READING | tables/pictographs/bar graphs | `TABLE_GRAPH_READING_ENGINE.md` | PRODUCTION_CANDIDATE |
| WORD_PROBLEM_GENERIC | real-life word problems | core only | SUPPORTED_GENERIC |

## Routing examples

- `การหาระยะเวลา`, `เวลาเริ่มต้น/สิ้นสุด` → TIME
- `การอ่านตราชั่ง`, `กิโลกรัมและขีด` → MEASUREMENT_WEIGHT
- `อ่านนาฬิกาเข็ม` → TIME_CLOCK
- `อ่านไม้บรรทัด`, `เซนติเมตร/มิลลิเมตร` → MEASUREMENT_LENGTH
- `อ่านอุณหภูมิ`, `เทอร์โมมิเตอร์` → MEASUREMENT_TEMPERATURE
- `อ่านระดับน้ำ`, `ลิตร/มิลลิลิตร` → MEASUREMENT_CAPACITY
- `ซื้อของ`, `รวมเงิน`, `เงินทอน` → MONEY
- `วัน เดือน วันที่`, `ปฏิทิน` → CALENDAR
- `อ่านตาราง`, `แผนภูมิรูปภาพ`, `กราฟแท่ง` → DATA_READING

## Maturity rule

`PRODUCTION_HARDENED` requires deterministic generation/validation, domain-specific QA, regression evidence, and the post-render evidence threshold in `qa/DOMAIN_RELEASE_MATRIX.md`.

`PRODUCTION_CANDIDATE` has deterministic rules and QA design but still requires broader actual-render regression before promotion.

The Gem MUST include the maturity status in QA when the domain is not hardened.

## Scale-reading note

`MEASUREMENT_WEIGHT` was deliberately returned to `PRODUCTION_CANDIDATE` after real rendered examples exposed systemic dial defects (off-center needle, distorted circle/ticks/layout). The engine rules have been repaired, but it must earn promotion again through the release matrix rather than by documentation alone.