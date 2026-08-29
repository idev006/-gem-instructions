# Usage Examples — Activity-Based Elementary Worksheet Generator

Version: 1.0.0

## 1. Happy path

### User

> สร้างใบงาน ป.3 คณิตศาสตร์ เรื่องการบอกระยะเวลาเป็นชั่วโมงและนาที 10 ข้อ ธีมกิจกรรมประจำวัน A4 แนวตั้ง ขาวดำ ไม่ต้องมีเฉลย

### Expected normalization

```text
GRADE_LEVEL = ป.3
SUBJECT = คณิตศาสตร์
DOMAIN = TIME
TOPIC = การบอกระยะเวลาเป็นชั่วโมงและนาที
QUESTION_TYPE = START_TIME_END_TIME_TO_DURATION
QUESTION_COUNT = 10
DIFFICULTY = AUTO
CONTEXT_MODE = EVERYDAY_ACTIVITY
PAGE_SIZE = A4
ORIENTATION = PORTRAIT
COLOR_MODE = BLACK_AND_WHITE
SHOW_STUDENT_HEADER = YES
SHOW_ANSWER_KEY = NO
AUTO_PAGINATION = YES
```

Expected behavior:

- create 10 unique daily-activity rows;
- calculate every elapsed-time answer internally;
- keep student blanks empty;
- generate semantic icons matching activities;
- output a verified content blueprint before the final image prompt.

---

## 2. Minimal prompt

### User

> ใบงาน ป.2 เรื่องเวลา 8 ข้อ

### Expected behavior

Infer safe defaults:

- mathematics;
- Thai language;
- A4 portrait;
- black and white;
- student header;
- no answer key;
- simple age-appropriate elapsed-time questions.

If the exact time skill is ambiguous and would materially change the worksheet, choose the simplest grade-appropriate pattern or ask one concise clarification question.

---

## 3. Detailed prompt

### User

> สร้างใบงาน ป.3 วิชาคณิตศาสตร์ เรื่องหาระยะเวลาจากเวลาเริ่มต้นและสิ้นสุด จำนวน 12 ข้อ ระดับปานกลาง ใช้ระบบ 24 ชั่วโมง ให้คำตอบมีทั้งชั่วโมงและนาที นาทีเป็นช่วงละ 5 นาที ไม่ข้ามเที่ยงคืน ธีมชีวิตประจำวันเด็กไทย มีหมายเลขข้อ มีช่อง ชื่อ ชั้น เลขที่ A4 แนวตั้ง ขาวดำ ไม่ต้องมีเฉลย ใช้เส้นภาพน่ารักแบบ coloring-book แต่ตกแต่งไม่เกิน 15% ของพื้นที่หน้า

### Expected normalization highlights

```text
QUESTION_COUNT = 12
DIFFICULTY = MEDIUM
TIME_FORMAT = 24_HOUR
ALLOW_MINUTES = YES
MINUTE_INTERVAL = 5
TIME_CROSS_MIDNIGHT_ALLOWED = NO
DECORATION_DENSITY = LOW_TO_MEDIUM
SHOW_QUESTION_NUMBER = YES
SHOW_ANSWER_KEY = NO
```

Expected behavior:

- determine whether 12 rows remain readable on one A4 page;
- use compact density or auto-pagination if needed;
- ensure every duration is valid and grade appropriate.

---

## 4. Whole-hour practice

### User

> ป.3 เรื่องระยะเวลา 10 ข้อ ขอแบบง่าย คำตอบเป็นชั่วโมงเต็มทั้งหมด แต่เวลาเริ่มต้นไม่จำเป็นต้องเป็นนาที 00 เช่น 08:15 ถึง 10:15 ได้

### Expected behavior

Use equal minute components in start/end values where useful.

Valid examples:

```text
08:15 → 10:15 = 2 ชั่วโมง
09:30 → 11:30 = 2 ชั่วโมง
06:45 → 07:45 = 1 ชั่วโมง
```

Do not generate unequal minute components that force hour-and-minute subtraction.

---

## 5. Hours and minutes

### User

> ทำให้ยากขึ้น ใช้คำตอบเป็นชั่วโมงและนาทีด้วย

### Expected revision behavior

Update:

```text
ALLOW_FULL_HOURS_ONLY = NO
ALLOW_MINUTES = YES
ANSWER_UNIT_MODE = HOURS_AND_MINUTES
```

Regenerate affected question data and rerun calculation, grade-level, layout, Thai, and prompt QA.

Do not merely alter the wording of the final prompt while leaving the old blueprint unchanged.

---

## 6. Theme-only revision

### User

> เปลี่ยนธีมเป็นอวกาศ แต่ห้ามเปลี่ยนเวลา กิจกรรม และคำตอบของทั้ง 10 ข้อ

### Expected behavior

Lock canonical content and change only visual parameters:

```text
VISUAL_THEME = FRIENDLY_SPACE
VALUE_LOCK = ON
CONTENT_LOCK = ON
```

Rerun layout and render-prompt QA. Do not regenerate academic data.

---

## 7. Remove question numbers

### User

> ไม่เอาหมายเลขข้อ

### Expected behavior

Set:

```text
SHOW_QUESTION_NUMBER = NO
```

Rebalance row layout so the freed column becomes usable whitespace or answer space.

---

## 8. Landscape revision

### User

> เปลี่ยนเป็น A4 แนวนอน แต่คงโจทย์เดิม

### Expected behavior

Set:

```text
ORIENTATION = LANDSCAPE
CONTENT_LOCK = ON
```

Recompile the layout. Do not alter verified source values or answers.

---

## 9. High question count edge case

### User

> ขอ 25 ข้อใน A4 หน้าเดียว

### Expected behavior

Do not blindly force 25 detailed rows onto one portrait page.

Explain or automatically apply the production-safe rule:

- if readability would fail, paginate;
- if the user insists on one page, explicitly warn that the requested density conflicts with primary-school readability and produce the safest compact layout possible without claiming it is optimal.

Default preferred action:

```text
AUTO_PAGINATION = YES
```

---

## 10. Answer key enabled

### User

> ขอหน้าเฉลยด้วย

### Expected behavior

Set:

```text
SHOW_ANSWER_KEY = YES
```

Generate a separate answer-key page or clearly separated answer-key output. Do not print answers inside the student worksheet unless explicitly requested.

---

## 11. Reference-image use case

### User

> ใช้ภาพใบงานที่ส่งให้เป็นตัวอย่างโครงสร้าง แต่ทำธีมและภาพประกอบใหม่ทั้งหมด

### Expected behavior

Extract:

- student header pattern;
- title hierarchy;
- instruction strip;
- repeated question-row grammar;
- icon + label + given data + blank response pattern;
- border/decorative density.

Do not copy:

- creator name;
- watermark;
- exact characters;
- exact decorative frame;
- proprietary branding.

---

## 12. User-supplied activities

### User

> ใช้กิจกรรม 5 อย่างนี้เท่านั้น: อ่านหนังสือ วาดรูป รดน้ำต้นไม้ เล่นฟุตบอล ทำการบ้าน และทำอย่างละ 2 ข้อ

### Expected behavior

Set:

```text
QUESTION_COUNT = 10
ACTIVITY_NAMES = [อ่านหนังสือ, วาดรูป, รดน้ำต้นไม้, เล่นฟุตบอล, ทำการบ้าน]
ACTIVITY_DISTRIBUTION = EXACTLY_2_EACH
```

Full question tuples must still be unique. Repetition of activity names is intentional and should not fail duplicate QA.

---

## 13. Invalid time prevention

The Gem must never release content like:

```text
08:15 → 10:15 = 3 ชั่วโมง
```

or, when midnight crossing is disabled:

```text
20:00 → 08:00
```

Such content must be repaired before the final prompt is emitted.

---

## 14. Thai text lock example

Canonical strings:

```text
ชื่อ ........................................................ ชั้น ............ เลขที่ ............
เวลาเริ่มต้น
เวลาสิ้นสุด
ใช้เวลา
ชั่วโมง
นาที
```

The final image prompt must explicitly tell the rendering model to use these exact strings and not paraphrase them.

---

## 15. Prompt-only output

### User

> ตรวจสอบทุกอย่างให้เสร็จ แล้วส่งเฉพาะ final prompt

### Expected behavior

Perform the full internal pipeline and QA, but return only `FINAL_IMAGE_GENERATION_PROMPT` because the user explicitly selected `PROMPT_ONLY`.
