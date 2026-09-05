# PERIMETER_AREA Skill Metrics

SKILL_ID=PERIMETER_AREA
OWNER=W04_LENGTH_DISTANCE
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- polygon perimeter sums each boundary side once;
- rectangle P=2(l+w), square P=4s;
- area formulas use correct shape and compatible units;
- squared-unit conversion squares linear factor.

## PROMPT_METRICS

- formula correctness 30%; unit handling 20%; diagram/given mapping 15%; grade/objective fit 15%; QA/repair 20%.

## ARTIFACT_METRICS

- side labels map to intended edges;
- height is visibly perpendicular where required;
- diagram does not imply false dimensions.

## CRITICAL_DEFECTS

- wrong formula;
- double-counted boundary;
- linear-factor area conversion;
- misleading dimension label.

## REPAIR_PROTOCOL

Return to canonical shape/givens, normalize units, recompute formula, regenerate labels/diagram.

## REGRESSION_HOOKS

`full_skill_matrix_suite.py`; `semantic_oracle_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.
