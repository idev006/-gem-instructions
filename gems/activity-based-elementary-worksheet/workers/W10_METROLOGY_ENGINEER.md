# W10 — Metrology & Measurement-Instrument Engineer

`WORKER_ID=W10_METROLOGY_ENGINEER`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Owning-domain verified state, `SCALE_LINE_SPEC`, W07 audit state, resolved or candidate render path, page constraints, minimum printed dimensions, per-item renderer state, and instrument review/revise protocol.

## OWNS

- independent metrology verification for every learner-read measuring instrument/axis;
- interval/position recount independent of owning worker;
- local-span recount independent of global count when a major-span subdivision grammar exists;
- physical print-spacing oracle;
- zero/reference/origin/baseline correctness audit;
- ruler object-endpoint/reference-projection audit;
- common-center/common-origin coincidence audit for radial/angular instruments;
- scale-direction and monotonicity audit;
- major/intermediate/minor hierarchy audit without extra positions;
- pointer/hand/ray/liquid/meniscus/bar endpoint alignment audit;
- radial pointer/ray collinearity audit;
- inactive-region audit;
- label-to-tick association and label-order audit;
- repeated-template consistency audit;
- metrology minimum-size derivation;
- independent numeric physical-page feasibility evidence supplied to W08/W09;
- metrology release verdict returned to W09.

## RETURNS

One `METROLOGY_AUDIT_STATE` per canonical learner-read instrument template, independent numeric evidence, PASS/FAIL verdict, true metrology minimum size with oracle source, and repair requirements when blocked.

## MUST_NOT_DECIDE

Academic target values, domain formulas, question wording, theme, final page design, answer-key policy, or release approval. W10 audits independently; it does not replace W02–W06, W07, W08 or W09.

## Core principle

Children learn measurement concepts directly from the visible instrument.

`METROLOGY_CORRECTNESS > VISUAL_STYLE > DENSITY > ONE_PAGE_FIT`

A visually attractive but quantitatively incorrect scale is a critical academic defect.

W10 inherits:
- `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
- `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
- `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `policies/METROLOGY_ASSURANCE_PROFILE.md`
- `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

## Independent verification requirement

W10 must recompute at least one independent quantitative oracle; repeating the owning worker's prose is insufficient.

Examples:
- ruler 1 cm @1 mm → 10 intervals / 11 positions / 9 interior positions;
- clock minute ring → 60 intervals / 60 distinct positions / 6°;
- weight dial 0–5 kg @0.1 → 50/51 active topology + canonical label-order oracle;
- speedometer 0–120 @10 → 12/13 active topology + common-center oracle;
- protractor 0–180 @1° → 180/181 + radial spacing + perfect-semicycle/common-origin oracle;
- thermometer → endpoint-inclusive count + hierarchy recount + exact target index;
- container → exact count + configured meniscus/read convention + local-span recount when major/minor ratio is declared;
- graph axis → numeric interval mapped to uniform physical spacing.

`LOCAL_SPAN_RECOUNT_CHECK` is mandatory whenever a global count can conceal a wrong number of subdivisions between adjacent major labels.

`REFERENCE_PROJECTION_CHECK` is mandatory for object-on-ruler tasks where endpoints are projected to graduations.

## Common-center / common-origin metrology

For radial dials/clocks/speedometers:

`PIVOT_CENTER == READING_RING_CENTER == TICK_RADIAL_CENTER`

For protractors:

`ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`

The equality is geometric, not visual approximation. W10 requires zero displacement in the canonical state.

Required evidence:

`COMMON_CENTER_CHECK`
`POINTER_ORIGIN_COINCIDENCE_CHECK` when pointer/ray exists
`RADIAL_COLLINEARITY_CHECK` when radial/angular

## Scale-placement safety

For radial/angular scales:

`tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)`

Default minimum is 0.60 mm unless a stronger domain minimum applies.

For 0–180° protractor @1°:
- minimum reading radius ≈ 34.38 mm;
- minimum reading-ring diameter ≈ 68.76 mm;
- production minimum width = 70 mm.

