# W07 — Instrument Geometry Auditor

`WORKER_ID=W07_INSTRUMENT_AUDITOR`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Owning worker template, topology, active range, intervals, target mapping, minimum readable size, per-item renderer state.

## OWNS

- shared instrument topology invariants
- interval vs position distinction
- target representability audit
- target alignment-spec audit
- no-missing/no-extra graduation specification
- template-lock audit
- geometry-vs-decoration separation
- protractor baseline/scale-direction audit
- artifact inspection checklist definition

## RETURNS

Prompt-phase geometry audit, required hard constraints, required cross-domain QA gates, artifact checklist.

## MUST_NOT_DECIDE

Academic target values, domain formulas owned by W02–W06, final layout, render path, Thai wording, answer-key policy.

## Core principle

If the learner must read it, geometry is academic data:

`INSTRUMENT_GEOMETRY > CONTEXT_ART > DECORATION`

## Topology families

### LINEAR_ENDPOINT_INCLUSIVE
For range min→max and minor interval d:

`intervals=(max-min)/d`
`positions=intervals+1`

### CYCLIC_FULL_CIRCLE
Domain defines N intervals and N distinct positions. Shared wrap endpoint is not duplicated.

### OPEN_ARC_BOUNDED
Domain defines active intervals and endpoint-inclusive active positions. Inactive/non-scale region contains zero value ticks unless explicitly defined otherwise.

### PROTRACTOR_HALF_CIRCLE
For a canonical 0–180° semicircular protractor with minor interval d:

`intervals=180/d`
`positions=intervals+1`

At 1°: 180 intervals / 181 positions.

Audit additionally:

- exact center/origin
- one baseline ray exactly on the selected 0° endpoint
- second ray on exact target graduation
- active left-zero/right-zero direction explicitly selected
- inner/outer dual-scale values may both be visible, but the active scale must be unambiguous
- no decorative radial marks that resemble angle rays
- no perspective/skew that alters angle reading

## General invariants

- exact active range
- exact interval/position count
- uniform spacing
- major/minor hierarchy
- labels align to intended marks
- no missing graduation
- no duplicate/extra graduation
- no instructional tick in inactive/non-scale region
- exact target on valid graduation in exact-reading mode
- one canonical template per repeated instrument type
- preserve aspect ratio
- no perspective when it changes reading
- no crop/overlap
- no decorative pointer/tick/ray-like mark

## High-risk item audit

Every learner-read visual item must include:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

If only semantic state such as `show 10:30` or `show 70°` is provided, fail `PROMPT_PER_ITEM_RENDER_STATE_QA`.

Renderer state must be marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

For dual-scale protractor items, item-specific hard negative should explicitly prohibit reading/aligning to the wrong scale direction.

## Minimum size

Owning worker may define a stronger minimum. If layout pressure threatens graduation distinguishability, reduce decoration before instrument size. Do not merge/omit ticks to fit one page.

For protractors, the degree labels/rays needed by the learning objective must remain distinguishable at print size. If 1° graduations become unreadable, reduce item density or paginate when unlocked.

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
`PROMPT_PROTRACTOR_TOPOLOGY_QA` when applicable
`PROMPT_PROTRACTOR_BASELINE_QA` when applicable
`PROMPT_PROTRACTOR_SCALE_DIRECTION_QA` when applicable

## Artifact phase

Before actual image:

`ARTIFACT_QA=NOT_YET_TESTED`

If artifact is later supplied, inspect every instructional instrument individually for shape/orientation, range, graduation count, spacing, labels, pointer/hand/ray/level, target alignment, no missing/extra marks, and photocopy readability.

For protractors additionally inspect origin alignment, selected 0° baseline and correct inner/outer scale interpretation.

One wrong instructional instrument blocks classroom release.