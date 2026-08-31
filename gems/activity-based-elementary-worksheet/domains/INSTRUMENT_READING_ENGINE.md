# INSTRUMENT_READING_ENGINE — Shared Educational Geometry Rules

Version: 1.4.0
Status: Mandatory shared rules for learner-read visual instruments
Owning cross-domain worker: `W07_INSTRUMENT_AUDITOR`
Compatible Gem baseline: 2.6.x
Requires: `policies/SCALE_LINE_INTEGRITY_PROFILE.md`

Applies to analog clocks, dial scales, rulers, thermometers, graduated capacity instruments, protractors, and learner-read graph/axis geometry.

## 1. Core principle

If the learner must read a visual instrument, its geometry is **academic data**.

`INSTRUMENT GEOMETRY > CONTEXT ART > DECORATION`

A missing/extra tick, wrong pointer, distorted scale, ambiguous start point, or unreadable graduation is not a minor art defect.

All learner-read scales additionally inherit the complete `SCALE_LINE_INTEGRITY_PROFILE.md`. The domain worker owns numeric meaning; W07 audits physical scale-line integrity.

## 2. Three layers

1. `CONTEXT_LAYER` — decorative/supportive scene.
2. `INSTRUCTIONAL_INSTRUMENT_LAYER` — authoritative object the child reads.
3. `RESPONSE_LAYER` — blank/student answer area.

Do not make the child read a tiny decorative instrument when a main teaching instrument exists.

## 3. Visibility

Academic target values/indices/angles/levels belong to:

`TEACHER_VISIBLE_PROMPT_METADATA`

when required to draw the instrument. Mark:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

Student Blueprint must not expose hidden target values, tick indices, angles, levels, or solved answers.

Canonical labels required by the instrument remain student-visible and must not be removed by leak guards.

## 4. Template lock

Within a worksheet, repeated instruments of one type use one canonical template unless the task explicitly changes the scale.

Lock:

- outer geometry/orientation
- active range
- topology
- major/minor spacing
- label positions
- stroke hierarchy
- scale-line anchoring baseline/ring
- scale direction
- endpoint/inactive-region behavior
- reserved box/aspect ratio

Only intended pedagogical state changes, e.g. needle angle, hand position, liquid level, object endpoint.

## 5. Topology families

### LINEAR_ENDPOINT_INCLUSIVE

