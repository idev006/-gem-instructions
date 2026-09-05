# Physical Page Feasibility Profile — Instrument & Graph Packing Safety

Version: 1.1.0
Status: Mandatory page-geometry safety contract
Compatible Gem baseline: 2.6.x
Primary owners: `W08_LAYOUT_RENDER_THAI` + independent feasibility evidence from `W10_METROLOGY_ENGINEER`
Release arbiter: `W09_QA_RELEASE`

## Mission

A correct instrument scale is still unusable if the compiled page plan cannot physically contain it at the claimed print size.

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

`ONE_PAGE_PREFERRED != ONE_PAGE_LOCKED`

For A4 portrait:
- physical page width = 210 mm
- physical page height = 297 mm

Margins, header, title, directions, question text, answer zones, graph titles, inter-item gaps and instrument bounding boxes all consume physical space. They may not be ignored when approving page feasibility.

## Required physical packing state

Before `PROMPT_ONE_PAGE_FEASIBILITY_QA` or `PROMPT_METROLOGY_PAGE_FEASIBILITY_QA` can PASS, W08/W10 must serialize numeric evidence containing at least:

`PAGE_WIDTH_MM`
`PAGE_HEIGHT_MM`
`MARGIN_LEFT_MM`
`MARGIN_RIGHT_MM`
`MARGIN_TOP_MM`
`MARGIN_BOTTOM_MM`
`HEADER_TITLE_DIRECTIONS_HEIGHT_MM`
`FOOTER_RESERVED_HEIGHT_MM` when applicable
`GRID_COLUMNS`
`GRID_ROWS`
`ITEM_MIN_WIDTH_MM`
`ITEM_MIN_HEIGHT_MM`
`COLUMN_GAP_MM`
`ROW_GAP_MM`
`ANSWER_ZONE_HEIGHT_MM`
`INTERNAL_VERTICAL_CLEARANCE_MM`
`USABLE_WIDTH_MM`
`USABLE_HEIGHT_MM`
`REQUIRED_GRID_WIDTH_MM`
`REQUIRED_GRID_HEIGHT_MM`
`WIDTH_FEASIBLE=YES|NO`
`HEIGHT_FEASIBLE=YES|NO`
`PAGE_FEASIBILITY_VERDICT=PASS|FAIL`

If any required physical dimension is unknown, the gate is `NOT_RUN`, never assumed PASS.

## Canonical equations

`USABLE_WIDTH_MM = PAGE_WIDTH_MM - MARGIN_LEFT_MM - MARGIN_RIGHT_MM`

`USABLE_HEIGHT_MM = PAGE_HEIGHT_MM - MARGIN_TOP_MM - MARGIN_BOTTOM_MM - HEADER_TITLE_DIRECTIONS_HEIGHT_MM - FOOTER_RESERVED_HEIGHT_MM`

`REQUIRED_GRID_WIDTH_MM = GRID_COLUMNS * ITEM_MIN_WIDTH_MM + (GRID_COLUMNS - 1) * COLUMN_GAP_MM`

`REQUIRED_GRID_HEIGHT_MM = GRID_ROWS * ITEM_MIN_HEIGHT_MM + (GRID_ROWS - 1) * ROW_GAP_MM`

PASS requires both:

`REQUIRED_GRID_WIDTH_MM <= USABLE_WIDTH_MM`

and

`REQUIRED_GRID_HEIGHT_MM <= USABLE_HEIGHT_MM`

For an item containing a learner-read instrument plus response area:

`ITEM_MIN_HEIGHT_MM >= INSTRUMENT_BODY_HEIGHT_MM + ANSWER_ZONE_HEIGHT_MM + INTERNAL_VERTICAL_CLEARANCE_MM`

## Shape-aware bounding boxes — mandatory

Page feasibility must use the **actual shape footprint**, not a generic square assumption.

### Full circular dial / clock / speedometer

If diameter is `D`:

`INSTRUMENT_BODY_WIDTH_MM = D`
`INSTRUMENT_BODY_HEIGHT_MM = D`

### Semicircular protractor

If production width is `W=2R`:

`INSTRUMENT_BODY_WIDTH_MM = W`
`INSTRUMENT_BODY_HEIGHT_MM = R = W/2`

Therefore a 70 mm-wide protractor has a 35 mm semicircle body height before numeric labels, baseline clearance, question number, answer zone and row spacing.

**Forbidden inference:** `five rows × 70 mm protractor width = 350 mm required height`.

That mixes horizontal width with vertical height and is a false feasibility oracle.

The correct protractor item height is:

`ITEM_MIN_HEIGHT_MM >= W/2 + PROTRACTOR_LABEL_BASELINE_CLEARANCE_MM + ANSWER_ZONE_HEIGHT_MM + INTERNAL_VERTICAL_CLEARANCE_MM`

### Vertical linear instrument

For thermometer/container scale body height `H`, use the actual selected body height plus answer/label reserves.

## Page-policy semantics

Default:

