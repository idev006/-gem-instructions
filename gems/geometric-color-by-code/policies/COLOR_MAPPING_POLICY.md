# Geometric Color-by-Code — Color Mapping Policy

Version: 1.1.0
Status: Gem-specific policy

## Purpose

Define deterministic and auditable mapping from verified worksheet answers to color codes and the student-facing color legend.

## Mapping pipeline

```text
Question
→ Correct Answer
→ Normalized Answer / Code
→ Answer Group / Category
→ Color ID
→ Legend Entry
→ Question Region
```

## Critical integrity rules

1. Every question has exactly one intended correct answer unless the canonical activity explicitly uses a controlled category/code response.
2. Every normalized answer/code maps to exactly one color within a worksheet.
3. One color may represent multiple normalized answers/codes when intentionally grouped.
4. No question region may receive a color that conflicts with its verified answer.
5. Legend entries must be generated from the same mapping source used by worksheet regions and answer key.
6. Changing the number of colors requires rebuilding the mapping; do not merely recolor the legend.
7. `QUESTION_COUNT`, answer data, region IDs and mapping counts must reconcile before prompt assembly.
8. Every student-facing legend entry must have at least one mapped question/region by default.
9. An unused legend color/category is a Critical FAIL unless the user explicitly requested an informational legend that may contain inactive entries.
10. If the activity says `เน้น <category>` / `focus <category>`, the focus distribution must be resolved and validated before mapping.

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

For vocabulary/classification activities, prefer atomic single-word responses when the learning objective does not require phrases. This reduces ambiguity and improves deterministic classification.

## Distribution

Default target: `BALANCED` unless a focus category is explicitly requested.

The mapping engine should distribute question regions across requested colors as evenly as practical while preserving content correctness and focus semantics.

Example for 30 questions / 6 colors:

- target average: 5 question regions per color
- minor imbalance is acceptable when needed for valid answer grouping
- correctness always overrides perfect numerical balance

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

## Answer key

The answer key must be generated from the same verified mapping data and should support at least:

```text
Question ID | Correct Answer | Normalized Code | Category | Color
```

For category activities, also retain aggregate usage counts per category/color so QA can verify coverage and focus ratios.

## QA gates

PASS only when:
- all questions have verified answers
- no normalized code maps to more than one color
- all question regions have valid mapping records
- legend count equals requested color count
- every legend entry has usage count >= 1 unless explicitly allowed otherwise
- focus-category distribution matches the resolved policy when applicable
- legend colors and labels agree
- answer key agrees with worksheet mapping
- there are no orphan colors or orphan regions unless explicitly allowed
