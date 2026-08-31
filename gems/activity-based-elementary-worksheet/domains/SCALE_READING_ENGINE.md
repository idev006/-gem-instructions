# SCALE_READING_ENGINE — Weight / Dial Scale Rules

Version: 1.4.0
Status: PRODUCTION_CANDIDATE
Owning worker: `W03_WEIGHT_SCALE`
Requires `INSTRUMENT_READING_ENGINE.md` when a learner reads a dial.
Applies to: `DOMAIN=MEASUREMENT_WEIGHT`

## 1. Scope

Supports:

- dial scale reading
- kg/g/ขีด representation
- weight addition/subtraction/difference/comparison
- kg↔g conversion
- grade-appropriate mixed-unit weight problems

## 2. Exact weight relations

`1000 g = 1 kg`

Thai elementary context when applicable:

`1 ขีด = 100 g = 0.1 kg`

Canonical arithmetic base unit: grams for exact integer elementary weight calculations.

Before arithmetic:

1. convert all quantities to grams;
2. compute exactly;
3. independently verify;
4. convert to requested display unit/format.

## 3. Thai Grade 3 canonical dial default

- 0–5 kg
- 1 kg major division
- 0.1 kg minor division
- 10 intervals/kg
- answer: `........ กิโลกรัม ........ ขีด`

If the user specifies another valid dial capacity/resolution, derive its topology rather than silently forcing the 5 kg template.

## 4. Mandatory dial geometry

- perfect front-facing circle/arc template;
- no perspective/ellipse/skew/crop;
- one authoritative center `DIAL_CENTER=(cx,cy)`;
- `READING_RING_CENTER=DIAL_CENTER`;
- `NEEDLE_PIVOT=DIAL_CENTER`;
- exactly one instructional needle;
- needle endpoint lands on the exact target tick centerline of the authoritative reading ring.

Off-center pivot is an academic geometry failure even if the needle visually touches the intended tick.

## 5. Canonical 0–5 kg teaching dial — critical

The canonical value scale is **not** a 360° full-circle graduated value scale.

Angle convention:

`0° = top / 12 o'clock`
`CLOCKWISE_POSITIVE=YES`

Use exactly:

- `ACTIVE_START_ANGLE=0°` at 0 kg;
- `ACTIVE_SWEEP_DEG=300°`;
- `ACTIVE_END_ANGLE=300°` at 5 kg;
- `INACTIVE_GAP_START_ANGLE=300°`;
- `INACTIVE_GAP_END_ANGLE=360°/0°`;
- `INACTIVE_GAP_SWEEP_DEG=60°`;
- `INACTIVE_GAP_TICK_COUNT=0`;
- `INACTIVE_GAP_RADIAL_MARK_COUNT=0`;
- 1 kg = 60°;
- 0.1 kg = 6°;
- 50 active intervals;
- 51 active tick positions including endpoints.

Canonical labels:

`LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`

Major labels must increase clockwise in the exact sequence:

`CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]`

A counter-clockwise, rotated-without-state, scrambled, or duplicated label sequence is `CRITICAL_ACADEMIC`.

## 6. Target mapping

For canonical 0.1 kg profile:

`tick_index = round(w/0.1)`
`target_angle = (6*tick_index) mod 360`

Require exact representability.

Per-item renderer state:

`SEMANTIC TARGET + TICK INDEX + RELATION TO MAJOR LABEL + TARGET ANGLE + CENTER→TICK NEEDLE + ITEM HARD NEGATIVE`

Mark the whole state `RENDER_ONLY_NOT_FOR_WORKSHEET`.

## 7. Canonical-label preservation

Dial labels `0,1,2,3,4,5` are legitimate instructional labels and must remain visible in the canonical profile.

Leak guard forbids item-specific target text such as `1.2 kg` from being printed as an extra annotation or completed answer. It does **not** remove canonical scale labels.

## 8. Weight calculations

Task types:

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

