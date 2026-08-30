# Measurement Coverage P1–P6 — Activity-Based Elementary Worksheet Generator

Version: 1.1.0
Compatible Gem baseline: 2.6.x
Status: Canonical capability/progression guide

## 1. Purpose

Define formal worksheet-generation coverage for elementary measurement topics from ป.1–ป.6.

This document is a **conservative pedagogical progression**, not a claim that every Thai school follows one identical sequence. Use `CURRICULUM_PROFILE` when a specific mapping is required.

## 2. Formal coverage

### TIME / CLOCK

- read analog clock
- whole hour, half hour, quarter hour, 5-minute and 1-minute precision when grade-appropriate
- seconds/time-unit conversion when explicitly taught
- 12-hour and 24-hour representations
- day/night paired reading
- start time + duration → end time
- end time − duration → start time
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
- cm/mm and mixed metric expression
- addition/subtraction/difference/comparison
- exact metric conversion
- endpoint mapping and graduation counting

Exact length relations:

`10 mm = 1 cm`
`100 cm = 1 m`
`1000 m = 1 km`

### DISTANCE

- total distance
- difference between routes
- round trip
- multiple segments
- route comparison
- m/km conversion
- daily-life/map-style word problems

Speed/rate is not included automatically. Distance remains distance unless speed is explicitly requested.

### ANGLE / PROTRACTOR

- identify/compare angles
- read a semicircular protractor
- explicit baseline ray and selected scale direction
- acute/right/obtuse/straight classification
- target angle aligned to exact graduation
- optional drawing/construction prompts when explicitly requested

Canonical 0–180° protractor with 1° resolution:

- 180 intervals
- 181 endpoint-inclusive positions
- vertex at exact origin
- one ray at selected 0° baseline
- second ray at exact target graduation

Dual-scale protractors must make the active direction unambiguous.

### PERIMETER

- polygon perimeter = sum all side lengths exactly once
- rectangle `P=2(l+w)`
- square `P=4s`
- mixed-unit perimeter after unit normalization

### AREA

Supported deterministic formulas when grade/objective supports them:

- rectangle `A=l×w`
- square `A=s²`
- triangle `A=1/2×b×h`
- parallelogram `A=b×h`
- trapezoid `A=1/2×(a+b)×h`
- circle `A=πr²`
- circle circumference `C=2πr=πd`

Circle tasks require one explicit `PI_POLICY`, e.g. `3.14` or `22/7`, used consistently within the worksheet.

Area-unit relations:

`1 m² = 10,000 cm²`
`1 km² = 1,000,000 m²`

Area conversions square the linear conversion factor; never use a linear factor for squared units.

### WEIGHT / MASS

- dial scale reading
- kg, g, kg+g
- Thai elementary `ขีด` relation when applicable
- add/subtract/difference/compare
- kg↔g conversion
- optional metric-tonne conversion when explicitly requested

Exact relations:

`1000 g = 1 kg`
`1000 kg = 1 metric tonne`
Thai elementary context: `1 ขีด = 100 g = 0.1 kg`

### TEMPERATURE

- read thermometer
- °C / °F scale when requested
- compare temperature/change
- exact discrete tick representability

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

Cubic-unit conversion uses the **cube** of the linear conversion factor.

## 3. Calculation integrity

For any measurement arithmetic:

1. parse each quantity and unit;
2. convert to one canonical compatible unit;
3. perform exact arithmetic/formula;
4. independently recompute/verify;
5. convert verified result to requested display unit;
6. build student-visible givens/blanks without answer leakage.

Never add/subtract incompatible units as raw numerals.

## 4. Conservative grade progression

### ป.1 — direct comparison/basic whole-unit concepts

Recommended AUTO:

- compare longer/shorter, heavier/lighter, more/less capacity
- simple whole-unit length measurement
- simple clock whole-hour tasks when requested
- intuitive boundary/perimeter language only when objective calls for it
- no dense mm scales, multi-step conversion, scientific meniscus or advanced area formulas by default

### ป.2 — basic instrument reading and one-step measurement arithmetic

Recommended AUTO:

- clear cm ruler reading
- simple m/cm contexts
- basic kg/g and L contexts
- hour/minute reading with familiar increments
- one-step like-unit addition/subtraction
- simple perimeter by counting/summing clearly given sides when appropriate

### ป.3 — finer graduations and core relationships

Recommended AUTO:

- ruler cm/mm reading
- controlled nonzero ruler starts
- kg/ขีด dial reading
- mL/L graduated container reading
- analog clock common minute increments
- start/end/duration calculations
- basic length/distance sum/difference
- simple exact unit conversions
- basic perimeter of rectangles/squares when requested

