# Parameter Policy — Activity-Based Elementary Worksheet Generator

Version: 2.2.0
Status: Canonical supporting policy
Audience: teachers, Gem maintainers, automation builders

## 1. Principle

Teachers use natural language. Parameter names are an internal normalization contract.

Every parameter belongs to exactly one class:

1. `REQUIRED`
2. `CONDITIONALLY_REQUIRED`
3. `OPTIONAL_DEFAULT`
4. `OPTIONAL_AUTO`
5. `OPTIONAL_NONE`

No released spec may contain silent `UNDEFINED` values.

## 2. Minimum teacher-facing input

Normally require only:

- `GRADE_LEVEL`
- `TOPIC_OR_SKILL`
- `QUESTION_COUNT`

Examples:

> ป.3 การอ่านตราชั่ง 10 ข้อ

> ป.2 อ่านนาฬิกา 8 ข้อ

> ป.4 อ่านกราฟแท่ง 10 ข้อ

If a topic is clearly mathematical, infer `SUBJECT=คณิตศาสตร์`.

## 3. Required parameters

### `GRADE_LEVEL` — REQUIRED
Affects difficulty, wording, diagram density, and answer space.

### `TOPIC_OR_SKILL` — REQUIRED
Used to route to a domain engine and derive objective/question type.

### `QUESTION_COUNT` — REQUIRED
Affects content generation and layout capacity. If omitted, ask one short question rather than inventing a production count.

## 4. Conditionally required

### `SUBJECT`
Infer when unambiguous.

### `QUESTION_TYPE`
Derive from the stated skill. Ask only if multiple task types materially change the learning objective.

### `LANGUAGE`
Default THAI for Thai requests.

### Domain values with no safe default
If a specialized domain needs a parameter that materially changes correctness and cannot be safely inferred, ask only for that parameter.

## 5. Core optional parameters

### Education

| Parameter | Class | Default/Auto |
|---|---|---|
| SUBJECT | CONDITIONALLY_REQUIRED | derive from topic |
| SUBTOPIC | OPTIONAL_AUTO | derive |
| LEARNING_OBJECTIVE | OPTIONAL_AUTO | derive from grade + skill |
| DIFFICULTY | OPTIONAL_AUTO | AUTO |
| LANGUAGE | OPTIONAL_DEFAULT | THAI for Thai request |
| CURRICULUM_CONTEXT | OPTIONAL_NONE | no binding unless requested |

### Content

| Parameter | Class | Default/Auto |
|---|---|---|
| QUESTION_TYPE | CONDITIONALLY_REQUIRED | domain route |
| ANSWER_TYPE | OPTIONAL_AUTO | derive |
| QUESTION_FORMAT | OPTIONAL_AUTO | derive |
| SHOW_QUESTION_NUMBER | OPTIONAL_DEFAULT | YES |
| SHOW_ANSWER_KEY | OPTIONAL_DEFAULT | NO |
| CONTEXT_MODE | OPTIONAL_DEFAULT | child-appropriate real-life context |
| THEME | OPTIONAL_DEFAULT | CUTE_SCHOOL / domain-appropriate |
| ITEM_SET | OPTIONAL_NONE | engine chooses if absent |
| DISTRIBUTION_MODE | OPTIONAL_DEFAULT | BALANCED |

### Page / Print

| Parameter | Class | Default/Auto |
|---|---|---|
| PAGE_SIZE | OPTIONAL_DEFAULT | A4 |
| ORIENTATION | OPTIONAL_DEFAULT | PORTRAIT |
| PAGE_COUNT | OPTIONAL_AUTO | target 1 page first |
| ONE_PAGE_PREFERRED | OPTIONAL_DEFAULT | YES |
| ONE_PAGE_LOCK | OPTIONAL_DEFAULT | OFF |
| AUTO_PAGINATION | OPTIONAL_DEFAULT | YES, but only after one-page optimization when lock is OFF |
| DENSITY_MODE | OPTIONAL_AUTO | derive from payload |
| COLOR_MODE | OPTIONAL_DEFAULT | BLACK_AND_WHITE |
| SAFE_MARGIN | OPTIONAL_DEFAULT | YES |
| PRINT_MODE | OPTIONAL_DEFAULT | PRINTABLE |

### Header/Text

