# ANGLE_PROTRACTOR Skill Metrics

SKILL_ID=ANGLE_PROTRACTOR
OWNER=W04_LENGTH_DISTANCE
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- 0–180° @1°: 180 intervals/181 positions;
- perfect upper semicircle;
- center=baseline midpoint=ray origin;
- 10° major, 5° intermediate, 1° minor; one active numeric scale by default.

## PROMPT_METRICS

- topology 20%; shape/common-center 25%; ray target 20%; scale direction/labels 15%; print spacing 10%; QA/pedagogy 10%.

## ARTIFACT_METRICS

- no ellipse/shear/perspective;
- every tick radial from common center;
- target ray intersects exact graduation;
- scale readable at production size.

## CRITICAL_DEFECTS

- distorted semicircle;
- wrong center/baseline;
- wrong ray target;
- ambiguous dual-scale when not taught.

## REPAIR_PROTOCOL

Reconstruct canonical semicircle and radial tick coordinates; then regenerate target ray and layout with uniform scale only.

## REGRESSION_HOOKS

`protractor_scale_safety_regression_suite.py`; `metrology_full_audit_regression_suite.py`; `instrument_geometry_artifact_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.


## RUNTIME_INVARIANT

`CANONICAL_STATE_REQUIRED=YES`
Canonical state = semicircle center/baseline, 181 exact positions, active scale direction and target ray. Tick hierarchy 10° major > 5° intermediate > 1° minor must reuse canonical positions.


## Explicit 181-position manifest contract

This skill inherits `policies/PROTRACTOR_181_TICK_MANIFEST_PROFILE.md`.

For 0–180° @1°:
- exactly 181 tick records, degrees 0..180;
- exactly 19 labels, values 0,10,...,180;
- major count 19;
- intermediate count 18;
- minor count 144;
- label values unique;
- every tick radial from the same origin.

`PROMPT_PROTRACTOR_181_POSITION_MANIFEST_QA`
`PROMPT_PROTRACTOR_LABEL_UNIQUENESS_QA`

Missing/extra/merged ticks or duplicate/missing labels are critical academic defects.
