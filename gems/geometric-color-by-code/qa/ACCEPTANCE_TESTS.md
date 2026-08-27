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
21. No sketch texture, fuzzy edge, hairline, double stroke, broken line or ambiguous border.
22. No accidental starburst junctions.
23. Shared borders read as one clean deterministic boundary.
24. Every intended coloring region is visually closed.
25. Question text has a safe area and does not collide with tile borders.
26. Thai visible text passes spelling/glyph/render QA.
27. Main artwork is monochrome by default; actual color is limited to controlled legend previews.
28. Print-safe margins and no clipping.
29. High-density requests reduce micro detail or paginate before sacrificing line/text quality.
30. Follow-up revisions preserve unrelated verified content.
31. `PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED`.
32. Final printable boundaries come from deterministic geometry/vector paths.
33. Shared-edge topology is deterministic: one logical edge is rendered once.
34. Final visible academic text is deterministic for final print.
35. Any image-model-only raster is labeled preview/mockup, not production-final.
36. Production raster preview derives from vector master.

## Natural Harmony gates
When `COMPOSITION_SYSTEM = NATURAL_HARMONY` or AUTO resolves to Natural Harmony:
37. Focal hierarchy is visually clear.
38. `COMPOSITION_BALANCE` and `SYMMETRY_MODE` suit the theme.
39. Golden-section guidance does not distort content, legend, margins or question safe areas.
40. Fibonacci rhythm is used only where useful and not forced everywhere.
41. Phyllotaxis/golden-angle-inspired detail does not create cells below minimum colorable size.
42. Natural Harmony does not replace primary-shape construction grammar.
43. `QUESTION_FLOW = FOLLOW_VISUAL_RHYTHM` preserves exact content/mapping and maintains or improves readability.
44. `QUESTION_DISTRIBUTION_BALANCE = REQUIRED` passes.
45. Natural scale hierarchy shows focal / secondary / supporting levels coherently.
46. No exact golden-ratio/Fibonacci/golden-angle claim without calculated evidence.
47. Natural Harmony does not materially reduce cleanliness/readability versus `REFERENCE_BEAUTIFUL`.
48. Natural Harmony does not materially reduce visual impact versus `REFERENCE_WOW`.

## V3 promotion gate
A candidate may be promoted to `REFERENCE_NATURAL_HARMONY_V3` only when all applicable critical gates PASS and final production geometry is deterministic/vector-first.

## Cross-theme validation
Before treating the Natural Harmony engine as robust, test at least one non-flower theme such as solar system, underwater world, or rainforest. PASS only if the engine adapts composition to the theme instead of mechanically reproducing flower symmetry.

## Critical FAIL
FAIL production immediately if final raster linework is generative-only, exact content/mapping is altered for aesthetics, shared borders double/break, Thai glyphs are missing, natural pattern creates uncolorable micro-detail, or a raster-only mockup is labeled production-final/Golden Reference.
