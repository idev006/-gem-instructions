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
- angle reading with a protractor
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

Normalize to one base unit before arithmetic. For exact elementary integer metric work, millimetres are the preferred internal base unit.

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

Canonical 1 cm @1 mm:

- 10 equal intervals
- 11 endpoint-inclusive positions

Zero start: `length=end`

Nonzero start: `length=end-start`

Both endpoints must be valid graduations in exact-reading mode.

## Length calculation

Task types:

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

Normalize units, compute exactly, independently verify, then format as requested.

## Distance calculation

Task types:

`TOTAL | DIFFERENCE | ROUND_TRIP | MULTI_SEGMENT | ROUTE_COMPARE | CONVERT`

- total = sum each segment exactly once
- default elementary difference = nonnegative absolute difference unless wording is directional
- same-route round trip = `2×one_way` only when same route is explicit/clear
- asymmetric return = outbound + return
- independently total each route before comparison

Do not invent map scale or speed/rate unless explicitly requested.

## Angle / protractor

Supported elementary angle reading uses a canonical protractor with an explicit selected scale direction.

For a semicircular 0–180° protractor with minor interval `d`:

`interval_count=180/d`
`tick_position_count=interval_count+1`

For 1° resolution: 180 intervals / 181 positions.

Geometry invariants:

- vertex exactly at protractor center/origin
- one baseline ray aligned exactly with selected 0° direction
- second ray intersects the exact target graduation
- selected scale direction stated unambiguously
- dual-scale labels may exist but must not create ambiguity about which 0° baseline is active
- no perspective/skew
- no decorative radial lines that resemble angle rays

Angle classifications:

- acute: `0° < angle < 90°`
- right: `90°`
- obtuse: `90° < angle < 180°`
- straight: `180°`
- full turn: `360°` when explicitly taught

Renderer-only target angle/tick state belongs to teacher-visible metadata, not Student Blueprint.

## Perimeter

General polygon perimeter:

`P=sum(all side lengths exactly once)`

Rectangle:
`P=2(l+w)`

Square:
`P=4s`

Normalize side units before addition.

## Area

Supported deterministic formulas:

Rectangle:
`A=l×w`

Square:
`A=s²`

Triangle:
`A=1/2×b×h`

Parallelogram:
`A=b×h`

Trapezoid when grade/objective supports:
`A=1/2×(a+b)×h`

Circle when explicitly requested:
`A=πr²`
`C=2πr=πd`

For circle problems, `PI_POLICY` must be explicit or safely derived from teacher/curriculum context, e.g. `3.14` or `22/7`. Do not mix π approximations within one worksheet.

## Area unit relations

`1 m² = 10,000 cm²`
`1 km² = 1,000,000 m²`

When converting squared units, square the linear conversion factor. Do not convert area using a linear factor.

## Visibility

Ruler/protractor target endpoints, ticks, angles and ray positions used for drawing are `RENDER_ONLY_NOT_FOR_WORKSHEET`. Student Blueprint contains only learner-visible figures/givens/blanks.

Canonical ruler/protractor labels remain visible; leak guard prohibits hidden target callouts, not scale labels.

## Grade progression

Use `domains/MEASUREMENT_COVERAGE_P1_P6.md` and `domains/LENGTH_READING_ENGINE.md`.

Conservative AUTO:

- P1–P2: direct length/perimeter intuition and simple whole-unit tasks
- P3: ruler cm/mm and basic perimeter/distance
- P4: nonzero ruler starts, unit conversion, angle/protractor, rectangle/square perimeter/area
- P5: triangle/parallelogram/trapezoid area when objective supports; mixed-unit measurement
- P6: polygon/circle measurement and multi-step area/perimeter reasoning when requested

Do not force advanced geometry merely because grade is higher.

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
`PROMPT_ANGLE_TARGET_QA`
`PROMPT_PERIMETER_QA`
`PROMPT_AREA_FORMULA_QA`
`PROMPT_AREA_UNIT_CONVERSION_QA`
`PROMPT_PI_POLICY_QA` when circles are used
`PROMPT_CANONICAL_LABEL_PRESERVATION_QA`

Wrong conversion/arithmetic, route relation, ruler reference, protractor baseline/scale, perimeter/area formula, squared-unit conversion, or hidden-target leak blocks release.