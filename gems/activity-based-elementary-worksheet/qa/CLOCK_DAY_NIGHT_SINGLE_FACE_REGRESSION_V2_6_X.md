# Clock Day/Night Single-Face Regression — 2.6.x

Status: Critical prompt-generation regression
Owner: `W02_TIME_CLOCK`
Release auditor: `W09_QA_RELEASE`

## DN-01 — one face only
For `CLOCK_READING_MODE=DAY_NIGHT_PAIR`, each question contains exactly one analog clock face.

FAIL if one daytime clock and one nighttime clock are drawn for the same question without explicit user request.

## DN-02 — exactly two blanks
Each paired question contains exactly two blank response fields:

`กลางวัน ........ น. | กลางคืน ........ น.`

or an explicitly requested equivalent.

## DN-03 — same hand state
The daytime and nighttime interpretations use exactly the same hand geometry. There is only one renderer clock state per question.

## DN-04 — 12-hour relation
The verified pair differs by exactly 12 hours modulo 24.

Examples:

- 07:00 ↔ 19:00
- 10:30 ↔ 22:30
- 12:15 ↔ 00:15

## DN-05 — minute preservation
Both paired answers preserve the same minute component.

## DN-06 — second preservation
If seconds are active, both paired answers preserve the same second component.

## DN-07 — midnight representation
For a 12:xx analog face paired with midnight interpretation, use `00:xx`, never `24:xx`.

## DN-08 — Student Blueprint isolation
Student Blueprint contains no target daytime/nighttime values, hand angles or answer pair.

## DN-09 — renderer metadata retained
Final Prompt contains the one required clock renderer state marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

## DN-10 — no target labels
Neither paired answer may appear as a visible annotation beside/inside the clock when `SHOW_ANSWER_KEY=NO`.

## DN-11 — canonical numerals preserved
Clock numerals 1–12 remain visible when the template requires them. Leak guard must not remove them.

## DN-12 — half-hour geometry
For a 10:30 face:

- minute hand = 180°
- hour hand = 315°
- hour hand exactly halfway 10–11
- pair = 10:30 and 22:30 according to the active day/night mapping

## DN-13 — layout readability
A one-page 10-item worksheet may use 2×5 only if each clock remains readable and both response fields remain writable. Decoration is reduced before instructional geometry.

## DN-14 — artifact boundary
Before the actual generated worksheet image is inspected:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

## Release rule

Any two-clock substitution, changed hand state, missing blank, wrong 12-hour relation, target leak or unreadable clock blocks prompt release for DAY_NIGHT_PAIR mode.