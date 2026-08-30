# Output Contract — Activity-Based Elementary Worksheet Generator

Version: 2.1.0
Default mode: `PROMPT_PACKAGE`

## Required visible section order

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

`PROMPT_ONLY` and `BLUEPRINT_ONLY` may hide sections, but all hidden validation still runs.

## Internal views

### INTERNAL_VERIFIED_BLUEPRINT

Contains hidden answers, formulas, target values, geometry metadata, validation status, and domain-specific render metadata.

### STUDENT_CONTENT_BLUEPRINT

Contains only student-visible givens/labels/diagrams and blank response areas.

When `SHOW_ANSWER_KEY=NO`, verified answers may not appear as visible worksheet content.

For instrument/graph tasks, hidden target metadata may be passed to the render compiler only to construct the correct diagram. It must be clearly marked `RENDER_ONLY_NOT_VISIBLE`.

## Visible-output sanitizer — mandatory final gate

Before returning any visible package to the user, scan the complete assembled output, not only the student blueprint.

When `SHOW_ANSWER_KEY=NO`, the visible package must contain none of the following for the active worksheet:

- verified answers
- answer vectors/lists
- solved values in parenthetical notes
- internal formulas paired with resolved active answers
- internal blueprint objects containing answer fields
- QA prose that reveals answers while claiming they are hidden

Allowed exceptions:

- generic examples that are clearly unrelated to the active generated questions
- non-visible render metadata that never appears in user-visible output

If the sanitizer detects active answers, redact/rebuild before release. `ANSWER_LEAK_QA` cannot PASS merely because the final image prompt is blank; the **entire visible response** must be clean.

## A. NORMALIZED_WORKSHEET_SPEC

Always include resolved values for:

`GRADE_LEVEL, SUBJECT, DOMAIN, DOMAIN_MATURITY, TOPIC, SUBTOPIC, LEARNING_OBJECTIVE, QUESTION_TYPE, QUESTION_COUNT, DIFFICULTY, LANGUAGE, PAGE_SIZE, ORIENTATION, PAGE_COUNT, COLOR_MODE, SHOW_ANSWER_KEY, TEXT_RENDER_MODE`

Also include active domain parameters that affect correctness.

Examples:

- scale: max capacity, major/minor division, answer format
- clock: minute granularity, number/mark mode, clock-reading mode, answer time format
- ruler: major/minor division, unit mode, zero-start mode
- thermometer: min/max/interval/unit
- capacity: max/minor division/unit
- money: currency/question type/price constraints
- calendar: month/year/week start
- graph: dataset/axis interval/key

No optional parameter may remain silently undefined.

## B. STUDENT_CONTENT_BLUEPRINT

Exactly one object/row per question. Schema is domain-specific.

Examples:

### Elapsed time
`ID | ACTIVITY | START_TIME | END_TIME | ANSWER_RENDER | UNIT_RENDER`

### Dial scale
`ID | OBJECT | DIAL_TEMPLATE_ID | NEEDLE_TARGET_RELATION(RENDER_ONLY) | ANSWER_RENDER`

### Clock — single reading
`ID | CLOCK_TEMPLATE_ID | HAND_TARGET_RELATION(RENDER_ONLY) | ANSWER_RENDER`

### Clock — day/night paired reading
One question = one clock + two blank response fields.

`ID | CLOCK_TEMPLATE_ID | HAND_TARGET_RELATION(RENDER_ONLY) | DAY_ANSWER_RENDER | NIGHT_ANSWER_RENDER`

The day/night verified values remain internal. Do not duplicate the clock face merely to produce the second answer field.

### Ruler
`ID | OBJECT | START_MARK | END_MARK/ENDPOINT_RELATION(RENDER_ONLY) | ANSWER_RENDER`

### Graph/table
`ID | DATASET_REF | QUESTION_TEXT | ANSWER_RENDER`

Student-facing output must never contain an answer column when the key is off.

## C. LAYOUT_BLUEPRINT

Must specify:

- page size/orientation/page count
- safe margins
- header/title/instruction regions
- question region pattern
- per-question reserved dimensions
- answer-space dimensions
- illustration/decorative zones
- domain-specific minimum instrument/graph size
- pagination trigger

