# Metrology Assurance Profile — Learner-Read Measurement Instruments

Version: 1.1.0
Status: Mandatory independent measurement-safety contract
Compatible Gem baseline: 2.6.x
Independent owner: `W10_METROLOGY_ENGINEER`

## Mission

A learner-read measuring instrument is not decorative art. Its visible graduations, labels, reference line, pointer/hand/ray/liquid endpoint and geometric spacing are academic data from which a child learns measurement concepts.

`ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER`

This profile provides an independent second audit after the owning academic worker and W07 geometry audit. W10 does not create target values or override domain formulas. W10 independently verifies that the specified instrument can physically and visually encode those values correctly at final print size.

This profile inherits `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md` for page-packing evidence.

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
6. scale direction and monotonicity;
7. uniform geometric spacing for equal value intervals;
8. final printed tick-center spacing;
9. major/intermediate/minor hierarchy without creating extra positions;
10. tick anchoring to one authoritative baseline/ring/arc/axis;
11. label-to-tick association and clearance;
12. target representability in discrete-reading mode;
13. pointer/hand/ray/level/meniscus/bar endpoint alignment;
14. inactive-region integrity;
15. absence of decoration that can be mistaken for a graduation;
16. repeated-template consistency;
17. photocopy/print distinguishability;
18. true metrology minimum size and its oracle source;
19. selected render size distinguished from minimum size;
20. numeric dimensional feasibility under complete page constraints.

## Independent quantitative oracles

### Linear endpoint-inclusive scales

`intervals=(max-min)/minor_interval`
`positions=intervals+1`
`interior=max(positions-2,0)`

Canonical ruler 1 cm @1 mm:
`10 intervals / 11 positions / 9 interior positions`.
The physical ruler edge is not an extra graduation.

For a printed linear scale of length `L`:
`tick_center_spacing_mm = L / intervals`.
The comparison operator in prose must agree with the computed result.

### Cyclic full-circle scales

N equal intervals have N distinct physical positions because the wrap endpoint is shared.

Canonical clock minute ring:
`60 intervals / 60 distinct positions / 6° per interval`.

### Open-arc bounded scales

`active_positions=active_intervals+1`.
No value tick may appear in the inactive gap unless the owning domain explicitly defines one.

Canonical weight dial 0–5 kg @0.1 kg:
`50 active intervals / 51 active positions`.

Canonical speedometer 0–120 km/h @10 km/h:
`12 active intervals / 13 active positions`.

### Angular scale print-spacing oracle

For radial/angular scales:

`tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)`

The result must satisfy the configured print floor. Default:
`MIN_TICK_CENTER_SPACING_MM >= 0.60`.

Canonical semicircular protractor 0–180° @1° therefore requires:
`reading_radius >= 34.38 mm`
and a reading-ring diameter of at least `68.76 mm`; production minimum is `70 mm`.

### Thermometer / vertical linear scale

`intervals=(max-min)/minor_interval`, endpoint-inclusive positions, monotonic vertical mapping, exact target representability, and liquid endpoint on the target graduation centerline.

For 0–50°C @1°C using a 60 mm printed scale:
`60/50 = 1.20 mm` exactly. Valid statements include `spacing=1.20 mm`, `spacing>=1.20 mm`, or `spacing>0.60 mm`; `spacing>1.20 mm` is false for that exact geometry.

### Graduated container

Exact interval/position count plus a single declared read convention (`SIMPLE_FLAT`, concave-bottom, or convex-top as configured). The level/meniscus read point must map exactly to the target value.

### Graph axis

Equal numeric increments must map to equal physical distances. Bar/data endpoints must map to the canonical dataset and configured axis scale.

## Instrument-family audit matrix

W10 audit is mandatory for:

- analog clocks;
- weight/spring/dial scales;
- rulers and linear scales;
- speedometers;
- semicircular and full-circle protractors;
- thermometers;
- graduated cylinders/containers and meniscus tasks;
- learner-read graph axes;
- any future instrument where a student reads a graduated visual scale.

## Render-path safety

If scale correctness depends on exact geometry, `RENDER_PATH=AUTO` may exist only before resolution. The final prompt must resolve to `DETERMINISTIC_VECTOR` or `HYBRID` with deterministic instrument geometry. `IMAGE_ONLY` is forbidden when nondeterministic drawing can alter learner-read graduation geometry.

