# ANALOG_CLOCK Skill Metrics

SKILL_ID=ANALOG_CLOCK
OWNER=W02_TIME_CLOCK
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- 60 minute positions, 12 hour positions, common center;
- minute_angle=6*m;
- hour_angle=30*(h mod 12)+0.5*m;
- deterministic vector endpoints;
- :15=25%, :30=50%, :45=75% hour displacement.

## PROMPT_METRICS

- topology 20%; target-angle math 20%; endpoint serialization 20%; anti-snap rules 15%; grade/pedagogy 10%; QA/repair 15%.

## ARTIFACT_METRICS

- 60 positions visible and evenly distributed;
- both hands share exact pivot;
- minute hand reaches correct minute position;
- hour hand continuously displaced;
- hand hierarchy/readability clear.

## CRITICAL_DEFECTS

- any nonzero-minute hour hand snapped to whole-hour numeral;
- wrong minute hand;
- off-center pivot;
- missing/extra minute positions.

## REPAIR_PROTOCOL

Return to semantic time, recompute angles/endpoints, rebuild both hands from common center, re-audit.

## REGRESSION_HOOKS

`clock_hand_endpoint_regression_suite.py`; `runtime_uat_regression_suite.py`; `measurement_reference_artifact_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.
