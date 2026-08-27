# Geometric Color-by-Code — Regression Tests

Version: 1.4.0

## R1 — Shape becomes decoration only
FAIL if requested shape is only overlaid on a conventional illustration.
PASS when tile grammar constructs most of the themed image.

## R2 — Question count forces bad micro density
FAIL if question count is used as the tile count and creates tiny cells.
PASS when micro tiles and question regions are independent.

## R3 — Freeform theme drift
FAIL if major flowers/clouds/leaves/wings/body shapes are freeform under HIGH dominance.
PASS when they are built primarily from shape clusters.

## R4 — Mapping conflict
FAIL if one normalized answer maps to multiple colors.

## R5 — Image model invents academic text
FAIL if visual generation may rewrite questions/answers/legend mappings.

## R6 — Over-dense single page
FAIL if text or strokes are reduced below practical print quality.
PASS when micro detail is reduced or pagination is used first.

## R7 — False tessellation claim
FAIL if approximate packing is described as exact tessellation.

## R8 — Revision drift
FAIL if changing geometry unexpectedly changes verified question content.

## R9 — Open-ended misuse
FAIL if long responses are forced into coloring regions.

## R10 — Main-art color leakage
FAIL if default monochrome student artwork receives unintended fills/tints.

## R11 — Orphan legend entry
FAIL if a legend color/category cannot be produced by any question.

## R12 — Focus not actually emphasized
FAIL if a requested focus category ties a secondary category without a valid reason.

## R13 — Freeform silhouette with geometric skin
FAIL if geometric pattern is only decorative texture on a freeform object.

## R14 — HIGH dominance with low coverage
FAIL if primary-shape structural rhythm is materially below the resolved target.

## R15 — Ambiguous phrase where atomic item suffices
FAIL when unnecessary multi-word content makes classification ambiguous.

## R16 — Distribution planned after render
FAIL if category/answer/color usage is discovered only after visual generation.

## R17 — Question regions abandon shape grammar
FAIL when large circle/leaf/cloud containers dominate a shape-based worksheet.

## R18 — Uncontrolled tile-scale split
FAIL when page areas use unrelated tile-size systems.

## R19 — Double lines
FAIL when shared edges appear as parallel strokes.

## R20 — Broken joins / open regions
FAIL when intended coloring cells are not visually closed.

## R21 — Tiny sliver cells
FAIL when a child cannot practically color a cell.

## R22 — Freeform nature elements in triangle mosaic
FAIL when rounded/scalloped motifs dominate instead of triangle clusters.

## R23 — Answer/color distribution left to image model
FAIL when balanced usage should have been deterministic.

## R24 — Border/text collision
FAIL when question text touches or crosses multiple borders.

## R25 — Hairline rendering
FAIL when internal lines are so thin that rasterization/printing makes them broken or inconsistent.

## R26 — Flat stroke hierarchy
FAIL when outer frame, silhouette and internal tiles all use visually identical heavy stroke and reduce readability.
PASS when `frame > silhouette > internal tile` is clearly perceived.

## R27 — Starburst junction noise
FAIL when many tiny edges converge at one point and create a dark burst or apparent broken-line artifact.
PASS after merge/stagger/simplification.

## R28 — Minimum segment violation
FAIL when numerous very short segments create visual noise without educational/structural benefit.

## R29 — Excessive micro-detail after line failure
FAIL if regeneration keeps the same dense geometry after line-quality failure.
PASS when density/junction count is intentionally reduced.

## R30 — Thai font fallback failure
FAIL when Thai glyphs, marks, baseline, or digits visibly mismatch due to unsupported fallback.

## R31 — Golden-reference imitation
FAIL if the system copies a prior Golden Reference composition even when a new theme/shape calls for a different layout.
PASS when only quality gates are inherited.

## R32 — Raster candidate mislabeled production-final
FAIL when fuzzy/broken generative lines are accepted despite vector/deterministic rendering being available or required.
