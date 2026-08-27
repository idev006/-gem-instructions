# Geometric Color-by-Code — Regression Tests

## R1 — Shape becomes decoration only

FAIL if triangle is requested but worksheet is a normal cartoon scene with a few triangle overlays.
PASS only when triangle tiling constructs most of the main image.

## R2 — Question count equals micro-tile count by force

FAIL if 30 questions force exactly 30 tiny tiles and reduce aesthetic quality/readability.
PASS when micro tiles may exceed 30 and are grouped into 30 question regions.

## R3 — Theme destroys geometric grammar

FAIL if freeform flowers/butterflies dominate the garden scene.
PASS when garden elements are recognizable from geometric tile clusters.

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
