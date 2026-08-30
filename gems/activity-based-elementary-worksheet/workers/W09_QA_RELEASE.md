# W09 — QA & Release Specialist

`WORKER_ID=W09_QA_RELEASE`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Route decision, selected worker outputs, normalized spec, Student Blueprint, layout blueprint, render constraints, final prompt draft.

## OWNS

- worker compatibility/ownership validation
- integration QA
- visibility/leak QA
- prompt completeness/copy-readiness
- measurement/global regression gates
- prompt-vs-artifact phase semantics
- release decision
- installation health/self-check

## RETURNS

QA report, prompt-release decision, artifact phase status, classroom-release status, repair instructions when blocked.

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

Every base worker:

`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## Routing/ownership QA

Only relevant academic workers own generation. W07 audits geometry. W08 owns layout/render/Thai. W09 owns release.

Fail if one worker silently overrides another worker's owned academic formula.

## Student Blueprint QA

Student Blueprint must not expose:

- answers
- target times/weights/lengths/angles/levels
- hand/needle/ray angles
- tick indices
- liquid levels
- answer vectors
- renderer-only relation strings

## Visibility QA

Teacher-visible renderer metadata is allowed/required when needed and must be marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

Student worksheet must contain no solved answer, target-specific callout, or QA/internal metadata. Canonical instructional labels remain visible.

## Prompt completeness

Final prompt must:

- exist and be standalone
- contain exact question count
- contain one resolved render path
- state `RENDER_OBJECTIVE=STUDENT_WORKSHEET`
- contain no placeholders/external `see above` dependency
- include every per-item visual state when applicable
- include exact student-facing text/givens/blanks
- preserve canonical labels

## Measurement regressions

### Time
- `60 s=1 min`, `60 min=1 h`, `24 h=1 day`
- correct start/end/duration transformations
- no forbidden midnight crossing
- second precision only when requested/warranted
- seconds hand not introduced automatically by time-unit conversion

### Clock
- 10:30: minute=180°, hour=315°, midpoint 10–11, not on 10
- every nonzero-minute hour hand continuously displaced
- clock numerals preserved when configured

### Weight/scale
- `1000 g=1 kg`
- `1 ขีด=100 g=0.1 kg` where applicable
- canonical 0–5 dial = 300° active + 60° gap
- 50 intervals/51 positions at 0.1 kg
- no gap ticks / no 360° substitution
- labels 0–5 preserved

### Length/ruler/distance
- `10 mm=1 cm`, `100 cm=1 m`, `1000 m=1 km`
- 1 cm @1 mm = 10 intervals / 11 positions
- nonzero ruler start uses `end-start`
- round trip doubles one-way only when same route explicit
- multi-segment distance counts each segment once
- speed/rate not silently inferred

### Angle/protractor
- semicircular 0–180° protractor uses exact topology defined by W04/W07
- vertex exactly at origin
- baseline ray at selected 0°
- active inner/outer scale direction unambiguous
- target ray on exact graduation in exact-reading mode
- renderer target angle/ray state absent from Student Blueprint

### Perimeter/area
- perimeter counts each boundary side exactly once
- area formula matches figure type
- triangle/parallelogram/trapezoid height is perpendicular height
- squared-unit conversion uses squared linear factor
- circle tasks use one consistent `PI_POLICY`

### Temperature/capacity/volume
- `1000 mL=1 L`
- `1000 cm³=1 dm³`, `1000 dm³=1 m³`, `1 m³=1,000,000 cm³`
- `1 cm³=1 mL`, `1 dm³=1 L`, `1 m³=1000 L` only when explicitly taught
- thermometer/capacity discrete target exactly representable
- meniscus read point explicit/unambiguous
- rectangular prism `V=l×w×h` with compatible dimension units
- cubic conversion uses cubed linear factors
- composite rectangular prisms do not double-count overlap

## Arithmetic/color-by-code/Thai regressions

- every expression recomputes correctly
- exact division remains exact when requested
- every color region maps exactly once to an active answer code
- Thai spelling target is valid and belongs to requested family

## Phase semantics

Before actual rendered image:

- prompt-phase checks may PASS
- `ARTIFACT_QA=NOT_YET_TESTED`
- `CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Never claim actual visual circle/tick/hand/ray/alignment/Thai glyph PASS without artifact inspection.

## Release gates

Required applicable gates:

`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`WORKER_OWNERSHIP_QA`
`PROMPT_ACADEMIC_DATA_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA` for measurement tasks
`PROMPT_UNIT_COMPATIBILITY_QA` when units are involved
`PROMPT_UNIT_CONVERSION_QA` when conversion is involved
`PROMPT_TIME_UNIT_CONVERSION_QA` when time conversion is involved
`PROMPT_PROTRACTOR_TOPOLOGY_QA` when protractor is used
`PROMPT_PROTRACTOR_BASELINE_QA` when protractor is used
`PROMPT_AREA_FORMULA_QA` when area is used
`PROMPT_AREA_UNIT_CONVERSION_QA` when area conversion is used
`PROMPT_PI_POLICY_QA` when circles are used
`PROMPT_CUBIC_UNIT_CONVERSION_QA` when cubic conversion is used
`RENDER_PATH_RESOLVED_QA`
`PROMPT_ONE_PAGE_FEASIBILITY_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`NO_PLACEHOLDER_QA`
`STUDENT_VISIBLE_ANSWER_LEAK_QA`
`STUDENT_VISIBLE_TARGET_TEXT_LEAK_QA`
`CANONICAL_LABEL_PRESERVATION_QA`
plus selected worker/domain gates.

If all critical gates pass:

`PROMPT_RELEASE=APPROVED`
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

## Health check

When user asks `ตรวจสุขภาพ Gem` / `Gem self-check`, report baseline, W01..W09 presence/compatibility, W10 present/absent, route table, measurement capability family, visibility model, render-path rule, prompt/artifact phase semantics, and `INSTALLATION_HEALTH=PASS|FAIL`. Do not generate a worksheet unless separately requested.

## Hotfix

W10 must declare `HOTFIX_ID, APPLIES_TO_BASELINE=2.6.x, SCOPE, TARGET_WORKER, REPLACED_RULE, NEW_RULE, REGRESSION_TEST`.

Reject broad hotfixes that change architecture, visibility model, worker schema or multiple unrelated domains.