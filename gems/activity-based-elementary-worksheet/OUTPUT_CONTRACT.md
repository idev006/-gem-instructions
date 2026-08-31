# Output Contract — Activity-Based Elementary Worksheet Generator

Version: 2.6.2-LTS
Default mode: `PROMPT_PACKAGE`
Primary deliverable: `FINAL_IMAGE_GENERATION_PROMPT`
Product role: `PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

## 1. Product boundary

The Gem compiles and verifies a worksheet-generation prompt. It does not claim the downstream worksheet artifact has passed visual QA before that artifact is supplied and inspected.

Default success:

`TEACHER REQUEST → VERIFIED WORKER OUTPUTS → STUDENT-SAFE BLUEPRINT → COPY-READY FINAL PROMPT`

For learner-read instruments the final prompt must also contain a renderer-side prevention loop. This prevention loop does not replace artifact inspection.

## 2. Default visible package

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

Section 6 is the primary deliverable and must work when copied alone.

## 3. Visibility scopes

### INTERNAL_VERIFIED_STATE
Hidden answers, formulas, normalized values, target states, geometry and QA metadata.

### TEACHER_VISIBLE_PROMPT_METADATA
Renderer-only values needed to draw correctly. Mark:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

### STUDENT_VISIBLE_WORKSHEET
Only title, directions, givens, canonical labels, diagrams and blank response areas.

Answer/target leak guards must not delete legitimate scale labels or renderer metadata needed to construct the worksheet.

## 4. Student Blueprint contract

Exactly one student-facing object/row per question.

Allowed: neutral ID, learner-visible text/givens, neutral template ID, blank answer format, learner-visible category/label.

Forbidden when answer key is off: solved answers, target time/weight/length/angle/speed/temperature/level, hand/needle/ray angles, tick indices, target endpoints, liquid levels, answer vectors, renderer relations/hard negatives.

## 5. Worker/profile compatibility

Before compilation:

- route with `KB_ROUTER.md`;
- verify installation with `KB_MANIFEST.md`;
- use `DOMAIN_REGISTRY.md` for route/maturity;
- apply W09 release rules.

Every runtime worker bundle must contain:

- `SYSTEM_WIDE_QUALITY_PROFILE.md`
- `SCALE_LINE_INTEGRITY_PROFILE.md`
- `INSTRUMENT_REVIEW_REVISE_PROFILE.md`

Missing mandatory runtime knowledge blocks release.

## 6. Normalized specification

Always resolve at least:

`GRADE_LEVEL, SUBJECT, DOMAIN, SUBDOMAIN, DOMAIN_MATURITY, TOPIC, LEARNING_OBJECTIVE, QUESTION_TYPE, QUESTION_COUNT, DIFFICULTY, LANGUAGE, CURRICULUM_PROFILE, PAGE_SIZE, ORIENTATION, TARGET_PAGE_COUNT, ONE_PAGE_PREFERRED, ONE_PAGE_LOCK, COLOR_MODE, SHOW_ANSWER_KEY, RENDER_PATH, OUTPUT_MODE, PRIMARY_DELIVERABLE`

No silent production `UNDEFINED` values.

## 7. Render path and layout

Allowed final render paths:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

AUTO must resolve before release.

Layout Blueprint must specify page/orientation, target/resolved page count, page-lock semantics, safe margins, header/title/instruction regions, question pattern, answer-space size, instructional visual minimum size, decoration zones and pagination trigger when unlocked.

One-page-first must not reduce academic correctness, requested count, scale topology, geometry readability, Thai readability or answer space.

When `ONE_PAGE_LOCK=OFF`, final prompt must preserve safe pagination wording. Do not compile preference into `exactly one page`.

## 8. Global render constraints

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
`SCALE_LINE_SPEC_REQUIRED=YES` when a scale/axis is read
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

## 9. Instrument topology and scale-line contract

Endpoint-inclusive linear scales:

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/MINOR_INTERVAL`
`EXPECTED_TICK_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`
`EXPECTED_INTERIOR_POSITION_COUNT=max(EXPECTED_TICK_POSITION_COUNT-2,0)`

Canonical ruler 1 cm @1 mm:

- 10 intervals
- 11 positions
- 9 interior positions
- physical ruler edge is not an extra graduation

Every learner-read scale must serialize a resolved `SCALE_LINE_SPEC` with topology family, active range, major/minor interval, exact interval/position count, direction, reference baseline/ring/arc, tick anchoring, major/minor hierarchy, endpoint behavior, minimum printed size and minimum tick-center spacing; add inactive-region rule when applicable.

Clock, weight dial, speedometer and other non-linear instruments use their owning-domain topology.

## 10. Per-item visual serialization

For every high-risk visual item, Final Prompt must contain one atomic renderer-only state:

`ITEM_ID`
`SEMANTIC_TARGET`
`EXACT_RENDER_STATE`
`RELATIONAL_VERIFICATION`
`ITEM_SPECIFIC_HARD_NEGATIVE`

