# Output Contract — Activity-Based Elementary Worksheet Generator

Version: 1.0.0

Default mode: `PROMPT_PACKAGE`

## Required section order

1. `NORMALIZED_WORKSHEET_SPEC`
2. `VERIFIED_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

The user may explicitly request `PROMPT_ONLY` or `BLUEPRINT_ONLY`. Hidden validation must still run even when intermediate sections are omitted from the response.

## A. NORMALIZED_WORKSHEET_SPEC

Must contain the effective values that govern the output, including at minimum when applicable:

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
```

For time worksheets also include the active time constraints that materially affect generation.

## B. VERIFIED_CONTENT_BLUEPRINT

For `START_TIME_END_TIME_TO_DURATION`, use columns equivalent to:

```text
ID | ACTIVITY | ICON | START_TIME | END_TIME | VERIFIED_ANSWER
```

Requirements:

- exactly one row per question;
- all source values deterministic;
- all answers independently checked;
- verified answers may be shown in the blueprint but must remain hidden from student blanks when `SHOW_ANSWER_KEY = NO`.

## C. LAYOUT_BLUEPRINT

Must specify:

- page size and orientation;
- page count or pagination plan;
- student-header area;
- title/instruction area;
- question-row structure;
- row density;
- answer-space requirements;
- illustration/decorative zones;
- safe-margin behavior.

## D. RENDER_CONSTRAINTS

Must identify hard constraints that the image model must not improvise.

For time worksheets include at minimum:

```text
CONTENT_LOCK = ON
THAI_TEXT_LOCK = ON
NUMERIC_VALUE_LOCK = ON
QUESTION_COUNT_LOCK = ON
STUDENT_ANSWER_BLANKS = EMPTY when SHOW_ANSWER_KEY = NO
NO_EXTRA_QUESTIONS
NO_OMITTED_QUESTIONS
NO_CROPPED_TEXT
NO_TEXT_ILLUSTRATION_OVERLAP
```

## E. QA_REPORT

Show applicable gates in a compact form:

```text
INTENT_QA = PASS|FAIL
ACADEMIC_QA = PASS|FAIL
CALCULATION_QA = PASS|FAIL
DUPLICATE_QA = PASS|FAIL
THAI_QA = PASS|FAIL
LAYOUT_QA = PASS|FAIL
PRINT_QA = PASS|FAIL
PROMPT_QA = PASS|FAIL
```

If the Gem automatically repairs an issue, note the repair briefly.

A critical FAIL blocks final prompt release until fixed.

## F. FINAL_IMAGE_GENERATION_PROMPT

The final prompt must be self-contained and contain:

- page specification;
- target learner and subject;
- exact title and instruction text;
- exact student-header text;
- exact verified question data;
- exact question count;
- row anatomy;
- layout requirements;
- visual/illustration requirements;
- Thai text lock;
- numeric value lock;
- answer-key behavior;
- hard negative constraints.

The final prompt must not rely on hidden calculations or unstated data.

## Student worksheet vs answer key

When `SHOW_ANSWER_KEY = NO`:

- verified answers exist only for QA/blueprint logic;
- student response areas remain blank;
- final prompt explicitly prohibits pre-filled answers.

When `SHOW_ANSWER_KEY = YES`:

- keep the student worksheet unsolved;
- generate a separate answer-key page or clearly separated answer-key output unless the user explicitly requests inline solutions.

## Revision contract

A follow-up request must first mutate the normalized specification. Then regenerate only affected components and rerun all dependent QA.

Examples:

- theme change → preserve content unless requested otherwise; rerun layout/render QA;
- difficulty change → regenerate affected question data; rerun academic/calculation/layout QA;
- orientation change → preserve content; rerun layout/print/prompt QA;
- question-count change → regenerate content count and pagination plan; rerun all count-dependent QA.

Never patch only the prose of the final prompt while leaving the canonical blueprint inconsistent.
