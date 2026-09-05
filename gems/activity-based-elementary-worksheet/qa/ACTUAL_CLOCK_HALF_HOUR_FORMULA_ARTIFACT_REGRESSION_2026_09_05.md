# Actual Clock Half-Hour Formula Artifact Regression — 2026-09-05

Status: CRITICAL_ACADEMIC
Scope: Analog clock worksheet artifacts showing :30 times
Origin: User-supplied rendered worksheet image where minute hands point to 6 but hour hands still appear visually inconsistent with true half-hour positions.

## Root cause

The clock skill already contains the correct continuous hour-hand formula, but rendered artifacts can still fail when a downstream image renderer draws clock hands by visual approximation rather than by deterministic formula-derived endpoints.

For analog clock worksheets, a semantic phrase such as `1:30` is not sufficient. The final render state must include formula-derived hand angles, normalized endpoints, and a relation check for every item.

## External formula reference summary

The standard clock-angle formula uses:

- minute hand angle from 12 o'clock: `minute_angle = 6 × M`
- hour hand angle from 12 o'clock: `hour_angle = 30 × (H mod 12) + 0.5 × M`

This means the hour hand moves continuously by 0.5 degrees per minute.

## Half-hour rule

For every `H:30` clock:

- `minute_angle = 180°` so the long hand points exactly to 6;
- `hour_angle = 30 × (H mod 12) + 15°`;
- the short hand must be exactly halfway between numeral H and H+1;
- the short hand must never point directly at H.

Examples:

| Time | Minute hand | Hour hand angle | Required hour-hand relation |
|---|---:|---:|---|
| 1:30 / 13:30 | 180° | 45° | halfway between 1 and 2 |
| 2:30 / 14:30 | 180° | 75° | halfway between 2 and 3 |
| 3:30 / 15:30 | 180° | 105° | halfway between 3 and 4 |
| 4:30 / 16:30 | 180° | 135° | halfway between 4 and 5 |
| 5:30 / 17:30 | 180° | 165° | halfway between 5 and 6 |
| 6:30 / 18:30 | 180° | 195° | halfway between 6 and 7 |
| 7:30 / 19:30 | 180° | 225° | halfway between 7 and 8 |
| 8:30 / 20:30 | 180° | 255° | halfway between 8 and 9 |
| 9:30 / 21:30 | 180° | 285° | halfway between 9 and 10 |
| 10:30 / 22:30 | 180° | 315° | halfway between 10 and 11 |
| 11:30 / 23:30 | 180° | 345° | halfway between 11 and 12 |
| 12:30 / 00:30 | 180° | 15° | halfway between 12 and 1 |

## Release-blocking rule

If a rendered `:30` clock has the minute hand at 6 but the hour hand remains at the starting hour numeral or is not visually/geometrically halfway toward the next numeral, then:

`ARTIFACT_CLOCK_HALF_HOUR_MIDPOINT_QA=FAIL`

`ARTIFACT_CLOCK_HAND_FORMULA_QA=FAIL`

`ARTIFACT_QA=FAIL`

`CLASSROOM_RELEASE=BLOCKED`

## Required repair

Regenerate the clock from canonical formula-derived state. Do not visually nudge or redraw the short hand by eye.

Required item state:

- `SEMANTIC_TARGET`
- `MINUTE_HAND_ANGLE_DEG=180`
- `HOUR_HAND_ANGLE_DEG=30*(H mod 12)+15`
- `HOUR_HAND_RELATION=exactly halfway between H and H+1`
- `MINUTE_ENDPOINT_NORMALIZED`
- `HOUR_ENDPOINT_NORMALIZED`
- `ITEM_SPECIFIC_HARD_NEGATIVE=Do not place the hour hand on the starting hour numeral for :30`

## Boundary

This regression documents the artifact failure mode and the formula oracle. It does not by itself certify future rendered worksheets. Future worksheets still require actual Artifact QA.
