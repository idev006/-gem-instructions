# ACADEMIC_ARITHMETIC_THAI Skill Metrics

SKILL_ID=ACADEMIC_ARITHMETIC_THAI
OWNER=W01_ACADEMIC_CONTENT
PASS_THRESHOLD=95
CRITICAL_OVERRIDE=YES

## CANONICAL_ORACLE

- exact arithmetic and exact-division state;
- standard, grade-appropriate Thai orthography and requested word-family membership;
- no hidden answer leakage.

## PROMPT_METRICS

- arithmetic validity 25%; Thai/content validity 20%; answer-set/mapping integrity 15%; grade appropriateness 15%; duplicate/distribution control 10%; answer-format/visibility 15%.

## ARTIFACT_METRICS

- every visible expression/word is legible and unambiguous;
- response blank matches requested answer;
- no answer/key leak;
- theme does not alter academic content.

## CRITICAL_DEFECTS

- wrong arithmetic;
- invalid Thai spelling/word-family target;
- ambiguous or leaked answer.

## REPAIR_PROTOCOL

Repair canonical answer/word state, regenerate dependents, independently recheck all W01 QA.

## REGRESSION_HOOKS

`full_dry_run_suite.py`; `full_skill_matrix_suite.py`; `primary_school_pedagogy_regression_suite.py`.

## Release

`SKILL_PROMPT_SCORE>=95` is required for prompt release.
`SKILL_ARTIFACT_SCORE>=95` and zero critical defects are required for classroom release.
