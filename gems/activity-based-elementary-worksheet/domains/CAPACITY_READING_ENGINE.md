# CAPACITY_READING_ENGINE — Graduated Capacity / Volume Reading

Version: 1.2.1
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal
Student reads volume/capacity from a graduated container using a clear, deterministic scale.

## Core parameters
`SCALE_MIN, MAX_CAPACITY, MAJOR_DIVISION, MINOR_DIVISION, UNIT=L|ML, TARGET_LEVELS, CONTAINER_TYPE, MENISCUS_MODE=SIMPLE_FLAT|SCIENTIFIC, MENISCUS_READ_POINT=BOTTOM|TOP`.

## Geometry invariants
- container upright/front-facing
- no perspective/skew/stretch
- scale endpoints explicit
- graduations uniformly spaced
- labels aligned with major ticks
- no decorative waves/bubbles/lines that create competing reading levels
- identical orientation/direction within a locked template

## Deterministic graduation structure
Let `d=MINOR_DIVISION`.

`EXPECTED_INTERVAL_COUNT = round((MAX_CAPACITY-SCALE_MIN)/d)`
`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

Require exact representability. Examples:
- 0–1000 mL @100 mL → 10 intervals / 11 positions
- 0–1000 mL @50 mL → 20 / 21
- 500–1500 mL @100 mL → 10 / 11; do not invent zero outside active scale

## Deterministic target mapping
`tick_index = round((target-SCALE_MIN)/d)`
`represented_value = SCALE_MIN + tick_index*d`

Require exact target representability unless interpolation is explicitly part of the learning objective.

## SIMPLE_FLAT
Liquid surface is a single horizontal instructional line. It must intersect the exact target graduation centerline. No visual wave, slosh, bubble or second line may create ambiguity.

## SCIENTIFIC MENISCUS — CRITICAL
The selected reading point is academic data.

### READ_BOTTOM_MENISCUS
Use a clearly concave meniscus. The **lowest point of the curved surface** must align exactly with the target graduation.

### READ_TOP_MENISCUS
Use a clearly convex/appropriate meniscus for the intended scientific convention. The **highest designated reading point of the curved surface** must align exactly with the target graduation.

The prompt must define the curve and the reading point. A nearly flat ambiguous line is not sufficient when `SCIENTIFIC` mode is requested.

## Prompt serialization redundancy
For every item serialize:
- target renderer value
- tick index
- level ratio
- meniscus mode/read point
- exact relational wording

Example:
`ITEM 2: target renderer state=76 mL; target tick index=28 on the configured 2 mL scale; READ_TOP_MENISCUS; highest designated point of the curved meniscus intersects that target graduation exactly; DO NOT print “76” as an added scale label, arrow caption, or answer.`

## Renderer-only target-value leak guard
Target values used to place liquid are `RENDER_ONLY_NOT_VISIBLE` unless they are canonical printed scale labels already required by the scale.
The renderer MUST NOT add target-specific numbers beside the scale, beside an arrow, or inside the item card.

Instructional arrows explaining meniscus convention should normally appear once in the worksheet instruction/example area, not repeated beside every item unless explicitly pedagogically required. Repeated arrows must never expose target numbers.

## Mandatory final-prompt block
```text
CAPACITY / MENISCUS GEOMETRY — CRITICAL
- compute exact scale interval and graduation counts before drawing
- every target must be exactly representable by the configured minor division unless interpolation is explicitly intended
- SIMPLE_FLAT: one horizontal surface exactly on target graduation
- READ_BOTTOM_MENISCUS: lowest point of concave meniscus exactly on target graduation
- READ_TOP_MENISCUS: highest designated reading point exactly on target graduation
- the meniscus curvature and reading point must be visually unambiguous
- renderer-only target numbers must never appear as extra labels, annotations, arrow text, or answers
- no extra/missing/duplicate graduations and no decorative competing reading lines
```

## Post-render QA
Inspect every container individually:
- active range/count/spacing
- target graduation exists
- designated reading point coincides with target tick centerline
- correct meniscus curvature/convention
- no ambiguous second reading line
- no target-value leakage

## QA
`CONTAINER_GEOMETRY_QA, SCALE_RANGE_QA, SCALE_DIRECTION_QA, INTERVAL_COUNT_QA, GRADUATION_COUNT_QA, TICK_SPACING_QA, MAJOR_MINOR_QA, NO_MISSING_TICK_QA, NO_EXTRA_TICK_QA, TARGET_REPRESENTABILITY_QA, LEVEL_ALIGNMENT_QA, MENISCUS_CURVATURE_QA, MENISCUS_READ_POINT_QA, NO_COMPETING_LEVEL_QA, TARGET_VALUE_LEAK_QA, LABEL_QA, UNIT_QA, MINIMUM_SIZE_QA`.

Wrong reading point, ambiguous meniscus, wrong graduation count, nonrepresentable target, or visible renderer-only target value blocks release.