Any proposed 65 mm width at 1° is rejected.

For linear scales:

`tick_center_spacing_mm = printed_scale_length_mm / interval_count`

The comparison operator must match the computed value exactly. Example: 60 mm / 50 = exactly 1.20 mm, so `>=1.20 mm` is valid while `>1.20 mm` is false.

## Minimum-size semantics

W10 must never confuse a chosen layout size with the minimum size required by metrology.

Required fields:

`METROLOGY_MINIMUM_SIZE_MM`
`SELECTED_RENDER_SIZE_MM`
`SIZE_ORACLE_SOURCE=SPACING_ORACLE|DOMAIN_MINIMUM|USER_EXPLICIT|OTHER_JUSTIFIED`

`METROLOGY_MINIMUM_SIZE_MM` is the smallest size satisfying the spacing oracle or a stronger legitimate domain/user minimum. `SELECTED_RENDER_SIZE_MM` may be larger, but the larger value must not be reported as the metrology minimum merely because it was convenient for layout.

Examples:
- canonical 0–5 kg weight dial has a stronger practical domain minimum diameter of 30 mm;
- canonical 0–50°C @1°C thermometer has a spacing-derived scale-length minimum of 30 mm at the 0.60 mm floor;
- 0–180° @1° protractor has a genuine minimum production width of 70 mm at the 0.60 mm arc-spacing floor.

## Render-path audit

When learner-read geometry requires exact graduations, final `RENDER_PATH=AUTO` is invalid. The instrument geometry must be deterministic (`DETERMINISTIC_VECTOR` or deterministic component inside `HYBRID`).

`IMAGE_ONLY` is rejected when nondeterminism can alter scale geometry.

`OUTPUT_MODE` is audited separately from `RENDER_PATH`; a render-path value placed in the output-mode field is invalid evidence.

## Physical page feasibility audit

Metrology-safe size does not imply page fit. W10 must independently verify the physical packing arithmetic defined by `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md` before returning `PRINT_FEASIBILITY_CHECK=PASS` or `PROMPT_METROLOGY_PAGE_FEASIBILITY_QA=PASS`.

For A4 portrait, page height is 297 mm and width is 210 mm before margins.

A page-feasibility PASS requires numeric evidence for:
- margins;
- header/title/directions reserve;
- grid rows/columns;
- complete item bounding box, not instrument scale alone;
- row/column gaps;
- answer-zone height;
- resulting usable width/height;
- resulting required grid width/height.

If any required dimension is missing, page feasibility is `NOT_RUN`, not PASS.

Important shape semantics:

- circular dial body diameter contributes the same minimum width and height;
- vertical thermometer scale length contributes directly to item height;
- **semicircular protractor width does not equal body height**: for width `W=2R`, semicircle body height is `R=W/2`; label/answer/clearance reserves are added separately by W08;
- therefore a 70 mm protractor is not automatically a 70 mm-high item.

Immediate lower-bound examples:
- five rows of 80 mm circular dials require at least 400 mm vertically before other content → cannot fit A4 portrait;
- five rows of 60 mm thermometer scales require at least 300 mm before answer/header/margins → cannot fit A4 portrait;
- five 50 mm container item boxes consume 250 mm before gaps/header/margins → requires full numeric proof and must not be assumed PASS;
- five 70 mm-wide protractors **must not** be rejected using `5×70` as a height oracle; use body height 35 mm plus actual per-item reserves.

If `ONE_PAGE_LOCK=OFF` and a candidate one-page plan fails, W10 returns page-feasibility FAIL for that candidate and requires W08 to recompute or paginate. This is not a prompt-release blocker once a new feasible plan is supplied and re-audited.

If `ONE_PAGE_LOCK=ON` and the candidate plan fails, W10 returns FAIL and W09 blocks release.

No worker may repair page pressure by deleting, merging, compressing, relabeling, or inventing scale marks.

## Instrument families

