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
- numeric physical page packing proof before any one-page/grid approval
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

## Layout families

- numeric/text dense: deterministic table/grid
- ruler/clock/weight-dial/thermometer/capacity/speedometer: repeated card/grid with locked instrument zone
- protractor: larger geometry cards with enough diameter for required degree ticks, labels and rays
- perimeter/area: figure zone + dimension-label clearance + answer zone
- length/distance/time word problems: rows/tables preserving reading flow
- color-by-code: region/mosaic plan with readable expressions and separate legend
- graphs/tables: reserve exact data area before decoration
- volume: clear 3D diagram/dimension-label zone without decorative occlusion

Do not mechanically force 2×5 when the smallest graduation becomes ambiguous. Reduce decoration or paginate before shrinking scale geometry below minimums.

For 0–180° @1° protractors with `MIN_TICK_CENTER_SPACING_MM=0.60`, use the geometric oracle from the shared scale profile. `PRODUCTION_MIN_PROTRACTOR_WIDTH_MM=70`. A proposed 65 mm protractor is invalid because 1° tick spacing is approximately 0.567 mm. Five vertical rows of 70 mm instruments already require at least 350 mm before header, margins or answer zones, so an A4 portrait 2×5 plan cannot PASS; with `ONE_PAGE_LOCK=OFF`, paginate.

For a thermometer with a 60 mm vertical 0→50 scale, five rows consume at least 300 mm before header, margins or answer zones. A one-page five-row plan cannot PASS. If 60 mm is only a selected render size rather than a domain/metrology minimum, W08 may choose another size only if W10 confirms it remains at or above the true audited minimum; otherwise paginate.

For graduated-container cards, include the complete item-box height and answer zone. Five 50 mm item boxes consume 250 mm before row gaps/header/margins, so no PASS is allowed without explicit numeric proof.

For graph worksheets, axis height alone does not prove fit. Include graph title, axis/category labels, questions and answer lines in the physical content stack.

## Scale-line layout integrity

All learner-read scales inherit `SCALE_LINE_INTEGRITY_PROFILE.md`.

W08 must preserve:

- exact `SCALE_LINE_SPEC` fields from the owning worker/W07;
- authoritative baseline/ring/arc;
- exact interval/position count;
- minimum tick-center separation;
- computed `PRINT_SPACING_ORACLE` for dense scales;
- major/minor hierarchy;
- label alignment/clearance;
- target alignment zone;
- inactive-region integrity;
- canonical template consistency.

Theme, borders, card dividers, shadows, texture or illustration may not introduce repeated strokes that could be read as graduations.

For semicircular protractors, use one clearly active scale direction unless dual-scale interpretation is explicitly the lesson objective. A mirrored competing inner scale must not be introduced merely to imitate a commercial protractor. If per-item relations use 5° ticks, the canonical template must require 5° intermediate marks consistently.

## Mandatory renderer-side review/revise serialization

For any learner-read instrument, W08 must include a standalone final-prompt block named or semantically equivalent to:

`INSTRUMENT_REVIEW_REVISE_PROTOCOL`

It must instruct the downstream renderer:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

and include:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

The protocol must require deterministic recount, alignment checks, repair/regenerate on mismatch, and a complete recheck after repair.

For ruler 1 cm @1 mm, explicitly require 10 intervals / 11 positions / 9 interior positions and prohibit counting the physical ruler edge as a graduation.

For a 1° protractor, explicitly require 180 intervals / 181 positions, printed tick-spacing oracle ≥0.60 mm, width ≥70 mm under the default profile, one active reading direction, exact origin/baseline/ray alignment, and no unresolved AUTO render path.

For a 0–50°C thermometer whose scale is exactly 60 mm long, serialize spacing as exactly `1.20 mm`, therefore `>=1.20 mm` and `>0.60 mm`; never claim `>1.20 mm`.

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
`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA` when learner-read instruments apply
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA` when learner-read instruments apply
`PROMPT_PROTRACTOR_READABILITY_QA` when applicable
`PROMPT_PROTRACTOR_ACTIVE_SCALE_QA` when applicable
`PROMPT_PROTRACTOR_RENDER_PATH_QA` when applicable
`PROMPT_DIMENSION_LABEL_CLEARANCE_QA` when geometry figures are used

Unresolved render path, field-semantic mismatch, missing numeric page proof, unsafe page semantics, unreadable Thai, insufficient answer space, compromised scale geometry, missing review protocol, ambiguous labels or theme interference blocks release.
