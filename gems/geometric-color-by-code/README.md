# Geometric Color-by-Code

Status: Production Gem family
Canonical instruction: `GEM_INSTRUCTIONS_PRODUCTION.md`

## Purpose

Geometric Color-by-Code creates worksheet-generation prompts and verified blueprints in which a user-selected geometric shape acts as the primary visual construction grammar of the page. The picture should emerge from repeated geometric tiles or cells, similar to mosaic / tessellation / tiled artwork, rather than drawing a conventional illustration and merely overlaying geometric lines.

## Core product idea

```text
User request
→ Normalized worksheet spec
→ Verified content blueprint
→ Answer/code/color mapping
→ Geometric tiling grammar
→ Theme silhouette from tile grouping
→ Question-region grouping
→ Render pipeline selection
→ Final worksheet output
→ QA
```

Key distinction:

```text
CORRECT: shape → tiles → grouped silhouette → recognizable themed image
WRONG: themed illustration → geometric grid drawn on top
```

## Default behavior

- Page: A4 Portrait
- Language: Thai-first
- Question count: 24
- Color count: 6
- Primary shape: Triangle
- Shape dominance: High
- Tiling mode: Tessellation / Mosaic
- Question regions: grouped from many micro tiles
- Main worksheet: monochrome / coloring-friendly
- Color legend: real color preview allowed
- Answer key: enabled
- Line quality: crisp, clean, vector-like
- Tile density: controlled for print quality
- Preferred production renderer: deterministic/vector when available

## Document map

### Core
- `GEM_INSTRUCTIONS_PRODUCTION.md` — canonical Gem behavior and parameter contract
- `USER_GUIDE.md` — practical teacher/user guide
- `OUTPUT_CONTRACT.md` — required pipeline outputs and integrity rules
- `CONVERSATION_STARTERS.md` — ready-to-use starter commands

### Examples
- `examples/USAGE_EXAMPLES.md` — minimal, detailed, revision and edge-case commands

### Policies
- `policies/GEOMETRY_LAYOUT_POLICY.md` — shape grammar, tiling, silhouette, question-region construction and topology
- `policies/LINE_RENDERING_POLICY.md` — crisp printable line quality, stroke, tile-density and junction rules
- `policies/RENDER_PIPELINE_POLICY.md` — VECTOR_FIRST / HYBRID / IMAGE_PROMPT_ONLY render strategy
- `policies/COLOR_MAPPING_POLICY.md` — answer/code/color mapping and legend integrity
- `policies/PAGE_FORMAT_POLICY.md` — page size, orientation, print layout, density and pagination

### QA
- `qa/ACCEPTANCE_TESTS.md` — critical production acceptance tests
- `qa/REGRESSION_TESTS.md` — recurring failure-prevention tests
- `qa/DRY_RUN_REPORT.md` — 9-round dry-run findings and hardening record
- `qa/LINE_QUALITY_REMEDIATION_REPORT_2026-08-27.md` — line-fragmentation root cause, proof tests and closure criteria

## Documentation completeness gate

A change is not considered complete if it changes user-visible behavior but leaves related documentation inconsistent. Update, as applicable:

```text
Canonical instruction
→ User guide
→ Output contract
→ Policies
→ Usage examples / conversation starters
→ Acceptance & regression tests
→ Changelog
```

## Design priority

```text
CORRECTNESS
> MAPPING INTEGRITY
> SHAPE-AS-PRIMARY-GRAMMAR
> CRISP LINE QUALITY
> TOPOLOGY QUALITY
> READABILITY
> PRINT USABILITY
> THEME RECOGNIZABILITY
> DECORATION
```

## Production rendering recommendation

```text
BEST = verified content + deterministic SVG/PDF geometry/text
GOOD = AI-assisted composition + deterministic vector finalization
FALLBACK = strict image prompt + iterative line-quality QA
```

For fallback image rendering, reduce micro-tile density and simplify geometry before regenerating when line quality fails. Do not repeatedly render the same over-dense geometry.

## Example

```text
สร้างใบงาน Color by Code
ระดับชั้น ป.3
วิชา คณิตศาสตร์
เรื่อง การบวกเลข 1 หลัก
30 ข้อ 6 สี
ธีม สวนดอกไม้
ใช้รูปสามเหลี่ยมเป็นรูปทรงหลัก
ให้ภาพสวนดอกไม้เกิดจากการเรียงสามเหลี่ยมแบบ mosaic/tessellation
A4 แนวตั้ง
```

The Gem should resolve this into verified academic content first, then construct the visual grammar. Important questions, answers, mappings and visible academic text must not be invented by the image model. Final printable line boundaries should be deterministic/vector when the environment supports that mode.
