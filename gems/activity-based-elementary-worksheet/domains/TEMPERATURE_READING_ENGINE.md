# TEMPERATURE_READING_ENGINE — Thermometer Reading

Version: 1.1.0
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal

Student reads temperature from a clear graduated thermometer scale.

## Core parameters

`MIN_TEMP, MAX_TEMP, MAJOR_INTERVAL, MINOR_INTERVAL, UNIT=C|F, TARGET_TEMPERATURES, ORIENTATION=VERTICAL, ANSWER_FORMAT`

Default Thai primary profile: Celsius, vertical thermometer, values increase upward.

## Geometry invariants

- straight vertical scale unless explicitly horizontal
- fixed rectangular instrument zone; no perspective/skew/stretch
- scale direction locked: default `MIN_TEMP` at bottom, `MAX_TEMP` at top
- uniform graduation spacing across the full active range
- major/minor ticks visually distinct
- labels aligned to major ticks
- zero label shown when zero lies inside the active range
- negative labels use a clear minus sign when applicable
- bulb/tube centered and not confused with a pointer
- liquid/column has one unambiguous top endpoint
- no decorative line crossing the scale

## Deterministic mapping

For target `t` and minor interval `d`:

`tick_index = round((t - MIN_TEMP) / d)`

`tick_count = round((MAX_TEMP - MIN_TEMP) / d)`

Require:

- `MIN_TEMP <= t <= MAX_TEMP`
- `MAX_TEMP > MIN_TEMP`
- `d > 0`
- full range exactly representable by `d`
- target exactly representable by `d`

Conceptual normalized height from bottom:

`level_ratio = (t - MIN_TEMP) / (MAX_TEMP - MIN_TEMP)`

The top of the liquid column must align exactly with that graduation/ratio.

## Misconception guard

Do not let the image model treat the thermometer as a generic icon with arbitrary liquid height. The liquid top is academic question data.

Do not reverse the scale direction between questions. Do not omit zero when negative and positive values share the same scale.

## Layout/readability

The smallest active interval must remain visually distinguishable after print/photocopying. If not, increase instrument height, reduce question density, or paginate.

## Render-only metadata

Compile per item:

`TARGET_TEMP, TICK_INDEX, LEVEL_RATIO, UNIT, SCALE_MIN, SCALE_MAX, MINOR_INTERVAL`

The target is geometry control, not visible answer text.

## QA

`THERMOMETER_GEOMETRY_QA, SCALE_RANGE_QA, SCALE_DIRECTION_QA, TICK_SPACING_QA, ZERO_NEGATIVE_QA, LABEL_QA, COLUMN_ALIGNMENT_QA, TARGET_TEMP_QA, UNIT_QA, MINIMUM_SIZE_QA`

Wrong column height, reversed scale, or ambiguous graduation blocks release.