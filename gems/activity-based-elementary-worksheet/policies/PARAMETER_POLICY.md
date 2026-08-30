# Parameter Policy — Activity-Based Elementary Worksheet Generator

Version: 2.3.2
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
Derive from the stated skill. Ask only if multiple task types materially change the objective.

### `LANGUAGE`
Default THAI for Thai requests.

### Domain values with no safe default
Ask only when a missing value materially changes correctness and cannot be safely inferred.

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
| TARGET_PAGE_COUNT | OPTIONAL_DEFAULT | 1 |
| ONE_PAGE_PREFERRED | OPTIONAL_DEFAULT | YES |
| ONE_PAGE_LOCK | OPTIONAL_DEFAULT | OFF |
| AUTO_PAGINATION | OPTIONAL_DEFAULT | YES_AFTER_ONE_PAGE_OPTIMIZATION when lock is OFF |
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

### Render / prompt

| Parameter | Class | Default/Auto |
|---|---|---|
| RENDER_PATH | OPTIONAL_AUTO | AUTO |
| RENDER_OBJECTIVE | OPTIONAL_DEFAULT | STUDENT_WORKSHEET |
| VISUAL_QA_REQUIRED | OPTIONAL_AUTO | YES when nondeterministic rendering carries academic risk |
| OUTPUT_MODE | OPTIONAL_DEFAULT | PROMPT_PACKAGE |
| PRIMARY_DELIVERABLE | OPTIONAL_DEFAULT | FINAL_IMAGE_GENERATION_PROMPT |
| PER_ITEM_RENDER_STATE_REQUIRED | OPTIONAL_AUTO | YES for visual questions |
| TARGET_ALIGNMENT_REQUIRED | OPTIONAL_AUTO | YES for learner-read instruments |

`RENDER_PATH` values:

- `AUTO`
- `DOCUMENT_FIRST`
- `HYBRID`
- `DETERMINISTIC_VECTOR`
- `IMAGE_ONLY`

AUTO resolution guidance:

- text/table/numeric-heavy → `DOCUMENT_FIRST` or `HYBRID`;
- exact instrument/graph + theme art → `HYBRID`;
- mostly deterministic educational diagram → `DETERMINISTIC_VECTOR`;
- `IMAGE_ONLY` only when text/data/geometry fidelity is not threatened or explicitly requested.

Thai text-heavy worksheets and exact measuring-instrument worksheets must not default to generative image-only rendering.

### Render safety

Teachers normally do not set these.

| Parameter | Default |
|---|---|
| CONTENT_LOCK | ON |
| THAI_TEXT_LOCK | ON |
| NUMERIC_VALUE_LOCK | ON |
| QUESTION_COUNT_LOCK | ON |
| ANSWER_LEAK_GUARD | ON |
| TARGET_VALUE_LEAK_GUARD | ON when renderer-only targets exist |
| GEOMETRY_LOCK | ON when geometry carries educational meaning |
| TEMPLATE_LOCK | ON for repeated instruments/graphs |
| PER_ITEM_RENDER_STATE_REQUIRED | YES for visual questions |
| TARGET_ALIGNMENT_REQUIRED | YES for learner-read instruments |

## 6. Global one-page policy — applies to EVERY worksheet family

Default:

`ONE_PAGE_PREFERRED = YES`
`TARGET_PAGE_COUNT = 1`

The layout engine MUST attempt a valid one-page A4 solution before page 2.

Optimization order:

1. preserve academic correctness and exact question count;
2. preserve domain minimum diagram/instrument size;
3. preserve readable Thai text and writable answer space;
4. choose a more efficient valid layout;
5. remove/simplify decoration;
6. shorten nonessential instructions;
7. reduce nonessential whitespace/padding within safe limits;
8. reduce decorative context size;
9. only then paginate when `ONE_PAGE_LOCK=OFF`.

Never achieve one page by shrinking instruments below minimum size, distorting diagrams, making text unreadable, removing required data/answer fields, clipping, overlapping, reducing question count, leaking answers/targets, or changing the objective.

### 6.1 ONE_PAGE_LOCK

`ONE_PAGE_LOCK = OFF` by default.

Explicit requests such as `1 หน้าเท่านั้น` or `A4 หน้าเดียว` normalize to:

`ONE_PAGE_LOCK = ON`
`PAGE_COUNT = 1`

If a valid one-page layout is impossible after optimization:

`ONE_PAGE_FEASIBILITY_QA = FAIL`
`LAYOUT_QA = FAIL`

