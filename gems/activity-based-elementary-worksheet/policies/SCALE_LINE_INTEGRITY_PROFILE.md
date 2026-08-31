# Scale-Line Integrity Profile — All Learner-Read Scales

Version: 1.2.0
Status: Mandatory cross-domain runtime profile
Compatible Gem baseline: 2.6.x
Primary auditor: `W07_INSTRUMENT_AUDITOR`
Companion prevention profile: `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`

Applies whenever a learner reads graduations, ticks, marks, grid/axis intervals, or a pointer/level against a scale, including:

- analog clock minute/hour marks
- weight/dial scales
- rulers and linear measuring scales
- **vehicle speedometers / open-arc speed dials**
- thermometers
- graduated capacity containers
- semicircular/full-circle protractors
- learner-read graph axes

This profile complements domain formulas. Owning domain workers define values/topology; this profile protects the physical/visual integrity of the scale lines used to represent them. The companion review-revise profile requires the downstream renderer to recount and repair learner-read instruments before finalization.

## 1. Core rule

A scale line is academic data.

`SCALE_LINE_INTEGRITY > THEME_ART > DECORATION`

Missing, extra, merged, floating, uneven, misaligned, reversed, occluded, or visually ambiguous graduations are critical academic defects when the learner must read them.

A scale is not valid merely because its interval count is numerically correct. The final printed geometry must also preserve independently verifiable spacing, anchoring, hierarchy, direction, labels, and target alignment.

## 2. Mandatory scale-line specification

Every learner-read scale must resolve a `SCALE_LINE_SPEC` before prompt release containing at least:

- `TOPOLOGY_FAMILY`
- `ACTIVE_RANGE`
- `MINOR_INTERVAL`
- `MAJOR_INTERVAL`
- `EXPECTED_INTERVAL_COUNT`
- `EXPECTED_POSITION_COUNT`
- `SCALE_DIRECTION`
- `REFERENCE_BASELINE_OR_RING`
- `TICK_ANCHOR_MODE`
- `MAJOR_MINOR_HIERARCHY`
- `ENDPOINT_BEHAVIOR`
- `INACTIVE_REGION_RULE` when applicable
- `MIN_PRINTED_INSTRUMENT_SIZE`
- `MIN_TICK_CENTER_SPACING_MM`
- `PRINT_SPACING_ORACLE` for dense learner-read scales

If any required field is unresolved for a learner-read scale, `PROMPT_SCALE_LINE_SPEC_QA=FAIL`.

## 3. Exact count and topology

The smallest instructional graduation defines the count.

