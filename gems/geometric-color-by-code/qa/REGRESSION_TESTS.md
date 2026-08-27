# Geometric Color-by-Code — Regression Tests

Version: 1.1.0

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

Audit-derived FAIL example:

```text
legend = แม่กง, แม่กน, แม่กม, แม่เกย, แม่เกอว
question distribution = 4, 4, 2, 0, 0
```

## R12 — Focus category is not actually emphasized

FAIL if worksheet says `เน้นแม่กง` but แม่กง ties with another category for highest count without explicit rationale.
PASS when resolved focus category has a clearly greater count than each secondary category, normally around 40–60% of questions unless otherwise requested.

## R13 — Freeform silhouette with geometric skin

FAIL if elephant, bird, house, flower, etc. is first drawn as a large conventional freeform silhouette and geometric pattern is merely inserted inside or around it.
PASS when head/body/wing/leg/roof/etc. are themselves constructed from grouped cells derived from the primary-shape grammar.

## R14 — HIGH dominance but large freeform areas remain

FAIL if `SHAPE_DOMINANCE = HIGH` while large curved/polygonal freeform regions dominate the main composition.
PASS when roughly >=80% of structural tiling rhythm derives from the primary shape and freeform structural area remains minor (target ~15–20% or less).

## R15 — Ambiguous phrase used where atomic word suffices

FAIL when a classification worksheet uses multi-word phrases that introduce unnecessary classification ambiguity even though a single word would test the same objective.
PASS when `PREFER_ATOMIC_RESPONSE = YES` selects clear single-word items where possible.

## R16 — Category plan created after rendering

FAIL if category counts are discovered only after image generation.
PASS when category set, focus share, usage counts, legend coverage, verified items, and mapping are frozen before visual prompt assembly.
