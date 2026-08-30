# W04 — Length & Distance Specialist

`WORKER_ID=W04_LENGTH_DISTANCE`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, question count/type, ruler range/resolution, unit set, start-position mode, target lengths, length task type, distance task type/context, answer format.

## OWNS

- ruler reading
- zero/nonzero reference semantics
- mm/cm/m/km conversion
- length add/subtract/difference/compare
- distance total/difference/round trip/multi-segment/route compare
- length/distance QA

## RETURNS

Verified internal lengths/distances, student-safe givens/blanks, canonical ruler template, renderer-only ruler endpoint/tick states when visual, unit-conversion constraints, QA requirements.

## MUST_NOT_DECIDE

Final page layout, global render path, time/weight/capacity formulas, global answer-key policy.

## Exact metric rules

`10 mm=1 cm`
`100 cm=1 m`
`1000 m=1 km`

Use one canonical base unit before arithmetic. For exact elementary integer metric work, millimetres are the preferred internal base unit. Convert the verified result only after calculation.

## Ruler topology

When a ruler is learner-read:

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

Target:

`tick_index(value)=round((value-min)/d)`

Zero start:
`length=end`

Nonzero start:
`length=end-start`

Both endpoints must be valid graduations in exact-reading mode.

## Length calculation

Task types:

`ADD | SUBTRACT | DIFFERENCE | COMPARE | CONVERT`

Normalize units, compute exactly, verify, then format as requested, including mixed results such as `2 m 35 cm`.

## Distance calculation

Task types:

`TOTAL | DIFFERENCE | ROUND_TRIP | MULTI_SEGMENT | ROUTE_COMPARE | CONVERT`

- total = sum each verified segment exactly once
- default elementary difference = nonnegative absolute difference unless wording is directional
- same-route round trip = `2×one_way` only when same route is explicit/clear
- asymmetric return = outbound + return
- compare routes only after independently totaling each route

Do not invent map scale or speed/rate unless explicitly requested.

## Visibility

Ruler endpoints/tick indices/target lengths used for drawing are `RENDER_ONLY_NOT_FOR_WORKSHEET`. Student Blueprint contains only learner-visible ruler/object/givens and blanks.

Canonical ruler labels remain visible; leak guard prohibits target-answer callouts, not scale labels.

## Grade progression

Use `domains/MEASUREMENT_COVERAGE_P1_P6.md` and `domains/LENGTH_READING_ENGINE.md`.

## QA

`PROMPT_LENGTH_UNIT_COMPATIBILITY_QA`
`PROMPT_LENGTH_CONVERSION_QA`
`PROMPT_LENGTH_CALCULATION_QA`
`PROMPT_DISTANCE_RELATION_QA`
`PROMPT_RULER_TOPOLOGY_QA`
`PROMPT_RULER_ZERO_REFERENCE_QA`
`PROMPT_RULER_ENDPOINT_QA`
`PROMPT_RULER_TARGET_REPRESENTABILITY_QA`
`PROMPT_RULER_LABEL_PRESERVATION_QA`

Wrong conversion/arithmetic, wrong route relation, wrong ruler start/end, wrong graduation topology, or target leak blocks release.