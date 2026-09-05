# W09 — QA & Release Specialist

`WORKER_ID=W09_QA_RELEASE`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Route decision, owning-worker outputs, normalized spec/provenance, Student Blueprint, W07 geometry audit, W10 `METROLOGY_AUDIT_STATE`, layout blueprint, physical page state, render constraints, resolved `SCALE_LINE_SPEC`, review/revise protocol, and final prompt draft.

## OWNS

- worker compatibility/ownership validation
- integration QA
- visibility/leak QA
- prompt completeness/copy-readiness
- measurement/global regression gates
- scale-line and common-center release gates
- independent metrology release gates
- renderer review/revise protocol gates
- physical page/render-path/provenance gates
- prompt-vs-artifact phase semantics
- release decision
- installation health/self-check

## RETURNS

QA report, `PROMPT_RELEASE` decision, artifact status, classroom status and repair instructions when blocked.

## MUST_NOT_DECIDE

Academic formulas, domain target values, instrument topology, metrology formulas owned by W10 profile, page design or Thai wording except detecting violations.

## Installation health

Required base worker IDs:

`W01_ACADEMIC_CONTENT`
`W02_TIME_CLOCK`
`W03_WEIGHT_SCALE`
`W04_LENGTH_DISTANCE`
`W05_TEMPERATURE_CAPACITY_VOLUME`
`W06_MONEY_CALENDAR_DATA`
`W07_INSTRUMENT_AUDITOR`
`W08_LAYOUT_RENDER_THAI`
`W09_QA_RELEASE`
`W10_METROLOGY_ENGINEER`

All declare `BASELINE_COMPATIBILITY=2.6.x` and `WORKER_SCHEMA_VERSION=1`.

Mandatory shared runtime profiles — exactly five:

