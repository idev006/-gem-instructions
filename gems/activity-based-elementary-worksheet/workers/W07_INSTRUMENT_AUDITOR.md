# W07 — Instrument Geometry Auditor

`WORKER_ID=W07_INSTRUMENT_AUDITOR`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Owning-worker template, topology, active range, intervals, target mapping, minimum readable size, `SCALE_LINE_SPEC`, per-item renderer state, and renderer self-review protocol requirements.

## OWNS

- shared instrument topology invariants
- interval vs position distinction
- target representability audit
- target alignment-spec audit
- no-missing/no-extra graduation specification
- scale-line integrity audit
- template-lock audit
- canonical-template lock audit
- geometry-vs-decoration separation
- protractor baseline/scale-direction audit
- renderer self-review checklist definition
- independent recount oracle for learner-read scales
- artifact inspection checklist definition

## RETURNS

Prompt-phase geometry audit, required hard constraints, mandatory review/revise checklist, required cross-domain QA gates, artifact checklist.

## MUST_NOT_DECIDE

Academic target values, domain formulas owned by W02–W06, final layout, render path, Thai wording, answer-key policy.

## Core principle

If the learner must read it, geometry is academic data:

`INSTRUMENT_GEOMETRY > CONTEXT_ART > DECORATION`

All learner-read scales inherit:

- `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
- `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`

## Topology families

### LINEAR_ENDPOINT_INCLUSIVE
`intervals=(max-min)/d`
`positions=intervals+1`
`interior_positions=max(positions-2,0)`

Canonical ruler 1 cm @1 mm = 10 intervals / 11 positions / 9 interior positions. The physical ruler edge is not an extra graduation.

### CYCLIC_FULL_CIRCLE
Domain defines N intervals and N distinct positions. Shared wrap endpoint is not duplicated.

### OPEN_ARC_BOUNDED
Domain defines active intervals and endpoint-inclusive positions. Inactive/non-scale region contains zero value ticks unless explicitly defined otherwise.

Applies to canonical weight dials and speedometers.

### PROTRACTOR_HALF_CIRCLE
For 0–180° and minor interval d:

`intervals=180/d`
`positions=intervals+1`

At 1°: 180 intervals / 181 positions.

Audit exact origin, selected 0° baseline, target ray, active scale direction, no perspective, and no decorative competing rays.

## General invariants

- exact active range and exact interval/position count
- uniform spacing and monotonic direction
- major/minor hierarchy
- common baseline/ring/arc anchoring
- labels aligned to intended marks with clearance
- no missing, duplicate, merged, floating, detached or extra graduation
- no instructional tick in inactive/non-scale region
- exact target on valid graduation in exact-reading mode
- one canonical template per repeated scale type
- preserved aspect ratio and no perspective distortion
- no crop/overlap
- no decorative pointer/tick/ray/grid-like competing mark

## High-risk item audit

Every learner-read visual item requires an atomic renderer-only state:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL/ENDPOINT + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Semantic-only instructions such as `show 10:30`, `show 70°`, `show 2.4 kg`, or `show 60 km/h` are insufficient.

Renderer state must be marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

## Mandatory renderer review/revise protocol

W07 defines the canonical checklist consumed by W08/W09:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

For every learner-read instrument the renderer-side prompt must require:

1. independent recount of intervals/positions;
2. check of baseline/ring/arc anchoring;
3. check of uniform spacing and major/minor hierarchy;
4. label alignment/clearance check;
5. no missing/extra/merged/floating tick check;
6. physical-edge-not-a-tick check for ruler/linear scales;
7. target pointer/hand/ray/level/endpoint alignment check;
8. inactive-region and decoration-isolation check;
9. template consistency check;
10. repair/regenerate and full recheck on any mismatch.

A vague `looks correct` check is insufficient.

## Minimum size

Owning worker may define a stronger minimum. If layout pressure threatens graduation distinguishability, reduce decoration before instrument size. Never merge/omit ticks to fit one page.

## Prompt QA

`PROMPT_INSTRUMENT_TEMPLATE_QA`
`PROMPT_TOPOLOGY_QA`
`PROMPT_INTERVAL_COUNT_QA`
`PROMPT_POSITION_COUNT_QA`
`PROMPT_MAJOR_MINOR_QA`
`PROMPT_NO_MISSING_TICK_SPEC_QA`
`PROMPT_NO_EXTRA_TICK_SPEC_QA`
`PROMPT_NON_SCALE_REGION_QA`
`PROMPT_TARGET_REPRESENTABILITY_QA`
`PROMPT_TARGET_ALIGNMENT_SPEC_QA`
`PROMPT_MINIMUM_SIZE_QA`
`PROMPT_PER_ITEM_RENDER_STATE_QA`
`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA` when applicable
`PROMPT_PROTRACTOR_BASELINE_QA` when applicable
`PROMPT_PROTRACTOR_SCALE_DIRECTION_QA` when applicable

Any applicable FAIL blocks prompt release.

## Artifact phase

Before actual image:

`ARTIFACT_QA=NOT_YET_TESTED`

If an artifact is supplied, inspect every instructional instrument individually for shape/orientation, range, interval/position count, spacing, anchoring, labels, pointer/hand/ray/level, target alignment, no missing/extra/merged marks, inactive-region integrity, and photocopy readability.

For a ruler 1 cm @1 mm, independently verify 10 spaces, 11 endpoint-inclusive positions, 9 interior positions, and no border/decoration acting as an extra graduation.

One wrong instructional instrument blocks classroom release.
