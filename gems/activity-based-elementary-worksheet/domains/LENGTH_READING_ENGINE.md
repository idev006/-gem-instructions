# LENGTH_READING_ENGINE — Ruler / Length Reading

Version: 1.2.0
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal

Student reads an object's length from a ruler or number-line style measuring scale without confusing the ruler edge with the zero graduation.

## Core parameters

`SCALE_MIN_CM, MAX_LENGTH_CM, MAJOR_DIVISION_CM, MINOR_DIVISION_CM, UNIT_MODE=CM|MM|CM_AND_MM, START_POSITION_MODE=ZERO|NONZERO_ADVANCED, TARGET_LENGTHS, ANSWER_FORMAT`

Elementary metric defaults:

- `SCALE_MIN_CM = 0`
- major division = `1 cm`
- minor division = `0.1 cm = 1 mm` when millimetre reading is intended
- beginner object start = exact zero graduation

## Geometry invariants

- ruler baseline straight and front-facing
- no perspective, skew, stretch or non-uniform scale
- graduation spacing uniform
- zero graduation explicit and visually distinct from physical ruler edge
- centimetre marks stronger/longer than millimetre marks
- object start/end guides unambiguous
- no decorative art covering endpoint, zero mark or labels
- identical scale geometry for repeated questions unless the task explicitly changes scale

## Deterministic graduation structure

For active ruler range `SCALE_MIN_CM` to `SCALE_MAX_CM` with `d = MINOR_DIVISION_CM`:

`EXPECTED_INTERVAL_COUNT = round((SCALE_MAX_CM - SCALE_MIN_CM) / d)`

`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

Require exact representability within tolerance.

For the canonical millimetre profile:

- `1 cm = 10 mm`
- between adjacent whole-centimetre values there are exactly **10 equal intervals**
- including both endpoints, that 1 cm span contains **11 graduation positions**
- whole-centimetre marks are major ticks; internal millimetre positions are minor ticks

A ruler that visually shows 9, 11, or another number of intervals per centimetre is academically wrong even if spacing looks regular.

## Deterministic mapping

For any active minor division `d = MINOR_DIVISION_CM`:

`tick_index(value) = round((value - SCALE_MIN_CM) / d)`

Require exact representability:

`abs(value - (SCALE_MIN_CM + tick_index*d)) < tolerance`

For zero-start tasks:

`length = end_value - 0`

For nonzero-start tasks:

`length = end_value - start_value`

and both start/end must be valid graduations.

Never assume `tick_index = length_mm` unless `d = 0.1 cm` and `SCALE_MIN_CM = 0`.

## Critical misconception guard

The academic measurement begins at the selected start graduation, normally zero, not automatically at the physical edge of the ruler.

If an object is offset from zero in an advanced task, students must read both endpoints or the start marker must be explicit.

## Layout/readability

The smallest active graduation must be distinguishable after printing/photocopying.

- reserve a rectangular instrument zone with fixed aspect ratio
- preserve the exact graduation count before decoration
- prefer fewer questions or pagination over compressing/merging 1 mm ticks
- labels may not collide with ticks or object endpoints
- object must not visually float above an ambiguous start/end location

## Render-only target metadata

For each item compile:

`START_VALUE, END_VALUE, START_TICK_INDEX, END_TICK_INDEX, TARGET_LENGTH, UNIT, EXPECTED_INTERVAL_COUNT, EXPECTED_TICK_POSITION_COUNT`

These values control geometry but answers remain invisible when answer key is off.

## Post-render QA

Inspect every ruler individually. Count the active intervals and graduation positions rather than judging only visual regularity.

Critical failures include missing/duplicated millimetre marks, wrong count per centimetre, a major mark not aligned to its value, start/end placed between intended ticks, or decorative marks that could be mistaken for graduations.

## QA

`RULER_STRAIGHT_QA, SCALE_RANGE_QA, ZERO_ALIGNMENT_QA, INTERVAL_COUNT_QA, TICK_POSITION_COUNT_QA, TICK_SPACING_QA, MAJOR_MINOR_QA, NO_MISSING_TICK_QA, NO_EXTRA_TICK_QA, START_ENDPOINT_QA, END_ENDPOINT_QA, VALUE_QA, UNIT_QA, MINIMUM_SIZE_QA`

Incorrect start reference, endpoint, interval count, tick count, spacing, or value is a critical blocker.
