# SCALE_READING_ENGINE — Weight / Dial Scale Rules

Version: 1.3.0
Status: PRODUCTION_CANDIDATE
Owning worker: `W03_WEIGHT_SCALE`
Requires `INSTRUMENT_READING_ENGINE.md` only when a learner reads a dial.
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

- perfect front-facing circle
- exact center pivot
- exactly one instructional needle
- no perspective/ellipse/skew/crop
- needle endpoint lands on the tick ring

## 5. Canonical 0–5 kg teaching dial — critical

The canonical value scale is **not** a 360° full circle.

Use exactly:

- 300° active sweep 0→5
- 60° inactive gap 5→0
- angle convention: 0° top, clockwise positive
- labels: 0@240°, 1@300°, 2@0°, 3@60°, 4@120°, 5@180°
- 1 kg = 60°
- 0.1 kg = 6°
- 50 active intervals
- 51 active tick positions including endpoints
- zero value ticks in inactive-gap interior

A 360° substitution or continuous tick ring through the inactive gap is `CRITICAL_ACADEMIC`.

## 6. Target mapping

For canonical 0.1 kg profile:

`tick_index = round(w/0.1)`
`target_angle = (240 + 6*tick_index) mod 360`

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

For 10 canonical 0.1 kg dial items on A4 portrait, first attempt 2×5 only if each dial remains large enough. Preferred diameter 32–42 mm; absolute minimum 30 mm for this dense scale.

Reduce decoration before dial size. Under one-page lock, fail feasibility rather than merge/omit ticks.

## 11. QA

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
`PROMPT_DIAL_TARGET_REPRESENTABILITY_QA`
`PROMPT_NEEDLE_MAPPING_QA`
`PROMPT_MINOR_TARGET_DISTRIBUTION_QA`
`PROMPT_SCALE_LABEL_PRESERVATION_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`

Artifact geometry is not PASS until the rendered worksheet is inspected.

Any wrong conversion/arithmetic, full-circle substitution, ticks in inactive gap, wrong label geometry, nonrepresentable target, or wrong needle mapping blocks prompt release.

## 12. Inactive-gap geometry contract — mandatory after 2026-08-31 artifact defect

The inactive gap is not merely a semantic statement. It is a geometric exclusion zone that must be serialized and independently audited.

Canonical 0–5 kg gap contract:

`ACTIVE_START_ANGLE=240°`
`ACTIVE_SWEEP_DEG=300°`
`ACTIVE_END_ANGLE=180°`
`INACTIVE_GAP_SWEEP_DEG=60°`
`INACTIVE_GAP_START_ANGLE=180°`
`INACTIVE_GAP_END_ANGLE=240°`
`INACTIVE_GAP_TICK_COUNT=0`
`INACTIVE_GAP_RADIAL_MARK_COUNT=0`

The active tick positions are generated only by:

`active_tick_angle(i)=(240 + 6*i) mod 360, i=0..50`

There are exactly 51 active tick positions. No additional radial line may be inserted between the active endpoint at 5 and the active endpoint at 0.

Inside the open 60° inactive arc, forbid all scale-like radial marks, including:

- minor or major value ticks;
- unlabeled pseudo-ticks;
- decorative rays, hatch marks or repeated short strokes;
- border embellishments that visually continue the scale;
- duplicate endpoint ticks displaced into the gap.

The circular outline may continue through the gap, but the outline is not a graduation. Labels and theme art must not create radial scale-like strokes there.

The canonical numeric label angles are locked to the canonical template and must be serialized exactly:

`LABEL_ANGLES={0:240°,1:300°,2:0°,3:60°,4:120°,5:180°}`

Rotating/rearranging the labels without rotating the entire canonical scale state is a template failure. A renderer must not independently invent a visually familiar 0-at-top layout when the supplied canonical template uses another orientation.

Mandatory additional gates:

`PROMPT_DIAL_GAP_GEOMETRY_SERIALIZATION_QA`
`PROMPT_DIAL_GAP_RADIAL_MARK_ZERO_QA`
`PROMPT_DIAL_ACTIVE_TICK_SET_QA`
`PROMPT_DIAL_CANONICAL_LABEL_ANGLE_QA`
`PROMPT_DIAL_GAP_DECORATION_ISOLATION_QA`

Artifact rule: one visible radial scale-like mark in the inactive gap is `P0_CRITICAL_ACADEMIC`, sets `ARTIFACT_QA=FAIL`, and blocks `CLASSROOM_RELEASE`.