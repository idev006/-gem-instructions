# Clock Day/Night Single-Face Regression — 2.6.x

Version: 1.1.0
Status: Critical prompt-generation regression
Owner: `W02_TIME_CLOCK`
Release auditor: `W09_QA_RELEASE`

## DN-01 — Thai P3 AUTO mode
Request: `ป.3 อ่านนาฬิกาเข็ม 10 ข้อ`

Expected normalized mode:

`CLOCK_READING_MODE=DAY_NIGHT_PAIR`
`ONE_CLOCK_TWO_ANSWERS=YES`

unless the teacher explicitly requests SINGLE.

## DN-02 — one face only
Each DAY_NIGHT_PAIR question contains exactly one analog clock face.

## DN-03 — exactly two blanks
Each paired question contains exactly two blank response fields:

`กลางวัน ........ น. | กลางคืน ........ น.`

or an explicitly requested equivalent.

## DN-04 — same hand state
Both interpretations use exactly the same clock geometry. There is one renderer hand state per question.

## DN-05 — deterministic label mapping
For Thai paired reading:

- h12 1..5 → `กลางวัน=h+12`, `กลางคืน=h`
- h12 6..11 → `กลางวัน=h`, `กลางคืน=h+12`
- h12 12 → `กลางวัน=12`, `กลางคืน=00`

Examples:

- 01:30 → กลางวัน 13:30 | กลางคืน 01:30
- 05:30 → กลางวัน 17:30 | กลางคืน 05:30
- 06:30 → กลางวัน 06:30 | กลางคืน 18:30
- 10:30 → กลางวัน 10:30 | กลางคืน 22:30
- 12:30 → กลางวัน 12:30 | กลางคืน 00:30

## DN-06 — 12-hour relation
Paired values differ by exactly 12 hours modulo 24.

## DN-07 — minute preservation
Both answers preserve the same minute component.

## DN-08 — second preservation
If seconds are active, both answers preserve the same second component.

## DN-09 — midnight representation
Use `00:xx`, never `24:xx`.

## DN-10 — strict half-hour intent
Request: `ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ไม่มีเฉลย`

Expected:

`TARGET_MINUTE_MODE=EXACT_MINUTE_SET`
`TARGET_MINUTE_SET={30}`

Every one of the 10 target times must have minute=30. Any `:00` item is FAIL unless mixed whole-hour targets were explicitly requested.

## DN-11 — Student Blueprint isolation
Student Blueprint may contain one neutral clock template + two blank labeled fields, but contains no target face time, day/night answers, hand angles, renderer hard negatives or `RENDER_ONLY_NOT_FOR_WORKSHEET` item block.

## DN-12 — renderer metadata retained
Final Prompt contains one renderer state per item marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

## DN-13 — numeric angles mandatory
Every high-risk clock renderer item includes numeric angles.

For `h:m`:

`minute_angle=6*m`
`hour_angle=30*(h mod 12)+0.5*m`

Relational wording alone is insufficient.

## DN-14 — 10:30 regression
For face 10:30:

- minute hand = 180°
- hour hand = 315°
- hour hand exactly halfway 10–11
- day = 10:30
- night = 22:30
- hard negative: hour hand not directly on 10

## DN-15 — no target labels
Neither paired answer may be printed beside/inside the clock when `SHOW_ANSWER_KEY=NO`.

## DN-16 — canonical numerals preserved
Clock numerals 1–12 remain visible when the template requires them.

## DN-17 — page-lock provenance
The request `ป.3 อ่านนาฬิกาเข็ม 10 ข้อ...` does not by itself activate `ONE_PAGE_LOCK`.

Expected default:

`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

Only explicit one-page-only wording may turn the lock ON.

## DN-18 — layout readability
A 2×5 A4 layout is allowed only if clocks remain readable and both answer fields remain writable. Decoration is reduced first.

## DN-19 — false-PASS prevention
If Student Blueprint isolation, paired blanks, half-hour exactness, numeric renderer angles or page-lock provenance fails, W09 must emit:

`PROMPT_RELEASE=BLOCKED`

It is forbidden to report `PROMPT_RELEASE=APPROVED` with any applicable critical failure.

## DN-20 — artifact boundary
Before actual image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

## Release rule

Any wrong default mode, wrong label mapping, two-clock substitution, changed hand state, missing blank, non-30 minute under strict half-hour intent, target leak, missing numeric angle, invalid page-lock provenance or false-PASS release blocks prompt release.