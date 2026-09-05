# DISTANCE Skill Metrics

SKILL_ID=DISTANCE
OWNER=W04_LENGTH_DISTANCE
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- total=sum segments exactly once;
- round trip=2×one-way only when same route explicit;
- route comparison computes each route independently;
- exact m/km conversion.

## PROMPT_METRICS

- relation correctness 30%; unit normalization 20%; context fidelity 15%; grade appropriateness 15%; QA/repair 20%.

## ARTIFACT_METRICS

- route/table/diagram labels map unambiguously to distances;
- no decorative path implies extra segment;
- response unit clear.

## CRITICAL_DEFECTS

- invented segment/rate;
- double counting;
- wrong unit conversion;
- route-label ambiguity.

## REPAIR_PROTOCOL

Return to canonical segment list, normalize units, recompute each route, regenerate visible route state.

## REGRESSION_HOOKS

`full_skill_matrix_suite.py`; `semantic_oracle_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.
