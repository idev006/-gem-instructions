# CLOCK_READING_ENGINE — Analog Clock Reading

Version: 1.1.0
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`

## Learning goal

Student reads hour and minute from an analog clock accurately and, when requested, connects one analog-clock geometry to its two valid 24-hour readings in a day/night pair.

## Core parameters

`CLOCK_FORMAT=12_HOUR`, `MINUTE_GRANULARITY`, `SHOW_MINUTE_MARKS`, `SHOW_NUMBERS`, `HOUR_HAND_MODE`, `ANSWER_FORMAT`, `TARGET_TIMES`, `CLOCK_READING_MODE=SINGLE|DAY_NIGHT_PAIR`, `ANSWER_TIME_FORMAT=12_HOUR|24_HOUR`, `DAY_NIGHT_LABEL_MODE=TEXT|ICON_TEXT`

Suggested defaults by progression:

- EASY: whole hours / half hours
- MEDIUM: 5-minute intervals
- HARD: 1-minute intervals when grade-appropriate

For Thai elementary dual-reading worksheets, prefer:

- `CLOCK_READING_MODE=DAY_NIGHT_PAIR`
- `ANSWER_TIME_FORMAT=24_HOUR`
- one clock face per question
- two blank answer fields per question: `กลางวัน` and `กลางคืน`

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

For analog time `h:m` where `h` is interpreted on a 12-hour face:

- minute-hand angle = `6*m` degrees clockwise from 12
- hour-hand angle = `30*(h mod 12) + 0.5*m` degrees clockwise from 12

The hour hand MUST move continuously between hour marks. At 7:30 it must be halfway between 7 and 8, not fixed at 7.

Compile both semantic and geometric instructions.

## DAY_NIGHT_PAIR mode — one clock, two answers

### Pedagogical rule

One analog clock face can represent two times in a 24-hour day, separated by 12 hours. In this worksheet mode, **one question contains one clock face and two student answers**:

`☀ กลางวัน ........ นาฬิกา ........ นาที`

`☾ กลางคืน ........ นาฬิกา ........ นาที`

or an equivalent compact 24-hour answer format such as:

`กลางวัน ........ น.    กลางคืน ........ น.`

The clock hands are drawn only once. Do NOT create separate day and night clocks unless the user explicitly asks for two clocks.

### Deterministic Thai day/night mapping

Let analog face hour be `h12` in `1..12` and minute be `m` in `0..59`.

For elementary Thai day/night pairing, use the following canonical mapping:

- if `1 <= h12 <= 5`:
  - `DAY_HOUR_24 = h12 + 12`
  - `NIGHT_HOUR_24 = h12`
- if `6 <= h12 <= 11`:
  - `DAY_HOUR_24 = h12`
  - `NIGHT_HOUR_24 = h12 + 12`
- if `h12 = 12`:
  - `DAY_HOUR_24 = 12`
  - `NIGHT_HOUR_24 = 0`

Minutes are identical in both answers.

Examples:

- analog `2:30` → กลางวัน `14:30 น.` / กลางคืน `02:30 น.`
- analog `7:45` → กลางวัน `07:45 น.` / กลางคืน `19:45 น.`
- analog `12:15` → กลางวัน `12:15 น.` / กลางคืน `00:15 น.`

This is a paired 24-hour reading task. Do not infer the two answers from decorative icons alone; compute both answers deterministically from the analog time.

### Important semantic guard

Do NOT apply a universal rule `night = day + 12` without normalization. For face hours 1–5, the smaller 24-hour value is the night reading and the larger value is the daytime reading. For 6–11 the reverse applies. For 12, the pair is 12:xx and 00:xx.

The pair must always satisfy:

`(DAY_HOUR_24 - NIGHT_HOUR_24) mod 12 = 0`

and represent the two distinct occurrences of the same 12-hour clock geometry within 24 hours.

## Blueprint for DAY_NIGHT_PAIR

### Internal verified object

```text
{
  id: 1,
  analog_hour: 2,
  minute: 30,
  minute_hand_angle_deg: 180,
  hour_hand_angle_deg: 75,
  verified_day_time_24: "14:30",
  verified_night_time_24: "02:30",
  validation: PASS
}
```

### Student render object

```text
{
  id: 1,
  clock_template_id: "TH_ANALOG_12H_V1",
  hand_target_relation: "RENDER_ONLY_NOT_VISIBLE",
  day_answer_render: "กลางวัน ........ น.",
  night_answer_render: "กลางคืน ........ น."
}
```

Verified day/night answers must remain internal when the answer key is off.

## Layout/readability

Preferred printed clock diameter >= 30 mm for 5-minute reading; increase for 1-minute reading.

For DAY_NIGHT_PAIR, reserve enough vertical answer space for two clearly associated response lines per clock. The sun/moon icons are optional visual cues; the labels `กลางวัน` and `กลางคืน` are authoritative and must remain readable in monochrome printing.

For 10 questions on A4 portrait, prefer a 2-column × 5-row card grid only if each clock remains at or above the minimum readable diameter and both response lines fit without crowding. Otherwise paginate.

## Answer integrity

When `SHOW_ANSWER_KEY=NO`:

- do not print the verified 24-hour day/night pair anywhere in visible sections;
- do not expose internal answer vectors in notes, QA prose, parentheticals, or examples tied to the active worksheet;
- render-only hand geometry may be present only as non-visible compiler metadata.

## QA

Base clock QA:

`CLOCK_CIRCLE_QA, CLOCK_PIVOT_QA, HAND_COUNT_QA, HAND_LENGTH_QA, MINUTE_MARK_QA, HOUR_HAND_INTERPOLATION_QA, TARGET_TIME_QA, MINIMUM_SIZE_QA`

Additional DAY_NIGHT_PAIR QA:

`DAY_NIGHT_PAIR_MODE_QA`
`ONE_CLOCK_TWO_ANSWERS_QA`
`DAY_TIME_MAPPING_QA`
`NIGHT_TIME_MAPPING_QA`
`MINUTE_PRESERVATION_QA`
`TWELVE_ZERO_MAPPING_QA`
`PAIR_12_HOUR_EQUIVALENCE_QA`
`DAY_NIGHT_LABEL_QA`
`DAY_NIGHT_ANSWER_LEAK_QA`

Any wrong hand position, wrong day/night mapping, missing second answer field, duplicate clock when one was requested, or visible answer leakage blocks release.
