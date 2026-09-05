# CAPACITY Skill Metrics

SKILL_ID=CAPACITY
OWNER=W05_TEMPERATURE_CAPACITY_VOLUME
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- canonical 0–1000 mL @50: 20 intervals/21 positions;
- each adjacent 100 mL span has exactly 2 intervals /3 positions /one +50 mL interior mark;
- explicit flat/meniscus read convention.

## PROMPT_METRICS

- global topology 20%; local-span recount 25%; level/meniscus alignment 20%; label hierarchy 10%; unit/calculation 10%; QA/pedagogy 15%.

## ARTIFACT_METRICS

- no extra local pseudo-ticks;
- read point exactly on target graduation;
- meniscus shape/read convention visually unambiguous.

## CRITICAL_DEFECTS

- extra/missing local graduation;
- wrong meniscus read point;
- liquid level not on canonical target.

## REPAIR_PROTOCOL

Rebuild global and every local span from canonical values; then redraw level/meniscus from target.

## REGRESSION_HOOKS

`measurement_reference_artifact_regression_suite.py`; `metrology_full_audit_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.


## RUNTIME_INVARIANT

`CANONICAL_STATE_REQUIRED=YES`
Canonical state = global range/resolution, every local 100 mL span, target level and meniscus convention. Local-span hierarchy is reconstructed from canonical positions; no decorative pseudo-ticks.