| Parameter | Class | Default/Auto |
|---|---|---|
| SHOW_STUDENT_HEADER | OPTIONAL_DEFAULT | YES |
| HEADER_FIELDS | OPTIONAL_DEFAULT | ชื่อ / ชั้น / เลขที่ |
| WORKSHEET_TITLE | OPTIONAL_AUTO | derive |
| SHOW_INSTRUCTION | OPTIONAL_DEFAULT | YES |
| INSTRUCTION_TEXT | OPTIONAL_AUTO | short grade-appropriate instruction |
| TEXT_RENDER_MODE | OPTIONAL_DEFAULT | HYBRID for Thai-heavy pages |

### Design

| Parameter | Class | Default/Auto |
|---|---|---|
| VISUAL_THEME | OPTIONAL_DEFAULT | CUTE_SCHOOL |
| ART_STYLE | OPTIONAL_DEFAULT | clean child-friendly line art |
| SHOW_CHARACTERS | OPTIONAL_DEFAULT | YES, decorative only |
| CHARACTER_LOCATION | OPTIONAL_DEFAULT | corners/header/footer |
| ICON_STYLE | OPTIONAL_DEFAULT | simple outlined semantic icon |
| BORDER_STYLE | OPTIONAL_DEFAULT | rounded/simple |
| DECORATION_DENSITY | OPTIONAL_DEFAULT | LOW_TO_MEDIUM for data-heavy worksheets |
| LINE_WEIGHT | OPTIONAL_DEFAULT | CONSISTENT |

### Render safety

Teachers normally do not set these.

| Parameter | Default |
|---|---|
| CONTENT_LOCK | ON |
| THAI_TEXT_LOCK | ON |
| NUMERIC_VALUE_LOCK | ON |
| QUESTION_COUNT_LOCK | ON |
| ANSWER_LEAK_GUARD | ON |
| GEOMETRY_LOCK | ON when geometry carries educational meaning |
| TEMPLATE_LOCK | ON for repeated instruments/graphs |

## 6. Global one-page policy — applies to EVERY worksheet family

The product default is:

`ONE_PAGE_PREFERRED = YES`

This applies globally to arithmetic, word problems, time, analog clocks, scales, rulers, thermometers, capacity, money, calendars, graphs/tables, language worksheets, color-by-code, and future domains unless a specialized engine explicitly requires otherwise.

### 6.1 Meaning of ONE_PAGE_PREFERRED

The layout engine MUST attempt a valid one-page A4 solution before adding a second page.

Optimization order:

1. preserve academic correctness and exact question count;
2. preserve domain minimum diagram/instrument size;
3. preserve readable Thai text and writable answer space;
4. choose a more space-efficient valid layout (rows, columns, cards, grid, table, compact repeated pattern);
5. remove or simplify footer art, characters, borders, decorative labels, and nonessential illustrations;
6. shorten instructions without changing meaning;
7. reduce nonessential whitespace/padding within safe limits;
8. reduce decorative context size while keeping instructional content dominant;
9. only then consider pagination when `ONE_PAGE_LOCK=OFF`.

Never achieve one page by:

- shrinking educational instruments below domain minimum size;
- distorting/stretching diagrams;
- reducing Thai text to an unreadable size;
- removing required question data or answer fields;
- clipping/cropping content;
- overlapping text, diagrams, or answer areas;
- silently reducing question count;
- leaking answers;
- changing the learning objective.

### 6.2 ONE_PAGE_LOCK

`ONE_PAGE_LOCK = OFF` by default.

When a teacher explicitly says such as:

> 1 หน้าเท่านั้น

> ให้อยู่ใน A4 หน้าเดียว

normalize to:

`ONE_PAGE_LOCK = ON`
`PAGE_COUNT = 1`

When locked, page 2 is prohibited.

If a pedagogically valid one-page layout is impossible after the optimization sequence above, the Gem MUST NOT silently shrink, crop, remove questions, or violate a domain minimum. It must return:

`ONE_PAGE_FEASIBILITY_QA = FAIL`
`LAYOUT_QA = FAIL`

and briefly state the blocking constraint. The system may propose the smallest safe change (for example landscape orientation, fewer questions, a larger paper size, or two pages), but it must not violate the explicit one-page lock without user approval.

### 6.3 One-page feasibility planning

Before compiling the render prompt, estimate capacity from:

`usable_page_area ÷ per_question_minimum_footprint`

where the minimum footprint includes required text, answer area, and domain-specific diagram/instrument minimum size.

