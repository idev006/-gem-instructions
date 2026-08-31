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

## RETURNS

One resolved render path, layout blueprint, minimum dimensions, safe-margin/page plan, theme/art rules, Thai/text constraints, scale-readability constraints, and layout/render QA requirements.

## MUST_NOT_DECIDE

Academic target values, arithmetic results, clock/dial/ruler/protractor/speedometer/area/volume formulas, domain maturity, prompt release approval.

## Render path

Resolve AUTO to exactly one:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

- Thai/text/table/numeric-heavy → DOCUMENT_FIRST
- exact academic geometry + theme art → HYBRID
- geometry-dominant/minimal art → DETERMINISTIC_VECTOR
- IMAGE_ONLY only when nondeterminism cannot threaten required academic/text fidelity or explicitly requested

Never emit unresolved alternatives.

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

If `ONE_PAGE_LOCK=ON` and unsafe, return FAIL. Do not silently shrink/crop/reduce count/merge graduations/paginate.

When `ONE_PAGE_LOCK=OFF`, preserve safe pagination wording; never compile a preference into a hard one-page mandate.

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

## Scale-line layout integrity

All learner-read scales inherit `SCALE_LINE_INTEGRITY_PROFILE.md`.

W08 must preserve:

- exact `SCALE_LINE_SPEC` fields from the owning worker/W07;
- authoritative baseline/ring/arc;
- exact interval/position count;
- minimum tick-center separation;
- major/minor hierarchy;
- label alignment/clearance;
- target alignment zone;
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

The protocol must require deterministic recount, alignment checks, repair/regenerate on mismatch, and a complete recheck after repair.

For ruler 1 cm @1 mm, explicitly require 10 intervals / 11 positions / 9 interior positions and prohibit counting the physical ruler edge as a graduation.

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
`PROMPT_ONE_PAGE_FEASIBILITY_QA`
`PROMPT_LAYOUT_QA`
`PROMPT_READABILITY_QA`
`PROMPT_ANSWER_SPACE_QA`
`PROMPT_SAFE_MARGIN_QA`
`PROMPT_THAI_TEXT_QA`
`PROMPT_TEXT_EXACTNESS_QA`
`PROMPT_PRINT_QA`
`PROMPT_THEME_INTERFERENCE_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA` when learner-read scales apply
`PROMPT_SCALE_LABEL_CLEARANCE_QA` when scale labels apply
`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA` when learner-read instruments apply
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA` when learner-read instruments apply
`PROMPT_PROTRACTOR_READABILITY_QA` when applicable
`PROMPT_DIMENSION_LABEL_CLEARANCE_QA` when geometry figures are used

Unresolved render path, unsafe page semantics, unreadable Thai, insufficient answer space, compromised scale geometry, missing review protocol, ambiguous labels or theme interference blocks release.