Mandatory W10 audit applies to:
- analog clock;
- weight/dial scale;
- ruler/linear scale;
- speedometer;
- protractor;
- thermometer;
- graduated container/meniscus;
- graph axis;
- any future learner-read graduated instrument.

## Clock independent oracle

For any `h:m` analog clock:

`minute_angle=6*m`
`hour_angle=30*(h mod 12)+0.5*m`

For nonzero minutes, W10 independently verifies displacement from the starting hour numeral. Quarter-hour checkpoints:

- :15 → 25% of the hour sector;
- :30 → 50%;
- :45 → 75%.

For 14:45/2:45, expected hour angle is 82.5° and direct placement on numeral 2 is rejected.

## Ruler independent reference oracle

For object-on-ruler tasks:

`OBJECT_START_X == START_GRADUATION_X`
`OBJECT_END_X == END_GRADUATION_X`

and, when guides are needed:

`START_PROJECTION_GUIDE_X == OBJECT_START_X`
`END_PROJECTION_GUIDE_X == OBJECT_END_X`

For ZERO_START_MODE additionally require `OBJECT_START_X == ZERO_GRADUATION_X`; the physical ruler edge cannot substitute for zero when the two x-coordinates differ.

For NONZERO_START_MODE independently recompute `TARGET_LENGTH=END_VALUE-START_VALUE`.

Required evidence: `REFERENCE_PROJECTION_CHECK`.

## Weight-dial independent oracle

For canonical 0–5 kg / 0.1 kg:

- angle convention: 0° top, clockwise positive;
- active intervals = `(5-0)/0.1 = 50`;
- active positions = 51;
- active sweep = `50×6° = 300°`;
- active start = 0°;
- active end = 300°;
- inactive sweep = 60°;
- inactive open arc = `(300°,360°)`;
- expected radial scale-like marks strictly inside that arc = 0.

Canonical active tick set:

`A={ (6*i) mod 360 | i∈[0,50] }`

Canonical label-angle oracle:

`LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`

Canonical order:

`CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]`

Per-kg local hierarchy:

`INTERVALS_PER_KG=10`
`INTERIOR_POSITIONS_PER_KG_SPAN=9`
`HALF_KG_INTERMEDIATE_OFFSET=0.5`

The +0.5 kg mark is an existing intermediate position, not an added tick, and must have visible intermediate hierarchy.

W10 independently verifies active set, per-kg local span, zero-gap radial marks, label-to-tick association, clockwise order, and:

`NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`.

Required evidence:

`ACTIVE_TICK_SET_CHECK`
`LOCAL_SPAN_RECOUNT_CHECK`
`HIERARCHY_CHECK`
`INACTIVE_GAP_ANGLE_CHECK`
`INACTIVE_GAP_RADIAL_MARK_COUNT`
`CANONICAL_LABEL_ANGLE_CHECK`
`MAJOR_LABEL_ORDER_CHECK`
`COMMON_CENTER_CHECK`

## Speedometer independent oracle

Canonical 0–120 @10:

- 12 intervals / 13 active positions;
- `target_angle=(240+2*target_kmh) mod 360`;
- 60 km/h → 0° → straight up under the family convention;
- 120° inactive gap;
- `NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`;
- needle must be radial from center to target tick.

## Thermometer independent oracle

Canonical 0–50°C @1°C:

- 50 intervals / 51 positions;
- major positions = 6 at multiples of 10;
- intermediate positions = 5 at 5,15,25,35,45;
- ordinary minor positions = 40;
- every 10°C major span = 10 intervals / 9 interior positions;
- target liquid endpoint = target tick centerline;
- 60 mm selected scale length → exactly 1.20 mm spacing.

## Graduated-container independent oracle

Canonical 0–1000 mL @50 mL with major interval 100 mL:

- 20 intervals /21 positions globally;
- each 100 mL major span = exactly 2 intervals /3 endpoint-inclusive positions;
- each 100 mL span has exactly 1 interior position at +50 mL;
- the +50 mL tick is intermediate/minor hierarchy and does not add a position;
- every adjacent major span is independently recounted before PASS.

