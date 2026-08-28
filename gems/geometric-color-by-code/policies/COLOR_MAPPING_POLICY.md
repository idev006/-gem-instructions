# Geometric Color-by-Code — Color Mapping Policy

Version: 1.2.0
Status: Gem-specific policy

## Purpose

Define deterministic and auditable mapping for verified worksheet answers/codes, colors, legend entries, and regions. For generated worksheets, mapping is planned **before** question generation so every question is guaranteed to resolve to a displayed color.

Read together with `ANSWER_FIRST_GENERATION_POLICY.md`.

## Canonical mapping pipeline

Default generative workflow:

```text
Requested Color Count
→ Active Answer/Code Set
→ Color IDs / Legend Entries
→ Usage Distribution Plan
→ Target Answer/Code per Region
→ Generate Valid Question from Target
→ Verify Correct Answer
→ Freeze Question/Answer/Color/Region Record
```

Hard rule:

```text
NO QUESTION MAY PRODUCE AN ANSWER/CODE OUTSIDE THE ACTIVE LEGEND.
```

Question-first mapping is allowed only when the user supplies fixed questions/content and 100% legend coverage can be proven before render.

## Critical integrity rules

1. Every question has exactly one intended correct answer unless the canonical activity explicitly uses a controlled category/code response.
2. Every normalized answer/code maps to exactly one color within a worksheet.
3. One color may represent multiple normalized answers/codes only when intentionally grouped.
4. Every generated question must derive from a preassigned target answer/code that already has a valid legend color.
5. No question region may receive a color that conflicts with its verified answer.
6. Legend entries must be generated from the same mapping source used by worksheet regions and answer key.
7. Changing the number of colors requires rebuilding the active answer/code set and distribution before generating/revalidating affected questions.
8. `QUESTION_COUNT`, answer data, region IDs and mapping counts must reconcile before prompt/render assembly.
9. Every student-facing legend entry must have at least one mapped question/region by default.
10. An unused legend color/category is a Critical FAIL unless the user explicitly requested an informational legend that may contain inactive entries.
11. If the activity says `เน้น <category>` / `focus <category>`, the focus distribution must be resolved before question generation.
12. A question whose verified answer has no active legend entry is a Critical FAIL and blocks rendering.

## Required generation controls

```text
CONTENT_GENERATION_MODE = ANSWER_FIRST
ACTIVE_CODE_SET = RESOLVED_BEFORE_QUESTION_GENERATION
COLOR_USAGE_PLAN = FROZEN_BEFORE_QUESTION_GENERATION
QUESTION_GENERATION_SOURCE = TARGET_ANSWER_OR_CODE
```

## Category focus policy

For category-based activities:

```text
FOCUS_CATEGORY = <category> or NONE
CATEGORY_FOCUS_MODE = EMPHASIZED | BALANCED | CUSTOM | AUTO
```

If `EMPHASIZED` and no explicit percentage is provided, target approximately 40–60% of questions for the focus category, while keeping at least one question for every displayed legend category when feasible.

The focus category must have a greater question count than each secondary category unless arithmetic constraints or explicit user instructions make that impossible.

Example: 10 questions, 5 categories, focus = แม่กง:

```text
แม่กง 5
แม่กน 2
แม่กม 1
แม่เกย 1
แม่เกอว 1
```

A 4/4/2/0/0 distribution must FAIL if the legend still displays all 5 categories and claims the worksheet focuses on แม่กง.

## Supported response families

- `NUMERIC`
- `WORD`
- `SHORT_TEXT`
- `CHOICE`
- `CATEGORY`
- `TRUE_FALSE`
- `MATCH_CODE`

For non-numeric subjects, normalize text/category responses before color assignment. Do not force textual subjects into artificial numeric ranges.

For vocabulary/classification activities, prefer atomic single-word responses when the learning objective does not require phrases.

## Mathematics: target-answer generation

For numeric Color-by-Code activities:

```text
Target Answer
→ Generate operands/operator
→ Validate requested topic/grade constraints
→ Independently recompute answer
→ Accept only when answer == target
```

Example: exact division, 2-digit dividend ÷ 1-digit divisor. If target answer is `5`, valid candidates may include `20 ÷ 4`, `25 ÷ 5`, `30 ÷ 6`, `35 ÷ 7`, `40 ÷ 8`, `45 ÷ 9`, subject to duplicate and difficulty policies.

Never generate an arbitrary division question and then discover that its quotient is not represented in the legend.

## Distribution

Default target: `BALANCED` unless a focus category is explicitly requested.

The mapping engine resolves usage counts before questions are generated.

Example for 30 questions / 6 colors:
- target average: 5 question regions per color

Example for 48 questions / 6 colors:
- target: 8 question regions per color

When exact balance is impossible, use the smallest practical imbalance while preserving correctness. Sum of usage counts must equal `QUESTION_COUNT`.

## Student-facing legend

Default:

```text
LEGEND_COLOR_PREVIEW = YES
MAIN_ART_COLOR_MODE = MONOCHROME
LEGEND_COVERAGE_POLICY = NO_ORPHAN_LEGEND_ENTRY
```

The main worksheet remains black-and-white for student coloring. A small real-color sample may appear in the legend.

Allowed preview forms:
- swatch
- circle
- pencil tip
- compact colored-pencil/bar sample

The Thai/English color label must match the actual displayed color.

## Full monochrome override

If the user explicitly requests no color anywhere, including the legend:

```text
LEGEND_COLOR_PREVIEW = NO
```

Use text/number/code labels only.

## Required mapping record

Every generated question/region must have:

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

Required invariant:

```text
target_answer_or_code == normalized_answer_code
color_id == active_legend[normalized_answer_code]
validation_status == PASS
```

## Answer key

The answer key must be generated from the same verified mapping data and should support at least:

```text
Question ID | Correct Answer | Normalized Code | Category | Color
```

For category activities, also retain aggregate usage counts per category/color so QA can verify coverage and focus ratios.

## Pre-render QA gates

PASS only when:
- exact requested question count exists
- all questions have verified answers
- every verified answer/code is inside the active legend domain
- no normalized code maps to more than one color
- all question regions have valid mapping records
- all regions have a resolvable `color_id`
- legend count equals requested color count
- every displayed legend entry has usage count >= 1 unless explicitly allowed otherwise
- sum of color usage counts equals question count
- focus-category distribution matches the resolved policy when applicable
- legend colors and labels agree
- answer key agrees with worksheet mapping when requested
- there are no orphan colors, orphan answers, orphan questions, or orphan regions

Any failure above blocks final rendering.
