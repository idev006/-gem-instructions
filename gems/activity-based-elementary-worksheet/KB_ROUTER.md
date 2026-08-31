# KB Router — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
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
- `W10_METROLOGY_ENGINEER`

W08 and W09 apply to every production request. W07 and W10 both apply whenever learner-read geometry/axis/instrument state carries academic meaning.

## 3. Route table

| Request family | Worker route |
|---|---|
| arithmetic / number operations | W01 + W08 + W09 |
| color-by-code arithmetic | W01 + W08 + W09 |
| Thai literacy / spelling | W01 + W08 + W09 |
| elapsed time / start-end-duration / time-unit conversion / seconds | W02 + W08 + W09 |
| analog clock reading | W02 + W07 + W10 + W08 + W09 |
| weight arithmetic/comparison/conversion | W03 + W08 + W09 |
| dial scale reading | W03 + W07 + W10 + W08 + W09 |
| length arithmetic/conversion | W04 + W08 + W09 |
| distance total/difference/round trip/multi-segment | W04 + W08 + W09 |
| ruler reading | W04 + W07 + W10 + W08 + W09 |
| direct speedometer reading / vehicle speed dial | W04 + W07 + W10 + W08 + W09 |
| angle/protractor reading | W04 + W07 + W10 + W08 + W09 |
| perimeter/area/circle measurement | W04 + W08 + W09; add W07 + W10 when learner-read geometry is part of the question |
| temperature calculation/change context | W05 + W08 + W09 |
| thermometer reading | W05 + W07 + W10 + W08 + W09 |
| capacity arithmetic/conversion | W05 + W08 + W09 |
| graduated container / meniscus | W05 + W07 + W10 + W08 + W09 |
| rectangular-prism/simple composite volume and cubic-unit conversion | W05 + W08 + W09 |
| money / calendar / tables | W06 + W08 + W09 |
| pictograph / bar graph | W06 + W08 + W09; add W07 + W10 when exact visual scale geometry is learner-read |

Mixed-domain worksheets select every owning academic worker, then W08/W09, plus W07 + W10 if any selected item contains learner-read academic geometry.

## 4. Academic ownership

- W01 owns general academic content not owned by a specialist.
- W02 owns time-unit, elapsed-time and clock formulas.
- W03 owns weight/dial formulas and units.
- W04 owns ruler/length/distance/direct-speedometer-reading/angle/protractor/perimeter/area.
- W05 owns temperature/capacity/volume.
- W06 owns money/calendar/data mappings.
- W07 audits shared topology and scale geometry but does not invent domain targets.
- W10 independently audits metrology and printed measurement feasibility but does not invent domain targets.
- W08 owns layout/render/Thai/print/theme and serializes mandatory instrument review protocol.
- W09 owns integration/release QA, not academic formulas.

`WORKER_OWNERSHIP_QA=FAIL` if a worker overrides another worker's owned academic rule.

Direct speedometer reading is an instrument-reading skill. It must not silently activate `speed=distance/time` calculation.

## 5. Measurement routes

Examples:

- `อ่านไม้บรรทัด` → W04 + W07 + W10 + W08 + W09
- `อ่านหน้าปัดความเร็วรถ 0–120 km/h` → W04 + W07 + W10 + W08 + W09
- `อ่านมุมจากโพรแทรกเตอร์` → W04 + W07 + W10 + W08 + W09
- `อ่านนาฬิกา 10:30` → W02 + W07 + W10 + W08 + W09
- `อ่านตราชั่ง kg/ขีด` → W03 + W07 + W10 + W08 + W09
- `อ่านเทอร์โมมิเตอร์` → W05 + W07 + W10 + W08 + W09
- `อ่าน 750 mL` → W05 + W07 + W10 + W08 + W09
- `กราฟแท่งที่เด็กต้องอ่านแกนค่า` → W06 + W07 + W10 + W08 + W09

## 6. Learner-read instrument route — mandatory

Every learner-read instrument route must inherit:

- `domains/INSTRUMENT_READING_ENGINE.md`
- `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
- `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `policies/METROLOGY_ASSURANCE_PROFILE.md`

Required runtime semantics:

`PER_ITEM_RENDER_STATE_REQUIRED=YES`
`TARGET_ALIGNMENT_REQUIRED=YES`
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`
`METROLOGY_AUDIT_REQUIRED=YES`

Every high-risk item state:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL/ENDPOINT + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Mandatory audit chain:

`OWNING WORKER → W07 → W10 → W08 → W09`

W10 must produce independent quantitative evidence, not a copy of W07's conclusion.

## 7. Precedence

When rules conflict:

1. explicit valid user requirement, unless academically unsafe/contradictory
2. `GEM_INSTRUCTIONS_PRODUCTION.md`
3. `domains/DOMAIN_REGISTRY.md`
4. owning Specialist Worker/domain engine
5. `policies/SCALE_LINE_INTEGRITY_PROFILE.md` + W07
6. `policies/METROLOGY_ASSURANCE_PROFILE.md` + W10 independent audit
7. `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
8. `policies/PARAMETER_POLICY.md`
9. W08 layout/render/Thai/print
10. `OUTPUT_CONTRACT.md`
11. W09/QA suites

QA may make release stricter but may not redefine an owning worker's formula.

## 8. Base-update policy

W10 is a base production worker in 2.6.3-LTS, not a hotfix override. Architecture, scale-safety, visibility, routing or metrology changes require base SSOT changes, permanent regression, full CI and reinstall.

## 9. Routing QA

`KB_ROUTE_QA=PASS` only if:

- primary/mixed domains are correctly detected;
- all owning workers are selected;
- W07 and W10 are present for learner-read geometry;
- W08/W09 are present;
- mandatory scale/review/metrology profiles apply when needed;
- no unrelated worker overrides the route;
- precedence is respected.

`KB_COMPATIBILITY_QA=PASS` only if installed worker IDs/schema/baseline and mandatory shared profiles match `KB_MANIFEST.md`.
