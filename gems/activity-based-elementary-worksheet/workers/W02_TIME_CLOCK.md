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
`:45` → 75% to next hour

Quarter-hour interpolation is mandatory geometry, not optional visual styling.

Canonical quarter-hour relations for any starting hour `h`:

- `h:15` → hour hand displaced `7.5°` from h toward h+1;
- `h:30` → displaced `15°`;
- `h:45` → displaced `22.5°`, exactly 75% of the 30° hour sector.

14:45 / 2:45 permanent regression:
- minute hand = `270°` at numeral 9;
- hour hand = `82.5°` clockwise from 12;
- hour hand = exactly 75% of the way from 2 to 3;
- hard negative: never place the short hand directly on numeral 2.

10:30 regression:
- minute hand 180° at 6
- hour hand 315°
- exactly halfway 10–11
- hard negative: never directly on 10

## Deterministic vector endpoint state — MANDATORY

Actual artifact evidence showed that correct formulas and relational wording alone are insufficient: a renderer can still draw an hour hand on an approximate or snapped ray. W02 therefore owns a numeric vector endpoint state for every hand.

Angle convention: 0° at 12 o'clock, positive clockwise.

For angle `θ`:

`UNIT_DIRECTION_X = sin(radians(θ))`
`UNIT_DIRECTION_Y = -cos(radians(θ))`

Use normalized center `C=(0,0)` and normalized radius `R=1` in renderer metadata:

`MINUTE_HAND_LENGTH_RATIO=0.78`
`HOUR_HAND_LENGTH_RATIO=0.55`

`MINUTE_ENDPOINT_NORMALIZED=(0.78*sin(radians(minute_angle)), -0.78*cos(radians(minute_angle)))`

`HOUR_ENDPOINT_NORMALIZED=(0.55*sin(radians(hour_angle)), -0.55*cos(radians(hour_angle)))`

The downstream renderer may uniformly scale/translate the complete clock but MUST NOT independently move, rotate, snap, or aesthetically adjust either endpoint.

Every hand is the exact straight segment:

`HAND_SEGMENT = CLOCK_CENTER → COMPUTED_ENDPOINT`

### Anti-snap invariant
For every `m != 0`:

`HOUR_DISPLACEMENT_FROM_START_HOUR_DEG = 0.5*m`

The renderer is forbidden to reduce this displacement. For example:
- 3:30 → hour angle 105°, not 90°;
- 9:30 → hour angle 285°, not 270°;
- 11:45 → hour angle 352.5°, not 330°;
- 2:45 → hour angle 82.5°, not 60°.

### Mandatory atomic renderer-only state
Every analog clock item MUST return all of these fields:

`SEMANTIC_TARGET`
`CLOCK_CENTER_NORMALIZED=(0,0)`
`CLOCK_RADIUS_NORMALIZED=1`
`MINUTE_HAND_ANGLE_DEG`
`HOUR_HAND_ANGLE_DEG`
`MINUTE_HAND_LENGTH_RATIO=0.78`
`HOUR_HAND_LENGTH_RATIO=0.55`
`MINUTE_ENDPOINT_NORMALIZED`
`HOUR_ENDPOINT_NORMALIZED`
`RELATIONAL_VERIFICATION`
`ITEM_SPECIFIC_HARD_NEGATIVE`

If any endpoint field is missing, `PROMPT_CLOCK_VECTOR_ENDPOINT_QA=FAIL`.

### Required examples
3:30:
- minute angle 180°
- hour angle 105°
- minute endpoint ≈ `(0.000000,0.780000)`
- hour endpoint ≈ `(0.531259,0.142350)`
- relation: exactly halfway between 3 and 4
- hard negative: do not draw the short hand directly at 3 or 4

2:45:
- minute angle 270°
- hour angle 82.5°
- relation: exactly 75% from 2 toward 3
- hard negative: do not draw the short hand directly at 2 or 3

Every nonzero-minute item includes **all five** geometry/verification components:

`SEMANTIC TARGET + EXACT NUMERIC ANGLES + EXACT NORMALIZED ENDPOINTS + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Missing numeric hand angles or endpoint vectors for a high-risk clock item blocks prompt release.

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
- hand endpoint coordinates
- target tick/index values
- renderer relation strings

Clock target time/angles/endpoints belong only to INTERNAL state and teacher-visible renderer metadata in the Final Prompt, marked `RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

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
`PROMPT_CLOCK_QUARTER_HOUR_INTERPOLATION_QA`
`PROMPT_CLOCK_VECTOR_ENDPOINT_QA`
`PROMPT_CLOCK_RADIAL_COLLINEARITY_QA`
`PROMPT_CLOCK_ANTI_SNAP_QA`
`PROMPT_DAY_NIGHT_MAPPING_QA`
`PROMPT_DAY_NIGHT_SINGLE_FACE_QA`
`PROMPT_DAY_NIGHT_TWO_BLANKS_QA`
`PROMPT_DAY_NIGHT_SAME_HAND_STATE_QA`
`PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA`
`PROMPT_CLOCK_LABEL_PRESERVATION_QA`

Any wrong unit conversion, mode resolution, half-hour normalization, day/night label mapping, hand formula, missing numeric angles/endpoints, pinned nonzero-minute hour hand, wrong quarter/half-hour interpolation, Student Blueprint target leak, or filled answer blocks release.