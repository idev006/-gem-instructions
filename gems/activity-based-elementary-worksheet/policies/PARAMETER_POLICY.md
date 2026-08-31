# Parameter Policy — Activity-Based Elementary Worksheet Generator

Version: 2.6.1-LTS
Compatible Gem baseline: 2.6.x
Status: Canonical supporting policy

## 1. Principle

Teachers use natural language. Parameters are internal normalization contracts. Valid explicit teacher requirements override AUTO/default values. No production specification may contain silent `UNDEFINED` values.

Minimum teacher-facing input normally requires:

`GRADE_LEVEL + TOPIC_OR_SKILL + QUESTION_COUNT`

Ask only when a missing value materially changes academic correctness and cannot be derived safely.

## 2. Global defaults

`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`
`SHOW_ANSWER_KEY=NO`
`SHOW_STUDENT_HEADER=YES`
`HEADER_FIELDS=ชื่อ-นามสกุล / ชั้น / เลขที่`
`LANGUAGE=THAI` for Thai requests
`COLOR_MODE=BLACK_AND_WHITE`
`RENDER_PATH=AUTO`
`RENDER_OBJECTIVE=STUDENT_WORKSHEET`
`OUTPUT_MODE=PROMPT_PACKAGE`
`PRIMARY_DELIVERABLE=FINAL_IMAGE_GENERATION_PROMPT`
`CURRICULUM_PROFILE=AUTO`

`ONE_PAGE_LOCK=ON` only when the user explicitly requires one page, such as `1 หน้าเท่านั้น` or `A4 หน้าเดียว`. A preferred target of one page does not activate the lock.

## 3. Render path

AUTO must resolve before release to exactly one:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

Thai/text/table/numeric-heavy → DOCUMENT_FIRST.
Exact learner-read geometry + context art → HYBRID.
Geometry-dominant/minimal art → DETERMINISTIC_VECTOR.
IMAGE_ONLY only when nondeterminism cannot threaten required academic/text fidelity or when explicitly requested.

## 4. Safety/visibility defaults

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

`STUDENT_CONTENT_BLUEPRINT` never contains renderer-only target metadata.

## 5. Time/clock parameters

`TIME_SUBDOMAIN=CLOCK_READING|TIME_CALCULATION|TIME_UNIT_CONVERSION`
`TIME_FORMAT=12_HOUR|24_HOUR`
`TIME_PRECISION=HOUR|MINUTE|SECOND`
`MINUTE_GRANULARITY=60|30|15|5|1`
`SECOND_GRANULARITY=60|30|15|10|5|1` when seconds are active
`TARGET_MINUTE_MODE=ANY_VALID|MULTIPLE_OF_GRANULARITY|EXACT_MINUTE_SET`
`TARGET_MINUTE_SET={...}` when exact minute targets are required
`TIME_TASK_TYPE=READ_CLOCK|START_PLUS_DURATION|START_END_TO_DURATION|END_MINUS_DURATION|COMPARE_TIME|SCHEDULE|CONVERT`
`CLOCK_READING_MODE=AUTO|SINGLE|DAY_NIGHT_PAIR`
`ONE_CLOCK_TWO_ANSWERS=YES|NO`
`DAY_NIGHT_LABELS`
`TIME_CROSS_MIDNIGHT_ALLOWED=NO|YES`
`START_TIME_RANGE`
`MIN_DURATION`
`MAX_DURATION`
`TARGET_TIMES`
`ANSWER_TIME_FORMAT`

Exact relations:

`60 s=1 min`
`60 min=1 h`
`24 h=1 day`

Thai Grade 3 analog-clock `CLOCK_READING_MODE=AUTO` resolves to `DAY_NIGHT_PAIR` unless the teacher explicitly requests a single interpretation.

Paired defaults:

`ONE_CLOCK_TWO_ANSWERS=YES`
`CLOCKS_PER_QUESTION=1`
`ANSWER_FIELDS_PER_QUESTION=2`
`DAY_NIGHT_LABELS=กลางวัน,กลางคืน`
`ANSWER_TIME_FORMAT=24_HOUR`

For strict half-hour intent such as `เน้นเวลาครึ่งชั่วโมง`:

`TARGET_MINUTE_MODE=EXACT_MINUTE_SET`
`TARGET_MINUTE_SET={30}`

Do not model strict half-hour intent only as `MINUTE_GRANULARITY=30`, because that would also admit `:00`.

Seconds are introduced only when explicitly requested or academically warranted. Time-unit conversion alone does not imply a seconds hand.

## 6. Length/ruler/distance/measurement-geometry parameters

