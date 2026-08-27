# Geometric Color-by-Code — Page Format Policy

Version: 1.0.0
Status: Gem-specific policy

## Purpose

Define page-size, orientation, safe-area, density and pagination behavior for printable geometric Color-by-Code worksheets.

## Supported page sizes

At minimum:
- A3
- A4
- A5
- Letter
- Legal
- Custom

Default:

```text
PAGE_SIZE = A4
ORIENTATION = PORTRAIT
```

## Layout recalculation rule

When page size or orientation changes, recompute the geometric construction and question-region layout. Never stretch an existing page proportionally as a substitute for layout planning.

## Print-safe behavior

Default target:
- keep essential content inside a conservative print-safe area
- use approximately 10–12 mm safe margin where practical
- keep title, instructions, name fields, legend and main mosaic separated
- no academic text or region labels may touch trim/page edges

## Density priority

```text
READABILITY > QUESTION COUNT PER PAGE > DECORATION DENSITY
```

If the page becomes crowded:
1. reduce decorative details
2. simplify micro-tile density while preserving shape grammar
3. enlarge or regroup question regions
4. move legend if necessary
5. paginate
6. never solve crowding by making critical text unreadably small

## Question regions vs micro tiles

`MICRO_TILE_COUNT` may be much higher than `QUESTION_REGION_COUNT`.

Example:

```text
QUESTION_COUNT = 30
QUESTION_REGION_COUNT = 30
MICRO_TILE_COUNT = 120
```

Four micro triangles may contribute to one readable question region while the overall picture remains strongly triangular.

## Pagination

Use auto-pagination when the requested combination of:
- question count
- response length
- color legend size
- page size
- geometry density

cannot fit readably on one page.

Pagination must preserve:
- total question count
- unique question IDs
- mapping integrity
- consistent color legend semantics
- shape grammar and theme coherence

Do not silently drop questions to fit one page.

## Orientation resolver

Prefer Portrait when:
- user does not specify
- composition is vertically balanced
- legend fits beneath the mosaic

Prefer Landscape when:
- user explicitly requests it
- theme silhouette is strongly horizontal
- requested mosaic geometry benefits materially from wider composition

Explicit user orientation overrides AUTO unless it makes output unusable; if unusable, report the constraint rather than silently changing it.

## Main activity area

The geometric mosaic should normally be the dominant visual area of the worksheet. Administrative fields and decorations must not consume excessive space.

## Print QA

PASS only when:
- requested page size/orientation resolved correctly
- all required questions are represented
- legend is readable
- numbers/words inside regions are readable at print size
- no overlaps or clipped content
- main line art remains usable in grayscale/photocopy output
- shape grammar remains visually recognizable after pagination/layout adaptation
