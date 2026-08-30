# CLOCK_READING_ENGINE — Analog Clock Reading

Version: 1.2.1
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`
Registry authority: `domains/DOMAIN_REGISTRY.md`

## Learning goal
Student reads hour and minute from an analog clock accurately and, when requested, connects one analog geometry to valid day/night 24-hour readings.

## Core parameters
`CLOCK_FORMAT=12_HOUR`, `MINUTE_GRANULARITY`, `SHOW_MINUTE_MARKS`, `SHOW_NUMBERS`, `HOUR_HAND_MODE`, `ANSWER_FORMAT`, `TARGET_TIMES`, `CLOCK_READING_MODE=SINGLE|DAY_NIGHT_PAIR`, `ANSWER_TIME_FORMAT=12_HOUR|24_HOUR`.

Suggested progression: EASY whole/half hours; MEDIUM 5-minute intervals; HARD 1-minute intervals when grade-appropriate.

## Geometry invariants
- perfect circular face in square reserved box
- exact center pivot
- exactly two instructional hands unless seconds requested
- minute hand visibly longer than hour hand
- 12 hour positions evenly spaced
- standard clockwise grammar: 12 top, 3 right, 6 bottom, 9 left
- no decorative pointer/hand

## Deterministic minute-mark topology
A clock is cyclic. For a full minute-mark face:
- exactly 60 equal minute intervals around 360°
- exactly 60 distinct minute positions
- 6° spacing
- 12 hour positions every fifth minute mark = 30°
- minute 0/60 is one shared position at 12; never duplicate the tick
- major hour marks may be stronger but do not add positions
- no missing/duplicated/merged/extra minute positions

## Continuous hand placement — CRITICAL
For analog time `h:m`:
- `minute_hand_angle_deg = 6*m` clockwise from 12
- `hour_hand_angle_deg = 30*(h mod 12) + 0.5*m` clockwise from 12

The hour hand moves continuously. It is permitted to point exactly at an hour numeral only when `m=00`.

Mandatory relational interpretation:
- `m=15` → hour hand is 25% of the way from h to h+1
- `m=30` → hour hand is exactly halfway from h to h+1
- `m=45` → hour hand is 75% of the way from h to h+1

Example: `10:30` MUST place the hour hand exactly halfway between 10 and 11; it MUST NOT point directly at 10.

Any rendered nonzero-minute clock whose hour hand remains on the original hour numeral is `CRITICAL_ACADEMIC`.

## Prompt serialization redundancy
For every item, the final image prompt MUST serialize both geometry and human-readable relation. Example renderer-only state:

`ITEM 4: semantic time=10:30; minute=30; minute_hand_angle=180°; minute hand exactly at 6; hour_hand_angle=315°; hour hand exactly halfway between 10 and 11; NEVER place hour hand directly on 10.`

Do not rely on only a semantic phrase such as “10:30”. Do not rely on only angles. Use both.

For all nonzero-minute items add an item-specific negative such as:
`WRONG: hour hand directly on the starting hour numeral.`

## DAY_NIGHT_PAIR
One question = one clock + two blank response fields. Do not create two clocks unless explicitly requested.

Thai mapping:
- h12 1–5: DAY=h+12, NIGHT=h
- h12 6–11: DAY=h, NIGHT=h+12
- h12=12: DAY=12, NIGHT=0
Minutes remain identical.

Verified day/night values remain internal when key is off. Renderer geometry may be serialized but must not be printed as answers.

## Layout
Preferred printed diameter >=30 mm for 5-minute reading; larger for 1-minute reading. For 10 items A4 portrait, first attempt 2×5 only if hand positions and minute marks remain distinguishable. Readability outranks one-page density.

## Mandatory final-prompt block
```text
CLOCK GEOMETRY — CRITICAL
- use one canonical circular clock template for all items
- exactly 12 hour positions; full minute face = exactly 60 distinct minute marks at 6° spacing
- exactly two hands; minute hand longer
- minute angle = 6*m
- hour angle = 30*(h mod 12)+0.5*m
- hour hand moves continuously; if m != 00 it must NOT stay on the hour numeral
- at :30 hour hand is exactly halfway between adjacent hour numerals
- serialize per-item semantic relation + exact angles + visual relation
- no decorative extra hands, no ellipse, no perspective, no missing/extra minute marks
```

## Post-render QA
Inspect every clock individually:
- 60 distinct minute positions when full marks shown
- exact hand count/length
- minute hand on target minute
- hour hand on computed continuous angle
- for every `m!=00`, verify hour hand is displaced from the hour numeral by `0.5*m` degrees
- for `:30`, verify midpoint visually and geometrically
- no answer leakage

## QA
`CLOCK_CIRCLE_QA, CLOCK_PIVOT_QA, HAND_COUNT_QA, HAND_LENGTH_QA, MINUTE_INTERVAL_COUNT_QA, MINUTE_POSITION_COUNT_QA, MINUTE_MARK_SPACING_QA, HOUR_POSITION_QA, HOUR_HAND_INTERPOLATION_QA, NONZERO_MINUTE_HOUR_DISPLACEMENT_QA, HALF_HOUR_MIDPOINT_QA, TARGET_TIME_QA, NO_MISSING_TICK_QA, NO_EXTRA_TICK_QA, MINIMUM_SIZE_QA, ONE_CLOCK_TWO_ANSWERS_QA, DAY_NIGHT_MAPPING_QA, DAY_NIGHT_ANSWER_LEAK_QA`.

Any wrong hand position, especially an hour hand pinned to the hour numeral when minutes are nonzero, blocks release.