1. `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
3. `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `policies/METROLOGY_ASSURANCE_PROFILE.md`
5. `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

`KB_COMPATIBILITY_QA=FAIL` if any base worker/profile is missing or incompatible.

## Routing/ownership QA

Only owning academic workers generate domain truth. W07 independently audits geometry/topology. W10 independently audits metrology/common-center/shape/print/page feasibility. W08 owns layout/render/Thai and review serialization. W09 owns integration/release.

Every learner-read instrument route includes owning worker + `W07 + W10 + W08 + W09`.

Cross-worker academic override = FAIL. W10 may reject unsafe geometry but may not invent targets or override W02–W06 formulas.

## Student Blueprint isolation

`STUDENT_CONTENT_BLUEPRINT` contains student-visible semantics only.

Forbidden: renderer-only markers, target values, paired answers, hand/needle/ray angles, tick indices, target endpoints/liquid levels, solved vectors, renderer relations/hard negatives, W07 audit state, W10 metrology state.

Any leak:
`PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA=FAIL`
`PROMPT_RELEASE=BLOCKED`

No sanitizer may convert a structurally invalid blueprint into PASS.

## Instrument academic-safety hard gate

When a learner reads an instrument, visible geometry is academic data. Release requires:

1. owning-domain academic state PASS;
2. W07 geometry/scale audit PASS;
3. W10 independent metrology audit PASS;
4. W08 shape-aware layout/render constraints PASS;
5. renderer review/revise protocol present;
6. all applicable W09 gates PASS.

Final prompt includes:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

and:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

A vague `looks correct` review is insufficient.

### Renderer review/revise release gates — mandatory

For every learner-read instrument, all applicable review gates must be explicitly present and PASS:

`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`

The serialized protocol must require deterministic recount/rederivation, geometry/alignment checks, repair or regeneration on any mismatch, and a complete recheck after repair. Missing, contradictory, FAIL, or NOT_RUN review evidence forces `PROMPT_RELEASE=BLOCKED`.

## Independent W10 hard gate

Every canonical learner-read template requires independent `METROLOGY_AUDIT_STATE` evidence including, as applicable:

`TOPOLOGY_CHECK`
`COUNT_ORACLE`
`LOCAL_SPAN_RECOUNT_CHECK`
`SPACING_ORACLE`
`METROLOGY_MINIMUM_SIZE_MM`
`SELECTED_RENDER_SIZE_MM`
`SIZE_ORACLE_SOURCE`
`REFERENCE_ORIGIN_CHECK`
`REFERENCE_PROJECTION_CHECK`
`COMMON_CENTER_CHECK`
`POINTER_ORIGIN_COINCIDENCE_CHECK`
`RADIAL_COLLINEARITY_CHECK`
`DIRECTION_MONOTONICITY_CHECK`
`HIERARCHY_CHECK`
`LABEL_ASSOCIATION_CHECK`
`LABEL_ORDER_CHECK`
`TARGET_ALIGNMENT_CHECK`
`INACTIVE_REGION_CHECK`
`SHAPE_INTEGRITY_CHECK`
`PHYSICAL_PAGE_STATE`
`PRINT_FEASIBILITY_CHECK`
`INDEPENDENT_VERDICT`

Missing, copied, contradictory, FAIL or NOT_RUN applicable evidence forces `PROMPT_RELEASE=BLOCKED`.

Mandatory gates include:

`PROMPT_METROLOGY_AUDIT_REQUIRED_QA`
`PROMPT_METROLOGY_INDEPENDENCE_QA`
`PROMPT_METROLOGY_INTERVAL_COUNT_QA`
`PROMPT_METROLOGY_POSITION_COUNT_QA`
`PROMPT_METROLOGY_LOCAL_SPAN_RECOUNT_QA` when applicable
`PROMPT_METROLOGY_REFERENCE_QA`
`PROMPT_METROLOGY_REFERENCE_PROJECTION_QA` when applicable
`PROMPT_METROLOGY_COMMON_CENTER_QA` when radial/angular
`PROMPT_METROLOGY_RADIAL_COLLINEARITY_QA` when radial/angular
`PROMPT_METROLOGY_SPACING_ORACLE_QA`
`PROMPT_METROLOGY_HIERARCHY_QA`
`PROMPT_METROLOGY_LABEL_ASSOCIATION_QA`
`PROMPT_METROLOGY_LABEL_ORDER_QA` when applicable
`PROMPT_METROLOGY_TARGET_ALIGNMENT_QA`
`PROMPT_METROLOGY_INACTIVE_REGION_QA` when applicable
`PROMPT_METROLOGY_TEMPLATE_CONSISTENCY_QA`
`PROMPT_METROLOGY_SHAPE_INTEGRITY_QA` when applicable
`PROMPT_METROLOGY_RENDER_PATH_QA`
`PROMPT_METROLOGY_SIZE_ORACLE_QA`
`PROMPT_METROLOGY_PAGE_FEASIBILITY_QA`
`PROMPT_METROLOGY_PRINT_FEASIBILITY_QA`
`PROMPT_PHYSICAL_PAGE_STATE_QA`
`PROMPT_SHAPE_AWARE_BOUNDING_BOX_QA`

## Scale-line hard gates

For every learner-read scale require resolved `SCALE_LINE_SPEC` and exact topology/count, local-span topology when applicable, anchoring, spacing, hierarchy, labels/order, common center/origin, target alignment, inactive-region integrity, decoration isolation, shape integrity and template consistency.

Critical gates:

`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_SCALE_PRINT_SPACING_ORACLE_QA`
`PROMPT_SCALE_UNIFORM_SPACING_QA`
`PROMPT_SCALE_DIRECTION_QA`
`PROMPT_SCALE_LABEL_ALIGNMENT_QA`
`PROMPT_SCALE_LABEL_CLEARANCE_QA`
`PROMPT_SCALE_LABEL_ORDER_QA` when applicable
`PROMPT_SCALE_TARGET_ALIGNMENT_QA`
`PROMPT_SCALE_INACTIVE_REGION_QA` when applicable
`PROMPT_SCALE_DECORATION_ISOLATION_QA`
`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA`
`PROMPT_SCALE_LINE_SERIALIZATION_QA`
`PROMPT_INSTRUMENT_COMMON_CENTER_QA` when radial/angular
`PROMPT_POINTER_ORIGIN_COINCIDENCE_QA` when pointer/ray exists
`PROMPT_RADIAL_COLLINEARITY_QA` when radial/angular
`PROMPT_INSTRUMENT_SHAPE_INTEGRITY_QA`
`PROMPT_LOCAL_SPAN_RECOUNT_QA` when applicable

## Ruler hard gates

For 1 mm resolution, every complete 1 cm span independently verifies:

`INTERVALS_PER_CM=10`
`POSITIONS_PER_CM_SPAN=11`
`INTERIOR_POSITIONS_PER_CM_SPAN=9`
`PHYSICAL_EDGE_IS_GRADUATION=NO`

A 5 mm hierarchy mark occupies an existing position.

For object-on-ruler measurement, require exact endpoint/reference identity and projection guides:

`OBJECT_START_X == START_GRADUATION_X`
`OBJECT_END_X == END_GRADUATION_X`
`START_PROJECTION_GUIDE_X == OBJECT_START_X`
`END_PROJECTION_GUIDE_X == OBJECT_END_X`

For ZERO_START_MODE additionally require `OBJECT_START_X == ZERO_GRADUATION_X`; the physical edge cannot substitute for zero if they differ.

Required:
`PROMPT_RULER_SUBDIVISION_COUNT_QA`
`PROMPT_RULER_EDGE_NOT_TICK_QA`
`PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA`
`PROMPT_RULER_ZERO_START_ALIGNMENT_QA`
`PROMPT_RULER_NONZERO_START_RELATION_QA`

## Clock/day-night hard gates

Thai Grade 3 AUTO analog-clock requests resolve to `DAY_NIGHT_PAIR` unless explicit SINGLE intent. Paired mode requires one face, exactly two blank response fields, deterministic day/night mapping, the same hand state for the day/night pair, 12-hour separation modulo 24, and no target values/angles in Student Blueprint. Strict half-hour intent means minute=30 unless the teacher explicitly requests a mixed minute set.

Each high-risk clock item still requires the canonical atomic renderer state: semantic target + exact numeric hand angles + relational verification + item-specific hard negative. Clock hands share one exact pivot.

Continuous hour-hand interpolation is mandatory for all nonzero minutes. Quarter-hour checkpoints are :15=25%, :30=50%, :45=75% of the way to the next hour. For 14:45/2:45 the short hand must be at 82.5° and must not remain on numeral 2.

Applicable clock gates — retained as permanent compatibility/release contracts:

`PROMPT_CLOCK_MODE_RESOLUTION_QA`
`PROMPT_HALF_HOUR_INTENT_QA`
`PROMPT_DAY_NIGHT_MAPPING_QA`
`PROMPT_DAY_NIGHT_SINGLE_FACE_QA`
`PROMPT_DAY_NIGHT_TWO_BLANKS_QA`
`PROMPT_DAY_NIGHT_SAME_HAND_STATE_QA`
`PROMPT_PER_ITEM_RENDER_STATE_QA`
`PROMPT_NONZERO_MINUTE_DISPLACEMENT_QA`
`PROMPT_CLOCK_QUARTER_HOUR_INTERPOLATION_QA`
`PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA`

Any applicable clock gate FAIL/NOT_RUN blocks prompt release.

## Weight-dial hard gates

Canonical 0–5 kg @0.1:

- angle convention `0°=top`, clockwise positive;
- `LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`;
- `CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]`;
- 50 active intervals /51 positions;
- active formula `active_tick_angle(i)=(6*i) mod 360, i=0..50`;
- `INTERVALS_PER_KG=10`;
- 0.5 kg existing position is a required intermediate tick, longer than ordinary 0.1 kg ticks and shorter/weaker than major kg ticks;
- inactive open gap `(300°,360°)` with `INACTIVE_GAP_RADIAL_MARK_COUNT=0`;
- `NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`.

Applicable gates:
`PROMPT_DIAL_LABEL_ORDER_QA`
`PROMPT_DIAL_CANONICAL_LABEL_ANGLE_QA`
`PROMPT_DIAL_COMMON_CENTER_QA`
`PROMPT_DIAL_GAP_RADIAL_MARK_ZERO_QA`
`PROMPT_DIAL_ACTIVE_TICK_SET_QA`
`PROMPT_WEIGHT_PER_KG_SUBDIVISION_QA`
`PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA`.

## Speedometer hard gates

Canonical default:
- 0–120 km/h;
- 240° active open arc starting at240°, clockwise;
- major20/minor10;
- 12 intervals /13 positions;
- 120° inactive gap;
- `target_angle=(240+2*target_kmh) mod 360`;
- 60 km/h→0°→straight up under this family convention;
- `NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`;
- needle radial/collinear from center to target tick.

Applicable gates:
`PROMPT_SPEEDOMETER_TOPOLOGY_QA`
`PROMPT_SPEEDOMETER_INTERVAL_POSITION_COUNT_QA`
`PROMPT_SPEEDOMETER_TARGET_REPRESENTABILITY_QA`
`PROMPT_SPEEDOMETER_ANGLE_MAPPING_QA`
`PROMPT_SPEEDOMETER_NEEDLE_ALIGNMENT_QA`
`PROMPT_SPEEDOMETER_PIVOT_CENTER_QA`
`PROMPT_SPEEDOMETER_RADIAL_COLLINEARITY_QA`
`PROMPT_SPEEDOMETER_INACTIVE_GAP_QA`.

Direct speedometer reading does not silently activate `speed=distance/time`.

## Thermometer hard gates

Canonical 0–50°C @1°C:
- 50 intervals /51 positions;
- 6 major positions at 0,10,20,30,40,50;
- 5 intermediate positions at 5,15,25,35,45;
- 40 ordinary minor positions;
- each 10°C span =10 intervals /9 interior positions;
- bottom-to-top;
- liquid endpoint exactly on target graduation.

Other profiles retain their exact interval/position rules.

Applicable gates:
`PROMPT_THERMOMETER_TOPOLOGY_QA`
`PROMPT_THERMOMETER_INTERVAL_COUNT_QA`
`PROMPT_THERMOMETER_POSITION_COUNT_QA`
`PROMPT_THERMOMETER_TEN_DEGREE_SPAN_QA`
`PROMPT_THERMOMETER_HIERARCHY_COUNT_QA`
`PROMPT_TEMP_TARGET_REPRESENTABILITY_QA`
`PROMPT_TEMP_ENDPOINT_ALIGNMENT_SPEC_QA`
`PROMPT_TEMP_SCALE_DIRECTION_QA`
`PROMPT_TEMP_LABEL_ALIGNMENT_QA`
`PROMPT_NO_BETWEEN_TICKS_QA`.

## Graduated-container hard gates

Canonical 0–1000 mL @50 mL with 100 mL majors:
- 20 intervals /21 positions globally;
- `INTERVALS_PER_100ML=2`;
- `INTERIOR_POSITIONS_PER_100ML_SPAN=1`;
- the sole interior position is +50 mL;
- the +50 mL tick is shorter/weaker and normally unlabeled;
- every adjacent 100 mL major span is independently recounted.

Applicable gates:
`PROMPT_CAPACITY_TOPOLOGY_QA`
`PROMPT_CAPACITY_PER_100ML_SUBDIVISION_QA`
`PROMPT_CAPACITY_LOCAL_SPAN_RECOUNT_QA`
`PROMPT_CAPACITY_MAJOR_MINOR_HIERARCHY_QA`
`PROMPT_LEVEL_ALIGNMENT_SPEC_QA`.

## Protractor hard gates

Canonical 0–180° @1°:
- perfect upper semicircle;
- 180 intervals /181 positions;
- one active numeric scale by default;
- 0° right,90° top,180° left;
- 10° major/5° intermediate/1° minor reuse positions;
- `ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`;
- all ticks/rays radial from common center;
- deterministic geometry;
- no ellipse/perspective/shear/non-uniform stretch;
- radial print-spacing floor 0.60mm → production width>=70mm; 65mm rejected.

Shape-aware page rule: 70mm width means 35mm semicircle body height before labels/answer reserves. Do not reject/approve 2×5 without complete numeric packing proof.

Applicable gates:
`PROMPT_PROTRACTOR_TOPOLOGY_QA`
`PROMPT_PROTRACTOR_BASELINE_QA`
`PROMPT_PROTRACTOR_DIRECTION_QA`
`PROMPT_PROTRACTOR_PRINT_SPACING_QA`
`PROMPT_PROTRACTOR_ACTIVE_SCALE_QA`
`PROMPT_PROTRACTOR_SINGLE_SCALE_QA`
`PROMPT_PROTRACTOR_COMMON_CENTER_QA`
`PROMPT_PROTRACTOR_RADIAL_TICK_QA`
`PROMPT_PROTRACTOR_SHAPE_INTEGRITY_QA`
`PROMPT_PROTRACTOR_RENDER_PATH_QA`
`PROMPT_PROTRACTOR_INTERMEDIATE_HIERARCHY_QA`.

## Physical page-policy provenance

Defaults:
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

One-page PASS requires numeric `PHYSICAL_PAGE_STATE` using shape-aware bounding boxes. `ONE_PAGE_LOCK=ON` requires explicit user provenance. Missing provenance or infeasible locked plan blocks release.

Required page gates:
`PROMPT_PAGE_LOCK_PROVENANCE_QA`
`PROMPT_ONE_PAGE_FEASIBILITY_QA`
`PROMPT_PHYSICAL_WIDTH_FEASIBILITY_QA`
`PROMPT_PHYSICAL_HEIGHT_FEASIBILITY_QA`
`PROMPT_ITEM_BOUNDING_BOX_QA`
`PROMPT_SHAPE_AWARE_BOUNDING_BOX_QA`
`PROMPT_ANSWER_ZONE_PRESERVATION_QA`
`PROMPT_PAGINATION_FALLBACK_QA`
`PROMPT_PAGE_POLICY_SERIALIZATION_QA`
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`
`PROMPT_OUTPUT_MODE_QA`
`PROMPT_FIELD_SEMANTICS_QA`
`PROMPT_QA_EVIDENCE_CONSISTENCY_QA`.

