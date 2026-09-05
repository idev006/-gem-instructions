# MONEY Skill Metrics

SKILL_ID=MONEY
OWNER=W06_MONEY_CALENDAR_DATA
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- exact smallest currency unit when decimals active;
- total=sum prices;
- change=paid-total with paid>=total unless explicitly taught otherwise;
- price association unambiguous.

## PROMPT_METRICS

- arithmetic 30%; association 20%; currency/denomination validity 15%; grade/context 15%; QA/repair 20%.

## ARTIFACT_METRICS

- every price belongs to one item;
- coin/note art is academic only when recognition is taught;
- no conflicting price labels.

## CRITICAL_DEFECTS

- wrong total/change;
- ambiguous item-price association;
- false denomination when denomination recognition is the objective.

## REPAIR_PROTOCOL

Repair canonical monetary data, recompute totals/change, regenerate labels and questions.

## REGRESSION_HOOKS

`full_skill_matrix_suite.py`; capability scorecard.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.
