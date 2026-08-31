# LENGTH_READING_ENGINE — Ruler / Length / Distance Rules

Version: 1.4.0
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
- object start/end references are explicit and machine-checkable
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

## 7. Object endpoint projection/reference geometry — mandatory

For elementary object-on-ruler worksheets, the learner must be able to see exactly which ruler graduations correspond to the two object endpoints.

Canonical coordinate contract:

`OBJECT_START_X == START_GRADUATION_X`
`OBJECT_END_X == END_GRADUATION_X`

When the object is drawn above the ruler and does not physically touch the reading line, use two thin dashed vertical projection guides:

`START_PROJECTION_GUIDE_X = OBJECT_START_X = START_GRADUATION_X`
`END_PROJECTION_GUIDE_X = OBJECT_END_X = END_GRADUATION_X`

The projection guides:

- run from the exact object endpoint down to the ruler reading/graduation zone;
- remain perpendicular to the ruler baseline;
- use a dashed/helper style visually distinct from ruler graduations;
- must not obscure, replace, thicken, duplicate, or create a graduation;
- are instructional reference geometry, not decoration.

### ZERO_START_MODE

If the task says or implies measurement starts at zero:

`START_GRADUATION_VALUE=0`
`OBJECT_START_X == ZERO_GRADUATION_X`
`START_PROJECTION_GUIDE_X == ZERO_GRADUATION_X`

The physical ruler border/edge is not a substitute for the zero graduation unless the owning template explicitly defines exact geometric coincidence between them. Default elementary templates keep the zero graduation visibly inside/distinct from the physical edge.

### NONZERO_START_MODE

If the task explicitly teaches a nonzero start:

`START_GRADUATION_VALUE != 0` is permitted;
`TARGET_LENGTH = END_VALUE - START_VALUE`;
both projection guides remain required so the subtraction relation is visually unambiguous.

A picture in which the object starts at the physical ruler edge while the zero graduation lies elsewhere is `CRITICAL_ACADEMIC` in ZERO_START_MODE.

## 8. Length calculation

Task types:

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

For subtraction in nonnegative elementary mode, generate values that produce a valid nonnegative result unless negatives are explicitly taught.

Mixed-unit answer formats may be generated after exact base-unit computation, e.g. `2 m 35 cm`.

## 9. Distance calculation

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

## 10. Grade progression

Follow `MEASUREMENT_COVERAGE_P1_P6.md`.

Conservative defaults:

- P1: whole-unit/direct comparison; no complex conversion
- P2: clear cm/simple m contexts
- P3: cm/mm ruler and basic distance arithmetic
- P4: integer mm/cm/m/km conversion, nonzero starts, multi-segment distance
- P5: mixed-unit/decimal conversion where appropriate, multi-step distance
- P6: multi-step conversion + route reasoning

## 11. Renderer-only ruler metadata

For each ruler item compile internally:

`START_VALUE, END_VALUE, START_TICK_INDEX, END_TICK_INDEX, TARGET_LENGTH, UNIT, EXPECTED_INTERVAL_COUNT, EXPECTED_TICK_POSITION_COUNT, START_GRADUATION_X, END_GRADUATION_X, START_PROJECTION_GUIDE_X, END_PROJECTION_GUIDE_X`

Put exact geometry only in teacher-visible renderer metadata marked `RENDER_ONLY_NOT_FOR_WORKSHEET`. Do not expose target values/indices in Student Blueprint.

## 12. Canonical labels

Ruler labels/graduations required by the configured scale are legitimate instructional data and must remain visible. Leak guards prohibit target-answer callouts, not canonical ruler labels.

## 13. Layout/readability

The smallest active graduation must remain distinguishable after print/photocopy.

- reserve fixed-aspect instrument zone
- preserve exact graduation count before decoration
- reserve space for projection guides without cropping object endpoints
- reduce decoration before ruler size
- if one-page lock cannot preserve the scale, fail feasibility rather than merge/omit ticks

## 14. QA

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
`PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA`
`PROMPT_RULER_ZERO_START_ALIGNMENT_QA`
`PROMPT_RULER_NONZERO_START_RELATION_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`

Artifact checks run only after render and inspect every ruler individually.

Critical blockers include wrong conversion/arithmetic, wrong start reference, object endpoint not aligned to its intended graduation, missing/misplaced projection guide, physical-edge substitution for zero, wrong interval/position count, missing/extra graduation, between-tick target in exact mode, or misleading distance relation.