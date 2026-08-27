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
→ Final worksheet prompt
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

## Documents

- `GEM_INSTRUCTIONS_PRODUCTION.md` — canonical Gem behavior and parameter contract
- `USER_GUIDE.md` — practical teacher/user guide
- `OUTPUT_CONTRACT.md` — required pipeline outputs and integrity rules
- `examples/USAGE_EXAMPLES.md` — sample commands and edge cases
- `policies/GEOMETRY_LAYOUT_POLICY.md` — shape grammar, tiling, silhouette, region construction
- `policies/COLOR_MAPPING_POLICY.md` — color/code mapping and legend integrity
- `policies/PAGE_FORMAT_POLICY.md` — page size, orientation, print layout and pagination
- `qa/ACCEPTANCE_TESTS.md` — critical production acceptance tests
- `qa/REGRESSION_TESTS.md` — recurring failure-prevention tests
- `qa/DRY_RUN_REPORT.md` — dry-run findings and hardening record

## Design priority

```text
CORRECTNESS
> MAPPING INTEGRITY
> SHAPE-AS-PRIMARY-GRAMMAR
> READABILITY
> PRINT USABILITY
> THEME RECOGNIZABILITY
> DECORATION
```

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

The Gem should resolve this into verified academic content first, then construct the visual grammar. Important questions, answers, mappings and visible academic text must not be invented by the image model.
