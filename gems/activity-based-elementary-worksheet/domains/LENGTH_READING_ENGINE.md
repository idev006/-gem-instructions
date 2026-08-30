# LENGTH_READING_ENGINE — Ruler / Length / Distance Rules

Version: 1.3.0
Status: PRODUCTION_CANDIDATE
Owning worker: `W04_LENGTH_DISTANCE`
Requires `INSTRUMENT_READING_ENGINE.md` only when a learner reads a ruler/scale.

## 1. Learning scope

Supports:

- ruler reading
- zero-start and nonzero-start measurement
- length addition/subtraction/difference/comparison
- mm/cm/m/km conversion
- distance total/difference/round trip/multi-segment/route comparison
- grade-appropriate measurement word problems

Speed/rate is outside this engine unless explicitly requested through another rule set.

## 2. Core parameters

`LENGTH_SUBDOMAIN, SCALE_MIN_CM, SCALE_MAX_CM, MAJOR_DIVISION_CM, MINOR_DIVISION_CM, UNIT_SET, START_POSITION_MODE, TARGET_LENGTHS, LENGTH_TASK_TYPE, DISTANCE_TASK_TYPE, DISTANCE_CONTEXT, ANSWER_FORMAT`

## 3. Exact metric relations

`10 mm = 1 cm`
`100 cm = 1 m`
`1000 m = 1 km`

Canonical arithmetic base unit: **millimetres** for exact integer metric length calculations unless a decimal-safe representation is explicitly used.

Before adding/subtracting/comparing mixed units:

1. convert every quantity to one base unit;
2. perform exact arithmetic;
3. independently verify;
4. convert result to requested display format.

Never add `m + cm` or `km + m` as raw numerals without unit conversion.

## 4. Ruler geometry

Elementary defaults when ruler reading is intended:

- `SCALE_MIN_CM=0`
- major division `1 cm`
- minor division `0.1 cm = 1 mm` when mm reading is taught
- beginner object start = exact zero graduation

Geometry invariants:

- straight front-facing baseline
- no perspective/skew/stretch
- uniform graduation spacing
- zero graduation visually distinct from physical ruler edge
- cm marks stronger/longer than mm marks
- object start/end guides unambiguous
- no decoration that resembles graduations
- repeated rulers share one template unless task explicitly changes scale

## 5. Linear graduation topology

For scale min/max and minor interval `d`:

`EXPECTED_INTERVAL_COUNT = round((SCALE_MAX-SCALE_MIN)/d)`
`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

Require exact representability.

Canonical mm profile:

- 1 cm = 10 equal intervals
- 1 cm endpoint-inclusive span = 11 graduation positions

A ruler showing 9, 11, or another number of **intervals** per cm is academically wrong.

## 6. Ruler target mapping

`tick_index(value)=round((value-SCALE_MIN)/d)`

Require:

`abs(value-(SCALE_MIN+tick_index*d)) < tolerance`

Zero-start:

`length=end_value`

Nonzero-start:

`length=end_value-start_value`

Both endpoints must be valid graduations in exact-reading mode.

Do not confuse measurement start with the physical ruler edge.

## 7. Length calculation

Task types:

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

For subtraction in nonnegative elementary mode, generate values that produce a valid nonnegative result unless negatives are explicitly taught.

Mixed-unit answer formats may be generated after exact base-unit computation, e.g. `2 m 35 cm`.

## 8. Distance calculation

Task types:

`TOTAL | DIFFERENCE | ROUND_TRIP | MULTI_SEGMENT | ROUTE_COMPARE | CONVERT`

Rules:

- total = sum verified segment distances after unit normalization
- difference = absolute or directed difference according to wording; default elementary comparison uses nonnegative absolute difference
- same-route round trip = `2×one_way_distance` only when the same route is stated/implied clearly
- asymmetric outbound/return = `outbound + return`; do not assume equality
- multi-segment = sum each segment exactly once
- route compare = independently total each route, then compare/difference

Map-style illustrations are contextual unless scale-map mathematics is explicitly requested; do not invent a map scale.

## 9. Grade progression

Follow `MEASUREMENT_COVERAGE_P1_P6.md`.

Conservative defaults:

- P1: whole-unit/direct comparison; no complex conversion
- P2: clear cm/simple m contexts
- P3: cm/mm ruler and basic distance arithmetic
- P4: integer mm/cm/m/km conversion, nonzero starts, multi-segment distance
- P5: mixed-unit/decimal conversion where appropriate, multi-step distance
- P6: multi-step conversion + route reasoning

## 10. Renderer-only ruler metadata

For each ruler item compile internally:

`START_VALUE, END_VALUE, START_TICK_INDEX, END_TICK_INDEX, TARGET_LENGTH, UNIT, EXPECTED_INTERVAL_COUNT, EXPECTED_TICK_POSITION_COUNT`

Put exact geometry only in teacher-visible renderer metadata marked `RENDER_ONLY_NOT_FOR_WORKSHEET`. Do not expose target values/indices in Student Blueprint.

## 11. Canonical labels

Ruler labels/graduations required by the configured scale are legitimate instructional data and must remain visible. Leak guards prohibit target-answer callouts, not canonical ruler labels.

## 12. Layout/readability

The smallest active graduation must remain distinguishable after print/photocopy.

- reserve fixed-aspect instrument zone
- preserve exact graduation count before decoration
- reduce decoration before ruler size
- if one-page lock cannot preserve the scale, fail feasibility rather than merge/omit ticks

## 13. QA

Prompt-phase gates:

`PROMPT_LENGTH_UNIT_COMPATIBILITY_QA`
`PROMPT_LENGTH_CONVERSION_QA`
`PROMPT_LENGTH_CALCULATION_QA`
`PROMPT_DISTANCE_RELATION_QA`
`PROMPT_RULER_TOPOLOGY_QA`
`PROMPT_RULER_ZERO_REFERENCE_QA`
`PROMPT_RULER_ENDPOINT_QA`
`PROMPT_RULER_TARGET_REPRESENTABILITY_QA`
`PROMPT_RULER_LABEL_PRESERVATION_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`

Artifact checks run only after render and inspect every ruler individually.

Critical blockers include wrong conversion/arithmetic, wrong start reference, wrong interval/position count, missing/extra graduation, between-tick target in exact mode, or misleading distance relation.