Never shrink/delete/merge scale marks to force one page.

## Prompt completeness

Final prompt is standalone, exact question count, one resolved render path, `OUTPUT_MODE=PROMPT_PACKAGE`, `RENDER_OBJECTIVE=STUDENT_WORKSHEET`, exact student strings/blanks, all per-item state, canonical labels, page provenance/state, scale spec, W10 evidence and review protocol.

Required:
`PROMPT_COPY_READY_QA`
`PROMPT_COMPLETENESS_QA`
`NO_PLACEHOLDER_QA`.

## Release gate semantics

Critical QA is conjunctive, not advisory.

If **any** applicable critical gate is FAIL or NOT_RUN:

`PROMPT_RELEASE=BLOCKED`

W09 never emits `PROMPT_RELEASE=APPROVED` while compiled output violates a gate.

## Phase semantics

W07/W10 prompt audits and renderer self-review are prevention, not artifact proof.

Before actual image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

If actual artifact contains incorrect learner-read scale, local-span subdivision, endpoint reference/projection, label order, pivot/origin, hour-hand interpolation, or distorted protractor:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and defect becomes permanent regression before next accepted release.

## Health check

When user asks for Gem health/self-check, report 2.6.3 release family, W01–W10 compatibility, W10 metrology status, five mandatory profiles, routes, shape-aware render/page rules, regression gate, and prompt/artifact phase semantics.

