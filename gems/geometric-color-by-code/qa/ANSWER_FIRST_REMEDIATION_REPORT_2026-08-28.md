# Answer-First Remediation Report — 2026-08-28

Status: Implemented
Target release: Geometric Color-by-Code v1.8.0

## Incident

During a real Gem test for a Grade 3 exact-division Color-by-Code worksheet, several generated quotient values were not represented in the visible color legend. The worksheet looked visually strong, but some regions had no valid student action because no color was defined for their answers.

## Root cause

The previous specification described mapping integrity but did not make generation direction strict enough. The practical execution could still follow this anti-pattern:

```text
Generate arbitrary question
→ compute answer
→ attempt color mapping
```

This allows the question generator to produce answers outside the active legend domain.

Contributing factors:
1. `ANSWER_FREQUENCY_PLAN` existed but was not an explicit prerequisite to question generation.
2. Legend coverage checked displayed colors but did not explicitly forbid out-of-legend generated answers before render.
3. The math adapter did not require inverse/target-answer construction for every generated numeric question.
4. `ANSWER_KEY = NO` could be misread as reducing the need for hidden verified mapping, even though the Student worksheet still depends on complete mapping.
5. Image generation could visually reproduce question text without a hard pre-render record proving target-answer/color identity.

## Corrective architecture

Production generation is now:

```text
Resolve colors
→ resolve active answer/code set
→ map answer/code to color
→ freeze usage counts
→ assign target answer/code to each region
→ generate question from target
→ independently validate answer and subject constraints
→ freeze mapping
→ render
```

Hard invariant:

```text
NO QUESTION MAY PRODUCE AN ANSWER/CODE OUTSIDE THE ACTIVE LEGEND.
```

## Math-specific correction

For generated math questions, the engine must use target-answer generation. Example for exact division:

```text
Target quotient = 5
→ choose one-digit divisor d
→ dividend = 5 × d
→ require dividend to satisfy requested digit range
→ require divisor to satisfy requested digit range
→ verify dividend ÷ divisor = 5 with remainder 0
```

The same pattern generalizes to addition, subtraction, multiplication and other deterministic numeric topics.

## Development changes

1. Added `policies/ANSWER_FIRST_GENERATION_POLICY.md`.
2. Updated canonical `GEM_INSTRUCTIONS_PRODUCTION.md` to v1.8.0.
3. Updated `COLOR_MAPPING_POLICY.md` to v1.2.0.
4. Updated `OUTPUT_CONTRACT.md` with mandatory `ANSWER_CODE_COLOR_PLAN`.
5. Updated `USER_GUIDE.md` with answer-first examples.
6. Added acceptance gates for active legend closure, target-answer generation, usage reconciliation and exact division constraints.
7. Added regression tests against question-first generation and out-of-legend answers.
8. Updated README to describe the architecture.

## Required pre-render record

Every question/region must have:

```text
question_id
region_id
target_answer_or_code
prompt_text
verified_correct_answer
normalized_answer_code
color_id
legend_entry_id
validation_status
```

Rendering is blocked unless:

```text
target_answer_or_code == normalized_answer_code
normalized_answer_code IN active_legend
color_id == active_legend[normalized_answer_code]
validation_status == PASS
```

## QA closure criteria

PASS only when:
- requested question count is exact
- every question answer is correct
- every answer/code belongs to the active legend
- every region has a color ID
- all displayed legend entries are used unless explicitly allowed otherwise
- sum of color usage counts equals question count
- exact-division constraints pass when requested
- no visual generation changes academic text after mapping freeze
- Student mapping completeness passes even when `ANSWER_KEY = NO`

## Expected result

The Gem should no longer produce a visually valid but logically incomplete Color-by-Code worksheet where a child encounters a question whose answer has no corresponding color instruction.
