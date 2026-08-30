# Measurement Expansion Regression — v2.6.0

Status: Critical prompt-generation regression
Applies to: `activity-based-elementary-worksheet` baseline 2.6.x

## Length / distance

### M-01 — mm/cm relation
10 mm = 1 cm exactly.

### M-02 — cm/m relation
100 cm = 1 m exactly.

### M-03 — m/km relation
1000 m = 1 km exactly.

### M-04 — mixed length normalization
`2 m 35 cm + 80 cm` → 315 cm / 3 m 15 cm according to requested format.

### M-05 — ruler zero reference
Beginner ruler starts at zero graduation, not physical edge.

### M-06 — ruler nonzero reference
Object from 2.3 cm to 7.8 cm has length 5.5 cm; renderer geometry may encode endpoints but Student Blueprint must not print the hidden answer.

### M-07 — ruler topology
1 cm @1 mm = 10 intervals / 11 positions.

### M-08 — distance total
1.2 km + 800 m = 2.0 km after unit normalization.

### M-09 — round trip same route
1.5 km one way, explicitly same route → 3.0 km.

### M-10 — asymmetric return
Outbound 1.5 km, return 1.8 km → 3.3 km; must not use `2×1.5`.

### M-11 — route comparison
Route A/B totals independently recomputed before difference.

### M-12 — no implicit speed
Distance-only prompt contains no speed/rate formula unless explicitly requested.

## Weight / dial

### M-13 — kg/g relation
1000 g = 1 kg exactly.

### M-14 — Thai tick relation
When kg+ขีด mode applies: 1 ขีด = 100 g = 0.1 kg.

### M-15 — weight mixed units
2 kg 300 g + 750 g = 3050 g = 3 kg 50 g according to requested format.

### M-16 — canonical dial topology
0–5 kg @0.1 kg = 300° active, 60° gap, 50 intervals/51 positions, no gap ticks.

### M-17 — canonical dial labels
0–5 remain visible; item target must not appear as added label.

## Capacity / temperature / volume

### M-18 — capacity relation
1000 mL = 1 L exactly.

### M-19 — capacity mixed units
1 L 250 mL + 750 mL = 2000 mL = 2 L.

### M-20 — discrete thermometer
20–120°F @2°F accepts only 20+2k targets unless interpolation explicitly taught.

### M-21 — thermometer alignment
Liquid endpoint specification exactly on target graduation centerline.

### M-22 — bottom meniscus
Concave lowest point exactly at target graduation.

### M-23 — top meniscus
Appropriate curved highest designated point exactly at target graduation.

### M-24 — meniscus target leak
Renderer-only target number absent from arrow/scale/answer blank.

### M-25 — rectangular prism
2 cm × 3 cm × 4 cm = 24 cm³.

### M-26 — unit normalization before volume
2 m × 30 cm × 40 cm must convert dimensions to compatible units before multiplication.

### M-27 — composite volume
Non-overlapping components; each counted once.

### M-28 — capacity-volume relation
1 cm³ = 1 mL only when explicitly part of the learning objective.

## Time / clock

### M-29 — clock half hour
10:30 = minute 180°, hour 315°, exact midpoint 10–11, never directly on 10.

### M-30 — elapsed time
08:15→09:45 = 90 minutes.

### M-31 — midnight guard
20:00→08:00 rejected when crossing disabled.

### M-32 — Student Blueprint isolation
No renderer target values/angles/tick indices/levels.

### M-33 — teacher renderer metadata
Necessary geometry appears in final prompt marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

### M-34 — canonical-label preservation
Leak guard preserves clock numerals, dial labels, ruler/protractor graduations and configured scale labels.

### M-35 — single render path
Final prompt resolves exactly one render path.

### M-36 — grade appropriateness
AUTO P1 does not default to dense mm/nonzero-start/multi-step conversion.

### M-37 — one-page lock
Locked layout never drops graduations or shrinks below minimum to force fit.

### M-38 — prompt/artifact phase
Before actual image: `ARTIFACT_QA=NOT_YET_TESTED`; no false visual PASS.

## New completeness regressions

### M-39 — time-unit conversion
`2 h 5 min 30 s` = 7530 s; conversion must use `60 s=1 min`, `60 min=1 h`.

### M-40 — seconds-hand guard
A worksheet converting minutes/seconds must not automatically add a seconds hand unless analog-second reading is explicitly part of the objective.

### M-41 — protractor topology
0–180° @1° = 180 intervals / 181 endpoint-inclusive positions.

### M-42 — protractor baseline
Vertex exactly at origin; one ray exactly on selected 0° baseline; target ray on exact target graduation; active inner/outer scale direction explicit.

### M-43 — protractor target leak
Target angle/tick/ray metadata may appear only as renderer metadata, not Student Blueprint answer text.

### M-44 — perimeter integrity
Rectangle 8 cm × 5 cm → perimeter 26 cm; count boundary only.

### M-45 — area formula
Triangle b=8 cm, perpendicular h=5 cm → 20 cm²; slanted side may not substitute for height.

### M-46 — squared-unit conversion
1 m² = 10,000 cm². A linear ×100 conversion is a critical failure.

### M-47 — PI policy
Circle worksheet uses exactly one declared π policy throughout; mixing 3.14 and 22/7 without explicit item-level policy is FAIL.

### M-48 — cubic relation
1000 cm³ = 1 dm³; 1000 dm³ = 1 m³; 1 m³ = 1,000,000 cm³.

### M-49 — cubed conversion factor
1 m³ → cm³ uses `100³`, not ×100.

### M-50 — dm³/L relation scope
1 dm³ = 1 L is introduced only when capacity-volume relation is explicitly taught/requested.

## Release rule

Any wrong unit relation, arithmetic/formula, reference point, topology, route assumption, scale direction, target alignment specification, squared/cubic conversion, grade progression, visibility scope, or phase claim blocks prompt release for the applicable measurement task.