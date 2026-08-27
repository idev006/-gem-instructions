# Geometric Color-by-Code

Status: Production Gem family
Canonical instruction: `GEM_INSTRUCTIONS_PRODUCTION.md`
Current production version: 1.4.0

## Purpose

Geometric Color-by-Code creates verified multi-subject Color-by-Code worksheet plans in which a user-selected geometric shape acts as the primary visual construction grammar. The themed picture emerges from repeated tiles/cells rather than a conventional illustration with geometry overlaid afterward.

## Core product idea

```text
User request
→ Verified content
→ Answer/code/color mapping
→ Geometric tiling grammar
→ Theme silhouette
→ Question-region grouping
→ Colorability + stroke planning
→ Render pipeline selection
→ Final output
→ QA
```

```text
CORRECT: shape → tiles → grouped silhouette → themed image
WRONG: themed illustration → geometric pattern overlay
```

## Default production behavior

- A4 Portrait
- Thai-first
- 24 questions
- 6 colors
- Triangle primary shape
- HIGH shape dominance
- grouped question regions
- monochrome main artwork
- colored legend preview allowed
- clean vector-like lines
- controlled tile density
- minimum colorable-area protection
- three-level stroke hierarchy
- deterministic/vector rendering preferred when available

## Document map

### Core
- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `USER_GUIDE.md`
- `OUTPUT_CONTRACT.md`
- `CONVERSATION_STARTERS.md`

### Examples
- `examples/USAGE_EXAMPLES.md`

### Policies
- `policies/GEOMETRY_LAYOUT_POLICY.md`
- `policies/LINE_RENDERING_POLICY.md`
- `policies/RENDER_PIPELINE_POLICY.md`
- `policies/GOLDEN_REFERENCE_STANDARD.md`
- `policies/COLOR_MAPPING_POLICY.md`
- `policies/PAGE_FORMAT_POLICY.md`

### QA
- `qa/ACCEPTANCE_TESTS.md`
- `qa/REGRESSION_TESTS.md`
- `qa/DRY_RUN_REPORT.md`
- `qa/LINE_QUALITY_REMEDIATION_REPORT_2026-08-27.md`

## Quality priority

```text
CORRECTNESS
> MAPPING
> GEOMETRIC GRAMMAR
> LINE / TOPOLOGY QUALITY
> COLORABILITY
> READABILITY
> THAI/TEXT RENDERING
> PRINT USABILITY
> THEME
> DECORATION
```

## Golden Reference

Golden Reference means a candidate has passed all critical academic, mapping, geometry, colorability, line, text and print gates. It is a quality target, not a fixed composition template.
