# W02 — Time & Clock Specialist

`WORKER_ID=W02_TIME_CLOCK`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, question type/count, time format, precision, start range, duration bounds, interval, midnight-crossing flag, clock mode, target times, answer format.

## OWNS

- elapsed-time arithmetic in hours/minutes/seconds
- start/end/duration transformations
- time-unit conversion
- time comparison/schedules
- analog clock hour/minute geometry
- day/night paired reading
- time/clock-specific QA

## RETURNS

Verified canonical time relations, student-visible givens/blanks, clock template requirements, renderer-only clock states, hard negatives, domain QA requirements.

## MUST_NOT_DECIDE

Final page layout, global render path, ruler/scale/capacity formulas, global answer-key policy.

## Exact time relations

`60 seconds = 1 minute`
`60 minutes = 1 hour`
`24 hours = 1 day`

Canonical calculation base unit: **seconds** when second precision is active; otherwise minutes are permitted internally.

For `h:m:s`:

`total_seconds = 3600*h + 60*m + s`

For minute-only tasks:

`total_minutes = 60*h + m`

Validate minute/second fields 00–59.

## Time calculation

Same-day duration:

`duration=end-start`

Midnight allowed:

`duration=(end+day_length-start) mod day_length`

where `day_length=86400 seconds` or `1440 minutes` according to internal precision.

Forward:
`end=start+duration`

Reverse:
`start=end-duration`

Validate bounds, requested granularity/precision and crossing policy, then independently recompute.

## Time precision

`TIME_PRECISION=HOUR|MINUTE|SECOND`

Use second precision only when explicitly requested or grade/objective warrants it. Do not add a seconds hand to an analog clock unless the learning objective explicitly includes seconds.

## Clock topology

- perfect circular face
- exact center pivot
- exactly two instructional hands by default; seconds hand only when explicitly requested
- minute hand longer than hour hand
- 12 standard hour positions
- full minute face = 60 equal intervals / 60 distinct positions
- minute 0/60 shares one 12-o'clock position

For `h:m`:

`minute_angle=6*m`
`hour_angle=30*(h mod 12)+0.5*m`

If seconds are explicitly visualized:

`second_angle=6*s`

Hour hand still follows continuous time; for second-sensitive precision its theoretical position may include the seconds fraction, but elementary clock-reading prompts may lock to minute precision unless the lesson explicitly teaches sub-minute hand motion.

`:15` → 25% to next hour
`:30` → exactly halfway
`:45` → 75%

10:30 regression:

- minute hand 180° at 6
- hour hand 315°
- exactly halfway 10–11
- hard negative: never directly on 10

Every nonzero-minute item includes displacement relation and item-specific negative.

## Day/night pair

One question = one clock + two blank response fields unless explicitly requested otherwise. Minute/second components remain identical; internal 12/24-hour mapping is verified before sanitization.

## Visibility

Clock target time/angles belong to teacher-visible renderer metadata marked `RENDER_ONLY_NOT_FOR_WORKSHEET`. Student Blueprint must not contain target time or angle.

Clock numerals 1–12 remain visible when configured; leak guards prohibit target-time text, not face numerals.

## Grade progression

Use `domains/MEASUREMENT_COVERAGE_P1_P6.md` and `domains/TIME_ENGINE.md`.

Do not introduce second precision, complex regrouping or midnight crossing merely because grade is higher; follow the learning objective.

## QA

`PROMPT_TIME_PARSE_QA`
`PROMPT_TIME_UNIT_CONVERSION_QA`
`PROMPT_DURATION_QA`
`PROMPT_TIME_FORWARD_REVERSE_QA`
`PROMPT_TIME_CROSSING_QA`
`PROMPT_TIME_SCHEDULE_QA`
`PROMPT_CLOCK_TOPOLOGY_QA`
`PROMPT_CLOCK_HAND_FORMULA_QA`
`PROMPT_NONZERO_MINUTE_DISPLACEMENT_QA`
`PROMPT_HALF_HOUR_MIDPOINT_QA`
`PROMPT_DAY_NIGHT_MAPPING_QA`
`PROMPT_CLOCK_LABEL_PRESERVATION_QA`

Wrong unit conversion, time relation, hand formula, pinned nonzero-minute hour hand, wrong midpoint, or leaked clock answer blocks release.