### ป.4 — multi-unit reasoning and measurement geometry

Recommended AUTO:

- mm/cm/m/km integer conversion
- mixed-unit length arithmetic
- multi-segment/round-trip distance
- varied elapsed-time tasks
- nonzero ruler starts
- kg/g and L/mL conversion/arithmetic
- angle reading with a protractor
- rectangle/square perimeter and area
- seconds/time-unit conversion when objective supports it

### ป.5 — mixed units, area and volume applications

Recommended AUTO:

- mixed/decimal metric conversion when appropriate
- multi-step distance/time problems
- triangle/parallelogram/trapezoid area when taught
- rectangular-prism volume
- cm³/dm³ and capacity-volume relations when explicitly taught
- thermometer/capacity scales with finer but readable graduations

### ป.6 — multi-step measurement reasoning

Recommended AUTO:

- multi-step conversion + arithmetic
- combined length/distance/time contexts without silently introducing speed
- polygon/circle perimeter/area when explicitly requested
- consistent π policy for circle problems
- rectangular-prism and simple composite rectangular-prism volume
- cm³/dm³/m³ conversion when appropriate
- advanced comparison/difference problems

The Gem must not automatically raise complexity merely because a grade is higher. Explicit learning objective remains primary.

## 5. Instrument-specific rules

### Ruler

- beginner: exact zero start
- advanced: explicit nonzero start and `end-start`
- 1 cm @1 mm = 10 intervals / 11 positions
- physical ruler edge is not the zero graduation

### Clock

- hour hand moves continuously
- nonzero minutes displace hour hand
- :30 = midpoint between adjacent numerals
- full minute face = 60 intervals / 60 distinct positions
- seconds hand only when explicitly requested

### Protractor

- vertex exactly at origin
- baseline ray exactly at selected 0°
- second ray intersects exact target graduation
- selected inner/outer scale direction unambiguous
- no decorative radial lines that resemble angle rays

### Dial scale

Canonical 0–5 kg @0.1 kg:

- 300° active sweep
- 60° inactive gap
- 50 intervals / 51 active positions
- no ticks in inactive gap

### Thermometer / capacity

- discrete targets exactly representable by minor interval
- endpoint/read point exactly on intended graduation
- target value controls renderer geometry but is not a learner-visible callout

## 6. Distance integrity

Task types:

`TOTAL | DIFFERENCE | ROUND_TRIP | MULTI_SEGMENT | ROUTE_COMPARE | CONVERT`

- total = sum verified segments once
- difference = absolute or directional according to wording
- same-route round trip = `2×one_way` only when same route is explicit/clear
- asymmetric return = outbound + return

Do not invent map scale or speed.

## 7. Area/perimeter integrity

- normalize side/dimension units before formulas
- perimeter counts boundary lengths, not interior diagonals unless explicitly part of boundary
- area uses square units
- height in triangle/parallelogram/trapezoid formulas must be perpendicular height, not an arbitrary slanted side
- circle tasks use one consistent π policy

## 8. Volume integrity

Rectangular prism:

`V=l×w×h`

All dimensions must be in one compatible linear unit before multiplication.

Composite rectangular prisms:

- decompose into non-overlapping components
- compute each once
- no double-counted overlap

Complex solids outside this grammar route to generic support and must not claim specialized deterministic coverage.

## 9. Coverage QA

Applicable gates include:

`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`
`PROMPT_UNIT_COMPATIBILITY_QA`
`PROMPT_UNIT_CONVERSION_QA`
`PROMPT_TIME_UNIT_CONVERSION_QA`
`PROMPT_MEASUREMENT_CALCULATION_QA`
`PROMPT_DISTANCE_RELATION_QA`
`PROMPT_RULER_REFERENCE_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA`
`PROMPT_PROTRACTOR_BASELINE_QA`
`PROMPT_ANGLE_TARGET_QA`
`PROMPT_PERIMETER_QA`
`PROMPT_AREA_FORMULA_QA`
`PROMPT_AREA_UNIT_CONVERSION_QA`
`PROMPT_PI_POLICY_QA` when circles are used
`PROMPT_INSTRUMENT_TOPOLOGY_QA`
`PROMPT_VOLUME_FORMULA_QA`
`PROMPT_CUBIC_UNIT_CONVERSION_QA`
`PROMPT_VOLUME_DECOMPOSITION_QA`

Wrong unit relation, arithmetic/formula, ruler/protractor reference, route assumption, squared/cubic conversion, instrument topology or unsupported complexity presented as deterministic specialized coverage blocks prompt release.