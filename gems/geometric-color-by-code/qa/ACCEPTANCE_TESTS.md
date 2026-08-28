# Geometric Color-by-Code — Acceptance Tests

Version: 1.8.1

## Critical production gates

1. Default page = A4 Portrait when unspecified.
2. `QUESTION_REGION_COUNT = QUESTION_COUNT` by default.
3. Exact requested question count and color count are preserved.
4. `CONTENT_GENERATION_MODE = ANSWER_FIRST` by default for generated worksheets.
5. Active answer/code set is resolved before question generation.
6. Color usage distribution is frozen before question generation.
7. Every generated question is created from a preassigned target answer/code.
8. Every generated question has a verified correct answer equal to its target after normalization.
9. Every normalized answer/code maps to one color only.
10. Every verified answer/code belongs to the active legend domain.
11. No question may produce an answer/code outside the active legend.
12. Every question region has a resolvable `color_id` before render.
13. Sum of color-usage counts equals exact question count.
14. Legend and answer key use the same mapping source.
15. No orphan legend/question/answer/region.
16. For mathematics, arithmetic and all requested topic constraints are independently validated.
17. For exact division, every problem divides evenly and satisfies requested digit constraints.
18. Primary shape dominates the main activity area when requested/default HIGH.
19. Minimum colorable-cell, line, topology, Thai text and print-safe gates pass.
20. `PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED`.
21. Final printable boundaries come from deterministic geometry/vector paths.

## Deterministic visible-content gates

22. `ACADEMIC_TEXT_RENDER_MODE = DETERMINISTIC_OVERLAY` for production/test-conformance output.
23. `ACADEMIC_TEXT_RENDER_SOURCE = VERIFIED_CONTENT_BLUEPRINT`.
24. `QUESTION_NUMBER_RENDER_SOURCE = VERIFIED_CONTENT_BLUEPRINT`.
25. `LEGEND_RENDER_SOURCE = VERIFIED_MAPPING`.
26. Image model does not invent/rewrite final academic questions, question numbers, or legend values.
27. `POST_RENDER_CONTENT_PARITY = REQUIRED` is completed before PASS.
28. `rendered_question_count == QUESTION_COUNT`.
29. Rendered question IDs exactly equal expected question IDs.
30. Rendered question IDs are unique; no unexpected duplicate IDs.
31. Rendered question IDs are complete/sequential when the activity uses numbered questions.
32. For every question ID, rendered prompt text equals verified prompt text.
33. Rendered legend domain exactly equals the active legend domain.
34. Rendered legend color labels/swatches agree with `VERIFIED_MAPPING` and verified palette.
35. Out-of-legend answer count in the visible final output is zero.
36. An image-model-only full-page academic-text render may be used only as a concept preview and must not be labeled Gem-conformant/production-final.

## Student / Answer-Key gates

37. `STUDENT_WORKSHEET_REQUIRED = YES` by default.
38. Student activity regions contain no solution fill color.
39. `ANSWER_KEY = YES` produces a separate colored solution view by default.
40. Student and Answer Key use the same master geometry, region IDs, verified text and mapping.
41. Answer Key fill colors come only from `VERIFIED_COLOR_MAPPING`.
42. A single wrong answer-key region color is a Critical FAIL.
43. `ANSWER_KEY = NO` suppresses the answer-key page without weakening Student mapping/content QA.

## 40–50 item single-page stress gates

44. One Student A4 Portrait page is allowed only when all readability/colorability/print gates pass.
45. Decoration/micro-detail is reduced before text, stroke, margins or colorable-cell usability is compromised.
46. Academic text placement remains deterministic even at high density.
47. Question numbering remains complete, unique and readable.
48. Rendered question count still equals the requested count.
49. Preplanned color usage remains valid; no late answer falls outside the legend.
50. If one-page QA cannot pass, system must report the constraint and paginate rather than falsely claim readiness.

## Natural Harmony gates

51. Natural Harmony does not replace primary-shape construction grammar.
52. Focal hierarchy/balance/symmetry suit the theme.
53. Golden/Fibonacci/phyllotaxis guidance does not damage readability, margins or colorability.
54. Natural Harmony never changes verified question IDs, count, answers, colors or text.
55. No exact mathematical natural-proportion claim without calculated evidence.

## Critical FAIL

FAIL immediately if:
- any generated or rendered answer/code is outside active legend
- any question region lacks a valid color mapping
- color usage counts do not reconcile to question count
- exact-division constraints are violated
- rendered question count differs from `QUESTION_COUNT`
- a question number is missing/duplicated unexpectedly
- visible question text differs from verified blueprint
- visible legend differs from verified mapping
- image model is the final academic-text source in an output claimed production/test-conformant
- post-render parity is skipped but output is claimed PASS
- final linework/geometry or print usability fails required gates
