# CLOCK_READING_ENGINE — Analog Clock Reading

Version: 1.0.0
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal

Student reads hour and minute from an analog clock accurately.

## Core parameters

`CLOCK_FORMAT=12_HOUR`, `MINUTE_GRANULARITY`, `SHOW_MINUTE_MARKS`, `SHOW_NUMBERS`, `HOUR_HAND_MODE`, `ANSWER_FORMAT`, `TARGET_TIMES`

Suggested defaults by progression:

- EASY: whole hours / half hours
- MEDIUM: 5-minute intervals
- HARD: 1-minute intervals when grade-appropriate

## Geometry invariants

- true circular clock face in square reserved box
- exact center pivot
- exactly two instructional hands unless seconds are explicitly requested
- minute hand visibly longer than hour hand
- 12 hour positions evenly spaced
- 60 minute intervals when minute-level reading is required
- standard clockwise clock grammar 12 at top, 3 right, 6 bottom, 9 left
- no decorative pointer or hand

## Hand placement

For time `h:m`:

- minute-hand angle = `6*m` degrees clockwise from 12
- hour-hand angle = `30*(h mod 12) + 0.5*m` degrees clockwise from 12

The hour hand MUST move continuously between hour marks. At 7:30 it must be halfway between 7 and 8, not fixed at 7.

Compile both semantic and geometric instructions.

## Layout/readability

Preferred printed clock diameter >= 30 mm for 5-minute reading; increase for 1-minute reading.

## QA

`CLOCK_CIRCLE_QA, CLOCK_PIVOT_QA, HAND_COUNT_QA, HAND_LENGTH_QA, MINUTE_MARK_QA, HOUR_HAND_INTERPOLATION_QA, TARGET_TIME_QA, MINIMUM_SIZE_QA`

Any wrong hand position blocks release.