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

The canonical classroom orientation is intentionally simple and monotonic:

- angle convention: `0° = top / 12 o'clock`, clockwise positive;
- label `0` is at the top;
- values increase clockwise around the active scale;
- labels: `0@0°`, `1@60°`, `2@120°`, `3@180°`, `4@240°`, `5@300°`;
- 300° active sweep from 0→5;
- 60° inactive gap from the 5 kg endpoint at 300° back to the 0 kg endpoint at 360°/0°;
- 0.1 kg = 6°;
- 50 active intervals / 51 endpoint-inclusive active positions;
- zero instructional or decorative radial scale-like marks in the open inactive gap;
- one instructional needle;
- `NEEDLE_PIVOT == DIAL_CENTER == ACTIVE_TICK_RING_CENTER` exactly.

Hard negatives:

- **DO NOT** reverse the label sequence;
- **DO NOT** rotate labels independently from ticks/needle mapping;
- **DO NOT** draw a 360° value scale;
- **DO NOT** continue ticks through the 5→0 gap;
- **DO NOT** move the needle pivot away from the center used to construct the reading ring.

Target mapping for canonical 0.1 kg profile:

`tick_index=round(w/0.1)`
`target_angle=(6*tick_index) mod 360`

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

For the canonical 0–5 kg dial, W03 must return an explicit geometric state rather than prose such as `leave a gap`:

`ACTIVE_START_ANGLE=0°`
`ACTIVE_END_ANGLE=300°`
`ACTIVE_SWEEP_DEG=300°`
`INACTIVE_GAP_START_ANGLE=300°`
`INACTIVE_GAP_END_ANGLE=360°/0°`
`INACTIVE_GAP_SWEEP_DEG=60°`
`INACTIVE_GAP_TICK_COUNT=0`
`INACTIVE_GAP_RADIAL_MARK_COUNT=0`

Active positions are exactly:

`active_tick_angle(i)=(6*i) mod 360, i=0..50`

There are exactly 51 active tick positions. No renderer may add another radial line inside the open arc `(300°,360°)`. This prohibition includes unlabeled pseudo-ticks, decorative hatch marks, repeated rays, and duplicate endpoint marks. The outer housing/arc may continue through the gap but is not a graduation.

Canonical label angles are template-locked:

`LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`

Label-order oracle:

`CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]`

The renderer must verify both angle association and monotonic label order. A visually plausible but counter-clockwise or scrambled sequence is `CRITICAL_ACADEMIC`.

## Common-center contract

For every radial dial:

`DIAL_CENTER=(cx,cy)`
`READING_RING_CENTER=DIAL_CENTER`
`NEEDLE_PIVOT=DIAL_CENTER`

The needle is a radial segment beginning at `DIAL_CENTER` and directed at `target_angle`. Its endpoint must intersect the target graduation on the authoritative reading ring. Moving the pivot to improve composition is forbidden.

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
`PROMPT_DIAL_COMMON_CENTER_QA`
`PROMPT_MINOR_TARGET_DISTRIBUTION_QA`
`PROMPT_SCALE_LABEL_PRESERVATION_QA`
`PROMPT_DIAL_LABEL_ORDER_QA`
`PROMPT_DIAL_GAP_GEOMETRY_SERIALIZATION_QA`
`PROMPT_DIAL_GAP_RADIAL_MARK_ZERO_QA`
`PROMPT_DIAL_ACTIVE_TICK_SET_QA`
`PROMPT_DIAL_CANONICAL_LABEL_ANGLE_QA`
`PROMPT_DIAL_GAP_DECORATION_ISOLATION_QA`

Wrong conversion/arithmetic, reversed/scrambled major-label order, full-circle substitution, any radial scale-like mark in the inactive gap, off-center pivot, wrong target mapping, wrong canonical label angle, or label/target leak blocks release.
