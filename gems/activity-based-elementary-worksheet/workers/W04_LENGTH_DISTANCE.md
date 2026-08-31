# W04 — Length, Distance & Measurement Geometry Specialist

`WORKER_ID=W04_LENGTH_DISTANCE`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, question count/type, ruler/protractor range/resolution, unit set, start-position mode, target lengths/angles, length/distance task type, perimeter/area task type, figure parameters, answer format.

## OWNS

- ruler reading
- zero/nonzero reference semantics
- mm/cm/m/km conversion
- length add/subtract/difference/compare
- distance total/difference/round trip/multi-segment/route compare
- angle reading with 0–180° semicircular or 0–360° full-circle protractor when explicitly requested
- perimeter calculation
- area calculation for supported elementary figures
- length/distance/angle/perimeter/area QA

## RETURNS

Verified internal quantities, student-safe givens/blanks, canonical ruler/protractor template when visual, renderer-only endpoint/tick/ray states, unit-conversion constraints, QA requirements.

## MUST_NOT_DECIDE

Final page layout, global render path, time/weight/capacity formulas, global answer-key policy.

## Exact length relations

`10 mm=1 cm`
`100 cm=1 m`
`1000 m=1 km`

Normalize to one base unit before arithmetic. Millimetres are the preferred exact elementary internal base unit.

## Ruler topology

When ruler is learner-read:

- straight front-facing scale
- explicit zero graduation distinct from physical edge
- uniform graduations
- cm marks stronger than mm marks
- no perspective/skew/stretch
- no decorative tick-like marks

For minor interval `d`:

`interval_count=(max-min)/d`
`tick_position_count=interval_count+1`

Canonical 1 cm @1 mm: 10 equal intervals / 11 endpoint-inclusive positions.

Zero start: `length=end`
Nonzero start: `length=end-start`

Both endpoints must be valid graduations in exact-reading mode.

## Length calculation

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

Normalize units, compute exactly, independently verify, then format as requested.

## Distance calculation

`TOTAL | DIFFERENCE | ROUND_TRIP | MULTI_SEGMENT | ROUTE_COMPARE | CONVERT`

- total = sum each segment exactly once
- default elementary difference = nonnegative absolute difference unless wording is directional
- same-route round trip = `2×one_way` only when same route is explicit/clear
- asymmetric return = outbound + return
- independently total each route before comparison
- do not invent map scale or speed/rate unless explicitly requested

## Angle / protractor

### Semicircular 0–180°

For minor interval `d`:

`interval_count=180/d`
`tick_position_count=interval_count+1`

At 1° resolution: 180 intervals / 181 endpoint-inclusive positions.

Required geometry:

- vertex exactly at center/origin
- one baseline ray exactly aligned with selected 0° direction
- second ray intersects exact target graduation
- selected left-zero/right-zero scale direction explicit
- dual-scale labels may exist but active scale must be unambiguous
- no perspective/skew
- no decorative radial lines resembling rays

### Full-circle 0–360°

Use only when `PROTRACTOR_RANGE=0_360` is explicitly requested or curriculum/objective requires a full-turn measuring instrument.

Topology is `CYCLIC_FULL_CIRCLE`, not endpoint-inclusive linear duplication.

For minor interval `d` where `360/d` is an integer:

`interval_count=360/d`
`distinct_tick_position_count=360/d`

The 0° and 360° directions are the **same physical position**; do not draw a duplicate 360° graduation at the origin.

At 1° resolution: 360 equal intervals / 360 distinct positions.

Required geometry:

- exact center/origin
- one baseline ray exactly on selected 0° direction
- direction explicit as clockwise or counterclockwise
- target ray intersects exact target graduation
- target normalized to `[0,360)` for renderer geometry; a pedagogical answer of 360° is allowed only for a full-turn concept explicitly taught
- no duplicated 0°/360° physical mark
- no perspective/skew
- no decorative radial lines resembling measurement rays

### Angle classifications

- acute: `0° < angle < 90°`
- right: `90°`
- obtuse: `90° < angle < 180°`
- straight: `180°`
- reflex: `180° < angle < 360°` when taught
- full turn: `360°` when explicitly taught

Renderer-only target angle/tick/ray state belongs to teacher-visible metadata, not Student Blueprint.

## Perimeter

General polygon: `P=sum(all boundary side lengths exactly once)`
Rectangle: `P=2(l+w)`
Square: `P=4s`

Normalize side units before addition.

## Area

Rectangle: `A=l×w`
Square: `A=s²`
Triangle: `A=1/2×b×h`
Parallelogram: `A=b×h`
Trapezoid: `A=1/2×(a+b)×h`
Circle when explicitly requested: `A=πr²`, `C=2πr=πd`

Triangle/parallelogram/trapezoid height is the perpendicular height.

Circle problems require one consistent `PI_POLICY` such as `3.14`, `22/7`, symbolic π, or teacher-defined custom policy.

## Area unit relations

`1 m² = 10,000 cm²`
`1 km² = 1,000,000 m²`

Squared-unit conversion uses the square of the linear factor.

## Visibility

Ruler/protractor target endpoints, ticks, angles and ray positions are `RENDER_ONLY_NOT_FOR_WORKSHEET`. Student Blueprint contains only learner-visible figures/givens/blanks.

Canonical ruler/protractor labels remain visible; leak guards prohibit hidden target callouts, not instructional scale labels.

## Grade progression

Use `domains/MEASUREMENT_COVERAGE_P1_P6.md` and `domains/LENGTH_READING_ENGINE.md` conservatively.

- P1–P2: direct length/perimeter intuition and simple whole-unit tasks
- P3: ruler cm/mm and basic perimeter/distance
- P4: nonzero ruler starts, unit conversion, semicircular protractor, rectangle/square perimeter/area
- P5: broader area/mixed units
- P6: polygon/circle measurement; full-circle protractor only when explicitly taught/requested

## QA

`PROMPT_LENGTH_UNIT_COMPATIBILITY_QA`
`PROMPT_LENGTH_CONVERSION_QA`
`PROMPT_LENGTH_CALCULATION_QA`
`PROMPT_DISTANCE_RELATION_QA`
`PROMPT_RULER_TOPOLOGY_QA`
`PROMPT_RULER_ZERO_REFERENCE_QA`
`PROMPT_RULER_ENDPOINT_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA`
`PROMPT_PROTRACTOR_BASELINE_QA`
`PROMPT_PROTRACTOR_DIRECTION_QA`
`PROMPT_ANGLE_TARGET_QA`
`PROMPT_PERIMETER_QA`
`PROMPT_AREA_FORMULA_QA`
`PROMPT_AREA_UNIT_CONVERSION_QA`
`PROMPT_PI_POLICY_QA` when circles are used
`PROMPT_CANONICAL_LABEL_PRESERVATION_QA`

Wrong conversion/arithmetic, route relation, ruler reference, protractor topology/baseline/direction, perimeter/area formula, squared-unit conversion, or hidden-target leak blocks release.