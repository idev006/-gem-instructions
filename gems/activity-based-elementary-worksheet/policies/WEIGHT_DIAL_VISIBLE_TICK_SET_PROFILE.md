# Weight Dial Visible Tick-Set Profile — Canonical 0–5 kg Teaching Dial

Version: 1.0.0
Status: MANDATORY domain-specific runtime policy
Compatible Gem baseline: 2.6.x
Applies to: `W03_WEIGHT_SCALE + W07_INSTRUMENT_AUDITOR + W08_LAYOUT_RENDER_THAI + W09_QA_RELEASE + W10_METROLOGY_ENGINEER`

## Educational safety rule

For a learner-read 0–5 kg dial with `MINOR_INTERVAL=0.1 kg`, the visible graduation set itself is academic data.

A renderer may NOT preserve only the integer labels while simplifying the physical minor ticks.

`ONE MISSING 0.1 KG GRADUATION = ARTIFACT_QA FAIL`

## Canonical topology

- range: 0–5 kg
- 1 ขีด = 0.1 kg = 100 g
- active sweep: 300°
- angle convention: 0° at top, clockwise positive
- total active intervals: 50
- total endpoint-inclusive active positions: 51
- active tick angle: `tick_angle(i)=6*i degrees`, `i=0..50`
- inactive gap: open arc `(300°,360°)`
- radial scale-like marks in inactive gap: 0

## Per-kilogram visible tick-set contract

Every complete 1 kg span contains exactly 10 equal intervals and exactly 11 endpoint-inclusive graduation positions.

For integer kilogram `k` where `k=0..4`, the physical positions in span `k → k+1` are:

`k+0.0, k+0.1, k+0.2, k+0.3, k+0.4, k+0.5, k+0.6, k+0.7, k+0.8, k+0.9, k+1.0`

There are exactly 9 interior positions in each span.

The corresponding angles are:

`60*k + {0°,6°,12°,18°,24°,30°,36°,42°,48°,54°,60°}`

Example 0→1 kg:

`0.0@0°, 0.1@6°, 0.2@12°, 0.3@18°, 0.4@24°, 0.5@30°, 0.6@36°, 0.7@42°, 0.8@48°, 0.9@54°, 1.0@60°`

A renderer must physically draw every one of these graduation positions. It must not reduce the span to 5 intervals, 6 intervals, or any visually simplified subset.

## Mutually exclusive hierarchy

Within each 1 kg span:

- major: whole-kilogram endpoints (`j=0` and `j=10`)
- intermediate: midpoint only (`j=5`, +0.5 kg)
- ordinary minor: `j in {1,2,3,4,6,7,8,9}`

The midpoint is one existing position, not an extra graduation.

Visual hierarchy:

`major_length > intermediate_length > minor_length`

and

`major_stroke >= intermediate_stroke >= minor_stroke`

The hierarchy must never remove any required position.

## Mandatory final-prompt serialization

For canonical 0–5 kg @0.1 kg, final renderer prompt must include all of:

`INTERVALS_PER_KG=10`
`POSITIONS_PER_KG_ENDPOINT_INCLUSIVE=11`
`INTERIOR_POSITIONS_PER_KG_SPAN=9`
`VISIBLE_TICK_OFFSETS_PER_KG={0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0}`
`VISIBLE_TICK_ANGLE_OFFSETS_PER_KG={0°,6°,12°,18°,24°,30°,36°,42°,48°,54°,60°}`
`HALF_KG_INTERMEDIATE_INDEX=5`
`LOCAL_SPAN_VISIBLE_TICK_RECOUNT_REQUIRED=YES`

Hard negative:

`DO NOT simplify, omit, merge, or sparsify 0.1 kg graduations between whole-kilogram labels.`

## Independent audit requirements

W07 and W10 must independently verify every adjacent whole-kilogram span.

For each span, expected:
- 10 intervals
- 11 endpoint-inclusive positions
- 9 interior positions
- 1 midpoint intermediate position
- 8 ordinary interior minor positions

The audit is not satisfied by checking global 50/51 alone.

## Renderer review

For every generated weight dial, renderer self-review must:
1. select each span `0→1`, `1→2`, `2→3`, `3→4`, `4→5`;
2. physically count 10 spaces between integer marks;
3. physically count 9 interior graduation marks;
4. confirm +0.5 kg is the fifth interval and has intermediate hierarchy;
5. confirm no required 0.1 kg position is missing or merged;
6. regenerate the dial if any span fails.

## Release gates

`PROMPT_WEIGHT_VISIBLE_TICK_SET_SERIALIZATION_QA`
`PROMPT_WEIGHT_PER_KG_VISIBLE_INTERVAL_COUNT_QA`
`PROMPT_WEIGHT_PER_KG_VISIBLE_POSITION_COUNT_QA`
`PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA`
`PROMPT_WEIGHT_VISIBLE_TICK_RECOUNT_PROTOCOL_QA`

Any FAIL or NOT_RUN blocks prompt release.

Artifact rule:

If any rendered whole-kilogram span contains fewer or more than 10 intervals, or fewer/more than 9 interior graduations, set:

`ARTIFACT_WEIGHT_PER_KG_SUBDIVISION_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`