For repeated questions, test likely structures such as:

- 1 column × N rows
- 2 columns × N rows
- 3 columns × N rows when text payload is small
- compact tables for text/numeric tasks
- card grids for visual/instrument tasks
- mosaic/high-density structures only when readability remains valid

Select the most readable valid one-page layout, not merely the densest.

### 6.4 Default normalized result

Unless the user overrides it, every worksheet normalized spec should include:

`PAGE_SIZE = A4`
`ORIENTATION = PORTRAIT`
`ONE_PAGE_PREFERRED = YES`
`ONE_PAGE_LOCK = OFF`
`TARGET_PAGE_COUNT = 1`
`AUTO_PAGINATION = YES_AFTER_ONE_PAGE_OPTIMIZATION`

## 7. Domain-specific defaults

### TIME / elapsed time

- TIME_FORMAT = 24_HOUR
- TIME_CROSS_MIDNIGHT_ALLOWED = NO
- ANSWER_DISTRIBUTION = BALANCED
- difficulty controls minute granularity

### MEASUREMENT_WEIGHT / dial scale

For Thai Grade 3 unless explicitly changed:

- DIAL_MAX_KG = 5
- MAJOR_DIVISION_KG = 1
- MINOR_DIVISION_KG = 0.1
- MINOR_DIVISIONS_PER_KG = 10
- TICK_MEANING = 1 ขีด = 0.1 กก. = 100 กรัม
- ANSWER_FORMAT = `........ กิโลกรัม ........ ขีด`
- DIAL_SHAPE = TRUE_CIRCLE
- VIEW = FRONT_ORTHOGRAPHIC
- CENTER_PIVOT_LOCK = ON
- SINGLE_NEEDLE_ONLY = YES
- NEEDLE_TARGET_MODE = EXACT_TICK
- default 10-question A4 portrait layout = 2 columns × 5 rows if minimum dial size is preserved

### TIME_CLOCK / analog clock

- CLOCK_FORMAT = 12_HOUR
- standard 12/3/6/9 orientation
- two hands only unless seconds requested
- minute granularity derived from grade/difficulty
- TEMPLATE_LOCK = ON
- visual clock tasks must respect the clock-domain minimum size even when one-page optimization is active

### MEASUREMENT_LENGTH / ruler

- metric system
- MAJOR_DIVISION = 1 cm
- MINOR_DIVISION = 1 mm when mm reading is taught
- START_POSITION_MODE = ZERO for beginner worksheets

### MEASUREMENT_TEMPERATURE

- UNIT = Celsius for Thai primary default
- vertical scale
- min/max/interval derived from objective or safe grade-appropriate range

### MEASUREMENT_CAPACITY

- UNIT = L or mL derived from topic
- MENISCUS_MODE = SIMPLE_FLAT for early primary unless science-specific meniscus reading is requested

### MONEY

- CURRENCY = THB for Thai context
- arithmetic performed in smallest currency unit when decimals are active
- SHOW_ANSWER_KEY = NO

### CALENDAR

- real Gregorian date relationships
- WEEK_START derived from worksheet convention and recorded explicitly
- invalid dates prohibited

### DATA_READING

- DATASET is canonical before visualization
- graph/table must visualize exact dataset
- 3D/perspective graph distortion prohibited

## 8. Default resolution algorithm

For every field:

1. valid explicit user value wins;
2. else apply domain-specific default;
3. else apply core default/auto rule;
4. record resolved value in normalized spec;
5. run one-page feasibility planning;
6. if no safe rule exists and correctness changes, ask one concise clarification.

## 9. Teacher-friendly rule

Bad interaction:

> Please provide MAX_CAPACITY, MINOR_DIVISION, TEMPLATE_LOCK, GEOMETRY_LOCK...

Good interaction:

> ได้ครับ ป.3 การอ่านตราชั่ง 10 ข้อ ผมจะใช้ตราชั่ง 5 กก. แบ่งขีดย่อย 0.1 กก. A4 แนวตั้ง ขาวดำ ไม่ใส่เฉลย และจะจัดให้จบใน 1 หน้าเป็นอันดับแรกโดยอัตโนมัติ

The teacher may override any visible educational choice in ordinary language.

## 10. Advanced users

Automation builders may provide structured parameter names directly. The same normalization and QA still apply. Technical input never bypasses validation.