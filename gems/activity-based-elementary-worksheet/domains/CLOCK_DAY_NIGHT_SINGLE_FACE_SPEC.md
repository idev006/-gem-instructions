# Clock Day/Night Single-Face Specification

Version: 1.0.0
Compatible Gem baseline: 2.6.x
Owner: `W02_TIME_CLOCK`
Visual auditor: `W07_INSTRUMENT_AUDITOR`

## Purpose

Define the canonical worksheet behavior when one analog clock image is used to ask for both daytime and nighttime interpretations.

## Canonical normalized mode

`CLOCK_READING_MODE=DAY_NIGHT_PAIR`
`ONE_CLOCK_TWO_ANSWERS=YES`
`CLOCKS_PER_QUESTION=1`
`ANSWER_FIELDS_PER_QUESTION=2`
`DAY_NIGHT_LABELS=กลางวัน,กลางคืน`
`ANSWER_TIME_FORMAT=24_HOUR` unless explicitly overridden

## Student-visible composition

Each question must contain exactly:

1. one analog clock face;
2. one blank daytime answer field;
3. one blank nighttime answer field.

Default answer line:

`กลางวัน ........ น. | กลางคืน ........ น.`

The same clock image is used for both answers. A separate day clock and night clock are prohibited unless the teacher explicitly requests two clocks.

## Academic mapping

The two interpretations of one analog face preserve the same minute component and differ by 12 hours modulo 24.

Examples:

- 1:30 ↔ 13:30
- 7:00 ↔ 19:00
- 10:30 ↔ 22:30
- 12:15 ↔ 00:15

Never render `24:xx` as a student answer; use `00:xx`.

If seconds are active, the second component is preserved too.

## Clock geometry

The analog hand state is generated once per question.

For `h:m`:

`minute_angle=6*m`
`hour_angle=30*(h mod 12)+0.5*m`

Both daytime and nighttime answers refer to exactly this same geometry.

No second copy of the clock is required.

## Visibility contract

Internal/teacher-visible state may contain:

- canonical 12-hour semantic target;
- both verified 24-hour interpretations;
- hand angles;
- relational wording;
- hard negatives.

Mark renderer geometry:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

Student Blueprint must contain only one neutral clock item plus two blank labeled fields. It must not reveal either target interpretation.

## Renderer hard negatives

- DO NOT draw two clocks for one question.
- DO NOT create different hand positions for daytime and nighttime.
- DO NOT print target times near the clock.
- DO NOT fill either response blank.
- DO NOT remove required face numerals 1–12 merely to avoid answer leakage.
- DO NOT add AM/PM labels unless explicitly requested.

## Layout guidance

For 10 questions on A4 portrait, W08 should attempt an efficient one-page layout such as 2 columns × 5 rows only if the clock remains large enough to read and both answer fields remain writable.

Reduce decorative art before reducing instructional clock size.

## QA

`PROMPT_DAY_NIGHT_SINGLE_FACE_QA=PASS` requires:

- exactly one clock per question;
- exactly two blank answer fields per question;
- same hand state for both interpretations;
- verified 12-hour separation;
- identical minute/second components;
- no target answer leakage;
- canonical face labels preserved.

`PROMPT_DAY_NIGHT_TWO_BLANKS_QA=PASS` requires both labeled blanks to be present.

`PROMPT_DAY_NIGHT_SAME_HAND_STATE_QA=PASS` requires one renderer hand state per question, not separate day/night states.

Artifact QA remains separate. Before the downstream image is inspected:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`.