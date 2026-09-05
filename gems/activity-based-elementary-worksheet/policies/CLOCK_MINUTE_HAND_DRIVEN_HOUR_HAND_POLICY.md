# Clock Minute-Hand-Driven Hour-Hand Policy

Version: 1.0.0
Status: Mandatory analog-clock geometry policy
Applies to: ANALOG_CLOCK / W02 / W07 / W08 / W09 / W10

## Core principle

The hour hand position is not derived from the hour numeral alone.

For any analog clock with minutes, the minute hand is the causal driver of the hour-hand displacement within the current hour sector.

`MINUTE_HAND_DRIVES_HOUR_HAND_POSITION=YES`

## Canonical formula sequence

Compute in this order:

1. Parse semantic time `(H,M)`.
2. Compute minute-hand angle:
   `minute_hand_angle_deg = 6*M`
3. Compute hour-sector base:
   `hour_sector_base_deg = 30*(H mod 12)`
4. Compute hour-hand displacement from the minute hand:
   `hour_hand_displacement_deg = minute_hand_angle_deg / 12`
5. Compute final hour-hand angle:
   `hour_hand_angle_deg = hour_sector_base_deg + hour_hand_displacement_deg`

This is equivalent to:
`hour_hand_angle_deg = 30*(H mod 12) + 0.5*M`

The minute hand therefore determines how far the hour hand has progressed from the starting hour numeral toward the next hour numeral.

## Pedagogical interpretation

- If `minute_hand_angle_deg = 0°`, the hour hand is exactly on the hour numeral.
- If `minute_hand_angle_deg = 90°`, the hour hand has moved `7.5°` = 25% of the hour sector.
- If `minute_hand_angle_deg = 180°`, the hour hand has moved `15°` = 50% of the hour sector.
- If `minute_hand_angle_deg = 270°`, the hour hand has moved `22.5°` = 75% of the hour sector.

## Example: 15:30 / 3:30

`H=3`, `M=30`

`minute_hand_angle_deg = 6*30 = 180°`

`hour_sector_base_deg = 30*3 = 90°`

`hour_hand_displacement_deg = 180/12 = 15°`

`hour_hand_angle_deg = 90+15 = 105°`

Therefore:
- minute hand points to numeral 6;
- hour hand points exactly halfway between 3 and 4;
- hour hand must not point at 3.

## Hard negatives

- Do not place the hour hand by choosing the nearest hour numeral.
- Do not draw the hour hand at the starting hour numeral when `M != 0`.
- Do not treat `3:30` as `3:00` plus a minute hand.
- Do not let decoration, typography, or layout pressure reduce the computed displacement.
- Do not accept a clock whose hour hand is visually plausible but does not match `minute_hand_angle_deg / 12`.

## QA gates

`PROMPT_CLOCK_MINUTE_HAND_DRIVER_QA`
`PROMPT_CLOCK_HOUR_DISPLACEMENT_FROM_MINUTE_ANGLE_QA`
`PROMPT_CLOCK_HALF_HOUR_FROM_MINUTE_DRIVER_QA`
`ARTIFACT_CLOCK_MINUTE_HAND_DRIVER_QA`

Any violation is `CRITICAL_ACADEMIC` and blocks classroom release.