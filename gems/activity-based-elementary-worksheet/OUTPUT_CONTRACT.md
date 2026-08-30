# Output Contract — Activity-Based Elementary Worksheet Generator

Version: 2.2.1
Default mode: `PROMPT_PACKAGE`

## Required visible section order

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

The section name `FINAL_IMAGE_GENERATION_PROMPT` is retained for backward compatibility. Its content MUST follow the resolved `RENDER_PATH`; for `DOCUMENT_FIRST` or `HYBRID`, it is a final render instruction package and must not falsely imply that a generative image model is the preferred renderer.

`PROMPT_ONLY` and `BLUEPRINT_ONLY` may hide sections, but all hidden validation still runs.

## Internal views

### INTERNAL_VERIFIED_BLUEPRINT
Contains hidden answers, formulas, target values, geometry metadata, validation status, and domain-specific render metadata.

### STUDENT_CONTENT_BLUEPRINT
Contains only student-visible givens/labels/diagrams and blank response areas.

When `SHOW_ANSWER_KEY=NO`, verified answers may not appear as visible worksheet content.

For instrument/graph tasks, hidden target metadata may be passed to the render compiler only to construct the correct diagram and must be marked `RENDER_ONLY_NOT_VISIBLE`.

## Visible-output sanitizer — mandatory final gate

Before returning any visible package, scan the complete assembled response, not only the student blueprint.

When `SHOW_ANSWER_KEY=NO`, the visible package must contain none of the following for the active worksheet:

- verified answers;
- answer vectors/lists;
- solved values in notes/parentheticals;
- internal formulas paired with resolved active answers;
- internal blueprint objects containing answer fields;
- QA prose that reveals answers while claiming they are hidden.

If found, redact/rebuild before release. `ANSWER_LEAK_QA` cannot PASS merely because blanks remain in the final render prompt.

## A. NORMALIZED_WORKSHEET_SPEC

Always include resolved values for:

`GRADE_LEVEL, SUBJECT, DOMAIN, DOMAIN_MATURITY, TOPIC, SUBTOPIC, LEARNING_OBJECTIVE, QUESTION_TYPE, QUESTION_COUNT, DIFFICULTY, LANGUAGE, PAGE_SIZE, ORIENTATION, PAGE_COUNT, TARGET_PAGE_COUNT, ONE_PAGE_PREFERRED, ONE_PAGE_LOCK, COLOR_MODE, SHOW_ANSWER_KEY, TEXT_RENDER_MODE, RENDER_PATH`

No optional parameter may remain silently undefined.

### Render-path resolution

