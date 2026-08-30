# Domain Registry — Activity-Based Elementary Worksheet Generator

Version: 2.3.2
Status: Canonical SSOT for domain routing and overall domain maturity
Compatible Gem baseline: 2.3.2

This file is the single source of truth for domain routing and **overall domain maturity**. `KB_ROUTER.md` may select dependencies, but it does not override this registry's domain/maturity mapping. If an engine header disagrees with this registry, the registry wins and the mismatch is a release-blocking governance defect that must be repaired.

| Domain | Question family | Required engine set | Maturity |
|---|---|---|---|
| TIME | elapsed time / start-end-duration transformations | `TIME_ENGINE.md` | PRODUCTION_CANDIDATE |
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
- `อ่านระดับน้ำ`, `ลิตร/มิลลิลิตร`, `เมนิสคัส` → MEASUREMENT_CAPACITY
- `ซื้อของ`, `รวมเงิน`, `เงินทอน` → MONEY
- `วัน เดือน วันที่`, `ปฏิทิน` → CALENDAR
- `อ่านตาราง`, `แผนภูมิรูปภาพ`, `กราฟแท่ง` → DATA_READING

## Routing validation

Before prompt release:

1. normalized topic resolves to exactly one primary domain or an explicitly supported mixed-domain plan;
2. required engine set above is present in the installed KB;
3. `KB_ROUTE_QA=PASS`;
4. `KB_COMPATIBILITY_QA=PASS` according to `KB_MANIFEST.md`.

If a visual instrument domain is selected without `INSTRUMENT_READING_ENGINE.md`, production prompt release is blocked.

## Maturity rule

`PRODUCTION_HARDENED` requires deterministic generation/validation, domain-specific QA, regression evidence, and the evidence threshold in `qa/DOMAIN_RELEASE_MATRIX.md`.

`PRODUCTION_CANDIDATE` has deterministic rules and QA design but still requires one or more release-evidence requirements before promotion.

`SUPPORTED_GENERIC` may use the core pipeline but must not claim domain-specific deterministic guarantees that do not exist.

The Gem MUST include the maturity status in QA whenever the domain is not hardened.

## Academic maturity vs overall maturity

A domain can have a mature deterministic academic core while its **overall domain status remains candidate** because render/layout evidence is incomplete. QA may report this distinction, e.g. `ACADEMIC_RULES=DETERMINISTIC_MATURE`, but must use the overall registry status for `DOMAIN_MATURITY`.

## Path-specific evidence rule

Overall maturity is not the same as render-path evidence. A candidate domain may have a strong deterministic-vector/overlay path while a generative-only path remains weak. The QA report may state path-specific evidence, but MUST NOT upgrade overall maturity unless the promotion rule is satisfied.

## Actual-render hardening note

Observed downstream failures do not automatically change maturity. They must be converted into prompt/domain regression requirements and then validated. Current actual-render failure classes include clock hour-hand interpolation, exact thermometer target alignment, meniscus reading-point/target-leak failures, and canonical 0–5 kg dial full-circle substitution. See `qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md`.

## TIME note

TIME arithmetic/validation rules are deterministic and mature, but the release matrix does not yet document the required ≥10 actual rendered worksheet audits. Therefore overall TIME remains `PRODUCTION_CANDIDATE` until that evidence is recorded.

## Scale-reading note

`MEASUREMENT_WEIGHT` remains `PRODUCTION_CANDIDATE`. Deterministic-overlay evidence is strong, but generative downstream render failures justify retaining candidate status until the release matrix promotion rule is met.