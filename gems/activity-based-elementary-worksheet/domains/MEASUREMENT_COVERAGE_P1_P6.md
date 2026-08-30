# Measurement Coverage P1–P6 — Activity-Based Elementary Worksheet Generator

Version: 1.0.0
Compatible Gem baseline: 2.6.x
Status: Canonical capability/progression guide

## 1. Purpose

Define what the Gem can generate and validate across elementary measurement topics from ป.1–ป.6.

This document is a **conservative pedagogical progression**, not a claim that every Thai school follows one identical sequence. Use `CURRICULUM_PROFILE` when a specific curriculum mapping is required.

## 2. Formal coverage

### TIME / CLOCK
- read analog clock
- whole hour, half hour, quarter hour, 5-minute and 1-minute precision when grade-appropriate
- 12-hour and 24-hour representations
- day/night paired reading
- start time + duration → end time
- end time − duration → start time
- start/end → elapsed duration
- compare times/schedules
- controlled midnight crossing

### LENGTH / RULER
- direct ruler reading
- zero-start and nonzero-start measurement
- mm, cm, m, km
- cm/mm mixed expression
- addition/subtraction/difference/comparison
- exact metric conversion
- endpoint mapping and graduation counting

### DISTANCE
- total distance
- difference between routes
- round trip
- multiple segments
- route comparison
- m/km conversion
- daily-life/map-style word problems

Speed/rate is not included automatically. Distance remains distance unless speed is explicitly requested.

### WEIGHT / MASS
- dial scale reading
- kg, g, kg+g
- Thai elementary `ขีด` relation when applicable
- add/subtract/difference/compare
- kg↔g conversion
- exact target-to-dial mapping for canonical teaching dial

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

### SOLID VOLUME
- rectangular prism: `V = length × width × height`
- compatible-unit normalization before multiplication
- simple composite shapes made from rectangular prisms when grade-appropriate
- `cm³` and `m³`
- capacity relation `1 cm³ = 1 mL`, `1000 cm³ = 1 L` only when explicitly part of the lesson

## 3. Exact unit relations

Length:

- `10 mm = 1 cm`
- `100 cm = 1 m`
- `1000 m = 1 km`

Weight:

- `1000 g = 1 kg`
- Thai elementary context: `1 ขีด = 100 g = 0.1 kg`

Capacity:

- `1000 mL = 1 L`

Volume/capacity when explicitly taught:

- `1 cm³ = 1 mL`
- `1000 cm³ = 1 L`

Always compute in one canonical base unit before converting the verified result to the requested answer format.

## 4. Conservative grade progression

### ป.1 — Direct comparison and simple whole-unit reading
Recommended AUTO scope:

- compare longer/shorter, heavier/lighter, more/less capacity
- simple direct length measurement with clear whole-unit marks
- familiar whole-unit contexts
- simple clock reading where requested, normally whole-hour emphasis
- no complex mixed-unit conversion by default

Avoid by default:

- dense millimetre graduations
- multi-step conversions
- nonzero ruler starts without explicit teaching intent
- complex elapsed-time regrouping

### ป.2 — Basic instrument reading and one-step measurement arithmetic
Recommended AUTO scope:

- ruler reading with clear cm scale; mm only when explicitly appropriate
- simple m/cm relationships
- basic kg/g contexts
- L and simple capacity comparisons
- hour/minute reading with familiar increments
- one-step addition/subtraction of like units

### ป.3 — Finer graduations and core measurement relationships
Recommended AUTO scope:

- ruler cm/mm reading
- zero and controlled nonzero starts
- kg/ขีด dial reading
- mL/L graduated container reading
- analog clock to 5/30-minute levels as requested
- start/end/duration calculations
- basic length/distance sum/difference
- simple unit conversions using exact integer relationships

### ป.4 — Multi-unit reasoning and route/time applications
Recommended AUTO scope:

- mm/cm/m/km conversion with integer values
- mixed-unit length arithmetic after canonical conversion
- multi-segment distance and round trip
- more varied elapsed-time tasks
- nonzero-start ruler reading
- measurement comparison/difference problems
- capacity/weight conversion and arithmetic

### ป.5 — Mixed units, decimals where appropriate, capacity/volume applications
Recommended AUTO scope:

- decimal or mixed-unit length/weight/capacity conversions when requested/appropriate
- multi-step distance problems
- elapsed-time reasoning with regrouping/cross-hour complexity
- rectangular-prism volume
- capacity-volume relationships when explicitly taught
- thermometer/capacity scales with finer but readable graduations

### ป.6 — Multi-step measurement reasoning
Recommended AUTO scope:

- multi-step conversion + arithmetic
- combined length/distance/time contexts without silently introducing speed
- rectangular-prism and simple composite rectangular-prism volume
- advanced comparison/difference problems
- mixed-unit results and reasoning

The Gem must not automatically raise difficulty merely because a grade is higher. Explicit learning objective remains primary.

## 5. Instrument-specific progression rules

### Ruler
- beginner: start at exact zero
- intermediate: explicit nonzero start and compute `end − start`
- mm scale requires distinguishable 1 mm graduations after printing
- do not confuse physical ruler edge with zero graduation

### Clock
- hour hand moves continuously
- nonzero minutes displace hour hand from numeral
- :30 = midpoint between adjacent numerals
- full minute face = 60 equal intervals / 60 distinct positions

### Dial scale
Canonical 0–5 kg teaching dial:

- 300° active sweep
- 60° inactive gap
- 50 intervals / 51 active positions at 0.1 kg
- no ticks in inactive gap

### Thermometer / capacity
- discrete targets must be exactly representable by minor division
- endpoint/read point aligns exactly with intended graduation
- target values may control renderer geometry but must not become learner-visible callouts

## 6. Calculation integrity

For measurement arithmetic:

1. parse each quantity and unit;
2. convert to one canonical base unit;
3. perform exact arithmetic;
4. independently recompute/verify;
5. convert verified result to requested display unit;
6. build student-visible givens/blanks without answer leakage.

Never add values with incompatible units before conversion.

## 7. Distance integrity

Supported distance task types:

`TOTAL | DIFFERENCE | ROUND_TRIP | MULTI_SEGMENT | ROUTE_COMPARE | CONVERT`

Examples:

- total: `a+b+c`
- difference: `|routeA-routeB|`
- same-route round trip: `2×one_way_distance`
- asymmetric round trip: `outbound + return`

Do not assume outbound and return distances are equal unless the problem states/safely implies the same route.

## 8. Volume integrity

Rectangular prism:

`V = length × width × height`

All three dimensions must be in compatible units before multiplication.

Simple composite rectangular prisms:

- decompose into non-overlapping rectangular prisms;
- compute each verified volume;
- sum exactly once;
- do not double-count overlap.

Complex solids outside this explicit grammar route to generic support and must not claim deterministic specialized coverage.

## 9. Coverage QA

Applicable gates:

`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`
`PROMPT_UNIT_COMPATIBILITY_QA`
`PROMPT_UNIT_CONVERSION_QA`
`PROMPT_MEASUREMENT_CALCULATION_QA`
`PROMPT_DISTANCE_RELATION_QA`
`PROMPT_RULER_REFERENCE_QA`
`PROMPT_INSTRUMENT_TOPOLOGY_QA`
`PROMPT_VOLUME_FORMULA_QA`
`PROMPT_VOLUME_DECOMPOSITION_QA` when composite volume is used

Any wrong unit relationship, wrong arithmetic, ambiguous reference point, or unsupported complexity presented as specialized deterministic coverage blocks prompt release.