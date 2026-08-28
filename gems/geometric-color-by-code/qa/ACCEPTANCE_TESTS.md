# Geometric Color-by-Code — Acceptance Tests

Version: 1.8.0

## Critical production gates

1. Default page = A4 Portrait when unspecified.
2. `QUESTION_REGION_COUNT = QUESTION_COUNT` by default.
3. Exact requested question count and color count are preserved.
4. `CONTENT_GENERATION_MODE = ANSWER_FIRST` by default for generated worksheets.
5. Active answer/code set is resolved before question generation.
6. Color usage distribution is frozen before question generation.
7. Every generated question is created from a preassigned target answer/code.
8. Every generated question has a verified correct answer equal to its target answer/code after normalization.
9. Every normalized answer/code maps to one color only.
10. Every verified answer/code belongs to the active legend domain.
11. No question may produce an answer/code outside the active legend.
12. Every question region has a resolvable `color_id` before render.
13. Sum of color-usage counts equals exact question count.
14. Legend and answer key use the same mapping source.
15. No orphan legend entry by default.
16. No orphan question, orphan answer/code, or orphan region.
17. Focus category distribution is genuinely emphasized when requested.
18. Answer/color frequency plan is frozen before render.
19. For mathematics, target-answer question generation independently validates the arithmetic result and all topic constraints.
20. For exact division, every problem divides evenly and satisfies requested digit constraints.
21. Primary shape dominates the main activity area.
22. HIGH dominance targets about >=85% primary-shape structural rhythm.
23. Theme silhouette is built from tile grouping, not a freeform illustration overlay.
24. Question regions derive from primary-shape grouping by default.
25. `TILE_SCALE_VARIATION = CONTROLLED` across the page.
26. `MIN_COLORABLE_CELL_SIZE = AGE_APPROPRIATE_PRINT_USABLE` passes.
27. `MIN_SEGMENT_LENGTH = ENFORCED`; no visual-noise micro segments.
28. No unusable sliver/needle cells.
29. Freeform detail is limited to small recognizability details.
30. No freeform major object when shape dominance is HIGH.
31. Stroke hierarchy passes: frame > silhouette > internal tile.
32. No sketch texture, fuzzy edge, hairline, double stroke, broken line or ambiguous border.
33. No accidental starburst junctions.
34. Shared borders read as one clean deterministic boundary.
35. Every intended coloring region is visually closed.
36. Question text has a safe area and does not collide with tile borders.
37. Thai visible text passes spelling/glyph/render QA.
38. Student main artwork is monochrome/unfilled by default; actual color is limited to controlled legend previews.
39. Print-safe margins and no clipping.
40. High-density requests reduce micro detail before sacrificing line/text quality.
41. Follow-up revisions preserve unrelated verified content.
42. `PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED`.
43. Final printable boundaries come from deterministic geometry/vector paths.
44. Shared-edge topology is deterministic: one logical edge is rendered once.
45. Final visible academic text is deterministic for final print.
46. Any image-model-only raster is labeled preview/mockup, not production-final.
47. Production raster preview derives from vector master.

## Twin Output & Answer-Key gates

48. `STUDENT_WORKSHEET_REQUIRED = YES` by default.
49. Student activity regions contain no solution fill color.
50. `ANSWER_KEY = YES` produces a separate colored solution view by default.
51. `PAIR_PRESENTATION_MODE = SEPARATE` by default.
52. Default Student page size = A4 Portrait.
53. Default Answer Key page size = A4 Portrait.
54. Default Student page count target = 1.
55. Default Answer Key page count target = 1.
56. Default package order is Page 1 Student, Page 2 Answer Key.
57. Student Worksheet and Answer Key must not be placed side-by-side or stacked on the same student-facing page.
58. Student and Answer Key use the same `master_geometry_id` / geometry version.
59. Student and Answer Key contain identical region IDs and region boundaries.
60. Student and Answer Key contain identical question IDs and verified prompt text.
61. Student and Answer Key use the same legend/mapping source.
62. Answer Key fill colors come only from `VERIFIED_COLOR_MAPPING`.
63. For every `region_id`, `answer_key.fill_color_id == verified_mapping[question_id]`.
64. A single wrong answer-key region color is a Critical FAIL.
65. Answer Key may add `เฉลย`/teacher annotation but may not change topology or academic content.
66. Answer Key is not generated from an independent stochastic image composition.
67. Student and Answer Key use the same line master so line clarity/topology cannot drift between the pair.
68. Pair QA confirms `PAIR_TOPOLOGY_IDENTITY`, `PAIR_TEXT_IDENTITY`, and `PAIR_MAPPING_IDENTITY`.
69. Same-page comparison is allowed only when explicitly requested as teacher/QA proof output and must not be labeled as the student worksheet.
70. `ANSWER_KEY = NO` must suppress the answer-key page without weakening mapping QA for the Student worksheet.

