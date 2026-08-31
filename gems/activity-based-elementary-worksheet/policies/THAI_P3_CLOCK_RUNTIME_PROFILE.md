# Thai Primary 3 Analog Clock Runtime Profile

Version: 1.0.0
Compatible Gem baseline: 2.6.x
Priority: mandatory runtime normalization profile for Thai P3 analog-clock reading

## Trigger

Apply when all are true unless explicitly overridden by the teacher:

- language/context is Thai;
- grade is ป.3 / Primary 3;
- task is analog-clock reading.

## Mandatory default resolution

For a generic request such as:

`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ไม่มีเฉลย`

normalize to:

`CLOCK_READING_MODE=DAY_NIGHT_PAIR`
`ONE_CLOCK_TWO_ANSWERS=YES`
`CLOCKS_PER_QUESTION=1`
`ANSWER_FIELDS_PER_QUESTION=2`
`DAY_NIGHT_LABELS=กลางวัน,กลางคืน`
`ANSWER_TIME_FORMAT=24_HOUR`

The Student Blueprint and Final Prompt must therefore show exactly two blank response fields per clock, e.g.:

`กลางวัน ........ น. | กลางคืน ........ น.`

Do not silently fall back to one generic answer line.

Teacher may override this only by explicitly requesting SINGLE / one answer / AM-only / PM-only or another unambiguous single-interpretation format.

## Strict half-hour wording

`เน้นเวลาครึ่งชั่วโมง`, `เฉพาะครึ่งชั่วโมง`, `half-hour only`, and equivalent wording mean:

`TARGET_MINUTE_MODE=EXACT_MINUTE_SET`
`TARGET_MINUTE_SET={30}`

All target minute values must be exactly 30 unless the teacher explicitly requests mixed whole-hour items.

## Required per-item renderer state

Every learner-read clock item must serialize all of:

1. semantic target;
2. exact numeric `minute_angle`;
3. exact numeric `hour_angle`;
4. relational wording;
5. item-specific hard negative.

For `h:30`:

`minute_angle=180°`
`hour_angle=(30*(h mod 12)+15) mod 360`

Relational wording alone such as `halfway between 10 and 11` is insufficient.

## Clock topology lock

For this profile use the canonical full minute face:

- numerals 1–12 preserved;
- 60 equal minute positions/ticks when the configured template requires minute ticks;
- do not reduce to only 5-minute ticks merely because page space is tight;
- reduce decoration or paginate when unlocked rather than degrading instructional topology.

## Page-policy provenance

Default remains:

`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

`ONE_PAGE_LOCK=ON` is allowed only when the teacher explicitly requests a one-page lock such as `1 หน้าเท่านั้น` or `A4 หน้าเดียว`.

A 2-column × 5-row layout may be chosen while `ONE_PAGE_LOCK=OFF` if it safely fits.

## Deterministic day/night mapping

For one 12-hour face `h12:m`:

- `h12=1..5`: กลางวัน=`h12+12`, กลางคืน=`h12`
- `h12=6..11`: กลางวัน=`h12`, กลางคืน=`h12+12`
- `h12=12`: กลางวัน=`12`, กลางคืน=`00`

Preserve minute/second components. Never use `24:xx`; use `00:xx`.

## Release-blocking runtime invariants

Block prompt release if any occur:

- Thai P3 generic analog-clock request outputs one answer field without explicit SINGLE provenance;
- strict half-hour output contains `:00` targets;
- `ONE_PAGE_LOCK=ON` without explicit provenance;
- a high-risk clock item lacks numeric hand angles;
- Student Blueprint contains target times/angles;
- Final Prompt allows reduced/incomplete clock graduations for layout convenience;
- QA reports PASS/APPROVED while one of these violations exists.
