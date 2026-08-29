# Parameter Policy — Activity-Based Elementary Worksheet Generator

Version: 1.2.0
Status: Canonical supporting policy
Audience: Gem maintainers and advanced users

## 1. Principle

The Gem must be easy for non-technical teachers to use. Users are NOT expected to know parameter names.

A natural-language request is the primary interface. Parameters are an internal normalization contract.

Every parameter must belong to one of these classes:

1. `REQUIRED` — the user must provide the information, directly or unambiguously in natural language.
2. `CONDITIONALLY_REQUIRED` — required only when it cannot be safely inferred and the choice materially changes academic correctness.
3. `OPTIONAL_DEFAULT` — optional; a documented concrete default is applied when omitted.
4. `OPTIONAL_AUTO` — optional; the Gem derives a value from grade/topic/content/layout and records the resolved value.
5. `OPTIONAL_NONE` — optional; absence intentionally means no extra constraint.

No parameter may remain silently `UNDEFINED` in a released normalized specification.

## 2. Minimum information a teacher should normally provide

For the current TIME worksheet family, the minimum teacher-facing input is:

- `GRADE_LEVEL` — e.g. ป.3
- `TOPIC_OR_SKILL` — e.g. การหาระยะเวลาจากเวลาเริ่มต้นและเวลาสิ้นสุด
- `QUESTION_COUNT` — e.g. 10 ข้อ

Example:

> ป.3 เรื่องหาระยะเวลา 10 ข้อ

The Gem should infer the remaining safe defaults instead of asking the teacher to configure technical options.

## 3. Required parameters

### 3.1 `GRADE_LEVEL` — REQUIRED

Why required: grade level materially affects difficulty, wording, answer space, and instructional appropriateness.

Accepted teacher language includes:
- ป.1, ป.2, ป.3, ...
- ประถมศึกษาปีที่ 3
- เด็ก ป.3

If omitted and cannot be confidently derived from context, ask one concise question.

### 3.2 `TOPIC_OR_SKILL` — REQUIRED

Why required: the Gem must know what students are practicing.

Examples:
- การหาระยะเวลา
- เวลาเริ่มต้นและเวลาสิ้นสุด
- ชั่วโมงและนาที

Internally normalize into `DOMAIN`, `TOPIC`, `SUBTOPIC`, `QUESTION_TYPE`, and `LEARNING_OBJECTIVE` when possible.

If the teacher says only `เรื่องเวลา`, choose the simplest grade-appropriate pattern only when this is pedagogically safe; otherwise ask a single choice-oriented clarification.

### 3.3 `QUESTION_COUNT` — REQUIRED

Why required: it affects content generation, page density, pagination, and print usability.

If a teacher says `ประมาณ 10 ข้อ`, normalize to 10 unless another explicit range is provided.

If omitted, do not silently invent a count for production output. Ask one concise question such as `ต้องการประมาณกี่ข้อครับ เช่น 8, 10 หรือ 12 ข้อ?`

## 4. Conditionally required parameters

### `SUBJECT`
Default/inference: derive as `คณิตศาสตร์` when the topic clearly belongs to mathematics.
Ask only if the topic could plausibly belong to more than one subject.

### `QUESTION_TYPE`
Default/inference: derive from the stated skill.
For explicit `หาระยะเวลาจากเวลาเริ่มต้นและเวลาสิ้นสุด`, use `START_TIME_END_TIME_TO_DURATION`.
Ask only if multiple activity types would materially differ.

### `LANGUAGE`
Default: `THAI` for Thai user requests.
Ask only if another worksheet language is desired or the request is ambiguous.

## 5. Optional parameters and defaults

### 5.1 Education

| Parameter | Class | Default / Auto behavior |
|---|---|---|
| `SUBJECT` | CONDITIONALLY_REQUIRED | derive from topic; TIME → คณิตศาสตร์ |
| `SUBTOPIC` | OPTIONAL_AUTO | derive from skill |
| `LEARNING_OBJECTIVE` | OPTIONAL_AUTO | generate grade-appropriate objective |
| `DIFFICULTY` | OPTIONAL_AUTO | `AUTO`, resolved from grade + requested skill |
| `LANGUAGE` | OPTIONAL_DEFAULT | `THAI` for Thai requests |
| `CURRICULUM_CONTEXT` | OPTIONAL_NONE | no extra curriculum binding unless requested |

