# KB Router — Activity-Based Elementary Worksheet Generator

Version: 2.6.0-LTS
Compatible Gem baseline: 2.6.x
Status: Canonical worker-routing policy

## 1. Purpose

Route each request to the smallest complete Specialist Worker set. Do not blend every Knowledge file indiscriminately.

## 2. Base worker set

Required production installation:

- `W01_ACADEMIC_CONTENT`
- `W02_TIME_CLOCK`
- `W03_WEIGHT_SCALE`
- `W04_LENGTH_DISTANCE`
- `W05_TEMPERATURE_CAPACITY_VOLUME`
- `W06_MONEY_CALENDAR_DATA`
- `W07_INSTRUMENT_AUDITOR`
- `W08_LAYOUT_RENDER_THAI`
- `W09_QA_RELEASE`

Optional slot 10: `W10_HOTFIX_OVERRIDE`.

W08 and W09 apply to every production request. W07 applies only when learner-read geometry/axis/instrument state carries academic meaning.

## 3. Route table

| Request family | Worker route |
|---|---|
| arithmetic / number operations | W01 + W08 + W09 |
| color-by-code arithmetic | W01 + W08 + W09 |
| Thai literacy / spelling | W01 + W08 + W09 |
| elapsed time / start-end-duration | W02 + W08 + W09 |
| analog clock reading | W02 + W07 + W08 + W09 |
| weight arithmetic/comparison/conversion | W03 + W08 + W09 |
| dial scale reading | W03 + W07 + W08 + W09 |
| length arithmetic/conversion | W04 + W08 + W09 |
| distance total/difference/round trip | W04 + W08 + W09 |
| ruler reading | W04 + W07 + W08 + W09 |
| temperature calculation/conversion context | W05 + W08 + W09 |
| thermometer reading | W05 + W07 + W08 + W09 |
| capacity arithmetic/conversion | W05 + W08 + W09 |
| graduated container / meniscus | W05 + W07 + W08 + W09 |
| rectangular-prism volume | W05 + W08 + W09 |
| money / calendar / tables | W06 + W08 + W09 |
| pictograph / bar graph | W06 + W08 + W09; add W07 when exact visual scale geometry is learner-read |

Mixed-domain worksheets select every owning academic worker, then W08/W09, plus W07 if any selected item contains learner-read academic geometry.

## 4. Academic ownership

- W01 owns general academic content that no more specialized worker owns.
- W02 owns time/clock formulas.
- W03 owns weight/scale formulas and unit rules.
- W04 owns ruler/length/distance and length-unit conversion.
- W05 owns temperature/capacity/volume and related unit rules.
- W06 owns money/calendar/data mappings.
- W07 audits shared geometry but does not invent domain target values.
- W08 owns layout/render/Thai/print/theme, not academic formulas.
- W09 owns integration/release QA, not academic formulas.

`WORKER_OWNERSHIP_QA=FAIL` if a worker overrides another worker's owned academic rule without an explicit compatible hotfix.

## 5. Measurement routes

Measurement coverage is documented in `domains/MEASUREMENT_COVERAGE_P1_P6.md`.

Examples:

- `อ่านไม้บรรทัด` → W04 + W07 + W08 + W09
- `บวกความยาว 2 เมตร 35 เซนติเมตร` → W04 + W08 + W09
- `ระยะทางไปกลับ` → W04 + W08 + W09
- `แปลง 3.2 กิโลเมตรเป็นเมตร` → W04 + W08 + W09
- `อ่านนาฬิกา 10:30` → W02 + W07 + W08 + W09
- `หาระยะเวลา` → W02 + W08 + W09
- `อ่านตราชั่ง kg/ขีด` → W03 + W07 + W08 + W09
- `แปลง kg เป็น g` → W03 + W08 + W09
- `อ่าน 750 mL` → W05 + W07 + W08 + W09
- `แปลง L เป็น mL` → W05 + W08 + W09
- `ปริมาตรทรงสี่เหลี่ยมมุมฉาก` → W05 + W08 + W09

## 6. Precedence

When rules conflict:

1. explicit valid user requirement, unless academically unsafe/contradictory
2. `GEM_INSTRUCTIONS_PRODUCTION.md` for product/global architecture
3. `domains/DOMAIN_REGISTRY.md` for domain and maturity
4. owning Specialist Worker for academic rules
5. W07 for cross-instrument geometry invariants
6. `policies/PARAMETER_POLICY.md` for defaults
7. W08 for layout/render/Thai/print
8. `OUTPUT_CONTRACT.md` for packaging
9. W09/QA suites for release gating
10. user guide/README for explanation only

QA may make release stricter but may not redefine an owning worker's formula.

## 7. High-risk visual route

Learner-read visual items require:

`PER_ITEM_RENDER_STATE_REQUIRED=YES`
`TARGET_ALIGNMENT_REQUIRED=YES`

Each item state:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Mark renderer-only data `RENDER_ONLY_NOT_FOR_WORKSHEET`.

## 8. Hotfix route

W10 may override one narrow rule only when it declares:

`HOTFIX_ID`
`APPLIES_TO_BASELINE=2.6.x`
`SCOPE`
`TARGET_WORKER`
`REPLACED_RULE`
`NEW_RULE`
`REGRESSION_TEST`

Reject broad hotfixes that alter architecture, visibility model, worker schema, or multiple unrelated domains.

## 9. Routing QA

`KB_ROUTE_QA=PASS` only if:

- primary/mixed domains are correctly detected;
- all owning workers are selected;
- W07 is present for learner-read geometry;
- W08/W09 are present;
- no unrelated worker overrides the route;
- precedence is respected.

`KB_COMPATIBILITY_QA=PASS` only if installed worker IDs/schema/baseline match `KB_MANIFEST.md`.