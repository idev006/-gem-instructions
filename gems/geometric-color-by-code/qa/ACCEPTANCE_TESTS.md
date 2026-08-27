# Geometric Color-by-Code — Acceptance Tests

Version: 1.6.0

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
32. `PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED` for final printable geometric worksheets.
33. Final printable boundaries come from deterministic geometry/vector paths, not directly from generative raster lines.
34. Shared-edge topology is deterministic: one logical edge is rendered once.
35. Final visible academic text is deterministic when final print output is produced.
36. Any image-model-only raster must be labeled preview/mockup, not production-final.
37. Raster preview for production should be rasterized from the vector master.

## Natural Proportion gates

เมื่อเปิด `COMPOSITION_SYSTEM = NATURAL_PROPORTION` หรือ AUTO resolve มาใช้ natural composition ต้อง PASS เพิ่ม:

38. Natural proportion improves composition without reducing readability or colorability.
39. `GOLDEN_RATIO_GUIDE` is used as a guide, not forced exact geometry unless explicitly calculated and validated.
40. `PHYLLOTAXIS_MODE` never creates micro-detail below minimum colorable/segment thresholds.
41. Fibonacci-inspired repetition does not alter verified question count or mapping.
42. Radial symmetry/petal rhythm remains compatible with the primary-shape grammar.
43. Natural scale hierarchy has a clear focal element, secondary elements, and supporting motifs.
44. Natural pattern does not override question safe areas, legend space, or print margins.
45. No unsupported claim of exact golden ratio, Fibonacci spiral, or golden-angle construction.
46. If natural rhythm conflicts with usability, usability wins and the natural pattern is simplified.

## Reference V3 promotion gate

A candidate may be promoted to `REFERENCE_NATURAL_HARMONY_V3` only when:
- all critical production gates PASS
- natural-proportion gates PASS when used
- visual impact is not materially weaker than `REFERENCE_WOW`
- cleanliness/readability is not materially weaker than `REFERENCE_BEAUTIFUL`
- composition shows deliberate focal hierarchy and natural rhythm
- geometric grammar remains obvious at first glance
- line clarity, Thai text, mapping and colorability remain production quality

## Golden Reference promotion gate

A candidate may be promoted to Golden Reference only when:
- all applicable gates above PASS
- academic/mapping accuracy is complete
- final geometry master is deterministic/vector-first
- line clarity is commercial-print quality
- primary shape is obvious at first glance
- colorability is practical for the target grade
- visual hierarchy is clean
- no major freeform drift exists
- Thai text shaping/glyphs are correct

Golden Reference is a quality target, not a fixed composition template.

## Triangle-garden reference case

Input:

```text
ป.3 คณิตศาสตร์ การบวกเลข 1 หลัก
30 ข้อ 6 สี
ธีมสวนดอกไม้
PRIMARY_SHAPE = TRIANGLE
TILING_MODE = MOSAIC
COMPOSITION_SYSTEM = NATURAL_PROPORTION
A4 Portrait
```

Expected:
- 30 verified questions
- 6 colors
- target about 5 regions per color when valid
- triangle-built flowers/leaves/butterflies/clouds/ground
- focal hierarchy inspired by natural proportion
- petal/seed rhythms may use radial, Fibonacci or phyllotaxis-inspired grouping
- no forced exact golden-ratio distortion
- deterministic vector final linework
- controlled tile density
- no tiny sliver cells
- stroke hierarchy visible
- monochrome main art + colored legend preview
- any PNG preview generated from vector master

## Critical render FAIL

FAIL production immediately if:
- final linework comes directly from image-model raster and shows broken/fuzzy strokes
- shared borders are doubled or inconsistent
- Thai glyphs are missing/tofu
- geometry must be guessed from a raster preview
- a raster-only mockup is labeled print-ready or Golden Reference
