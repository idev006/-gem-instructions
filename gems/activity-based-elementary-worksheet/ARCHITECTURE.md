# Architecture — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
Status: Production Orchestrator + 10 Specialist Workers + Dual Instrument-Safety Audit

## 1. System model

The Gem is an Orchestrator over ten logical Specialist Workers.

1. `INTERACTION/NORMALIZATION` — parse teacher language and resolve safe defaults/provenance.
2. `WORKER_ROUTING` — select owning academic workers plus W08/W09 and W07+W10 for learner-read geometry.
3. `ACADEMIC_WORKER_LAYER` — deterministic content/rules owned by W01–W06.
4. `INSTRUMENT_GEOMETRY_LAYER` — owning worker creates canonical state; W07 audits topology, scale lines, common centers/origins and shape integrity.
5. `METROLOGY_ASSURANCE_LAYER` — W10 independently recomputes count, spacing, reference/common-center, label order, target alignment, shape and physical page evidence.
6. `VISIBILITY_LAYER` — separate INTERNAL, teacher-visible renderer metadata and student-visible worksheet.
7. `LAYOUT_RENDER_LAYER` — W08 resolves render path, shape-aware page feasibility, Thai/text, print/theme and review protocol.
8. `PROMPT_COMPILER` — compile one self-contained downstream prompt.
9. `QA_RELEASE_LAYER` — W09 runs conjunctive compatibility, ownership, academic, leak, geometry, metrology and page gates.
10. `DOWNSTREAM_RENDER_PREVENTION_LOOP` — renderer generates, self-reviews, repairs/regenerates, rechecks, finalizes.
11. `DOWNSTREAM_ARTIFACT_PHASE` — actual image/document requires separate inspection.

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

Every worker contract defines:

`ACCEPTS | OWNS | RETURNS | MUST_NOT_DECIDE | QA`

W10 is a production base worker, not a hotfix override.

## 3. Five mandatory shared runtime profiles

Every W01–W10 generated Knowledge bundle inherits:

1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `METROLOGY_ASSURANCE_PROFILE.md`
5. `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

When learner-read geometry exists, `INSTRUMENT_READING_ENGINE.md` supplies shared geometry semantics while owning domain engine defines numeric truth.

## 4. Canonical state objects

### REQUEST_CONTEXT
Raw teacher request + references + revisions.

### NORMALIZED_WORKSHEET_SPEC
Resolved parameters/provenance/domain/grade/render input/page policy.

### WORKER_ROUTE_DECISION
Selected worker IDs, reason, ownership and applicable QA.

### INTERNAL_VERIFIED_STATE
Hidden academic content, formulas, targets and independent verification.

### STUDENT_CONTENT_BLUEPRINT
Learner-visible givens/labels/blanks only; no hidden targets/audits.

### SCALE_LINE_SPEC
Required for learner-read scales. Includes topology, range, intervals/counts, direction, baseline/ring/axis, anchoring, hierarchy, endpoint semantics, min/selected size, spacing oracle, inactive-region rule and common center/origin when radial/angular.

### W07_GEOMETRY_AUDIT_STATE
Canonical topology/scale geometry, common-center/shape state and renderer-review requirements.

### METROLOGY_AUDIT_STATE
Required W10 independent second opinion:

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

### PHYSICAL_PAGE_STATE
Numeric shape-aware page proof: page dimensions, margins, header/title/directions reserve, rows/columns, complete item boxes, answer zones, gaps, usable dimensions, required dimensions and PASS/FAIL inequalities.

### TEACHER_VISIBLE_RENDER_STATE
Renderer-only metadata marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

Each learner-read item is atomic:
`ITEM_ID + SEMANTIC_TARGET + EXACT_RENDER_STATE + RELATIONAL_VERIFICATION + ITEM_SPECIFIC_HARD_NEGATIVE`.

### INSTRUMENT_REVIEW_REVISE_PROTOCOL
Required when learner-read instruments exist, including `NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`.

### LAYOUT_BLUEPRINT
Page regions, shape-aware item boxes, safe sizes and pagination.

### FINAL_IMAGE_GENERATION_PROMPT
Primary self-contained downstream prompt.

### QA_REPORT
Prompt gates + explicit artifact status.

## 5. Canonical process

`Teacher request`
→ normalize/provenance
→ route workers
→ independently verify academic state
→ build canonical instrument state
→ resolve `SCALE_LINE_SPEC`
→ W07 geometry/common-center/shape audit
→ W10 independent metrology/page audit
→ student-safe blueprint
→ resolve render path
→ W08 numeric shape-aware layout
→ compile prompt
→ W09 conjunctive QA
→ prompt release
→ downstream render
→ renderer self-review/revise/recheck
→ actual artifact inspection.

Mandatory learner-read route:

`OWNING WORKER → W07 → W10 → W08 → W09`

## 6. Independent measurement safety

W07 and W10 have distinct responsibilities. W10 independently recomputes quantitative evidence rather than repeating W07 PASS.

Universal W10 checks: count, references, common center/origin, direction, spacing, hierarchy, labels/order, target representability/alignment, radial collinearity, inactive region, shape integrity, template consistency and shape-aware page feasibility.

## 7. Critical canonical smoke oracles

Clock: 60 intervals/60 positions/6°; hands share pivot; 10:30→minute180°, hour315°.

Weight dial: 0–5kg @0.1, top-zero clockwise labels `{0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`, 50/51, gap `(300°,360°)`, pivot=center.

Ruler: 1cm @1mm→10 intervals/11 positions/9 interior; edge not tick; nonzero reading=end-start.

Speedometer: 0–120 @10→12/13, 240° active,120° gap, `target_angle=(240+2*target_kmh) mod 360`, pivot=center, radial needle.

Thermometer: 0–50°C @1→50/51; 6 major/5 intermediate/40 minor; each10°C span10 intervals/9 interior; endpoint exact.

Protractor: perfect upper semicircle 0–180° @1→180/181; single active scale default; common center=baseline midpoint=ray origin; radial ticks/rays; width>=70mm at0.60mm floor; body height=W/2 before layout reserves.

Graduated container: exact topology + declared read convention.

Graph axis: equal numeric increments→equal geometric increments.

## 8. Shape-aware page safety

`RENDER_PATH=AUTO` resolves before prompt release. Learner-read exact geometry uses deterministic instrument geometry.

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

Shape-aware examples:
- circular diameter D contributes D×D body;
- semicircular protractor width W contributes body height W/2;
- vertical thermometer uses selected scale/body height.

If `ONE_PAGE_LOCK=OFF`, failed candidate is recomputed/paginated. If lock ON conflicts with safe geometry, release blocked. Never delete/merge/compress graduations to fit.

## 9. Renderer prevention loop

Mandatory when learner-read geometry exists:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Review checks count, anchoring, common center/origin, spacing, hierarchy, label order, target alignment, radial collinearity, inactive region, shape integrity and print readability. `Looks correct` is insufficient.

## 10. Visibility architecture

Three scopes:
1. `INTERNAL_VERIFIED_STATE`
2. `TEACHER_VISIBLE_PROMPT_METADATA`
3. `STUDENT_VISIBLE_WORKSHEET`

W07/W10 evidence never prints on student worksheet.

## 11. Release and artifact boundary

Any applicable critical gate FAIL/NOT_RUN means:
`PROMPT_RELEASE=BLOCKED`.

Before actual artifact inspection:
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`.

One incorrect instructional scale, label order, pivot/origin or distorted geometry means:
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`
and requires permanent regression before next accepted release.
