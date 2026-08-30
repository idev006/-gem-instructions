# CLOCK_READING_ENGINE — Analog Clock Reading

Version: 1.1.1
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`
Registry authority: `domains/DOMAIN_REGISTRY.md`

## Learning goal

Student reads hour and minute from an analog clock accurately and, when requested, connects one analog-clock geometry to its two valid 24-hour readings in a day/night pair.

## Core parameters

`CLOCK_FORMAT=12_HOUR`, `MINUTE_GRANULARITY`, `SHOW_MINUTE_MARKS`, `SHOW_NUMBERS`, `HOUR_HAND_MODE`, `ANSWER_FORMAT`, `TARGET_TIMES`, `CLOCK_READING_MODE=SINGLE|DAY_NIGHT_PAIR`, `ANSWER_TIME_FORMAT=12_HOUR|24_HOUR`, `DAY_NIGHT_LABEL_MODE=TEXT|ICON_TEXT`

Suggested progression:

- EASY: whole hours / half hours
- MEDIUM: 5-minute intervals
- HARD: 1-minute intervals when grade-appropriate

For Thai elementary dual-reading worksheets, prefer:

- `CLOCK_READING_MODE=DAY_NIGHT_PAIR`
- `ANSWER_TIME_FORMAT=24_HOUR`
- one clock face per question
- two blank response fields: `กลางวัน` and `กลางคืน`

## Geometry invariants

- true circular clock face in square reserved box
- exact center pivot
- exactly two instructional hands unless seconds explicitly requested
- minute hand visibly longer than hour hand
- 12 hour positions evenly spaced
- 60 minute intervals when minute-level reading is required
- standard clockwise grammar: 12 top, 3 right, 6 bottom, 9 left
- no decorative pointer/hand

## Hand placement

For analog time `h:m`:

- minute-hand angle = `6*m` degrees clockwise from 12
- hour-hand angle = `30*(h mod 12) + 0.5*m` degrees clockwise from 12

The hour hand MUST move continuously. At 7:30 it is halfway between 7 and 8.

Compile semantic + geometric instructions redundantly.

## DAY_NIGHT_PAIR — one clock, two answers

One question contains one clock and two answer fields:

`☀ กลางวัน ........ นาฬิกา ........ นาที`

`☾ กลางคืน ........ นาฬิกา ........ นาที`

or compact equivalent:

`กลางวัน ........ น.    กลางคืน ........ น.`

Do not create separate day/night clocks unless explicitly requested.

### Deterministic Thai mapping

Let `h12` be 1..12 and minute `m` be 0..59.

- if `1 <= h12 <= 5`: DAY=`h12+12`, NIGHT=`h12`
- if `6 <= h12 <= 11`: DAY=`h12`, NIGHT=`h12+12`
- if `h12 = 12`: DAY=`12`, NIGHT=`0`

Minutes stay identical.

Examples:

- 2:30 → day 14:30 / night 02:30
- 7:45 → day 07:45 / night 19:45
- 12:15 → day 12:15 / night 00:15

Do not use a universal `night = day + 12` rule without normalization. Do not derive answers from icons.

The pair must represent the two occurrences of the same 12-hour geometry in 24 hours.

## Blueprint

### Internal

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

### Student

```text
{
 id: 1,
 clock_template_id: "TH_ANALOG_12H_V1",
 hand_target_relation: "RENDER_ONLY_NOT_VISIBLE",
 day_answer_render: "กลางวัน ........ น.",
 night_answer_render: "กลางคืน ........ น."
}
```

Verified answers remain internal when key is off.

## Layout / one-page policy

Preferred printed clock diameter >=30 mm for 5-minute reading; increase for 1-minute reading.

For DAY_NIGHT_PAIR, reserve two response lines before decoration.

For 10 questions on A4 portrait, first attempt a 2-column × 5-row grid if minimum clock diameter and answer space remain valid.

Apply global one-page optimization before pagination. If one page remains impossible:

- `ONE_PAGE_LOCK=OFF` → paginate;
- `ONE_PAGE_LOCK=ON` → `ONE_PAGE_FEASIBILITY_QA=FAIL` and `LAYOUT_QA=FAIL`; do not create page 2 and do not shrink the clock below minimum readability.

Sun/moon icons are optional; text labels are authoritative and must remain readable in monochrome.

## Render-path guidance

Preferred:

`HYBRID` or `DETERMINISTIC_VECTOR`

Clock face, minute marks, center pivot, and hands are educational geometry and should be deterministic when possible. Theme art may be generative outside the clock zone.

## Answer integrity

When `SHOW_ANSWER_KEY=NO`:

- do not print verified day/night values anywhere visible;
- do not expose internal answer vectors in notes, QA prose, parentheticals, or active examples;
- render-only hand geometry is non-visible compiler metadata only.

## QA

Base:

`CLOCK_CIRCLE_QA, CLOCK_PIVOT_QA, HAND_COUNT_QA, HAND_LENGTH_QA, MINUTE_MARK_QA, HOUR_HAND_INTERPOLATION_QA, TARGET_TIME_QA, MINIMUM_SIZE_QA`

DAY_NIGHT_PAIR:

`DAY_NIGHT_PAIR_MODE_QA`
`ONE_CLOCK_TWO_ANSWERS_QA`
`DAY_TIME_MAPPING_QA`
`NIGHT_TIME_MAPPING_QA`
`MINUTE_PRESERVATION_QA`
`TWELVE_ZERO_MAPPING_QA`
`PAIR_12_HOUR_EQUIVALENCE_QA`
`DAY_NIGHT_LABEL_QA`
`DAY_NIGHT_ANSWER_LEAK_QA`

Global integration:

`ONE_PAGE_FEASIBILITY_QA`
`RENDER_PATH_QA`

Any wrong hand position, wrong mapping, missing second answer field, unintended duplicate clock, unsafe shrinking, or visible answer leakage blocks release.
