# Scale-Line Integrity Profile — All Learner-Read Scales

Version: 1.4.0
Status: Mandatory cross-domain runtime profile
Compatible Gem baseline: 2.6.x
Primary geometry auditor: `W07_INSTRUMENT_AUDITOR`
Independent metrology auditor: `W10_METROLOGY_ENGINEER`
Companion prevention profile: `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
Companion independent audit: `policies/METROLOGY_ASSURANCE_PROFILE.md`
Companion packing audit: `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Applies whenever a learner reads graduations, ticks, marks, grid/axis intervals, or a pointer/level against a scale, including analog clocks, weight/dial scales, rulers, speedometers, thermometers, graduated capacity containers, protractors, and learner-read graph axes.

## 1. Core rule

A scale line is academic data.

`SCALE_LINE_INTEGRITY > THEME_ART > DECORATION`

Missing, extra, merged, floating, uneven, misaligned, reversed, occluded, off-center, distorted, or visually ambiguous graduations are critical academic defects when the learner must read them.

A scale is not valid merely because its interval count is numerically correct. Final geometry must also preserve spacing, anchoring, hierarchy, direction, label association/order, common center/origin where applicable, target alignment, shape integrity, and metrology feasibility.

## 2. Mandatory scale-line specification

Every learner-read scale must resolve a `SCALE_LINE_SPEC` before prompt release containing at least:

- `TOPOLOGY_FAMILY`
- `ACTIVE_RANGE`
- `MINOR_INTERVAL`
- `INTERMEDIATE_INTERVAL` when applicable
- `MAJOR_INTERVAL`
- `EXPECTED_INTERVAL_COUNT`
- `EXPECTED_POSITION_COUNT`
- `SCALE_DIRECTION`
- `REFERENCE_BASELINE_OR_RING`
- `TICK_ANCHOR_MODE`
- `MAJOR_MINOR_HIERARCHY`
- `ENDPOINT_BEHAVIOR`
- `INACTIVE_REGION_RULE` when applicable
- `METROLOGY_MINIMUM_SIZE_MM`
- `SELECTED_RENDER_SIZE_MM`
- `MIN_TICK_CENTER_SPACING_MM`
- `PRINT_SPACING_ORACLE` for dense learner-read scales
- authoritative center/origin fields for radial/angular instruments.

If any required field is unresolved, `PROMPT_SCALE_LINE_SPEC_QA=FAIL`.

## 3. Exact count and topology

### LINEAR_ENDPOINT_INCLUSIVE

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/MINOR_INTERVAL`
`EXPECTED_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`
`EXPECTED_INTERIOR_POSITION_COUNT=max(EXPECTED_POSITION_COUNT-2,0)`

Canonical ruler 1 cm @1 mm:
- 10 intervals
- 11 endpoint-inclusive positions
- 9 interior positions
- physical ruler edge is not an extra graduation.

Canonical thermometer 0–50°C @1°C:
- 50 intervals / 51 positions;
- 6 major positions at 0,10,20,30,40,50;
- 5 intermediate positions at 5,15,25,35,45;
- 40 ordinary minor positions;
- every 10°C span has 10 intervals / 9 interior positions.

### CYCLIC_FULL_CIRCLE

N equal intervals = N distinct physical positions. The wrap endpoint is shared and must not be duplicated.

Analog clock full minute face: exactly 60 intervals / 60 positions.

### OPEN_ARC_BOUNDED

The active arc is endpoint-inclusive; the inactive/non-scale region contains no value ticks or tick-like radial marks unless the owning domain explicitly defines otherwise.

Canonical 0–5 kg teaching dial:
- angle convention 0° top, clockwise positive;
- labels `0@0°,1@60°,2@120°,3@180°,4@240°,5@300°`;
- 50 active intervals / 51 positions;
- inactive open gap `(300°,360°)`;
- clockwise major-label order `[0,1,2,3,4,5]`.

Canonical 0–120 km/h speedometer with 10 km/h minor interval: 12 active intervals / 13 active positions plus a 120° inactive gap.

### PROTRACTOR_HALF_CIRCLE

For 0–180° at minor interval d:

`EXPECTED_INTERVAL_COUNT=180/d`
`EXPECTED_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`

At 1°: 180 intervals / 181 positions.

Canonical teaching orientation: perfect upper semicircle; 0° right, 90° top, 180° left; one active numeric scale by default.

## 4. Tick anchoring and common center

All graduations must be anchored to one authoritative baseline/ring/arc.

For radial dials/clocks/speedometers:

`PIVOT_CENTER == READING_RING_CENTER == TICK_RADIAL_CENTER`

For protractors:

`ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`

Every radial tick, pointer, hand, or ray must be geometrically radial/collinear from that exact common center. A pointer that visually reaches a target tick from an offset pivot is invalid.

Linear scales: every tick starts from one authoritative baseline/scale edge. Graph ticks intersect the axis at exact data positions.

No floating/detached tick fragments or independent center translations.

Required gates:
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_INSTRUMENT_COMMON_CENTER_QA` when radial/angular
`PROMPT_POINTER_ORIGIN_COINCIDENCE_QA` when pointer/ray exists
`PROMPT_RADIAL_COLLINEARITY_QA` when radial/angular.

