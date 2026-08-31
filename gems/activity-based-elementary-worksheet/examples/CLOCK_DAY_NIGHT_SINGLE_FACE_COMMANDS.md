# Clock Day/Night Single-Face — Teacher Command Examples

Compatible Gem baseline: 2.6.x

## Core behavior

One question uses one analog clock image and asks for both daytime and nighttime answers.

Default response line:

`กลางวัน ........ น. | กลางคืน ........ น.`

## Examples

### ป.2 ชั่วโมงเต็ม
`ป.2 อ่านนาฬิกาเข็ม 10 ข้อ ชั่วโมงเต็ม ให้ 1 หน้าปัดถามทั้งกลางวันและกลางคืน ไม่มีเฉลย`

### ป.3 ครึ่งชั่วโมง
`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ให้ภาพนาฬิกา 1 ภาพต่อข้อ และตอบทั้งกลางวันกับกลางคืน รูปแบบ กลางวัน ........ น. | กลางคืน ........ น. ไม่มีเฉลย`

### ป.3 ทุก 5 นาที
`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ ช่วงเวลา 5 นาที 1 หน้าปัดต่อข้อ ถามทั้งกลางวันและกลางคืน ไม่มีเฉลย`

### ป.4 ละเอียด 1 นาที
`ป.4 อ่านนาฬิกาเข็ม 10 ข้อ ความละเอียด 1 นาที ใช้หน้าปัดเดียวต่อข้อ และมีช่องตอบกลางวัน/กลางคืน 2 ช่อง ไม่มีเฉลย`

### Explicit parameter-style request
`CLOCK_READING_MODE=DAY_NIGHT_PAIR; ONE_CLOCK_TWO_ANSWERS=YES; CLOCKS_PER_QUESTION=1; ANSWER_FIELDS_PER_QUESTION=2; DAY_NIGHT_LABELS=กลางวัน,กลางคืน; ANSWER_TIME_FORMAT=24_HOUR`

## Expected prompt behavior

- exactly one analog clock per question
- exactly two blank response fields
- same hand state for both interpretations
- verified pair differs by 12 hours modulo 24
- no target time printed on worksheet
- canonical numerals remain visible
- renderer-only geometry remains in Final Prompt

## Regression example

A 10:30 face must be drawn once:

- minute hand 180°
- hour hand 315°
- halfway 10–11

The two verified interpretations are 10:30 and 22:30 under the active mapping, but neither is printed when answer key is off.