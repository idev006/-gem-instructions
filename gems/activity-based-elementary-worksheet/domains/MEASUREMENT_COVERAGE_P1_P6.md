# Measurement Coverage P1–P6 — Activity-Based Elementary Worksheet Generator

Version: 1.2.0
Compatible Gem baseline: 2.6.x
Status: Canonical capability/progression guide

## 1. Purpose

Define formal worksheet-generation coverage for elementary measurement topics from ป.1–ป.6.

This is a conservative pedagogical progression, not a claim that every Thai school follows one identical sequence. Explicit valid teacher objectives and `CURRICULUM_PROFILE` remain primary.

For any learner-read scale/instrument, the scale itself is academic data and must inherit scale-line integrity plus mandatory renderer review/revise behavior.

## 2. Formal coverage

### TIME / CLOCK

- read analog clock
- whole/half/quarter hour, 5-minute and 1-minute precision when grade-appropriate
- seconds/time-unit conversion when explicitly taught
- 12-hour and 24-hour representations
- day/night paired reading
- start + duration → end
- end − duration → start
- start/end → elapsed duration
- compare times/schedules
- controlled midnight crossing

Exact time relations:

`60 seconds = 1 minute`
`60 minutes = 1 hour`
`24 hours = 1 day`

### LENGTH / RULER

- direct ruler reading
- zero-start and nonzero-start measurement
- mm, cm, m, km
- addition/subtraction/difference/comparison
- exact metric conversion
- endpoint mapping and graduation counting

Exact length relations:

`10 mm = 1 cm`
`100 cm = 1 m`
`1000 m = 1 km`

Canonical 1 cm @1 mm:

- 10 intervals
- 11 endpoint-inclusive positions
- 9 interior positions
- physical ruler border/edge is not an extra graduation

### DISTANCE

- total distance
- difference between routes
- round trip
- multiple segments
- route comparison
- m/km conversion
- daily-life/map-style word problems

Distance remains distance. Do not silently introduce speed/rate.

### SPEEDOMETER READING

Supports **direct reading of a vehicle speedometer** as an instrument-reading skill.

Canonical elementary profile:

- range 0–120 km/h
- `OPEN_ARC_BOUNDED`
- active sweep 240° starting at 240°, clockwise
- major interval 20 km/h
- minor interval 10 km/h
- 12 active intervals
- 13 active positions
- 120° inactive gap with zero value ticks
- one instructional needle
- `target_angle=(240+2*target_kmh) mod 360`

Direct speedometer reading does not automatically enable `speed=distance/time` calculation.

### ANGLE / PROTRACTOR

- identify/compare angles
- read a semicircular protractor
- explicit baseline ray and selected scale direction
- acute/right/obtuse/straight classification
- target angle aligned to exact graduation
- optional construction prompts when explicitly requested

Canonical 0–180° @1°:

- 180 intervals
- 181 endpoint-inclusive positions
- exact origin
- selected 0° baseline
- exact target graduation

### PERIMETER / AREA

Perimeter:
- polygon = sum boundary sides exactly once
- rectangle `P=2(l+w)`
- square `P=4s`

Area when grade/objective supports:
- rectangle `A=l×w`
- square `A=s²`
- triangle `A=1/2×b×h`
- parallelogram `A=b×h`
- trapezoid `A=1/2×(a+b)×h`
- circle `A=πr²`
- circumference `C=2πr=πd`

Circle tasks require one consistent `PI_POLICY`.

Area-unit relations:

`1 m² = 10,000 cm²`
`1 km² = 1,000,000 m²`

Area conversions square the linear conversion factor.

### WEIGHT / MASS

- dial scale reading
- kg, g, kg+g
- Thai elementary ขีด when applicable
- add/subtract/difference/compare
- kg↔g conversion
- optional metric tonne when explicitly requested

Exact relations:

`1000 g = 1 kg`
`1000 kg = 1 metric tonne`
`1 ขีด = 100 g = 0.1 kg`