`RENDER_PATH = AUTO | DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

Default is `AUTO`.

Resolve `AUTO` using educational payload:

- text/table/numeric-heavy worksheet → `DOCUMENT_FIRST` or `HYBRID`;
- exact instrument/graph geometry + themed illustration → `HYBRID`;
- mostly deterministic diagram with minimal art → `DETERMINISTIC_VECTOR`;
- `IMAGE_ONLY` only when nondeterministic rendering does not threaten text/data/geometry fidelity or when explicitly requested, and then `VISUAL_QA_REQUIRED=YES`.

Do not recommend generative image-only rendering as the primary path for Thai text-heavy worksheets or exact measurement diagrams.

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
One question = one clock + two blank response fields:

`ID | CLOCK_TEMPLATE_ID | HAND_TARGET_RELATION(RENDER_ONLY) | DAY_ANSWER_RENDER | NIGHT_ANSWER_RENDER`

Verified day/night values remain internal. Do not duplicate the clock merely to produce the second answer field.

### Ruler
`ID | OBJECT | START_MARK | END_MARK/ENDPOINT_RELATION(RENDER_ONLY) | ANSWER_RENDER`

### Graph/table
`ID | DATASET_REF | QUESTION_TEXT | ANSWER_RENDER`

Student-facing output must never contain an answer column when the key is off.

## C. LAYOUT_BLUEPRINT

Must specify:

- page size/orientation;
- `TARGET_PAGE_COUNT`, `ONE_PAGE_PREFERRED`, `ONE_PAGE_LOCK`;
- resolved page count or feasibility result;
- safe margins;
- header/title/instruction regions;
- question-region pattern;
- per-question reserved dimensions;
- answer-space dimensions;
- illustration/decorative zones;
- domain-specific minimum instrument/graph size;
- pagination trigger when unlocked.

### One-page policy

Every worksheet starts with a one-page attempt unless explicitly overridden.

Optimization order:

1. preserve correctness and exact question count;
2. preserve minimum educational diagram/instrument size;
3. preserve readable text and writable answer area;
4. choose a more efficient valid layout;
5. remove/simplify decoration;
6. shorten nonessential instructions;
7. reduce nonessential padding/whitespace;
8. reduce decorative context size.

If still impossible:

- `ONE_PAGE_LOCK=OFF` → paginate;
- `ONE_PAGE_LOCK=ON` → `ONE_PAGE_FEASIBILITY_QA=FAIL`, `LAYOUT_QA=FAIL`, no page 2, no unsafe shrinking.

For paired-response questions, reserve all response lines before decoration.

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

For clock day/night paired mode:

`ONE_CLOCK_PER_QUESTION=YES`
`TWO_RESPONSE_FIELDS_PER_QUESTION=YES`
`DAY_NIGHT_MAPPING_DETERMINISTIC=YES`

For explicit page lock:

`PAGE_COUNT_LOCK=1`
`NO_PAGE_2=YES`

## E. QA_REPORT

Global gates:

`INTENT_QA`
`PARAMETER_QA`
`DOMAIN_ROUTE_QA`
`DOMAIN_MATURITY_QA`
`ACADEMIC_QA`
`CALCULATION_QA`
`CONSTRAINT_QA`
`ANSWER_LEAK_QA`
`VISIBLE_OUTPUT_SANITIZER_QA`
`DUPLICATE_QA`
`THAI_QA`
`GLYPH_COVERAGE_QA` when deterministic text is rendered
`RENDER_PATH_QA`
`ONE_PAGE_FEASIBILITY_QA`
`PAGE_COUNT_QA`
`LAYOUT_QA`
`READABILITY_QA`
`PRINT_QA`
`PROMPT_QA`
`RENDER_OBJECTIVE_QA`

Also include domain-specific gates and the registry-sourced domain maturity.

A critical FAIL blocks release.

## F. FINAL_IMAGE_GENERATION_PROMPT

Must be self-contained and include:

- resolved render path;
- page policy and exact page spec;
- target learner/subject/topic/objective;
- exact question count;
- exact student-facing content;
- domain-specific educational geometry/data constraints;
- layout and minimum-size rules;
- illustration rules;
- text/numeric locks;
- blank-answer rule;
- hard negatives;
- explicit `RENDER_OBJECTIVE`.

For `DOCUMENT_FIRST`, instruct deterministic text/table/document layout and treat illustrations as secondary. For `HYBRID`, separate deterministic text/geometry zones from generative context art. For `IMAGE_ONLY`, state that post-render visual QA is mandatory.

When `SHOW_ANSWER_KEY=NO`, answers must not be visible anywhere.

For clock day/night paired mode, explicitly state one analog clock face + two blank answer fields labelled day/night per question.

## Answer-key behavior

Default when `SHOW_ANSWER_KEY=YES`:

- student worksheet remains unsolved;
- separate answer-key page/section is generated.

Inline solved worksheets require explicit user request.

## Post-render result contract

If an actual image/PDF/document is rendered, append `POST_RENDER_QA` when possible:

- artifact type / render path;
- actual page count;
- question count;
- text readability/glyph coverage;
- value/diagram fidelity;
- geometry accuracy;
- answer leakage;
- cropping/overlap;
- writable response space;
- photocopy usability.

For clock day/night pair also verify exactly one instructional clock and two clearly associated blank response fields per question.

A prompt may pass while a rendered artifact fails. Classroom release requires the artifact to pass applicable post-render checks.

## Revision contract

Mutate normalized data first, then rebuild affected views.

- theme-only → preserve academic data; rerun one-page/layout/render QA;
- difficulty → regenerate academic data; rerun domain/calculation/page QA;
- orientation → preserve content; rerun one-page/layout/print QA;
- count → regenerate content/distribution and rerun one-page feasibility;
- key toggle → rebuild student/key views and rerun answer-leak QA;
- instrument capacity/resolution → regenerate target relations/geometry;
- clock SINGLE↔DAY_NIGHT_PAIR → rebuild answer schema/layout and rerun clock/answer-leak/page QA;
- graph dataset → regenerate visualization and dependent questions;
- render-path change → preserve canonical academic data, rebuild render plan and rerun render/layout/post-render QA.

Never patch only final prompt prose while canonical data remains inconsistent.
