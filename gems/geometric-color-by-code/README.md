# Geometric Color-by-Code

Status: Production Gem family
Canonical instruction: `GEM_INSTRUCTIONS_PRODUCTION.md`
Current production version: 1.8.0 — Answer-First Generation Integrity

## Purpose
สร้าง verified multi-subject Color-by-Code worksheet plans ที่กำหนด **active answer/code set + color mapping ก่อนสร้างโจทย์** เพื่อรับประกันว่าทุกข้อมีสีรองรับ จากนั้นจึงใช้ geometric construction grammar, Natural Harmony และ deterministic rendering สร้างใบงานที่ถูกต้องและพิมพ์ใช้งานได้จริง.

## Core product idea
```text
User request
→ Active answer/code set
→ Color mapping + usage distribution
→ Target answer/code per region
→ Generate verified questions from targets
→ Freeze mapping
→ Primary-shape grammar
→ Natural-Harmony composition
→ Deterministic master geometry
→ Student worksheet
→ Answer key when requested
→ Mapping + visual + print QA
```

```text
CORRECT: answer/code/color plan first → generate questions from targets
WRONG: generate arbitrary questions first → discover answers → try to fit colors afterward
```

## Hard mapping rule
```text
NO QUESTION MAY PRODUCE AN ANSWER/CODE OUTSIDE THE ACTIVE LEGEND.
```

A single out-of-legend answer blocks final rendering.

## Default production behavior
- Thai-first
- `CONTENT_GENERATION_MODE = ANSWER_FIRST`
- active answer/code set resolved before question generation
- color usage plan frozen before question generation
- generated questions derive from target answers/codes
- Student Worksheet = A4 Portrait, monochrome/unfilled
- Answer Key = separate A4 Portrait when requested
- 24 questions / 6 colors by default
- 40–50 items on one Student A4 page is a stress-case target only when readability/colorability/print QA pass
- Triangle primary shape
- HIGH shape dominance
- Natural Harmony AUTO
- colored legend preview allowed
- clean 3-level stroke hierarchy
- deterministic/vector final printable boundaries

## Document map
### Core
- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `USER_GUIDE.md`
- `OUTPUT_CONTRACT.md`
- `CONVERSATION_STARTERS.md`

### Policies
- `policies/ANSWER_FIRST_GENERATION_POLICY.md`
- `policies/COLOR_MAPPING_POLICY.md`
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
- `qa/LINE_QUALITY_REMEDIATION_REPORT_2026-08-27.md`

## Final quality priority
```text
ACADEMIC CORRECTNESS
> COMPLETE ACTIVE-LEGEND COVERAGE
> ANSWER-FIRST GENERATION INTEGRITY
> MAPPING INTEGRITY
> USER INTENT
> READABILITY
> COLORING USABILITY
> DETERMINISTIC FINAL GEOMETRY
> LINE / TOPOLOGY QUALITY
> GEOMETRIC GRAMMAR
> NATURAL HARMONY
> THAI/TEXT RENDERING
> PRINT USABILITY
> THEME RECOGNIZABILITY
> DECORATION
```