For scale `MIN→MAX` with smallest instructional interval `d`:

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/d`
`EXPECTED_TICK_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`

Require exact representability.

Example: 0–1 cm @1 mm → 10 intervals / 11 positions.

### CYCLIC_FULL_CIRCLE

N equal intervals and N distinct positions; shared wrap endpoint is one location, not a duplicate.

Example: analog clock = 60 minute intervals / 60 distinct minute positions.

### OPEN_ARC_BOUNDED

Active interval count plus endpoint-inclusive active positions. Inactive/non-scale gap contains zero value ticks unless the owning domain explicitly defines otherwise.

Example: canonical 0–5 kg teaching dial = 50 active intervals / 51 positions + 60° inactive gap.

### PROTRACTOR_HALF_CIRCLE

For a canonical 0–180° semicircular protractor with minor interval d:

`intervals=180/d`
`positions=intervals+1`

At 1°: 180 intervals / 181 positions.

## 6. Mandatory SCALE_LINE_SPEC

Before release, every learner-read scale must resolve the shared profile fields including:

`TOPOLOGY_FAMILY, ACTIVE_RANGE, MINOR_INTERVAL, MAJOR_INTERVAL, EXPECTED_INTERVAL_COUNT, EXPECTED_POSITION_COUNT, SCALE_DIRECTION, REFERENCE_BASELINE_OR_RING, TICK_ANCHOR_MODE, MAJOR_MINOR_HIERARCHY, ENDPOINT_BEHAVIOR, MIN_PRINTED_INSTRUMENT_SIZE, MIN_TICK_CENTER_SPACING_MM`.

Add `INACTIVE_REGION_RULE` when applicable.

Missing or vague scale-line state fails `PROMPT_SCALE_LINE_SPEC_QA`.

## 7. General geometry invariants

- exact active range
- exact interval/position count
- uniform spacing
- common baseline/ring anchoring
- no floating/detached ticks
- major/minor hierarchy
- labels aligned to intended marks with clearance
- no missing graduation
- no duplicate/extra/merged graduation
- no instructional tick in inactive/non-scale region
- exact target on valid graduation in exact-reading mode
- scale values monotonic in configured direction
- one canonical template per repeated instrument type
- preserve aspect ratio
- no perspective when it changes reading
- no crop/overlap
- no decorative pointer/tick/ray-like mark

## 8. Scale-line print integrity

Use `SCALE_LINE_INTEGRITY_PROFILE.md` as SSOT. Default lower bounds at final print size:

- minor tick stroke >= 0.25 mm;
- major tick stroke >= 0.35 mm;
- major tick length >= 1.5× minor tick length;
- smallest adjacent tick-center spacing >= 0.60 mm.

If the intended scale cannot satisfy these while preserving readability, increase instrument size or paginate. Never solve density by deleting or merging required ticks.

## 9. Target representability

For a discrete linear scale:

`tick_index=round((target-MIN)/d)`
`represented=MIN+tick_index*d`

Require `target==represented` within tolerance unless interpolation is explicitly part of the learning objective.

The target endpoint/read point must be specified to coincide with the exact intended graduation.

## 10. High-risk prompt serialization

Every learner-read high-risk visual item must contain:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Repeated instruments compile as:

`CANONICAL TEMPLATE + RESOLVED SCALE_LINE_SPEC + ITEM 1 STATE + ... + ITEM N STATE`

Semantic-only instructions such as `show 10:30`, `show 2.4 kg`, or `draw clear scale marks` are insufficient.

No `same as above`, `etc.`, or omitted states.

## 11. Minimum readability

Owning domain defines/derives minimum printed size; the scale-line profile adds minimum tick-center spacing and stroke hierarchy.

When layout pressure threatens the smallest required graduation:

1. use a more efficient layout;
2. reduce/remove decoration;
3. shorten nonessential instruction;
4. reduce nonessential padding;
5. preserve instrument size, scale lines and answer space;
6. paginate when unlocked.

If one-page lock still cannot fit safely, fail feasibility. Never merge/omit graduations to fit.

## 12. Prompt-phase QA

Applicable:

`PROMPT_INSTRUMENT_TEMPLATE_QA`
`PROMPT_TOPOLOGY_QA`
`PROMPT_INTERVAL_COUNT_QA`
`PROMPT_POSITION_COUNT_QA`
`PROMPT_MAJOR_MINOR_QA`
`PROMPT_NO_MISSING_TICK_SPEC_QA`
`PROMPT_NO_EXTRA_TICK_SPEC_QA`
`PROMPT_NON_SCALE_REGION_QA`
`PROMPT_TARGET_REPRESENTABILITY_QA`
`PROMPT_TARGET_ALIGNMENT_SPEC_QA`
`PROMPT_MINIMUM_SIZE_QA`
`PROMPT_PER_ITEM_RENDER_STATE_QA`
`CANONICAL_LABEL_PRESERVATION_QA`

Mandatory scale-line family:

`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_SCALE_UNIFORM_SPACING_QA`
`PROMPT_SCALE_DIRECTION_QA`
`PROMPT_SCALE_LABEL_ALIGNMENT_QA` when labels apply
`PROMPT_SCALE_LABEL_CLEARANCE_QA` when labels apply
`PROMPT_SCALE_TARGET_ALIGNMENT_QA`
`PROMPT_SCALE_INACTIVE_REGION_QA` when applicable
`PROMPT_SCALE_DECORATION_ISOLATION_QA`
`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA`
`PROMPT_SCALE_LINE_SERIALIZATION_QA`

These gates validate the **prompt specification**, not pixels.

## 13. Artifact phase

Before actual downstream image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`

After an artifact exists, inspect every instructional instrument individually:

- shape/orientation
- active range
- exact interval/position count
- no missing/extra/merged tick
- uniform spacing
- common tick anchoring ring/baseline
- major/minor hierarchy
- label placement/clearance
- pointer/hand/level/endpoint target alignment
- inactive-region integrity
- scale direction
- no competing decorative marks
- readability/photocopy quality

One incorrect instructional instrument blocks classroom release.

## 14. Domain authority

The owning domain worker/engine defines domain formulas (clock angles, dial sweep, ruler reference, meniscus convention, protractor direction, graph mapping, etc.). W07/shared engine audits cross-domain invariants and must not invent a conflicting formula.