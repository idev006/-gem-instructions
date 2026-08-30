# INSTRUMENT_READING_ENGINE — Shared Educational Geometry Rules

Version: 1.3.0
Status: Mandatory shared rules for learner-read visual instruments
Owning cross-domain worker: `W07_INSTRUMENT_AUDITOR`
Compatible Gem baseline: 2.6.x

Applies to analog clocks, dial scales, rulers, thermometers, graduated capacity instruments, and learner-read graph/axis geometry.

## 1. Core principle

If the learner must read a visual instrument, its geometry is **academic data**.

`INSTRUMENT GEOMETRY > CONTEXT ART > DECORATION`

A missing/extra tick, wrong pointer, distorted scale, ambiguous start point, or unreadable graduation is not a minor art defect.

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

## 6. General geometry invariants

- exact active range
- exact interval/position count
- uniform spacing
- major/minor hierarchy
- labels aligned to intended marks
- no missing graduation
- no duplicate/extra graduation
- no instructional tick in inactive/non-scale region
- exact target on valid graduation for exact-reading mode
- preserve aspect ratio
- no perspective if it changes reading
- no crop/overlap
- no decorative pointer/tick-like mark

## 7. Target representability

For a discrete linear scale:

`tick_index=round((target-MIN)/d)`
`represented=MIN+tick_index*d`

Require `target==represented` within tolerance unless interpolation is explicitly part of the learning objective.

The target endpoint/read point must be specified to coincide with the exact intended graduation.

## 8. High-risk prompt serialization

Every learner-read high-risk visual item must contain:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Semantic-only instructions such as `show 10:30` or `show 2.4 kg` are insufficient.

Repeated instruments compile as:

`CANONICAL TEMPLATE + ITEM 1 STATE + ... + ITEM N STATE`

No `same as above`, `etc.`, or omitted states.

## 9. Minimum readability

Owning domain defines/derives minimum printed size.

When layout pressure threatens the smallest required graduation:

1. use a more efficient layout;
2. reduce/remove decoration;
3. shorten nonessential instruction;
4. reduce nonessential padding;
5. preserve instrument size and answer space.

If one-page lock still cannot fit safely, fail feasibility. Never merge/omit graduations to fit.

## 10. Prompt-phase QA

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

These gates validate the **prompt specification**, not pixels.

## 11. Artifact phase

Before actual downstream image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`

After an artifact exists, inspect every instructional instrument individually:

- shape/orientation
- active range
- interval/position count
- spacing
- label placement
- pointer/hand/level/endpoint
- target alignment
- no missing/extra marks
- readability/photocopy quality

One incorrect instructional instrument blocks classroom release.

## 12. Domain authority

The owning domain worker/engine defines domain formulas (clock angles, dial sweep, ruler reference, meniscus convention, etc.). W07/shared engine audits cross-domain invariants and must not invent a conflicting formula.