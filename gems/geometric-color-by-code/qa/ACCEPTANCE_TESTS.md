# Geometric Color-by-Code — Acceptance Tests

Version: 1.2.0

## Critical gates

1. Default page = A4 Portrait when unspecified.
2. `QUESTION_REGION_COUNT = QUESTION_COUNT` by default.
3. `MICRO_TILE_COUNT` may exceed question count.
4. Exact requested color count must be preserved.
5. Every question has verified correct answer.
6. Every normalized answer/code maps to one color only.
7. Legend and answer key come from the same mapping source.
8. Every legend entry has at least one mapped question/region unless explicitly allowed otherwise.
9. If a focus category is requested, its resolved distribution must be greater than each secondary category and normally target about 40–60% of questions unless the user specifies another ratio.
10. Primary shape must dominate the main activity area.
11. With `SHAPE_DOMINANCE = HIGH`, target about >=85% of structural cell boundaries / visible tiling rhythm from primary-shape grammar.
12. `FREEFORM_MAJOR_OBJECTS = PROHIBITED_WHEN_HIGH` must be respected.
13. Theme silhouette must be built from tile grouping, not freeform illustration overlay.
14. `QUESTION_REGION_SHAPE_GRAMMAR = PRIMARY_SHAPE_GROUP` by default.
15. Question regions must remain compatible with the primary tiling grammar; large circular/leaf/freeform answer containers are not acceptable unless explicitly justified as small label anchors.
16. `TILE_SCALE_VARIATION = CONTROLLED`; the page must not split into unrelated large-tile and micro-tile visual systems.
17. Visual-language consistency must pass across the whole main activity area.
18. Question text must remain readable.
19. Main art monochrome by default.
20. Thai visible text must pass critical QA.
21. Print-safe margins and no overlap.
22. High-density requests must paginate before shrinking text below usable size.
23. Follow-up revisions preserve unrelated parameters/content.
24. No unsupported claim of exact tessellation for shapes/modes that only approximate tessellation.
25. For vocabulary/classification, prefer atomic single-word items when the learning objective does not require phrases.
26. Category usage counts, legend coverage, focus distribution, and answer/color frequency plan must be frozen before visual prompt assembly.
27. `LINE_TOPOLOGY_QA = CRITICAL` must pass: no accidental double lines, broken joins, ambiguous shared borders, unintended open regions, or unusable sliver cells.
28. Shared region borders must read as single clear boundaries and must not collide with question text.

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
- answer-frequency plan approximately 5 regions per color when mathematically/content-valid
- triangle primary shape
- triangle-dominant mosaic
- primary-shape coverage target about >=85%
- micro tiles > 30 allowed
- 30 grouped question regions
- question-region boundaries derived from triangle groups
- garden recognizability from triangle clusters
- flowers, leaves, butterflies, clouds, hills and ground bands built primarily from triangle clusters
- no large freeform flowers/leaves/clouds replacing the mosaic
- controlled tile scale across the page
- clean topology with no double lines/broken joins/sliver cells
- A4 Portrait default
- monochrome main art + colored legend preview

## Audit regression case — Thai category worksheet

Input intent:

```text
ป.3 ภาษาไทย มาตราตัวสะกด เน้นแม่กง
10 ข้อ
5 สี
PRIMARY_SHAPE = RHOMBUS
SHAPE_DOMINANCE = HIGH
```

Expected content plan example:

```text
แม่กง 5
แม่กน 2
แม่กม 1
แม่เกย 1
แม่เกอว 1
```

PASS only when:
- all 5 legend categories are actually used
- แม่กง has the highest count
- no ambiguous category item
- single-word items preferred where possible
- animal/scene silhouettes are constructed from rhombus-derived tile clusters
- no conventional freeform elephant/bird drawing with diamond pattern merely overlaid

FAIL example:

```text
แม่กง 4
แม่กน 4
แม่กม 2
แม่เกย 0
แม่เกอว 0
```

when the worksheet still says “เน้นแม่กง” and displays all five legend categories.

## Latest visual reference regression — triangle garden

FAIL if:
- flowers use large rounded freeform petals
- leaves are large freeform leaf containers for questions
- clouds use conventional scalloped freeform outlines
- circular question containers dominate flower centers
- top and bottom of page use visibly unrelated tile-scale systems
- ground mosaic contains accidental double lines or tiny sliver cells

PASS when those elements are reconstructed from triangle clusters while maintaining readable question areas.

## Multi-subject regression set

- Math: one-digit addition, triangle mosaic
- Math: multiplication, square tessellation
- Thai: vowel-word categories, diamond mosaic
- Thai: final-consonant categories with focus distribution
- English: vocabulary categories, hexagon mosaic
- Science: animal classification, honeycomb/hexagon
- Social studies: factual categories, mixed polygon mosaic

## Visual PASS

- clear geometric rhythm
- primary shape obvious at first glance
- theme recognizable
- controlled tile scale
- no clutter
- no tiny question text
- no question collisions
- no decorative freeform art dominating tiles
- question-region boundaries remain compatible with the primary tiling grammar
- line topology is closed, clean and practical for student coloring
