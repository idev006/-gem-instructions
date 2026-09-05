# Instrument Tick Hierarchy Policy

Version: 1.0.0
Status: Mandatory for learner-read instruments
Depends on: `policies/SCALE_TICK_STANDARD.md`

## 1. Purpose

Children learn scale structure from line length, line repetition, labels, and pointer alignment. Tick hierarchy must therefore be intentional and consistent.

`INSTRUMENT_TICK_HIERARCHY_QA=MANDATORY`

## 2. Hierarchy levels

### Major tick
A major tick represents the main labeled value.

Requirements:
- longest visible tick in its local span;
- aligned with its label;
- never hidden by decoration;
- all major ticks in the same instrument class have consistent length.

### Intermediate tick
An intermediate tick represents a meaningful subdivision such as half unit, 5 mm, 5°C, 5°, or other lesson-appropriate midpoint.

Requirements:
- longer than ordinary minor ticks;
- shorter/weaker than major ticks;
- located exactly at the canonical subdivision position;
- not added as an extra interval-changing mark.

### Minor tick
A minor tick represents the smallest visible subdivision.

Requirements:
- equal length within the same scale class;
- equal spacing when the quantity is linear;
- no missing or extra minor ticks.

## 3. Recommended default ratios

Use these when the skill does not provide stricter ratios:

- `MAJOR_TICK_LENGTH_RATIO=1.00`
- `INTERMEDIATE_TICK_LENGTH_RATIO=0.75`
- `MINOR_TICK_LENGTH_RATIO=0.50`

Acceptable tolerance for rendered artifacts:
- major must be visibly longer than intermediate;
- intermediate must be visibly longer than minor;
- no intermediate tick may be confused with a missing or extra major label tick.

## 4. Common skill mappings

| Skill | Major | Intermediate | Minor |
|---|---|---|---|
| Analog clock | hour numeral / 5-minute mark when minute tick scale is shown | optional quarter emphasis only when pedagogically chosen | ordinary minute tick |
| Weight dial | whole kg | half kg | 0.1 kg |
| Ruler | centimeter | 5 mm | 1 mm |
| Thermometer | labeled 10°C or 10°F | 5-unit midpoint | 1-unit or configured minor |
| Protractor | 10° | 5° | 1° |
| Speedometer | labeled major speed | configured midpoint such as 10 km/h when labels are 20 km/h apart | configured minor |
| Capacity vessel | labeled major volume | half-span volume | configured minor |
| Graph axis | labeled major grid line | optional minor grid line | tick/grid subdivision |

## 5. Failure modes

The following are critical when they affect student reading:
- intermediate tick absent;
- intermediate tick same length as minor when lesson depends on half-step recognition;
- minor ticks absent in some spans but present in others;
- major label offset from its tick;
- decorative strokes look like scale ticks;
- pointer/ray/liquid endpoint aligns to decoration instead of real tick.

## 6. QA gates

- `PROMPT_TICK_HIERARCHY_DECLARED_QA`
- `PROMPT_TICK_HIERARCHY_RATIO_QA`
- `PROMPT_INTERMEDIATE_TICK_LOCATION_QA`
- `PROMPT_MAJOR_LABEL_ALIGNMENT_QA`
- `PROMPT_MINOR_TICK_CONSISTENCY_QA`
- `ARTIFACT_TICK_HIERARCHY_VISIBLE_QA`

Any failure that can change the reading blocks release.
