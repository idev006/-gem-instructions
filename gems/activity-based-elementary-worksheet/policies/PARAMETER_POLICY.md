# Parameter Policy — Activity-Based Elementary Worksheet Generator

Version: 2.6.0-LTS
Status: Canonical supporting policy
Audience: teachers, Gem maintainers, automation builders

## 1. Principle

Teachers use natural language. Parameter names are an internal normalization contract. No released specification may contain silent `UNDEFINED` production values.

Parameter classes:

`REQUIRED | CONDITIONALLY_REQUIRED | OPTIONAL_DEFAULT | OPTIONAL_AUTO | OPTIONAL_NONE`

## 2. Minimum teacher-facing input

Normally require only:

- `GRADE_LEVEL`
- `TOPIC_OR_SKILL`
- `QUESTION_COUNT`

Infer subject/language/domain when unambiguous. Ask only when a missing value materially changes academic correctness and cannot be safely derived.

## 3. Global defaults

`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`
`SHOW_ANSWER_KEY=NO`
`SHOW_STUDENT_HEADER=YES`
`HEADER_FIELDS=ชื่อ-นามสกุล / ชั้น / เลขที่`
`LANGUAGE=THAI` for Thai request
`COLOR_MODE=BLACK_AND_WHITE`
`RENDER_PATH=AUTO`
`RENDER_OBJECTIVE=STUDENT_WORKSHEET`
`OUTPUT_MODE=PROMPT_PACKAGE`
`PRIMARY_DELIVERABLE=FINAL_IMAGE_GENERATION_PROMPT`
`CURRICULUM_PROFILE=AUTO`

## 4. Curriculum profile

Allowed:

`AUTO | TH_PRIMARY_2568_P1_P3 | TH_CORE_2551_REV2560 | CUSTOM`

`AUTO` uses the conservative grade progression in `domains/MEASUREMENT_COVERAGE_P1_P6.md`; it is a pedagogical default, not a claim that every school uses one identical curriculum sequence.

Explicit teacher requirements override AUTO when academically valid.

## 5. Core education/content parameters

`GRADE_LEVEL, SUBJECT, TOPIC, SUBTOPIC, LEARNING_OBJECTIVE, DIFFICULTY, LANGUAGE, CURRICULUM_PROFILE, QUESTION_COUNT, QUESTION_TYPE, ANSWER_TYPE, ANSWER_FORMAT, SHOW_QUESTION_NUMBER, SHOW_ANSWER_KEY, THEME, DISTRIBUTION_MODE`

Defaults:

- `DIFFICULTY=AUTO`
- `SHOW_QUESTION_NUMBER=YES` unless user/workflow prohibits it
- `SHOW_ANSWER_KEY=NO`
- `DISTRIBUTION_MODE=BALANCED`

## 6. Page/render parameters

`PAGE_SIZE, ORIENTATION, PAGE_COUNT, TARGET_PAGE_COUNT, ONE_PAGE_PREFERRED, ONE_PAGE_LOCK, AUTO_PAGINATION, DENSITY_MODE, COLOR_MODE, SAFE_MARGIN, PRINT_MODE, RENDER_PATH, RENDER_OBJECTIVE, VISUAL_QA_REQUIRED, OUTPUT_MODE, PRIMARY_DELIVERABLE`

Final `RENDER_PATH` must resolve to exactly one:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

`AUTO` is input-only.

Default resolution:

- Thai/text/table/numeric-heavy → DOCUMENT_FIRST
- exact learner-read geometry + theme/context art → HYBRID
- geometry-dominant/minimal art → DETERMINISTIC_VECTOR
- IMAGE_ONLY only when nondeterminism cannot threaten required correctness or explicitly requested

## 7. Render safety parameters

Defaults when applicable:

`CONTENT_LOCK=ON`
`THAI_TEXT_LOCK=ON`
`NUMERIC_VALUE_LOCK=ON`
`QUESTION_COUNT_LOCK=ON`
`STUDENT_VISIBLE_ANSWER_LEAK_GUARD=ON`
`STUDENT_VISIBLE_TARGET_TEXT_LEAK_GUARD=ON`
`CANONICAL_LABEL_PRESERVATION=ON`
`GEOMETRY_LOCK=ON` when visual geometry is academic
`TEMPLATE_LOCK=ON` for repeated instruments/graphs
`PER_ITEM_RENDER_STATE_REQUIRED=YES` for learner-read visuals
`TARGET_ALIGNMENT_REQUIRED=YES` for exact-reading instruments

