# Geometric Color-by-Code — Regression Tests

Version: 1.8.0

## Core content and geometry regressions
R1 FAIL if requested shape is only overlaid on a conventional illustration.
R2 FAIL if question count is forced to equal micro-tile count and creates tiny cells.
R3 FAIL if major theme elements are freeform under HIGH dominance.
R4 FAIL if one normalized answer maps to multiple colors.
R5 FAIL if visual generation may rewrite verified academic text or mappings.
R6 FAIL if text/strokes are reduced below practical print quality to keep one page.
R7 FAIL if approximate packing is called exact tessellation.
R8 FAIL if changing geometry unexpectedly changes verified content.
R9 FAIL if long open-ended responses are forced into coloring regions.
R10 FAIL if default monochrome student main art receives unintended fills/tints.
R11 FAIL if a legend color/category cannot be produced by any question.
R12 FAIL if a requested focus category is not actually emphasized.
R13 FAIL if geometric pattern is merely decorative skin on freeform silhouettes.
R14 FAIL if primary-shape coverage is materially below the resolved HIGH target.
R15 FAIL when unnecessary multi-word content creates classification ambiguity.
R16 FAIL if distribution is discovered only after visual generation.
R17 FAIL when large freeform containers abandon primary-shape grammar.
R18 FAIL when page areas use unrelated tile-size systems.
R19 FAIL when shared edges appear as parallel/doubled strokes.
R20 FAIL when intended coloring cells are visually open.
R21 FAIL when a child cannot practically color a sliver/needle cell.
R22 FAIL when rounded/scalloped motifs dominate a triangle mosaic.
R23 FAIL when answer/color distribution is left to the image model.
R24 FAIL when question text collides with tile borders.
R25 FAIL when hairline rendering breaks during rasterization/printing.
R26 FAIL when stroke hierarchy is flat and harms readability.
R27 FAIL when excessive junctions create starburst noise.
R28 FAIL when short segments add visual noise without structural value.
R29 FAIL if density is not reduced after line-quality failure.
R30 FAIL when Thai font fallback causes missing/misaligned glyphs.
R31 FAIL if a prior Golden Reference composition is copied instead of only inheriting quality gates.
R32 FAIL when fuzzy/broken generative raster is accepted as production-final.

## Answer-first generation regressions
R33 FAIL if a normal generated worksheet creates questions before resolving the active answer/code set.
R34 FAIL if any verified question answer/code is absent from the active legend.
R35 FAIL if any region reaches render without a resolvable color ID.
R36 FAIL if the system generates arbitrary math problems and only afterward tries to fit their answers into the legend.
R37 FAIL if `COLOR_USAGE_PLAN` is not frozen before generated questions are created.
R38 FAIL if the sum of usage counts per color does not equal `QUESTION_COUNT`.
R39 FAIL if `target_answer_or_code != normalized_answer_code` after validation.
R40 FAIL if a target numeric answer is silently replaced by an out-of-legend result because generation constraints are difficult.
R41 FAIL if exact-division content contains a remainder or violates requested dividend/divisor digit constraints.
R42 FAIL if image generation invents, rewrites, or recalculates academic questions after mapping freeze.
R43 FAIL if changing color count only recolors the legend without rebuilding active code/distribution planning.
R44 FAIL if fixed user-supplied questions are allowed to render before proving 100% legend coverage.

## Render-pipeline regressions
R45 FAIL if prompt wording is assumed to guarantee crisp final boundaries.
R46 FAIL if generative raster is called vector-quality without deterministic paths.
R47 FAIL if a shared edge is rendered twice.
R48 FAIL if raster-only output is promoted to production Golden Reference.
R49 FAIL if production PNG/JPG is generated independently of the vector master.
R50 FAIL if final Thai text is delegated to the image model.
R51 FAIL if renderer fallback is hidden from the user.
R52 FAIL if broken-line output is repeatedly regenerated without root-cause change.

## Natural Harmony regressions
R53 FAIL if layout sacrifices readability/margins/legend to force 1.618.
R54 FAIL if approximate composition is described as exact golden ratio/Fibonacci/golden-angle without validation.
R55 FAIL if phyllotaxis creates cells below minimum colorable size.
R56 FAIL if Fibonacci/petal counts alter verified question count or mapping.
R57 FAIL if natural rhythm replaces primary-shape construction grammar.
R58 FAIL if mirror symmetry is forced when dynamic natural balance would suit the theme better.
R59 FAIL if `NATURAL_SCALE_HIERARCHY = YES` has no clear focal / secondary / supporting levels.
R60 FAIL if V3 gains natural styling but materially loses WOW impact or BEAUTIFUL cleanliness/readability.
R61 FAIL if question regions are placed in leftover spaces instead of following the resolved question-flow plan.
R62 FAIL if `QUESTION_FLOW = FOLLOW_VISUAL_RHYTHM` changes question IDs, answers, codes, colors or count.
R63 FAIL if natural symmetry is mechanically reused across unrelated themes.
R64 FAIL if a solar-system/underwater/rainforest test reproduces a flower-like radial composition without thematic justification.
R65 FAIL if natural-detail strength is increased while colorability or line clarity decreases.
R66 FAIL if the system claims Natural Harmony is mathematically exact when it is only inspired/approximate.

## Twin Output / Answer-Key regressions
R67 FAIL if the Student worksheet is solution-filled by default instead of remaining monochrome/unfilled.
R68 FAIL if Student and Answer Key are generated from separate geometry/composition masters.
R69 FAIL if a region exists in one output but not the other, or region boundaries differ.
R70 FAIL if question IDs/text differ between Student and Answer Key except approved teacher-only labels.
R71 FAIL if Answer Key colors are chosen by image-model interpretation instead of verified mapping.
R72 FAIL if even one Answer-Key region fill does not equal `verified_mapping[question_id]`.
R73 FAIL if Student and Answer Key use different legends or color IDs.
R74 FAIL if line topology/stroke geometry drifts between Student and Answer Key.
R75 FAIL if changing only colors causes a new Student geometry to be generated unnecessarily.
R76 FAIL if Answer Key is regenerated stochastically to “look prettier” and mapping integrity is no longer auditable.
R77 FAIL if a pair is called production-ready without explicit pair-identity QA.
R78 FAIL if `ANSWER_KEY = NO` accidentally disables Student mapping/legend completeness validation.

## PASS principle
A regression passes only when correctness, complete active-legend coverage, answer-first generation, mapping, Student/Answer pair identity when applicable, readability, colorability, deterministic geometry, primary-shape grammar and print usability remain intact while the requested visual/composition behavior is achieved.