## Base update policy

W10 is `W10_METROLOGY_ENGINEER`, not a hotfix override. Broad architecture, visibility, worker schema, metrology, geometry or scale-safety changes require canonical SSOT + permanent regression + full rebuild/reinstall.

## Skill Metric Pack release gate

Every request MUST resolve to one or more `SKILL_ID` values and load the corresponding project SSOT under `skill-metrics/`.

Required:
- `SKILL_METRIC_PACK_QA=PASS`
- `SKILL_PROMPT_SCORE>=95`
- no `CRITICAL_ACADEMIC_DEFECT`
- for classroom release, `SKILL_ARTIFACT_SCORE>=95`

For multi-skill worksheets, EVERY active skill must independently pass. Do not average one weak skill into a stronger skill.

A missing/extra scale mark, false pointer/hand/ray/level alignment, wrong reference center/zero, or data-to-visual mismatch is non-compensatory and blocks release.


## Clock minute-driver + canonical one-page hard gate

For analog clocks, release additionally requires:
`PROMPT_CLOCK_MINUTE_HAND_DRIVER_QA=PASS`
`PROMPT_CLOCK_HOUR_DISPLACEMENT_FROM_MINUTE_ANGLE_QA=PASS`

The short hand must be derived from:
`hour_displacement = minute_angle / 12`.

For the canonical Thai P3 DAY_NIGHT_PAIR, 10-item, strict :30 profile with no explicit page/accessibility override, W09 requires the numeric 2×5 A4 portrait proof from `THAI_P3_CLOCK_HALF_HOUR_ONE_PAGE_PROFILE.md`.

When the proof remains valid:
`PROMPT_CLOCK_P3_HALF_HOUR_10_ITEM_ONE_PAGE_QA=PASS`
`PROMPT_CLOCK_P3_HALF_HOUR_2X5_QA=PASS`
`FEASIBILITY_CONFIRMED_ONE_PAGE_LAYOUT_REQUIRED=YES`

A two-page 5+5 result under the unchanged feasible state is a layout defect. It may not be justified merely by `ONE_PAGE_LOCK=OFF`.

Any failed minute-driver or canonical one-page gate blocks prompt release for this profile.