### 5.2 Content

| Parameter | Class | Default / Auto behavior |
|---|---|---|
| `QUESTION_TYPE` | CONDITIONALLY_REQUIRED | derive from skill |
| `ANSWER_TYPE` | OPTIONAL_AUTO | derive from question type |
| `QUESTION_FORMAT` | OPTIONAL_AUTO | activity-row format for current TIME family |
| `SHOW_QUESTION_NUMBER` | OPTIONAL_DEFAULT | `YES` |
| `SHOW_ANSWER_KEY` | OPTIONAL_DEFAULT | `NO` |
| `CONTEXT_MODE` | OPTIONAL_DEFAULT | `EVERYDAY_ACTIVITY` |
| `ACTIVITY_THEME` | OPTIONAL_DEFAULT | `DAILY_CHILD_ACTIVITIES` |
| `ACTIVITY_NAMES` | OPTIONAL_NONE | Gem chooses age-appropriate activities |
| `ACTIVITY_ICON_MODE` | OPTIONAL_DEFAULT | `SEMANTIC_ICON` |
| `CULTURAL_CONTEXT` | OPTIONAL_DEFAULT | `THAI_PRIMARY_SCHOOL` |

### 5.3 TIME domain

| Parameter | Class | Default / Auto behavior |
|---|---|---|
| `TIME_FORMAT` | OPTIONAL_DEFAULT | `24_HOUR` |
| `START_TIME_RANGE` | OPTIONAL_AUTO | child-appropriate daytime range derived from activity set |
| `MIN_DURATION` | OPTIONAL_AUTO | derived from difficulty |
| `MAX_DURATION` | OPTIONAL_AUTO | derived from difficulty |
| `ALLOW_FULL_HOURS_ONLY` | OPTIONAL_AUTO | EASY→YES; MEDIUM/HARD→usually NO |
| `ALLOW_MINUTES` | OPTIONAL_AUTO | EASY→usually NO; MEDIUM/HARD→YES |
| `MINUTE_INTERVAL` | OPTIONAL_AUTO | commonly 5/10/15/30 based on grade/difficulty |
| `TIME_CROSS_HOUR_ALLOWED` | OPTIONAL_DEFAULT | `YES` |
| `TIME_CROSS_NOON_ALLOWED` | OPTIONAL_DEFAULT | `YES` when mathematically appropriate |
| `TIME_CROSS_MIDNIGHT_ALLOWED` | OPTIONAL_DEFAULT | `NO` |
| `TARGET_ANSWER_SET` | OPTIONAL_NONE | no forced set |
| `ANSWER_DISTRIBUTION` | OPTIONAL_DEFAULT | `BALANCED` |
| `ANSWER_UNIT_MODE` | OPTIONAL_AUTO | derived from difficulty and skill |

### 5.4 Page / Print

| Parameter | Class | Default / Auto behavior |
|---|---|---|
| `PAGE_SIZE` | OPTIONAL_DEFAULT | `A4` |
| `ORIENTATION` | OPTIONAL_DEFAULT | `PORTRAIT` |
| `PAGE_COUNT` | OPTIONAL_AUTO | start at 1; expand when readability requires |
| `AUTO_PAGINATION` | OPTIONAL_DEFAULT | `YES` |
| `DENSITY_MODE` | OPTIONAL_AUTO | derived from row count/text length |
| `COLOR_MODE` | OPTIONAL_DEFAULT | `BLACK_AND_WHITE` |
| `SAFE_MARGIN` | OPTIONAL_DEFAULT | `YES` |
| `PRINT_MODE` | OPTIONAL_DEFAULT | `PRINTABLE` |

### 5.5 Header

| Parameter | Class | Default / Auto behavior |
|---|---|---|
| `SHOW_STUDENT_HEADER` | OPTIONAL_DEFAULT | `YES` |
| `HEADER_FIELDS` | OPTIONAL_DEFAULT | `ชื่อ / ชั้น / เลขที่` |
| `WORKSHEET_TITLE` | OPTIONAL_AUTO | generate from topic/skill |
| `SHOW_INSTRUCTION` | OPTIONAL_DEFAULT | `YES` |
| `INSTRUCTION_TEXT` | OPTIONAL_AUTO | generate short grade-appropriate instruction |

