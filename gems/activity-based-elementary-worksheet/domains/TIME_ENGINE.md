# TIME_ENGINE — Elapsed-Time Worksheet Rules

Version: 1.0.0
Status: PRODUCTION_HARDENED

Applies to elapsed time from start/end times and closely related duration tasks.

## Core parameters

`TIME_FORMAT, START_TIME_RANGE, MIN_DURATION, MAX_DURATION, ALLOW_FULL_HOURS_ONLY, ALLOW_MINUTES, MINUTE_INTERVAL, TIME_CROSS_MIDNIGHT_ALLOWED, TARGET_ANSWER_SET, ANSWER_DISTRIBUTION, ANSWER_UNIT_MODE`

Default Thai elementary behavior:

- 24-hour notation
- daytime activities
- midnight crossing disabled
- balanced answers
- answer key off

## Deterministic calculation

`total_minutes = hour*60 + minute`

Same day:

`duration = end_minutes - start_minutes`

If midnight crossing is allowed:

`duration = (end_minutes + 1440 - start_minutes) % 1440`

Require positive duration unless explicitly requested otherwise.

Derive:

`hours = duration // 60`
`minutes = duration % 60`

## Invariants

- valid hour/minute syntax
- minute 00–59
- valid hour for selected format
- positive duration
- duration within min/max
- no forbidden midnight crossing
- whole-hour mode requires `duration % 60 == 0`
- active minute granularity must be respected
- rendered unit matches expected response

## Difficulty defaults

EASY: whole-hour duration; matching start/end minute components allowed.

MEDIUM: hours + minutes using grade-appropriate 5/10/15/30-minute increments.

HARD: mixed minutes/regrouping/cross-hour or cross-noon while remaining age appropriate.

## Answer-first generation

Choose valid duration first, then start time, derive end time, independently recompute, then attach an age-appropriate activity.

## Student rendering

When answer key is off, show only activity, start/end values, blank response field, and required units. Hidden verified duration remains internal.

## QA

`TIME_PARSE_QA, DURATION_QA, BOUNDS_QA, INTERVAL_QA, CROSSING_QA, UNIT_QA, ANSWER_LEAK_QA`

Any incorrect duration blocks release.