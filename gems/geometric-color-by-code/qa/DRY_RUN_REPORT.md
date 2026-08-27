# Geometric Color-by-Code — Dry Run Report

Date: 2026-08-27
Reference scenario: ป.3 คณิตศาสตร์ การบวกเลข 1 หลัก, 30 ข้อ, 6 สี, ธีมสวนดอกไม้, PRIMARY_SHAPE=TRIANGLE, MOSAIC

## Round 1 — Baseline interpretation

Finding: initial interpretation risked using triangles merely as decorative separators while the garden illustration stayed freeform.

Action:
- defined `PRIMARY_SHAPE` as construction grammar
- added `SHAPE_DOMINANCE = HIGH`
- prohibited freeform-scene-first + shape-overlay behavior

Result: PASS

## Round 2 — Mosaic beauty vs question count

Finding: forcing exactly 30 triangles for 30 questions produced a coarse image and weak mosaic effect; forcing one question into every tiny tile would make text unreadable.

Action:
- separated `MICRO_TILE_COUNT` from `QUESTION_REGION_COUNT`
- defaulted to `GROUPED_TILES`
- allowed 90–180+ micro tiles for 30 question regions when appropriate

Result: PASS

## Round 3 — Theme recognizability

Finding: a pure abstract triangular tessellation could satisfy geometry but fail the requested garden theme.

Action:
- added `THEME_SILHOUETTE_MODE = TILE_GROUPING`
- required recognizable flowers/leaves/butterflies/path structures to emerge from triangle clusters
- kept freeform curves minimal

Result: PASS

## Round 4 — Academic and mapping integrity

Finding: visual generation must not be responsible for arithmetic correctness or color mapping.

Action:
- locked verified question/answer set before layout
- added normalized answer codes
- enforced one normalized code → one color
- legend and answer key share the same mapping source

Result: PASS

## Round 5 — Thai/text reliability

Finding: image models can alter Thai instructions, arithmetic expressions, or count of regions.

Action:
- introduced `VERIFIED_CONTENT_BLUEPRINT`
- final prompt must preserve verified text/numbers exactly
- deterministic text placement recommended whenever supported

Result: PASS with implementation caution

## Round 6 — A4 readability

Finding: 30 questions plus legend plus decorative garden detail can become crowded on A4 Portrait.

Action:
- reduction order: decorations → tile grouping → legend placement → visual complexity → pagination
- readability must beat single-page density

Result: PASS

## Round 7 — Shape-specific geometry truthfulness

Finding: not every requested shape creates gap-free tessellation in the same way; circles are a common example.

Action:
- distinguished exact tessellation, approximate tessellation, and repeated cell packing
- prohibited unsupported claims that every shape is an exact tessellation

Result: PASS

## Round 8 — Revision behavior

Finding: changing geometry/theme should not unexpectedly regenerate verified questions.

Action:
- layer-specific revision rule
- geometry change regenerates geometry/layout only
- theme change regenerates silhouette/layout only
- content regenerates only when content parameters change or user requests it

Result: PASS

## Round 9 — Multi-subject audit

Finding: numeric mapping works naturally for math, but other subjects need normalized categorical codes; open-ended content is not suitable directly.

Action:
- added WORD, CATEGORY, CHOICE, TRUE_FALSE, MATCH_CODE and SHORT_TEXT response modes
- added subject/topic adapter
- open-ended topics must be transformed into concise objectively checkable activities first

Result: PASS

## Final audit

Reference scenario resolved as:

```text
GRADE_LEVEL = ป.3
SUBJECT = คณิตศาสตร์
TOPIC = การบวกเลข 1 หลัก
QUESTION_COUNT = 30
COLOR_COUNT = 6
PRIMARY_SHAPE = TRIANGLE
TILING_MODE = MOSAIC
SHAPE_DOMINANCE = HIGH
QUESTION_REGION_COUNT = 30
QUESTION_REGION_MODE = GROUPED_TILES
MICRO_TILE_COUNT = AUTO (>30)
THEME = สวนดอกไม้
THEME_SILHOUETTE_MODE = TILE_GROUPING
THEME_RECOGNIZABILITY = REQUIRED
PAGE_SIZE = A4
ORIENTATION = PORTRAIT
MAIN_ART_COLOR_MODE = MONOCHROME
LEGEND_COLOR_PREVIEW = YES
```

Final gates:

```text
PASS — content model
PASS — answer validation model
PASS — mapping model
PASS — geometric-grammar model
PASS — theme construction model
PASS — readability policy
PASS — print policy
PASS — multi-subject extensibility
PASS — revision behavior
PASS — user guide/examples/QA coverage
```

## Conclusion

Stopped after 9 dry-run rounds because the critical failure modes identified during testing were converted into canonical rules and regression tests. Additional rounds were not needed at this stage.
