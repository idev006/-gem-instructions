# TEMPERATURE_READING_ENGINE — Thermometer Reading

Version: 1.2.0
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

## Deterministic graduation structure

Let `d = MINOR_INTERVAL`.

`EXPECTED_INTERVAL_COUNT = round((MAX_TEMP - MIN_TEMP) / d)`

`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

Require the full active range to be exactly representable by `d` within tolerance.

Examples:

- `0–50°C`, minor interval `1°C` → 50 equal intervals, 51 endpoint-inclusive graduation positions
- `-10–40°C`, minor interval `1°C` → 50 equal intervals, 51 positions; the 0°C position must occur exactly 10 intervals above -10°C
- `0–100°C`, minor interval `5°C` → 20 intervals, 21 positions

If `MAJOR_INTERVAL=10°C` and `MINOR_INTERVAL=1°C`, each adjacent pair of major labels spans exactly 10 equal minor intervals.

Missing, duplicate, or extra graduations are critical academic failures.

## Deterministic mapping

For target `t` and minor interval `d`:

`tick_index = round((t - MIN_TEMP) / d)`

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

Do not allow decorative strokes, tube edges, or shading to look like extra graduation marks.

## Layout/readability

The smallest active interval must remain visually distinguishable after print/photocopying. If not, increase instrument height, reduce question density, or paginate according to the global one-page policy. Never merge adjacent graduations to force density.

## Render-only metadata

Compile per item:

`TARGET_TEMP, TICK_INDEX, LEVEL_RATIO, UNIT, SCALE_MIN, SCALE_MAX, MINOR_INTERVAL, EXPECTED_INTERVAL_COUNT, EXPECTED_TICK_POSITION_COUNT`

The target is geometry control, not visible answer text.

## Post-render QA

Inspect every thermometer individually and verify:

- exact active range endpoints;
- expected interval count and tick-position count;
- major-to-minor interval ratio;
- zero position when applicable;
- no missing/duplicate/extra ticks;
- liquid top exactly on target graduation.

## QA

`THERMOMETER_GEOMETRY_QA, SCALE_RANGE_QA, SCALE_DIRECTION_QA, INTERVAL_COUNT_QA, TICK_POSITION_COUNT_QA, TICK_SPACING_QA, MAJOR_MINOR_QA, NO_MISSING_TICK_QA, NO_EXTRA_TICK_QA, ZERO_NEGATIVE_QA, LABEL_QA, COLUMN_ALIGNMENT_QA, TARGET_TEMP_QA, UNIT_QA, MINIMUM_SIZE_QA`

Wrong graduation count, wrong column height, reversed scale, or ambiguous graduation blocks release.
