# W02 — Time & Clock Specialist

`WORKER_ID=W02_TIME_CLOCK`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, question type/count, time format, start range, duration bounds, minute interval, midnight-crossing flag, clock mode, minute granularity, target times, answer format.

## OWNS

- elapsed-time arithmetic
- start/end/duration transformations
- time comparison/schedules
- analog clock hand geometry
- day/night paired reading
- time/clock-specific QA

## RETURNS

Verified canonical time relations, student-visible givens/blanks, clock template requirements, renderer-only clock states, hard negatives, domain QA requirements.

## MUST_NOT_DECIDE

Final page layout, global render path, ruler/scale/capacity formulas, global answer-key policy.

## Time calculation

`total_minutes=hour*60+minute`

Same-day duration:
`duration=end-start`

Midnight allowed:
`duration=(end+1440-start)%1440`

Forward:
`end=start+duration`

Reverse:
`start=end-duration`

Validate syntax, bounds, minute granularity and crossing policy, then independently recompute.

## Clock topology

- perfect circular face
- exact center pivot
- exactly two instructional hands unless seconds requested
- minute hand longer
- 12 standard hour positions
- full minute face = 60 equal intervals / 60 distinct positions
- minute 0/60 shares one 12-o'clock position

For `h:m`:

`minute_angle=6*m`
`hour_angle=30*(h mod 12)+0.5*m`

Hour hand moves continuously.

`:15` → 25% to next hour
`:30` → exactly halfway
`:45` → 75%

10:30 regression:

- minute hand 180° at 6
- hour hand 315°
- exactly halfway 10–11
- hard negative: never directly on 10

Every nonzero-minute item must include hour-hand displacement relation and item-specific negative.

## Day/night pair

One question = one clock + two blank response fields unless user explicitly requests otherwise. Minutes remain identical. Internal mapping follows the selected 12/24-hour convention; verified paired answers do not leak when key is off.

## Visibility

Clock target time/angles belong to teacher-visible renderer metadata marked `RENDER_ONLY_NOT_FOR_WORKSHEET`. Student Blueprint must not contain target times or angles.

Clock numerals 1–12 remain visible when configured; leak guards prohibit target time text, not face numerals.

## Grade progression

Use `domains/MEASUREMENT_COVERAGE_P1_P6.md` and `domains/TIME_ENGINE.md`. Do not introduce minute precision, regrouping or midnight crossing beyond the stated objective merely because grade is higher.

## QA

`PROMPT_TIME_PARSE_QA`
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

Wrong time relation, wrong hand formula, pinned nonzero-minute hour hand, wrong :30 midpoint, or leaked clock answer blocks release.