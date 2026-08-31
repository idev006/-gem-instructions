# Consolidated Physical Page Feasibility Regression — 2026-08-31

Status: PERMANENT REGRESSION SOURCE
Severity: CRITICAL_INTEGRATION / EDUCATIONAL_RENDER_SAFETY
Source: user-supplied prompt-package UAT reports after 2.6.3-LTS

## Purpose

Several UAT outputs showed correct local scale arithmetic while incorrectly approving or rejecting full A4 page plans. The systemic defect is the W10→W08→W09 handoff.

Root cause:

`SCALE_GEOMETRY_PASS != PAGE_PACKING_PASS`

A spacing oracle proves local readability only. It does not prove complete page fit. A later full-SSOT audit also found a false page oracle for semicircular protractors: horizontal width had been incorrectly reused as vertical body height.

## Permanent invariants

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

`ONE_PAGE_PREFERRED != ONE_PAGE_LOCKED`

`PAGE_PACKING_MUST_USE_SHAPE_AWARE_BOUNDING_BOXES`

When `ONE_PAGE_LOCK=OFF`, an infeasible preferred plan must be recomputed or paginated. It must not be hard-compiled into one page.

## UAT A — Weight dial 0–5 kg

Observed selected dial diameter=80mm with planned 2×5 A4 portrait and feasibility PASS.

Circular body lower bound:

`5 rows × 80mm = 400mm`

A4 portrait height=297mm before other content. Candidate fails. If80mm is selected rather than true minimum, distinguish `SELECTED_RENDER_SIZE_MM` from `METROLOGY_MINIMUM_SIZE_MM`, choose a safe smaller selected size at/above true minimum, or paginate.

Also observed field error:
`OUTPUT_MODE=DETERMINISTIC_VECTOR`.

Correct:
`OUTPUT_MODE=PROMPT_PACKAGE`
`RENDER_PATH=DETERMINISTIC_VECTOR`.

## UAT B — Protractor 0–180° @1° — audit correction

Observed true production minimum **width**=70mm and a 2-column candidate layout.

An earlier audit incorrectly concluded:

`5 rows × 70mm = 350mm vertical body height`

That inference is **wrong** because a semicircular protractor width is `W=2R` while geometric body height is `R=W/2`.

Correct shape oracle at W=70mm:

`PROTRACTOR_BODY_WIDTH=70mm`
`PROTRACTOR_BODY_HEIGHT=35mm`

Five geometric bodies consume 175mm, but that alone still does not prove full page fit. Complete item height must add label/baseline clearance, question number, answer zone and internal spacing; page stack adds row gaps, header/title/directions and margins.

Permanent expected behavior:

- prefer two columns when horizontal proof passes;
- do not automatically reject 2×5 from width-as-height confusion;
- do not automatically approve 2×5 from body height alone;
- calculate complete shape-aware `PHYSICAL_PAGE_STATE`;
- if candidate fails and lock=OFF, paginate;
- never reduce verified 70mm width below the print-spacing minimum merely to force a page.

## UAT C — Thermometer 0–50°C @1°C

Observed selected scale length=60mm, 2×5 candidate, and renderer checklist claimed spacing `>1.2mm`.

Independent oracles:

`5×60mm=300mm` scale-body height before header/margins/answers → this selected five-row plan cannot fit A4 portrait.

`60mm/50 intervals=1.20mm` exactly.

Valid wording:
- `spacing=1.20mm`, or
- `spacing>=1.20mm`, or
- `spacing>0.60mm`.

Forbidden for exact60mm geometry:
`spacing>1.20mm`.

Also: 60mm is a selected size, not the spacing-derived minimum. At0.60mm floor, minimum scale length is30mm unless stronger readability rule applies.

## UAT D — Graduated container 0–1000mL @50mL

Observed item bounding box minimum=80×50mm, 2×5 plan, no complete page proof.

Five 50mm boxes consume250mm before row gaps/header/margins. Expected: calculate complete stack; no assumed PASS; paginate if needed.

## UAT E — Bar graphs, two graphs + ten questions

Observed graph axis minimum height60mm each and one-page wording compiled from axis spacing alone.

Expected: graph-axis readability is not page-fit proof. Include graph titles, X/Y labels, graph boxes, ten question lines, ten answer zones, header/directions and margins in physical page state.

## Speedometer clarification — NOT A DEFECT

`60 km/h → exact_angle=360° (0°) → straight up` is correct under the canonical speedometer convention where0° is top and clockwise is positive.

Do not create a regression rejecting this relation. Canonical machine state SHOULD normalize angle to `[0,360)`.

## Required owning fixes

- `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`
- W10: minimum vs selected size + shape-aware numeric page evidence
- W08: complete packing proof + pagination fallback
- W09: no contradictory/missing page evidence approval
- package embeds page profile
- CI keeps permanent additive executable regression.

## Required gates

`PROMPT_PHYSICAL_PAGE_STATE_QA`
`PROMPT_PHYSICAL_WIDTH_FEASIBILITY_QA`
`PROMPT_PHYSICAL_HEIGHT_FEASIBILITY_QA`
`PROMPT_ITEM_BOUNDING_BOX_QA`
`PROMPT_SHAPE_AWARE_BOUNDING_BOX_QA`
`PROMPT_ANSWER_ZONE_PRESERVATION_QA`
`PROMPT_PAGINATION_FALLBACK_QA`
`PROMPT_PAGE_POLICY_SERIALIZATION_QA`
`PROMPT_METROLOGY_SIZE_ORACLE_QA`
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`
`PROMPT_OUTPUT_MODE_QA`
`PROMPT_FIELD_SEMANTICS_QA`
`PROMPT_QA_EVIDENCE_CONSISTENCY_QA`

Any applicable FAIL or NOT_RUN blocks approval of the current compiled plan.
