# W07 — Instrument Geometry Auditor

`WORKER_ID=W07_INSTRUMENT_AUDITOR`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Owning-worker template, topology, active range, intervals, target mapping, minimum readable size, `SCALE_LINE_SPEC`, per-item renderer state, and renderer self-review protocol requirements.

## OWNS

- shared instrument topology invariants
- interval vs position distinction
- target representability audit
- target alignment-spec audit
- no-missing/no-extra graduation specification
- scale-line integrity audit
- template-lock audit
- canonical-template lock audit
- common-center/common-origin geometry audit
- label-order/label-to-major-tick audit
- geometry-vs-decoration separation
- protractor baseline/scale-direction/shape-integrity audit
- renderer self-review checklist definition
- independent recount oracle for learner-read scales
- local-span recount audit where global counts can hide subdivision errors
- ruler endpoint projection/reference audit
- artifact inspection checklist definition

## RETURNS

Prompt-phase geometry audit, required hard constraints, mandatory review/revise checklist, required cross-domain QA gates, artifact checklist.

## MUST_NOT_DECIDE

Academic target values, domain formulas owned by W02–W06, final layout, render path, Thai wording, answer-key policy.

## Core principle

If the learner must read it, geometry is academic data:

`INSTRUMENT_GEOMETRY > CONTEXT_ART > DECORATION`

All learner-read scales inherit:

- `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
- `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `policies/METROLOGY_ASSURANCE_PROFILE.md`

## Topology families

### LINEAR_ENDPOINT_INCLUSIVE
`intervals=(max-min)/d`
`positions=intervals+1`
`interior_positions=max(positions-2,0)`

Canonical ruler 1 cm @1 mm = 10 intervals / 11 positions / 9 interior positions. The physical ruler edge is not an extra graduation.

### CYCLIC_FULL_CIRCLE
Domain defines N intervals and N distinct positions. Shared wrap endpoint is not duplicated.

### OPEN_ARC_BOUNDED
Domain defines active intervals and endpoint-inclusive positions. Inactive/non-scale region contains zero value ticks or scale-like pseudo-ticks unless explicitly defined otherwise.

Applies to canonical weight dials and speedometers.

### PROTRACTOR_HALF_CIRCLE
For 0–180° and minor interval d:

`intervals=180/d`
`positions=intervals+1`

At 1°: 180 intervals / 181 positions.

Audit exact common origin, selected 0° baseline, target ray, active scale direction, radial tick construction, perfect semicircle shape, no perspective/non-uniform distortion, and no decorative competing rays.

## Common-center / common-origin invariant

For radial dials/clocks/speedometers:

`PIVOT_CENTER == READING_RING_CENTER == TICK_RADIAL_CENTER`

For protractors:

`ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`

Pointer/ray geometry is valid only if it begins at the exact common center and is collinear with the radius to its target graduation.

Any independent pivot/origin translation is `CRITICAL_ACADEMIC`.

## General invariants

- exact active range and exact interval/position count;
- uniform spacing and monotonic direction;
- major/intermediate/minor hierarchy without extra positions;
- local-span topology must agree with global topology when a major span has a declared subdivision grammar;
- common baseline/ring/arc anchoring;
- common center/origin for radial/angular geometry;
- labels aligned to intended marks with clearance and correct value order;
- no missing, duplicate, merged, floating, detached or extra graduation;
- no instructional tick in inactive/non-scale region;
- exact target on valid graduation in exact-reading mode;
- one canonical template per repeated scale type;
- preserved aspect ratio and no perspective/non-uniform distortion;
- no crop/overlap;
- no decorative pointer/tick/ray/grid-like competing mark.

## High-risk item audit

