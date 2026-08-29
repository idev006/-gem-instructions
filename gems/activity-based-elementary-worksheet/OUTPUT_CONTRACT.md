# Output Contract — Activity-Based Elementary Worksheet Generator

Version: 1.1.0

Default mode: `PROMPT_PACKAGE`

## Required section order

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

The user may explicitly request `PROMPT_ONLY` or `BLUEPRINT_ONLY`. Hidden validation must still run even when intermediate sections are omitted.

## Internal vs user-visible data

The Gem maintains two views:

- `INTERNAL_VERIFIED_BLUEPRINT` — contains hidden verified answers and QA metadata.
- `STUDENT_CONTENT_BLUEPRINT` — contains only student-facing givens, labels, icons, units, and blank response areas.

When `SHOW_ANSWER_KEY = NO`, verified answers MUST NOT appear in the user-visible blueprint or final student image prompt unless the user explicitly asks to inspect QA answers.

This separation is a critical release requirement.

## A. NORMALIZED_WORKSHEET_SPEC

Include effective values that govern the output, including when applicable:

```text
GRADE_LEVEL
SUBJECT
DOMAIN
TOPIC
SUBTOPIC
LEARNING_OBJECTIVE
QUESTION_TYPE
QUESTION_COUNT
DIFFICULTY
LANGUAGE
PAGE_SIZE
ORIENTATION
COLOR_MODE
SHOW_STUDENT_HEADER
SHOW_QUESTION_NUMBER
SHOW_ANSWER_KEY
AUTO_PAGINATION
VISUAL_THEME
TEXT_RENDER_MODE
```

For time worksheets include active time constraints that materially affect generation.

## B. STUDENT_CONTENT_BLUEPRINT

For `START_TIME_END_TIME_TO_DURATION`, use columns equivalent to:

```text
ID | ACTIVITY | ICON | START_TIME | END_TIME | ANSWER_RENDER | UNIT_RENDER
```

Requirements:

- exactly one row per question;
- all source values already validated internally;
- response field is blank when answer key is disabled;
- no hidden answer column in student-facing output;
- no internal QA metadata leaked into render data.

## C. INTERNAL_VERIFIED_BLUEPRINT

Not returned by default when `SHOW_ANSWER_KEY = NO`.

Internal structure should retain values equivalent to:

```text
ID | START_TIME | END_TIME | VERIFIED_DURATION_MINUTES | VERIFIED_ANSWER_DISPLAY | VALIDATION_STATUS
```

It is authoritative for calculation QA and may be exposed only when the user explicitly requests answer/QA inspection or when generating a separate answer key.

## D. LAYOUT_BLUEPRINT

Must specify:

- page size and orientation;
- page count or pagination plan;
- student-header area;
- title/instruction area;
- question-row structure;
- density;
- answer-space requirements;
- illustration/decorative zones;
- safe-margin behavior;
- treatment for multi-component answers.

## E. RENDER_CONSTRAINTS

At minimum:

```text
CONTENT_LOCK = ON
THAI_TEXT_LOCK = ON
NUMERIC_VALUE_LOCK = ON
QUESTION_COUNT_LOCK = ON
ANSWER_LEAK_GUARD = ON
STUDENT_ANSWER_BLANKS = EMPTY when SHOW_ANSWER_KEY = NO
NO_EXTRA_QUESTIONS
NO_OMITTED_QUESTIONS
NO_CROPPED_TEXT
NO_TEXT_ILLUSTRATION_OVERLAP
```

For Thai-heavy worksheets, default `TEXT_RENDER_MODE = HYBRID`, preserving clean text zones for deterministic post-render correction if needed.

## F. QA_REPORT

Show applicable gates compactly:

```text
INTENT_QA = PASS|FAIL
DOMAIN_QA = PASS|FAIL
ACADEMIC_QA = PASS|FAIL
CALCULATION_QA = PASS|FAIL
CONSTRAINT_QA = PASS|FAIL
ANSWER_LEAK_QA = PASS|FAIL
DUPLICATE_QA = PASS|FAIL
THAI_QA = PASS|FAIL
LAYOUT_QA = PASS|FAIL
PRINT_QA = PASS|FAIL
PROMPT_QA = PASS|FAIL
```

A critical FAIL blocks final prompt release until repaired.

## G. FINAL_IMAGE_GENERATION_PROMPT

The final student prompt must be self-contained and contain:

- page specification;
- target learner and subject;
- exact title/instruction/header text;
- exact STUDENT-FACING question data only;
- exact question count;
- row anatomy;
- layout rules;
- illustration rules;
- Thai text lock;
- given-value lock;
- answer-key behavior;
- hard negative constraints.

Critical rule:

```text
If SHOW_ANSWER_KEY = NO, never include VERIFIED_ANSWER values anywhere in the final student image prompt.
```

The prompt may state expected response units, but must not include the numeric/semantic answer itself.

## Student worksheet vs answer key

When `SHOW_ANSWER_KEY = NO`:

- verified answers exist only internally;
- student response areas remain blank;
- student-facing blueprint omits answers;
- final prompt omits answers completely.

When `SHOW_ANSWER_KEY = YES`:

- keep the student worksheet unsolved;
- create a separate answer-key page/section by default;
- only use inline solved responses if explicitly requested.

## Revision contract

A follow-up request first mutates the normalized specification. Then regenerate affected components and rerun dependent QA.

Examples:

- theme change → preserve content; rerun layout/render QA;
- difficulty change → regenerate relevant question values; rerun domain/calculation/layout QA;
- orientation change → preserve content; rerun layout/print/prompt QA;
- question-count change → regenerate IDs/content/pagination; rerun count-dependent QA;
- answer-key toggle → preserve givens; rebuild student/answer views; rerun answer-leak/prompt QA.

Never patch only final-prompt prose while leaving canonical data inconsistent.