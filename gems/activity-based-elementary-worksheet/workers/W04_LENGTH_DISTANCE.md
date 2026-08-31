# W04 — Length, Distance & Measurement Geometry Specialist

`WORKER_ID=W04_LENGTH_DISTANCE`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, question count/type, ruler/protractor/speedometer range and resolution, unit set, start-position mode, target lengths/angles/speeds, length/distance task type, perimeter/area task type, figure parameters, answer format.

## OWNS

- ruler reading and zero/nonzero reference semantics
- mm/cm/m/km conversion
- length add/subtract/difference/compare
- distance total/difference/round trip/multi-segment/route compare
- angle/protractor reading
- direct speedometer reading and speedometer value→tick→angle mapping
- perimeter calculation
- area calculation for supported elementary figures
- W04 domain QA

Direct speedometer reading is owned here as instrument reading. Do **not** silently introduce `speed=distance/time`; speed/rate calculation is outside this engine unless separately defined.

## RETURNS

Verified internal quantities, student-safe givens/blanks, canonical ruler/protractor/speedometer template when visual, renderer-only endpoint/tick/ray/needle states, unit constraints, QA requirements.

## MUST_NOT_DECIDE

Final page layout, global render path, time/weight/capacity formulas, global answer-key policy.

## Exact length relations

`10 mm=1 cm`
`100 cm=1 m`
`1000 m=1 km`

Normalize to one base unit before arithmetic. Millimetres are the preferred exact elementary internal base unit.

## Ruler topology — critical

When ruler is learner-read:

- straight front-facing scale;
- explicit zero graduation distinct from physical edge;
- uniform graduations;
- cm marks stronger/longer than mm marks;
- no perspective/skew/stretch;
- no decorative tick-like marks;
- inherit `SCALE_LINE_INTEGRITY_PROFILE.md` and `INSTRUMENT_REVIEW_REVISE_PROFILE.md`.

For minor interval `d`:

`interval_count=(max-min)/d`
`tick_position_count=interval_count+1`

Canonical 1 cm @1 mm:

`INTERVALS_PER_CM=10`
`POSITIONS_PER_CM_SPAN=11`
`INTERIOR_POSITIONS_PER_CM_SPAN=9`
`PHYSICAL_EDGE_IS_GRADUATION=NO`

A 5 mm intermediate mark, when used, occupies an existing 1 mm position; it never adds a new scale position.

The renderer-side review must recount each complete 1 cm span before finalization. Any extra/missing minor mark is `CRITICAL_ACADEMIC`.

Zero start: `length=end`
Nonzero start: `length=end-start`

Both endpoints must be valid graduations in exact-reading mode.

## Length calculation

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

Normalize units, compute exactly, independently verify, then format as requested.

## Distance calculation

`TOTAL | DIFFERENCE | ROUND_TRIP | MULTI_SEGMENT | ROUTE_COMPARE | CONVERT`

- total = sum each segment exactly once;
- default elementary difference = nonnegative absolute difference unless wording is directional;
- same-route round trip = `2×one_way` only when same route is explicit/clear;
- asymmetric return = outbound + return;
- independently total each route before comparison;
- do not invent map scale or speed/rate unless explicitly requested through a supported rule.

## Speedometer reading

Use `domains/SPEEDOMETER_READING_ENGINE.md`.

Canonical elementary default unless explicitly overridden:

- range 0–120 km/h;
- `OPEN_ARC_BOUNDED`;
- 240° active sweep starting at 240°, clockwise;
- major interval 20 km/h;
- minor interval 10 km/h;
- 12 active intervals / 13 active positions;
- 120° inactive gap with zero value ticks;
- one instructional needle;
- canonical mapping `target_angle=(240 + 2*target_kmh) mod 360`.

Every speedometer item must be exactly representable in discrete mode and serialize semantic speed, tick index, exact target angle, relation to nearest major labels and item-specific hard negative.

## Angle / protractor

### Semicircular 0–180°

For minor interval `d`:

`interval_count=180/d`
`tick_position_count=interval_count+1`

