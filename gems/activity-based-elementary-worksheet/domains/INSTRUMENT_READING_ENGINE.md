# INSTRUMENT_READING_ENGINE — Shared Educational Geometry Rules

Version: 1.5.0
Status: Mandatory shared rules for learner-read visual instruments
Owning cross-domain worker: `W07_INSTRUMENT_AUDITOR`
Compatible Gem baseline: 2.6.x
Requires: `policies/SCALE_LINE_INTEGRITY_PROFILE.md`, `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`

Applies to analog clocks, weight/dial scales, rulers, speedometers, thermometers, graduated capacity instruments, protractors, and learner-read graph/axis geometry.

## 1. Core principle

If the learner must read a visual instrument, its geometry is **academic data**.

`INSTRUMENT_GEOMETRY > CONTEXT_ART > DECORATION`

A missing/extra tick, wrong pointer, distorted scale, ambiguous start point, unreadable graduation, or wrong target alignment is a critical academic defect.

All learner-read instruments inherit both mandatory profiles:

- `SCALE_LINE_INTEGRITY_PROFILE.md`
- `INSTRUMENT_REVIEW_REVISE_PROFILE.md`

The domain worker owns numeric meaning; W07 audits physical scale-line integrity and renderer self-review coverage.

## 2. Three layers

1. `CONTEXT_LAYER` — decoration/support only.
2. `INSTRUCTIONAL_INSTRUMENT_LAYER` — authoritative object the learner reads.
3. `RESPONSE_LAYER` — blank/student answer area.

Never make a decorative mini-instrument the authoritative reading object.

## 3. Visibility

Academic target values/indices/angles/levels belong to teacher-visible renderer metadata when needed to draw the instrument. Mark:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

Student Blueprint must not expose hidden target values, indices, angles, levels, or solved answers. Canonical labels remain student-visible.

## 4. Template lock

Repeated instruments of one configured type use one canonical template unless the task intentionally changes the scale.

Lock:

- outer geometry/orientation
- active range/topology
- major/minor spacing
- label positions
- stroke hierarchy
- scale-line baseline/ring/arc
- scale direction
- endpoint/inactive-region behavior
- reserved box/aspect ratio

Only intended state changes, e.g. needle angle, hand position, liquid level, object endpoint.

## 5. Topology families

### LINEAR_ENDPOINT_INCLUSIVE

