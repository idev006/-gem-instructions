# TEMPERATURE_READING_ENGINE — Thermometer Reading

Version: 1.4.0
Status: PRODUCTION_CANDIDATE
Owning worker: `W05_TEMPERATURE_CAPACITY_VOLUME`
Visual auditor: `W07_INSTRUMENT_AUDITOR`
Requires: `INSTRUMENT_READING_ENGINE.md`, `policies/SCALE_LINE_INTEGRITY_PROFILE.md`, `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
Compatible Gem baseline: 2.6.x

## 1. Learning goal

Student reads temperature from a clear graduated thermometer scale and, when requested, compares temperature/change using verified values.

The learner may infer the scale relation directly from the image, so graduation count, scale direction and liquid endpoint are academic data.

## 2. Core parameters

`MIN_TEMP`
`MAX_TEMP`
`MAJOR_INTERVAL`
`MINOR_INTERVAL`
`UNIT=C|F`
`TARGET_TEMPERATURES`
`ORIENTATION=VERTICAL|HORIZONTAL`
`ANSWER_FORMAT`

## 3. Geometry invariants

- one straight authoritative scale axis;
- no perspective/skew/stretch;
- direction locked across repeated items;
- uniform graduations;
- major/minor hierarchy consistent;
- labels aligned to major ticks with clearance;
- zero/minus signs clear when applicable;
- one unambiguous liquid endpoint/read point;
- no decorative strokes resembling ticks, labels or a second liquid endpoint;
- repeated thermometers use one canonical template unless scale parameters intentionally change.

All thermometer scales inherit the shared scale-line integrity profile.

## 4. Deterministic topology

Let `d=MINOR_INTERVAL`.

`EXPECTED_INTERVAL_COUNT=round((MAX_TEMP-MIN_TEMP)/d)`
`EXPECTED_TICK_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`

Require exact divisibility/representability of the configured range.

Canonical safe profiles:

- 0–50°C @1°C → 50 intervals / 51 positions
- -10–40°C @1°C → 50 intervals / 51 positions; zero index=10
- 0–100°C @5°C → 20 intervals / 21 positions
- 20–120°F @2°F → 50 intervals / 51 positions

## 5. Target mapping — critical

For target `t`:

`tick_index=round((t-MIN_TEMP)/d)`
`represented_value=MIN_TEMP+tick_index*d`

Require `abs(t-represented_value)<tolerance` in discrete mode.

The liquid endpoint must coincide exactly with the target graduation centerline. Do not place it between ticks unless interpolation is explicitly part of the learning objective.

Example: with 20–120°F @2°F:

- 36°F → valid, tick index 8
- 35°F → invalid in default discrete mode

## 6. Renderer-only item state

Every visual item serializes one atomic renderer-only block containing:

`ITEM_ID`
`SEMANTIC_TARGET_TEMPERATURE`
`TICK_INDEX`
`REPRESENTED_VALUE`
`LEVEL_RATIO`
`NEAREST_MAJOR_LABELS`
`RELATIONAL_VERIFICATION`
`ITEM_SPECIFIC_HARD_NEGATIVE`

Mark:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

Do not print target temperature as an extra annotation/completed answer when answer key is off. Canonical configured scale labels remain visible.

## 7. Mandatory SCALE_LINE_SPEC

The canonical thermometer template must resolve at least:

`TOPOLOGY_FAMILY=LINEAR_ENDPOINT_INCLUSIVE`
`ACTIVE_RANGE=MIN_TEMP..MAX_TEMP`
`MINOR_INTERVAL`
`MAJOR_INTERVAL`
`EXPECTED_INTERVAL_COUNT`
`EXPECTED_POSITION_COUNT`
`SCALE_DIRECTION`
`REFERENCE_BASELINE_OR_RING=THERMOMETER_AXIS`
`TICK_ANCHOR_MODE=COMMON_AXIS`
`MAJOR_MINOR_HIERARCHY`
`ENDPOINT_BEHAVIOR=ENDPOINT_INCLUSIVE`
`MIN_PRINTED_INSTRUMENT_SIZE`
`MIN_TICK_CENTER_SPACING_MM`

## 8. Mandatory renderer self-review / revise

Final Prompt must include the shared `INSTRUMENT_REVIEW_REVISE_PROTOCOL` and:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Before finalizing each thermometer, the downstream renderer must independently:

1. recount `(MAX_TEMP-MIN_TEMP)/MINOR_INTERVAL` intervals and +1 positions;
2. confirm uniform spacing and configured direction;
3. confirm major/minor hierarchy and label alignment;
4. recompute the target tick index and represented value;
5. verify the visible liquid endpoint lies exactly on that graduation centerline;
6. verify no extra/missing/merged/floating tick and no decorative competing line;
7. repair/regenerate any mismatch;
8. run the entire checklist again after repair.

A vague `looks correct` review is insufficient. A visually attractive but numerically wrong thermometer is `CRITICAL_ACADEMIC`.

Renderer self-review is prevention only and never proves artifact QA.

## 9. Grade progression

Use `MEASUREMENT_COVERAGE_P1_P6.md` conservatively.

Do not select unnecessarily fine scales for early grades merely because they are mathematically representable. Fahrenheit, negative ranges or interpolation require objective/context appropriate to the lesson.

## 10. QA

Prompt-phase:

`PROMPT_THERMOMETER_TOPOLOGY_QA`
`PROMPT_THERMOMETER_INTERVAL_COUNT_QA`
`PROMPT_THERMOMETER_POSITION_COUNT_QA`
`PROMPT_TEMP_TARGET_REPRESENTABILITY_QA`
`PROMPT_TEMP_ENDPOINT_ALIGNMENT_SPEC_QA`
`PROMPT_TEMP_SCALE_DIRECTION_QA`
`PROMPT_TEMP_LABEL_ALIGNMENT_QA`
`PROMPT_NO_BETWEEN_TICKS_QA`
`PROMPT_TEMP_LABEL_PRESERVATION_QA`
`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`

Wrong graduation count, nonrepresentable target, between-tick endpoint, reversed scale, wrong label alignment, missing review/revise protocol or learner-visible target leakage blocks prompt release.

## 11. Artifact boundary

Actual visual alignment/count remains:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

until the rendered worksheet is supplied and inspected. One incorrect thermometer blocks classroom release and must become a permanent regression.
