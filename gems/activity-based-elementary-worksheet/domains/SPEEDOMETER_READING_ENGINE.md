# SPEEDOMETER_READING_ENGINE — Vehicle Speedometer Reading

Version: 1.1.0
Status: PRODUCTION_CANDIDATE
Owning worker: `W04_LENGTH_DISTANCE`
Visual auditor: `W07_INSTRUMENT_AUDITOR`
Compatible Gem baseline: 2.6.x
Requires: `INSTRUMENT_READING_ENGINE.md`, `policies/SCALE_LINE_INTEGRITY_PROFILE.md`, `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`

## 1. Scope

Supports direct reading of a vehicle speedometer as a learner-read instrument.

This engine does **not** silently introduce the formula `speed=distance/time`. Direct speedometer reading is an instrument-reading skill. Speed/rate calculation remains outside this engine unless a separate explicit deterministic rule is added.

## 2. Core parameters

`SPEEDOMETER_MIN_KMH`
`SPEEDOMETER_MAX_KMH`
`SPEEDOMETER_ACTIVE_SWEEP_DEG`
`SPEEDOMETER_START_ANGLE_DEG`
`SPEEDOMETER_MAJOR_INTERVAL_KMH`
`SPEEDOMETER_MINOR_INTERVAL_KMH`
`TARGET_SPEEDS_KMH`
`ANSWER_FORMAT`
`SPEEDOMETER_DIRECTION=CLOCKWISE|COUNTERCLOCKWISE`

## 3. Canonical elementary teaching profile

Unless the teacher explicitly requests another valid profile:

`SPEEDOMETER_MIN_KMH=0`
`SPEEDOMETER_MAX_KMH=120`
`SPEEDOMETER_ACTIVE_SWEEP_DEG=240`
`SPEEDOMETER_START_ANGLE_DEG=240`
`SPEEDOMETER_DIRECTION=CLOCKWISE`
`SPEEDOMETER_MAJOR_INTERVAL_KMH=20`
`SPEEDOMETER_MINOR_INTERVAL_KMH=10`
`UNIT=km/h`

Angle convention for this family:

`0° = top / 12 o'clock`
`CLOCKWISE_POSITIVE=YES`

This gives:

- active range 0–120 km/h;
- 12 equal minor intervals;
- 13 endpoint-inclusive active positions;
- each 10 km/h interval = 20°;
- major labels 0,20,40,60,80,100,120;
- 120° inactive/non-scale gap at the lower portion of the dial;
- zero value ticks or radial pseudo-ticks inside the inactive gap.

## 4. Topology

Topology family: `OPEN_ARC_BOUNDED`.

