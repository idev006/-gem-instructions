# W09 — QA & Release Specialist

`WORKER_ID=W09_QA_RELEASE`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Route decision, selected worker outputs, normalized spec with provenance, Student Blueprint, layout blueprint, render constraints and final prompt draft.

## OWNS

- worker compatibility/ownership validation
- integration QA
- visibility/leak QA
- prompt completeness/copy-readiness
- measurement/global regression gates
- provenance checks for locked behaviors
- prompt-vs-artifact phase semantics
- release decision
- installation health/self-check

## RETURNS

QA report, prompt-release decision, artifact phase status, classroom-release status and repair instructions when blocked.

## MUST_NOT_DECIDE

Academic formulas, domain target values, instrument topology, page design or Thai wording except detecting violations.

## Installation health

Required base worker IDs:

`W01_ACADEMIC_CONTENT`
`W02_TIME_CLOCK`
`W03_WEIGHT_SCALE`
`W04_LENGTH_DISTANCE`
`W05_TEMPERATURE_CAPACITY_VOLUME`
`W06_MONEY_CALENDAR_DATA`
`W07_INSTRUMENT_AUDITOR`
`W08_LAYOUT_RENDER_THAI`
`W09_QA_RELEASE`

Every base worker must declare `BASELINE_COMPATIBILITY=2.6.x` and `WORKER_SCHEMA_VERSION=1`.

## Routing/ownership QA

Only owning academic workers generate domain truth. W07 audits learner-read geometry. W08 owns layout/render/Thai. W09 owns integration release.

Cross-worker academic override = FAIL.

## Hard Student Blueprint isolation

`STUDENT_CONTENT_BLUEPRINT` is student-visible semantics only.

The following tokens/content classes are forbidden inside that section when they represent hidden targets:

- `RENDER_ONLY_NOT_FOR_WORKSHEET`
- target time/weight/length/angle/temperature/level
- paired day/night answer values
- hand/needle/ray angles
- target tick/index/endpoint/liquid level
- solved answer vectors
- renderer relation strings or hard negatives

If any renderer-only item state is found inside Student Blueprint:

`PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA=FAIL`
`PROMPT_RELEASE=BLOCKED`

Do not allow a later sanitizer label to convert a structurally invalid Student Blueprint into PASS.

## Visibility QA

Teacher-visible renderer metadata is allowed and required when needed, but only in the renderer/final-prompt scope and marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

Student worksheet contains no solved answer, target-specific callout or QA/internal metadata. Canonical instructional labels remain visible.

## Clock/day-night hard gates

For Thai Grade 3 analog-clock requests with `CLOCK_READING_MODE=AUTO`, require resolution to `DAY_NIGHT_PAIR` unless explicit user intent selects SINGLE.

When DAY_NIGHT_PAIR is active, every item requires:

- exactly one clock face
- exactly two blank fields
- labels `กลางวัน` and `กลางคืน` or explicit equivalent
- one shared hand state
- deterministic W02 label mapping
- identical minute/second components across pair
- 12-hour separation modulo 24
- no target values in Student Blueprint

For strict half-hour intent, every target minute must equal `30`. Presence of `:00` without explicit mixed-target request is FAIL.

Every high-risk analog clock renderer item requires:

`SEMANTIC TARGET + EXACT NUMERIC ANGLES + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Relational wording without numeric angles is insufficient.

Applicable mandatory gates:

`PROMPT_CLOCK_MODE_RESOLUTION_QA`
`PROMPT_HALF_HOUR_INTENT_QA`
`PROMPT_DAY_NIGHT_MAPPING_QA`
`PROMPT_DAY_NIGHT_SINGLE_FACE_QA`
`PROMPT_DAY_NIGHT_TWO_BLANKS_QA`
`PROMPT_DAY_NIGHT_SAME_HAND_STATE_QA`
`PROMPT_PER_ITEM_RENDER_STATE_QA`
`PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA`

Any FAIL above forces `PROMPT_RELEASE=BLOCKED`.

## Page-policy provenance

Default:

`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

`ONE_PAGE_LOCK=ON` requires explicit user provenance such as `1 หน้าเท่านั้น` or `A4 หน้าเดียว`.

If lock=ON without explicit provenance:

`PROMPT_PAGE_LOCK_PROVENANCE_QA=FAIL`
`PROMPT_RELEASE=BLOCKED`

A 2×5 layout may still be selected while the lock remains OFF.

## Prompt completeness

Final prompt must:

- exist and be standalone
- contain exact question count
- contain exactly one resolved render path
- state `RENDER_OBJECTIVE=STUDENT_WORKSHEET`
- contain no placeholders/external `see above` dependency
- include every per-item visual state when applicable
- include exact student-facing text/givens/blanks
- preserve canonical labels
- preserve requested/derived mode and page-policy provenance

