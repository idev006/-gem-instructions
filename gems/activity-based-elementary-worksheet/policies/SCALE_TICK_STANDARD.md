# Scale Tick Standard

Version: 1.0.0
Status: Mandatory cross-skill standard
Applies to: every worksheet skill that contains a learner-read scale, tick mark, axis, dial, pointer, hand, ray, liquid level, or graduated reference.

## 1. Principle

Scale truth is academic truth.

A scale, tick, pointer, hand, ray, liquid endpoint, or graph axis is not decorative artwork. It is part of the teaching content.

If a child can learn a false measurement model from it, the defect is critical.

`SCALE_TICK_STANDARD_QA=MANDATORY`
`CRITICAL_SCALE_DEFECT=CRITICAL_ACADEMIC_DEFECT`

## 2. Required scale specification fields

Every scale-based skill MUST serialize the following before layout/render:

- `SCALE_FAMILY`
- `ACTIVE_RANGE`
- `MINOR_INTERVAL`
- `MAJOR_INTERVAL`
- `INTERMEDIATE_INTERVAL` when applicable
- `EXPECTED_INTERVAL_COUNT`
- `EXPECTED_POSITION_COUNT`
- `EXPECTED_INTERIOR_TICK_COUNT`
- `SCALE_DIRECTION`
- `REFERENCE_ORIGIN_OR_CENTER`
- `TICK_ANCHOR_MODE`
- `MAJOR_TICK_DEFINITION`
- `INTERMEDIATE_TICK_DEFINITION`
- `MINOR_TICK_DEFINITION`
- `LABEL_TO_TICK_ASSOCIATION_RULE`
- `TARGET_ALIGNMENT_RULE`
- `MIN_TICK_CENTER_SPACING_MM`
- `TICK_LENGTH_RATIOS`

Missing required fields means `PROMPT_SCALE_TICK_STANDARD_QA=FAIL`.

## 3. Intervals vs positions

Do not confuse intervals with positions.

Example: 1 kg divided by 0.1 kg:
- intervals = 10;
- endpoint-inclusive positions = 11;
- interior tick marks between endpoints = 9.

A midpoint/intermediate tick is an existing subdivision position made visually stronger. It is not an extra new mark that changes interval count.

## 4. Tick hierarchy

Default visible hierarchy:

- Major tick: longest/strongest, associated with primary label values.
- Intermediate tick: longer/stronger than minor ticks, shorter/weaker than major ticks.
- Minor tick: shortest/weakest ordinary subdivision.

Recommended relative length ratios:

`MAJOR_TICK_LENGTH_RATIO=1.00`
`INTERMEDIATE_TICK_LENGTH_RATIO=0.72..0.80`
`MINOR_TICK_LENGTH_RATIO=0.45..0.55`

When exact vector rendering is possible, prefer fixed ratios:

`MAJOR=1.00`
`INTERMEDIATE=0.75`
`MINOR=0.50`

Thickness may reinforce hierarchy but must not replace length hierarchy.

## 5. Mandatory recount gates

Every scale must pass:

- `PROMPT_TICK_COUNT_INTEGRITY_QA`
- `PROMPT_INTERVAL_COUNT_INTEGRITY_QA`
- `PROMPT_POSITION_COUNT_INTEGRITY_QA`
- `PROMPT_INTERIOR_TICK_COUNT_QA`
- `PROMPT_TICK_LENGTH_HIERARCHY_QA`
- `PROMPT_LABEL_TO_TICK_ASSOCIATION_QA`
- `PROMPT_TARGET_ALIGNMENT_QA`
- `PROMPT_REFERENCE_ORIGIN_OR_CENTER_QA`
- `PROMPT_NO_DECORATIVE_PSEUDO_TICK_QA`

Artifact inspection must repeat the equivalent visual checks.

## 6. Skill-specific examples

### Analog clock
- 60 minute positions.
- 12 hour numeral positions.
- 5-minute marks may be visually stronger than ordinary minute ticks.
- Hour hand moves continuously: 15:30 has the minute hand at 6 and the hour hand halfway between 3 and 4.

### Weight dial 0–5 kg @0.1 kg
- Whole dial: 50 intervals / 51 positions.
- Each 1 kg span: 10 intervals / 11 positions / 9 interior marks.
- 0.5 kg midpoint tick is intermediate and visually longer than ordinary 0.1 kg ticks.
- Pointer tip must land on the canonical target tick.

### Ruler 1 cm @1 mm
- Each 1 cm span: 10 mm intervals / 11 positions / 9 interior marks.
- 5 mm mark is intermediate.
- Centimeter mark is major.
- Physical edge is never substituted for zero graduation unless explicitly specified.

### Thermometer 0–50°C @1°C
- 50 intervals / 51 positions.
- 10°C major, 5°C intermediate, 1°C minor.
- Liquid endpoint aligns exactly to the target graduation.

### Protractor 0–180° @1°
- 180 intervals / 181 positions.
- 10° major, 5° intermediate, 1° minor.
- All ticks and rays are radial from the common center.

### Speedometer 0–120 km/h @10
- 12 intervals / 13 positions.
- Pointer pivot equals dial center.
- Inactive gap has no scale-like pseudo ticks.

### Capacity / graduated container
- Global and local spans are both counted.
- Level/meniscus read point is specified.
- No local pseudo-subdivisions may appear.

### Bar graph / data axis
- Axis tick spacing is uniform.
- Bar height maps exact canonical data values.
- Decorative marks may not resemble data ticks.

## 7. Release blocker

Any missing/extra tick, wrong interval count, wrong tick hierarchy, label mismatch, wrong pointer/hand/ray/liquid endpoint, wrong zero/center/origin, or data-axis mismatch is non-compensatory.

`CRITICAL_SCALE_DEFECT => ARTIFACT_QA=FAIL`
`CRITICAL_SCALE_DEFECT => CLASSROOM_RELEASE=BLOCKED`
