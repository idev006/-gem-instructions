# CALENDAR_ENGINE — Calendar / Date Reading

Version: 1.0.0
Status: PRODUCTION_CANDIDATE

## Learning goals

Supports:

- identify day/date
- count days forward/backward
- identify weekday for a date
- compare dates
- read simple monthly calendars

## Core parameters

`YEAR`, `MONTH`, `WEEK_START`, `QUESTION_TYPE`, `TARGET_DATES`, `DATE_FORMAT`, `SHOW_ADJACENT_MONTH_DAYS`

Default Thai worksheet behavior: use Thai labels and clearly state month/year when calendar structure matters.

## Deterministic calendar rules

Use real Gregorian calendar relationships unless the user explicitly requests a fictional practice calendar.

Validate:

- days in month
- leap year handling
- weekday mapping
- forward/backward day arithmetic
- no invalid dates such as 31 April

## Visual integrity

- exactly 7 weekday columns
- consistent week-start convention
- dates aligned to correct weekday
- target highlight/marker must not obscure the date number
- no duplicate/missing dates in the active month

## QA

`DATE_VALIDITY_QA, LEAP_YEAR_QA, WEEKDAY_QA, CALENDAR_GRID_QA, DATE_SEQUENCE_QA, TARGET_MARKER_QA`

Any invalid calendar mapping blocks release.