# TIME_ENGINE — Elapsed-Time Worksheet Rules

Version: 1.0.1
Status: PRODUCTION_CANDIDATE
Registry authority: `domains/DOMAIN_REGISTRY.md`
Academic rules status: DETERMINISTIC_MATURE

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

For forward transformation:

`end_minutes = start_minutes + duration_minutes`

For reverse transformation:

`start_minutes = end_minutes - duration_minutes`

Normalize into the active day/clock rules and reject forbidden crossings.

## Invariants

- valid hour/minute syntax
- minute 00–59
- valid hour for selected format
- positive duration
- duration within min/max
- no forbidden midnight crossing
- whole-hour mode requires `duration % 60 == 0`
- active minute granularity respected
- rendered unit matches expected response
- forward/reverse transformation recomputes to the original relation

## Difficulty defaults

EASY: whole-hour duration; matching start/end minute components allowed.

MEDIUM: hours + minutes using grade-appropriate 5/10/15/30-minute increments.

HARD: mixed minutes/regrouping/cross-hour or cross-noon while remaining age appropriate.

## Answer-first generation

Choose valid duration first, then start time, derive end time, independently recompute, then attach an age-appropriate activity.

For reverse question types, still generate from a canonical verified time relation first, then expose only the requested givens.

## Student rendering

When answer key is off, show only required activity/givens and blank response fields. Hidden verified values remain internal and must not appear in notes, QA prose, or parentheticals in the visible package.

## Render-path guidance

Elapsed-time worksheets are normally text/table/numeric-heavy. Preferred path:

`DOCUMENT_FIRST` or `HYBRID`

Do not default to generative image-only rendering for Thai text-heavy tables. Illustrations are optional secondary decoration.

## One-page guidance

Apply the global `ONE_PAGE_PREFERRED=YES` policy. For typical 10-question A4 tasks, first try a compact deterministic table or efficient row layout. Preserve readable text and writable answer cells. If `ONE_PAGE_LOCK=ON` and a valid one-page layout is impossible, fail feasibility rather than shrinking below readability.

## QA

`TIME_PARSE_QA, DURATION_QA, BOUNDS_QA, INTERVAL_QA, CROSSING_QA, UNIT_QA, FORWARD_REVERSE_QA, ANSWER_LEAK_QA, ONE_PAGE_FEASIBILITY_QA, RENDER_PATH_QA`

Any incorrect time relation blocks release.

## Maturity note

The academic calculation layer is deterministic and mature. Overall domain maturity remains `PRODUCTION_CANDIDATE` until the actual-render evidence threshold in `qa/DOMAIN_RELEASE_MATRIX.md` is documented.
