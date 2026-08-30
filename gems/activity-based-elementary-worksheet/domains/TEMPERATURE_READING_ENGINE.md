# TEMPERATURE_READING_ENGINE — Thermometer Reading

Version: 1.0.0
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal

Student reads temperature from a graduated thermometer scale.

## Core parameters

`MIN_TEMP, MAX_TEMP, MAJOR_INTERVAL, MINOR_INTERVAL, UNIT=C|F, TARGET_TEMPERATURES, ORIENTATION=VERTICAL, ANSWER_FORMAT`

Default Thai primary profile: Celsius.

## Geometry invariants

- straight vertical scale unless explicitly horizontal
- uniform tick spacing
- major/minor ticks visually distinct
- labels aligned to major ticks
- bulb/tube centered and not confused with a pointer
- liquid/column level has one unambiguous top endpoint
- no decorative line crossing the scale

## Deterministic mapping

For target `t`:

`tick_index = round((t - MIN_TEMP) / MINOR_INTERVAL)`

Require exact representability by the active interval.

The liquid column top must align exactly with the target graduation.

## Misconception guard

Do not let the image model treat the thermometer as a generic icon with arbitrary mercury height. The level is the question data.

## Layout/readability

Printed scale must be large enough that adjacent minor marks can be distinguished. Prefer fewer questions or multiple pages over tiny thermometers.

## QA

`THERMOMETER_SCALE_QA, TICK_SPACING_QA, LABEL_QA, COLUMN_ALIGNMENT_QA, TARGET_TEMP_QA, UNIT_QA, MINIMUM_SIZE_QA`

Wrong column height is a critical blocker.