For range `MIN→MAX` with minor interval `d`:

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/d`
`EXPECTED_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`

Require exact divisibility/representability.

For the canonical profile:

`EXPECTED_INTERVAL_COUNT=12`
`EXPECTED_POSITION_COUNT=13`

A full-circle value scale or value ticks through the inactive gap is academically wrong.

## 5. Value-to-angle mapping

Let:

`range=MAX-MIN`
`ratio=(target-MIN)/range`

For clockwise mode:

`target_angle=(START_ANGLE + ratio*ACTIVE_SWEEP) mod 360`

For the canonical profile:

`target_angle=(240 + 2*target_kmh) mod 360`

Examples:

- 0 km/h → 240°
- 30 km/h → 300°
- 60 km/h → 0° = straight up
- 90 km/h → 60°
- 120 km/h → 120°

## 6. Target representability

For discrete-reading mode:

`tick_index=round((target-MIN)/MINOR_INTERVAL)`
`represented=MIN+tick_index*MINOR_INTERVAL`

Require exact representability unless interpolation is explicitly part of the objective.

For canonical 10 km/h minor intervals, 35 km/h is invalid in default discrete mode; 30 or 40 km/h is valid.

## 7. Mandatory common-center geometry — critical

Every speedometer is generated from one authoritative center coordinate:

`DIAL_CENTER=(cx,cy)`
`ACTIVE_ARC_CENTER=DIAL_CENTER`
`READING_RING_CENTER=DIAL_CENTER`
`NEEDLE_PIVOT=DIAL_CENTER`

The pivot is **not** an independent decorative point. It is the same exact coordinate used to construct the circular arc and every radial graduation.

For each active tick angle θ:

- outer tick point lies on the authoritative reading radius from `DIAL_CENTER`;
- inner tick point lies on the same radial line;
- the needle is a radial segment beginning exactly at `DIAL_CENTER`;
- needle direction equals the target angle;
- needle tip intersects the target graduation centerline/read ring.

Required equality:

`distance(NEEDLE_PIVOT,DIAL_CENTER)=0`

Any visible pivot offset, even when the needle tip appears to touch the correct label/tick, is `CRITICAL_ACADEMIC` because the pointer is no longer a true radial reading.

## 8. Mandatory geometry

- one front-facing circular/arc dial housing;
- one instructional needle only;
- active ticks share one authoritative reading ring;
- major ticks visibly stronger/longer than minor ticks;
- labels align to their exact major tick radial lines;
- no perspective/skew/ellipse/non-uniform transform;
- inactive arc remains visually non-scale;
- no decorative dashboard marks resembling value ticks or a second needle;
- template translation/uniform scaling may move the whole instrument but cannot move pivot, arc, ticks, labels, or needle origin independently.

## 9. Renderer-only item state

Each item must serialize an atomic renderer-only block containing:

`ITEM_ID`
`SEMANTIC_TARGET_SPEED_KMH`
`TICK_INDEX`
`TARGET_ANGLE_DEG`
`DIAL_CENTER`
`NEEDLE_PIVOT=DIAL_CENTER`
`NEAREST_MAJOR_LABELS`
`RELATIONAL_VERIFICATION`
`ITEM_SPECIFIC_HARD_NEGATIVE`

Canonical angles should be normalized to `[0,360)` in machine-stable state. Expanded equivalents such as 380° may be explanatory metadata only, never the canonical geometry key.

Mark renderer state `RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

## 10. Student-visible format

Default learner view:

- one speedometer face per question;
- blank answer line such as `ความเร็ว ............ กิโลเมตรต่อชั่วโมง` or teacher-requested equivalent;
- no printed target speed or target angle;
- canonical numeric labels remain visible.

## 11. Grade/difficulty guidance

Conservative progression:

- EASY: targets on labelled 20 km/h major marks only;
- MEDIUM: targets on 10 km/h minor marks, including unlabeled intermediate ticks;
- HARD: finer valid minor interval only when explicitly requested and printable/readable.

Do not increase difficulty by making the scale visually ambiguous.

## 12. Renderer self-review

Renderer self-review must independently:

1. recount 12 active intervals / 13 active positions for the canonical profile;
2. verify 120° inactive gap contains zero scale-like radial marks;
3. verify major/minor hierarchy and labels;
4. recompute target angle;
5. verify `NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`;
6. verify the needle is radial from that center and intersects the exact target tick;
7. reject any ellipse/skew/pivot translation;
8. regenerate and repeat the complete checklist after a failure.

## 13. QA

`PROMPT_SPEEDOMETER_TOPOLOGY_QA`
`PROMPT_SPEEDOMETER_RANGE_QA`
`PROMPT_SPEEDOMETER_INTERVAL_POSITION_COUNT_QA`
`PROMPT_SPEEDOMETER_TARGET_REPRESENTABILITY_QA`
`PROMPT_SPEEDOMETER_ANGLE_MAPPING_QA`
`PROMPT_SPEEDOMETER_NEEDLE_ALIGNMENT_QA`
`PROMPT_SPEEDOMETER_PIVOT_CENTER_QA`
`PROMPT_SPEEDOMETER_RADIAL_COLLINEARITY_QA`
`PROMPT_SPEEDOMETER_INACTIVE_GAP_QA`
`PROMPT_SPEEDOMETER_LABEL_PRESERVATION_QA`
`PROMPT_SPEEDOMETER_ONE_NEEDLE_QA`
`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`

Any wrong active sweep, count, direction, target mapping, off-center pivot, non-radial needle, gap ticks, full-circle substitution, target leak, or missing self-review protocol blocks prompt release.

Artifact geometry remains `ARTIFACT_QA=NOT_YET_TESTED` until the rendered worksheet is inspected.
