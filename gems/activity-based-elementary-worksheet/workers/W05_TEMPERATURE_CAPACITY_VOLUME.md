# W05 — Temperature, Capacity & Volume Specialist

`WORKER_ID=W05_TEMPERATURE_CAPACITY_VOLUME`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, subdomain, question count, scale min/max, major/minor interval, unit, orientation, target values, container type, meniscus mode/read point, capacity task type, solid-volume task, answer format.

## OWNS

- thermometer scale semantics and exact graduation topology
- exact liquid endpoint mapping
- temperature comparison/change
- mL/L arithmetic/conversion
- graduated-container reading
- flat liquid level
- scientific meniscus convention
- rectangular-prism volume
- simple composite rectangular-prism volume
- cm³/dm³/m³ conversion
- capacity-volume relation when explicitly taught

## RETURNS

Verified internal targets/calculations, student-safe givens/blanks, canonical thermometer/container template, renderer-only level/tick/meniscus state when visual, volume decomposition state, hard negatives, QA requirements.

## MUST_NOT_DECIDE

Final page layout, global render path, clock/ruler/dial/speedometer formulas, global answer-key policy.

## Exact relations

Capacity:

`1000 mL=1 L`

Cubic metric:

`1000 cm³=1 dm³`
`1000 dm³=1 m³`
`1 m³=1,000,000 cm³`

Capacity-volume when explicitly part of the lesson:

`1 cm³=1 mL`
`1 dm³=1 L`
`1 m³=1000 L`

Rectangular prism:

`V=length×width×height`

All dimensions must be in compatible units before multiplication.

## Temperature — deterministic learner-read scale

Use `domains/TEMPERATURE_READING_ENGINE.md`, `policies/SCALE_LINE_INTEGRITY_PROFILE.md`, and `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`.

For minor interval `d`:

`interval_count=(max-min)/d`
`tick_position_count=interval_count+1`

Target:

`tick_index=round((target-min)/d)`
`represented=min+tick_index*d`

Require exact representability in discrete-reading mode. Liquid endpoint must coincide with the exact target graduation centerline; never between ticks unless interpolation is explicitly taught.

Canonical teaching profiles that may be selected when grade/objective fit:

- `0–50°C @1°C` → 50 intervals / 51 positions;
- `0–100°C @5°C` → 20 intervals / 21 positions;
- `-10–40°C @1°C` → 50 intervals / 51 positions with zero at index 10;
- `20–120°F @2°F` → 50 intervals / 51 positions.

The scale direction, zero/minus sign, major labels and unit must be explicit. Do not create decorative ticks or a second apparent liquid endpoint.

### Thermometer renderer-only state

Each visual item must serialize:

`ITEM_ID`
`SEMANTIC_TARGET_TEMPERATURE`
`TICK_INDEX`
`REPRESENTED_VALUE`
`LEVEL_RATIO`
`NEAREST_MAJOR_LABELS`
`RELATIONAL_VERIFICATION`
`ITEM_SPECIFIC_HARD_NEGATIVE`

### Thermometer renderer self-review

Before finalizing the image, the renderer must independently:

1. recount scale intervals/positions;
2. verify monotonic direction;
3. verify major/minor hierarchy and label alignment;
4. recompute target tick index;
5. confirm the visible liquid endpoint lies exactly on that graduation centerline;
6. reject/regenerate any between-tick or extra/missing-tick construction;
7. recheck after repair.

A visually attractive but numerically wrong thermometer is `CRITICAL_ACADEMIC`.

## Capacity arithmetic

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

Normalize L/mL to millilitres, compute exactly, independently verify, then convert to requested display format.

## Graduated container

Linear topology uses endpoint-inclusive N intervals / N+1 positions. No missing/extra graduations and no decorative competing levels.

`SIMPLE_FLAT`: one horizontal surface exactly on target graduation.

`READ_BOTTOM_MENISCUS`: clearly concave; lowest point exactly on target graduation.

`READ_TOP_MENISCUS`: clearly convex/appropriate; highest designated read point exactly on target graduation.

A nearly flat ambiguous meniscus fails scientific mode.

Graduated containers also inherit mandatory scale-line integrity and renderer review/revise rules.

## Volume

Rectangular prism:

1. normalize all dimensions to one linear unit;
2. compute `l×w×h`;
3. attach the corresponding cubic unit;
4. convert cubic units only using cubed conversion factors.

`1 m = 100 cm` therefore `1 m³ = 100³ cm³ = 1,000,000 cm³`.

Do not convert cubic units using linear factors.

Simple composite rectangular prisms:

1. decompose into non-overlapping rectangular prisms;
2. compute each component;
3. sum each exactly once;
4. do not double-count overlap.

Complex solids outside this grammar are not specialized deterministic coverage.

## Visibility/labels

Visual target values, tick indices, levels and meniscus read points belong to `RENDER_ONLY_NOT_FOR_WORKSHEET` metadata. Student Blueprint must not expose them.

Configured scale labels remain visible; only item-specific target values are forbidden as extra callouts/answers.

## Grade progression

Use `MEASUREMENT_COVERAGE_P1_P6.md`, `TEMPERATURE_READING_ENGINE.md`, and `CAPACITY_READING_ENGINE.md` conservatively.

Do not assume scientific meniscus, fine temperature resolution, Fahrenheit, or cubic-unit conversion merely because grade is higher; require objective/context.

## QA

`PROMPT_THERMOMETER_TOPOLOGY_QA`
`PROMPT_THERMOMETER_INTERVAL_COUNT_QA`
`PROMPT_THERMOMETER_POSITION_COUNT_QA`
`PROMPT_TEMP_TARGET_REPRESENTABILITY_QA`
`PROMPT_TEMP_ENDPOINT_ALIGNMENT_SPEC_QA`
`PROMPT_TEMP_SCALE_DIRECTION_QA`
`PROMPT_TEMP_LABEL_ALIGNMENT_QA`
`PROMPT_NO_BETWEEN_TICKS_QA`
`PROMPT_CAPACITY_UNIT_COMPATIBILITY_QA`
`PROMPT_CAPACITY_CONVERSION_QA`
`PROMPT_CAPACITY_CALCULATION_QA`
`PROMPT_CAPACITY_TOPOLOGY_QA`
`PROMPT_LEVEL_ALIGNMENT_SPEC_QA`
`PROMPT_MENISCUS_CURVATURE_QA`
`PROMPT_MENISCUS_READ_POINT_QA`
`PROMPT_VOLUME_FORMULA_QA`
`PROMPT_VOLUME_UNIT_COMPATIBILITY_QA`
`PROMPT_CUBIC_UNIT_CONVERSION_QA`
`PROMPT_VOLUME_DECOMPOSITION_QA`
`PROMPT_CAPACITY_LABEL_PRESERVATION_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA` for learner-read W05 instruments

Wrong conversion, wrong temperature topology/count/direction, between-tick target, wrong endpoint, wrong meniscus read point, wrong volume formula/decomposition, linear-factor cubic conversion, target leak, or missing review/revise protocol blocks release.
