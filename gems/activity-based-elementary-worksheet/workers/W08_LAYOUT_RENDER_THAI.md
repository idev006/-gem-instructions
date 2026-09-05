# W08 — Layout, Render & Thai Specialist

`WORKER_ID=W08_LAYOUT_RENDER_THAI`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Normalized spec, Student Blueprint, owning-worker minimum geometry sizes, `SCALE_LINE_SPEC`, instrument review checklist, question count, page constraints, theme/art style, color mode, header/instruction requirements.

## OWNS

- one-page feasibility planning
- page/grid/table/card structure
- answer-space sizing
- render-path resolution
- Thai/text exactness contract
- print-safe composition
- theme/decorative separation
- final worksheet visual hierarchy
- serialization of mandatory renderer-side instrument review/revise protocol
- serialization of verified local-span and reference/projection geometry
- numeric physical page packing proof before any one-page/grid approval
- shape-aware item bounding boxes
- pagination fallback when `ONE_PAGE_LOCK=OFF`
- strict separation of `OUTPUT_MODE` from `RENDER_PATH`

## RETURNS

One resolved render path, layout blueprint, minimum dimensions, safe-margin/page plan, theme/art rules, Thai/text constraints, scale-readability constraints, numeric `PHYSICAL_PAGE_STATE`, and layout/render QA requirements.

## MUST_NOT_DECIDE

Academic target values, arithmetic results, clock/dial/ruler/protractor/speedometer/area/volume formulas, domain maturity, prompt release approval.

W08 inherits mandatory `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`.

## Render path

Resolve AUTO to exactly one:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

- Thai/text/table/numeric-heavy → DOCUMENT_FIRST
- exact academic geometry + theme art → HYBRID
- geometry-dominant/minimal art → DETERMINISTIC_VECTOR
- IMAGE_ONLY only when nondeterminism cannot threaten required academic/text fidelity or explicitly requested

Never emit unresolved alternatives.

`OUTPUT_MODE` and `RENDER_PATH` are different fields. For the normal prompt-package workflow, preserve `OUTPUT_MODE=PROMPT_PACKAGE` while independently resolving `RENDER_PATH`. Never emit `OUTPUT_MODE=DETERMINISTIC_VECTOR`.

For a learner-read semicircular protractor at 1° resolution, the instrument geometry must be deterministic vector geometry. The final prompt must not contain unresolved `RENDER_PATH=AUTO`. If theme art is used, it remains a separate decorative layer and may not own the protractor ticks, labels, origin or rays.

## One-page feasibility

Attempt safe one-page A4 before page 2 unless user requests another policy.

Preserve, in order:

1. academic correctness and exact count;
2. canonical instrument topology and exact scale-line count;
3. domain minimum geometry size and tick separation;
4. Thai/numeral readability;
5. writable response space;
6. safe margins;
7. efficient valid layout;
8. reduced decoration;
9. shortened nonessential instruction/spacing;
10. pagination if unlocked.

No one-page/grid plan may PASS from verbal judgment such as `fits safely`. W08 must construct the numeric `PHYSICAL_PAGE_STATE` defined in `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md` and prove both width and height inequalities.

For A4 portrait use physical dimensions `210 mm × 297 mm`. Required grid height includes every item bounding box, row gap, header/title/directions reserve, margins and answer zone. Required grid width includes item widths, column gaps and margins.

If any required dimension is unknown, `PROMPT_PHYSICAL_PAGE_STATE_QA=NOT_RUN` and release cannot be approved.

If `ONE_PAGE_LOCK=ON` and unsafe, return FAIL. Do not silently shrink/crop/reduce count/merge graduations/paginate.

When `ONE_PAGE_LOCK=OFF`, preserve safe pagination wording; never compile a preference into a hard one-page mandate. If a candidate `2×5` plan fails numeric packing, paginate and recompute the new page plan.

A hard-coded layout such as `2 columns × 5 rows` is allowed in the final prompt only after numeric packing proof passes for that exact plan.

