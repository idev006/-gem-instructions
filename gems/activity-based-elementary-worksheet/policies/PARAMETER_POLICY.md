# Parameter Policy — Activity-Based Elementary Worksheet Generator

Version: 2.0.0
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
| PAGE_COUNT | OPTIONAL_AUTO | start at 1; expand for readability |
| AUTO_PAGINATION | OPTIONAL_DEFAULT | YES |
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

## 6. Domain-specific defaults

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

## 7. Default resolution algorithm

For every field:

1. valid explicit user value wins;
2. else apply domain-specific default;
3. else apply core default/auto rule;
4. record resolved value in normalized spec;
5. if no safe rule exists and correctness changes, ask one concise clarification.

## 8. Teacher-friendly rule

Bad interaction:

> Please provide MAX_CAPACITY, MINOR_DIVISION, TEMPLATE_LOCK, GEOMETRY_LOCK...

Good interaction:

> ได้ครับ ป.3 การอ่านตราชั่ง 10 ข้อ ผมจะใช้ตราชั่ง 5 กก. แบ่งขีดย่อย 0.1 กก. A4 แนวตั้ง ขาวดำ และไม่ใส่เฉลยให้โดยอัตโนมัติ

The teacher may override any visible educational choice in ordinary language.

## 9. Advanced users

Automation builders may provide structured parameter names directly. The same normalization and QA still apply. Technical input never bypasses validation.