### TEMPERATURE

- read thermometer
- °C and °F when requested/appropriate
- compare temperature/change
- exact discrete tick representability
- exact liquid-endpoint alignment
- negative ranges when objective supports them

Canonical safe profiles include:

- 0–50°C @1°C → 50 intervals /51 positions
- 0–100°C @5°C → 20 /21
- -10–40°C @1°C → 50 /51, zero index 10
- 20–120°F @2°F → 50 /51

### CAPACITY

- read graduated container
- mL/L
- add/subtract/difference/compare
- mL↔L conversion
- simple flat liquid level
- scientific meniscus when explicitly requested

Exact relation:

`1000 mL = 1 L`

### SOLID VOLUME

- rectangular prism: `V = length × width × height`
- compatible linear units before multiplication
- simple composite shapes made from non-overlapping rectangular prisms
- cm³, dm³, m³
- capacity-volume relation when explicitly part of the lesson

Exact cubic relations:

`1000 cm³ = 1 dm³`
`1000 dm³ = 1 m³`
`1 m³ = 1,000,000 cm³`

Capacity-volume relations when explicitly taught:

`1 cm³ = 1 mL`
`1 dm³ = 1 L`
`1 m³ = 1000 L`

Cubic-unit conversion uses the cube of the linear factor.

## 3. Calculation integrity

For measurement arithmetic:

1. parse quantity/unit;
2. normalize to one compatible canonical unit;
3. compute exactly;
4. independently recompute/verify;
5. convert verified result to requested display unit;
6. build student-visible givens/blanks without answer leakage.

Never add/subtract incompatible units as raw numerals.

## 4. Learner-read instrument integrity

Every learner-read instrument/axis uses:

- owning deterministic domain engine;
- `INSTRUMENT_READING_ENGINE.md`;
- `SCALE_LINE_INTEGRITY_PROFILE.md` when ticks/graduations/axis intervals are read;
- `INSTRUMENT_REVIEW_REVISE_PROFILE.md`.

Required renderer prevention behavior:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

The review independently recounts scale topology/count and checks target alignment. It is not a substitute for actual artifact QA.

## 5. Conservative grade progression

### ป.1

Recommended AUTO:
- direct comparison and simple whole-unit concepts
- simple clock whole-hour tasks when requested
- no dense scales or advanced conversions by default

### ป.2

Recommended AUTO:
- clear cm ruler reading
- simple m/cm contexts
- basic kg/g and L contexts
- familiar hour/minute increments
- one-step like-unit arithmetic

### ป.3

Recommended AUTO:
- ruler cm/mm reading with exact 1 mm subdivisions
- controlled nonzero ruler starts
- kg/ขีด dial reading
- mL/L graduated-container reading
- analog clock common minute increments/day-night where profile requires
- start/end/duration calculations
- basic length/distance sum/difference
- simple exact unit conversion
- basic perimeter when requested
- **simple speedometer reading on labelled major marks when explicitly requested**
- simple thermometer reading with readable whole-unit/friendly intervals

### ป.4

Recommended AUTO:
- mm/cm/m/km integer conversion
- mixed-unit length arithmetic
- multi-segment/round-trip distance
- protractor reading
- rectangle/square perimeter and area
- kg/g and L/mL arithmetic/conversion
- **speedometer minor-tick reading such as 10 km/h intervals when explicitly requested**
- broader thermometer profiles including finer but readable intervals

### ป.5

Recommended AUTO:
- mixed/decimal metric conversion when appropriate
- multi-step distance/time contexts
- triangle/parallelogram/trapezoid area when taught
- rectangular-prism volume
- cm³/dm³ and capacity-volume relation when explicitly taught
- thermometer/capacity scales with finer but readable graduations

### ป.6

Recommended AUTO:
- multi-step conversion + arithmetic
- combined length/distance/time contexts without silently introducing speed-rate
- polygon/circle perimeter/area when explicitly requested
- consistent π policy
- rectangular/simple-composite prism volume
- cm³/dm³/m³ conversion when appropriate
- advanced comparison/difference problems