## 5. Major / intermediate / minor hierarchy

Hierarchy classes reuse existing positions and never add positions.

Default print-safe hierarchy unless a domain specifies stronger values:
- minor tick stroke width >=0.25 mm;
- major tick stroke width >=0.35 mm and not thinner than minor;
- major tick length >=1.5× minor length;
- optional/required intermediate ticks use one consistent level between major and minor;
- identical semantic levels use identical geometry throughout the template.

Mutually exclusive classification is required when divisibility overlaps. Example thermometer 0–50 @1:
- major: `i%10==0`;
- intermediate: `i%5==0 AND i%10!=0`;
- minor: all remaining positions.

Never draw both major and intermediate strokes as separate ticks at one physical position.

`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA` is mandatory.

## 6. Spacing and print readability

At final intended print size:
- adjacent smallest instructional tick centers satisfy the resolved minimum spacing oracle; default >=0.60 mm;
- ticks remain individually distinguishable after B&W photocopying;
- required marks cannot rely on gray-only strokes;
- dense scales enlarge or paginate before tick identity is compromised.

Radial/angular spacing:

`tick_center_spacing_mm = reading_radius_mm × radians(MINOR_INTERVAL_DEG)`

For 0–180° @1° and 0.60 mm floor:

`MIN_READING_RADIUS_MM≈34.38`
`MIN_READING_RING_DIAMETER_MM≈68.76`
`PRODUCTION_MIN_PROTRACTOR_WIDTH_MM=70`

65 mm width fails (~0.567 mm spacing).

Linear spacing:

`tick_center_spacing_mm = printed_scale_length_mm / interval_count`

For thermometer 0–50 @1 using 60 mm selected scale length, spacing is exactly 1.20 mm. `>1.20 mm` is false for that exact geometry.

W10 independently recomputes spacing evidence.

## 7. Uniformity, monotonicity, and label order

Within every uniform scale segment:
- equal value intervals have equal geometric spacing;
- values progress monotonically in the configured direction;
- no local compression/expansion/reversal;
- no missing/extra physical value position;
- ordered major labels preserve the owning-domain sequence.

For canonical weight dial, clockwise labels must be exactly `[0,1,2,3,4,5]` associated with `0°,60°,120°,180°,240°,300°`.

`PROMPT_SCALE_UNIFORM_SPACING_QA`, `PROMPT_SCALE_DIRECTION_QA`, and `PROMPT_SCALE_LABEL_ORDER_QA` when applicable are mandatory.

## 8. Labels and scale lines

- every major numeric label aligns unambiguously with its intended major graduation;
- labels must not cover/erase/bend/displace ticks;
- label association must not be ambiguous;
- degree symbols, minus signs, decimal points and units remain legible;
- label omission is permitted only by configured pedagogy, never because layout is crowded.

`PROMPT_SCALE_LABEL_ALIGNMENT_QA` and `PROMPT_SCALE_LABEL_CLEARANCE_QA` are mandatory when labels exist.

## 9. Pointer / level / endpoint alignment

When a pointer, hand, ray, liquid level, object endpoint, or bar height is read against a scale:
- designated reading endpoint terminates/intersects the authoritative target position;
- exact-reading pointers never sit between ticks;
- pointer thickness does not create two plausible readings;
- radial pointers originate at the exact common center;
- protractor rays originate exactly at baseline midpoint/arc center;
- liquid endpoint lies on the target graduation centerline.

`PROMPT_SCALE_TARGET_ALIGNMENT_QA` is mandatory.

## 10. Shape integrity

Geometry carrying academic meaning may not be warped for composition.

Forbidden:
- perspective transform of learner-read scale;
- ellipse substitution for a required circle/semicircle;
- shear;
- non-uniform scaling;
- local arc deformation;
- moving center, baseline, ticks, labels, or pointer independently after template construction.

Canonical protractor uses a perfect upper semicircle. For width `W=2R`, semicircle body height is `R=W/2`.

Gate: `PROMPT_INSTRUMENT_SHAPE_INTEGRITY_QA`; protractor also uses `PROMPT_PROTRACTOR_SHAPE_INTEGRITY_QA`.

## 11. Inactive and non-scale regions

For instruments with inactive regions/gaps:
- zero instructional value ticks inside inactive region;
- zero radial pseudo-ticks/decoration that continues the active scale;
- active endpoints remain distinct;
- open-arc scales are not closed into false full-circle value scales.

`PROMPT_SCALE_INACTIVE_REGION_QA` is mandatory when applicable.

