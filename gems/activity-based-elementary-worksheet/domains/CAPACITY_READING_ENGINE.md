# CAPACITY_READING_ENGINE — Capacity / Volume / Meniscus Rules

Version: 1.3.0
Status: PRODUCTION_CANDIDATE
Owning worker: `W05_TEMPERATURE_CAPACITY_VOLUME`
Requires `INSTRUMENT_READING_ENGINE.md` only when a learner reads a graduated container.

## 1. Scope

Supports:

- graduated capacity reading
- mL/L arithmetic and conversion
- simple flat liquid levels
- scientific meniscus when explicitly requested
- rectangular-prism volume
- simple composite rectangular-prism volume
- capacity-volume relation when explicitly part of the lesson

## 2. Exact relations

Capacity:

`1000 mL = 1 L`

Volume/capacity when explicitly taught:

`1 cm³ = 1 mL`
`1000 cm³ = 1 L`

Rectangular prism:

`V = length × width × height`

All dimensions must be in compatible units before multiplication.

## 3. Core parameters

`CAPACITY_SUBDOMAIN, SCALE_MIN, MAX_CAPACITY, MAJOR_DIVISION, MINOR_DIVISION, UNIT, TARGET_LEVELS, CONTAINER_TYPE, MENISCUS_MODE, MENISCUS_READ_POINT, CAPACITY_TASK_TYPE, SOLID_VOLUME_TASK, ANSWER_FORMAT`

## 4. Capacity arithmetic/conversion

Task types:

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

Canonical arithmetic base unit: millilitres for elementary L/mL tasks.

Process:

1. convert each quantity to mL;
2. compute exactly;
3. independently verify;
4. convert to requested answer format.

Do not add raw L and mL numerals before conversion.

## 5. Graduated-container geometry

- upright/front-facing container
- explicit active scale endpoints
- uniform graduations
- labels aligned to major ticks
- no perspective/skew/stretch
- no decorative waves/bubbles/tick-like lines that create competing readings
- locked template across repeated questions unless scale intentionally changes

## 6. Linear graduation topology

Let `d=MINOR_DIVISION`.

`EXPECTED_INTERVAL_COUNT = round((MAX_CAPACITY-SCALE_MIN)/d)`
`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

Require exact representability.

Examples:

- 0–1000 mL @100 mL → 10 intervals / 11 positions
- 0–1000 mL @50 mL → 20 / 21
- 500–1500 mL @100 mL → 10 / 11; do not invent zero outside active scale

## 7. Target mapping

`tick_index = round((target-SCALE_MIN)/d)`
`represented_value = SCALE_MIN + tick_index*d`

Require exact target representability unless interpolation is explicitly taught.

## 8. SIMPLE_FLAT

One horizontal instructional liquid surface intersects the exact target graduation centerline. No wave/slosh/bubble/second reading line.

## 9. SCIENTIFIC MENISCUS — critical

The selected reading point is academic data.

### READ_BOTTOM_MENISCUS
Use a clearly concave meniscus. The **lowest point** aligns exactly with the target graduation.

### READ_TOP_MENISCUS
Use a clearly convex/appropriate meniscus for the intended convention. The **highest designated reading point** aligns exactly with the target graduation.

A nearly flat ambiguous curve is insufficient in scientific mode.

Instructional explanation should normally appear once in instruction/example space, not as repeated target-revealing arrows beside every item.

## 10. Renderer-only state and label preservation

For each visual item serialize internally:

`TARGET VALUE + TICK INDEX + LEVEL RATIO + MENISCUS MODE/READ POINT + EXACT RELATION + HARD NEGATIVE`

Mark `RENDER_ONLY_NOT_FOR_WORKSHEET`.

Configured scale labels are legitimate instructional labels and must remain visible. Only item-specific target values are forbidden as extra callouts/answers when key is off.

## 11. Rectangular-prism volume

For dimensions `l,w,h` in compatible units:

`V=l×w×h`

If units differ, convert first.

For simple composite rectangular-prism shapes:

1. decompose into non-overlapping rectangular prisms;
2. compute each verified volume;
3. sum each component exactly once;
4. do not double-count overlap.

Complex solids outside this grammar must not be presented as specialized deterministic coverage.

## 12. Grade progression

Follow `MEASUREMENT_COVERAGE_P1_P6.md`.

Conservative defaults:

- P1–P2: direct comparison/simple L contexts only
- P3: mL/L reading and basic arithmetic
- P4: capacity conversion/arithmetic with integer relationships
- P5: rectangular-prism volume and capacity-volume relation when appropriate
- P6: multi-step capacity/volume and simple composite rectangular prisms

Scientific meniscus is not assumed merely because grade is higher; require explicit objective/context.

## 13. QA

Prompt-phase gates:

`PROMPT_CAPACITY_UNIT_COMPATIBILITY_QA`
`PROMPT_CAPACITY_CONVERSION_QA`
`PROMPT_CAPACITY_CALCULATION_QA`
`PROMPT_CAPACITY_TOPOLOGY_QA`
`PROMPT_CAPACITY_TARGET_REPRESENTABILITY_QA`
`PROMPT_LEVEL_ALIGNMENT_SPEC_QA`
`PROMPT_MENISCUS_CURVATURE_QA`
`PROMPT_MENISCUS_READ_POINT_QA`
`PROMPT_NO_COMPETING_LEVEL_QA`
`PROMPT_CAPACITY_LABEL_PRESERVATION_QA`
`PROMPT_VOLUME_FORMULA_QA`
`PROMPT_VOLUME_UNIT_COMPATIBILITY_QA`
`PROMPT_VOLUME_DECOMPOSITION_QA` when composite volume is used
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`

Artifact alignment/curvature/tick visual checks remain NOT TESTED until the rendered worksheet is inspected.

Wrong conversion, wrong volume formula, double-counted composite volume, wrong meniscus read point, ambiguous level, nonrepresentable target, or target-number leakage blocks prompt release.