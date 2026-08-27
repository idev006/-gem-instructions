# Geometric Color-by-Code — Regression Tests

Version: 1.3.0

## R1 — Shape becomes decoration only
FAIL if triangle/rhombus is requested but worksheet is a normal cartoon scene with a few geometric overlays.
PASS only when requested-shape tiling constructs most of the main image.

## R2 — Question count equals micro-tile count by force
FAIL if 30 questions force exactly 30 tiny tiles and reduce aesthetic quality/readability.
PASS when micro tiles may exceed 30 and are grouped into 30 question regions.

## R3 — Theme destroys geometric grammar
FAIL if freeform flowers/butterflies/animals dominate the scene.
PASS when theme elements are recognizable from geometric tile clusters.

## R4 — Mapping conflict
FAIL if the same normalized answer maps to two colors.
PASS when mapping is deterministic and legend/answer key share one source.

## R5 — Image model invents academic text
FAIL if final prompt asks image model to create or rewrite questions/answers.
PASS when verified content is locked before visual prompt assembly.

## R6 — Over-dense single page
FAIL if text becomes tiny to fit high question counts.
PASS when decoration is reduced, grouping changes, then pagination is used.

## R7 — False tessellation claim
FAIL if circle packing is called exact tessellation while gaps remain.
PASS when exact/approximate/cell-pattern mode is identified correctly.

## R8 — Revision regenerates unrelated content
FAIL if changing triangle to hexagon changes the question set.
PASS when only geometry/layout layers regenerate unless user requests new content.

## R9 — Open-ended subject misuse
FAIL if long essay answers are inserted into mosaic tiles.
PASS when activity is adapted to factual short-response/category/choice/true-false form.

## R10 — Legend/main-art color leakage
FAIL if main student activity is pre-colored when default monochrome is active.
PASS when color is limited to legend previews unless explicitly requested otherwise.

## R11 — Orphan legend entry
FAIL when the legend shows a color/category that no question can produce.
PASS when every legend entry has usage count >= 1 unless the user explicitly requests an informational inactive entry.

## R12 — Focus category is not actually emphasized
FAIL if worksheet says `เน้นแม่กง` but แม่กง ties with another category for highest count without explicit rationale.
PASS when resolved focus category has a clearly greater count than each secondary category, normally around 40–60% of questions unless otherwise requested.

## R13 — Freeform silhouette with geometric skin
FAIL if elephant, bird, house, flower, etc. is first drawn as a large conventional freeform silhouette and geometric pattern is merely inserted inside or around it.
PASS when major components are themselves constructed from grouped cells derived from the primary-shape grammar.

## R14 — HIGH dominance but large freeform areas remain
FAIL if `SHAPE_DOMINANCE = HIGH` while large curved/polygonal freeform regions dominate the main composition.
PASS when roughly >=85% of structural tiling rhythm derives from the primary shape and freeform structural area remains minor.

## R15 — Ambiguous phrase used where atomic word suffices
FAIL when a classification worksheet uses multi-word phrases that introduce unnecessary classification ambiguity even though a single word would test the same objective.
PASS when `PREFER_ATOMIC_RESPONSE = YES` selects clear single-word items where possible.

## R16 — Category plan created after rendering
FAIL if category counts are discovered only after image generation.
PASS when category set, focus share, usage counts, legend coverage, verified items, and mapping are frozen before visual prompt assembly.

## R17 — Question regions abandon primary-shape grammar
FAIL when triangle mosaic uses large circular flower centers or freeform leaves as primary question containers.
PASS when question regions derive from grouped triangle cells or use only small label anchors when required for readability.

## R18 — Uncontrolled tile-scale split
FAIL when one half of the page uses very large sparse tiles and another half uses unrelated tiny dense tiles without coherent transition.
PASS when `TILE_SCALE_VARIATION = CONTROLLED` and the entire page reads as one mosaic system.

## R19 — Accidental double lines
FAIL when shared borders appear as parallel/doubled lines due to overlapping objects or contour corrections.
PASS when each shared border reads as one clean boundary.

## R20 — Broken joins / open regions
FAIL when cell borders do not meet cleanly and a coloring region appears open or ambiguous.
PASS when every intended region is visually closed and topology is unambiguous.

## R21 — Tiny sliver cells
FAIL when contour corrections create tiny narrow regions that are impractical for children to color.
PASS when sliver cells are merged/simplified while preserving mapping integrity.

## R22 — Freeform nature elements in triangle mosaic
FAIL when triangle garden uses conventional rounded flower petals, freeform leaf silhouettes, scalloped clouds, or rounded butterfly wings as dominant shapes.
PASS when these objects are constructed primarily from triangle clusters.

## R23 — Answer/color distribution left to image model
FAIL when 30 questions / 6 colors have no frozen usage-frequency plan before render.
PASS when an answer/color frequency plan exists first, targeting about 5 regions per color when content-valid.

## R24 — Border/text collision
FAIL when question text touches or crosses multiple tile borders in a way that reduces readability.
PASS when question placement preserves a clear text-safe area or uses a controlled label anchor.

## R25 — Sketch-like / fragmented line rendering
FAIL when tile borders look rough, fuzzy, broken, scratchy, pencil-like, or visibly fragmented at normal viewing scale.
PASS when line art is clean, smooth, vector-like, continuous, and single-pass.

## R26 — Excessive micro-density causes line failure
FAIL when additional micro triangles create noisy intersections, short fragments, or broken-looking strokes.
PASS when micro-tile density is reduced until every tile boundary remains clear and printable.

## R27 — Hairline segment misuse
FAIL when small tiles rely on very thin hairline edges that disappear or become inconsistent in print.
PASS when internal borders remain a stable medium stroke and tiny geometry is simplified instead.

## R28 — Starburst junction noise
FAIL when many edges converge at one point and create a dark, messy starburst that obscures cell boundaries.
PASS when junctions are simplified, usually to 2–3 meaningful edges, while preserving the mosaic silhouette.

## R29 — Main-art tint leakage
FAIL when monochrome main artwork contains beige, gray, pale yellow, colored shading, or accidental wash.
PASS when main activity is black line + white fill only, with actual color restricted to the legend when enabled.

## R30 — Wrong quality tradeoff
FAIL when detail is preserved at the cost of crisp lines.
PASS when the system follows:

```text
CRISP_LINES > MICRO_TILE_DENSITY
READABILITY > GEOMETRIC_DETAIL
PRINT_USABILITY > DECORATIVE_COMPLEXITY
```
