# CALENDAR Skill Metrics

SKILL_ID=CALENDAR
OWNER=W06_MONEY_CALENDAR_DATA
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- real Gregorian calendar unless fictional practice explicitly requested;
- valid days/month/leap year/weekday mapping;
- exactly 7 weekday columns; explicit week-start.

## PROMPT_METRICS

- date validity 25%; weekday/grid mapping 25%; sequence/leap year 20%; learner clarity 10%; QA/repair 20%.

## ARTIFACT_METRICS

- no duplicate/missing active-month date;
- dates appear under correct weekday;
- marker does not obscure date.

## CRITICAL_DEFECTS

- impossible date;
- wrong weekday;
- duplicate/missing active date;
- inconsistent week-start.

## REPAIR_PROTOCOL

Recompute Gregorian month structure from YEAR/MONTH/WEEK_START and rebuild complete grid.

## REGRESSION_HOOKS

`full_skill_matrix_suite.py`; capability scorecard.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.
