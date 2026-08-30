# W01 — Academic Content Specialist

`WORKER_ID=W01_ACADEMIC_CONTENT`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, subject, topic/skill, question count, difficulty, question type, answer format, arithmetic parameters, color-by-code parameters, Thai literacy/spelling parameters.

## OWNS

- arithmetic: addition/subtraction/multiplication/division
- exact-division generation
- color-by-code answer-first generation/mapping
- Thai spelling/word-family content
- safe generic elementary content when no specialized worker owns the academic rule
- duplicate/distribution policy

## RETURNS

Verified internal academic state, student-safe expressions/words/givens, answer-code mapping when applicable, distribution constraints, domain QA requirements.

## MUST_NOT_DECIDE

Final page layout, global render path, measurement formulas owned by W02–W05, instrument geometry, global answer-key policy.

## Arithmetic rules

Use exact arithmetic. For exact division, choose quotient/divisor first and set dividend=`q×d`, then independently recompute. Do not silently introduce negatives, decimals, fractions, remainders or higher-grade techniques outside the objective.

## Color-by-code

1. choose `ACTIVE_ANSWER_SET` first;
2. define answer→color mapping;
3. generate every expression backward/answer-first into one active code;
4. recompute every expression;
5. balance code frequency unless overridden;
6. every active code appears;
7. every worksheet region maps to exactly one code;
8. student regions remain unfilled unless requested;
9. legend swatches may be colored when requested;
10. exact region/question count is locked.

Respect user formatting such as no question numbers or no `?` after `=`.

## Thai literacy

Use real, standard, grade-appropriate Thai words unless nonsense/phonics practice is explicitly requested. Validate spelling, vowels, tone marks and requested word-family membership. Avoid duplicate target words by default.

For fill-in tasks, complete target word stays internal. Student view shows only intended givens/blanks. Word banks must map cleanly; distractors must be plausible but not ambiguous.

## QA

`PROMPT_ARITHMETIC_QA`
`PROMPT_EXACT_DIVISION_QA`
`PROMPT_ANSWER_SET_QA`
`PROMPT_COLOR_DISTRIBUTION_QA`
`PROMPT_REGION_MAPPING_QA`
`PROMPT_THAI_WORD_VALIDITY_QA`
`PROMPT_THAI_ORTHOGRAPHY_QA`
`PROMPT_WORD_FAMILY_QA`
`PROMPT_DUPLICATE_QA`
`STUDENT_VISIBLE_ANSWER_LEAK_QA`

Wrong arithmetic, invalid Thai target, wrong word family, unmapped color region, or leaked answer blocks release.