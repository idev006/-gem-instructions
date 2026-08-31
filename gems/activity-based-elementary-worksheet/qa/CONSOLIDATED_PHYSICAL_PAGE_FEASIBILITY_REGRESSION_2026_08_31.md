# Consolidated Physical Page Feasibility Regression — 2026-08-31

Status: PERMANENT REGRESSION SOURCE
Severity: CRITICAL_INTEGRATION / EDUCATIONAL_RENDER_SAFETY
Source: User-supplied prompt-package UAT reports after 2.6.3-LTS 1107-case baseline

## Purpose

Several UAT outputs showed correct scale topology/metrology while incorrectly approving an impossible or unproved A4 page plan. The defect is systemic across the W10 → W08 → W09 handoff.

Root cause:

`SCALE_GEOMETRY_PASS was incorrectly treated as PAGE_PACKING_PASS`.

A print-spacing oracle proves local instrument readability only. It does not prove that N instruments, headers, directions, answer zones, margins and gaps fit on the requested page.

## Permanent invariant

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

`ONE_PAGE_PREFERRED != ONE_PAGE_LOCKED`

When `ONE_PAGE_LOCK=OFF`, an infeasible preferred one-page plan must paginate. It must not be hard-compiled into `1 PAGE` or `2×5`.

## UAT defect A — Weight dial 0–5 kg

Observed generated prompt state:
- claimed minimum dial diameter = 80 mm;
- planned 2 columns × 5 rows on A4 portrait;
- `PRINT_FEASIBILITY_CHECK=PASS`.

Independent lower bound:

`5 rows × 80 mm = 400 mm`

A4 portrait height is 297 mm before margins/header/answer zones.

Expected:
- candidate 2×5 plan = FAIL;
- if 80 mm is merely selected size, distinguish it from true metrology minimum;
- owning weight profile stronger practical minimum is 30 mm diameter;
- recompute a feasible selected size at or above the true minimum, or paginate;
- `ONE_PAGE_LOCK=OFF` means pagination is allowed.

Also observed in one prompt:
`OUTPUT_MODE=DETERMINISTIC_VECTOR`.

Expected semantic separation:
`OUTPUT_MODE=PROMPT_PACKAGE`
`RENDER_PATH=DETERMINISTIC_VECTOR`.

## UAT defect B — Protractor 0–180° @1°

Observed:
- true production minimum width = 70 mm;
- planned 2 columns × 5 rows A4 portrait;
- page feasibility declared PASS.

Independent lower bound:

`5 rows × 70 mm = 350 mm`

This exceeds 297 mm before header, answer zones or margins.

Expected:
- 2×5 candidate = FAIL;
- because `ONE_PAGE_LOCK=OFF`, paginate;
- never reduce the 70 mm protractor width to force one page.

## UAT defect C — Thermometer 0–50°C @1°C

Observed:
- 60 mm scale length;
- 2×5 plan;
- page release effectively approved;
- renderer checklist said spacing `>1.2 mm`.

Independent oracles:

`5 × 60 mm = 300 mm` before header/margins/answers → one-page five-row candidate impossible.

`60 mm / 50 intervals = 1.20 mm` exactly.

Expected wording:
- `spacing = 1.20 mm`, or
- `spacing >= 1.20 mm`, or
- `spacing > 0.60 mm`.

Forbidden for exact 60 mm geometry:
`spacing > 1.20 mm`.

## UAT defect D — Graduated container 0–1000 mL @50 mL

Observed:
- item bounding box minimum = 80 mm × 50 mm;
- 2×5 A4 portrait plan;
- no complete physical page proof.

Lower bound:

`5 × 50 mm = 250 mm`

This leaves only 47 mm of the full page height before margins, row gaps, header/title/directions and response zones.

Expected:
- no PASS from item height alone;
- calculate complete physical stack;
- if it fails, paginate because lock is OFF.

## UAT defect E — Bar graphs, two graphs + ten questions

Observed:
- graph axis minimum height 60 mm each;
- one-page preferred state compiled as `1 PAGE`;
- only axis spacing was used as metrology evidence.

Expected:
- graph-axis readability PASS is not page-fit proof;
- include graph titles, X labels, Y labels, two graph boxes, ten question lines and ten answer zones, header/directions and margins in physical page state;
- hard one-page wording forbidden unless complete numeric proof passes.

## Speedometer clarification — NOT A DEFECT

The speedometer report contained:
`60 km/h → exact_angle=360° (0°) → straight up`.

Under the canonical GEM angle convention for this dial family, 0° is top and clockwise is positive. Therefore `60 km/h → 0° → straight up` is internally correct.

Do NOT create a regression that rejects this relation.

Expanded angles such as `380° (20°)` are mathematically equivalent, but canonical serialization SHOULD prefer normalized `[0,360)` angles for machine stability while preserving equivalent relations.

## Required owning fixes

- `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`
- W10: distinguish minimum vs selected size; numeric page evidence required
- W08: numeric packing proof + unlocked pagination fallback
- W09/runtime release: do not approve contradictory or missing page evidence
- package: embed new profile in every worker bundle
- CI: permanent additive executable regression

## Required gates

`PROMPT_PHYSICAL_PAGE_STATE_QA`
`PROMPT_PHYSICAL_WIDTH_FEASIBILITY_QA`
`PROMPT_PHYSICAL_HEIGHT_FEASIBILITY_QA`
`PROMPT_ITEM_BOUNDING_BOX_QA`
`PROMPT_ANSWER_ZONE_PRESERVATION_QA`
`PROMPT_PAGINATION_FALLBACK_QA`
`PROMPT_PAGE_POLICY_SERIALIZATION_QA`
`PROMPT_METROLOGY_SIZE_ORACLE_QA`
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`
`PROMPT_OUTPUT_MODE_QA`
`PROMPT_FIELD_SEMANTICS_QA`
`PROMPT_QA_EVIDENCE_CONSISTENCY_QA`

Any applicable FAIL or NOT_RUN blocks approval of the current compiled prompt plan.
