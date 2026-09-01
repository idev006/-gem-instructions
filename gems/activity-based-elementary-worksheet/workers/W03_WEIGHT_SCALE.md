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

### Per-kilogram subdivision hierarchy

Every complete 1 kg span must serialize and verify:

`INTERVALS_PER_KG=10`
`POSITIONS_PER_KG_ENDPOINT_INCLUSIVE=11`
`INTERIOR_POSITIONS_PER_KG_SPAN=9`
`HALF_KG_INTERMEDIATE_OFFSET=0.5`
`HALF_KG_INTERMEDIATE_TICK_REUSES_EXISTING_POSITION=YES`

Within each 1 kg span, the whole-kilogram endpoints are major ticks; the existing +0.5 kg position is an intermediate tick; all other interior 0.1 kg positions are ordinary minor ticks. The +0.5 kg intermediate tick must be visually longer/more prominent than ordinary minor ticks but shorter/weaker than a whole-kilogram major tick. It never creates an extra graduation.

### Visible tick-set serialization — MANDATORY

The renderer must receive the physical graduation set explicitly; numeric interval counts alone are not sufficient.

For every integer kilogram span `k → k+1`, `k=0..4`:

`VISIBLE_TICK_OFFSETS_PER_KG={0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0}`
`VISIBLE_TICK_ANGLE_OFFSETS_PER_KG={0°,6°,12°,18°,24°,30°,36°,42°,48°,54°,60°}`
`HALF_KG_INTERMEDIATE_INDEX=5`
`LOCAL_SPAN_VISIBLE_TICK_RECOUNT_REQUIRED=YES`

Therefore the 0→1 kg span is exactly:

`0.0@0°, 0.1@6°, 0.2@12°, 0.3@18°, 0.4@24°, 0.5@30°, 0.6@36°, 0.7@42°, 0.8@48°, 0.9@54°, 1.0@60°`.

Every one of those 11 endpoint-inclusive positions must be physically drawn. The renderer must not simplify the scale to fewer visible graduations for aesthetics, spacing, theme, or page density.

For each span, W03 must provide or require a visible recount:
- 10 spaces between adjacent whole-kilogram labels;
- 9 interior graduation marks;
- the fifth interval (+0.5 kg) is the single intermediate hierarchy mark;
- 8 other interior marks are ordinary 0.1 kg minor ticks.

Hard negative:

`DO NOT simplify, omit, merge, or sparsify 0.1 kg graduations between whole-kilogram labels.`

Hard negatives:

- **DO NOT** reverse the label sequence;
- **DO NOT** rotate labels independently from ticks/needle mapping;
- **DO NOT** draw a 360° value scale;
- **DO NOT** continue ticks through the 5→0 gap;
- **DO NOT** move the needle pivot away from the center used to construct the reading ring;
- **DO NOT** render all ten 0.1 kg subdivisions with identical hierarchy when the canonical teaching profile requires the +0.5 kg intermediate tick;
- **DO NOT** add an extra tick at +0.5 kg;
- **DO NOT** reduce the number of visible 0.1 kg graduations between integer labels.

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
`PROMPT_WEIGHT_PER_KG_SUBDIVISION_QA`
`PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA`
`PROMPT_WEIGHT_VISIBLE_TICK_SET_SERIALIZATION_QA`
`PROMPT_WEIGHT_PER_KG_VISIBLE_INTERVAL_COUNT_QA`
`PROMPT_WEIGHT_PER_KG_VISIBLE_POSITION_COUNT_QA`
`PROMPT_WEIGHT_VISIBLE_TICK_RECOUNT_PROTOCOL_QA`

Wrong conversion/arithmetic, reversed/scrambled major-label order, wrong per-kilogram subdivision or missing/extra half-kilogram hierarchy mark, missing/sparsified 0.1 kg visible graduations, full-circle substitution, any radial scale-like mark in the inactive gap, off-center pivot, wrong target mapping, wrong canonical label angle, or label/target leak blocks release.
