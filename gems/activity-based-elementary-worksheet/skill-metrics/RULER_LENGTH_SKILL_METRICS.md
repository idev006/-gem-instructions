# RULER_LENGTH Skill Metrics

SKILL_ID=RULER_LENGTH
OWNER=W04_LENGTH_DISTANCE
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- 1 cm @1 mm: 10 intervals /11 positions /9 interior;
- physical ruler edge is not an extra graduation;
- zero-start uses ZERO_GRADUATION_X;
- nonzero length=end-start;
- object endpoints project to authoritative scale.

## PROMPT_METRICS

- topology 25%; zero/reference 20%; endpoint mapping 15%; nonzero arithmetic 15%; projection guides 10%; pedagogy/QA 15%.

## ARTIFACT_METRICS

- exact 1 mm graduations visible;
- 5 mm hierarchy reuses existing position;
- start/end projection guides align endpoints;
- no extra border-as-tick.

## CRITICAL_DEFECTS

- extra/missing tick;
- object aligned to physical edge instead of zero;
- endpoint guide/mapping wrong;
- end-start relation wrong.

## REPAIR_PROTOCOL

Reconstruct ruler coordinate system and graduation set first; then realign object endpoints and projection guides.

## REGRESSION_HOOKS

`measurement_reference_artifact_regression_suite.py`; `scale_line_integrity_regression_suite.py`; `instrument_geometry_artifact_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.


## RUNTIME_INVARIANT

`CANONICAL_STATE_REQUIRED=YES`
Canonical state = zero graduation coordinate, exact mm tick set, start/end graduation coordinates and projection guides. Physical border is never silently promoted to a graduation.
