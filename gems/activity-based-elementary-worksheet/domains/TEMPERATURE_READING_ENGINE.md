# TEMPERATURE_READING_ENGINE — Thermometer Reading

Version: 1.3.0
Status: PRODUCTION_CANDIDATE
Owning worker: `W05_TEMPERATURE_CAPACITY_VOLUME`
Requires: `INSTRUMENT_READING_ENGINE.md`
Compatible Gem baseline: 2.6.x

## Learning goal

Student reads temperature from a clear graduated thermometer scale and, when requested, compares temperature/change using verified values.

## Core parameters

`MIN_TEMP, MAX_TEMP, MAJOR_INTERVAL, MINOR_INTERVAL, UNIT=C|F, TARGET_TEMPERATURES, ORIENTATION=VERTICAL|HORIZONTAL, ANSWER_FORMAT`

## Geometry invariants

- straight scale; no perspective/skew/stretch
- direction locked across repeated items
- uniform graduations
- labels aligned to major ticks
- zero/minus signs clear when applicable
- liquid column has one unambiguous endpoint
- no decorative strokes resembling ticks or liquid endpoint

## Deterministic topology

Let `d=MINOR_INTERVAL`.

`EXPECTED_INTERVAL_COUNT=round((MAX_TEMP-MIN_TEMP)/d)`
`EXPECTED_TICK_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`

Require exact representability of the scale range.

Examples:

- 0–50°C @1°C → 50 intervals / 51 positions
- -10–40°C @1°C → 50 / 51; zero index=10
- 0–100°C @5°C → 20 / 21
- 20–120°F @2°F → 50 / 51

## Target mapping — critical

For target `t`:

`tick_index=round((t-MIN_TEMP)/d)`
`represented_value=MIN_TEMP+tick_index*d`

Require `abs(t-represented_value)<tolerance` in discrete mode.

The liquid endpoint must coincide exactly with the target graduation centerline. Do not place it between ticks unless interpolation is explicitly part of the lesson.

Example: with 20–120°F @2°F, 35°F is invalid in default discrete mode.

## Renderer metadata / visibility

For each visual item serialize:

- semantic target
- tick index
- level ratio
- nearest labelled major marks
- exact relational wording
- item-specific hard negative

Mark this block:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

The renderer-only target may appear in the **teacher-visible final prompt** because it controls geometry. It must not appear in Student Blueprint or as learner-visible extra scale label, arrow annotation, caption, or completed answer.

Canonical configured scale labels remain visible.

## Mandatory final-prompt principles

- exact active range/minor interval
- exact interval/position count
- every target exactly representable in discrete mode
- liquid top exactly on target graduation centerline
- no unintended between-tick endpoint
- no missing/extra/duplicate ticks
- no reversed scale
- no target-number callout
- preserve legitimate scale labels

## Grade progression

Use `MEASUREMENT_COVERAGE_P1_P6.md`. Do not select unnecessarily fine scales for early grades merely because they are mathematically representable.

## QA

Prompt-phase:

`PROMPT_THERMOMETER_TOPOLOGY_QA`
`PROMPT_TEMP_TARGET_REPRESENTABILITY_QA`
`PROMPT_TEMP_ENDPOINT_ALIGNMENT_SPEC_QA`
`PROMPT_NO_BETWEEN_TICKS_QA`
`PROMPT_TEMP_LABEL_PRESERVATION_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`

Actual visual alignment remains `ARTIFACT_QA=NOT_YET_TESTED` until the rendered worksheet is inspected.

Wrong graduation count, nonrepresentable target, between-tick specification, wrong unit/direction, or learner-visible target-value leakage blocks prompt release.