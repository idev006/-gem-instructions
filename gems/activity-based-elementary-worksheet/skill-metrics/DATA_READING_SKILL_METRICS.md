# DATA_READING Skill Metrics

SKILL_ID=DATA_READING
OWNER=W06_MONEY_CALENDAR_DATA
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- canonical dataset first;
- table cells map exact values;
- bar height maps exact axis value;
- pictograph count×key maps exact value;
- learner-read numeric axes inherit scale integrity.

## PROMPT_METRICS

- dataset correctness 20%; data-to-visual mapping 25%; axis/topology 20%; labels/key 15%; pedagogy/QA 20%.

## ARTIFACT_METRICS

- zero baseline unless truncated-axis lesson explicit;
- no 3D distortion;
- bars/icons/labels unambiguous;
- decoration cannot resemble data marks.

## CRITICAL_DEFECTS

- bar/axis mismatch;
- wrong pictograph key/count;
- missing/extra axis graduation;
- ambiguous table alignment.

## REPAIR_PROTOCOL

Return to canonical dataset, rebuild visualization from data coordinates, rerun W07 when numeric axis is learner-read.

## REGRESSION_HOOKS

`scale_line_integrity_regression_suite.py`; `full_skill_matrix_suite.py`; capability scorecard.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.


## RUNTIME_INVARIANT

`CANONICAL_STATE_REQUIRED=YES`
Canonical state = dataset, category order, axis origin/increment, pictograph key and exact data-to-visual mapping. Numeric axes inherit scale/tick integrity and no 3D/decorative distortion may alter apparent values.