Every learner-read visual item requires an atomic renderer-only state:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL/ENDPOINT + RELATIONAL WORDING + ITEM-SPECIFIC HARD_NEGATIVE`

Every high-risk item therefore carries an explicit **item-specific hard negative** as part of the same atomic state; the underscore form above is the machine-stable key and this phrase is the semantic contract.

For radial/angular instruments the state must also preserve the authoritative center/origin identity.

Semantic-only instructions such as `show 10:30`, `show 70°`, `show 2.4 kg`, or `show 60 km/h` are insufficient.

Renderer state must be marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

## Mandatory renderer review/revise protocol

W07 defines the canonical checklist consumed by W08/W09:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

For every learner-read instrument the renderer-side prompt must require:

1. independent recount of intervals/positions;
2. independent local-span recount when owning domain defines one;
3. check of baseline/ring/arc anchoring;
4. check common center/origin when radial/angular;
5. check uniform spacing and major/intermediate/minor hierarchy;
6. check label alignment, clearance and monotonic order;
7. no missing/extra/merged/floating tick;
8. physical-edge-not-a-tick check for ruler/linear scales;
9. endpoint projection/reference check for object-on-ruler tasks;
10. target pointer/hand/ray/level/endpoint alignment;
11. radial pointer/ray collinearity from the common center;
12. inactive-region and decoration-isolation check;
13. template shape/aspect-ratio consistency;
14. repair/regenerate and full recheck on any mismatch.

A vague `looks correct` check is insufficient.

## Ruler reference/projection audit

For object-on-ruler measurement:

`OBJECT_START_X == START_GRADUATION_X`
`OBJECT_END_X == END_GRADUATION_X`
`START_PROJECTION_GUIDE_X == OBJECT_START_X`
`END_PROJECTION_GUIDE_X == OBJECT_END_X`

Projection guides must be thin dashed vertical helper lines, perpendicular to the ruler baseline, visually distinct from ticks and excluded from graduation counts.

For `ZERO_START_MODE` additionally require:

`OBJECT_START_X == ZERO_GRADUATION_X`

The physical ruler edge is not accepted as the start reference when it differs from the zero graduation.

For `NONZERO_START_MODE`, W07 verifies both guides and the visual relation supporting `END_VALUE - START_VALUE`.

## Minimum size

Owning worker may define a stronger minimum. If layout pressure threatens graduation distinguishability, reduce decoration before instrument size. Never merge/omit ticks to fit one page.

## Weight-dial canonical audit

For canonical 0–5 kg @0.1 kg, angle convention is `0°=top`, clockwise positive.

Expected active tick set:

`active_tick_angle(i)=(6*i) mod 360, i=0..50`

Expected labels:

`LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`

Expected clockwise major-label order:

`[0,1,2,3,4,5]`

Expected local hierarchy for every 1 kg span:

`INTERVALS_PER_KG=10`
`INTERIOR_POSITIONS_PER_KG_SPAN=9`
`HALF_KG_INTERMEDIATE_OFFSET=0.5`

The +0.5 kg position is one existing intermediate graduation, longer/more prominent than ordinary 0.1 kg ticks and shorter/weaker than whole-kilogram major ticks. It must not add a physical position.

Expected gap state:

`INACTIVE_GAP_START_ANGLE=300°`
`INACTIVE_GAP_END_ANGLE=360°/0°`
`INACTIVE_GAP_SWEEP_DEG=60°`
`INACTIVE_GAP_TICK_COUNT=0`
`INACTIVE_GAP_RADIAL_MARK_COUNT=0`

W07 must explicitly search the open inactive arc `(300°,360°)` for **any radial scale-like segment**, not merely labeled value ticks. A short unlabeled stroke, decorative hatch, duplicate endpoint, or continuation of the active tick ring counts as a failure.

Also verify:

`NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`

A renderer-created reversed label order, independent label rotation or off-center pivot is a canonical-template failure.

## Speedometer audit

Canonical speedometer common-center rule:

`NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`

W07 must verify the needle is radial from that center to the target tick. Touching the correct tick from the wrong pivot is not acceptable.

## Thermometer audit

For 0–50°C @1°C:

- 50 intervals / 51 positions;
- major positions 0,10,20,30,40,50 = 6;
- intermediate positions 5,15,25,35,45 = 5;
- ordinary minor positions = 40;
- each 10°C major span contains 10 intervals / 9 interior positions;
- liquid endpoint lies exactly on target graduation centerline.

## Graduated-container local-span audit

For canonical 0–1000 mL @50 mL with 100 mL major divisions:

`INTERVALS_PER_100ML=2`
`INTERIOR_POSITIONS_PER_100ML_SPAN=1`

W07 independently recounts every adjacent major span and verifies exactly one interior +50 mL graduation. Multiple short strokes between adjacent 100 mL labels are a failure even when the global labels appear correct.

## Protractor audit

For 0–180° @1°:

- perfect upper semicircle from one center `C` and radius `R`;
- baseline endpoints are `C±R` horizontally;
- 0° right, 90° top, 180° left;
- exactly 180 equal intervals / 181 radial positions;
- 10° major, 5° intermediate, 1° minor hierarchy uses existing positions;
- one active numeric scale only unless dual-scale selection is explicitly taught;
- `ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`;
- all ticks are radial from `C`;
- no ellipse, perspective, shear, non-uniform scale or warped arc;
- target ray begins at `C` and intersects exact target graduation.

## Prompt QA

`PROMPT_INSTRUMENT_TEMPLATE_QA`
`PROMPT_TOPOLOGY_QA`
`PROMPT_INTERVAL_COUNT_QA`
`PROMPT_POSITION_COUNT_QA`
`PROMPT_MAJOR_MINOR_QA`
`PROMPT_LOCAL_SPAN_RECOUNT_QA` when applicable
`PROMPT_NO_MISSING_TICK_SPEC_QA`
`PROMPT_NO_EXTRA_TICK_SPEC_QA`
`PROMPT_NON_SCALE_REGION_QA`
`PROMPT_TARGET_REPRESENTABILITY_QA`
`PROMPT_TARGET_ALIGNMENT_SPEC_QA`
`PROMPT_MINIMUM_SIZE_QA`
`PROMPT_PER_ITEM_RENDER_STATE_QA`
`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_INSTRUMENT_COMMON_CENTER_QA` when radial/angular
`PROMPT_POINTER_ORIGIN_COINCIDENCE_QA` when pointer/ray exists
`PROMPT_RADIAL_COLLINEARITY_QA` when radial/angular
`PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA` when object-on-ruler
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA` when applicable
`PROMPT_PROTRACTOR_BASELINE_QA` when applicable
`PROMPT_PROTRACTOR_SCALE_DIRECTION_QA` when applicable
`PROMPT_PROTRACTOR_SINGLE_SCALE_QA` when applicable
`PROMPT_PROTRACTOR_COMMON_CENTER_QA` when applicable
`PROMPT_PROTRACTOR_RADIAL_TICK_QA` when applicable
`PROMPT_PROTRACTOR_SHAPE_INTEGRITY_QA` when applicable
`PROMPT_DIAL_LABEL_ORDER_QA` when applicable
`PROMPT_DIAL_GAP_GEOMETRY_SERIALIZATION_QA` when applicable
`PROMPT_DIAL_GAP_RADIAL_MARK_ZERO_QA` when applicable
`PROMPT_DIAL_CANONICAL_LABEL_ANGLE_QA` when applicable

Any applicable FAIL blocks prompt release.

## Artifact phase

Before actual image:

`ARTIFACT_QA=NOT_YET_TESTED`

If an artifact is supplied, inspect every instructional instrument individually for shape/orientation, range, global and local interval/position count, spacing, anchoring, labels/order, common center/origin, projection/reference guides, pointer/hand/ray/level, target alignment, no missing/extra/merged marks, inactive-region integrity, distortion and photocopy readability.

For a ruler 1 cm @1 mm, independently verify 10 spaces, 11 endpoint-inclusive positions, 9 interior positions, no border/decoration acting as an extra graduation, and correct endpoint projections for object measurement.

For an open-arc dial, inspect the inactive region independently and count radial marks there; expected count is zero unless the owning domain explicitly defines otherwise.

One wrong instructional instrument blocks classroom release.