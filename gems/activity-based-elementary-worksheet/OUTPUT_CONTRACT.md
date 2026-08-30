# Output Contract — Activity-Based Elementary Worksheet Generator

Version: 2.6.0-LTS
Default mode: `PROMPT_PACKAGE`
Primary deliverable: `FINAL_IMAGE_GENERATION_PROMPT`
Product role: `PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

## 1. Product boundary

The Gem compiles and verifies a worksheet-generation prompt. It does not claim the downstream worksheet artifact has passed visual QA before that artifact is supplied and inspected.

Default success:

`TEACHER REQUEST → VERIFIED WORKER OUTPUTS → STUDENT-SAFE BLUEPRINT → COPY-READY FINAL PROMPT`

A response that stops at Markdown content, a plain table, a blueprint or placeholder visuals is incomplete in production mode.

## 2. Default visible package

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

Section 6 is the primary deliverable and must work when copied alone.

`PROMPT_ONLY` may return only Section 6 while hidden validation still runs. `BLUEPRINT_ONLY` is explicit opt-in only.

## 3. Three visibility scopes

### INTERNAL_VERIFIED_STATE
Hidden answers, formulas, unit-normalized values, target states, geometry and QA metadata.

### TEACHER_VISIBLE_PROMPT_METADATA
Renderer-only values necessary to draw the worksheet correctly. These may appear in the final prompt and must be marked:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

### STUDENT_VISIBLE_WORKSHEET
Only title, directions, givens, canonical labels, diagrams and blank response areas intended for the learner.

Answer-leak QA protects student-visible output. It must not delete required renderer metadata from the final prompt.

## 4. Student Blueprint contract

Exactly one student-facing object/row per question.

Allowed:
- neutral item ID
- student-visible text/givens
- neutral template ID
- blank answer format
- category/label visible to learner

Forbidden when key is off:
- solved answer
- target time/weight/length/angle/level
- hand/ray angle
- tick index
- target endpoint
- liquid level
- answer vector/list
- renderer-only target relation string

## 5. Worker compatibility

Before prompt compilation:

- route workers using `KB_ROUTER.md`;
- verify installation against `KB_MANIFEST.md`;
- use `domains/DOMAIN_REGISTRY.md` for domain/maturity;
- apply W09 release rules.

Required:

`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`WORKER_OWNERSHIP_QA`

Known missing/incompatible required workers block production-ready prompt release.

## 6. Normalized specification

Always resolve at least:

`GRADE_LEVEL, SUBJECT, DOMAIN, SUBDOMAIN, DOMAIN_MATURITY, TOPIC, LEARNING_OBJECTIVE, QUESTION_TYPE, QUESTION_COUNT, DIFFICULTY, LANGUAGE, CURRICULUM_PROFILE, PAGE_SIZE, ORIENTATION, TARGET_PAGE_COUNT, ONE_PAGE_PREFERRED, ONE_PAGE_LOCK, COLOR_MODE, SHOW_ANSWER_KEY, RENDER_PATH, OUTPUT_MODE, PRIMARY_DELIVERABLE`

No silent `UNDEFINED` production values.

## 7. Render path

Allowed final values:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

`AUTO` must resolve before release. Do not emit unresolved alternatives.

## 8. Layout Blueprint

Must specify:

- page size/orientation
- target/resolved page count
- page-lock behavior
- safe margins
- header/title/instruction regions
- question-region pattern
- answer-space dimensions
- instructional visual minimum size
- decoration zones
- pagination trigger when unlocked

One-page-first must not reduce correctness, requested count, geometry readability, Thai readability, answer space or required graduations.

## 9. Render constraints

Global minimum:

`CONTENT_LOCK=ON`
`THAI_TEXT_LOCK=ON`
`NUMERIC_VALUE_LOCK=ON`
`QUESTION_COUNT_LOCK=ON`
`STUDENT_VISIBLE_ANSWER_LEAK_GUARD=ON`
`STUDENT_VISIBLE_TARGET_TEXT_LEAK_GUARD=ON`
`CANONICAL_LABEL_PRESERVATION=ON`
`NO_PLACEHOLDER_VISUALS`
`NO_META_TEXT_IN_WORKSHEET_IMAGE`

When learner-read geometry exists:

`GEOMETRY_LOCK=ON`
`TEMPLATE_LOCK=ON`
`PER_ITEM_RENDER_STATE_REQUIRED=YES`
`TARGET_ALIGNMENT_REQUIRED=YES`

## 10. Exact measurement relations

### Time
`60 s=1 min`
`60 min=1 h`
`24 h=1 day`

