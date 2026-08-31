# activity-based-elementary-worksheet

Version: 2.6.0-LTS

Production Gem for generating **verified, copy-ready worksheet image prompts** for primary-school learning materials.

## Product role

`PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

Primary deliverable:

`FINAL_IMAGE_GENERATION_PROMPT`

The Gem is an **Orchestrator**. It routes requests to Specialist Workers, validates academic/measurement rules, separates student-visible content from renderer-only metadata, resolves layout/render strategy, and releases a self-contained downstream prompt.

It does not claim the final image has passed visual QA until the actual artifact is inspected.

## Current release gate

Baseline 2.6.x release builds are blocked unless all executable prompt-system suites pass:

- core deterministic/policy dry-run: `449/449`
- declared-skill matrix: `360/360`
- runtime UAT regression: `12/12`
- combined minimum gate: `821/821 PASS`

CI must also pass SSOT validation, package build, ZIP integrity verification and artifact upload.

A real UAT defect must be converted into a permanent regression case before the next release artifact is accepted.

## Nine Specialist Workers

- `W01_ACADEMIC_CONTENT` — arithmetic, color-by-code, Thai literacy, generic content
- `W02_TIME_CLOCK` — time units/calculation and analog clock
- `W03_WEIGHT_SCALE` — weight calculation/conversion and dial scale
- `W04_LENGTH_DISTANCE` — ruler, length, distance, angle/protractor, perimeter, area
- `W05_TEMPERATURE_CAPACITY_VOLUME` — thermometer, capacity, meniscus, solid volume
- `W06_MONEY_CALENDAR_DATA` — money, calendar, tables/graphs
- `W07_INSTRUMENT_AUDITOR` — shared geometry/topology audit
- `W08_LAYOUT_RENDER_THAI` — layout, render path, Thai/text, print/theme
- `W09_QA_RELEASE` — integration QA and release

Knowledge slot 10 is intentionally reserved for a narrow compatible hotfix.

## Canonical SSOT files

- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `OUTPUT_CONTRACT.md`
- `ARCHITECTURE.md`
- `KB_ROUTER.md`
- `KB_MANIFEST.md`
- `policies/PARAMETER_POLICY.md`
- `domains/DOMAIN_REGISTRY.md`
- `domains/MEASUREMENT_COVERAGE_P1_P6.md`
- `domains/THAI_P3_CLOCK_RUNTIME_PROFILE.md`
- `workers/` — W01..W09 contracts
- `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md`
- `qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md`
- `qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md`
- `qa/RUNTIME_UAT_CLOCK_REGRESSION_V2_6_X.md`
- `qa/BASELINE_2_6_0_RELEASE_CHECKLIST.md`
- `qa/DOMAIN_RELEASE_MATRIX.md`
- `tools/full_dry_run_suite.py`
- `tools/full_skill_matrix_suite.py`
- `tools/runtime_uat_regression_suite.py`
- `examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md`
- `USER_GUIDE.md`
- `GEM_INSTALLATION_GUIDE.md`

GitHub is the project SSOT. Installation packages must be generated from these rules and must not become a newer competing specification.

## Formal measurement coverage P1–P6

Baseline 2.6.x supports, when grade/objective appropriate:

### Time
- analog clock reading
- elapsed/start/end/duration calculation
- hours/minutes/seconds conversion
- schedules/day-night/midnight policy

### Length / distance / measurement geometry
- ruler reading including nonzero starts
- length arithmetic/comparison
- mm/cm/m/km conversion
- distance total/difference/round trip/multi-segment/route comparison
- angle/protractor reading
- perimeter
- supported elementary area formulas
- squared-unit conversion and consistent circle π policy

### Weight
- dial reading
- g/kg/ขีด arithmetic/conversion

### Temperature / capacity / volume
- thermometer reading
- mL/L capacity reading/arithmetic/conversion
- scientific meniscus when explicitly requested
- rectangular-prism/simple composite rectangular-prism volume
- cm³/dm³/m³ conversion
- capacity-volume relations only when explicitly taught

See `domains/MEASUREMENT_COVERAGE_P1_P6.md`.

Speed/rate is not silently inferred from distance.

## Thai P3 analog-clock runtime profile

For a Thai Grade 3 analog-clock request in AUTO mode, such as:

`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ไม่มีเฉลย`

canonical runtime behavior is:

- `CLOCK_READING_MODE=DAY_NIGHT_PAIR`
- one analog clock per question
- exactly two blank response fields: `กลางวัน` and `กลางคืน`
- strict half-hour intent means minute `30` only unless the teacher explicitly requests mixed whole-hour items
- deterministic day/night mapping
- exact numeric hand angles + relational wording + item-specific hard negative in renderer-only state
- no target time/angles inside Student Blueprint
- `ONE_PAGE_LOCK=OFF` unless the teacher explicitly requires exactly one page
- canonical instructional topology must not be degraded merely to force page fit

## Exact core relations

Time: `60 s=1 min`, `60 min=1 h`, `24 h=1 day`

Length: `10 mm=1 cm`, `100 cm=1 m`, `1000 m=1 km`

Area: `1 m²=10,000 cm²`, `1 km²=1,000,000 m²`

Weight: `1000 g=1 kg`; Thai context where appropriate `1 ขีด=100 g=0.1 kg`

Capacity: `1000 mL=1 L`

Volume: `1000 cm³=1 dm³`, `1000 dm³=1 m³`, `1 m³=1,000,000 cm³`

When explicitly taught: `1 cm³=1 mL`, `1 dm³=1 L`, `1 m³=1000 L`

Mixed-unit arithmetic normalizes to compatible units before calculation. Area conversions square linear factors; cubic conversions cube them.

## Three visibility scopes

- `INTERNAL_VERIFIED_STATE` — hidden answers/calculations
- `TEACHER_VISIBLE_PROMPT_METADATA` — renderer-only geometry/targets needed to draw correctly
- `STUDENT_VISIBLE_WORKSHEET` — learner-facing content only

Student Blueprint must not expose renderer target values/angles/tick indices/levels.

## High-risk visual rule

Every learner-read high-risk visual item uses:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Known guards include:

- clock 10:30 → minute 180°, hour 315°, midpoint 10–11, not on 10
- canonical 0–5 kg dial → 300° active + 60° gap, 50 intervals/51 positions, no 360° substitution
- ruler 1 cm @1 mm → 10 intervals/11 positions
- protractor → exact origin/0° baseline/active scale direction/target graduation
- discrete thermometer/capacity target → exact valid graduation
- meniscus → explicit read point; no target-number annotation

## Output and render path

Default:

`OUTPUT_MODE=PROMPT_PACKAGE`
`PRIMARY_DELIVERABLE=FINAL_IMAGE_GENERATION_PROMPT`

`RENDER_PATH=AUTO` is input-only and must resolve before release to exactly one:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

## One-page policy

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

Correctness, minimum educational geometry, readable Thai and writable answer space outrank one-page density.

## QA phase boundary

Before downstream artifact inspection:

`PROMPT_RELEASE=APPROVED` may be valid when prompt gates pass, but:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

`PROMPT_QA != ARTIFACT_QA`.

## Installation

See `GEM_INSTALLATION_GUIDE.md`.

Compact production installation uses one Orchestrator Instructions text plus exactly 9 Knowledge worker `.txt` files, leaving slot 10 free for a narrow hotfix.