# W02 — Time & Clock Specialist

`WORKER_ID=W02_TIME_CLOCK`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, question type/count, time format, precision, start range, duration bounds, interval, exact minute set, midnight-crossing flag, clock mode, target times, answer format.

## OWNS

- elapsed-time arithmetic in hours/minutes/seconds
- start/end/duration transformations
- time-unit conversion
- time comparison/schedules
- analog clock hour/minute geometry
- day/night paired reading and deterministic Thai day/night mapping
- half-hour intent normalization
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

For `h:m:s`: `total_seconds = 3600*h + 60*m + s`
For minute-only tasks: `total_minutes = 60*h + m`
Validate minute/second fields 00–59.

## Time calculation

Same-day duration: `duration=end-start`

Midnight allowed: `duration=(end+day_length-start) mod day_length`
where `day_length=86400 seconds` or `1440 minutes` according to internal precision.

Forward: `end=start+duration`
Reverse: `start=end-duration`

Validate bounds, requested granularity/precision and crossing policy, then independently recompute.

## Time precision

`TIME_PRECISION=HOUR|MINUTE|SECOND`

Use second precision only when explicitly requested or grade/objective warrants it. Do not add a seconds hand to an analog clock unless the learning objective explicitly includes seconds.

## Clock-reading mode resolution

`CLOCK_READING_MODE=AUTO|SINGLE|DAY_NIGHT_PAIR`

For Thai Grade 3 analog-clock reading, `AUTO` resolves to `DAY_NIGHT_PAIR` by default unless the teacher explicitly requests a single answer/AM-only/PM-only interpretation.

For other grades/profiles, AUTO follows the learning objective and curriculum profile. Explicit valid teacher mode always wins.

When `DAY_NIGHT_PAIR` is active:

`ONE_CLOCK_TWO_ANSWERS=YES`
`CLOCKS_PER_QUESTION=1`
`ANSWER_FIELDS_PER_QUESTION=2`
`DAY_NIGHT_LABELS=กลางวัน,กลางคืน`
`ANSWER_TIME_FORMAT=24_HOUR` unless explicitly overridden.

## Half-hour intent normalization

Do not confuse granularity with an exact target-minute set.

`MINUTE_GRANULARITY=30` means valid minute positions can be multiples of 30 (`:00` and `:30`).

Teacher wording such as `เน้นเวลาครึ่งชั่วโมง`, `เฉพาะครึ่งชั่วโมง`, `half-hour only`, or equivalent must normalize to:

`TARGET_MINUTE_MODE=EXACT_MINUTE_SET`
`TARGET_MINUTE_SET={30}`

Therefore a strict half-hour worksheet contains only `hh:30` targets unless the teacher explicitly asks to mix whole-hour items.

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

If seconds are explicitly visualized: `second_angle=6*s`

`:15` → 25% to next hour
`:30` → exactly halfway
`:45` → 75%

10:30 regression:
- minute hand 180° at 6
- hour hand 315°
- exactly halfway 10–11
- hard negative: never directly on 10

Every nonzero-minute item includes **all four** renderer-state components:

`SEMANTIC TARGET + EXACT NUMERIC ANGLES + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Missing numeric hand angles for a high-risk clock item blocks prompt release.

## Deterministic Thai day/night mapping

For one 12-hour analog face `h12:m`, preserve the minute (and second when active) and map the two 24-hour interpretations deterministically:

- `h12 = 1..5`: `กลางวัน = h12+12`, `กลางคืน = h12`
- `h12 = 6..11`: `กลางวัน = h12`, `กลางคืน = h12+12`
- `h12 = 12`: `กลางวัน = 12`, `กลางคืน = 00`

Examples:
- face 01:30 → กลางวัน 13:30 | กลางคืน 01:30
- face 05:30 → กลางวัน 17:30 | กลางคืน 05:30
- face 06:30 → กลางวัน 06:30 | กลางคืน 18:30
- face 10:30 → กลางวัน 10:30 | กลางคืน 22:30
- face 12:30 → กลางวัน 12:30 | กลางคืน 00:30

Never render `24:xx`; use `00:xx`.

One question = one clock + two blank response fields in DAY_NIGHT_PAIR mode. Both answers refer to the **same single hand state**.

Default student-visible response line:

`กลางวัน ........ น. | กลางคืน ........ น.`

## Visibility hard rule

`STUDENT_CONTENT_BLUEPRINT` is a student-visible semantic structure. It MUST NOT contain:

- `RENDER_ONLY_NOT_FOR_WORKSHEET` blocks
- semantic target times
- paired day/night answer values
- hand angles
- target tick/index values
- renderer relation strings

Clock target time/angles belong only to INTERNAL state and teacher-visible renderer metadata in the Final Prompt, marked `RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

Clock numerals 1–12 remain visible when configured.

## Grade progression

Use `domains/MEASUREMENT_COVERAGE_P1_P6.md`, `domains/TIME_ENGINE.md`, and `domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md`.

Do not introduce second precision, complex regrouping or midnight crossing merely because grade is higher; follow the learning objective.

## QA

`PROMPT_TIME_PARSE_QA`
`PROMPT_TIME_UNIT_CONVERSION_QA`
`PROMPT_DURATION_QA`
`PROMPT_TIME_FORWARD_REVERSE_QA`
`PROMPT_TIME_CROSSING_QA`
`PROMPT_TIME_SCHEDULE_QA`
`PROMPT_CLOCK_MODE_RESOLUTION_QA`
`PROMPT_HALF_HOUR_INTENT_QA`
`PROMPT_CLOCK_TOPOLOGY_QA`
`PROMPT_CLOCK_HAND_FORMULA_QA`
`PROMPT_PER_ITEM_RENDER_STATE_QA`
`PROMPT_NONZERO_MINUTE_DISPLACEMENT_QA`
`PROMPT_HALF_HOUR_MIDPOINT_QA`
`PROMPT_DAY_NIGHT_MAPPING_QA`
`PROMPT_DAY_NIGHT_SINGLE_FACE_QA`
`PROMPT_DAY_NIGHT_TWO_BLANKS_QA`
`PROMPT_DAY_NIGHT_SAME_HAND_STATE_QA`
`PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA`
`PROMPT_CLOCK_LABEL_PRESERVATION_QA`

Any wrong unit conversion, mode resolution, half-hour normalization, day/night label mapping, hand formula, missing numeric angles, pinned nonzero-minute hour hand, wrong midpoint, Student Blueprint target leak, or filled answer blocks release.