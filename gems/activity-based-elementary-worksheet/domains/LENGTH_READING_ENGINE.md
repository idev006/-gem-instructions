# LENGTH_READING_ENGINE — Ruler / Length Reading

Version: 1.0.0
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal

Student reads an object's length from a ruler or number-line style measuring scale.

## Core parameters

`MAX_LENGTH_CM, MAJOR_DIVISION_CM, MINOR_DIVISION_CM, UNIT_MODE=CM|MM|CM_AND_MM, START_POSITION_MODE=ZERO|NONZERO_ADVANCED, TARGET_LENGTHS, ANSWER_FORMAT`

Default elementary metric profile:

- major mark = 1 cm
- minor mark = 1 mm = 0.1 cm when millimetre reading is intended
- object normally starts exactly at zero for beginner worksheets

## Geometry invariants

- ruler baseline straight and horizontal/vertical as specified
- no perspective or skew
- evenly spaced graduations
- zero mark explicit and aligned to measurement start
- centimetre marks stronger than millimetre marks
- object endpoints unambiguous
- no decorative art covering endpoints or tick labels

## Deterministic mapping

`length_mm = round(length_cm * 10)`

For zero-start tasks, endpoint tick index = `length_mm` when minor division is 1 mm.

For nonzero-start tasks:

`length = end_value - start_value`

Generate and validate both endpoints before rendering.

## Critical misconception guard

Do not measure from the physical edge of the drawn ruler unless the zero mark is exactly at that edge. The academic start point is the zero graduation.

## Layout/readability

Minor marks must remain distinguishable in print. If 1 mm divisions become too dense, enlarge the ruler or reduce question density.

## QA

`RULER_STRAIGHT_QA, ZERO_ALIGNMENT_QA, TICK_SPACING_QA, MAJOR_MINOR_QA, ENDPOINT_QA, VALUE_QA, UNIT_QA, MINIMUM_SIZE_QA`

Incorrect zero alignment or endpoint is a critical blocker.