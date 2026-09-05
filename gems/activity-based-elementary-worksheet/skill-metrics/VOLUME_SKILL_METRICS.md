# VOLUME Skill Metrics

SKILL_ID=VOLUME
OWNER=W05_TEMPERATURE_CAPACITY_VOLUME
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- rectangular prism V=l×w×h;
- composite solids decompose into non-overlapping prisms;
- cubic conversions use cubed linear factor;
- 1 cm³=1 mL and 1 dm³=1 L only when lesson includes relation.

## PROMPT_METRICS

- formula/decomposition 30%; unit normalization 25%; conversion 20%; grade/objective fit 10%; QA/repair 15%.

## ARTIFACT_METRICS

- dimensions unambiguously label intended edges/components;
- diagram does not hide overlap/decomposition assumptions.

## CRITICAL_DEFECTS

- wrong volume formula;
- double-counted overlap;
- linear rather than cubic conversion.

## REPAIR_PROTOCOL

Normalize dimensions, rebuild component model, recompute each component and total, regenerate diagram labels.

## REGRESSION_HOOKS

`full_skill_matrix_suite.py`; `semantic_oracle_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.
