# All-Skills Runtime Invariant Profile

Version: 1.0.0
Status: Mandatory cross-skill SSOT
Compatible Gem baseline: 2.6.x
Release family: 2.6.3-LTS

## Purpose

Prevent a skill from being correct only in prose while losing truth during routing, layout, serialization or rendering.

Every active skill MUST follow:
`CANONICAL_STATE -> INDEPENDENT_VERIFY -> STUDENT_VIEW_DERIVATION -> LAYOUT -> RELEASE`

No downstream layer may invent or mutate academic truth.

## Universal runtime state

Every active skill serializes internally:
- `SKILL_ID`
- `CANONICAL_INPUT_STATE`
- `CANONICAL_TARGET_ORACLE`
- `DERIVED_VISIBLE_STATE`
- `INDEPENDENT_VERIFICATION`
- `ITEM_SPECIFIC_HARD_NEGATIVE` when a known failure mode exists
- `REPAIR_OWNER`
- `SKILL_PROMPT_SCORE`

Any learner-read visual additionally serializes exact geometry/data coordinates sufficient to reconstruct the visual deterministically.

## Universal invariants

1. Owner formulas/data are authoritative.
2. Visible content derives from canonical state, never the reverse.
3. Decoration cannot alter, cover, imitate or contradict academic data.
4. Layout may uniformly translate/scale locked academic geometry but may not independently distort components.
5. A repair starts from canonical state and reruns all dependent derivations.
6. Multi-skill worksheets require every active skill to pass independently.
7. A critical academic defect is non-compensatory.
8. Prompt QA never substitutes for Artifact QA.
9. Default page is A4 Portrait unless explicitly overridden.
10. If a canonical one-page profile has numeric feasibility PASS, pagination is not an arbitrary aesthetic option.

## Per-skill canonical state minimums

- ACADEMIC_ARITHMETIC_THAI: operands/operation/exact answer or canonical Thai target/category.
- TIME_CALCULATION: start/end/duration canonical minutes or seconds + crossing mode.
- ANALOG_CLOCK: semantic H:M + minute angle + hour displacement from minute angle + exact endpoints.
- WEIGHT_SCALE: range/resolution/tick indices/label map/target tick/pointer center.
- RULER_LENGTH: scale origin/resolution/start/end graduations/projection coordinates.
- DISTANCE: ordered segment list + units + route relation.
- SPEEDOMETER: canonical arc topology + target speed + target angle + common center.
- ANGLE_PROTRACTOR: range/resolution/common origin/baseline/direction/target ray.
- PERIMETER_AREA: shape type + canonical dimensions + unit-normalized formula state.
- TEMPERATURE: scale range/resolution/tick set + target index + liquid endpoint.
- CAPACITY: scale range/resolution/local-span grammar + target level/meniscus read point.
- VOLUME: solid decomposition + normalized dimensions + component volumes.
- MONEY: item-price mapping + paid/total/change in smallest active currency unit.
- CALENDAR: year/month/week-start + canonical Gregorian grid.
- DATA_READING: canonical dataset + exact visual mapping coordinates/key/axis state.

## High-risk learner-read chain

`OWNER -> W07 -> W10 -> W08 -> W09`

W07 audits visual topology/geometry.
W10 independently recomputes metrology/page evidence.
W08 owns layout without changing academic geometry.
W09 blocks release on any missing/FAIL/NOT_RUN critical evidence.

## Page precedence

Explicit valid user page requirement wins when safe.
Otherwise A4 Portrait is mandatory default.

For ordinary unlocked layouts:
`ONE_PAGE_PREFERRED=YES` means prove one page first, paginate if proof fails.

For a named canonical profile with complete numeric proof:
`FEASIBILITY_CONFIRMED_ONE_PAGE_LAYOUT_REQUIRED=YES`
means pagination is forbidden unless changed audited minima or an explicit override invalidates the proof.

## Artifact boundary

Before pixels are inspected:
`ARTIFACT_QA=NOT_YET_TESTED`

Any visible mismatch between canonical state and rendered educational data:
`CRITICAL_ACADEMIC_DEFECT=YES`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`
