# Default Page + Weight Dial Render Profile

Version: 1.0.0
Status: Mandatory runtime/render contract
Compatible Gem baseline: 2.6.x
Owners/Auditors: `W03_WEIGHT_SCALE + W07_INSTRUMENT_AUDITOR + W10_METROLOGY_ENGINEER + W08_LAYOUT_RENDER_THAI + W09_QA_RELEASE`

## 1. Default page contract

When the user does not explicitly provide page size or orientation:

`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`
`PAGE_SIZE_PROVENANCE=SYSTEM_DEFAULT`
`ORIENTATION_PROVENANCE=SYSTEM_DEFAULT`

This is mandatory. Layout convenience, theme, renderer preference, image aspect ratio or question density MUST NOT silently change the page to Landscape, Letter, square canvas or another format.

A different page size/orientation is allowed only when the user explicitly requests it. The override must preserve provenance.

Required gate:
`PROMPT_DEFAULT_A4_PORTRAIT_QA`

## 2. Canonical Thai teaching weight dial

Applies to canonical `0–5 kg` dial with `0.1 kg` minor interval.

Exact relationships:

`1 kg = 10 ขีด`
`1 ขีด = 0.1 kg = 100 g`
`5 ขีด = 0.5 kg`

Canonical dial:
- 0 at top;
- values increase clockwise;
- integer labels `0,1,2,3,4,5`;
- each 1 kg span covers 60°;
- each 0.1 kg interval covers 6°;
- total active scale = 50 intervals / 51 endpoint-inclusive positions;
- inactive gap 5→0 = 60° and contains zero radial scale-like marks.

## 3. Per-kilogram visible tick grammar — MANDATORY

For every complete integer span `k → k+1`, `k=0..4`:

`INTERVALS_PER_KG=10`
`POSITIONS_PER_KG_ENDPOINT_INCLUSIVE=11`
`INTERIOR_TICK_COUNT_PER_KG=9`

Visible values are exactly:

`k+0.0, k+0.1, k+0.2, k+0.3, k+0.4, k+0.5, k+0.6, k+0.7, k+0.8, k+0.9, k+1.0`

Visible angle offsets from the span start are exactly:

`0°, 6°, 12°, 18°, 24°, 30°, 36°, 42°, 48°, 54°, 60°`

The renderer MUST physically draw all 11 endpoint-inclusive positions. It may not approximate the scale using fewer strokes.

## 4. Tick hierarchy

Within each 1 kg span:

- whole-kilogram endpoints (`index 0` and `index 10`) = MAJOR ticks;
- `index 5` = the existing +0.5 kg INTERMEDIATE tick;
- indices `1,2,3,4,6,7,8,9` = ordinary MINOR ticks.

The `index 5` / +0.5 kg tick MUST:
- be longer/more prominent than ordinary 0.1 kg minor ticks;
- be shorter/weaker than whole-kilogram major ticks;
- reuse the existing scale position;
- never create an additional graduation.

A recommended deterministic hierarchy is:

`MAJOR_TICK_LENGTH = 1.00 × hierarchy reference`
`INTERMEDIATE_TICK_LENGTH = 0.72–0.82 × major length`
`MINOR_TICK_LENGTH = 0.45–0.60 × major length`

Exact ratios may vary within those bands, but ordering MUST satisfy:

`MAJOR_LENGTH > INTERMEDIATE_LENGTH > MINOR_LENGTH`

## 5. Example span 0→1 kg

The physical sequence must be:

`0.0 major`
`0.1 minor`
`0.2 minor`
`0.3 minor`
`0.4 minor`
`0.5 INTERMEDIATE (longer)`
`0.6 minor`
`0.7 minor`
`0.8 minor`
`0.9 minor`
`1.0 major`

Thus there are exactly 10 spaces between 0 and 1 kg and exactly 9 interior marks. The fifth step is the 0.5 kg mark and is visually longer than the other minor marks.

The same grammar repeats identically for 1→2, 2→3, 3→4 and 4→5 kg.

## 6. Deterministic render serialization

The final prompt for this dial MUST serialize:

`VISIBLE_TICK_OFFSETS_PER_KG=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]`
`VISIBLE_TICK_ANGLE_OFFSETS_PER_KG=[0,6,12,18,24,30,36,42,48,54,60]`
`HALF_KG_INTERMEDIATE_INDEX=5`
`INTERIOR_TICK_COUNT_PER_KG=9`
`LOCAL_SPAN_VISIBLE_TICK_RECOUNT_REQUIRED=YES`

A prose-only statement such as `10 divisions per kg` is NOT sufficient by itself.

## 7. W07/W10 independent recount

For each span, W07 and W10 must independently verify:
- 10 intervals;
- 11 endpoint-inclusive positions;
- exactly 9 interior marks;
- the 5th interval position is +0.5 kg;
- only that midpoint interior mark uses intermediate hierarchy;
- 8 other interior marks use minor hierarchy;
- no missing, merged, duplicated or extra mark.

## 8. W08 renderer rule

W08 must preserve the explicit visible tick list in the `FINAL_IMAGE_GENERATION_PROMPT`. It must not summarize it away to a vague instruction such as `standard scale` or merely `10 divisions`.

If page density threatens readability, reduce decoration or paginate. Never delete graduations.

## 9. W09 release block

Required gates:

`PROMPT_WEIGHT_VISIBLE_TICK_SET_SERIALIZATION_QA`
`PROMPT_WEIGHT_PER_KG_VISIBLE_INTERVAL_COUNT_QA`
`PROMPT_WEIGHT_PER_KG_VISIBLE_POSITION_COUNT_QA`
`PROMPT_WEIGHT_INTERIOR_TICK_COUNT_QA`
`PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA`
`PROMPT_WEIGHT_VISIBLE_TICK_RECOUNT_PROTOCOL_QA`
`PROMPT_DEFAULT_A4_PORTRAIT_QA`

Any applicable FAIL or NOT_RUN blocks `PROMPT_RELEASE`.

## 10. Artifact rule

For an actual rendered 0–5 kg @0.1 kg teaching dial, inspect all five spans individually.

If any span has fewer or more than 10 intervals, fewer or more than 9 interior marks, or if the +0.5 kg mark is not visibly longer than ordinary minor marks, then:

`ARTIFACT_WEIGHT_DIAL_SUBDIVISION_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`