## 12. Decoration isolation

Inside/immediately adjacent to an instructional instrument:
- no decorative radial rays near radial scales;
- no repeated strokes parallel to ruler/thermometer/container graduations;
- no stars/dots/texture on tick positions;
- no border pattern continuing a scale;
- no decorative pointer-like line from center.

`PROMPT_SCALE_DECORATION_ISOLATION_QA` is mandatory.

## 13. Canonical template consistency

Repeated instruments with the same configured scale use one canonical template. Across items do not change count, spacing, hierarchy, label positions/order, active range, direction, reference, common center, aspect ratio or inactive-region geometry. Only intended item state may change.

`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA` is mandatory.

## 14. Domain-specific minimums

### Clock
60 minute positions when full minute face is required; 12 major hour positions reuse minute positions; hands share one pivot.

### Weight dial
0–5 kg canonical top-zero clockwise orientation; 50/51; gap `(300°,360°)`; clockwise labels `[0,1,2,3,4,5]`; pivot=center.

### Ruler
Each 1 cm @1 mm span =10 intervals/11 positions/9 interior; physical edge not tick; 5 mm hierarchy reuses position.

### Speedometer
Canonical 0–120 profile =12/13, 120° inactive gap, one needle; `NEEDLE_PIVOT==DIAL_CENTER==READING_RING_CENTER`.

### Thermometer
0–50 @1 =50/51; 6 major/5 intermediate/40 minor; every 10°C span 10 intervals/9 interior; endpoint aligned.

### Graduated container
Parallel/consistent anchored scale lines; read point exact; no competing scale.

### Protractor
Perfect upper semicircle; 0° right/90° top/180° left; 180/181 @1°; 10° major/5° intermediate/1° minor; one active numeric scale by default; all ticks/rays radial from common center; width>=70 mm at 0.60 mm floor; no ellipse/skew/shear/non-uniform scale.

### Graph axis
Exact uniform mapping; bar endpoints align to canonical data.

## 15. Prompt serialization

The final prompt includes resolved `SCALE_LINE_SPEC` once per canonical template and exact item states separately. Vague phrases like `standard scale` are insufficient.

Dense radial instruments serialize computed print-spacing evidence and safe printed size. Radial/angular items serialize the common-center identity.

`PROMPT_SCALE_LINE_SERIALIZATION_QA` blocks renderer invention of academic geometry.

## 16. Renderer review + W10 linkage

Every learner-read scale is checked by both renderer review protocol and W10 independent metrology. Renderer must recount/rederive visible scale, verify common-center/origin, label order, shape integrity, target alignment and gap integrity, then repair/regenerate and fully recheck any failure.

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Self-review and W10 prompt audit remain prevention, not pixel proof.

## 17. Artifact phase

Before image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`

For each artifact inspect at minimum:
1. exact tick/position count;
2. no missing/extra/merged tick;
3. uniform spacing;
4. hierarchy;
5. anchoring;
6. direction and label order;
7. labels/clearance;
8. common center/origin and radial collinearity;
9. pointer/level/endpoint alignment;
10. inactive-region integrity;
11. shape/aspect-ratio integrity;
12. decoration isolation;
13. print readability and spacing.

One incorrect instructional scale blocks classroom release.

## 18. Mandatory QA family

`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_SCALE_PRINT_SPACING_ORACLE_QA`
`PROMPT_SCALE_UNIFORM_SPACING_QA`
`PROMPT_SCALE_DIRECTION_QA`
`PROMPT_SCALE_LABEL_ALIGNMENT_QA` when labels apply
`PROMPT_SCALE_LABEL_CLEARANCE_QA` when labels apply
`PROMPT_SCALE_LABEL_ORDER_QA` when ordered labels apply
`PROMPT_SCALE_TARGET_ALIGNMENT_QA`
`PROMPT_SCALE_INACTIVE_REGION_QA` when applicable
`PROMPT_SCALE_DECORATION_ISOLATION_QA`
`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA`
`PROMPT_SCALE_LINE_SERIALIZATION_QA`
`PROMPT_INSTRUMENT_COMMON_CENTER_QA` when radial/angular
`PROMPT_POINTER_ORIGIN_COINCIDENCE_QA` when pointer/ray exists
`PROMPT_RADIAL_COLLINEARITY_QA` when radial/angular
`PROMPT_INSTRUMENT_SHAPE_INTEGRITY_QA`
`PROMPT_PROTRACTOR_ACTIVE_SCALE_QA` when applicable
`PROMPT_PROTRACTOR_RENDER_PATH_QA` when applicable
`PROMPT_PROTRACTOR_SHAPE_INTEGRITY_QA` when applicable
`PROMPT_METROLOGY_AUDIT_REQUIRED_QA`
`PROMPT_METROLOGY_INDEPENDENCE_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED`.
