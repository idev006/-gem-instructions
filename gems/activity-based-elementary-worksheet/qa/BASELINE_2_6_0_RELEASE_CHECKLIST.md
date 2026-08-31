# Baseline 2.6.0-LTS Release Checklist

Status: Critical integration checklist
Applies to: `activity-based-elementary-worksheet` baseline 2.6.x

## Required SSOT set

- `GEM_INSTRUCTIONS_PRODUCTION.md` — 2.6.0-LTS
- `OUTPUT_CONTRACT.md` — 2.6.0-LTS
- `ARCHITECTURE.md` — 2.6.0-LTS
- `KB_ROUTER.md` — 2.6.0-LTS
- `KB_MANIFEST.md` — 2.6.0-LTS
- `policies/PARAMETER_POLICY.md` — 2.6.0-LTS
- `domains/DOMAIN_REGISTRY.md` — 2.6.0-LTS
- `domains/MEASUREMENT_COVERAGE_P1_P6.md`
- `domains/THAI_P3_CLOCK_RUNTIME_PROFILE.md`
- W01..W09 worker contracts
- `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md`
- `qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md`
- `qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md`
- `qa/RUNTIME_UAT_CLOCK_REGRESSION_V2_6_X.md`
- `qa/DOMAIN_RELEASE_MATRIX.md`
- applicable older actual-render regressions
- `tools/full_dry_run_suite.py`
- `tools/full_skill_matrix_suite.py`
- `tools/runtime_uat_regression_suite.py`
- `examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md`

## Worker audit

Exactly 9 base workers:

`W01_ACADEMIC_CONTENT`
`W02_TIME_CLOCK`
`W03_WEIGHT_SCALE`
`W04_LENGTH_DISTANCE`
`W05_TEMPERATURE_CAPACITY_VOLUME`
`W06_MONEY_CALENDAR_DATA`
`W07_INSTRUMENT_AUDITOR`
`W08_LAYOUT_RENDER_THAI`
`W09_QA_RELEASE`

Each declares:

`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

Worker IDs must be unique.

## Core architecture audit

Verify core contains:

- Orchestrator role
- worker routing and ownership contract
- three visibility scopes
- Student Blueprint target-leak prohibition
- measurement P1–P6 coverage
- exact unit conversion rules
- high-risk visual serialization
- canonical-label preservation
- single render-path rule
- one-page-first policy
- Thai/theme policy
- answer-key behavior
- prompt/artifact QA distinction
- runtime-critical instruction profiles
- health check
- hotfix slot 10 policy

Missing a major contract = FAIL.

## Thai P3 analog-clock runtime audit

For Thai Grade 3 analog-clock AUTO requests, verify:

- AUTO resolves to `DAY_NIGHT_PAIR` unless explicit SINGLE intent
- one question = exactly one analog clock
- exactly two blank student response fields, `กลางวัน` and `กลางคืน`
- strict half-hour intent = minute `30` only unless mixed whole-hour request is explicit
- deterministic day/night mapping
- exact numeric hand angles per renderer item
- relational wording + item-specific hard negative
- Student Blueprint contains no target time, answer pair or angles
- `ONE_PAGE_LOCK=OFF` unless exact-one-page intent is explicit
- canonical clock topology is not degraded to force page fit

Any violation = FAIL and `PROMPT_RELEASE=BLOCKED`.

## Measurement capability audit

Verify deterministic rules for:

### Time/clock
- hours/minutes/seconds relations
- elapsed/start/end/duration
- clock interpolation
- seconds hand only when explicitly taught

### Length/distance
- ruler zero/nonzero start
- mm/cm/m/km conversion
- length arithmetic/comparison
- distance total/difference/round trip/multi-segment/route comparison
- no silent speed inference

### Angle/perimeter/area
- protractor 0° baseline and active scale direction
- exact target graduation
- perimeter formulas
- supported area formulas
- perpendicular height semantics
- squared-unit conversion
- one consistent `PI_POLICY` for circle tasks

### Weight
- g/kg/ขีด relations
- weight arithmetic/conversion
- canonical dial topology

### Temperature/capacity/volume
- thermometer representability/alignment specification
- mL/L arithmetic/conversion
- meniscus convention
- rectangular-prism volume
- simple composite rectangular-prism volume
- cm³/dm³/m³ conversion
- capacity-volume relation only when explicitly taught

## Required integration gates

`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`WORKER_OWNERSHIP_QA`
`PROMPT_ACADEMIC_DATA_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`
`PROMPT_UNIT_COMPATIBILITY_QA` when applicable
`PROMPT_UNIT_CONVERSION_QA` when applicable
`PROMPT_TIME_UNIT_CONVERSION_QA` when applicable
`PROMPT_CLOCK_MODE_RESOLUTION_QA` when clock mode applies
`PROMPT_HALF_HOUR_INTENT_QA` when strict half-hour applies
`PROMPT_DAY_NIGHT_MAPPING_QA` when paired mode applies
`PROMPT_DAY_NIGHT_SINGLE_FACE_QA` when paired mode applies
`PROMPT_DAY_NIGHT_TWO_BLANKS_QA` when paired mode applies
`PROMPT_PER_ITEM_RENDER_STATE_QA` for learner-read visuals
`PROMPT_PAGE_LOCK_PROVENANCE_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA` when applicable
`PROMPT_PROTRACTOR_BASELINE_QA` when applicable
`PROMPT_AREA_FORMULA_QA` when applicable
`PROMPT_AREA_UNIT_CONVERSION_QA` when applicable
`PROMPT_PI_POLICY_QA` when applicable
`PROMPT_CUBIC_UNIT_CONVERSION_QA` when applicable
`RENDER_PATH_RESOLVED_QA`
`PROMPT_ONE_PAGE_FEASIBILITY_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`NO_PLACEHOLDER_QA`
`STUDENT_VISIBLE_ANSWER_LEAK_QA`
`STUDENT_VISIBLE_TARGET_TEXT_LEAK_QA`
`CANONICAL_LABEL_PRESERVATION_QA`
plus owning-worker/domain gates.

## Executable release gate

A build candidate is eligible only when all current suites pass:

1. `tools/full_dry_run_suite.py` → `449/449 PASS`
2. `tools/full_skill_matrix_suite.py` → `360/360 PASS`
3. `tools/runtime_uat_regression_suite.py` → `12/12 PASS`

Combined minimum:

`821/821 PASS`

A real UAT defect must be represented by a permanent regression before the next accepted release artifact. Never lower the case count to make a release pass.

## High-risk smoke tests

1. Thai P3 half-hour clock AUTO → DAY_NIGHT_PAIR, one face, two blanks, minute 30 only, page lock OFF unless explicit.
2. 10:30 clock → minute 180°, hour 315°, midpoint 10–11, not on 10.
3. Time conversion → 2 h 5 min 30 s = 7530 s; no automatic seconds hand.
4. Canonical 0–5 kg dial → 300° active +60° gap, 50/51 topology, no 360° substitution.
5. Ruler 1 cm @1 mm → 10 intervals/11 positions.
6. Nonzero ruler start → `end-start`.
7. Distance round trip → double only when same route explicit.
8. Protractor 0–180° @1° → 180 intervals/181 positions; active baseline/scale explicit.
9. Triangle area → use perpendicular height.
10. 1 m² → 10,000 cm²; reject ×100.
11. 20–120°F @2°F → only 20+2k discrete targets.
12. Bottom/top meniscus → designated read point exact and no target-number annotation.
13. Rectangular prism → compatible units before `l×w×h`.
14. 1 m³ → 1,000,000 cm³; reject linear-factor conversion.
15. Student Blueprint → no renderer target values.
16. Final prompt → one resolved render path.
17. Before image inspection → `ARTIFACT_QA=NOT_YET_TESTED`.

## Prompt/artifact boundary

Passing this checklist means the **prompt-generation baseline** is internally coherent. It does not mean third-party rendered worksheets are classroom-ready.

Before artifact inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

## Installation package audit

Compact package must contain:

- one main Instructions `.txt`
- exactly nine worker `.txt` Knowledge files
- no `.md` dependency required for Gemini upload
- install/health-check guide
- smoke tests
- SSOT validation report
- core dry-run report
- full skill-matrix report
- runtime UAT regression report
- checksum manifest

Knowledge slot 10 remains free unless an approved narrow hotfix is shipped.

## Release decision

Baseline 2.6.0 prompt-generation release may be marked READY only when static consistency, worker compatibility, all `821` current regression cases, package integrity and SSOT/package coherence pass with zero critical blockers.
