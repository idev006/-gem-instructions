# Geometric Color-by-Code — Regression Tests

Version: 1.6.0

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
R10 FAIL if default monochrome main art receives unintended fills/tints.
R11 FAIL if a legend color/category cannot be produced by any question.
R12 FAIL if a requested focus category is not actually emphasized.
R13 FAIL if geometric pattern is merely decorative skin on freeform silhouettes.
R14 FAIL if primary-shape coverage is materially below the resolved HIGH target.
R15 FAIL when unnecessary multi-word content creates classification ambiguity.
R16 FAIL if distribution is discovered only after visual generation.
R17 FAIL when large circle/leaf/cloud containers abandon primary-shape grammar.
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
R28 FAIL when very short segments add visual noise without structural value.
R29 FAIL if density is not reduced after line-quality failure.
R30 FAIL when Thai font fallback causes missing/misaligned glyphs.
R31 FAIL if a prior Golden Reference composition is copied instead of only inheriting quality gates.
R32 FAIL when fuzzy/broken generative raster is accepted as production-final.

## Render-pipeline regressions

### R33 — Prompt-only line-quality optimism
FAIL if the system assumes a stronger prompt can guarantee crisp geometric boundaries from an image model.
PASS when prompt-only output is treated as preview and final print boundaries are reconstructed deterministically.

### R34 — Image-model raster used as vector substitute
FAIL if generative raster is called vector-like/vector-quality merely because it visually resembles vector art.
PASS only when final geometry comes from actual deterministic paths/edge graph.

### R35 — Shared edge rendered twice
FAIL if two adjacent regions independently draw the same border and produce doubled/uneven line weight.
PASS when a shared-edge graph stores/renders one logical edge once.

### R36 — Raster-only Golden Reference
FAIL if an image-model-only raster is promoted to Golden Reference for production print.
PASS only when the Golden Reference has deterministic/vector final geometry or an equivalent renderer with auditable topology.

### R37 — Production PNG not derived from master
FAIL if production PNG/JPG is generated independently from the vector/deterministic master.
PASS when raster preview/export is rendered from the same master geometry and text source.

### R38 — Thai text delegated to image model
FAIL if final Thai title, instruction, question, color label, or answer key text is generated/re-written inside image generation.
PASS when final visible academic text is placed deterministically and passes Thai font/glyph QA.

### R39 — Renderer fallback hidden from user
FAIL if vector/deterministic rendering is unavailable but the system silently labels image-only output production-ready.
PASS when output is explicitly marked preview/mockup and the limitation is surfaced.

### R40 — Repeated image regeneration without root-cause change
FAIL if broken-line output is regenerated repeatedly with nearly identical image prompts and accepted after visual luck.
PASS when the pipeline switches renderer or reconstructs deterministic geometry instead of relying on stochastic improvement.

## Natural proportion regressions

### R41 — Forced golden ratio
FAIL if layout sacrifices readable question regions, margins, or legend space to force a 1.618 ratio.
PASS when golden-section guidance is subordinate to usability.

### R42 — Unsupported exactness claim
FAIL if an approximate visual composition is described as exact golden ratio, exact Fibonacci spiral, or exact golden-angle construction without calculation/validation.
PASS when language says inspired/guided unless exactness is actually verified.

### R43 — Phyllotaxis creates uncolorable micro-detail
FAIL if seed/petal simulation creates tiny cells below minimum colorable size.
PASS when seed/spiral structure is grouped into larger wedges/bands/clusters.

### R44 — Fibonacci count overrides content
FAIL if petal/rhythm counts alter verified question count or mapping.
PASS when natural pattern controls supporting visual grouping only.

### R45 — Natural proportion replaces primary-shape grammar
FAIL if spiral/radial motifs become freeform curves that obscure the requested geometric shape.
PASS when natural rhythm controls placement/scale while the primary shape still constructs objects.

### R46 — Mirror symmetry mistaken for natural harmony
FAIL if all elements are mirrored rigidly and the composition loses organic balance when `NATURAL_PROPORTION` is requested.
PASS when dynamic balance may include controlled asymmetry while retaining focal hierarchy.

### R47 — Natural hierarchy has no focal point
FAIL if all flowers/objects use equal size and equal visual weight under `SCALE_PROGRESSION = NATURAL_HIERARCHY`.
PASS when one focal element, secondary elements, and supporting motifs are clearly resolved.

### R48 — V3 loses approved strengths
FAIL if a V3 candidate gains natural-pattern styling but materially loses the visual impact of `REFERENCE_WOW` or the cleanliness/readability of `REFERENCE_BEAUTIFUL`.
PASS when V3 demonstrably combines both baselines plus natural rhythm.