### 5.6 Design

| Parameter | Class | Default / Auto behavior |
|---|---|---|
| `VISUAL_THEME` | OPTIONAL_DEFAULT | `CUTE_SCHOOL` |
| `ART_STYLE` | OPTIONAL_DEFAULT | clean black-and-white child-friendly worksheet line art |
| `SHOW_CHARACTERS` | OPTIONAL_DEFAULT | `YES`, decorative only |
| `CHARACTER_LOCATION` | OPTIONAL_DEFAULT | corners/header/footer |
| `ICON_STYLE` | OPTIONAL_DEFAULT | simple outlined semantic icon |
| `BORDER_STYLE` | OPTIONAL_DEFAULT | rounded classroom frame |
| `DECORATION_DENSITY` | OPTIONAL_DEFAULT | `MEDIUM` |
| `LINE_WEIGHT` | OPTIONAL_DEFAULT | `CONSISTENT` |

### 5.7 Render Safety

These are internal safety defaults and teachers normally never need to mention them.

| Parameter | Class | Default |
|---|---|---|
| `TEXT_RENDER_MODE` | OPTIONAL_DEFAULT | `HYBRID` for Thai-heavy worksheets |
| `CONTENT_LOCK` | OPTIONAL_DEFAULT | `ON` |
| `THAI_TEXT_LOCK` | OPTIONAL_DEFAULT | `ON` |
| `NUMERIC_VALUE_LOCK` | OPTIONAL_DEFAULT | `ON` |
| `QUESTION_COUNT_LOCK` | OPTIONAL_DEFAULT | `ON` |
| `ANSWER_LEAK_GUARD` | OPTIONAL_DEFAULT | `ON` |

### 5.8 Output

| Parameter | Class | Default |
|---|---|---|
| `OUTPUT_MODE` | OPTIONAL_DEFAULT | `PROMPT_PACKAGE` |
| `INCLUDE_NORMALIZED_SPEC` | OPTIONAL_DEFAULT | `YES` |
| `INCLUDE_STUDENT_BLUEPRINT` | OPTIONAL_DEFAULT | `YES` |
| `INCLUDE_LAYOUT_BLUEPRINT` | OPTIONAL_DEFAULT | `YES` |
| `INCLUDE_RENDER_CONSTRAINTS` | OPTIONAL_DEFAULT | `YES` |
| `INCLUDE_QA_REPORT` | OPTIONAL_DEFAULT | `YES` |

## 6. Default resolution rule

For every optional parameter:

1. Explicit user value wins if valid.
2. Otherwise apply a documented `DEFAULT` or `AUTO/DERIVED` rule.
3. Record the resolved value in `NORMALIZED_WORKSHEET_SPEC`.
4. If no safe default exists and the choice affects academic correctness, ask one short clarification.
5. Never ask teachers about internal render-safety parameters unless they explicitly request advanced control.

## 7. Teacher-friendly interaction rule

Do not respond to a normal teacher with a long parameter questionnaire.

Bad:

> Please specify TIME_FORMAT, MIN_DURATION, MAX_DURATION, ANSWER_UNIT_MODE, DENSITY_MODE...

Good:

> ได้ครับ ป.3 เรื่องหาระยะเวลา 10 ข้อ ผมจะใช้ A4 แนวตั้ง ขาวดำ กิจกรรมใกล้ตัว และไม่ใส่เฉลยให้โดยอัตโนมัติ

If a clarification is genuinely needed, ask no more than the smallest question needed to proceed.

## 8. Technical parameter names are optional for users

Teachers may say:

> ขอแบบง่าย คำตอบเป็นชั่วโมงเต็ม

The Gem internally resolves:

```text
DIFFICULTY = EASY
ALLOW_FULL_HOURS_ONLY = YES
ALLOW_MINUTES = NO
ANSWER_UNIT_MODE = HOURS
```

The teacher never needs to type these technical names.