### LINEAR_ENDPOINT_INCLUSIVE

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/MINOR_INTERVAL`
`EXPECTED_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`
`EXPECTED_INTERIOR_POSITION_COUNT=max(EXPECTED_POSITION_COUNT-2,0)`

Both endpoints are physical scale positions.

Canonical ruler 1 cm @1 mm:

- 10 intervals
- 11 endpoint-inclusive positions
- 9 interior positions
- physical ruler edge is not an extra graduation

### CYCLIC_FULL_CIRCLE

N equal intervals = N distinct physical positions. The wrap endpoint is shared and must not be duplicated.

Analog clock full minute face: exactly 60 intervals / 60 positions.

### OPEN_ARC_BOUNDED

The active arc is endpoint-inclusive; the inactive/non-scale region contains no value ticks unless the owning domain explicitly defines otherwise.

Canonical 0–5 kg teaching dial: 50 active intervals / 51 active positions plus a 60° inactive gap.

Canonical 0–120 km/h speedometer with 10 km/h minor interval: 12 active intervals / 13 active positions plus a 120° inactive gap.

### PROTRACTOR_HALF_CIRCLE

For 0–180° at minor interval d:

`EXPECTED_INTERVAL_COUNT=180/d`
`EXPECTED_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`

At 1°: 180 intervals / 181 positions.

## 4. Tick anchoring — mandatory

All graduations must be anchored to one authoritative baseline/ring/arc.

- radial scales: every tick touches the same reference ring/arc and extends consistently inward or outward;
- linear scales: every tick starts from the same authoritative baseline/scale edge;
- graph axes: tick marks intersect the axis line at their exact data position;
- no floating ticks;
- no detached tick fragments;
- no alternating anchor direction unless the configured instrument explicitly requires it;
- no perspective transform that changes tick spacing or angle.

`PROMPT_SCALE_TICK_ANCHOR_QA` is mandatory for learner-read scales.

## 5. Major / minor hierarchy

Major marks must be visibly and consistently stronger than minor marks without creating extra positions.

Default print-safe hierarchy unless a domain specifies stronger values:

- minor tick stroke width: at least 0.25 mm at final print size;
- major tick stroke width: at least 0.35 mm and not thinner than minor ticks;
- major tick length: at least 1.5× minor tick length;
- optional intermediate marks must have one consistent level between major and minor and must correspond to a real configured subdivision;
- when per-item verification references an intermediate mark such as a 5° protractor mark, that intermediate hierarchy becomes REQUIRED for the canonical template rather than optional;
- identical semantic levels use identical length/weight throughout one canonical template;
- do not use decorative stroke variation as if it were an instructional hierarchy.

If the renderer cannot maintain this hierarchy at the planned size, increase the instrument size or paginate; never delete minor marks to compensate.

`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA` is mandatory.

## 6. Spacing and print readability

At final intended print size:

- adjacent smallest instructional tick centers must satisfy the resolved minimum spacing oracle; default lower bound is at least 0.60 mm;
- ticks must remain individually distinguishable after black-and-white photocopying;
- two adjacent ticks must not merge into one dark block;
- no tick may be so faint/thin that photocopy loss is likely;
- no gray-only scale lines for required graduations;
- dense scales must increase instrument size or paginate before compromising tick identity.

`MIN_TICK_CENTER_SPACING_MM=0.60` is the default lower bound; a domain may require more, never less without explicit audited justification.

For radial scales, do not estimate spacing from overall page width. Compute it at the authoritative reading/tick ring:

`tick_center_spacing_mm = reading_radius_mm × radians(MINOR_INTERVAL_DEG)`

For a 0–180° protractor at 1° resolution and the default 0.60 mm minimum:

`MIN_READING_RADIUS_MM = 0.60 / radians(1) ≈ 34.38 mm`
`MIN_READING_RING_DIAMETER_MM ≈ 68.76 mm`
`PRODUCTION_MIN_PROTRACTOR_WIDTH_MM = 70 mm`

A 65 mm diameter protractor fails this spacing oracle because its 1° arc spacing is only about 0.567 mm. It must not pass `PROMPT_SCALE_PRINT_SEPARATION_QA`.

`PROMPT_SCALE_PRINT_SEPARATION_QA` is mandatory.

## 7. Uniformity and monotonicity

Within every uniform scale segment:

- equal value intervals have equal geometric spacing;
- scale values progress monotonically in the configured direction;
- no local compression/expansion;
- no reversed subsection;
- no duplicated physical position for two different non-wrap values;
- no missing value position;
- no extra unlabeled instructional-looking graduation.

`PROMPT_SCALE_UNIFORM_SPACING_QA` and `PROMPT_SCALE_DIRECTION_QA` are mandatory.

## 8. Labels and scale lines

Labels are subordinate to scale geometry and must not alter it.

- every major numeric label aligns unambiguously with its intended major graduation;
- labels must not cover, erase, shorten, bend, or displace ticks;
- labels must not sit so close to adjacent ticks that association becomes ambiguous;
- no decorative numeral may resemble a scale label;
- negative signs, degree symbols, decimal points, units, and zero labels must remain legible where configured;
- label omission is allowed only when the domain/grade profile intentionally defines an unlabeled minor mark, never because layout is crowded.

`PROMPT_SCALE_LABEL_ALIGNMENT_QA` and `PROMPT_SCALE_LABEL_CLEARANCE_QA` are mandatory when labels are present.

## 9. Pointer / level / endpoint alignment

When a pointer, hand, ray, liquid level, object endpoint, or bar height is read against a scale:

- the designated reading endpoint must terminate/intersect the authoritative reading ring/baseline/centerline at the exact target position;
- the pointer must not terminate between ticks in exact-reading mode;
- the pointer/level must not hide enough neighboring ticks to make the local scale unreadable;
- pointer thickness must not create two plausible target ticks;
- the center pivot/origin/baseline must remain exact for radial/angular instruments;
- the renderer-only state must specify both semantic target and exact geometric target.

`PROMPT_SCALE_TARGET_ALIGNMENT_QA` is mandatory.

## 10. Inactive and non-scale regions

For instruments with inactive regions/gaps:

- zero instructional value ticks inside the inactive region unless explicitly defined by domain;
- decoration in the gap must not resemble ticks, labels, pointer positions, or continuation of the active scale;
- active endpoints remain visually distinct;
- do not close an open-arc scale into a false full-circle scale.

`PROMPT_SCALE_INACTIVE_REGION_QA` is mandatory when an inactive region exists.

## 11. Decoration isolation

Theme/context artwork must not create scale-like ambiguity.

Inside or immediately adjacent to an instructional instrument:

- no decorative radial rays near radial scales;
- no short repeated decorative strokes parallel to ruler/thermometer/container graduations;
- no stars/dots/texture placed on tick positions;
- no border pattern that visually continues a scale;
- no shading/texture that hides minor ticks;
- no decorative pointer-like line from the center pivot.

`PROMPT_SCALE_DECORATION_ISOLATION_QA` is mandatory.

## 12. Canonical template consistency

Repeated instruments sharing the same configured scale must use one canonical `SCALE_LINE_SPEC`.

Across those items, do not change count, spacing, hierarchy, label positions, active range, direction, reference ring/baseline, stroke hierarchy or inactive-region geometry.

Only the intended item state (pointer/hand/level/endpoints/data value) may change.

`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA` is mandatory.

## 13. Domain-specific minimums

### Clock
- 60 distinct minute positions when a full minute face is required;
- 12 major hour positions exactly every fifth minute mark;
- major hour marks stronger than minute marks but do not add positions;
- all radial ticks share one ring and consistent orientation.

### Weight dial
- honor owning-domain active sweep and inactive gap;
- all active ticks lie on the same arc/ring;
- endpoint ticks are present exactly once;
- no gap ticks.

### Ruler
- every graduation begins on the authoritative ruler baseline/edge;
- cm marks stronger/longer than mm marks;
- physical ruler edge must not substitute for or add to the zero graduation;
- at 1 mm resolution every 1 cm span has exactly 10 intervals / 11 positions / 9 interior positions;
- a 5 mm hierarchy mark occupies an existing position and never adds a new one.

### Speedometer
- topology is the owning-domain open arc, not an invented full circle;
- all active ticks share one reading ring;
- canonical 0–120 km/h profile has 12 intervals / 13 positions and a 120° inactive gap;
- one instructional needle only;
- needle endpoint intersects the exact target tick on the reading ring;
- no value ticks in the inactive gap.

### Thermometer
- graduations are perpendicular to one straight scale axis;
- labels align to configured major ticks;
- liquid endpoint aligns to the target graduation centerline;
- discrete targets do not sit between ticks.

### Graduated container
- scale lines are parallel and anchored consistently to one side/reference edge;
- liquid/meniscus reading point aligns to the target scale centerline;
- container decoration cannot create a second apparent scale.

### Protractor
- radial graduations share exact center/origin geometry;
- baseline 0° direction and active scale direction are explicit;
- 0°/180° endpoints are exact for semicircle;
- 0°/360° share one physical position for cyclic full-circle mode;
- 0–180° @1° uses exactly 180 intervals / 181 positions;
- `PRODUCTION_MIN_PROTRACTOR_WIDTH_MM=70` when `MIN_TICK_CENTER_SPACING_MM=0.60` and the reading ring spans the semicircle;
- a learner-read 1° protractor must use a deterministic vector instrument layer; unresolved `RENDER_PATH=AUTO` is forbidden in the final prompt;
- use one clearly active reading direction. A mirrored competing inner scale is forbidden unless the lesson explicitly teaches dual-scale selection;
- if 5° relations are used in item verification, 5° intermediate marks are required and occupy existing 1° positions.

### Graph axis
- tick marks intersect the axis at exact data positions;
- uniform numeric interval => uniform geometric interval;
- bar endpoints/heights align to the scale mapping;
- grid lines, if present, correspond exactly to configured axis ticks and are visually subordinate to data marks.

## 14. Prompt serialization

The final prompt must include the resolved `SCALE_LINE_SPEC` once per canonical scale template and exact item states separately.

Do not rely on vague phrases such as `draw clear scale marks`, `use normal ruler ticks`, `make a realistic thermometer`, `standard speedometer`, or `standard graph axis` without count, interval, direction, anchoring, hierarchy, endpoint semantics, and resolved print-spacing evidence.

For dense radial instruments, serialize the computed `PRINT_SPACING_ORACLE` result and minimum safe printed size. Do not serialize an empirically guessed size.

`PROMPT_SCALE_LINE_SERIALIZATION_QA` blocks release if the final prompt leaves scale-line geometry to renderer invention.

## 15. Mandatory renderer review linkage

For every learner-read instrument, scale-line rules must be consumed by the mandatory `INSTRUMENT_REVIEW_REVISE_PROTOCOL`.

The renderer must independently recount/rederive the visible scale against this profile and the owning domain state. If any count, spacing, anchoring, label, target-alignment or inactive-region mismatch is detected, repair/regenerate and re-run the entire instrument checklist before finalization.

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Renderer self-review remains a prevention layer and does not prove actual artifact correctness.

## 16. Artifact phase

Prompt QA cannot prove actual drawn scale lines.

Before image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`

