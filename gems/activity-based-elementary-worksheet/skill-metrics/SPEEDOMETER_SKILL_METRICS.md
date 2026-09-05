# SPEEDOMETER Skill Metrics

SKILL_ID=SPEEDOMETER
OWNER=W04_LENGTH_DISTANCE
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- 0–120 km/h @10: OPEN_ARC_BOUNDED, 12 intervals/13 positions, 240° active +120° gap;
- target_angle=(240+2*target_kmh) mod 360;
- pivot=dial center=reading-ring center.

## PROMPT_METRICS

- topology 25%; angle mapping 20%; common center 20%; inactive gap 10%; label hierarchy 10%; QA/pedagogy 15%.

## ARTIFACT_METRICS

- all required ticks present;
- pointer radial and collinear from center to target tick;
- inactive gap clean;
- labels map exact major positions.

## CRITICAL_DEFECTS

- off-center pivot;
- wrong target angle;
- missing/extra ticks;
- pseudo-ticks in inactive gap.

## REPAIR_PROTOCOL

Regenerate scale from canonical open-arc positions and reconstruct pointer from common center.

## REGRESSION_HOOKS

`instrument_review_speedometer_regression_suite.py`; `instrument_geometry_artifact_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.


## RUNTIME_INVARIANT

`CANONICAL_STATE_REQUIRED=YES`
Canonical state = active arc start/sweep, 10 km/h positions, 20 km/h major hierarchy, labels, target speed/angle and common pivot. Major ticks must be visually stronger than minor 10 km/h ticks without adding positions.
