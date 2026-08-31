# Metrology Assurance Profile — Learner-Read Measurement Instruments

Version: 1.2.0
Status: Mandatory independent measurement-safety contract
Compatible Gem baseline: 2.6.x
Independent owner: `W10_METROLOGY_ENGINEER`

## Mission

A learner-read measuring instrument is not decorative art. Its visible graduations, labels, reference line, pointer/hand/ray/liquid endpoint, common center/origin, shape and geometric spacing are academic data from which a child learns measurement concepts.

`ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER`

This profile provides an independent second audit after the owning academic worker and W07 geometry audit. W10 does not create target values or override domain formulas. W10 independently verifies that the specified instrument can physically and visually encode those values correctly at final print size.

This profile inherits `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md` for shape-aware page-packing evidence.

## Mandatory dual-audit chain

For every learner-read instrument or numeric axis:

`OWNING DOMAIN → W07 INSTRUMENT GEOMETRY AUDIT → W10 INDEPENDENT METROLOGY AUDIT → W08 RENDER/LAYOUT → W09 RELEASE`

W07 and W10 must not merely repeat the same assertion. W10 must independently recompute/recount at least one quantitative oracle appropriate to the instrument.

## Universal metrology audit

W10 independently checks:

1. topology family and active range;
2. exact interval count;
3. exact physical position count;
4. endpoint/wrap semantics;
5. zero/reference/baseline/origin correctness;
6. common-center/common-origin coincidence for radial/angular instruments;
7. scale direction and monotonicity;
8. uniform geometric spacing for equal value intervals;
9. final printed tick-center spacing;
10. major/intermediate/minor hierarchy without creating extra positions;
11. tick anchoring to one authoritative baseline/ring/arc/axis;
12. label-to-tick association, clearance and numeric order;
13. target representability in discrete-reading mode;
14. pointer/hand/ray/level/meniscus/bar endpoint alignment;
15. radial pointer/ray collinearity from the common center;
16. inactive-region integrity;
17. absence of decoration that can be mistaken for a graduation;
18. repeated-template consistency;
19. shape/aspect-ratio integrity without perspective/shear/non-uniform scaling;
20. photocopy/print distinguishability;
21. true metrology minimum size and its oracle source;
22. selected render size distinguished from minimum size;
23. numeric dimensional feasibility under complete shape-aware page constraints.

## Independent quantitative oracles

### Linear endpoint-inclusive scales

`intervals=(max-min)/minor_interval`
`positions=intervals+1`
`interior=max(positions-2,0)`

Canonical ruler 1 cm @1 mm:
`10 intervals / 11 positions / 9 interior positions`.
The physical ruler edge is not an extra graduation.

For printed linear scale length `L`:
`tick_center_spacing_mm = L / intervals`.
The comparison operator in prose must agree with the computed result.

Canonical thermometer 0–50°C @1°C:
- 50 intervals / 51 positions;
- 6 major positions at multiples of10;
- 5 intermediate positions at 5,15,25,35,45;
- 40 ordinary minor positions;
- each 10°C span =10 intervals /9 interior positions;
- spacing-derived minimum length at 0.60mm floor =30mm.

For selected 60mm length: `60/50=1.20mm` exactly. `>1.20mm` is false.

### Cyclic full-circle scales

N equal intervals have N distinct physical positions because the wrap endpoint is shared.

Canonical clock minute ring:
`60 intervals / 60 distinct positions / 6° per interval`.
Clock hands share one exact pivot.

### Open-arc bounded scales

`active_positions=active_intervals+1`.
No value tick or scale-like radial pseudo-tick may appear in inactive gap unless owning domain explicitly defines one.

Canonical weight dial 0–5 kg @0.1 kg:
- angle convention 0° top, clockwise positive;
- 50 active intervals /51 positions;
- active positions `angle(i)=6*i`, i=0..50;
- labels `{0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`;
- clockwise label order `[0,1,2,3,4,5]`;
- inactive open gap `(300°,360°)`;
- zero gap radial marks;
- needle pivot equals reading-ring center.

Canonical speedometer 0–120 km/h @10 km/h:
- 12 active intervals /13 positions;
- `target_angle=(240+2*target_kmh) mod 360`;
- 60 km/h→0°→straight up under its angle convention;
- 120° inactive gap;
- needle pivot equals reading-ring center.

### Angular scale print-spacing oracle

For radial/angular scales:

`tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)`

Default floor: `MIN_TICK_CENTER_SPACING_MM >= 0.60`.

Canonical semicircular protractor 0–180° @1° requires:
`reading_radius >=34.38mm`, reading-ring diameter >=68.76mm; production width=70mm.

A 65mm-wide protractor fails the default spacing oracle.

### Protractor shape/origin oracle

For perfect upper semicircle width `W=2R`:

`PROTRACTOR_CENTER=(cx,cy)`
`BASELINE_LEFT=(cx-R,cy)`
`BASELINE_RIGHT=(cx+R,cy)`
`OUTER(theta)=(cx+R*cos(theta), cy-R*sin(theta))`

0° right, 90° top, 180° left.