## Measurement regressions

### Time
- `60 s=1 min`, `60 min=1 h`, `24 h=1 day`
- correct start/end/duration transformations
- no forbidden midnight crossing
- seconds hand not introduced merely by time-unit conversion

### Clock
- 10:30: minute=180°, hour=315°, midpoint 10–11, not on 10
- every nonzero-minute hour hand continuously displaced
- Thai P3 AUTO → DAY_NIGHT_PAIR unless explicit SINGLE
- deterministic day/night label mapping
- strict half-hour → minute 30 only

### Weight/scale
- `1000 g=1 kg`
- `1 ขีด=100 g=0.1 kg` where applicable
- canonical 0–5 kg dial = 300° active + 60° gap
- 50 intervals/51 positions at 0.1 kg
- no gap ticks / no 360° substitution

### Length/ruler/distance
- `10 mm=1 cm`, `100 cm=1 m`, `1000 m=1 km`
- 1 cm @1 mm = 10 intervals / 11 positions
- nonzero ruler start uses `end-start`
- round trip doubles only when same route explicit
- speed/rate not silently inferred

### Angle/protractor
- 0–180° @1° = 180 intervals / 181 endpoint-inclusive positions
- 0–360° full-circle @1° = 360 intervals / 360 distinct cyclic positions, no duplicated 360° mark
- vertex/origin, baseline and direction explicit
- target ray on exact graduation

### Perimeter/area
- perimeter counts each boundary side once
- area formula matches figure
- required height is perpendicular
- squared-unit conversion uses squared factor
- one consistent `PI_POLICY` for circles

### Temperature/capacity/volume
- `1000 mL=1 L`
- cubic relations exact
- discrete target representability exact
- meniscus read point explicit
- rectangular prism `V=l×w×h` after compatible-unit normalization
- composite parts non-overlapping

## Arithmetic/color-by-code/Thai regressions

- expressions recompute exactly
- exact division remains exact when requested
- every color region maps exactly once to an active answer code
- Thai spelling target is valid and belongs to requested family

## Release gate semantics

Critical QA is conjunctive, not advisory.

If **any** applicable critical gate is FAIL or NOT_RUN:

`PROMPT_RELEASE=BLOCKED`

W09 must never emit `PROMPT_RELEASE=APPROVED` while simultaneously reporting or structurally containing a critical violation.

Required applicable gates include:

`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`WORKER_OWNERSHIP_QA`
`PROMPT_ACADEMIC_DATA_QA`
`PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`
`PROMPT_UNIT_COMPATIBILITY_QA`
`PROMPT_UNIT_CONVERSION_QA`
`PROMPT_CLOCK_MODE_RESOLUTION_QA` when clock mode applies
`PROMPT_HALF_HOUR_INTENT_QA` when strict half-hour intent applies
`PROMPT_DAY_NIGHT_MAPPING_QA` when paired mode applies
`PROMPT_PER_ITEM_RENDER_STATE_QA` for learner-read visuals
`PROMPT_PROTRACTOR_TOPOLOGY_QA` when protractor is used
`PROMPT_PROTRACTOR_BASELINE_QA` when protractor is used
`PROMPT_AREA_FORMULA_QA` when area is used
`PROMPT_CUBIC_UNIT_CONVERSION_QA` when cubic conversion is used
`PROMPT_PAGE_LOCK_PROVENANCE_QA`
`RENDER_PATH_RESOLVED_QA`
`PROMPT_ONE_PAGE_FEASIBILITY_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`NO_PLACEHOLDER_QA`
`STUDENT_VISIBLE_ANSWER_LEAK_QA`
`STUDENT_VISIBLE_TARGET_TEXT_LEAK_QA`
`CANONICAL_LABEL_PRESERVATION_QA`

## Phase semantics

Before actual rendered image:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Prompt QA never proves actual pixel/glyph/geometry correctness.

## Health check

When user asks `ตรวจสุขภาพ Gem` / `Gem self-check`, report baseline, W01..W09 compatibility, W10 status, route table, measurement capability family, visibility model, render-path rule, page-lock provenance rule and prompt/artifact phase semantics. Do not generate a worksheet unless separately requested.

## Hotfix

W10 must declare `HOTFIX_ID, APPLIES_TO_BASELINE=2.6.x, SCOPE, TARGET_WORKER, REPLACED_RULE, NEW_RULE, REGRESSION_TEST`.

Reject broad hotfixes that change architecture, visibility model, worker schema or multiple unrelated domains.