Examples of valid internal process:

- `2 kg 300 g + 750 g` → normalize to grams → add → convert result as requested
- `3.4 kg` → 3400 g
- `18 ขีด` → 1800 g → 1.8 kg when such representation is grade-appropriate

Do not mix raw numerals across units without conversion.

## 9. Pedagogy

If the learning objective is kg+ขีด dial reading, do not let the set be dominated by whole-kilogram targets. Include sufficient non-whole targets unless whole-kilogram practice is explicitly requested.

Use `MEASUREMENT_COVERAGE_P1_P6.md` for conservative grade progression.

## 10. Layout/readability

For 10 canonical 0.1 kg dial items on A4 portrait, a 2×5 plan is a candidate only after numeric `PHYSICAL_PAGE_STATE` proof. Preferred selected diameter may be 32–42 mm; the stronger practical domain minimum is 30 mm unless a user/domain rule requires larger.

`SELECTED_RENDER_SIZE_MM` and `METROLOGY_MINIMUM_SIZE_MM` are distinct. Reduce decoration before dial size. Under one-page lock, fail feasibility rather than merge/omit ticks.

## 11. Active/gap geometry contract

Active positions are generated only by:

`active_tick_angle(i)=(6*i) mod 360, i=0..50`

The active set has exactly 51 physical tick positions.

Inside the open inactive arc `(300°,360°)` forbid all scale-like radial marks, including:

- minor or major value ticks;
- unlabeled pseudo-ticks;
- decorative rays, hatch marks or repeated short strokes;
- duplicate endpoint ticks displaced into the gap;
- border embellishments that visually continue the scale.

The outer housing may continue through the gap, but it is not a graduation.

## 12. Common-center contract

All radial geometry is generated from one center:

`DIAL_CENTER=(cx,cy)`
`READING_RING_CENTER=DIAL_CENTER`
`NEEDLE_PIVOT=DIAL_CENTER`

For any target angle θ, the needle ray must be collinear with the center-to-target-tick radius. Composition/layout may translate or uniformly scale the whole canonical dial, but may not move pivot, labels, ticks, or ring independently.

## 13. QA

Prompt-phase gates:

`PROMPT_WEIGHT_UNIT_COMPATIBILITY_QA`
`PROMPT_WEIGHT_CONVERSION_QA`
`PROMPT_WEIGHT_CALCULATION_QA`
`PROMPT_DIAL_TOPOLOGY_QA`
`PROMPT_ACTIVE_SWEEP_QA`
`PROMPT_INACTIVE_GAP_QA`
`PROMPT_NO_FULL_CIRCLE_SUBSTITUTION_QA`
`PROMPT_DIAL_INTERVAL_POSITION_COUNT_QA`
`PROMPT_DIAL_LABEL_POSITION_QA`
`PROMPT_DIAL_LABEL_ORDER_QA`
`PROMPT_DIAL_TARGET_REPRESENTABILITY_QA`
`PROMPT_NEEDLE_MAPPING_QA`
`PROMPT_DIAL_COMMON_CENTER_QA`
`PROMPT_MINOR_TARGET_DISTRIBUTION_QA`
`PROMPT_SCALE_LABEL_PRESERVATION_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`
`PROMPT_DIAL_GAP_GEOMETRY_SERIALIZATION_QA`
`PROMPT_DIAL_GAP_RADIAL_MARK_ZERO_QA`
`PROMPT_DIAL_ACTIVE_TICK_SET_QA`
`PROMPT_DIAL_CANONICAL_LABEL_ANGLE_QA`
`PROMPT_DIAL_GAP_DECORATION_ISOLATION_QA`

Artifact geometry is not PASS until the rendered worksheet is inspected.

Any wrong conversion/arithmetic, reversed/scrambled label sequence, full-circle substitution, ticks/pseudo-ticks in the inactive gap, off-center pivot, nonrepresentable target, or wrong needle mapping blocks prompt release.
