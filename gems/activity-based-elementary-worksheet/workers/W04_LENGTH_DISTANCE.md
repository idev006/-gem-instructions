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

A 5 mm intermediate mark occupies an existing 1 mm position; it never adds a new scale position.

The renderer-side review must recount each complete 1 cm span before finalization. Any extra/missing minor mark is `CRITICAL_ACADEMIC`.

Zero start: `length=end`
Nonzero start: `length=end-start`

Both endpoints must be valid graduations in exact-reading mode.

### Ruler endpoint projection/reference contract

For an object drawn above the ruler, W04 returns exact reference geometry:

`OBJECT_START_X == START_GRADUATION_X`
`OBJECT_END_X == END_GRADUATION_X`
`START_PROJECTION_GUIDE_X = OBJECT_START_X = START_GRADUATION_X`
`END_PROJECTION_GUIDE_X = OBJECT_END_X = END_GRADUATION_X`

The start/end guides are thin dashed vertical helper lines from the exact object endpoints to the ruler reading zone. They must be perpendicular to the ruler baseline and visually distinct from ruler graduations. They do not count as ticks and may not obscure/create/duplicate a graduation.

For `ZERO_START_MODE`:

`OBJECT_START_X == ZERO_GRADUATION_X`
`START_GRADUATION_VALUE=0`

The physical ruler edge is not the measurement origin unless it coincides exactly with the zero graduation by explicit template definition. Default elementary templates keep the zero graduation visibly distinct from the physical border.

For `NONZERO_START_MODE`:

`TARGET_LENGTH = END_VALUE - START_VALUE`

Both projection guides remain present so the subtraction relation is visually explicit.

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
- angle convention `0°=top`, clockwise positive;
- 240° active sweep starting at 240°, clockwise;
- major interval 20 km/h;
- minor interval 10 km/h;
- 12 active intervals / 13 active positions;
- 120° inactive gap with zero value ticks/pseudo-ticks;
- one instructional needle;
- canonical mapping `target_angle=(240 + 2*target_kmh) mod 360`;
- `NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER` exactly.

Every speedometer item must be exactly representable in discrete mode and serialize semantic speed, tick index, normalized exact target angle, dial center, pivot-equals-center constraint, relation to nearest major labels and item-specific hard negative.

An off-center pivot is a release blocker even if the needle tip visually reaches the intended tick.

## Angle / protractor

### Semicircular 0–180°

For minor interval `d`:

`interval_count=180/d`
`tick_position_count=interval_count+1`

At 1°: 180 intervals / 181 endpoint-inclusive positions.

### Canonical coordinate system — mandatory

Use a perfect, undistorted upper semicircle generated from one center/origin:

`PROTRACTOR_CENTER=(cx,cy)`
`PROTRACTOR_RADIUS=R`
`BASELINE_LEFT=(cx-R,cy)`
`BASELINE_RIGHT=(cx+R,cy)`

Screen-coordinate convention (`y` increases downward):

- 0° = right horizontal direction;
- 90° = straight up;
- 180° = left horizontal direction;
- active scale reads counter-clockwise from right 0° to left 180°.

Outer reading-arc point at angle θ:

`OUTER(θ)=(cx + R*cos(θ), cy - R*sin(θ))`

Every graduation is radial from the same center. For tick inner radius `r(θ)`:

`INNER(θ)=(cx + r(θ)*cos(θ), cy - r(θ)*sin(θ))`

Required coincidence:

`ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == PROTRACTOR_CENTER`

Required shape:

`WIDTH=2R`
`SEMICIRCLE_BODY_HEIGHT=R`

Do not treat protractor width as its vertical body height. A 70 mm wide semicircular protractor has `R=35 mm` and a 35 mm semicircle body before label/answer/clearance reserves.

### Scale construction

For 0–180° @1°:

- exactly 180 equal 1° intervals / 181 positions;
- one active numeric scale only by default;
- labels `0,10,20,...,180` associated with their exact major ticks;
- 10° positions are major;
- 5° positions are intermediate and reuse existing 1° positions;
- all other integer-degree positions are minor;
- no second mirrored/complementary number row unless the explicit learning objective is dual-scale selection;
- no perspective, ellipse, non-uniform stretch, shear or local arc distortion;
- baseline must be straight and pass exactly through the center;
- target ray starts exactly at `PROTRACTOR_CENTER` and intersects the exact target graduation;
- no decorative competing rays.

For dense 1° learner-read protractors:

`tick_center_spacing_mm = reading_radius_mm × radians(1)`

With default `MIN_TICK_CENTER_SPACING_MM=0.60`:

`MIN_READING_RADIUS_MM ≈ 34.38`
`MIN_READING_RING_DIAMETER_MM ≈ 68.76`
`PRODUCTION_MIN_PROTRACTOR_WIDTH_MM=70`

A 65 mm wide protractor is invalid because its 1° reading-ring spacing is about 0.567 mm.

### Protractor page-box semantics

W04 returns geometric body dimensions, not a false square box:

`PROTRACTOR_BODY_WIDTH_MM >= 70`
`PROTRACTOR_BODY_HEIGHT_MM = PROTRACTOR_BODY_WIDTH_MM/2`

W08 must add numeric reserves for labels, question number, answer line, row gap and margins to obtain `ITEM_MIN_HEIGHT_MM` and then prove page packing. A 2-column layout is preferred when it passes the numeric page proof; 2×5 is neither automatically valid nor automatically invalid.

If `ONE_PAGE_LOCK=OFF` and 2×5 fails the complete proof, paginate. Never reduce the 70 mm width below the verified print-spacing minimum merely to force one page.

### Full-circle 0–360°

Use only when explicitly requested/required.

Topology is `CYCLIC_FULL_CIRCLE`.

`interval_count=360/d`
`distinct_tick_position_count=360/d`

At 1° resolution: 360 equal intervals / 360 distinct positions.

The 0° and 360° directions are the same physical position; no duplicated 0°/360° physical mark is allowed.

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
`PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA`
`PROMPT_RULER_ZERO_START_ALIGNMENT_QA`
`PROMPT_RULER_NONZERO_START_RELATION_QA`
`PROMPT_SPEEDOMETER_TOPOLOGY_QA`
`PROMPT_SPEEDOMETER_INTERVAL_POSITION_COUNT_QA`
`PROMPT_SPEEDOMETER_TARGET_REPRESENTABILITY_QA`
`PROMPT_SPEEDOMETER_ANGLE_MAPPING_QA`
`PROMPT_SPEEDOMETER_NEEDLE_ALIGNMENT_QA`
`PROMPT_SPEEDOMETER_PIVOT_CENTER_QA`
`PROMPT_SPEEDOMETER_RADIAL_COLLINEARITY_QA`
`PROMPT_SPEEDOMETER_INACTIVE_GAP_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA`
`PROMPT_PROTRACTOR_BASELINE_QA`
`PROMPT_PROTRACTOR_DIRECTION_QA`
`PROMPT_PROTRACTOR_PRINT_SPACING_QA`
`PROMPT_PROTRACTOR_ACTIVE_SCALE_QA`
`PROMPT_PROTRACTOR_SINGLE_SCALE_QA`
`PROMPT_PROTRACTOR_COMMON_CENTER_QA`
`PROMPT_PROTRACTOR_RADIAL_TICK_QA`
`PROMPT_PROTRACTOR_SHAPE_INTEGRITY_QA`
`PROMPT_PROTRACTOR_RENDER_PATH_QA`
`PROMPT_PROTRACTOR_INTERMEDIATE_HIERARCHY_QA`
`PROMPT_ANGLE_TARGET_QA`
`PROMPT_PERIMETER_QA`
`PROMPT_AREA_FORMULA_QA`
`PROMPT_AREA_UNIT_CONVERSION_QA`
`PROMPT_PI_POLICY_QA` when circles are used
`PROMPT_CANONICAL_LABEL_PRESERVATION_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA` for learner-read W04 instruments

Wrong conversion/arithmetic, ruler subdivision, missing/misaligned endpoint projection guides, physical-edge substitution for zero, speedometer mapping/gap/pivot, route relation, protractor geometry/distortion/print spacing/active scale/render path, perimeter/area formula, squared-unit conversion, hidden-target leak, or missing review protocol blocks release.

### Protractor explicit tick/label manifest — mandatory

For learner-read 0–180° @1°, W04 MUST return the complete renderer-only manifests defined in `PROTRACTOR_181_TICK_MANIFEST_PROFILE.md`.

`PROTRACTOR_TICK_MANIFEST` contains exactly 181 degree-indexed records.
`PROTRACTOR_LABEL_MANIFEST` contains exactly 19 unique labels 0,10,...,180.

Required class counts:
`MAJOR_TICK_COUNT=19`
`INTERMEDIATE_TICK_COUNT=18`
`MINOR_TICK_COUNT=144`

Do not rely on prose such as "draw 1° ticks". The renderer must consume the manifest.

Additional QA:
`PROMPT_PROTRACTOR_181_POSITION_MANIFEST_QA`
`PROMPT_PROTRACTOR_TICK_CLASS_COUNT_QA`
`PROMPT_PROTRACTOR_LABEL_SET_QA`
`PROMPT_PROTRACTOR_LABEL_UNIQUENESS_QA`