`OUTPUT_MODE` is a separate contract field; a render-path enum in `OUTPUT_MODE` is invalid.

Gates:
`PROMPT_METROLOGY_RENDER_PATH_QA`
`PROMPT_OUTPUT_MODE_QA`
`PROMPT_FIELD_SEMANTICS_QA`.

## Minimum-size semantics

W10 output must distinguish:

`METROLOGY_MINIMUM_SIZE_MM`
`SELECTED_RENDER_SIZE_MM`
`SIZE_ORACLE_SOURCE`

A selected size larger than necessary may not be relabeled as the metrology minimum without a stronger domain or user-explicit requirement.

## Page-pressure and physical packing rule

Page count, theme, card density and decoration may never force an instrument below its audited minimum geometry.

More importantly, tick-spacing PASS does **not** imply page-feasibility PASS.

Before `PROMPT_METROLOGY_PAGE_FEASIBILITY_QA=PASS`, W10 must provide the complete numeric `PHYSICAL_PAGE_STATE` required by `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`, including page dimensions, margins, header/title/directions reserve, rows/columns, complete item bounding boxes, gaps and answer zones.

For A4 portrait:
- width = 210 mm
- height = 297 mm

Immediate lower-bound examples:
- 5 × 80 mm dial rows = 400 mm → impossible on A4 portrait even before other content;
- 5 × 70 mm protractor rows = 350 mm → impossible;
- 5 × 60 mm thermometer scale rows = 300 mm → impossible before other content;
- 5 × 50 mm container item boxes = 250 mm → remaining content must be explicitly budgeted, not assumed.

If a candidate plan fails and `ONE_PAGE_LOCK=OFF`, W08 must paginate and return a new physical packing state for re-audit.

If `ONE_PAGE_LOCK=ON` conflicts with safe geometry, prompt release is blocked rather than shrinking, deleting, merging or compressing graduations.

Gate:
`PROMPT_METROLOGY_PAGE_FEASIBILITY_QA`.

## Mandatory W10 output

For each canonical learner-read instrument template, W10 returns an independent `METROLOGY_AUDIT_STATE` containing:

- `INSTRUMENT_FAMILY`
- `TOPOLOGY_CHECK`
- `COUNT_ORACLE`
- `SPACING_ORACLE`
- `METROLOGY_MINIMUM_SIZE_MM`
- `SELECTED_RENDER_SIZE_MM`
- `SIZE_ORACLE_SOURCE`
- `REFERENCE_ORIGIN_CHECK`
- `TARGET_ALIGNMENT_CHECK`
- `LABEL_ASSOCIATION_CHECK`
- `INACTIVE_REGION_CHECK` when applicable
- `PHYSICAL_PAGE_STATE`
- `PRINT_FEASIBILITY_CHECK`
- `INDEPENDENT_VERDICT=PASS|FAIL`

The audit state is teacher/runtime metadata and must never be printed on the student worksheet.

## Mandatory QA gates

`PROMPT_METROLOGY_AUDIT_REQUIRED_QA`
`PROMPT_METROLOGY_INDEPENDENCE_QA`
`PROMPT_METROLOGY_INTERVAL_COUNT_QA`
`PROMPT_METROLOGY_POSITION_COUNT_QA`
`PROMPT_METROLOGY_REFERENCE_QA`
`PROMPT_METROLOGY_SPACING_ORACLE_QA`
`PROMPT_METROLOGY_HIERARCHY_QA`
`PROMPT_METROLOGY_LABEL_ASSOCIATION_QA`
`PROMPT_METROLOGY_TARGET_ALIGNMENT_QA`
`PROMPT_METROLOGY_INACTIVE_REGION_QA` when applicable
`PROMPT_METROLOGY_TEMPLATE_CONSISTENCY_QA`
`PROMPT_METROLOGY_RENDER_PATH_QA`
`PROMPT_METROLOGY_SIZE_ORACLE_QA`
`PROMPT_METROLOGY_PAGE_FEASIBILITY_QA`
`PROMPT_METROLOGY_PRINT_FEASIBILITY_QA`
`PROMPT_PHYSICAL_PAGE_STATE_QA`
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED` for the current compiled plan.

## Artifact boundary

W10 prompt-phase verification does not prove downstream pixels. Before actual image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

When an artifact is supplied, each learner-read instrument must be visually inspected against the same metrology oracles. One wrong scale blocks classroom release and becomes a permanent regression.
