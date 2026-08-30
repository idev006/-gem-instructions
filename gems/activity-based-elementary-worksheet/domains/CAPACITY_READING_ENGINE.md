# CAPACITY_READING_ENGINE — Graduated Capacity / Volume Reading

Version: 1.2.0
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal

Student reads volume/capacity from a graduated container using a clear, deterministic scale.

## Core parameters

`SCALE_MIN, MAX_CAPACITY, MAJOR_DIVISION, MINOR_DIVISION, UNIT=L|ML, TARGET_LEVELS, CONTAINER_TYPE, MENISCUS_MODE=SIMPLE_FLAT|SCIENTIFIC`

For early primary worksheets default to:

- `SCALE_MIN = 0`
- simplified flat liquid level
- metric units appropriate to the task

## Geometry invariants

- container upright and front-facing
- no perspective/skew/stretch when graduations are instructional
- scale baseline and maximum explicitly defined
- graduations uniformly spaced
- labels aligned with major marks
- liquid surface horizontal in simplified mode
- level intersects intended graduation exactly
- no decorative waves/bubbles creating alternative reading lines
- identical scale orientation and direction across repeated questions

## Deterministic graduation structure

Let `d = MINOR_DIVISION`.

`EXPECTED_INTERVAL_COUNT = round((MAX_CAPACITY - SCALE_MIN) / d)`

`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

Require exact representability within tolerance.

Examples:

- `0–1000 mL`, minor `100 mL` → 10 equal intervals, 11 endpoint-inclusive graduation positions
- `0–1000 mL`, minor `50 mL` → 20 intervals, 21 positions
- `500–1500 mL`, minor `100 mL` → 10 intervals, 11 positions; do not invent a zero mark outside the active scale

When major and minor divisions are both defined, each major interval must contain exactly `MAJOR_DIVISION / MINOR_DIVISION` equal minor intervals.

Missing, duplicated, or extra graduations are critical academic failures.

## Deterministic mapping

`tick_index = round((target - SCALE_MIN) / d)`

Require:

- `MAX_CAPACITY > SCALE_MIN`
- `d > 0`
- `SCALE_MIN <= target <= MAX_CAPACITY`
- target exactly representable by `d`
- active range exactly representable by `d` when the full scale is shown

Normalized level from the minimum baseline:

`level_ratio = (target - SCALE_MIN) / (MAX_CAPACITY - SCALE_MIN)`

The instructional liquid line must align with the corresponding graduation.

Do not assume zero baseline when `SCALE_MIN` is nonzero.

## Scientific meniscus mode

Only use when explicitly requested and grade appropriate. Lock one convention:

- `READ_BOTTOM_MENISCUS`, or
- `READ_TOP_MENISCUS`

The chosen reading point must be visually explicit and used consistently.

## Layout/readability

- reserve fixed instrument zones
- smallest active graduation must remain readable after print/photocopy
- labels and liquid line may not collide
- preserve exact graduation count before decoration
- if tick density becomes ambiguous, enlarge/paginate according to global one-page policy rather than shrink/merge marks

## Render-only metadata

Compile per item:

`TARGET_LEVEL, TICK_INDEX, LEVEL_RATIO, SCALE_MIN, SCALE_MAX, MINOR_DIVISION, MENISCUS_RULE, UNIT, EXPECTED_INTERVAL_COUNT, EXPECTED_TICK_POSITION_COUNT`

This is geometry control and must not become visible answer text.

## Post-render QA

Inspect every container individually and verify:

- active range endpoints;
- exact interval count and graduation-position count;
- major/minor ratio;
- no missing/duplicate/extra graduations;
- no decorative line mistaken for a scale mark;
- target liquid level aligned to the intended graduation.

## QA

`CONTAINER_GEOMETRY_QA, SCALE_RANGE_QA, SCALE_DIRECTION_QA, INTERVAL_COUNT_QA, GRADUATION_COUNT_QA, TICK_SPACING_QA, MAJOR_MINOR_QA, NO_MISSING_TICK_QA, NO_EXTRA_TICK_QA, LEVEL_ALIGNMENT_QA, MENISCUS_QA, LABEL_QA, TARGET_VOLUME_QA, UNIT_QA, MINIMUM_SIZE_QA`

Ambiguous or incorrect liquid level, scale baseline, graduation count, or spacing blocks release.
