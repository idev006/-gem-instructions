# SPEEDOMETER_READING_ENGINE — Vehicle Speedometer Reading

Version: 1.0.0
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

This gives:

- active range 0–120 km/h;
- 12 equal minor intervals;
- 13 endpoint-inclusive active positions;
- each 10 km/h interval = 20°;
- major labels 0,20,40,60,80,100,120;
- 120° inactive/non-scale gap;
- zero value ticks inside the inactive gap.

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

because 240° / 120 km/h = 2° per km/h.

Examples:

- 0 km/h → 240°
- 30 km/h → 300°
- 60 km/h → 0°
- 90 km/h → 60°
- 120 km/h → 120°

## 6. Target representability

For discrete-reading mode:

`tick_index=round((target-MIN)/MINOR_INTERVAL)`
`represented=MIN+tick_index*MINOR_INTERVAL`

Require exact representability unless interpolation is explicitly part of the objective.

For canonical 10 km/h minor intervals, 35 km/h is invalid in default discrete mode; 30 or 40 km/h is valid.

## 7. Mandatory geometry

- one front-facing circular/arc dial housing;
- one exact center pivot;
- one instructional needle only;
- active ticks share one authoritative reading ring;
- needle endpoint reaches/intersects that reading ring at the exact target tick;
- major ticks visibly stronger/longer than minor ticks;
- labels align to major ticks;
- no perspective/skew/ellipse that changes reading;
- inactive arc remains visually non-scale;
- no decorative dashboard marks resembling value ticks or a second needle.

## 8. Renderer-only item state

Each item must serialize an atomic renderer-only block containing:

`ITEM_ID`
`SEMANTIC_TARGET_SPEED_KMH`
`TICK_INDEX`
`TARGET_ANGLE_DEG`
`NEAREST_MAJOR_LABELS`
`RELATIONAL_VERIFICATION`
`ITEM_SPECIFIC_HARD_NEGATIVE`

Example for 70 km/h canonical profile:

- tick index = 7
- target angle = 20°
- between major labels 60 and 80
- exactly halfway between 60 and 80
- hard negative: do not point to 60, 80, or any inactive-gap position.

Mark renderer state `RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

## 9. Student-visible format

Default learner view:

- one speedometer face per question;
- blank answer line such as `ความเร็ว ............ กิโลเมตรต่อชั่วโมง` or teacher-requested equivalent;
- no printed target speed or target angle;
- canonical numeric labels remain visible.

## 10. Grade/difficulty guidance

Conservative progression:

- EASY: targets on labelled 20 km/h major marks only;
- MEDIUM: targets on 10 km/h minor marks, including unlabeled intermediate ticks;
- HARD: finer valid minor interval only when explicitly requested and printable/readable.

Do not increase difficulty by making the scale visually ambiguous.

## 11. Scale-line and self-review

The final prompt must inherit both:

- `SCALE_LINE_INTEGRITY_PROFILE.md`
- `INSTRUMENT_REVIEW_REVISE_PROFILE.md`

Renderer self-review must recount active positions, confirm inactive-gap integrity, verify label/tick alignment, recompute target angle, and confirm the needle endpoint intersects the exact target tick before finalization.

## 12. QA

`PROMPT_SPEEDOMETER_TOPOLOGY_QA`
`PROMPT_SPEEDOMETER_RANGE_QA`
`PROMPT_SPEEDOMETER_INTERVAL_POSITION_COUNT_QA`
`PROMPT_SPEEDOMETER_TARGET_REPRESENTABILITY_QA`
`PROMPT_SPEEDOMETER_ANGLE_MAPPING_QA`
`PROMPT_SPEEDOMETER_NEEDLE_ALIGNMENT_QA`
`PROMPT_SPEEDOMETER_INACTIVE_GAP_QA`
`PROMPT_SPEEDOMETER_LABEL_PRESERVATION_QA`
`PROMPT_SPEEDOMETER_ONE_NEEDLE_QA`
`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`

Any wrong active sweep, count, direction, target mapping, needle alignment, gap ticks, full-circle substitution, target leak, or missing self-review protocol blocks prompt release.

Artifact geometry remains `ARTIFACT_QA=NOT_YET_TESTED` until the rendered worksheet is inspected.
