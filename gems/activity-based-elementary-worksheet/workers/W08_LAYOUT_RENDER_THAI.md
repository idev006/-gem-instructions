# W08 — Layout, Render & Thai Specialist

`WORKER_ID=W08_LAYOUT_RENDER_THAI`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Normalized spec, Student Blueprint, owning-worker minimum geometry sizes, question count, page constraints, theme/art style, color mode, header/instruction requirements.

## OWNS

- one-page feasibility planning
- page/grid/table/card structure
- answer-space sizing
- render-path resolution
- Thai/text exactness contract
- print-safe composition
- theme/decorative separation
- final worksheet visual hierarchy

## RETURNS

One resolved render path, layout blueprint, minimum dimensions, safe-margin/page plan, theme/art rules, Thai/text constraints, layout/render QA requirements.

## MUST_NOT_DECIDE

Academic target values, arithmetic results, clock/dial/ruler/protractor/area/volume formulas, domain maturity, prompt release approval.

## Render path

Resolve AUTO to exactly one:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

Guidance:

- Thai/text/table/numeric-heavy → DOCUMENT_FIRST
- exact academic geometry + theme art → HYBRID
- geometry-dominant/minimal art → DETERMINISTIC_VECTOR
- IMAGE_ONLY only when nondeterminism cannot threaten required academic/text fidelity or explicitly requested

Never emit unresolved `A or B` alternatives.

## One-page feasibility

Attempt safe one-page A4 before page 2 unless user requests another policy.

Preserve:

1. academic correctness and exact count
2. domain minimum geometry size
3. Thai/numeral readability
4. writable response space
5. safe margins
6. efficient valid layout
7. reduced decoration
8. shortened nonessential instruction
9. reduced nonessential spacing
10. pagination only if unlocked

If `ONE_PAGE_LOCK=ON` and unsafe, return FAIL; do not silently shrink/crop/reduce count/merge graduations/paginate.

## Layout families

- numeric/text dense: deterministic table/grid
- ruler/clock/scale/thermometer/capacity: repeated card/grid with locked instrument zone
- protractor: larger geometry cards with enough diameter for required degree ticks, labels and rays
- perimeter/area: figure zone + dimension-label clearance + answer zone; never place theme art on a side length, height, radius or diameter marker
- length/distance/time word problems: rows/tables preserving reading flow
- color-by-code: region/mosaic plan with readable expressions and separate legend
- graphs/tables: reserve exact data area before decoration
- volume: clear 3D diagram/dimension-label zone without decorative occlusion

Do not mechanically force 2×5 when domain minimum sizes do not fit.

For 1° protractor reading, reduce item density or paginate before making degree graduations/labels ambiguous.

For area/perimeter figures, maintain enough separation that dimension labels cannot be mistaken for one another and perpendicular-height markers remain clear.

## Thai text

Canonicalize before prompt compilation:

- correct spelling
- vowels/tone marks
- units
- Arabic numerals
- degree symbol and squared/cubic unit notation when used
- punctuation
- response blanks
- header fields

Downstream prompt must preserve exact Thai strings and prohibit paraphrasing/invented labels when wording is locked.

Default header:

`ชื่อ-นามสกุล ........................................ ชั้น ............ เลขที่ ............`

Use explicit user wording when provided.

## Black-and-white print

Prefer clean black outlines, white fill, low ink usage and photocopy-safe contrast. Avoid gray wash unless requested.

Color-by-code exception: student regions may remain unfilled while legend swatches use color as specified.

## Theme

Theme art may affect decorative context, border motifs and visual tone only. It must not alter academic values, instrument topology, graph data, dimension labels, angle rays, perpendicular-height markers, radius/diameter markers, answer mapping or question count.

No theme element may cover question text, answer area, ruler/clock/scale/protractor, graph axes, figure dimensions, or canonical scale labels.

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
`PROMPT_PROTRACTOR_READABILITY_QA` when applicable
`PROMPT_DIMENSION_LABEL_CLEARANCE_QA` when geometry figures are used

Unresolved render path, unsafe page lock, unreadable Thai, insufficient answer space, layout that compromises academic geometry, ambiguous dimension labels or theme interference blocks release.