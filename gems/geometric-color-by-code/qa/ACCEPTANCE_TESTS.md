# Geometric Color-by-Code — Acceptance Tests

Version: 1.4.0

## Critical production gates

1. Default page = A4 Portrait when unspecified.
2. `QUESTION_REGION_COUNT = QUESTION_COUNT` by default.
3. Exact requested question count and color count are preserved.
4. Every question has a verified correct answer.
5. Every normalized answer/code maps to one color only.
6. Legend and answer key use the same mapping source.
7. No orphan legend entry by default.
8. Focus category distribution is genuinely emphasized when requested.
9. Answer/color frequency plan is frozen before render when applicable.
10. Primary shape dominates the main activity area.
11. HIGH dominance targets about >=85% primary-shape structural rhythm.
12. Theme silhouette is built from tile grouping, not a freeform illustration overlay.
13. Question regions derive from primary-shape grouping by default.
14. `TILE_SCALE_VARIATION = CONTROLLED` across the page.
15. `MIN_COLORABLE_CELL_SIZE = AGE_APPROPRIATE_PRINT_USABLE` passes.
16. `MIN_SEGMENT_LENGTH = ENFORCED`; no visual-noise micro segments.
17. No unusable sliver/needle cells.
18. Freeform detail is limited to small recognizability details.
19. No freeform major object when shape dominance is HIGH.
20. Stroke hierarchy passes: frame > silhouette > internal tile.
21. Internal tile strokes remain crisp and printable.
22. No sketch texture, fuzzy edge, hairline, double stroke, broken line or ambiguous border.
23. No accidental starburst junctions.
24. Shared borders read as one clean boundary.
25. Every intended coloring region is visually closed.
26. Question text has a safe area and does not collide with tile borders.
27. Thai visible text passes spelling/glyph/render QA.
28. Main artwork is monochrome by default; actual color is limited to controlled legend previews.
29. Print-safe margins and no clipping.
30. High-density requests reduce micro detail or paginate before sacrificing line/text quality.
31. Follow-up revisions preserve unrelated verified content.
32. Render mode is resolved honestly; raster candidate with broken lines cannot be called production-ready.

## Golden Reference promotion gate

A candidate may be promoted to Golden Reference only when:
- all critical gates above PASS
- academic/mapping accuracy is complete
- line clarity is commercial-print quality
- primary shape is obvious at first glance
- colorability is practical for the target grade
- visual hierarchy is clean
- no major freeform drift exists

Golden Reference is a quality target, not a fixed composition template.

## Triangle-garden reference case

Input:

```text
ป.3 คณิตศาสตร์ การบวกเลข 1 หลัก
30 ข้อ 6 สี
ธีมสวนดอกไม้
PRIMARY_SHAPE = TRIANGLE
TILING_MODE = MOSAIC
A4 Portrait
```

Expected:
- 30 verified questions
- 6 colors
- target about 5 regions per color when valid
- triangle-built flowers/leaves/butterflies/clouds/ground
- clean vector-like line
- controlled tile density
- no tiny sliver cells
- stroke hierarchy visible
- monochrome main art + colored legend preview
