# Actual Instrument Geometry Defects — 2026-08-31

Status: PERMANENT NEGATIVE EVIDENCE
Severity: `P0_CRITICAL_ACADEMIC`
Source: user-supplied rendered worksheet artifacts
Affected families: weight dial, speedometer, thermometer, protractor

## Purpose

The supplied artifacts demonstrated that numerically plausible prompt state can still produce learner-read instruments that are academically wrong. These defects are permanent negative evidence and must remain protected by executable regressions.

`ONE WRONG INSTRUCTIONAL GEOMETRY = CLASSROOM RELEASE BLOCKER`

## Defect A — Speedometer pivot not at dial center

Observed: the needle pivot was visibly displaced from the center used by the active arc/tick ring. Some needle tips still visually touched intended ticks.

Why critical: a speedometer needle is a radial pointer. Touching a target tick from the wrong origin is not the same geometry and can teach a false dial construction.

Required canonical identity:

`DIAL_CENTER=(cx,cy)`
`READING_RING_CENTER=DIAL_CENTER`
`NEEDLE_PIVOT=DIAL_CENTER`
`distance(NEEDLE_PIVOT,DIAL_CENTER)=0`

The needle must be collinear with the center-to-target-tick radius.

Artifact gates:
`ARTIFACT_SPEEDOMETER_PIVOT_CENTER_QA`
`ARTIFACT_SPEEDOMETER_RADIAL_COLLINEARITY_QA`

Any visible pivot displacement: `ARTIFACT_QA=FAIL` and `CLASSROOM_RELEASE=BLOCKED`.

## Defect B — Weight-dial major label order/orientation

Observed: a 0–5 kg dial presented the numeric labels in an order/orientation inconsistent with the intended elementary top-zero clockwise teaching scale.

The later full-SSOT audit also discovered that the repository's previous rotated canonical (`0@240°...`) was itself inappropriate for the intended classroom template. The repository canonical is therefore corrected; this is a root-cause SSOT correction, not a renderer-only patch.

Correct canonical:

`ANGLE_CONVENTION=0°_TOP_CLOCKWISE_POSITIVE`
`LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`
`CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]`
`active_tick_angle(i)=(6*i) mod 360, i=0..50`
`INACTIVE_GAP=(300°,360°)`
`INACTIVE_GAP_RADIAL_MARK_COUNT=0`
`NEEDLE_PIVOT=DIAL_CENTER`

Artifact gates:
`ARTIFACT_DIAL_LABEL_ORDER_QA`
`ARTIFACT_DIAL_CANONICAL_LABEL_ANGLE_QA`
`ARTIFACT_DIAL_COMMON_CENTER_QA`
`ARTIFACT_DIAL_INACTIVE_GAP_QA`

## Defect C — Thermometer 0–50°C @1°C scale construction

Observed: the rendered thermometer looked thermometer-like, but the graduation structure was not sufficiently trustworthy as a 1°C scale. Major/intermediate/minor hierarchy and the exact subdivisions within each 10°C span were visually unsafe.

Correct canonical:

`EXPECTED_INTERVAL_COUNT=50`
`EXPECTED_POSITION_COUNT=51`
`MAJOR_POSITIONS={0,10,20,30,40,50}` → 6
`INTERMEDIATE_POSITIONS={5,15,25,35,45}` → 5
`ORDINARY_MINOR_POSITION_COUNT=40`

For every 10°C span:

`INTERVALS_PER_10C=10`
`INTERIOR_POSITIONS_PER_10C=9`
`INTERMEDIATE_POSITIONS_PER_10C=1`
`ORDINARY_MINOR_POSITIONS_PER_10C=8`

Hierarchy classes reuse the same physical 51 positions; no extra tick is created by styling.

Liquid endpoint must intersect the exact target graduation centerline.

Artifact gates:
`ARTIFACT_THERMOMETER_INTERVAL_COUNT_QA`
`ARTIFACT_THERMOMETER_POSITION_COUNT_QA`
`ARTIFACT_THERMOMETER_HIERARCHY_COUNT_QA`
`ARTIFACT_THERMOMETER_TEN_DEGREE_SPAN_QA`
`ARTIFACT_THERMOMETER_ENDPOINT_ALIGNMENT_QA`

## Defect D — Protractor distorted / ambiguous scale

Observed: the protractor drawing was visually warped/uneven and used competing numeric scales, making the reading geometry and direction unnecessarily ambiguous. The scale/tick construction could not be treated as a perfect deterministic semicircle.

Correct canonical for the elementary single-scale 0–180° @1° profile:

`PROTRACTOR_CENTER=(cx,cy)`
`PROTRACTOR_RADIUS=R`
`BASELINE_LEFT=(cx-R,cy)`
`BASELINE_RIGHT=(cx+R,cy)`
`OUTER(theta)=(cx+R*cos(theta),cy-R*sin(theta))`

- perfect upper semicircle;
- 0° right, 90° top, 180° left;
- 180 intervals /181 positions;
- 10° major, 5° intermediate, 1° minor;
- one active numeric scale by default;
- `ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`;
- every tick and target ray radial from this center;
- no ellipse, perspective, shear, non-uniform scaling, or warped local arc;
- production width >=70 mm at the default 0.60 mm tick-spacing floor.

Artifact gates:
`ARTIFACT_PROTRACTOR_SHAPE_INTEGRITY_QA`
`ARTIFACT_PROTRACTOR_COMMON_CENTER_QA`
`ARTIFACT_PROTRACTOR_RADIAL_TICK_QA`
`ARTIFACT_PROTRACTOR_SINGLE_SCALE_QA`
`ARTIFACT_PROTRACTOR_INTERVAL_POSITION_COUNT_QA`

## Page-box correction discovered during audit

A semicircular protractor's horizontal width is not its vertical body height.

For `W=2R`:

`PROTRACTOR_BODY_WIDTH=W`
`PROTRACTOR_BODY_HEIGHT=R=W/2`

Therefore a 70 mm-wide protractor has a 35 mm semicircle body. The previous inference `5×70mm=350mm required vertical body height` was wrong and is now forbidden. Page feasibility must add actual labels, answer zone, and clearance to the 35 mm body, then calculate the complete shape-aware page state.

## Permanent regression discipline

Future refactors must preserve all corrected positive oracles and actual negative evidence. A test must not be weakened to `looks correct` or a generic aesthetic check.

Before corrected artifacts are visually inspected:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

For the actual supplied defective artifacts:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`