## Shape-aware layout families

- numeric/text dense: deterministic table/grid
- ruler/clock/weight-dial/thermometer/capacity/speedometer: repeated card/grid with locked instrument zone
- protractor: shape-aware semicircle card; body height is radius, not width
- perimeter/area: figure zone + dimension-label clearance + answer zone
- length/distance/time word problems: rows/tables preserving reading flow
- color-by-code: region/mosaic plan with readable expressions and separate legend
- graphs/tables: reserve exact data area before decoration
- volume: clear 3D diagram/dimension-label zone without decorative occlusion

Do not mechanically force or reject 2×5. Use numeric shape-aware proof.

### Semicircular protractor layout

For 0–180° @1°:

`PRODUCTION_MIN_PROTRACTOR_WIDTH_MM=70`

At width 70 mm:

`PROTRACTOR_RADIUS_MM=35`
`PROTRACTOR_BODY_HEIGHT_MM=35`

Do **not** use 70 mm as the vertical body height. Add separate numeric reserves for label/baseline clearance, question number, response zone and internal spacing to obtain the item height.

A 2-column layout is preferred because two 70 mm-wide protractors plus a reasonable column gap can fit within A4 portrait usable width when margins are budgeted. A `2×5` plan may PASS only if the complete vertical stack also passes numeric proof; if it fails and `ONE_PAGE_LOCK=OFF`, paginate.

For protractor geometry, W08 must preserve:

- perfect upper semicircle / no skew or non-uniform transform;
- one active numeric scale unless dual-scale reading is explicitly taught;
- exact common origin/baseline center/ray origin;
- exact 180/181 topology;
- 10° major / 5° intermediate / 1° minor hierarchy.

### Ruler object-measurement layout

For object-on-ruler tasks, reserve enough vertical space for the object, the ruler reading zone and two projection guides.

The final prompt must serialize:

`OBJECT_START_X == START_GRADUATION_X`
`OBJECT_END_X == END_GRADUATION_X`
`START_PROJECTION_GUIDE_X = OBJECT_START_X = START_GRADUATION_X`
`END_PROJECTION_GUIDE_X = OBJECT_END_X = END_GRADUATION_X`

Projection guides are thin dashed vertical helper lines, not ruler ticks. For `ZERO_START_MODE`, explicitly serialize `OBJECT_START_X == ZERO_GRADUATION_X` and a hard negative forbidding use of the physical ruler border as the origin when it differs from zero.

### Weight-dial hierarchy serialization

For canonical 0–5 kg @0.1 kg, preserve both global topology and every 1 kg local span:

`INTERVALS_PER_KG=10`
`INTERIOR_POSITIONS_PER_KG_SPAN=9`
`HALF_KG_INTERMEDIATE_OFFSET=0.5`

The +0.5 kg existing position is an intermediate tick, longer/more prominent than ordinary 0.1 kg ticks and shorter/weaker than whole-kilogram major ticks. Do not create an extra tick for hierarchy.

### Thermometer layout

For a 0–50°C @1°C thermometer, the spacing-derived scale-length minimum is 30 mm at a 0.60 mm floor. A selected 60 mm scale has exactly 1.20 mm spacing but five 60 mm vertical scales consume 300 mm before other content. W08 may select a smaller size only if it remains above all W10/metrology/readability minima; otherwise paginate.

### Graduated-container layout

Include the complete item-box height and answer zone. Five 50 mm item boxes consume 250 mm before row gaps/header/margins, so no PASS is allowed without explicit numeric proof.

For canonical 0–1000 mL @50 mL with 100 mL majors, the final prompt must serialize both global and local topology:

`EXPECTED_INTERVAL_COUNT=20`
`EXPECTED_POSITION_COUNT=21`
`INTERVALS_PER_100ML=2`
`INTERIOR_POSITIONS_PER_100ML_SPAN=1`
`LOCAL_SPAN_RECOUNT_REQUIRED=YES`

