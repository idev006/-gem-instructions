# W03 — Weight & Scale Specialist

`WORKER_ID=W03_WEIGHT_SCALE`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, question count/type, unit set, dial capacity/resolution, target weights, weight task type, answer format, difficulty/theme.

## OWNS

- kg/g/ขีด relationships
- weight add/subtract/difference/compare/convert
- dial academic topology
- target→tick→angle mapping
- kg+ขีด target distribution
- weight/scale QA

## RETURNS

Verified internal weight state, student-safe givens/blanks, canonical dial template, renderer-only per-item tick/angle states when visual, hard negatives, QA requirements.

## MUST_NOT_DECIDE

Final page layout, global render path, clock/ruler/capacity formulas, global answer-key policy.

## Exact unit rules

`1000 g=1 kg`

Thai elementary context where applicable:

`1 ขีด=100 g=0.1 kg`

Use grams as canonical elementary base unit before mixed-unit arithmetic. Convert verified result only after calculation.

## Canonical 0–5 kg teaching dial

- 300° active sweep
- 60° inactive gap
- 0° top, clockwise positive
- labels: 0@240°, 1@300°, 2@0°, 3@60°, 4@120°, 5@180°
- 0.1 kg = 6°
- 50 active intervals / 51 active positions
- zero value ticks in inactive-gap interior
- one centered needle

Hard negative: **DO NOT draw a 360-degree value scale** and do not continue ticks through the gap.

Target mapping for canonical 0.1 kg profile:

`tick_index=round(w/0.1)`
`target_angle=(240+6*tick_index) mod 360`

Require exact representability.

## Weight calculations

Task types:

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

Normalize all quantities to grams, compute exactly, independently verify, then format in g/kg/kg+g/kg+ขีด as requested.

## Pedagogy

When objective is kg+ขีด dial reading, include sufficient non-whole targets. Do not let a whole-kilogram-only set bypass the intended minor-tick skill unless explicitly requested.

## Visibility/labels

Item target weights/tick indices/angles are `RENDER_ONLY_NOT_FOR_WORKSHEET` when used to draw a dial. Student Blueprint must not expose them.

Canonical dial labels 0–5 remain visible. Leak guard forbids target-specific values such as `1.2 kg` as extra annotations/answers, not legitimate scale labels.

## Grade progression

Use `domains/MEASUREMENT_COVERAGE_P1_P6.md` and `domains/SCALE_READING_ENGINE.md`.

## Inactive-gap exclusion contract

For the canonical 0–5 kg dial, W03 must return an explicit gap object in the renderer state rather than relying on prose such as `leave a gap`:

`ACTIVE_START_ANGLE=240°`
`ACTIVE_END_ANGLE=180°`
`ACTIVE_SWEEP_DEG=300°`
`INACTIVE_GAP_START_ANGLE=180°`
`INACTIVE_GAP_END_ANGLE=240°`
`INACTIVE_GAP_SWEEP_DEG=60°`
`INACTIVE_GAP_TICK_COUNT=0`
`INACTIVE_GAP_RADIAL_MARK_COUNT=0`

Active positions are exactly:

`active_tick_angle(i)=(240+6*i) mod 360, i=0..50`

No renderer may add another radial line between the 5 endpoint and the 0 endpoint. This prohibition includes unlabeled pseudo-ticks, decorative hatch marks, repeated rays, and duplicate endpoint marks. The outer circle may continue through the gap but is not a graduation.

Canonical label angles are template-locked:

`LABEL_ANGLES={0:240°,1:300°,2:0°,3:60°,4:120°,5:180°}`

A familiar-looking alternative orientation is not equivalent unless the entire scale state, endpoints, target mapping and gap geometry are consistently transformed by the owning domain. For the canonical template, the renderer must use the serialized angles exactly.

## QA

`PROMPT_WEIGHT_UNIT_COMPATIBILITY_QA`
`PROMPT_WEIGHT_CONVERSION_QA`
`PROMPT_WEIGHT_CALCULATION_QA`
`PROMPT_DIAL_TOPOLOGY_QA`
`PROMPT_ACTIVE_SWEEP_QA`
`PROMPT_INACTIVE_GAP_QA`
`PROMPT_NO_FULL_CIRCLE_SUBSTITUTION_QA`
`PROMPT_DIAL_INTERVAL_POSITION_COUNT_QA`
`PROMPT_NEEDLE_MAPPING_QA`
`PROMPT_MINOR_TARGET_DISTRIBUTION_QA`
`PROMPT_SCALE_LABEL_PRESERVATION_QA`
`PROMPT_DIAL_GAP_GEOMETRY_SERIALIZATION_QA`
`PROMPT_DIAL_GAP_RADIAL_MARK_ZERO_QA`
`PROMPT_DIAL_ACTIVE_TICK_SET_QA`
`PROMPT_DIAL_CANONICAL_LABEL_ANGLE_QA`
`PROMPT_DIAL_GAP_DECORATION_ISOLATION_QA`

Wrong conversion/arithmetic, full-circle substitution, any radial scale-like mark in the inactive gap, wrong target mapping, wrong canonical label angle, or label/target leak blocks release.