Do not create page 2 and do not silently violate readability. A safe alternative may be proposed but requires user approval.

### 6.2 Feasibility planning

Estimate capacity from:

`usable_page_area ÷ per_question_minimum_footprint`

The footprint includes required text, answer area, and domain minimum educational diagram size.

Test plausible structures such as 1-column rows, 2-column cards, 3-column compact cards, tables for text/numeric tasks, and grids for visual/instrument tasks. Select the most readable valid one-page solution, not merely the densest.

## 7. Domain-specific defaults

### TIME / elapsed time
- TIME_FORMAT = 24_HOUR
- TIME_CROSS_MIDNIGHT_ALLOWED = NO
- ANSWER_DISTRIBUTION = BALANCED
- difficulty controls minute granularity
- preferred render path for text/table-heavy sheets = DOCUMENT_FIRST or HYBRID

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
- canonical 5kg teaching dial = 300° active sweep + 60° inactive gap, not 360°
- default 10-question A4 portrait layout = 2 columns × 5 rows if minimum dial size is preserved
- preferred render path = HYBRID or DETERMINISTIC_VECTOR

### TIME_CLOCK / analog clock
- CLOCK_FORMAT = 12_HOUR
- standard 12/3/6/9 orientation
- two hands only unless seconds requested
- minute granularity derived from grade/difficulty
- HOUR_HAND_MODE = CONTINUOUS_INTERPOLATION
- TEMPLATE_LOCK = ON
- `CLOCK_READING_MODE=SINGLE|DAY_NIGHT_PAIR`
- day/night pair uses one clock + two answer fields
- preferred render path = HYBRID or DETERMINISTIC_VECTOR

### MEASUREMENT_LENGTH / ruler
- metric system
- MAJOR_DIVISION = 1 cm
- MINOR_DIVISION = 1 mm when mm reading is taught
- START_POSITION_MODE = ZERO for beginner worksheets
- preferred render path = HYBRID or DETERMINISTIC_VECTOR

### MEASUREMENT_TEMPERATURE
- UNIT = Celsius for Thai primary default
- vertical scale
- target must be exactly representable by MINOR_INTERVAL unless interpolation is explicitly taught
- liquid endpoint must align exactly to target graduation
- preferred render path = HYBRID or DETERMINISTIC_VECTOR

### MEASUREMENT_CAPACITY
- UNIT = L or mL derived from topic
- MENISCUS_MODE = SIMPLE_FLAT for early primary unless science-specific meniscus reading is requested
- scientific mode must explicitly lock READ_BOTTOM_MENISCUS or READ_TOP_MENISCUS
- renderer-only target numbers must not be printed as labels/annotations
- preferred render path = HYBRID or DETERMINISTIC_VECTOR

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
- preferred render path = DOCUMENT_FIRST, HYBRID, or DETERMINISTIC_VECTOR depending visualization

## 8. Prompt-generation defaults

Unless explicitly overridden:

`OUTPUT_MODE=PROMPT_PACKAGE`
`PRIMARY_DELIVERABLE=FINAL_IMAGE_GENERATION_PROMPT`

A visual question is production-complete only when its final prompt has one canonical template plus an explicit renderer state for every item. High-risk instrument states use:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`.

## 9. Default resolution algorithm

For every field:

1. valid explicit user value wins;
2. else apply domain-specific default;
3. else apply core default/auto rule;
4. record resolved value;
5. resolve KB route/compatibility;
6. resolve `RENDER_PATH`;
7. run one-page feasibility planning;
8. if no safe rule exists and correctness changes, ask one concise clarification.

## 10. Teacher-friendly rule

Bad interaction:

> Please provide MAX_CAPACITY, MINOR_DIVISION, TEMPLATE_LOCK, GEOMETRY_LOCK...

Good interaction:

> ได้ครับ ป.3 การอ่านตราชั่ง 10 ข้อ ผมจะใช้ตราชั่ง 5 กก. ขีดย่อย 0.1 กก. A4 แนวตั้ง ขาวดำ ไม่ใส่เฉลย จัดให้จบใน 1 หน้าเป็นอันดับแรก และสร้าง Final Image Generation Prompt ที่ล็อกหน้าปัดกับตำแหน่งเข็มให้ครบทุกข้อ

The teacher may override visible educational choices in ordinary language.

## 11. Advanced users

Automation builders may provide structured parameters directly. The same normalization, KB routing, and QA still apply. Technical input never bypasses validation.