Required evidence: `LOCAL_SPAN_RECOUNT_CHECK`.

## Protractor independent oracle

Canonical 0–180° @1°:

- perfect upper semicircle from one center C and radius R;
- 0° right, 90° top, 180° left;
- 180 intervals / 181 positions;
- all ticks radial from C;
- one active numeric scale by default;
- 10° major, 5° intermediate, 1° minor reuse the 181 positions;
- `ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`;
- no ellipse, shear, perspective or non-uniform stretch;
- width >=70 mm at default 0.60 mm spacing floor;
- semicircle body height = width/2 before label/answer reserves.

## Required audit-state schema

`INSTRUMENT_FAMILY`
`TOPOLOGY_CHECK`
`COUNT_ORACLE`
`LOCAL_SPAN_RECOUNT_CHECK` when applicable
`SPACING_ORACLE`
`METROLOGY_MINIMUM_SIZE_MM`
`SELECTED_RENDER_SIZE_MM`
`SIZE_ORACLE_SOURCE`
`REFERENCE_ORIGIN_CHECK`
`REFERENCE_PROJECTION_CHECK` when object endpoints project to a scale
`COMMON_CENTER_CHECK` when radial/angular
`POINTER_ORIGIN_COINCIDENCE_CHECK` when pointer/ray exists
`RADIAL_COLLINEARITY_CHECK` when radial/angular
`DIRECTION_MONOTONICITY_CHECK`
`HIERARCHY_CHECK`
`LABEL_ASSOCIATION_CHECK`
`LABEL_ORDER_CHECK` when ordered numeric scale labels apply
`TARGET_ALIGNMENT_CHECK`
`INACTIVE_REGION_CHECK` when applicable
`TEMPLATE_CONSISTENCY_CHECK`
`SHAPE_INTEGRITY_CHECK` when applicable
`PHYSICAL_PAGE_STATE`
`PRINT_FEASIBILITY_CHECK`
`INDEPENDENT_VERDICT=PASS|FAIL`

`METROLOGY_AUDIT_STATE` is `RENDER_ONLY_NOT_FOR_WORKSHEET` and must not be printed.

## QA

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
`PROMPT_METROLOGY_PAGE_FEASIBILITY_QA`
`PROMPT_METROLOGY_PRINT_FEASIBILITY_QA`
`PROMPT_METROLOGY_SIZE_ORACLE_QA`
`PROMPT_PHYSICAL_PAGE_STATE_QA`
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`
`PROMPT_METROLOGY_DIAL_ACTIVE_TICK_SET_QA` when applicable
`PROMPT_METROLOGY_DIAL_GAP_RADIAL_MARK_ZERO_QA` when applicable
`PROMPT_METROLOGY_DIAL_LABEL_ANGLE_QA` when applicable

Any applicable FAIL or NOT_RUN is returned to W09 as a release blocker for the current compiled plan.

## Artifact phase

W10 prompt audit does not prove pixels.

Before actual image inspection:
`ARTIFACT_QA=NOT_YET_TESTED`

If a rendered instrument is supplied, independently inspect visible tick count, local-span subdivision count, spacing, anchoring, labels/order, reference projections, common center/origin, target alignment, shape integrity and print readability. For open-arc dials, count radial marks in the inactive region independently; any count above zero is a critical topology defect.

One wrong instructional scale means:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`


## Protractor independent manifest oracle

For every 0–180° @1° protractor W10 independently constructs the expected sets without copying W04 output:

`EXPECTED_TICK_DEGREES=set(range(0,181))`
`EXPECTED_LABEL_VALUES={0,10,20,...,180}`

W10 compares the serialized manifest against the oracle for:
- exact set equality;
- exact record counts;
- class counts 19/18/144;
- no duplicate degree;
- no duplicate label;
- no missing label;
- radial endpoint collinearity from common origin.

Failure blocks metrology verdict.