Required identity:

`ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`

Every graduation/ray is radial from this center. One active numeric scale is default. No ellipse, shear, perspective, non-uniform stretch or warped arc.

Shape-aware body dimensions:

`PROTRACTOR_BODY_WIDTH=W`
`PROTRACTOR_BODY_HEIGHT=R=W/2`

Thus 70mm width gives 35mm semicircle body height before label/answer reserves. Width must never be substituted as vertical body height in page packing.

### Graduated container

Exact interval/position count plus one declared read convention (`SIMPLE_FLAT`, concave-bottom, or convex-top). Read point maps exactly to target.

### Graph axis

Equal numeric increments map to equal physical distances. Bar/data endpoints map to canonical dataset and configured scale.

## Instrument-family audit matrix

W10 audit is mandatory for analog clocks, weight/spring/dial scales, rulers, speedometers, protractors, thermometers, graduated containers/meniscus, learner-read graph axes, and any future graduated visual instrument.

## Render-path safety

If scale correctness depends on exact geometry, `RENDER_PATH=AUTO` may exist only before resolution. Final prompt resolves to `DETERMINISTIC_VECTOR` or `HYBRID` with deterministic instrument geometry. `IMAGE_ONLY` is forbidden when nondeterminism can alter learner-read graduations.

`OUTPUT_MODE` is separate; a render-path enum in `OUTPUT_MODE` is invalid.

Gates:
`PROMPT_METROLOGY_RENDER_PATH_QA`
`PROMPT_OUTPUT_MODE_QA`
`PROMPT_FIELD_SEMANTICS_QA`.

## Minimum-size semantics

W10 output distinguishes:

`METROLOGY_MINIMUM_SIZE_MM`
`SELECTED_RENDER_SIZE_MM`
`SIZE_ORACLE_SOURCE`

A selected size larger than necessary may not be relabeled as metrology minimum without stronger domain/user requirement.

## Page-pressure and physical packing rule

Tick-spacing PASS does **not** imply page-feasibility PASS.

Before page feasibility PASS, W10 provides complete numeric `PHYSICAL_PAGE_STATE` from `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`, including page dimensions, margins, header/title/directions, rows/columns, complete shape-aware item bounding boxes, gaps and answer zones.

For A4 portrait: width210mm, height297mm.

Examples:
- circular dial selected diameter80mm ×5 rows → circular bodies alone400mm high → impossible;
- thermometer selected scale length60mm ×5 rows → scale bodies alone300mm → impossible before other content;
- five container item boxes of50mm →250mm before other reserves → requires full proof;
- protractor width70mm means body height35mm, **not70mm**; five such bodies=175mm before labels/answers/gaps/header. The complete 2×5 plan must be numerically proved, not automatically rejected or accepted.

If candidate plan fails and `ONE_PAGE_LOCK=OFF`, W08 paginates/recomputes. If lock ON conflicts with safe geometry, prompt release is blocked rather than degrading instrument.

Gate: `PROMPT_METROLOGY_PAGE_FEASIBILITY_QA`.

## Mandatory W10 output

For each canonical learner-read template, W10 returns `METROLOGY_AUDIT_STATE` containing:

- `INSTRUMENT_FAMILY`
- `TOPOLOGY_CHECK`
- `COUNT_ORACLE`
- `SPACING_ORACLE`
- `METROLOGY_MINIMUM_SIZE_MM`
- `SELECTED_RENDER_SIZE_MM`
- `SIZE_ORACLE_SOURCE`
- `REFERENCE_ORIGIN_CHECK`
- `COMMON_CENTER_CHECK` when radial/angular
- `POINTER_ORIGIN_COINCIDENCE_CHECK` when pointer/ray exists
- `RADIAL_COLLINEARITY_CHECK` when radial/angular
- `DIRECTION_MONOTONICITY_CHECK`
- `HIERARCHY_CHECK`
- `LABEL_ASSOCIATION_CHECK`
- `LABEL_ORDER_CHECK` when ordered labels apply
- `TARGET_ALIGNMENT_CHECK`
- `INACTIVE_REGION_CHECK` when applicable
- `SHAPE_INTEGRITY_CHECK` when applicable
- `PHYSICAL_PAGE_STATE`
- `PRINT_FEASIBILITY_CHECK`
- `INDEPENDENT_VERDICT=PASS|FAIL`

Audit state is teacher/runtime metadata and never printed on student worksheet.

## Mandatory QA gates

`PROMPT_METROLOGY_AUDIT_REQUIRED_QA`
`PROMPT_METROLOGY_INDEPENDENCE_QA`
`PROMPT_METROLOGY_INTERVAL_COUNT_QA`
`PROMPT_METROLOGY_POSITION_COUNT_QA`
`PROMPT_METROLOGY_REFERENCE_QA`
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
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED` for current compiled plan.

## Artifact boundary

W10 prompt verification does not prove downstream pixels. Before actual image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

When artifact is supplied, inspect each learner-read instrument against same metrology oracles, including common center/origin, label order, hierarchy and shape integrity. One wrong scale blocks classroom release and becomes permanent regression.
