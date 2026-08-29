# Acceptance Tests — Activity-Based Elementary Worksheet Generator

Version: 1.0.0
Status: Critical QA / Regression Suite

A production release passes only when all critical tests below pass.

## Test 1 — Intent normalization

Input:

> สร้างใบงาน ป.3 คณิตศาสตร์ เรื่องการหาระยะเวลา 10 ข้อ ธีมกิจกรรมประจำวัน A4 แนวตั้ง ขาวดำ ไม่ต้องมีเฉลย

Expected:

- Grade = ป.3
- Subject = คณิตศาสตร์
- Domain = TIME
- Question count = 10
- A4 portrait
- black and white
- answer key disabled
- daily-activity context

Fail if any explicit user requirement changes silently.

## Test 2 — Exact question count

For `QUESTION_COUNT = 10`, the verified content blueprint and final prompt must contain exactly 10 question rows.

Fail on 9, 11, omitted rows, duplicated IDs, or decorative elements mistaken for questions.

## Test 3 — Whole-hour elapsed-time correctness

Input constraints:

```text
DIFFICULTY = EASY
ALLOW_FULL_HOURS_ONLY = YES
```

Every generated tuple must satisfy:

```text
(end_minutes - start_minutes) % 60 = 0
```

Examples that must pass:

- 08:15 → 10:15 = 2 ชั่วโมง
- 09:30 → 11:30 = 2 ชั่วโมง
- 06:45 → 07:45 = 1 ชั่วโมง

Example that must fail:

- 08:15 → 10:45 labeled as 2 ชั่วโมง

## Test 4 — Hours-and-minutes correctness

Input constraints:

```text
ALLOW_MINUTES = YES
ANSWER_UNIT_MODE = HOURS_AND_MINUTES
```

Example:

`08:15 → 09:45` must validate as `1 ชั่วโมง 30 นาที`.

Fail if answer is mathematically inconsistent.

## Test 5 — Midnight guard

Input:

```text
TIME_CROSS_MIDNIGHT_ALLOWED = NO
start = 20:00
end = 08:00
```

Expected: reject or repair before final output.

Fail if released as a same-day valid question.

## Test 6 — Student answer blank remains empty

Input:

```text
SHOW_ANSWER_KEY = NO
```

Expected final image prompt must explicitly prohibit pre-filled answers.

Fail if the student worksheet row contains the verified answer in its answer blank.

## Test 7 — Answer key separation

Input:

```text
SHOW_ANSWER_KEY = YES
```

Expected: answer key is separate from student blanks, preferably a separate page or clearly separated section.

Fail if the student activity itself becomes pre-solved without explicit request.

## Test 8 — Duplicate full-question prevention

Two rows with the exact same activity, start time, end time, and answer must not be released unless the user explicitly requests repetition.

Fail on accidental duplicate tuples.

## Test 9 — Intentional activity repetition

Input:

> ใช้ 5 กิจกรรมนี้อย่างละ 2 ข้อ

Expected: repeated activity names are allowed, while the full question tuples remain distinct.

Fail if duplicate QA wrongly rejects intentional activity reuse.

## Test 10 — Semantic icon mapping

Examples:

- `อ่านหนังสือ` must map to a book/reading-related icon.
- `เล่นฟุตบอล` must map to a football-related icon.
- `รดน้ำต้นไม้` must map to plant/watering-related imagery.

Fail if an icon contradicts or confuses the activity.

## Test 11 — Thai canonical terminology

Required canonical strings for the primary time pattern:

- เวลาเริ่มต้น
- เวลาสิ้นสุด
- ใช้เวลา
- ชั่วโมง
- นาที

Fail if canonical text contains misspellings or inconsistent terminology.

## Test 12 — Student header

Default Thai worksheet must include:

`ชื่อ ... ชั้น ... เลขที่ ...`

unless disabled by the user.

Fail if a default student worksheet omits required identity fields without reason.

## Test 13 — Layout capacity

Input:

> 25 detailed elapsed-time questions, A4 portrait, one page

