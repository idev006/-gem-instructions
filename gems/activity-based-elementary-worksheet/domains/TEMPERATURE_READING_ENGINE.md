# TEMPERATURE_READING_ENGINE — Thermometer Reading

Version: 1.5.0
Status: PRODUCTION_CANDIDATE
Owning worker: `W05_TEMPERATURE_CAPACITY_VOLUME`
Visual auditor: `W07_INSTRUMENT_AUDITOR`
Requires: `INSTRUMENT_READING_ENGINE.md`, `policies/SCALE_LINE_INTEGRITY_PROFILE.md`, `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
Compatible Gem baseline: 2.6.x

## 1. Learning goal

Student reads temperature from a clear graduated thermometer scale and, when requested, compares temperature/change using verified values.

The learner may infer the scale relation directly from the image, so graduation count, scale direction, hierarchy, label association and liquid endpoint are academic data.

## 2. Core parameters

`MIN_TEMP`
`MAX_TEMP`
`MAJOR_INTERVAL`
`INTERMEDIATE_INTERVAL` when used
`MINOR_INTERVAL`
`UNIT=C|F`
`TARGET_TEMPERATURES`
`ORIENTATION=VERTICAL|HORIZONTAL`
`ANSWER_FORMAT`

## 3. Geometry invariants

- one straight authoritative scale axis;
- no perspective/skew/stretch;
- direction locked across repeated items;
- equal numeric intervals map to equal geometric spacing;
- every required graduation is present exactly once;
- major/intermediate/minor hierarchy is mutually exclusive and consistent;
- labels align to major ticks with clearance;
- zero/minus signs clear when applicable;
- one unambiguous liquid endpoint/read point;
- no decorative strokes resembling ticks, labels or a second liquid endpoint;
- repeated thermometers use one canonical template unless scale parameters intentionally change.

All thermometer scales inherit the shared scale-line integrity profile.

## 4. Deterministic topology

Let `d=MINOR_INTERVAL`.

`EXPECTED_INTERVAL_COUNT=(MAX_TEMP-MIN_TEMP)/d`
`EXPECTED_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`

Require exact divisibility/representability of the configured range.

Canonical safe profiles:

- 0–50°C @1°C → 50 intervals / 51 positions
- -10–40°C @1°C → 50 intervals / 51 positions; zero index=10
- 0–100°C @5°C → 20 intervals / 21 positions
- 20–120°F @2°F → 50 intervals / 51 positions

## 5. Canonical 0–50°C @1°C teaching profile — critical

For the common Primary 4 profile:

`MIN_TEMP=0`
`MAX_TEMP=50`
`MINOR_INTERVAL=1`
`INTERMEDIATE_INTERVAL=5`
`MAJOR_INTERVAL=10`
`EXPECTED_INTERVAL_COUNT=50`
`EXPECTED_POSITION_COUNT=51`
`SCALE_DIRECTION=BOTTOM_TO_TOP`

Tick index set:

`i=0..50`
`value(i)=i °C`

Mutually exclusive hierarchy:

- major positions: `i % 10 == 0` → values `0,10,20,30,40,50`; exactly 6 major positions; longest ticks; labeled;
- intermediate positions: `i % 5 == 0 AND i % 10 != 0` → values `5,15,25,35,45`; exactly 5 intermediate positions; medium ticks; unlabeled by default;
- minor positions: all remaining indices; exactly 40 minor positions; shortest ticks.

For every consecutive pair of 10°C major ticks there are:

- exactly 10 equal intervals;
- exactly 9 interior graduation positions;
- exactly one 5°C intermediate position;
- exactly eight ordinary 1°C minor positions.

No hierarchy level adds an extra physical tick position.

## 6. Physical mapping

For a printed scale length `L` from the 0 tick centerline to the 50 tick centerline:

`tick_center_spacing_mm=L/50`

The metrology floor is 0.60 mm unless a stronger rule applies, so the mathematical spacing-derived minimum scale length is:

`METROLOGY_MINIMUM_SCALE_LENGTH_MM=50*0.60=30 mm`

A larger `SELECTED_RENDER_SIZE_MM` may be chosen for readability, but must not be mislabeled as the metrology minimum.

Example: if selected scale length is 60 mm, spacing is exactly `1.20 mm`; valid claims are `=1.20 mm`, `>=1.20 mm`, or `>0.60 mm`, not `>1.20 mm`.

## 7. Target mapping — critical

For target `t`:

`tick_index=round((t-MIN_TEMP)/d)`
`represented_value=MIN_TEMP+tick_index*d`

Require exact equality within tolerance in discrete mode.

The liquid endpoint must coincide exactly with the target graduation centerline. Do not place it between ticks unless interpolation is explicitly part of the learning objective.

The bulb and liquid stem below the 0 graduation are not extra scale positions.

## 8. Renderer-only item state

Every visual item serializes one atomic renderer-only block containing:

`ITEM_ID`
`SEMANTIC_TARGET_TEMPERATURE`
`TICK_INDEX`
`REPRESENTED_VALUE`
`LEVEL_RATIO`
`TARGET_TICK_Y`
`NEAREST_MAJOR_LABELS`
`RELATIONAL_VERIFICATION`
`ITEM_SPECIFIC_HARD_NEGATIVE`

Mark:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

Do not print target temperature as an extra annotation/completed answer when answer key is off. Canonical configured scale labels remain visible.

## 9. Mandatory SCALE_LINE_SPEC

The canonical thermometer template must resolve at least:

`TOPOLOGY_FAMILY=LINEAR_ENDPOINT_INCLUSIVE`
`ACTIVE_RANGE=MIN_TEMP..MAX_TEMP`
`MINOR_INTERVAL`
`INTERMEDIATE_INTERVAL` when applicable
`MAJOR_INTERVAL`
`EXPECTED_INTERVAL_COUNT`
`EXPECTED_POSITION_COUNT`
`SCALE_DIRECTION`
`REFERENCE_BASELINE_OR_RING=THERMOMETER_SCALE_AXIS`
`TICK_ANCHOR_MODE=COMMON_AXIS`
`MAJOR_INTERMEDIATE_MINOR_HIERARCHY`
`ENDPOINT_BEHAVIOR=ENDPOINT_INCLUSIVE`
`METROLOGY_MINIMUM_SCALE_LENGTH_MM`
`SELECTED_RENDER_SIZE_MM`
`MIN_TICK_CENTER_SPACING_MM`

## 10. Mandatory renderer self-review / revise

Final Prompt must include the shared `INSTRUMENT_REVIEW_REVISE_PROTOCOL` and:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Before finalizing each thermometer, the downstream renderer must independently:

1. recount `(MAX_TEMP-MIN_TEMP)/MINOR_INTERVAL` intervals and +1 positions;
2. for 0–50°C @1°C, verify exactly 51 tick positions;
3. verify each 10°C span has exactly 10 equal intervals / 9 interior positions;
4. verify 6 major + 5 intermediate + 40 minor positions with no extra positions;
5. confirm uniform spacing and bottom-to-top direction;
6. confirm major/intermediate/minor hierarchy and label association;
7. recompute target tick index and represented value;
8. verify the visible liquid endpoint lies exactly on the target graduation centerline;
9. verify no extra/missing/merged/floating tick and no decorative competing line;
10. repair/regenerate any mismatch and run the entire checklist again.

A vague `looks correct` review is insufficient. A visually attractive but numerically wrong thermometer is `CRITICAL_ACADEMIC`.

Renderer self-review is prevention only and never proves artifact QA.

## 11. Grade progression

Use `MEASUREMENT_COVERAGE_P1_P6.md` conservatively.

Do not select unnecessarily fine scales for early grades merely because they are mathematically representable. Fahrenheit, negative ranges or interpolation require objective/context appropriate to the lesson.

## 12. QA

Prompt-phase:

`PROMPT_THERMOMETER_TOPOLOGY_QA`
`PROMPT_THERMOMETER_INTERVAL_COUNT_QA`
`PROMPT_THERMOMETER_POSITION_COUNT_QA`
`PROMPT_THERMOMETER_TEN_DEGREE_SPAN_QA`
`PROMPT_THERMOMETER_HIERARCHY_COUNT_QA`
`PROMPT_TEMP_TARGET_REPRESENTABILITY_QA`
`PROMPT_TEMP_ENDPOINT_ALIGNMENT_SPEC_QA`
`PROMPT_TEMP_SCALE_DIRECTION_QA`
`PROMPT_TEMP_LABEL_ALIGNMENT_QA`
`PROMPT_NO_BETWEEN_TICKS_QA`
`PROMPT_TEMP_LABEL_PRESERVATION_QA`
`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`

Wrong graduation count, missing/extra 1°C tick, wrong hierarchy count, nonrepresentable target, between-tick endpoint, reversed scale, wrong label alignment, missing review/revise protocol or learner-visible target leakage blocks prompt release.

## 13. Artifact boundary

Actual visual alignment/count remains:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

until the rendered worksheet is supplied and inspected. One incorrect thermometer blocks classroom release and must become a permanent regression.
