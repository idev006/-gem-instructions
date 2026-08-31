# Architecture — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
Status: Production Orchestrator + 10 Specialist Workers + Dual Instrument-Safety Audit

## 1. System model

The Gem is an Orchestrator over ten logical Specialist Workers.

1. `INTERACTION/NORMALIZATION` — parse teacher language and resolve safe defaults/provenance.
2. `WORKER_ROUTING` — select owning academic workers plus universal W08/W09 and W07+W10 when learner-read geometry exists.
3. `ACADEMIC_WORKER_LAYER` — deterministic content/rules owned by W01–W06.
4. `INSTRUMENT_GEOMETRY_LAYER` — owning worker creates canonical state; W07 audits topology/geometry/scale-line construction.
5. `METROLOGY_ASSURANCE_LAYER` — W10 independently recomputes count, physical spacing, reference correctness, target alignment and print/page feasibility.
6. `VISIBILITY_LAYER` — separate INTERNAL, TEACHER_VISIBLE_PROMPT_METADATA and STUDENT_VISIBLE_WORKSHEET.
7. `LAYOUT_RENDER_LAYER` — W08 resolves render path, page feasibility, Thai/text, print/theme and serializes review/revise protocol.
8. `PROMPT_COMPILER` — compile one self-contained final downstream prompt.
9. `QA_RELEASE_LAYER` — W09 runs conjunctive compatibility, ownership, academic, leak, scale-line, metrology and review-protocol gates.
10. `DOWNSTREAM_RENDER_PREVENTION_LOOP` — renderer generates, self-reviews, repairs/regenerates mismatches, rechecks, finalizes.
11. `DOWNSTREAM_ARTIFACT_PHASE` — actual image/document requires separate artifact inspection.

The production endpoint is a verified generation prompt/package. W07/W10/renderer checks are prevention layers, not proof that pixels are correct.

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

## 3. Mandatory shared runtime profiles

Every W01–W10 generated Knowledge bundle inherits:

1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `METROLOGY_ASSURANCE_PROFILE.md`

When learner-read geometry exists, `INSTRUMENT_READING_ENGINE.md` supplies shared geometry semantics while the owning domain engine defines numeric truth.

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
Required for learner-read scales. Includes topology, range, minor/major interval, exact counts, direction, authoritative baseline/ring/arc/axis, anchoring, hierarchy, endpoint semantics, minimum printed size, minimum tick spacing and inactive-region rule when applicable.

### W07_GEOMETRY_AUDIT_STATE
Canonical topology/scale geometry and renderer-review requirements.

### METROLOGY_AUDIT_STATE
Required W10 independent second opinion:

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

### TEACHER_VISIBLE_RENDER_STATE
Renderer-only metadata marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

Each learner-read item is atomic:
`ITEM_ID + SEMANTIC_TARGET + EXACT_RENDER_STATE + RELATIONAL_VERIFICATION + ITEM_SPECIFIC_HARD_NEGATIVE`.

### INSTRUMENT_REVIEW_REVISE_PROTOCOL
Required when learner-read instruments exist, including:
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`.

### LAYOUT_BLUEPRINT
Page regions, minimum sizes, scale readability, one-page feasibility/pagination.

### FINAL_IMAGE_GENERATION_PROMPT
Primary self-contained downstream prompt.

### QA_REPORT
Prompt gates + explicit artifact status.

## 5. Canonical process

`Teacher request`
→ normalize + provenance
→ route workers
→ generate/independently verify academic state
→ build canonical instrument state when applicable
→ resolve `SCALE_LINE_SPEC`
→ W07 geometry audit
→ W10 independent metrology audit
→ build student-safe blueprint
→ resolve one render path
→ one-page feasibility using W07/W10 minima
→ W08 layout + atomic state + review serialization
→ compile Final Prompt
→ W09 conjunctive QA
→ prompt release
→ downstream render
→ renderer self-review/revise/recheck
→ actual artifact inspection.

Mandatory learner-read route is:

`OWNING WORKER → W07 → W10 → W08 → W09`

## 6. Independent measurement safety

W07 and W10 have different responsibilities. W07 verifies intended geometry/topology. W10 must independently recompute at least one quantitative metrology oracle and may not merely repeat W07's PASS.

Universal W10 checks include exact interval/position count, reference/origin, direction, uniformity, physical print spacing, hierarchy, labels, target representability/alignment, inactive region, template consistency, and print/page feasibility.

Radial print spacing:

`tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)`

For 0–180° @1° with 0.60 mm floor: minimum reading-ring diameter ≈68.76 mm; production width 70 mm. 65 mm is rejected.

## 7. Renderer prevention loop

Mandatory whenever learner-read geometry exists:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Review checks count, anchoring, spacing, hierarchy, labels, missing/extra ticks, reference edge/origin, target alignment, inactive region, decoration isolation, template consistency and print readability.

`Looks correct` is insufficient.

## 8. Visibility architecture

Three scopes:
1. `INTERNAL_VERIFIED_STATE`
2. `TEACHER_VISIBLE_PROMPT_METADATA`
3. `STUDENT_VISIBLE_WORKSHEET`

W07/W10 audit evidence is never printed on the student worksheet.

## 9. Measurement ownership

- W02: time and clocks
- W03: weight/dial scales
- W04: ruler/length/distance/direct speedometer/angle/protractor/perimeter/area
- W05: thermometer/capacity/meniscus/volume
- W06: money/calendar/data and graph semantics
- W07: shared instrument topology/geometry audit
- W10: independent metrology/measurement-instrument audit
- W08: layout/render/Thai/review serialization
- W09: conjunctive release

## 10. Smoke oracles

Clock: 60 intervals / 60 positions / 6°; 10:30 → minute 180°, hour 315°.

Weight dial: 0–5 kg @0.1 → 50 active intervals /51 positions +60° gap.

Ruler: 1 cm @1 mm → 10 intervals /11 positions /9 interior; edge not a tick; nonzero reading=end-start.

Speedometer: 0–120 @10 → 12/13, 240° active, 120° gap, `target_angle=(240+2*target_kmh) mod 360`.

Protractor: 0–180° @1° → 180/181 plus print-spacing oracle.

Thermometer: endpoint-inclusive topology and target-aligned liquid endpoint.

Graduated container: exact topology + declared read/meniscus convention.

Graph axis: equal numeric increments → equal geometric increments.

## 11. Page/render safety

`RENDER_PATH=AUTO` must resolve before prompt release. Learner-read exact geometry uses deterministic instrument geometry.

If `ONE_PAGE_LOCK=ON` conflicts with W07/W10 audited minimum geometry, release is blocked. Never solve density by deleting, merging, compressing or inventing graduations.

## 12. Release and artifact boundary

Any applicable critical gate FAIL/NOT_RUN, including missing W10 evidence, means:
`PROMPT_RELEASE=BLOCKED`.

Before actual artifact inspection:
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`.

One incorrect instructional scale in an actual artifact means:
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`
and requires a permanent regression before the next accepted release.