Expected: Gem identifies the density risk. Preferred behavior is pagination unless the user explicitly insists on one page.

Fail if the Gem claims that a heavily compressed page is production-optimal without checking readability.

## Test 14 — Auto-pagination

For question counts or text lengths exceeding readable capacity and `AUTO_PAGINATION = YES`, output must split content across pages with stable headers/layout rules.

Fail if content is cropped or reduced to unreadable size solely to remain on one page.

## Test 15 — Theme-only revision preserves content

Initial state: verified 10-row blueprint.

Revision:

> เปลี่ยนธีมเป็นอวกาศ แต่ห้ามเปลี่ยนโจทย์

Expected:

- activities unchanged;
- start/end times unchanged;
- verified answers unchanged;
- visual theme changed;
- layout/render QA rerun.

Fail if academic values are regenerated.

## Test 16 — Difficulty revision updates content deterministically

Initial state: EASY whole-hour questions.

Revision:

> เปลี่ยนเป็นระดับปานกลาง ให้มีชั่วโมงและนาที

Expected:

- normalized difficulty updated;
- affected question tuples regenerated or adjusted;
- all calculations revalidated;
- layout checked for longer answer labels.

Fail if only the final prompt wording changes while old content remains incompatible.

## Test 17 — No unsupported exact-copy behavior

Input:

> ทำให้เหมือนภาพต้นฉบับทุกพิกเซล

Expected: Gem may use the reference for information architecture and general design grammar but should not claim pixel-perfect copying as its production goal.

Fail if it reproduces creator marks, watermarks, logos, or proprietary characters without authorization.

## Test 18 — Reference image content independence

When a reference worksheet contains example time values, the Gem must not assume those are the required new worksheet values unless the user requests them.

Expected: independently generate and validate canonical data.

Fail if mathematical content is copied blindly from the image.

## Test 19 — Final prompt content lock

Final prompt must include explicit constraints equivalent to:

- do not change times;
- do not change activity names;
- do not invent extra questions;
- do not omit questions;
- do not alter locked Thai text;
- do not pre-fill student answers when answer key is disabled.

Fail if critical educational data is left for the image model to improvise.

## Test 20 — Print usability

For `COLOR_MODE = BLACK_AND_WHITE`, final prompt must request:

- white background;
- high-contrast black line art;
- readable text hierarchy;
- safe margins;
- no essential color coding.

Fail if understanding the worksheet requires color.

## Test 21 — Decoration priority

Decorative children, stars, hearts, clocks, or borders must not:

- cover text;
- intersect answer lines;
- reduce answer space below usable size;
- create ambiguity about question grouping.

Fail on content obstruction.

## Test 22 — Output contract completeness

Default `PROMPT_PACKAGE` output must include:

- NORMALIZED_WORKSHEET_SPEC
- VERIFIED_CONTENT_BLUEPRINT
- LAYOUT_BLUEPRINT
- RENDER_CONSTRAINTS
- QA_REPORT
- FINAL_IMAGE_GENERATION_PROMPT

Fail if a critical section is missing without explicit user request.

## Test 23 — Prompt-only mode

Input:

> ตรวจทุกอย่างภายในแล้วส่งเฉพาะ final prompt

Expected: run the full internal validation process but return only final prompt.

Fail if the Gem skips validation merely because intermediate sections are hidden.

## Test 24 — No fabricated guarantee

The Gem must not claim that any generative image model will render Thai text perfectly.

Expected: lock canonical text and recommend post-render verification.

Fail if it guarantees 100% visual text fidelity from a nondeterministic image generator.

## Test 25 — Release gate

Before production release, all applicable statuses must be PASS:

```text
INTENT_QA = PASS
ACADEMIC_QA = PASS
CALCULATION_QA = PASS
DUPLICATE_QA = PASS
THAI_QA = PASS
LAYOUT_QA = PASS
PRINT_QA = PASS
PROMPT_QA = PASS
```

A critical FAIL blocks final prompt release until repaired.
