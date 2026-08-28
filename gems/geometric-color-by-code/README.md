# Geometric Color-by-Code

Status: Production Gem family
Canonical instruction: `GEM_INSTRUCTIONS_PRODUCTION.md`
Current production version: 1.8.1 — Answer-First + Deterministic Content Render

## Purpose
สร้าง verified multi-subject Color-by-Code worksheet ที่กำหนด active answer/code set + color mapping ก่อนสร้างโจทย์ และรักษา **visible academic content fidelity** จนถึงภาพ final ด้วย deterministic academic-text/legend overlay.

## Core product idea

```text
User request
→ Active answer/code set
→ Color mapping + usage distribution
→ Target answer/code per region
→ Generate verified questions from targets
→ Freeze content/mapping
→ Geometry + theme artwork
→ Deterministic academic-text overlay
→ Deterministic legend overlay
→ Post-render parity QA
→ Student / Answer Key output
```

```text
CORRECT:
verified data → deterministic visible academic content

WRONG:
verified data → ask image model to redraw questions/legend from memory
```

## Hard rules

```text
NO QUESTION MAY PRODUCE AN ANSWER/CODE OUTSIDE THE ACTIVE LEGEND.
IMAGE MODEL MAY NOT CREATE OR REWRITE FINAL ACADEMIC TEXT.
RENDERED CONTENT MUST MATCH VERIFIED CONTENT 100%.
```

## Default production behavior
- Thai-first
- `CONTENT_GENERATION_MODE = ANSWER_FIRST`
- `ACADEMIC_TEXT_RENDER_MODE = DETERMINISTIC_OVERLAY`
- active answer/code set resolved before question generation
- color usage plan frozen before question generation
- generated questions derive from target answers/codes
- Student Worksheet = A4 Portrait, monochrome/unfilled
- Answer Key = separate A4 Portrait when requested
- 40–50 items on one Student A4 page = stress target only when QA passes
- Triangle primary shape by default, HIGH dominance
- Natural Harmony AUTO
- deterministic/vector final printable boundaries
- `POST_RENDER_CONTENT_PARITY = REQUIRED`

## Document map

### Core
- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `USER_GUIDE.md`
- `OUTPUT_CONTRACT.md`
- `CONVERSATION_STARTERS.md`

### Policies
- `policies/ANSWER_FIRST_GENERATION_POLICY.md`
- `policies/COLOR_MAPPING_POLICY.md`
- `policies/DETERMINISTIC_CONTENT_RENDER_POLICY.md`
- `policies/TWO_PAGE_A4_OUTPUT_POLICY.md`
- `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`
- `policies/GEOMETRY_LAYOUT_POLICY.md`
- `policies/LINE_RENDERING_POLICY.md`
- `policies/RENDER_PIPELINE_POLICY.md`
- `policies/NATURAL_PROPORTION_POLICY.md`
- `policies/REFERENCE_VERSION_POLICY.md`
- `policies/GOLDEN_REFERENCE_STANDARD.md`
- `policies/PAGE_FORMAT_POLICY.md`

### QA
- `qa/ACCEPTANCE_TESTS.md`
- `qa/REGRESSION_TESTS.md`
- `qa/DRY_RUN_REPORT.md`
- `qa/ANSWER_FIRST_REMEDIATION_REPORT_2026-08-28.md`
- `qa/RENDER_CONTENT_FIDELITY_REMEDIATION_REPORT_2026-08-28.md`
- `qa/LINE_QUALITY_REMEDIATION_REPORT_2026-08-27.md`

## Final quality priority

```text
VISIBLE ACADEMIC FIDELITY
> ACADEMIC CORRECTNESS
> COMPLETE ACTIVE-LEGEND COVERAGE
> ANSWER-FIRST GENERATION INTEGRITY
> MAPPING / QUESTION-ID / LEGEND PARITY
> USER INTENT
> READABILITY
> COLORING USABILITY
> DETERMINISTIC GEOMETRY
> LINE / TOPOLOGY QUALITY
> GEOMETRIC GRAMMAR
> NATURAL HARMONY
> PRINT USABILITY
> DECORATION
```