`LENGTH_SUBDOMAIN=RULER_READING|LENGTH_CALCULATION|DISTANCE_CALCULATION|UNIT_CONVERSION|ANGLE_PROTRACTOR|PERIMETER|AREA|CIRCLE_MEASUREMENT`
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
`ANGLE_TASK_TYPE=READ|CLASSIFY|COMPARE|CONSTRUCT`
`PROTRACTOR_RANGE=0_180|0_360`
`ANGLE_MINOR_DIVISION_DEG`
`TARGET_ANGLES`
`PROTRACTOR_SCALE_DIRECTION=LEFT_ZERO|RIGHT_ZERO|CLOCKWISE_ZERO|COUNTERCLOCKWISE_ZERO`
`PERIMETER_TASK_TYPE=POLYGON|RECTANGLE|SQUARE|MIXED`
`AREA_TASK_TYPE=RECTANGLE|SQUARE|TRIANGLE|PARALLELOGRAM|TRAPEZOID|CIRCLE|MIXED`
`AREA_UNIT=CM2|M2|KM2|MIXED`
`PI_POLICY=3.14|22/7|SYMBOLIC|CUSTOM` when circle calculation is used

Exact length relations:

`10 mm=1 cm`
`100 cm=1 m`
`1000 m=1 km`

Exact area relations:

`1 m²=10,000 cm²`
`1 km²=1,000,000 m²`

A 0–180° protractor uses semicircular endpoint-inclusive topology. A 0–360° protractor uses full-circle cyclic topology with one origin/center, one selected 0° baseline and no duplicated 360° position. W04/W07 must serialize the selected direction explicitly.

## 7. Weight parameters

`WEIGHT_SUBDOMAIN=DIAL_READING|WEIGHT_CALCULATION|UNIT_CONVERSION`
`UNIT_SET=G|KG|KG_AND_G|KG_AND_TICK|METRIC_TONNE`
`DIAL_MAX_KG`
`MAJOR_DIVISION_KG`
`MINOR_DIVISION_KG`
`TARGET_WEIGHTS`
`WEIGHT_TASK_TYPE=READ|ADD|SUBTRACT|COMPARE|DIFFERENCE|CONVERT`

Thai Grade 3 canonical dial when appropriate:

`DIAL_MAX_KG=5`
`MAJOR_DIVISION_KG=1`
`MINOR_DIVISION_KG=0.1`
`1 ขีด=0.1 kg=100 g`
`ANSWER_FORMAT=........ กิโลกรัม ........ ขีด`

`1000 g=1 kg`
`1000 kg=1 metric tonne` only when explicitly taught/requested.

## 8. Temperature parameters

`TEMPERATURE_SUBDOMAIN=THERMOMETER_READING|COMPARE|CHANGE`
`MIN_TEMP`
`MAX_TEMP`
`MAJOR_INTERVAL`
`MINOR_INTERVAL`
`UNIT=C|F`
`ORIENTATION=VERTICAL|HORIZONTAL`
`TARGET_TEMPERATURES`

Discrete targets must equal `MIN+k*MINOR_INTERVAL` unless interpolation is explicitly taught.

## 9. Capacity/volume parameters

`CAPACITY_SUBDOMAIN=READ_SCALE|MENISCUS|CAPACITY_CALCULATION|UNIT_CONVERSION|SOLID_VOLUME|CUBIC_UNIT_CONVERSION`
`UNIT=ML|L|MIXED|CM3|DM3|M3`
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
`1000 cm³=1 dm³`
`1000 dm³=1 m³`
`1 m³=1,000,000 cm³`

When explicitly taught:

`1 cm³=1 mL`
`1 dm³=1 L`
`1 m³=1000 L`

Rectangular prism: `V=length×width×height` after compatible-unit normalization.

## 10. General academic parameters

`GRADE_LEVEL, SUBJECT, TOPIC, SUBTOPIC, LEARNING_OBJECTIVE, DIFFICULTY, LANGUAGE, CURRICULUM_PROFILE, QUESTION_COUNT, QUESTION_TYPE, ANSWER_TYPE, ANSWER_FORMAT, SHOW_QUESTION_NUMBER, SHOW_ANSWER_KEY, THEME, DISTRIBUTION_MODE`

Defaults:

`DIFFICULTY=AUTO`
`SHOW_ANSWER_KEY=NO`
`DISTRIBUTION_MODE=BALANCED`

## 11. Grade progression AUTO

Use `domains/MEASUREMENT_COVERAGE_P1_P6.md` conservatively:

- P1: basic direct comparison/whole-unit reading
- P2: simple reading and one-step arithmetic
- P3: ruler cm/mm, duration, Thai day/night clock pair by default, kg/ขีด, mL/L, basic distance/perimeter
- P4: mixed units, nonzero ruler start, route arithmetic, protractor, rectangle/square area/perimeter, seconds when taught
- P5: mixed/decimal conversions, broader area, rectangular-prism volume
- P6: multi-step measurement, polygon/circle measurement, composite rectangular-prism volume and cubic conversions

Explicit valid teacher requirements override AUTO.

## 12. Default resolution algorithm

1. valid explicit user value wins;
2. else owning-worker/domain default;
3. else grade/curriculum default;
4. else core AUTO/default;
5. record resolved value and provenance;
6. route workers;
7. resolve exactly one render path;
8. run one-page feasibility;
9. if no safe rule exists and correctness changes, ask one concise clarification.

Every non-default lock or mode must record provenance. In particular, `ONE_PAGE_LOCK=ON` without explicit user provenance is invalid.