For scale `MIN→MAX` with smallest instructional interval `d`:

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/d`
`EXPECTED_TICK_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`
`EXPECTED_INTERIOR_POSITION_COUNT=max(EXPECTED_TICK_POSITION_COUNT-2,0)`

Canonical ruler 0–1 cm @1 mm:

- 10 intervals
- 11 positions
- 9 interior positions
- physical edge is not an extra graduation

### CYCLIC_FULL_CIRCLE

N equal intervals and N distinct positions; shared wrap endpoint is one location, not a duplicate.

Analog clock = 60 minute intervals / 60 distinct minute positions.

### OPEN_ARC_BOUNDED

Active interval count plus endpoint-inclusive active positions. Inactive/non-scale gap contains zero value ticks unless the owning domain explicitly defines otherwise.

Examples:

- canonical 0–5 kg dial = 50 active intervals / 51 positions + 60° inactive gap
- canonical 0–120 km/h speedometer = 12 active intervals / 13 positions + 120° inactive gap

### PROTRACTOR_HALF_CIRCLE

For 0–180° and minor interval d:

`intervals=180/d`
`positions=intervals+1`

At 1°: 180 intervals / 181 positions.

## 6. Mandatory SCALE_LINE_SPEC

Before release, every learner-read scale resolves:

`TOPOLOGY_FAMILY`
`ACTIVE_RANGE`
`MINOR_INTERVAL`
`MAJOR_INTERVAL`
`EXPECTED_INTERVAL_COUNT`
`EXPECTED_POSITION_COUNT`
`SCALE_DIRECTION`
`REFERENCE_BASELINE_OR_RING`
`TICK_ANCHOR_MODE`
`MAJOR_MINOR_HIERARCHY`
`ENDPOINT_BEHAVIOR`
`MIN_PRINTED_INSTRUMENT_SIZE`
`MIN_TICK_CENTER_SPACING_MM`

Add `INACTIVE_REGION_RULE` when applicable.

Missing/vague state fails `PROMPT_SCALE_LINE_SPEC_QA`.

## 7. General invariants

- exact active range and interval/position count
- uniform spacing and monotonic direction
- common baseline/ring/arc anchoring
- no floating/detached/merged/duplicate/extra ticks
- major/minor hierarchy
- labels aligned to intended marks with clearance
- no instructional tick in inactive region
- exact target on valid graduation in exact-reading mode
- one canonical template per repeated scale
- no perspective/crop/overlap that changes reading
- no decorative competing pointer/tick/ray/grid mark

## 8. Scale-line print integrity

Use `SCALE_LINE_INTEGRITY_PROFILE.md` as SSOT. Default lower bounds at final print size:

- minor stroke >= 0.25 mm
- major stroke >= 0.35 mm
- major tick length >= 1.5× minor tick length
- adjacent smallest tick-center spacing >= 0.60 mm

If these cannot be preserved, increase instrument size or paginate. Never delete/merge required ticks.

## 9. Target representability

For a discrete linear/open-arc scale:

`tick_index=round((target-MIN)/d)`
`represented=MIN+tick_index*d`

Require exact representability within tolerance unless interpolation is explicitly taught.

Target endpoint/read point must coincide with the intended graduation.

## 10. High-risk prompt serialization

Every learner-read item must contain an atomic renderer-only state:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL/ENDPOINT + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Repeated instruments compile as:

`CANONICAL TEMPLATE + RESOLVED SCALE_LINE_SPEC + ITEM 1 STATE + ... + ITEM N STATE`

Semantic-only instructions such as `show 10:30`, `show 2.4 kg`, `show 60 km/h`, or `draw clear scale marks` are insufficient.

## 11. Mandatory renderer self-review/revise loop

Every final prompt with learner-read instruments must serialize:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

and:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

The review must independently recount expected positions and verify anchoring, spacing, hierarchy, labels, target alignment, inactive regions, decoration isolation and template consistency.

If any mismatch is detected, repair/regenerate and repeat the full review. `Looks correct` is not sufficient evidence.

## 12. Domain-specific recount oracles

### Ruler 1 cm @1 mm
10 intervals / 11 positions / 9 interior positions; physical border not a graduation.

### Thermometer
Recompute `(MAX-MIN)/MINOR_INTERVAL`; endpoint exactly on target graduation; no between-tick endpoint in discrete mode.

### Speedometer canonical 0–120 km/h
240° active sweep, 120° inactive gap, 10 km/h minor interval, 12 intervals / 13 positions; target angle `(240+2*target_kmh) mod 360`; no gap ticks.

### Clock
60 distinct minute positions; continuous hour-hand geometry.

### Weight dial
Canonical active sweep/gap and exact needle mapping.

### Protractor
Exact origin/baseline/direction and graduation count.

### Graduated container
Exact scale count and read point.

### Graph axis
Uniform value interval ↔ uniform geometric spacing; data marks map to canonical data.

## 13. Prompt-phase QA

Core geometry:

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

Scale-line family:

`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_SCALE_UNIFORM_SPACING_QA`
`PROMPT_SCALE_DIRECTION_QA`
`PROMPT_SCALE_LABEL_ALIGNMENT_QA`
`PROMPT_SCALE_LABEL_CLEARANCE_QA`
`PROMPT_SCALE_TARGET_ALIGNMENT_QA`
`PROMPT_SCALE_INACTIVE_REGION_QA`
`PROMPT_SCALE_DECORATION_ISOLATION_QA`
`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA`
`PROMPT_SCALE_LINE_SERIALIZATION_QA`

Review/revise family:

`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`

Any applicable FAIL or NOT_RUN blocks prompt release.

## 14. Artifact phase

Before actual downstream image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`

After artifact exists, inspect every instructional instrument individually for exact count, spacing, anchoring, hierarchy, labels, target alignment, inactive-region integrity, competing marks, and print readability.

One incorrect instructional instrument blocks classroom release and becomes a permanent regression.

## 15. Domain authority

The owning domain worker/engine defines formulas (clock angles, dial sweep, ruler reference, speedometer mapping, meniscus convention, protractor direction, graph mapping). W07 audits cross-domain invariants and must not invent conflicting formulas.
