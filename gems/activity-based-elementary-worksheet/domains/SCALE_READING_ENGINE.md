# SCALE_READING_ENGINE — Deterministic Dial-Scale Worksheet Rules

Version: 1.1.2
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`
Applies to: `DOMAIN=MEASUREMENT_WEIGHT`, `QUESTION_TYPE=DIAL_SCALE_READING`
Registry authority: `domains/DOMAIN_REGISTRY.md`

## Learning goal
Learner reads weight from a canonical graduated teaching dial: identify kilogram labels → count minor divisions → follow one needle → express kg + ขีด.

Thai Grade 3 default:
- 0–5 kg
- 1 kg major division
- 0.1 kg minor division
- 10 intervals/kg
- 1 ขีด = 0.1 kg = 100 g
- answer: `........ กิโลกรัม ........ ขีด`

## Mandatory geometry
- perfect front-facing circle
- exact center pivot and one needle
- no perspective/ellipse/skew/crop
- needle endpoint lands on the tick ring

## Canonical 5 kg teaching dial — CRITICAL
The value scale is NOT a 360° full circle.

Use exactly:
- 300° active sweep from 0→5
- 60° inactive gap from 5→0
- angle convention: 0° top, clockwise positive
- labels: 0@240°, 1@300°, 2@0°, 3@60°, 4@120°, 5@180°
- 1 kg = 60°
- 0.1 kg = 6°
- 50 active intervals
- 51 active tick positions including endpoints 0 and 5
- zero value ticks in the interior of the inactive 60° gap

A renderer that distributes 0–5 around a 360° circle or draws ticks continuously from 5 back to 0 has substituted the wrong instrument grammar and is `CRITICAL_ACADEMIC`.

## Target mapping
For target w:
`tick_index = round(w/0.1)`
`target_angle = (240 + 6*tick_index) mod 360`
Require exact representability.

## Prompt serialization redundancy
Per item serialize semantic value + tick index + relation + exact angle.
Example:
`ITEM 3: renderer-only target=2.4 kg; tick_index=24; fourth minor tick after 2; target_angle=24° clockwise from top; needle from exact center to that tick; DO NOT print 2.4 kg as an answer.`

## Mandatory final-prompt block
```text
CANONICAL 0–5 KG DIAL — NON-NEGOTIABLE
- DO NOT draw a 360-degree value scale
- reserve a clearly visible 60-degree inactive blank gap between endpoint 5 and endpoint 0
- no value ticks inside the inactive gap
- active value sweep is exactly 300 degrees
- labels locked: 0@240°,1@300°,2@0°,3@60°,4@120°,5@180°
- exactly 50 active intervals and 51 active tick positions
- exactly 10 equal minor intervals per kilogram
- one canonical template cloned for all items; only needle angle changes
- one centered needle; endpoint exactly on target tick
- no clock grammar, no extra labels, no continuous ticks through the inactive gap
```

## Whole-kilogram pedagogy
If the learning objective is kg+ขีด, do not generate an item set dominated by whole-kilogram targets. Ensure sufficient minor-tick targets so learners actually practice counting ขีด. A whole-kilogram-only set is allowed only when explicitly requested.

## Layout
For 10 items A4 portrait, first attempt 2×5. Preferred dial 32–42 mm; absolute minimum 30 mm for 0.1 kg reading. Reduce decoration before dial size.

## Post-render QA
Inspect every dial:
- true circle/center pivot/one needle
- labels at locked positions
- 300° active sweep visually evident
- 60° inactive gap visually evident
- no tick inside gap interior
- 50 intervals/51 positions
- target needle exact
- template unchanged across items

## QA
`DIAL_CIRCLE_QA, CENTER_PIVOT_QA, SINGLE_NEEDLE_QA, ACTIVE_SWEEP_QA, INACTIVE_GAP_QA, INACTIVE_GAP_TICK_QA, FULL_CIRCLE_SUBSTITUTION_QA, ENDPOINT_DISTINCT_QA, TICK_COUNT_QA, TICK_SPACING_QA, LABEL_POSITION_QA, NEEDLE_TARGET_QA, TEMPLATE_LOCK_QA, MINOR_TARGET_DISTRIBUTION_QA, DIAL_SIZE_QA, DIAL_CLEARANCE_QA`.

Any full-circle substitution, ticks in inactive gap, wrong count/label geometry, or incorrect target needle blocks release.
