# TIME_CALCULATION Skill Metrics

SKILL_ID=TIME_CALCULATION
OWNER=W02_TIME_CLOCK
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- canonical minutes-from-day-start;
- forward/reverse/duration relations;
- explicit midnight-crossing mode;
- granularity constraints.

## PROMPT_METRICS

- parse/bounds 15%; formula relation 25%; granularity 15%; crossing policy 10%; answer formatting 10%; pedagogy 15%; repair/verification 10%.

## ARTIFACT_METRICS

- all visible times match canonical state;
- tables preserve chronology;
- decoration does not imply an extra time;
- response space clear.

## CRITICAL_DEFECTS

- invalid time;
- wrong duration/start/end;
- forbidden crossing;
- inconsistent schedule.

## REPAIR_PROTOCOL

Rebuild TIME_ITEM_STATE from canonical minutes and rerun complete relation check.

## REGRESSION_HOOKS

`full_skill_matrix_suite.py`; `semantic_oracle_regression_suite.py`; capability scorecard.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.
