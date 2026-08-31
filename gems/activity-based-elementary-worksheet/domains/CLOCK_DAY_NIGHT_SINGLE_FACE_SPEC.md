# Clock Day/Night Single-Face Specification

Version: 1.1.0
Compatible Gem baseline: 2.6.x
Owner: `W02_TIME_CLOCK`
Visual auditor: `W07_INSTRUMENT_AUDITOR`

## Purpose

Define canonical behavior when one analog clock image is used to ask for both daytime and nighttime interpretations.

## Mode resolution

`CLOCK_READING_MODE=AUTO|SINGLE|DAY_NIGHT_PAIR`

For Thai Grade 3 analog-clock reading, AUTO resolves to `DAY_NIGHT_PAIR` unless the teacher explicitly requests one answer only.

Canonical paired mode:

`CLOCK_READING_MODE=DAY_NIGHT_PAIR`
`ONE_CLOCK_TWO_ANSWERS=YES`
`CLOCKS_PER_QUESTION=1`
`ANSWER_FIELDS_PER_QUESTION=2`
`DAY_NIGHT_LABELS=กลางวัน,กลางคืน`
`ANSWER_TIME_FORMAT=24_HOUR` unless explicitly overridden

## Student-visible composition

Each question contains exactly:

1. one analog clock face;
2. one blank daytime field;
3. one blank nighttime field.

Default answer line:

`กลางวัน ........ น. | กลางคืน ........ น.`

A separate day clock and night clock are prohibited unless explicitly requested.

## Deterministic Thai academic mapping

The two interpretations preserve the same minute and differ by 12 hours modulo 24, but the **labels are not arbitrary**.

For face `h12:m`:

- `h12=1..5`: `กลางวัน=h12+12`, `กลางคืน=h12`
- `h12=6..11`: `กลางวัน=h12`, `กลางคืน=h12+12`
- `h12=12`: `กลางวัน=12`, `กลางคืน=00`

Examples:

- face 01:30 → กลางวัน 13:30 | กลางคืน 01:30
- face 05:30 → กลางวัน 17:30 | กลางคืน 05:30
- face 06:30 → กลางวัน 06:30 | กลางคืน 18:30
- face 07:00 → กลางวัน 07:00 | กลางคืน 19:00
- face 10:30 → กลางวัน 10:30 | กลางคืน 22:30
- face 12:15 → กลางวัน 12:15 | กลางคืน 00:15

Never render `24:xx`; use `00:xx`.

If seconds are active, preserve the second component too.

## Half-hour semantics

`MINUTE_GRANULARITY=30` alone is not equivalent to “half-hour only”. It permits `:00` and `:30`.

When teacher intent is `เน้นเวลาครึ่งชั่วโมง`, `เฉพาะครึ่งชั่วโมง`, `half-hour only`, or equivalent, normalize:

`TARGET_MINUTE_MODE=EXACT_MINUTE_SET`
`TARGET_MINUTE_SET={30}`

All generated targets must therefore use minute `30` unless the teacher explicitly asks for a mixed set.

## Clock geometry

The analog hand state is generated once per question.

For `h:m`:

`minute_angle=6*m`
`hour_angle=30*(h mod 12)+0.5*m`

Both day and night answers refer to this exact same geometry.

Every renderer item state must include:

`SEMANTIC TARGET + EXACT NUMERIC ANGLES + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

For 10:30 specifically:
- minute angle 180° / exactly at 6
- hour angle 315° / exactly halfway 10–11
- hard negative: hour hand must not point directly at 10

## Visibility contract

Student Blueprint contains only neutral clock item semantics plus the two blank labeled fields. It must not contain:

- target face time
- daytime/nighttime answer values
- hand angles
- `RENDER_ONLY_NOT_FOR_WORKSHEET` item blocks
- renderer relation strings

Internal/teacher-visible state may contain canonical target, verified interpretations and geometry. Mark renderer metadata:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

## Renderer hard negatives

- DO NOT draw two clocks for one question.
- DO NOT create different hand positions for daytime and nighttime.
- DO NOT print target times near the clock.
- DO NOT fill either response blank.
- DO NOT remove required face numerals 1–12.
- DO NOT add AM/PM labels unless explicitly requested.
- DO NOT omit numeric renderer angles from high-risk per-item metadata.

## Page policy

The paired mode does not imply `ONE_PAGE_LOCK=ON`.

Default remains:

`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

Only an explicit user request such as `1 หน้าเท่านั้น` or `A4 หน้าเดียว` may turn the lock ON.

## QA

`PROMPT_DAY_NIGHT_SINGLE_FACE_QA=PASS` requires one clock, two blank fields, same hand state, deterministic Thai label mapping, identical minute/second components, no target leakage and canonical face labels.

`PROMPT_HALF_HOUR_INTENT_QA=PASS` requires exact minute 30 for every item when strict half-hour intent is active.

`PROMPT_PER_ITEM_RENDER_STATE_QA=PASS` requires numeric angles + relational wording + item-specific hard negative for every clock item.

`PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA=PASS` requires zero target/renderer metadata in Student Blueprint.

Any failure above blocks `PROMPT_RELEASE`.

Before downstream image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`.