`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

When `ONE_PAGE_LOCK=OFF`:
- one page is attempted only if numeric packing proof passes;
- if it does not fit, paginate;
- do not shrink below audited instrument minimum;
- do not remove answer space;
- do not merge/delete ticks;
- do not crop labels;
- do not rewrite the final prompt as `1 PAGE` or hard-code `2×5` if the proof fails.

When `ONE_PAGE_LOCK=ON` and numeric proof fails:

`PROMPT_ONE_PAGE_FEASIBILITY_QA=FAIL`
`PROMPT_METROLOGY_PAGE_FEASIBILITY_QA=FAIL`
`PROMPT_RELEASE=BLOCKED`

## Minimum size vs selected size

W10 must distinguish:

`METROLOGY_MINIMUM_SIZE_MM` = smallest physical size justified by the relevant spacing/readability oracle or stronger domain minimum.

`SELECTED_RENDER_SIZE_MM` = actual size chosen by W08 for the page plan.

A larger selected size must not be mislabeled as a metrology minimum. An arbitrary oversized minimum that creates a false page contradiction is invalid evidence.

Required field:
`SIZE_ORACLE_SOURCE = SPACING_ORACLE | DOMAIN_MINIMUM | USER_EXPLICIT | OTHER_JUSTIFIED`

## Linear-scale inequality semantics

If scale length `L` is divided into `N` equal intervals:

`tick_center_spacing_mm = L / N`

If `L=60 mm` and `N=50`, spacing is exactly `1.20 mm`.

Therefore a prompt may state `>= 1.20 mm` or `> 0.60 mm`, but must not state `> 1.20 mm` for that exact geometry.

Gate:
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`.

## Output-mode / render-path separation

These fields are semantically distinct:

`OUTPUT_MODE=PROMPT_PACKAGE`

`RENDER_PATH=DETERMINISTIC_VECTOR|HYBRID|DOCUMENT_FIRST|IMAGE_ONLY`

A render path value in `OUTPUT_MODE` or an output-mode value in `RENDER_PATH` is a contract failure.

Gates:
`PROMPT_OUTPUT_MODE_QA`
`RENDER_PATH_RESOLVED_QA`
`PROMPT_FIELD_SEMANTICS_QA`

## Instrument-family implications

### Weight dial
A claimed 80 mm circular dial used in five vertical rows cannot be declared one-page-feasible merely because tick spacing passes: the circular body alone requires 400 mm of height.

### Protractor
For 0–180° @1°, production width >=70 mm is a genuine metrology minimum. Its semicircle body height at exactly 70 mm width is 35 mm, not 70 mm. A two-column layout is preferred when the complete numeric packing state passes. `2×5` must be **proved**, not automatically rejected or automatically accepted.

### Thermometer
A selected 60 mm 0–50°C scale has 1.20 mm interval spacing. Five such vertical scale bodies consume 300 mm before header, margins or answer zones; that selected 60 mm five-row plan cannot PASS. If 60 mm is not a true minimum, W08 may select a smaller size only after W10 verifies it remains above the metrology/readability minimum.

### Graduated container
Container item-box height, scale height and answer zone must all be included. A 50 mm item box × five rows consumes 250 mm before row gaps and page header; feasibility must be numerically proved rather than assumed.

### Graphs
Two graph axes of 60 mm height may fit vertically in isolation, but graph titles, category labels and ten question/answer lines also consume height. Graph worksheet feasibility requires the complete content stack, not only axis height.

## Final-prompt serialization rule

The final prompt must preserve page-policy semantics. If pagination is unlocked, use wording equivalent to:

`Prefer one page only if the audited physical packing state passes. Otherwise paginate while preserving instrument/graph geometry, labels, answer space and margins.`

A hard-coded grid is allowed only after the corresponding numeric packing proof passes.

## Mandatory QA gates

`PROMPT_PHYSICAL_PAGE_STATE_QA`
`PROMPT_PHYSICAL_WIDTH_FEASIBILITY_QA`
`PROMPT_PHYSICAL_HEIGHT_FEASIBILITY_QA`
`PROMPT_ITEM_BOUNDING_BOX_QA`
`PROMPT_SHAPE_AWARE_BOUNDING_BOX_QA`
`PROMPT_ANSWER_ZONE_PRESERVATION_QA`
`PROMPT_PAGINATION_FALLBACK_QA`
`PROMPT_PAGE_POLICY_SERIALIZATION_QA`
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`
`PROMPT_OUTPUT_MODE_QA`
`PROMPT_FIELD_SEMANTICS_QA`
`PROMPT_QA_EVIDENCE_CONSISTENCY_QA`

Any applicable FAIL or NOT_RUN blocks `PROMPT_RELEASE=APPROVED`.

## Artifact boundary

This profile proves only that the page plan is physically coherent. It does not prove downstream pixels.

Before rendered inspection:
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`


## Derived mandatory one-page decision after proof

`ONE_PAGE_PREFERRED=YES` means one page is evaluated first. When a specific canonical profile has complete numeric evidence and both inequalities PASS, W08/W09 may set:

`FEASIBILITY_CONFIRMED_ONE_PAGE_LAYOUT_REQUIRED=YES`

This is not equivalent to user-provenance `ONE_PAGE_LOCK=ON`. It means that, for the unchanged audited content/minima, pagination is no longer a valid arbitrary aesthetic choice.

Canonical example:
`THAI_P3_CLOCK_HALF_HOUR_ONE_PAGE_PROFILE.md` proves a 10-item DAY_NIGHT_PAIR strict-half-hour worksheet in A4 portrait using 2×5, required 186×231 mm inside usable 194×243 mm.

If a downstream system wants to paginate that profile, it must show changed audited dimensions or an explicit user/accessibility override that invalidates the prior proof.