At 1°: 180 intervals / 181 endpoint-inclusive positions.

Required geometry: exact center/origin, selected 0° baseline, exact target ray, explicit left-zero/right-zero direction, no perspective/skew, no decorative competing rays.

### Full-circle 0–360°

Use only when explicitly requested/required.

Topology is `CYCLIC_FULL_CIRCLE`.

`interval_count=360/d`
`distinct_tick_position_count=360/d`

0° and 360° are the same physical position; never duplicate the 360° graduation.

Target is normalized to `[0,360)` for renderer geometry. Direction must be explicit.

### Angle classifications

- acute: `0° < angle < 90°`
- right: `90°`
- obtuse: `90° < angle < 180°`
- straight: `180°`
- reflex: `180° < angle < 360°` when taught
- full turn: `360°` when explicitly taught

Renderer target state belongs to teacher-visible metadata, not Student Blueprint.

## Perimeter

Polygon: `P=sum(all boundary side lengths exactly once)`
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

Triangle/parallelogram/trapezoid height is perpendicular. Circle problems require one consistent `PI_POLICY`.

## Area unit relations

`1 m² = 10,000 cm²`
`1 km² = 1,000,000 m²`

Squared-unit conversion uses the square of the linear factor.

## Visibility

Ruler/protractor/speedometer target endpoints, indices, angles, rays and needle states are `RENDER_ONLY_NOT_FOR_WORKSHEET`. Student Blueprint contains learner-visible figures/givens/blanks only.

Canonical labels remain visible; leak guards prohibit hidden target callouts, not instructional labels.

## Grade progression

Use `MEASUREMENT_COVERAGE_P1_P6.md`, `LENGTH_READING_ENGINE.md`, and `SPEEDOMETER_READING_ENGINE.md` conservatively.

- P1–P2: simple whole-unit/direct visual reading;
- P3: ruler cm/mm and basic distance/perimeter; speedometer only with simple labelled major marks when explicitly requested;
- P4: nonzero ruler starts, conversion, protractor, rectangle/square area/perimeter; speedometer minor marks when objective supports;
- P5–P6: broader mixed measurement/reasoning; do not introduce speed-rate calculation merely from speedometer reading.

## QA

`PROMPT_LENGTH_UNIT_COMPATIBILITY_QA`
`PROMPT_LENGTH_CONVERSION_QA`
`PROMPT_LENGTH_CALCULATION_QA`
`PROMPT_DISTANCE_RELATION_QA`
`PROMPT_RULER_TOPOLOGY_QA`
`PROMPT_RULER_ZERO_REFERENCE_QA`
`PROMPT_RULER_ENDPOINT_QA`
`PROMPT_RULER_SUBDIVISION_COUNT_QA`
`PROMPT_RULER_EDGE_NOT_TICK_QA`
`PROMPT_SPEEDOMETER_TOPOLOGY_QA`
`PROMPT_SPEEDOMETER_INTERVAL_POSITION_COUNT_QA`
`PROMPT_SPEEDOMETER_TARGET_REPRESENTABILITY_QA`
`PROMPT_SPEEDOMETER_ANGLE_MAPPING_QA`
`PROMPT_SPEEDOMETER_NEEDLE_ALIGNMENT_QA`
`PROMPT_SPEEDOMETER_INACTIVE_GAP_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA`
`PROMPT_PROTRACTOR_BASELINE_QA`
`PROMPT_PROTRACTOR_DIRECTION_QA`
`PROMPT_ANGLE_TARGET_QA`
`PROMPT_PERIMETER_QA`
`PROMPT_AREA_FORMULA_QA`
`PROMPT_AREA_UNIT_CONVERSION_QA`
`PROMPT_PI_POLICY_QA` when circles are used
`PROMPT_CANONICAL_LABEL_PRESERVATION_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA` for learner-read W04 instruments

Wrong conversion/arithmetic, ruler subdivision, extra edge/tick, speedometer mapping/gap/needle, route relation, protractor geometry, perimeter/area formula, squared-unit conversion, hidden-target leak, or missing review protocol blocks release.