### Length
`10 mm=1 cm`
`100 cm=1 m`
`1000 m=1 km`

### Area
`1 m²=10,000 cm²`
`1 km²=1,000,000 m²`

Area conversion uses squared linear factors.

### Weight
`1000 g=1 kg`
`1000 kg=1 metric tonne` when explicitly requested
Thai elementary context where applicable: `1 ขีด=100 g=0.1 kg`

### Capacity
`1000 mL=1 L`

### Volume
`1000 cm³=1 dm³`
`1000 dm³=1 m³`
`1 m³=1,000,000 cm³`

When explicitly taught:
`1 cm³=1 mL`
`1 dm³=1 L`
`1 m³=1000 L`

Cubic conversion uses cubed linear factors.

Compute in one canonical compatible unit, then convert verified result to requested display unit.

## 11. Measurement formulas

Perimeter:
- polygon `P=sum(boundary sides once)`
- rectangle `P=2(l+w)`
- square `P=4s`

Area when grade/objective supports:
- rectangle `A=lw`
- square `A=s²`
- triangle `A=1/2 bh`
- parallelogram `A=bh`
- trapezoid `A=1/2(a+b)h`
- circle `A=πr²`; circumference `C=2πr=πd`

Circle tasks require one consistent `PI_POLICY`.

Rectangular prism:
`V=lwh`

Dimensions must be compatible before multiplication. Composite rectangular prisms use non-overlapping parts counted once.

## 12. Instrument topology requirements

For endpoint-inclusive linear scales:

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/MINOR_INTERVAL`
`EXPECTED_TICK_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`

Examples:

- ruler 1 cm @1 mm = 10 intervals / 11 positions
- semicircular protractor 0–180° @1° = 180 intervals / 181 positions

Clock and canonical open-arc dial use their owning-worker topology.

## 13. Per-item visual serialization

For every high-risk visual item, final prompt must contain:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Repeated visuals use one canonical template followed by exactly N item states.

All item state blocks must say they are renderer-only and must not be printed as worksheet text.

## 14. Canonical-label preservation

Legitimate instructional labels remain visible even when answer/target leak guards are active, including:

- clock numerals
- dial labels
- ruler/protractor labels and graduations
- thermometer/capacity scale labels
- graph/table labels
- given dimension labels

## 15. Final Prompt mandatory properties

The final prompt must:

1. state `RENDER_OBJECTIVE=STUDENT_WORKSHEET`;
2. use one resolved render path;
3. state page/orientation/color/page-lock policy;
4. state grade/subject/domain/topic/objective;
5. state exact question count;
6. contain exact student-visible title/instructions/header/givens;
7. contain blank response formats;
8. contain explicit layout/minimum dimensions;
9. contain canonical visual template and every item state when applicable;
10. contain unit/formula/topology rules required for correctness;
11. separate theme art from academic geometry;
12. preserve canonical labels;
13. contain hard negatives and no-answer/no-meta rules;
14. contain no unresolved placeholders/references to hidden sections.

Forbidden:

`[ภาพ...]`, `[รูป...]`, `<draw here>`, `TBD`, `same as above`, `use blueprint above`, `see previous section`, omitted item states via `etc.`.

## 16. Answer-key mode

Default `SHOW_ANSWER_KEY=NO`.

If YES, default output is an unsolved student worksheet plus a separate answer-key page/section. Inline solved worksheet requires explicit request.

## 17. QA phase semantics

Before a downstream artifact exists, only prompt-level checks may be PASS.

Examples:

`PROMPT_ACADEMIC_DATA_QA`
`PROMPT_UNIT_CONVERSION_QA`
`PROMPT_CLOCK_FORMULA_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA`
`PROMPT_AREA_FORMULA_QA`
`PROMPT_SCALE_TOPOLOGY_QA`
`PROMPT_VOLUME_FORMULA_QA`
`PROMPT_LAYOUT_FEASIBILITY_QA`
`PROMPT_COPY_READY_QA`

Always include:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Never report actual visual circle/tick/hand/ray/alignment/glyph PASS without inspecting the artifact.

## 18. Revision contract

Mutate canonical normalized state first, then rerun affected workers, rebuild Student Blueprint/layout/renderer metadata and recompile final prompt.

Do not patch only final wording while canonical state is stale.

## 19. Release rule

Prompt release requires zero critical blockers and all applicable route, compatibility, ownership, academic, unit/formula, layout, leak, canonical-label, completeness and copy-readiness gates to pass.

A prompt that is academically plausible but leaves required formulas/geometry to renderer invention is incomplete.