Every adjacent 100 mL major span must contain exactly one interior +50 mL tick. No extra pseudo-tick or decorative stroke may appear inside the span.

### Graph layout

Axis height alone does not prove fit. Include graph title, axis/category labels, questions and answer lines in the physical content stack.

## Scale-line layout integrity

All learner-read scales inherit `SCALE_LINE_INTEGRITY_PROFILE.md`.

W08 must preserve:

- exact `SCALE_LINE_SPEC` fields from owning worker/W07;
- authoritative baseline/ring/arc;
- exact interval/position count;
- local-span count/hierarchy when declared by the owner;
- minimum tick-center separation;
- computed `PRINT_SPACING_ORACLE` for dense scales;
- major/intermediate/minor hierarchy;
- label alignment/clearance/order;
- target alignment zone;
- common center/origin where radial/angular;
- reference/projection geometry where object endpoints map to a ruler;
- inactive-region integrity;
- canonical template consistency.

Theme, borders, card dividers, shadows, texture or illustration may not introduce repeated strokes that could be read as graduations.

## Mandatory renderer-side review/revise serialization

For any learner-read instrument, W08 must include a standalone final-prompt block named or semantically equivalent to:

`INSTRUMENT_REVIEW_REVISE_PROTOCOL`

It must instruct the downstream renderer:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

and include:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

The protocol must require deterministic recount, local-span recount where applicable, common-center/alignment/reference checks, repair/regenerate on mismatch, and a complete recheck after repair.

For ruler 1 cm @1 mm, explicitly require 10 intervals / 11 positions / 9 interior positions and prohibit counting the physical ruler edge as a graduation. For object-on-ruler tasks additionally require both dashed endpoint projection guides and exact start/end graduation alignment.

For a 1° protractor, explicitly require 180 intervals / 181 positions, printed tick-spacing oracle ≥0.60 mm, width ≥70 mm, one active scale direction, perfect semicircle, exact common origin/baseline/ray alignment, radial ticks and no unresolved AUTO render path.

For a 0–50°C thermometer, require 50/51 plus the exact 6-major/5-intermediate/40-minor hierarchy. If the selected scale is exactly 60 mm, serialize spacing as exactly `1.20 mm`, therefore `>=1.20 mm` and `>0.60 mm`; never claim `>1.20 mm`.

For canonical 0–5 kg @0.1 kg, explicitly require 10 intervals per kilogram and the existing +0.5 kg intermediate hierarchy tick.

For canonical 0–1000 mL @50 mL, explicitly require 20/21 globally and exactly 2 intervals /1 interior +50 mL tick in every 100 mL span.

For clocks, preserve exact numeric hand angles plus relational wording. For :45, explicitly verify the short hand is 75% of the way to the next hour and not pinned on the starting numeral.

For speedometers/weight dials, explicitly serialize that the pointer pivot equals the reading-ring center.

W08 must not claim that renderer self-review equals artifact QA.

## Thai text

Canonicalize before prompt compilation:

- correct spelling
- vowels/tone marks
- units
- Arabic numerals
- degree symbol and squared/cubic notation
- `km/h` / `กิโลเมตรต่อชั่วโมง` when speedometer reading is used
- punctuation
- response blanks
- header fields

Downstream prompt must preserve exact locked strings.

Default header:

`ชื่อ-นามสกุล ........................................ ชั้น ............ เลขที่ ............`

## Black-and-white print

Prefer clean black outlines, white fill, low ink use and photocopy-safe contrast. Required scale lines must not rely on gray-only strokes.

## Theme

Theme affects decorative context only. It must not alter academic values, topology, graph data, scale lines, dimension labels, angle rays, pointer/needle positions, liquid levels, answer mapping or question count.

No theme element may cover question text, answer area, learner-read instrument, graph axis or canonical scale labels.

## QA

