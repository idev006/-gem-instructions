# CAPACITY_READING_ENGINE — Graduated Capacity / Volume Reading

Version: 1.1.0
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

## Deterministic mapping

Let `d = MINOR_DIVISION`.

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
- if tick density becomes ambiguous, enlarge/paginate rather than shrink

## Render-only metadata

Compile per item:

`TARGET_LEVEL, TICK_INDEX, LEVEL_RATIO, SCALE_MIN, SCALE_MAX, MINOR_DIVISION, MENISCUS_RULE, UNIT`

This is geometry control and must not become visible answer text.

## QA

`CONTAINER_GEOMETRY_QA, SCALE_RANGE_QA, SCALE_DIRECTION_QA, GRADUATION_QA, LEVEL_ALIGNMENT_QA, MENISCUS_QA, LABEL_QA, TARGET_VOLUME_QA, UNIT_QA, MINIMUM_SIZE_QA`

Ambiguous or incorrect liquid level, scale baseline, or graduation blocks release.