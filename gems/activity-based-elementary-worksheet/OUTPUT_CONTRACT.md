# Output Contract — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
Default mode: `PROMPT_PACKAGE`
Primary deliverable: `FINAL_IMAGE_GENERATION_PROMPT`
Product role: `PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

## 1. Product boundary

The Gem compiles and verifies a worksheet-generation prompt. It does not claim downstream worksheet pixels have passed visual QA before the artifact is supplied and inspected.

For learner-read instruments, prompt release requires both W07 geometry evidence and W10 independent metrology evidence plus the renderer-side prevention loop.

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

Exactly one student-facing object/row per question.

Forbidden when answer key is off: solved answers, target time/weight/length/angle/speed/temperature/level, hand/needle/ray angles, tick indices, target endpoints, liquid levels, renderer relations, hard negatives, W07 audit data or W10 metrology data.

## 5. Worker/profile compatibility

Before compilation:

- route with `KB_ROUTER.md`;
- verify 10-worker installation with `KB_MANIFEST.md`;
- apply owning worker academic state;
- apply W07 geometry audit;
- apply W10 independent metrology audit;
- apply W08 layout/render/Thai;
- apply W09 conjunctive release.

Every runtime bundle contains:

- `SYSTEM_WIDE_QUALITY_PROFILE.md`
- `SCALE_LINE_INTEGRITY_PROFILE.md`
- `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `METROLOGY_ASSURANCE_PROFILE.md`

Missing mandatory runtime knowledge blocks release.

## 6. Render path and layout

Allowed final render paths:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

AUTO must resolve before release.

Exact learner-read graduations require deterministic geometry. `IMAGE_ONLY` is forbidden if nondeterminism can alter scale geometry.

One-page-first must not reduce scale topology, count, printed spacing, Thai readability or answer space. If `ONE_PAGE_LOCK=ON` conflicts with W07/W10 minimum geometry, release is blocked.

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
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

## 8. Scale-line and metrology contract

Endpoint-inclusive linear scale:

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/MINOR_INTERVAL`
`EXPECTED_TICK_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`
`EXPECTED_INTERIOR_POSITION_COUNT=max(EXPECTED_TICK_POSITION_COUNT-2,0)`

Canonical ruler 1 cm @1 mm = `10 intervals / 11 positions / 9 interior positions`; physical edge is not a graduation.

Radial print-spacing oracle:

`tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)`

Canonical 0–180° @1° protractor at 0.60 mm floor requires reading-ring diameter ≈68.76 mm and production width 70 mm; 65 mm is invalid.

## 9. Mandatory W10 metrology state

For every canonical learner-read instrument template, hidden/teacher metadata includes:

`METROLOGY_AUDIT_STATE`

with:

`INSTRUMENT_FAMILY`
`TOPOLOGY_CHECK`
`COUNT_ORACLE`
`SPACING_ORACLE`
`REFERENCE_ORIGIN_CHECK`
`DIRECTION_MONOTONICITY_CHECK`
`HIERARCHY_CHECK`
`LABEL_ASSOCIATION_CHECK`
`TARGET_ALIGNMENT_CHECK`
`INACTIVE_REGION_CHECK` when applicable
`TEMPLATE_CONSISTENCY_CHECK`
`PRINT_FEASIBILITY_CHECK`
`INDEPENDENT_VERDICT=PASS|FAIL`

This state must not be printed on the worksheet.

## 10. High-risk per-item state

Each learner-read item uses one atomic block:

`ITEM_ID`
`SEMANTIC_TARGET`
`EXACT_RENDER_STATE`
`RELATIONAL_VERIFICATION`
`ITEM_SPECIFIC_HARD_NEGATIVE`

No wide Markdown table may be used when wrapping/column drift can change field semantics.

## 11. Mandatory renderer review block

Final prompt with learner-read instruments includes `INSTRUMENT_REVIEW_REVISE_PROTOCOL` and:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Required semantics:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

A vague `looks correct` check is insufficient.

## 12. Prompt QA

Applicable gates include route/compatibility/ownership, academic data, Student Blueprint isolation, resolved render path, page-lock provenance, one-page feasibility, completeness, copy-ready, no-placeholder, label preservation, scale-line gates, review/revise gates and all W10 metrology gates.

If W10 audit is missing, copied from W07 without independent evidence, or FAIL/NOT_RUN:

`PROMPT_RELEASE=BLOCKED`

## 13. Artifact boundary

Before actual rendered image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

W07/W10 prompt audits and renderer self-review are prevention layers only.

One incorrect learner-read scale in an actual artifact means:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and the defect becomes a permanent regression.
