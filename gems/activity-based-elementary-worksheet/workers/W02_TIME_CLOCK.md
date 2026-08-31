# W02 — Time & Clock Specialist

`WORKER_ID=W02_TIME_CLOCK`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, question type/count, time format, precision, start range, duration bounds, interval, midnight-crossing flag, clock mode, target times, answer format, day/night labels, dual-answer mode.

## OWNS

- elapsed-time arithmetic in hours/minutes/seconds
- start/end/duration transformations
- time-unit conversion
- time comparison/schedules
- analog clock hour/minute geometry
- day/night paired reading
- **single-clock / two-answer day-night interpretation**
- time/clock-specific QA

## RETURNS

Verified canonical time relations, student-visible givens/blanks, clock template requirements, renderer-only clock states, day/night answer-pair state, hard negatives, domain QA requirements.

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

Hour hand moves continuously.

`:15` → 25% to next hour
`:30` → exactly halfway
`:45` → 75%

10:30 regression:

- minute hand 180° at 6
- hour hand 315°
- exactly halfway 10–11
- hard negative: never directly on 10

Every nonzero-minute item includes displacement relation and item-specific negative.

## DAY_NIGHT_PAIR — canonical single-face behavior

When the user requests one clock image to answer both daytime and nighttime, normalize to:

`CLOCK_READING_MODE=DAY_NIGHT_PAIR`
`ONE_CLOCK_TWO_ANSWERS=YES`
`CLOCKS_PER_QUESTION=1`
`ANSWER_FIELDS_PER_QUESTION=2`
`DAY_NIGHT_LABELS=กลางวัน,กลางคืน`
`ANSWER_TIME_FORMAT=24_HOUR` unless explicitly overridden

**Non-negotiable composition:**

`1 QUESTION = EXACTLY 1 ANALOG CLOCK FACE + EXACTLY 2 BLANK ANSWER FIELDS`

Student-visible default:

`กลางวัน ........ น. | กลางคืน ........ น.`

Do **not** create a separate daytime clock and nighttime clock for the same question.

The clock geometry is drawn once. Both answers are interpretations of the **same hand positions**.

### Pair mapping

Let the analog face represent canonical 12-hour value `h12:m`.

For ordinary paired elementary practice, the two 24-hour interpretations must:

- preserve the same minute value;
- preserve the same second value if seconds are active;
- differ by exactly 12 hours modulo 24.

Canonical pair examples:

- 1:30 ↔ 13:30
- 7:00 ↔ 19:00
- 10:30 ↔ 22:30
- 12:15 ↔ 00:15

For a 12-o'clock face, the pair is `12:xx` and `00:xx`; do not output `24:xx`.

If the requested labels are specifically `กลางวัน` and `กลางคืน`, use the pedagogical mapping defined by the task/profile and verify it internally before release. Do not invent contextual AM/PM cues that contradict the intended pair.

### Student-safe blueprint

Student Blueprint contains only:

- neutral item ID
- one neutral clock template reference
- two blank fields with the requested labels

It must not contain either paired target time.

### Renderer metadata

Final Prompt contains one renderer-only clock state per question:

`SEMANTIC_TARGET_12H + MINUTE_ANGLE + HOUR_ANGLE + RELATIONAL_WORDING + ITEM_SPECIFIC_HARD_NEGATIVE`

Mark:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

The two internal day/night answer values may be used for verification, but they must not be printed when `SHOW_ANSWER_KEY=NO`.

### Hard negatives

For DAY_NIGHT_PAIR:

- **DO NOT draw two clocks for one question.**
- **DO NOT change hand positions between daytime and nighttime answers.**
- **DO NOT print either target time beside/inside the clock.**
- **DO NOT fill either answer blank.**
- **DO NOT remove canonical clock numerals merely to hide target values.**

## Day/night pair source specification

Detailed feature contract:

`domains/CLOCK_DAY_NIGHT_SINGLE_FACE_SPEC.md`

## Visibility

Clock target time/angles and paired answers belong to teacher-visible/internal state. Student Blueprint must not contain target time or angle.

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
`PROMPT_DAY_NIGHT_SINGLE_FACE_QA`
`PROMPT_DAY_NIGHT_TWO_BLANKS_QA`
`PROMPT_DAY_NIGHT_SAME_HAND_STATE_QA`
`PROMPT_CLOCK_LABEL_PRESERVATION_QA`

Wrong unit conversion, time relation, hand formula, pinned nonzero-minute hour hand, wrong midpoint, wrong day/night pair, two clocks for one paired question, changed hand state between pair interpretations, or leaked clock answer blocks release.