## 40–50 item single-page stress gates

When the user requests 40–50 questions/words on one Student A4 Portrait page:

71. The Student worksheet remains one A4 Portrait page only if all readability/colorability/print gates pass.
72. Decoration is reduced before text size, stroke clarity, safe margins, or colorable-cell size are compromised.
73. Text remains readable for the target grade at normal print scale.
74. Line weight remains crisp and photocopy-safe.
75. No region becomes too small or narrow for practical coloring.
76. No safe-margin violation is introduced to force the content onto one page.
77. Question/word numbering is complete, unique, and sequential for the requested count.
78. Preplanned color usage remains valid at 40–50 items; no late-generated answer may fall outside the legend.
79. If the 40–50 item page cannot pass QA, the system must report the single-page constraint failure and offer pagination rather than falsely claiming production readiness.
80. The Answer Key remains a separate A4 Portrait page when requested and uses the same geometry/text/mapping master.

## Natural Harmony gates
When `COMPOSITION_SYSTEM = NATURAL_HARMONY` or AUTO resolves to Natural Harmony:
81. Focal hierarchy is visually clear.
82. `COMPOSITION_BALANCE` and `SYMMETRY_MODE` suit the theme.
83. Golden-section guidance does not distort content, legend, margins or question safe areas.
84. Fibonacci rhythm is used only where useful and not forced everywhere.
85. Phyllotaxis/golden-angle-inspired detail does not create cells below minimum colorable size.
86. Natural Harmony does not replace primary-shape construction grammar.
87. `QUESTION_FLOW = FOLLOW_VISUAL_RHYTHM` preserves exact content/mapping and maintains or improves readability.
88. `QUESTION_DISTRIBUTION_BALANCE = REQUIRED` passes.
89. Natural scale hierarchy shows focal / secondary / supporting levels coherently.
90. No exact golden-ratio/Fibonacci/golden-angle claim without calculated evidence.
91. Natural Harmony does not materially reduce cleanliness/readability versus `REFERENCE_BEAUTIFUL`.
92. Natural Harmony does not materially reduce visual impact versus `REFERENCE_WOW`.

## V3 promotion gate
A candidate may be promoted to `REFERENCE_NATURAL_HARMONY_V3` only when all applicable critical gates PASS and final production geometry is deterministic/vector-first.

## Cross-theme validation
Before treating the Natural Harmony engine as robust, test at least one non-flower theme such as solar system, underwater world, rainforest, or seaside/lighthouse. PASS only if the engine adapts composition to the theme instead of mechanically reproducing flower symmetry.

## Critical FAIL
FAIL production immediately if:
- active answer/code set is unresolved when generated questions are created
- any generated question answer/code is outside the active legend
- any question region lacks a valid color mapping
- color usage counts do not reconcile to question count
- exact-division constraints are violated
- image model invents or changes academic questions after mapping freeze
- final raster linework is generative-only
- exact content/mapping is altered for aesthetics
- shared borders double/break
- Thai glyphs are missing
- natural pattern creates uncolorable micro-detail
- Student worksheet is solution-filled without explicit user request
- Answer Key has even one region filled with the wrong color
- Student and Answer Key topologies differ
- Answer Key independently reinterprets answer/color mapping
- Student and Answer Key appear together on the same student-facing page by default
- Student or Answer Key is not A4 Portrait without explicit user override
- 40–50 items are forced onto one page by sacrificing readability/colorability/print safety
- a raster-only mockup is labeled production-final/Golden Reference
