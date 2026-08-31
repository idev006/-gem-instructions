# Output Contract — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
Default mode: `PROMPT_PACKAGE`
Primary deliverable: `FINAL_IMAGE_GENERATION_PROMPT`
Product role: `PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

## 1. Product boundary

The Gem compiles and verifies a worksheet-generation prompt. It does not claim downstream worksheet pixels have passed visual QA before the artifact is supplied and inspected.

Learner-read prompt release requires owning-domain evidence, W07 geometry evidence, W10 independent metrology evidence, W08 shape-aware page/render evidence, and renderer review/revise prevention loop.

## 2. Default visible package

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

Section 6 must be independently copy-ready.

## 3. Visibility scopes

### INTERNAL_VERIFIED_STATE
Answers, formulas, normalized values, target geometry, W07 audit and W10 `METROLOGY_AUDIT_STATE`.

### TEACHER_VISIBLE_PROMPT_METADATA
Renderer-only values marked:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

### STUDENT_VISIBLE_WORKSHEET
Only learner-facing title, directions, givens, canonical labels, diagrams and blank answer areas.

## 4. Student Blueprint contract

Exactly one student-facing object/row per question. Forbidden when answer key is off: solved answers, target time/weight/length/angle/speed/temperature/level, hand/needle/ray angles, tick indices, target endpoints, liquid levels, renderer relations/hard negatives, W07/W10 audit data.

## 5. Worker/profile compatibility

Before compilation:

- route with `KB_ROUTER.md`;
- verify 10-worker installation with `KB_MANIFEST.md`;
- apply owning worker academic state;
- apply W07 geometry audit;
- apply W10 independent metrology audit;
- apply W08 shape-aware layout/render/Thai;
- apply W09 conjunctive release.

Every runtime bundle contains five mandatory profiles:

- `SYSTEM_WIDE_QUALITY_PROFILE.md`
- `SCALE_LINE_INTEGRITY_PROFILE.md`
- `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `METROLOGY_ASSURANCE_PROFILE.md`
- `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Missing mandatory runtime knowledge blocks release.

## 6. Render path, output mode and page plan

`OUTPUT_MODE=PROMPT_PACKAGE`

Allowed final render paths:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

AUTO resolves before release. Exact learner-read graduations require deterministic geometry; `IMAGE_ONLY` is forbidden if nondeterminism can alter scale geometry.

One-page-first must not reduce topology/count/spacing/Thai readability/answer space. One-page PASS requires numeric `PHYSICAL_PAGE_STATE` with shape-aware item boxes. `ONE_PAGE_LOCK=OFF` allows pagination; `ONE_PAGE_LOCK=ON` conflicting with safe geometry blocks release.

## 7. Global render constraints

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
`SCALE_LINE_SPEC_REQUIRED=YES`
`METROLOGY_AUDIT_REQUIRED=YES`
`PHYSICAL_PAGE_STATE_REQUIRED=YES`
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

## 8. Scale-line and common-center contract

Endpoint-inclusive linear scale:

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/MINOR_INTERVAL`
`EXPECTED_TICK_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`
`EXPECTED_INTERIOR_POSITION_COUNT=max(EXPECTED_TICK_POSITION_COUNT-2,0)`

Canonical ruler 1cm @1mm =10 intervals/11 positions/9 interior; physical edge not graduation.

Radial/angular instruments require:

`PIVOT_CENTER == READING_RING_CENTER == TICK_RADIAL_CENTER`

or for protractor:

`ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`.

Pointers/rays must be radial/collinear from the common center.

## 9. Mandatory W10 metrology state

For each learner-read canonical template, hidden/teacher metadata includes:

`METROLOGY_AUDIT_STATE`

with at least:

`INSTRUMENT_FAMILY`
`TOPOLOGY_CHECK`
`COUNT_ORACLE`
`SPACING_ORACLE`
`METROLOGY_MINIMUM_SIZE_MM`
`SELECTED_RENDER_SIZE_MM`
`SIZE_ORACLE_SOURCE`
`REFERENCE_ORIGIN_CHECK`
`COMMON_CENTER_CHECK` when radial/angular
`POINTER_ORIGIN_COINCIDENCE_CHECK` when applicable
`RADIAL_COLLINEARITY_CHECK` when applicable
`DIRECTION_MONOTONICITY_CHECK`
`HIERARCHY_CHECK`
`LABEL_ASSOCIATION_CHECK`
`LABEL_ORDER_CHECK` when applicable
`TARGET_ALIGNMENT_CHECK`
`INACTIVE_REGION_CHECK` when applicable
`SHAPE_INTEGRITY_CHECK` when applicable
`TEMPLATE_CONSISTENCY_CHECK`
`PHYSICAL_PAGE_STATE`
`PRINT_FEASIBILITY_CHECK`
`INDEPENDENT_VERDICT=PASS|FAIL`

This state must not be printed.

## 10. Canonical instrument smoke contracts

Weight 0–5kg @0.1: top-zero clockwise labels `{0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`, 50/51, gap `(300°,360°)`, zero radial gap marks, pivot=center.

Speedometer 0–120 @10: 12/13, `target_angle=(240+2*target_kmh) mod 360`, 120° inactive gap, pivot=center, radial needle.

Thermometer 0–50°C @1: 50/51, 6 major/5 intermediate/40 ordinary minor, each10°C span10 intervals/9 interior, endpoint exact.

Protractor 0–180° @1: perfect upper semicircle, 180/181, single active numeric scale default, 0° right/90° top/180° left, common center/origin, radial ticks/rays, width>=70mm at0.60mm floor, no geometric distortion.

## 11. High-risk per-item state

Each learner-read item uses one atomic block:

`ITEM_ID`
`SEMANTIC_TARGET`
`EXACT_RENDER_STATE`
`RELATIONAL_VERIFICATION`
`ITEM_SPECIFIC_HARD_NEGATIVE`

Radial/angular state also serializes common center/origin identity. No wide Markdown table when wrapping could change field meaning.

## 12. Mandatory renderer review block

Final prompt with learner-read instruments includes `INSTRUMENT_REVIEW_REVISE_PROTOCOL` and:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Required semantics:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Review includes recount, label order, common center/origin, radial collinearity, shape integrity, target alignment and gap checks. A vague `looks correct` is insufficient.

## 13. Prompt QA

Applicable gates include route/compatibility/ownership, academic data, Student Blueprint isolation, resolved render path, field semantics, page provenance, physical page state, shape-aware item boxes, completeness, copy-ready, no-placeholder, scale-line/common-center/shape gates, review/revise gates and all W10 metrology gates.

If W10 audit is missing, copied, contradictory, FAIL or NOT_RUN:

`PROMPT_RELEASE=BLOCKED`

## 14. Artifact boundary

Before actual rendered image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

W07/W10 prompt audits and renderer self-review are prevention only.

One incorrect learner-read scale, label order, pivot/origin, or distorted instrument means:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and defect becomes permanent regression.
