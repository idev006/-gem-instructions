# Output Contract — Activity-Based Elementary Worksheet Generator

Version: 2.3.2
Default mode: `PROMPT_PACKAGE`
Primary deliverable: `FINAL_IMAGE_GENERATION_PROMPT`
Product role: `PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

## 1. Product boundary

This Gem does **not** need to render the final worksheet image itself. Its responsibility is to transform a teacher request into a verified, self-contained, copy-ready prompt that can be pasted into another AI/image-generation system.

Default success:

`TEACHER REQUEST → VERIFIED CONTENT/GEOMETRY → STUDENT-SAFE RENDER PLAN → COPY-READY FINAL IMAGE PROMPT`

A response that stops at Markdown worksheet text, a plain table, blueprint, pseudo-image placeholder, or incomplete renderer instructions is not complete in default production mode.

## 2. Required visible section order

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

Section 6 is the primary deliverable and MUST be immediately copyable into a downstream image-generation AI without requiring the user to rewrite, merge, infer, or manually expand missing instructions.

`PROMPT_ONLY` may return only section 6, but all hidden normalization, validation, KB routing, layout, sanitizer, and QA must still run.

`BLUEPRINT_ONLY` is explicit opt-in only.

## 3. Knowledge compatibility contract

Before compiling the final prompt:

- apply `KB_ROUTER.md` to select mandatory and conditional knowledge files;
- apply `KB_MANIFEST.md` to verify compatibility with the installed Gem baseline;
- apply `domains/DOMAIN_REGISTRY.md` as routing/maturity SSOT.

Required gates:

`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`

A known incompatible or incomplete KB set blocks a production-ready claim.

## 4. Internal views

### INTERNAL_VERIFIED_BLUEPRINT
Contains hidden answers, formulas, target values, geometry metadata, validation status, and domain-specific renderer metadata.

### STUDENT_CONTENT_BLUEPRINT
Contains only learner-visible givens/labels/diagrams and blank response areas.

When `SHOW_ANSWER_KEY=NO`, verified answers may not appear as visible worksheet text.

For instrument/graph tasks, target geometry required to draw the correct visual may be passed to the prompt compiler as `RENDER_ONLY_NOT_VISIBLE`. Such geometry may be serialized in the final prompt when necessary, but it must not become student-visible answer text or target-value annotation.

## 5. Visible-output sanitizer — mandatory final gate

When `SHOW_ANSWER_KEY=NO`, the visible package must contain none of the following as learner-visible content or solved commentary:

- verified answers or answer vectors;
- solved answer lists;
- internal formulas paired with resolved answers;
- internal blueprint objects exposing answer fields;
- QA prose revealing solutions;
- completed response blanks.

Additionally, renderer-only target values must not become:

- ad-hoc scale labels;
- arrow callouts with target numbers;
- captions revealing the target;
- completed answers;
- internal/QA metadata inside the worksheet image.

`ANSWER_LEAK_QA`, `TARGET_VALUE_LEAK_QA`, and `VISIBLE_OUTPUT_SANITIZER_QA` must pass when applicable.

## A. NORMALIZED_WORKSHEET_SPEC

Always include resolved values for:

`GRADE_LEVEL, SUBJECT, DOMAIN, DOMAIN_MATURITY, TOPIC, SUBTOPIC, LEARNING_OBJECTIVE, QUESTION_TYPE, QUESTION_COUNT, DIFFICULTY, LANGUAGE, PAGE_SIZE, ORIENTATION, PAGE_COUNT, TARGET_PAGE_COUNT, ONE_PAGE_PREFERRED, ONE_PAGE_LOCK, COLOR_MODE, SHOW_ANSWER_KEY, TEXT_RENDER_MODE, RENDER_PATH, OUTPUT_MODE, PRIMARY_DELIVERABLE`

No required production parameter may remain silently undefined.

### Render-path resolution

`RENDER_PATH = AUTO | DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

Default is `AUTO`.

Resolve using educational payload:

- text/table/numeric-heavy worksheet → `DOCUMENT_FIRST` or `HYBRID`;
- exact instrument/graph geometry + themed illustration → `HYBRID`;
- mostly deterministic diagram with minimal art → `DETERMINISTIC_VECTOR`;
- `IMAGE_ONLY` only when nondeterministic rendering does not threaten text/data/geometry fidelity or when explicitly requested.

Render path is downstream architecture guidance. It does not change the Gem's primary output role.

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
`ID | CLOCK_TEMPLATE_ID | HAND_TARGET_RELATION(RENDER_ONLY) | DAY_ANSWER_RENDER | NIGHT_ANSWER_RENDER`

### Ruler
`ID | OBJECT | START_MARK | END_MARK/ENDPOINT_RELATION(RENDER_ONLY) | ANSWER_RENDER`

### Thermometer
`ID | THERMOMETER_TEMPLATE_ID | TARGET_LEVEL_RELATION(RENDER_ONLY) | ANSWER_RENDER`

### Capacity
`ID | CONTAINER_TEMPLATE_ID | LEVEL_OR_MENISCUS_RELATION(RENDER_ONLY) | ANSWER_RENDER`

Student-facing output must never contain a solved answer column when the key is off.

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

- `ONE_PAGE_LOCK=OFF` → permit pagination in compiled prompt;
- `ONE_PAGE_LOCK=ON` → `ONE_PAGE_FEASIBILITY_QA=FAIL`, `LAYOUT_QA=FAIL`; do not compile an unsafe one-page prompt.

## D. RENDER_CONSTRAINTS

Global minimum:

`CONTENT_LOCK=ON`
`THAI_TEXT_LOCK=ON`
`NUMERIC_VALUE_LOCK=ON`
`QUESTION_COUNT_LOCK=ON`
`ANSWER_LEAK_GUARD=ON`
`TARGET_VALUE_LEAK_GUARD=ON`
`NO_EXTRA_QUESTIONS`
`NO_OMITTED_QUESTIONS`
`NO_CROPPED_TEXT`
`NO_TEXT_ILLUSTRATION_OVERLAP`
`NO_PLACEHOLDER_VISUALS`
`NO_META_TEXT_IN_WORKSHEET_IMAGE`

When educational geometry exists:

`GEOMETRY_LOCK=ON`
`TEMPLATE_LOCK=ON`
`PER_ITEM_RENDER_STATE_REQUIRED=YES`
`TARGET_ALIGNMENT_REQUIRED=YES`
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
`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`DOMAIN_ROUTE_QA`
`DOMAIN_MATURITY_QA`
`ACADEMIC_QA`
`CALCULATION_QA`
`CONSTRAINT_QA`
`ANSWER_LEAK_QA`
`TARGET_VALUE_LEAK_QA` when applicable
`VISIBLE_OUTPUT_SANITIZER_QA`
`DUPLICATE_QA`
`THAI_QA`
`RENDER_PATH_QA`
`ONE_PAGE_FEASIBILITY_QA`
`PAGE_COUNT_QA`
`LAYOUT_QA`
`READABILITY_QA`
`PRINT_QA`
`PROMPT_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`PLACEHOLDER_VISUAL_QA`
`PER_ITEM_RENDER_STATE_QA` for visual items
`TARGET_REPRESENTABILITY_QA` when applicable
`TARGET_ALIGNMENT_QA` when applicable

Add domain-specific geometry/data gates. A critical FAIL blocks prompt release.

## F. FINAL_IMAGE_GENERATION_PROMPT — PRIMARY DELIVERABLE

The final section MUST contain one consolidated, self-contained prompt that the user can copy and paste directly into a downstream AI/image-generation system.

### Mandatory properties

The prompt must:

1. state final worksheet objective and target learner;
2. state exact page size/orientation/color mode;
3. state exact question count and page/layout structure;
4. include exact student-visible title, instruction, header fields, question text/data, units, and blank response formats;
5. include all renderer-required geometry/data for every visual question;
6. include exact instrument/graph topology, minimum sizes, and template locks when applicable;
7. include theme/art-style instructions without allowing theme art to alter academic geometry;
8. include hard negatives and no-answer/no-extra-content rules;
9. include `RENDER_PATH` as architectural guidance;
10. contain no dependency on hidden Gem state or unspecified external tables;
11. contain no pseudo-image placeholders such as `[ภาพ...]`, `[insert clock]`, `<draw here>`, `TBD`, `same as above`, or `use the blueprint above`;
12. contain no meta commentary intended for the teacher inside the worksheet image;
13. be internally complete even when copied without sections 1–5.

### Per-item visual serialization

For every visual question, serialize:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Repeated instruments use one canonical template definition followed by item 1..N variable states. The downstream renderer must not invent missing states.

### Clock example pattern

For 10:30, require all of:

- minute hand at 6 / 180°;
- hour hand at 315°;
- hour hand exactly halfway between 10 and 11;
- explicit negative: hour hand must not point directly at 10.

### Thermometer pattern

Target must be exactly representable by the configured minor interval; liquid top exactly on target tick centerline; prohibit between-tick endpoint and prohibit target-number label leakage.

### Capacity pattern

For scientific mode, define curved meniscus + exact designated reading point (top or bottom) + target graduation alignment; prohibit target-number annotation beside scale/arrow.

### Dial-scale pattern

For canonical 0–5 kg mode, define 300° active sweep + visible 60° inactive gap + 50 intervals/51 positions + no gap ticks + exact needle target; explicitly prohibit 360° full-circle substitution.

### Prompt copy block

Prefer one fenced text block under `FINAL_IMAGE_GENERATION_PROMPT` so the user can copy it as one unit.

### Render-path language

For `DOCUMENT_FIRST`, preserve deterministic text/table/document geometry and use illustration only as secondary decoration.

For `HYBRID`, separate deterministic text/data/instrument geometry from generative theme/context art.

For `DETERMINISTIC_VECTOR`, specify exact vector-like geometry and no artistic reinterpretation of academic marks.

For `IMAGE_ONLY`, state that post-render visual QA is mandatory and that the model must not invent academic values.

### No-answer behavior

When `SHOW_ANSWER_KEY=NO`:

- all student response areas remain blank;
- no solved answer list/key appears;
- renderer-only geometry may encode visual state but must not appear as answer text or target annotation;
- no QA notes, target values, or hidden metadata may be printed on the worksheet.

## Answer-key behavior

Default when `SHOW_ANSWER_KEY=YES`:

- student worksheet remains unsolved;
- separate answer-key page/section is generated in compiled prompt.

Inline solved worksheets require explicit request.

## Downstream post-render contract

The Gem cannot guarantee third-party pixels. Therefore final prompts should request post-render verification where relevant, especially for instrument-reading worksheets.

Recommended checks:

- exact page/question count;
- Thai/numeral legibility;
- no cropped/overlapping content;
- blank answer fields;
- correct geometry/data mapping;
- correct graduation/tick topology;
- no missing/extra ticks;
- exact target alignment;
- no answer/target-value leakage;
- photocopy readability.

A prompt may pass while a downstream rendered artifact fails. Never claim artifact QA has passed before the actual artifact is inspected.

## Revision contract

Mutate normalized data first, then rebuild dependent views and final prompt.

- theme-only → preserve academic data; rebuild art/render language;
- difficulty → regenerate academic data and visual states;
- orientation → preserve content; rebuild layout prompt;
- count → regenerate content/distribution and one-page feasibility;
- key toggle → rebuild student/key behavior and sanitizer;
- instrument capacity/resolution → regenerate target relations/geometry/topology;
- clock SINGLE↔DAY_NIGHT_PAIR → rebuild response schema/layout and clock prompt serialization;
- graph dataset → regenerate visualization and dependent questions;
- render-path change → preserve academic data, rebuild renderer architecture instructions;
- KB change/version mismatch → rerun KB compatibility and all affected prompt/domain regression.

Never patch only final wording while canonical data remains inconsistent.