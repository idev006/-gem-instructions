# Geometric Color-by-Code — Visual Audit Remediation Plan

Date: 2026-08-27
Status: Implemented into v1.2.0
Reference case: ป.3 คณิตศาสตร์ การบวกเลข 1 หลัก 30 ข้อ 6 สี ธีมสวนดอกไม้ PRIMARY_SHAPE=TRIANGLE MOSAIC

## Audit summary

ผลลัพธ์ล่าสุดผ่านด้าน A4 layout, 30 questions, 6-color legend, monochrome main art, readability และ theme recognizability แต่ยังพบ visual fidelity issues ที่ต้อง harden ก่อนใช้เป็น production reference

## Findings

1. Triangle mosaic ยังมี freeform flower petals, leaves, butterfly wings และ clouds มากเกินไป
2. บาง question regions เป็นวงกลม/ใบไม้ freeform ไม่ derive จาก triangle grouping
3. tile scale ด้านบนและล่างของหน้าต่างกันมากจนเกิดสอง visual languages
4. พบความเสี่ยง accidental double lines, broken joins, ambiguous borders และ tiny sliver cells
5. answer/color usage ควรถูกวางแผน deterministic ก่อน render เช่น 30 ข้อ / 6 สี ≈ 5 regions ต่อสีเมื่อถูกต้องทางเนื้อหา

## Decisions

### D1 — Raise shape coverage target

```text
PRIMARY_SHAPE_COVERAGE_TARGET ≈ >=85%
```

### D2 — Prohibit major freeform objects when HIGH

```text
FREEFORM_MAJOR_OBJECTS = PROHIBITED_WHEN_HIGH
```

### D3 — Lock question-region grammar

```text
QUESTION_REGION_SHAPE_GRAMMAR = PRIMARY_SHAPE_GROUP
```

### D4 — Control tile scale

```text
TILE_SCALE_VARIATION = CONTROLLED
VISUAL_LANGUAGE_CONSISTENCY = REQUIRED
```

### D5 — Add topology QA

```text
LINE_TOPOLOGY_QA = CRITICAL
```

Must reject accidental double lines, broken joins, ambiguous shared borders, open regions and unusable sliver cells.

### D6 — Freeze answer/color frequency plan

For balanced numeric cases such as 30 questions / 6 colors, target approximately 5 regions per color when content-valid. The image model must not decide this distribution.

## Implementation scope

Updated:
- `GEM_INSTRUCTIONS_PRODUCTION.md` → v1.2.0
- `OUTPUT_CONTRACT.md` → v1.2.0
- `USER_GUIDE.md` → v1.2.0
- `examples/USAGE_EXAMPLES.md` → v1.2.0
- `policies/GEOMETRY_LAYOUT_POLICY.md` → v1.2.0
- `qa/ACCEPTANCE_TESTS.md` → v1.2.0
- `qa/REGRESSION_TESTS.md` → v1.2.0

## Closure criteria

A new triangle-garden test output can be considered reference-grade only when:
- all 30 questions and 6 colors match verified blueprint
- answer/color frequency plan is validated
- primary shape is visually dominant at first glance
- major flowers/leaves/butterflies/clouds/hills are built from triangle clusters
- question regions remain compatible with triangle grouping
- tile-scale variation is coherent across the page
- no large freeform object dominates
- no accidental double lines, broken joins or sliver cells
- text remains readable and print-safe

