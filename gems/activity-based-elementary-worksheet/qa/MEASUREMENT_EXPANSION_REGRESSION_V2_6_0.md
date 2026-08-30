# Measurement Expansion Regression — v2.6.0

Status: Critical prompt-generation regression
Applies to: `activity-based-elementary-worksheet` baseline 2.6.x

## M-01 — mm/cm relation
10 mm = 1 cm exactly.

## M-02 — cm/m relation
100 cm = 1 m exactly.

## M-03 — m/km relation
1000 m = 1 km exactly.

## M-04 — mixed length normalization
`2 m 35 cm + 80 cm` must normalize before arithmetic and verify to 315 cm / 3 m 15 cm according to requested format.

## M-05 — ruler zero reference
Beginner ruler starts at zero graduation, not physical edge.

## M-06 — ruler nonzero reference
Object from 2.3 cm to 7.8 cm has length 5.5 cm; final prompt must encode start/end geometry but not print hidden answer.

## M-07 — ruler topology
1 cm @1 mm = 10 intervals / 11 positions.

## M-08 — distance total
1.2 km + 800 m = 2.0 km after unit normalization.

## M-09 — round trip same route
1.5 km one way, explicitly same route → total 3.0 km.

## M-10 — asymmetric return
Outbound 1.5 km, return 1.8 km → total 3.3 km; must not use `2×1.5`.

## M-11 — route comparison
Route A and B totals are independently recomputed before difference.

## M-12 — no implicit speed
Distance-only prompt contains no speed/rate formula unless explicitly requested.

## M-13 — kg/g relation
1000 g = 1 kg exactly.

## M-14 — Thai tick relation
When kg+ขีด mode applies: 1 ขีด = 100 g = 0.1 kg.

## M-15 — weight mixed units
2 kg 300 g + 750 g = 3050 g = 3 kg 50 g according to requested format.

## M-16 — canonical dial topology
0–5 kg @0.1 kg = 300° active, 60° gap, 50 intervals/51 positions, no gap ticks.

## M-17 — canonical dial labels
0–5 remain visible; item-specific target value must not appear as added label.

## M-18 — capacity relation
1000 mL = 1 L exactly.

## M-19 — capacity mixed units
1 L 250 mL + 750 mL = 2000 mL = 2 L according to requested format.

## M-20 — discrete thermometer
20–120°F @2°F accepts only 20+2k targets unless interpolation is explicitly taught.

## M-21 — thermometer target alignment
Liquid endpoint specification coincides exactly with target graduation centerline.

## M-22 — bottom meniscus
Concave lowest point exactly at target graduation.

## M-23 — top meniscus
Appropriate curved highest designated point exactly at target graduation.

## M-24 — meniscus target leak
Renderer-only target number must not appear beside arrow/scale or in answer blank.

## M-25 — rectangular prism
2 cm × 3 cm × 4 cm = 24 cm³.

## M-26 — unit normalization before volume
2 m × 30 cm × 40 cm must convert to compatible units before multiplication; raw `2×30×40` with mixed units is invalid.

## M-27 — composite volume
Composite rectangular-prism decomposition uses non-overlapping components and counts each once.

## M-28 — capacity-volume relation
1 cm³ = 1 mL only when the learning objective explicitly includes that relation; do not inject into unrelated early-grade tasks.

## M-29 — clock half hour
10:30 = minute 180°, hour 315°, exact midpoint 10–11, never directly on 10.

## M-30 — elapsed time
08:15→09:45 = 90 minutes.

## M-31 — midnight guard
20:00→08:00 rejected when crossing disabled.

## M-32 — student blueprint isolation
Student Blueprint contains no renderer target values/angles/tick indices/levels.

## M-33 — teacher renderer metadata
Necessary geometry appears in final prompt marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

## M-34 — canonical-label preservation
Leak guard must preserve clock numerals, dial labels, ruler graduations and configured linear-scale labels.

## M-35 — single render path
Final prompt resolves exactly one render path.

## M-36 — grade appropriateness
AUTO uses conservative progression; e.g. P1 does not default to dense mm/nonzero-start/multi-step conversion.

## M-37 — one-page lock
Locked layout never drops required graduations or shrinks below minimum to force fit.

## M-38 — prompt/artifact phase
Before actual image: `ARTIFACT_QA=NOT_YET_TESTED`; no false visual PASS.

## Release rule

Any wrong unit relation, arithmetic, reference point, topology, route assumption, target alignment specification, grade progression, visibility scope, or phase claim blocks prompt release for the applicable measurement task.