Higher grade does not automatically mean harder/finer scale. Learning objective remains primary.

## 6. Instrument-specific canonical rules

### Ruler
- beginner: exact zero start
- advanced: nonzero start and `end-start`
- 1 cm @1 mm = 10 intervals /11 positions /9 interior positions
- physical border/edge is not a graduation
- 5 mm hierarchy mark occupies an existing position

### Clock
- hour hand moves continuously
- nonzero minutes displace hour hand
- :30 = midpoint between adjacent numerals
- full minute face = 60 intervals /60 distinct positions
- seconds hand only when explicitly requested

### Speedometer
- default 0–120 km/h open arc
- 12 intervals /13 active positions at 10 km/h minor interval
- 120° inactive gap with zero value ticks
- one needle
- exact value-to-angle mapping
- no silent rate calculation

### Protractor
- vertex exactly at origin
- baseline ray exactly at selected 0°
- second ray intersects exact target graduation
- active scale direction unambiguous

### Weight dial
Canonical 0–5 kg @0.1 kg:
- 300° active sweep
- 60° inactive gap
- 50 intervals /51 positions
- no ticks in inactive gap

### Thermometer
- exact range/interval/position count
- target representable in discrete mode
- liquid endpoint exactly on intended graduation centerline
- no reversed scale or extra tick

### Graduated container
- exact scale topology/count
- exact flat level or designated meniscus read point
- no competing decorative reading line

### Graph axis
- equal numeric intervals = equal geometric intervals
- data/bar endpoint maps exactly to canonical value
- grid lines correspond exactly to configured ticks if used

## 7. Layout/readability rule

When scale density threatens readability:

1. preserve academic values/count;
2. preserve exact scale topology;
3. preserve minimum tick separation/stroke hierarchy;
4. reduce decoration;
5. shorten nonessential instruction/padding;
6. increase instrument size;
7. paginate when unlocked.

Never delete/merge/shift graduations to fit one page.

## 8. Artifact boundary

Before actual rendered image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

One wrong learner-read scale in the artifact blocks classroom release and must become permanent regression evidence.

## 9. Coverage QA

Applicable gates include:

`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`
`PROMPT_UNIT_COMPATIBILITY_QA`
`PROMPT_UNIT_CONVERSION_QA`
`PROMPT_TIME_UNIT_CONVERSION_QA`
`PROMPT_MEASUREMENT_CALCULATION_QA`
`PROMPT_DISTANCE_RELATION_QA`
`PROMPT_RULER_REFERENCE_QA`
`PROMPT_RULER_SUBDIVISION_COUNT_QA`
`PROMPT_RULER_EDGE_NOT_TICK_QA`
`PROMPT_SPEEDOMETER_TOPOLOGY_QA`
`PROMPT_SPEEDOMETER_ANGLE_MAPPING_QA`
`PROMPT_THERMOMETER_INTERVAL_COUNT_QA`
`PROMPT_TEMP_ENDPOINT_ALIGNMENT_SPEC_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA`
`PROMPT_PROTRACTOR_BASELINE_QA`
`PROMPT_ANGLE_TARGET_QA`
`PROMPT_PERIMETER_QA`
`PROMPT_AREA_FORMULA_QA`
`PROMPT_AREA_UNIT_CONVERSION_QA`
`PROMPT_PI_POLICY_QA` when circles are used
`PROMPT_INSTRUMENT_TOPOLOGY_QA`
`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_VOLUME_FORMULA_QA`
`PROMPT_CUBIC_UNIT_CONVERSION_QA`
`PROMPT_VOLUME_DECOMPOSITION_QA`

Wrong unit relation, arithmetic/formula, instrument count/reference, route assumption, target alignment, scale topology, squared/cubic conversion, or unsupported complexity presented as deterministic specialized coverage blocks prompt release.
