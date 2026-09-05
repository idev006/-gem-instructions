# WEIGHT_SCALE Skill Metrics

SKILL_ID=WEIGHT_SCALE
OWNER=W03_WEIGHT_SCALE
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- canonical 0–5 kg @0.1 kg profile: 50 intervals / 51 active positions;
- each 1 kg span: 10 intervals / 11 endpoint-inclusive positions / 9 interior marks;
- +0.5 kg is existing index-5 intermediate tick;
- labels 0,1,2,3,4,5 clockwise at 0°,60°,120°,180°,240°,300°;
- inactive gap contains zero scale-like ticks.

## PROMPT_METRICS

- topology 25%; per-kg recount 20%; midpoint hierarchy 15%; label mapping 10%; needle mapping/center 15%; pedagogy/QA 15%.

## ARTIFACT_METRICS

- every 1 kg span visibly contains all required graduations;
- 0.5 tick longer than ordinary minor but weaker than major;
- needle pivot=center and tip aligns exact target tick;
- no pseudo-ticks in inactive gap.

## CRITICAL_DEFECTS

- missing/extra graduation;
- wrong label order;
- wrong midpoint hierarchy that changes reading;
- needle not aligned to target;
- inactive-gap scale marks.

## REPAIR_PROTOCOL

Rebuild visible tick set from canonical indices 0..50, then rebuild pointer from canonical target and common center.

## REGRESSION_HOOKS

`weight_dial_visible_subdivision_regression_suite.py`; `weight_dial_inactive_gap_regression_suite.py`; `instrument_geometry_artifact_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.


## RUNTIME_INVARIANT

`CANONICAL_STATE_REQUIRED=YES`
Canonical state = range/resolution, complete active tick index set, major/intermediate/minor class per index, label map, target tick and common pointer center. Tick hierarchy is data: major > 0.5 kg intermediate > ordinary 0.1 kg minor.
