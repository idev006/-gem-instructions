# TEMPERATURE_READING_ENGINE — Thermometer Reading

Version: 1.2.1
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal
Student reads temperature from a clear graduated thermometer scale.

## Core parameters
`MIN_TEMP, MAX_TEMP, MAJOR_INTERVAL, MINOR_INTERVAL, UNIT=C|F, TARGET_TEMPERATURES, ORIENTATION=VERTICAL|HORIZONTAL, ANSWER_FORMAT`.

## Geometry invariants
- straight scale; no perspective/skew/stretch
- direction locked for all repeated items
- uniform graduations across active range
- labels aligned to major ticks
- zero/minus signs clear when applicable
- liquid column has one unambiguous endpoint
- no decorative strokes that resemble ticks or liquid endpoints

## Deterministic graduation structure
Let `d=MINOR_INTERVAL`.

`EXPECTED_INTERVAL_COUNT = round((MAX_TEMP-MIN_TEMP)/d)`
`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

Require exact representability of the full range.

Examples:
- 0–50°C @1°C → 50 intervals / 51 positions
- -10–40°C @1°C → 50 / 51; zero index=10
- 0–100°C @5°C → 20 / 21
- 20–120°F @2°F → 50 / 51

## Target mapping — CRITICAL
For target `t`:

`tick_index = round((t-MIN_TEMP)/d)`
`represented_value = MIN_TEMP + tick_index*d`

Require `abs(t-represented_value) < tolerance`.

The liquid endpoint MUST coincide with the exact centerline of the target graduation. For a discrete graduated worksheet, the renderer must NOT place the liquid endpoint between two graduations.

If the configured minor interval is 2°F, a target such as 35°F is invalid unless the scale definition explicitly permits half-interval interpolation. Default elementary instrument-reading mode does not permit interpolation.

## Prompt serialization redundancy
For each item serialize:
- target semantic value (renderer-only)
- `tick_index`
- `level_ratio`
- nearest labelled major marks
- exact relational wording

Example:
`ITEM 2: target renderer state=46°F; minor interval=2°F; target tick index=13 from 20°F baseline; liquid top exactly on the 46°F graduation between 40 and 50; NEVER stop between ticks; DO NOT print 46 as an extra scale label or answer.`

## Answer-leak guard
Target numeric values used to control the liquid level are `RENDER_ONLY_NOT_VISIBLE`.
The downstream image MUST NOT add the target value as:
- an extra number beside the scale
- an annotation next to an arrow
- a caption inside the question card
- a completed answer

Only canonical scale labels may appear.

## Mandatory final-prompt block
```text
THERMOMETER GEOMETRY — CRITICAL
- exact active range and exact minor interval
- compute interval count and endpoint-inclusive tick-position count before drawing
- target values must be exactly representable by the minor interval
- liquid top must coincide exactly with the target graduation centerline
- never place liquid endpoint between ticks unless interpolation is explicitly part of the learning objective
- never print the renderer-only target value as an extra scale label or answer
- no missing/extra/duplicate ticks, no reversed scale, no decorative tick-like strokes
```

## Post-render QA
Inspect every thermometer:
- exact range/count/spacing
- target tick exists
- liquid endpoint coincides with target tick centerline
- no between-tick endpoint
- no target-value leakage
- correct unit and direction

## QA
`THERMOMETER_GEOMETRY_QA, SCALE_RANGE_QA, SCALE_DIRECTION_QA, INTERVAL_COUNT_QA, TICK_POSITION_COUNT_QA, TICK_SPACING_QA, MAJOR_MINOR_QA, NO_MISSING_TICK_QA, NO_EXTRA_TICK_QA, TARGET_REPRESENTABILITY_QA, TARGET_TICK_ALIGNMENT_QA, NO_BETWEEN_TICKS_QA, TARGET_VALUE_LEAK_QA, ZERO_NEGATIVE_QA, LABEL_QA, UNIT_QA, MINIMUM_SIZE_QA`.

Wrong graduation count, nonrepresentable target, endpoint between ticks, wrong column height, or visible renderer-only target value blocks release.