## 8. One-page-first policy

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`

Optimization order:

1. preserve academic correctness and exact question count
2. preserve domain minimum diagram/instrument size
3. preserve readable Thai/numerals and writable answer space
4. choose efficient valid layout
5. remove/simplify decoration
6. shorten nonessential instruction
7. reduce nonessential padding
8. reduce decorative context
9. paginate only when unlocked

Explicit `A4 หน้าเดียว` / `1 หน้าเท่านั้น` → `ONE_PAGE_LOCK=ON`, `PAGE_COUNT=1`.

If safe fit is impossible under lock:

`PROMPT_ONE_PAGE_FEASIBILITY_QA=FAIL`
`PROMPT_RELEASE=BLOCKED`

Never reduce question count, crop, merge ticks, or shrink below minimum to force one page.

## 9. Time/clock parameters

`TIME_SUBDOMAIN=CLOCK_READING|TIME_CALCULATION`
`TIME_FORMAT=12_HOUR|24_HOUR`
`MINUTE_GRANULARITY=60|30|15|5|1`
`TIME_TASK_TYPE=READ_CLOCK|START_PLUS_DURATION|START_END_TO_DURATION|END_MINUS_DURATION|COMPARE_TIME|SCHEDULE`
`CLOCK_READING_MODE=SINGLE|DAY_NIGHT_PAIR`
`DAY_NIGHT_MODE=OFF|ON`
`TIME_CROSS_MIDNIGHT_ALLOWED=NO|YES`
`START_TIME_RANGE`
`MIN_DURATION`
`MAX_DURATION`
`TARGET_TIMES`
`ANSWER_TIME_FORMAT`

Default Thai elapsed-time mode: 24-hour, no midnight crossing unless requested.

## 10. Length/ruler/distance parameters

`LENGTH_SUBDOMAIN=RULER_READING|LENGTH_CALCULATION|DISTANCE_CALCULATION|UNIT_CONVERSION`
`UNIT_SET=MM|CM|M|KM|CM_MM|M_CM|KM_M|MIXED_METRIC`
`RULER_SCALE_MIN`
`RULER_SCALE_MAX`
`MAJOR_DIVISION`
`MINOR_DIVISION`
`START_POSITION_MODE=ZERO_ONLY|NONZERO_ALLOWED|MIXED`
`TARGET_LENGTHS`
`LENGTH_TASK_TYPE=READ|ADD|SUBTRACT|COMPARE|DIFFERENCE|CONVERT`
`DISTANCE_TASK_TYPE=TOTAL|DIFFERENCE|ROUND_TRIP|MULTI_SEGMENT|ROUTE_COMPARE|CONVERT`
`DISTANCE_CONTEXT=DAILY_LIFE|ROUTE|MAP_STYLE|WORD_PROBLEM`

Exact metric relations:

`10 mm=1 cm`
`100 cm=1 m`
`1000 m=1 km`

Normalize to a canonical base unit before arithmetic.

## 11. Weight parameters

`WEIGHT_SUBDOMAIN=DIAL_READING|WEIGHT_CALCULATION|UNIT_CONVERSION`
`UNIT_SET=G|KG|KG_AND_G|KG_AND_TICK`
`DIAL_MAX_KG`
`MAJOR_DIVISION_KG`
`MINOR_DIVISION_KG`
`TARGET_WEIGHTS`
`WEIGHT_TASK_TYPE=READ|ADD|SUBTRACT|COMPARE|DIFFERENCE|CONVERT`

Thai Grade 3 dial default when appropriate:

`DIAL_MAX_KG=5`
`MAJOR_DIVISION_KG=1`
`MINOR_DIVISION_KG=0.1`
`1 ขีด=0.1 kg=100 g`
`ANSWER_FORMAT=........ กิโลกรัม ........ ขีด`

Exact conversion:

`1000 g=1 kg`

## 12. Temperature parameters

`TEMPERATURE_SUBDOMAIN=THERMOMETER_READING|COMPARE|CHANGE`
`MIN_TEMP`
`MAX_TEMP`
`MAJOR_INTERVAL`
`MINOR_INTERVAL`
`UNIT=C|F`
`ORIENTATION=VERTICAL|HORIZONTAL`
`TARGET_TEMPERATURES`

Discrete reading targets must be exactly representable by the minor interval unless interpolation is explicitly taught.

## 13. Capacity/volume parameters

`CAPACITY_SUBDOMAIN=READ_SCALE|MENISCUS|CAPACITY_CALCULATION|UNIT_CONVERSION|SOLID_VOLUME`
`UNIT=ML|L|MIXED|CM3|M3`
`SCALE_MIN`
`SCALE_MAX`
`MAJOR_DIVISION`
`MINOR_DIVISION`
`CONTAINER_TYPE`
`MENISCUS_MODE=SIMPLE_FLAT|SCIENTIFIC`
`MENISCUS_READ_POINT=BOTTOM|TOP`
`TARGET_LEVELS`
`CAPACITY_TASK_TYPE=READ|ADD|SUBTRACT|COMPARE|DIFFERENCE|CONVERT`
`SOLID_VOLUME_TASK=RECTANGULAR_PRISM|SIMPLE_COMPOSITE_RECTANGULAR_PRISMS`

Exact relations:

`1000 mL=1 L`
`1 cm³=1 mL` when explicitly taught
`1000 cm³=1 L` when explicitly taught

Rectangular-prism volume:

`V=length×width×height`

All dimensions must be expressed in compatible units before multiplication.

## 14. Grade progression AUTO

Use conservative defaults from `domains/MEASUREMENT_COVERAGE_P1_P6.md`.

General pattern:

- P1: direct comparison/basic whole-unit reading; minimal conversion
- P2: simple reading and one-step arithmetic with familiar units
- P3: finer graduations, duration, ruler mm/cm, kg/ขีด, mL/L, basic distance
- P4: multi-unit length/time, more nonzero-start ruler reading, route arithmetic, basic unit conversion
- P5: mixed-unit/decimal conversions where appropriate, capacity/volume applications
- P6: multi-step measurement reasoning, composite distance/time/volume problems

Do not introduce a higher-grade complexity merely because the renderer can display it.

## 15. Default resolution algorithm

1. valid explicit user value wins
2. else owning worker/domain default
3. else grade/curriculum-profile default
4. else core default/AUTO
5. record resolved value
6. route workers
7. resolve one render path
8. run one-page feasibility
9. if no safe rule exists and correctness changes, ask one concise clarification

## 16. Teacher-friendly interaction

Never ask ordinary teachers for technical fields such as `TICK_POSITION_COUNT` when a safe domain default exists. Translate natural language into parameters internally.

Advanced users may provide structured parameters directly; structured input never bypasses worker/domain validation.