# Geometric Color-by-Code — Acceptance Tests

## Critical gates

1. Default page = A4 Portrait when unspecified.
2. `QUESTION_REGION_COUNT = QUESTION_COUNT` by default.
3. `MICRO_TILE_COUNT` may exceed question count.
4. Exact requested color count must be preserved.
5. Every question has verified correct answer.
6. Every normalized answer/code maps to one color only.
7. Legend and answer key come from the same mapping source.
8. Primary shape must dominate the main activity area.
9. Theme silhouette must be built from tile grouping, not freeform illustration overlay.
10. Question text must remain readable.
11. Main art monochrome by default.
12. Thai visible text must pass critical QA.
13. Print-safe margins and no overlap.
14. High-density requests must paginate before shrinking text below usable size.
15. Follow-up revisions preserve unrelated parameters/content.
16. No unsupported claim of exact tessellation for shapes/modes that only approximate tessellation.

## Dry-run reference case

Input:

```text
ขอใบงาน color by code
ธีม สวนดอกไม้
วิชา คณิตการบวกเลข 1 หลัก
จำนวน 30 ข้อ
จำนวน 6 สี
ระดับชั้น ป.3
ให้ใช้รูปสามเหลี่ยมเป็นหลักในการสร้างภาพ
อยากได้แบบการปูกระเบื้อง mosaic
```

Expected:
- 30 verified one-digit addition questions
- 6 colors
- triangle primary shape
- triangle-dominant mosaic
- micro tiles > 30 allowed
- 30 grouped question regions
- garden recognizability from triangle clusters
- no large freeform flowers replacing the mosaic
- A4 Portrait default
- monochrome main art + colored legend preview

## Multi-subject regression set

- Math: one-digit addition, triangle mosaic
- Math: multiplication, square tessellation
- Thai: vowel-word categories, diamond mosaic
- English: vocabulary categories, hexagon mosaic
- Science: animal classification, honeycomb/hexagon
- Social studies: factual categories, mixed polygon mosaic

## Visual PASS

- clear geometric rhythm
- primary shape obvious
- theme recognizable
- no clutter
- no tiny question text
- no question collisions
- no decorative freeform art dominating tiles
