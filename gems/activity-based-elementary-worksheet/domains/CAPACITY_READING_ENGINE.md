# CAPACITY_READING_ENGINE — Graduated Capacity / Volume Reading

Version: 1.0.0
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal

Student reads volume/capacity from a graduated container or simplified measuring vessel.

## Core parameters

`MAX_CAPACITY, MAJOR_DIVISION, MINOR_DIVISION, UNIT=L|ML, TARGET_LEVELS, CONTAINER_TYPE, MENISCUS_MODE=SIMPLE_FLAT|SCIENTIFIC`

For early primary worksheets default to a simplified flat level unless a science-specific meniscus objective is requested.

## Geometry invariants

- container vertical and front-facing
- sides not perspective-distorted when the scale is used for reading
- graduations evenly spaced
- labels aligned with major marks
- liquid surface clearly horizontal in simplified mode
- level intersects the intended graduation exactly
- no bubbles/decorative waves that create an ambiguous reading line

## Deterministic mapping

`tick_index = round(target / MINOR_DIVISION)` when zero baseline is used.

Require target within 0..MAX_CAPACITY and exactly representable by active minor division.

## Scientific meniscus mode

Only use if explicitly requested and grade appropriate. Define whether reading is at the bottom/top of meniscus and keep that convention consistent.

## QA

`CONTAINER_GEOMETRY_QA, GRADUATION_QA, LEVEL_ALIGNMENT_QA, LABEL_QA, TARGET_VOLUME_QA, UNIT_QA, MINIMUM_SIZE_QA`

Ambiguous or incorrect liquid level blocks release.