For every rendered learner-read scale inspect, at minimum:

1. exact tick/position count;
2. no missing/extra/merged tick;
3. uniform spacing;
4. major/minor hierarchy;
5. common anchoring ring/baseline;
6. scale direction;
7. labels and clearance;
8. pointer/level/endpoint alignment;
9. inactive-region integrity;
10. print/photocopy distinguishability;
11. absence of decorative competing marks;
12. computed print-spacing oracle remains satisfied at actual output size.

One incorrect instructional scale blocks classroom release.

## 17. Mandatory QA family

`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_SCALE_PRINT_SPACING_ORACLE_QA`
`PROMPT_SCALE_UNIFORM_SPACING_QA`
`PROMPT_SCALE_DIRECTION_QA`
`PROMPT_SCALE_LABEL_ALIGNMENT_QA` when labels apply
`PROMPT_SCALE_LABEL_CLEARANCE_QA` when labels apply
`PROMPT_SCALE_TARGET_ALIGNMENT_QA`
`PROMPT_SCALE_INACTIVE_REGION_QA` when applicable
`PROMPT_SCALE_DECORATION_ISOLATION_QA`
`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA`
`PROMPT_SCALE_LINE_SERIALIZATION_QA`
`PROMPT_PROTRACTOR_ACTIVE_SCALE_QA` when applicable
`PROMPT_PROTRACTOR_RENDER_PATH_QA` when applicable

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED`.
