# activity-based-elementary-worksheet

Version: 2.6.0-LTS

Production Gem for generating **verified, copy-ready worksheet image prompts** for primary-school learning materials.

## Product role

`PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

Primary deliverable:

`FINAL_IMAGE_GENERATION_PROMPT`

The Gem is an **Orchestrator**. It routes requests to Specialist Worker knowledge, validates academic content/measurement rules, separates student-visible content from renderer-only metadata, resolves layout/render strategy, and releases a self-contained downstream prompt.

It does not claim the final image has passed visual QA until the artifact is actually inspected.

## Nine Specialist Workers

- `W01_ACADEMIC_CONTENT` — arithmetic, color-by-code, Thai literacy, generic content
- `W02_TIME_CLOCK` — elapsed time and analog clock
- `W03_WEIGHT_SCALE` — weight calculation/conversion and dial scale
- `W04_LENGTH_DISTANCE` — ruler, length, distance, metric conversion
- `W05_TEMPERATURE_CAPACITY_VOLUME` — thermometer, capacity, meniscus, volume
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
- `workers/` — W01..W09 contracts
- `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md`
- `qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md`
- `qa/BASELINE_2_6_0_RELEASE_CHECKLIST.md`
- `qa/DOMAIN_RELEASE_MATRIX.md`
- `USER_GUIDE.md`
- `GEM_INSTALLATION_GUIDE.md`

GitHub is the project SSOT. Installation ZIPs must be generated from these rules and must not become a newer competing specification.

## Measurement coverage

Baseline 2.6.x formally supports:

- analog clock reading
- elapsed-time/start-end-duration calculation
- ruler reading including nonzero starts
- length arithmetic/comparison
- mm/cm/m/km conversion
- distance totals, differences, round trips, multi-segment and route comparison
- dial weight reading
- g/kg/ขีด arithmetic/conversion
- thermometer reading
- mL/L capacity reading/arithmetic/conversion
- scientific meniscus when explicitly requested
- rectangular-prism volume and simple composite rectangular-prism volume when grade-appropriate

See `domains/MEASUREMENT_COVERAGE_P1_P6.md`.

## Exact measurement relations

Length:

`10 mm=1 cm`, `100 cm=1 m`, `1000 m=1 km`

Weight:

`1000 g=1 kg`; Thai elementary context where appropriate: `1 ขีด=100 g=0.1 kg`

Capacity:

`1000 mL=1 L`

When explicitly taught:

`1 cm³=1 mL`, `1000 cm³=1 L`

Mixed-unit arithmetic normalizes to one base unit before calculation.

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

The compact production package uses one Orchestrator Instructions text plus exactly 9 Knowledge worker `.txt` files, leaving slot 10 free for a narrow hotfix.