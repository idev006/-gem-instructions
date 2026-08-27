# Geometric Color-by-Code

Status: Production Gem family
Canonical instruction: `GEM_INSTRUCTIONS_PRODUCTION.md`
Current production version: 1.7.0 — Twin Output Integrity

## Purpose
สร้าง verified multi-subject Color-by-Code worksheet plans ที่ใช้รูปทรงเรขาคณิตเป็น construction grammar หลัก ใช้ Natural Harmony ช่วยเรื่อง placement/scale/rhythm เมื่อเหมาะสม และผลิต Student Worksheet + Colored Answer Key จาก geometry/mapping master เดียวกัน

## Core product idea
```text
User request
→ Verified content
→ Answer/code/color mapping
→ Primary-shape grammar
→ Natural-Harmony composition
→ Deterministic master geometry
→ Student worksheet view
→ Colored answer-key view
→ Pair + visual + print QA
```

```text
CORRECT: one master geometry + one verified mapping → two render views
WRONG: generate student and answer-key images independently
```

## Default production behavior
- A4 Portrait
- Thai-first
- 24 questions
- 6 colors
- Triangle primary shape
- HIGH shape dominance
- Natural Harmony AUTO
- Student main artwork = monochrome/unfilled
- colored legend preview allowed
- Answer Key = fully colored solution view
- Student and Answer Key share identical region topology/text/mapping
- clean 3-level stroke hierarchy
- deterministic/vector final printable boundaries

## Reference strategy
- `REFERENCE_WOW` — visual impact/richness
- `REFERENCE_BEAUTIFUL` — cleanliness/balance/readability
- `REFERENCE_NATURAL_HARMONY_V3` — combines both plus natural rhythm/hierarchy

## Document map
### Core
- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `USER_GUIDE.md`
- `OUTPUT_CONTRACT.md`
- `CONVERSATION_STARTERS.md`

### Policies
- `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`
- `policies/GEOMETRY_LAYOUT_POLICY.md`
- `policies/LINE_RENDERING_POLICY.md`
- `policies/RENDER_PIPELINE_POLICY.md`
- `policies/NATURAL_PROPORTION_POLICY.md`
- `policies/REFERENCE_VERSION_POLICY.md`
- `policies/GOLDEN_REFERENCE_STANDARD.md`
- `policies/COLOR_MAPPING_POLICY.md`
- `policies/PAGE_FORMAT_POLICY.md`

### Examples / QA
- `examples/USAGE_EXAMPLES.md`
- `qa/ACCEPTANCE_TESTS.md`
- `qa/REGRESSION_TESTS.md`
- `qa/V1_6_FINALIZATION_CHECKLIST.md`
- `qa/DRY_RUN_REPORT.md`
- `qa/LINE_QUALITY_REMEDIATION_REPORT_2026-08-27.md`

## Final quality priority
```text
CORRECTNESS
> MAPPING INTEGRITY
> STUDENT/ANSWER PAIR IDENTITY
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
