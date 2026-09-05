# TEMPERATURE Skill Metrics

SKILL_ID=TEMPERATURE
OWNER=W05_TEMPERATURE_CAPACITY_VOLUME
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- canonical profile 0–50°C @1°C: 50 intervals/51 positions; major=6, intermediate=5, ordinary minor=40;
- every 10°C span=10 intervals/9 interior;
- liquid endpoint exactly on target graduation.

## PROMPT_METRICS

- topology 25%; hierarchy/local recount 20%; target representability 15%; liquid alignment 20%; direction/labels 10%; QA/pedagogy 10%.

## ARTIFACT_METRICS

- all graduations complete and monotonic;
- endpoint exactly aligns target centerline;
- unit and labels legible;
- bulb/stem not counted as scale.

## CRITICAL_DEFECTS

- missing/extra tick;
- wrong hierarchy/value order;
- liquid endpoint between/wrong ticks.

## REPAIR_PROTOCOL

Rebuild tick set and target index from canonical range/resolution, then redraw liquid endpoint.

## REGRESSION_HOOKS

`metrology_full_audit_regression_suite.py`; `instrument_geometry_artifact_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.


## RUNTIME_INVARIANT

`CANONICAL_STATE_REQUIRED=YES`
Canonical state = range/resolution, exact tick set/classes, target index and liquid endpoint. Major 10°C > intermediate 5°C > minor 1°C hierarchy must not add or remove positions.
