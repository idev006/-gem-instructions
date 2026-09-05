# Actual Clock Half-Hour Hand + Page Layout Defect — 2026-09-05

Status: CRITICAL_ACADEMIC + LAYOUT_DEFECT
Source: user-supplied rendered Thai P3 half-hour worksheet artifact
Scope: ANALOG_CLOCK / DAY_NIGHT_PAIR / 10 items / A4 portrait

## Observed defects

1. Several short/hour hands are not reliably placed at the exact formula-derived midpoint for :30.
2. The requested 10-item worksheet was rendered as five items on the shown page, implying pagination despite a valid 2×5 A4 portrait packing plan for the canonical profile.

## Academic truth

For every `h:30`:
`minute_angle=180°`
`hour_displacement=minute_angle/12=15°`
`hour_angle=30*(h mod 12)+15°`

The hour hand is exactly halfway from h toward h+1.

Example:
3:30 / 15:30:
- minute hand = 180°, numeral 6;
- hour hand = 105°, exact midpoint between 3 and 4.

## Layout truth

For the canonical Thai P3, DAY_NIGHT_PAIR, 10-item, strict :30 profile:
- A4 portrait 210×297 mm;
- margins 8 mm;
- header reserve 38 mm;
- usable 194×243 mm;
- grid 2 columns ×5 rows;
- item box 91×43 mm;
- gaps 4 mm;
- required grid 186×231 mm;
- therefore width and height both pass.

## Root cause class

- formula present but renderer not sufficiently bound to minute-hand-derived displacement;
- minute-hand driver policy not yet embedded everywhere in prior installer;
- one-page preference was treated as optional even after numeric feasibility had passed;
- no dedicated regression combined clock hand truth with the exact 10-item A4 profile.

## Required repair

- minute hand drives hour-hand displacement;
- exact vector endpoints remain mandatory;
- embed minute-driver policy in W02/W07/W08/W09/W10 and main instructions;
- bind the canonical 2×5 profile after numeric proof;
- add dedicated regression and CI gate.

## Phase verdict

The supplied artifact remains:
`ARTIFACT_CLOCK_MINUTE_HAND_DRIVER_QA=FAIL`
`ARTIFACT_CLOCK_HALF_HOUR_MIDPOINT_QA=FAIL`
`ARTIFACT_PAGE_COUNT_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

Future renders remain `NOT_YET_TESTED` until inspected.
