# Geometric Color-by-Code — Color Mapping Policy

Version: 1.0.0
Status: Gem-specific policy

## Purpose

Define deterministic and auditable mapping from verified worksheet answers to color codes and the student-facing color legend.

## Mapping pipeline

```text
Question
→ Correct Answer
→ Normalized Answer / Code
→ Answer Group
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

## Supported response families

- `NUMERIC`
- `WORD`
- `SHORT_TEXT`
- `CHOICE`
- `CATEGORY`
- `TRUE_FALSE`
- `MATCH_CODE`

For non-numeric subjects, normalize text/category responses before color assignment. Do not force textual subjects into artificial numeric ranges.

## Distribution

Default target: `BALANCED`.

The mapping engine should distribute question regions across requested colors as evenly as practical while preserving content correctness.

Example for 30 questions / 6 colors:

- target average: 5 question regions per color
- minor imbalance is acceptable when needed for valid answer grouping
- correctness always overrides perfect numerical balance

## Student-facing legend

Default:

```text
LEGEND_COLOR_PREVIEW = YES
MAIN_ART_COLOR_MODE = MONOCHROME
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
Question ID | Correct Answer | Normalized Code | Color
```

## QA gates

PASS only when:
- all questions have verified answers
- no normalized code maps to more than one color
- all question regions have valid mapping records
- legend count equals requested color count
- legend colors and labels agree
- answer key agrees with worksheet mapping
- there are no orphan colors or orphan regions unless explicitly allowed