`RENDER_PATH_RESOLVED_QA`
`PROMPT_OUTPUT_MODE_QA`
`PROMPT_FIELD_SEMANTICS_QA`
`PROMPT_ONE_PAGE_FEASIBILITY_QA`
`PROMPT_PHYSICAL_PAGE_STATE_QA`
`PROMPT_PHYSICAL_WIDTH_FEASIBILITY_QA`
`PROMPT_PHYSICAL_HEIGHT_FEASIBILITY_QA`
`PROMPT_ITEM_BOUNDING_BOX_QA`
`PROMPT_SHAPE_AWARE_BOUNDING_BOX_QA`
`PROMPT_ANSWER_ZONE_PRESERVATION_QA`
`PROMPT_PAGINATION_FALLBACK_QA`
`PROMPT_PAGE_POLICY_SERIALIZATION_QA`
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`
`PROMPT_LAYOUT_QA`
`PROMPT_READABILITY_QA`
`PROMPT_ANSWER_SPACE_QA`
`PROMPT_SAFE_MARGIN_QA`
`PROMPT_THAI_TEXT_QA`
`PROMPT_TEXT_EXACTNESS_QA`
`PROMPT_PRINT_QA`
`PROMPT_THEME_INTERFERENCE_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA` when learner-read scales apply
`PROMPT_SCALE_PRINT_SPACING_ORACLE_QA` when dense learner-read scales apply
`PROMPT_SCALE_LABEL_CLEARANCE_QA` when scale labels apply
`PROMPT_LOCAL_SPAN_RECOUNT_QA` when a local span grammar applies
`PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA` when object-on-ruler applies
`PROMPT_INSTRUMENT_COMMON_CENTER_QA` when radial/angular
`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA` when learner-read instruments apply
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA` when learner-read instruments apply
`PROMPT_PROTRACTOR_READABILITY_QA` when applicable
`PROMPT_PROTRACTOR_ACTIVE_SCALE_QA` when applicable
`PROMPT_PROTRACTOR_COMMON_CENTER_QA` when applicable
`PROMPT_PROTRACTOR_SHAPE_INTEGRITY_QA` when applicable
`PROMPT_PROTRACTOR_RENDER_PATH_QA` when applicable
`PROMPT_DIMENSION_LABEL_CLEARANCE_QA` when geometry figures are used

Unresolved render path, field-semantic mismatch, missing numeric page proof, unsafe page semantics, unreadable Thai, insufficient answer space, compromised global/local scale geometry, missing/misaligned reference projection, off-center origin, distorted protractor, missing review protocol, ambiguous labels or theme interference blocks release.

## Thai P3 strict-half-hour 10-item one-page layout

W08 inherits `policies/THAI_P3_CLOCK_HALF_HOUR_ONE_PAGE_PROFILE.md`.

When the request resolves to Thai P3 + ANALOG_CLOCK + DAY_NIGHT_PAIR + 10 items + strict `:30` and no explicit page/orientation/accessibility override, use the profile's numerically proved A4 portrait candidate:

`GRID_COLUMNS=2`
`GRID_ROWS=5`
`ITEM_MIN_WIDTH_MM=91`
`ITEM_MIN_HEIGHT_MM=43`
`COLUMN_GAP_MM=4`
`ROW_GAP_MM=4`
`REQUIRED_GRID_WIDTH_MM=186`
`REQUIRED_GRID_HEIGHT_MM=231`
`USABLE_WIDTH_MM=194`
`USABLE_HEIGHT_MM=243`

When these audited dimensions remain valid:
`FEASIBILITY_CONFIRMED_ONE_PAGE_LAYOUT_REQUIRED=YES`

Do not paginate to 5+5 merely for spaciousness after numeric proof passes. This does not change `ONE_PAGE_LOCK=OFF`; it is a derived decision from a passed physical feasibility proof.

Required:
`PROMPT_CLOCK_P3_HALF_HOUR_10_ITEM_ONE_PAGE_QA`
`PROMPT_CLOCK_P3_HALF_HOUR_2X5_QA`

Clock geometry remains immutable under layout. Uniform scale/translation of the whole clock is allowed; independent hand movement, snap, tick deletion or circle distortion is forbidden.
