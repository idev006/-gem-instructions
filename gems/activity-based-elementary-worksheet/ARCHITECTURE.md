# Architecture — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
Status: Production Orchestrator + 10 Specialist Workers + Dual Instrument-Safety Audit + Primary Learner Quality

## 1. System model

The Gem is an Orchestrator over ten logical Specialist Workers.

1. `INTERACTION/NORMALIZATION` — parse teacher language and resolve safe defaults/provenance.
2. `WORKER_ROUTING` — select owning academic workers plus W08/W09 and W07+W10 for learner-read geometry.
3. `ACADEMIC_WORKER_LAYER` — deterministic content/rules owned by W01–W06.
4. `INSTRUMENT_GEOMETRY_LAYER` — owning worker creates canonical state; W07 audits topology, scale lines, common centers/origins and shape integrity.
5. `METROLOGY_ASSURANCE_LAYER` — W10 independently recomputes count, spacing, reference/common-center, label order, target alignment, shape and physical page evidence.
6. `VISIBILITY_LAYER` — separate INTERNAL, teacher-visible renderer metadata and student-visible worksheet.
7. `LAYOUT_RENDER_LAYER` — W08 resolves render path, shape-aware page feasibility, Thai/text, print/theme and review protocol.
8. `PRIMARY_LEARNER_LAYER` — mandatory pedagogy/usability checks for grade appropriateness, instruction clarity, ambiguity, typography, writing space, visual load, answer-format integrity and teaching-instrument simplicity.
9. `PROMPT_COMPILER` — compile one self-contained downstream prompt.
10. `QA_RELEASE_LAYER` — W09 runs conjunctive compatibility, ownership, academic, learner, leak, geometry, metrology and page gates.
11. `DOWNSTREAM_RENDER_PREVENTION_LOOP` — renderer generates, self-reviews, repairs/regenerates, rechecks, finalizes.
12. `DOWNSTREAM_ARTIFACT_PHASE` — actual image/document requires metrology inspection plus learner-simulation QA.

Production endpoint is a verified prompt/package. W07/W10/renderer checks are prevention, not proof pixels are correct.

## 2. Worker registry

- `W01_ACADEMIC_CONTENT`
- `W02_TIME_CLOCK`
- `W03_WEIGHT_SCALE`
- `W04_LENGTH_DISTANCE`
- `W05_TEMPERATURE_CAPACITY_VOLUME`
- `W06_MONEY_CALENDAR_DATA`
- `W07_INSTRUMENT_AUDITOR`
- `W08_LAYOUT_RENDER_THAI`
- `W09_QA_RELEASE`
- `W10_METROLOGY_ENGINEER`

Every worker contract defines `ACCEPTS | OWNS | RETURNS | MUST_NOT_DECIDE | QA`. W10 is a production base worker, not a hotfix override.

## 3. Mandatory runtime profiles

Every W01–W10 generated Knowledge bundle inherits five technical safety profiles:

1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `METROLOGY_ASSURANCE_PROFILE.md`
5. `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Every bundle also inherits:

`PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`

The first five remain the **five mandatory technical shared profiles**. The pedagogy profile is a separate mandatory learner-facing contract.

When learner-read geometry exists, `INSTRUMENT_READING_ENGINE.md` supplies shared geometry semantics while the owning domain engine defines numeric truth.

## 4. Canonical state objects

### REQUEST_CONTEXT
Raw teacher request + references + revisions.

### NORMALIZED_WORKSHEET_SPEC
Resolved parameters/provenance/domain/grade/render input/page policy. If no explicit page override exists: A4 Portrait.

### WORKER_ROUTE_DECISION
Selected worker IDs, reason, ownership and applicable QA.

### INTERNAL_VERIFIED_STATE
Hidden academic content, formulas, targets and independent verification.

### STUDENT_CONTENT_BLUEPRINT
Learner-visible givens/labels/blanks only; no hidden targets/audits. Must also satisfy primary-school clarity/ambiguity/answer-format rules.

### SCALE_LINE_SPEC
Required for learner-read scales. Includes topology, range, intervals/counts, direction, baseline/ring/axis, anchoring, hierarchy, endpoint semantics, min/selected size, spacing oracle, inactive-region rule and common center/origin when radial/angular.

### W07_GEOMETRY_AUDIT_STATE
Canonical topology/scale geometry, common-center/shape state and renderer-review requirements.

### METROLOGY_AUDIT_STATE
Required W10 independent second opinion with topology/count/spacing/reference/common-center/direction/hierarchy/labels/target/inactive-region/shape/template/page evidence and `INDEPENDENT_VERDICT=PASS|FAIL`.

### PHYSICAL_PAGE_STATE
Numeric shape-aware page proof: page dimensions, margins, header/title/directions reserve, rows/columns, complete item boxes, answer zones, gaps, usable dimensions, required dimensions and PASS/FAIL inequalities.

### PRIMARY_LEARNER_STATE
Applicable learner-facing evidence:
`GRADE_APPROPRIATENESS`
`INSTRUCTION_CLARITY`
`VISIBLE_AMBIGUITY_CHECK`
`TYPOGRAPHY_STATE`
`WRITING_SPACE_STATE`
`VISUAL_LOAD_STATE`
`DECORATION_ISOLATION`
`ANSWER_FORMAT_STATE`
`ITEM_PROGRESSION_STATE`
`PRINT_CONTRAST_STATE`

### TEACHER_VISIBLE_RENDER_STATE
Renderer-only metadata marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

Each learner-read item is atomic:
`ITEM_ID + SEMANTIC_TARGET + EXACT_RENDER_STATE + RELATIONAL_VERIFICATION + ITEM_SPECIFIC_HARD_NEGATIVE`.

### ACADEMIC_GEOMETRY_MANIFEST
For learner-read geometry:
`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES`
plus deterministic formulas/primitive positions sufficient to reconstruct educational geometry.

### INSTRUMENT_REVIEW_REVISE_PROTOCOL
Required when learner-read instruments exist, including `NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`.

### LAYOUT_BLUEPRINT
Page regions, shape-aware item boxes, safe sizes, typography/writing zones and pagination.

### FINAL_IMAGE_GENERATION_PROMPT
Primary self-contained downstream prompt.

### QA_REPORT
Prompt gates + explicit artifact status.

## 5. Canonical process

`Teacher request`
→ normalize/provenance
→ route workers
→ independently verify academic state
→ build canonical instrument state when applicable
→ W07 audit
→ W10 independent audit
→ student-safe blueprint
→ resolve render path
→ W08 numeric shape-aware layout
→ primary-school pedagogy/usability audit
→ compile prompt
→ W09 conjunctive QA
→ prompt release
→ downstream render
→ renderer self-review/revise/recheck
→ actual artifact metrology + learner-simulation inspection.

Mandatory learner-read route:
`OWNING WORKER → W07 → W10 → W08 → W09`

## 6. Deterministic academic geometry ownership

For learner-read geometry, free-form image generation may decorate but may not own/recreate academic ticks, labels, hands, pointers, rays, axes or reading levels.

Required:
`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES`
`CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES`
`POST_LAYOUT_GEOMETRY_TRANSFORM=UNIFORM_SCALE_AND_TRANSLATE_ONLY`

This closes the architectural gap where formulas were correct but image geometry was approximated.

## 7. Critical canonical smoke oracles

Clock: 60 positions; continuous hour hand; exact vector endpoint for nonzero minutes.

Weight dial: 0–5kg @0.1, top-zero clockwise, 50/51, exactly10 intervals/9 interior marks per kg, +0.5kg intermediate, gap clean, pivot=center.

Ruler:1cm @1mm→10/11/9, edge not tick, endpoint projections.

Speedometer:0–120 @10→12/13,240° active,120° gap,pivot=center,radial pointer.

Thermometer:0–50°C @1→50/51;6 major/5 intermediate/40 minor; each10°C span10/9; endpoint exact.

Protractor: perfect upper semicircle0–180° @1→180/181; single active scale default; common origin; radial ticks/rays; width>=70mm; body height=W/2 before reserves.

Graduated container: exact global/local topology + declared read convention.

Graph axis: equal numeric increments→equal physical increments, 2D presentation.

## 8. Shape-aware page + learner safety

Implicit page default is A4 Portrait. `RENDER_PATH=AUTO` resolves before prompt release.

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

But physical packing PASS does not prove learner usability. The same plan must preserve learner typography, writing space and visual clarity.

If `ONE_PAGE_LOCK=OFF`, failed/over-dense candidates are recomputed/paginated. Never delete required graduations, reduce required text below learner defaults, or remove response space to force one page.

## 9. Renderer prevention loop

Mandatory when learner-read geometry exists:
`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Review checks primitive manifest/count, anchoring, common center/origin, spacing, hierarchy, label order, target alignment, radial collinearity, inactive region, shape integrity and print readability. `Looks correct` is insufficient.

## 10. Visibility architecture

Three scopes:
1. `INTERNAL_VERIFIED_STATE`
2. `TEACHER_VISIBLE_PROMPT_METADATA`
3. `STUDENT_VISIBLE_WORKSHEET`

W07/W10 evidence and renderer geometry metadata never print on the student worksheet.

## 11. Release and artifact boundary

Any applicable critical technical or pedagogy gate FAIL/NOT_RUN means:
`PROMPT_RELEASE=BLOCKED`.

Before actual artifact inspection:
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`.

Actual inspection includes `ARTIFACT_LEARNER_SIMULATION_QA`: a child must be able to understand the task, locate the instructional evidence and response area, and solve from visible information alone.

One incorrect instructional scale, unreadable required text, ambiguous visual reference, wrong pivot/origin or distorted geometry means:
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`
and requires permanent regression before next accepted release.