Repeated visuals use one canonical template followed by exactly N item states.

Do not use a wide Markdown table when wrapping or column drift can change field meaning. No `same as above`, omitted states or `etc.`.

## 11. Mandatory INSTRUMENT_REVIEW_REVISE_PROTOCOL

When any learner-read instrument exists, Final Prompt must contain `INSTRUMENT_REVIEW_REVISE_PROTOCOL` or exact semantic equivalent and:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Required logical loop:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

The renderer must independently recount/rederive each instructional scale and verify:

- exact topology/range/count;
- baseline/ring/arc anchoring;
- uniform spacing and major/minor hierarchy;
- labels and clearance;
- no missing/extra/merged/floating tick;
- physical edge is not an extra scale mark for ruler/linear instruments;
- pointer/hand/ray/level/endpoint exact target alignment;
- inactive-region integrity;
- decoration isolation;
- canonical-template consistency;
- print readability.

If any mismatch is found, repair/regenerate and run the complete checklist again. `Looks correct` is not sufficient evidence.

## 12. Deterministic instrument examples

### Ruler
1 cm @1 mm = 10 intervals / 11 positions / 9 interior positions.

### Thermometer
Target must be exactly representable in discrete mode; liquid endpoint lies exactly on target graduation centerline. Example 0–50°C @1°C = 50 intervals/51 positions.

### Speedometer
Canonical direct-reading profile: 0–120 km/h, 240° active open arc, 10 km/h minor interval, 20 km/h major interval, 12 active intervals/13 positions, 120° inactive gap, one needle, `target_angle=(240+2*target_kmh) mod 360`.

Direct speedometer reading does not silently activate `speed=distance/time` calculation.

## 13. Exact measurement relations/formulas

Time: `60 s=1 min`, `60 min=1 h`, `24 h=1 day`.

Length: `10 mm=1 cm`, `100 cm=1 m`, `1000 m=1 km`.

Area: `1 m²=10,000 cm²`, `1 km²=1,000,000 m²`; conversion uses squared factors.

Weight: `1000 g=1 kg`; Thai context `1 ขีด=100 g=0.1 kg`.

Capacity/volume: `1000 mL=1 L`, `1000 cm³=1 dm³`, `1000 dm³=1 m³`, `1 m³=1,000,000 cm³`; cubic conversion uses cubed factors.

Perimeter: polygon boundary once, rectangle `2(l+w)`, square `4s`.

Area: rectangle `lw`, square `s²`, triangle `1/2 bh`, parallelogram `bh`, trapezoid `1/2(a+b)h`, circle `πr²` with one consistent `PI_POLICY`.

Rectangular prism: `V=lwh` after compatible-unit normalization.

## 14. Canonical labels

Legitimate instructional labels remain visible: clock numerals, dial/speedometer labels, ruler/protractor graduations, thermometer/capacity labels, graph/table labels and given dimensions.

## 15. Final Prompt mandatory properties

The Final Prompt must:

1. state `RENDER_OBJECTIVE=STUDENT_WORKSHEET`;
2. use one resolved render path;
3. state page/orientation/color/page policy;
4. state grade/subject/domain/topic/objective and exact question count;
5. contain exact learner-visible title/instructions/header/givens/blanks;
6. contain explicit layout/minimum dimensions;
7. contain canonical template and every visual item state;
8. contain resolved `SCALE_LINE_SPEC` when learner-read scale exists;
9. contain unit/formula/topology rules required for correctness;
10. contain `INSTRUMENT_REVIEW_REVISE_PROTOCOL` when learner-read instruments exist;
11. separate theme from academic geometry;
12. preserve canonical labels;
13. contain hard negatives/no-answer/no-meta rules;
14. contain no unresolved placeholders or hidden external dependencies.

Forbidden: `[ภาพ...]`, `[รูป...]`, `<draw here>`, `TBD`, `same as above`, `use blueprint above`, `see previous section`, omitted states via `etc.`.

## 16. Answer-key mode

Default `SHOW_ANSWER_KEY=NO`.

If YES, default is unsolved student worksheet + separate answer-key page/section. Inline solved worksheet requires explicit request.

## 17. QA phase semantics

Renderer self-review is prevention, not artifact proof.

Before actual downstream artifact inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Never report actual tick count/alignment/glyph/crop PASS without inspecting the artifact.

If supplied artifact contains one wrong instructional scale:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and the defect becomes a permanent regression.

## 18. Revision contract

Mutate canonical normalized state first, rerun affected workers, rebuild Student Blueprint/layout/renderer metadata, rerun QA and recompile Final Prompt.

Do not patch final wording while canonical state is stale.

## 19. Release rule

Prompt release requires zero critical blockers and all applicable route, compatibility, ownership, academic, scale-line, review/revise, formula, layout, leak, label, completeness and copy-readiness gates to PASS.

A prompt that leaves required geometry to renderer invention or permits blind first-pass release is incomplete.