For paired-response questions, reserve all required response lines inside each question region before decoration is placed.

If domain minimum readability cannot fit, layout must paginate rather than shrink/distort.

## D. RENDER_CONSTRAINTS

Global minimum:

`CONTENT_LOCK=ON`
`THAI_TEXT_LOCK=ON`
`NUMERIC_VALUE_LOCK=ON`
`QUESTION_COUNT_LOCK=ON`
`ANSWER_LEAK_GUARD=ON`
`NO_EXTRA_QUESTIONS`
`NO_OMITTED_QUESTIONS`
`NO_CROPPED_TEXT`
`NO_TEXT_ILLUSTRATION_OVERLAP`

When educational geometry exists:

`GEOMETRY_LOCK=ON`
`TEMPLATE_LOCK=ON`
`NO_PERSPECTIVE_DISTORTION` when perspective changes the reading
`VISUAL_QA_REQUIRED=YES` unless geometry is deterministically overlaid and verified

For clock day/night pairing:

`ONE_CLOCK_PER_QUESTION=YES`
`TWO_RESPONSE_FIELDS_PER_QUESTION=YES`
`DAY_NIGHT_MAPPING_DETERMINISTIC=YES`

## E. QA_REPORT

Global gates:

`INTENT_QA`
`PARAMETER_QA`
`DOMAIN_ROUTE_QA`
`ACADEMIC_QA`
`CALCULATION_QA`
`CONSTRAINT_QA`
`ANSWER_LEAK_QA`
`VISIBLE_OUTPUT_SANITIZER_QA`
`DUPLICATE_QA`
`THAI_QA`
`LAYOUT_QA`
`READABILITY_QA`
`PRINT_QA`
`PROMPT_QA`

Also include domain-specific gates and domain maturity.

Example:

```text
DOMAIN = MEASUREMENT_WEIGHT
DOMAIN_MATURITY = PRODUCTION_CANDIDATE
CENTER_PIVOT_QA = PASS
TICK_SPACING_QA = PASS
NEEDLE_TARGET_QA = PASS
VISUAL_QA_REQUIRED = YES
```

A critical FAIL blocks release.

## F. FINAL_IMAGE_GENERATION_PROMPT

Must be self-contained and include:

- page spec
- target learner/subject/topic/objective
- exact question count
- exact student-facing content
- domain-specific educational geometry/data constraints
- layout and minimum-size rules
- illustration rules
- text/numeric locks
- blank-answer rule
- hard negatives

When `SHOW_ANSWER_KEY=NO`, answers must not be visible anywhere.

For clock day/night paired mode, the final prompt must explicitly state that each question has one analog clock face and two blank answer fields labelled day/night; do not create two clocks unless explicitly requested.

## Answer-key behavior

Default when `SHOW_ANSWER_KEY=YES`:

- student worksheet remains unsolved
- separate answer-key page/section is generated

Inline solved worksheets require explicit user request.

## Post-render result contract

If an actual image/PDF is rendered, append a `POST_RENDER_QA` result when possible:

- count
- text readability
- value/diagram fidelity
- geometry accuracy
- answer leakage
- cropping/overlap
- photocopy usability

For clock day/night paired mode also verify:

- exactly one instructional clock per question
- exactly two response fields per question
- day/night labels are clearly associated with the same clock

A prompt may pass while a rendered image fails. Classroom release requires the rendered artifact to pass applicable post-render checks.

## Revision contract

Mutate normalized data first, then rebuild affected views.

- theme-only → preserve academic data
- difficulty → regenerate academic data
- orientation → preserve data, rerun layout
- count → regenerate content/distribution/pagination
- key toggle → rebuild student/key views
- instrument capacity/resolution → regenerate all target relations and geometry
- clock reading mode SINGLE↔DAY_NIGHT_PAIR → preserve/validate clock targets as appropriate, rebuild answer schema and layout, rerun clock/answer-leak QA
- graph dataset → regenerate visualization and dependent questions

Never patch only final prompt prose while canonical data remains inconsistent.
