# Geometric Color-by-Code — Line Quality Remediation Report

Date: 2026-08-27
Status: Closed for v1.3 line-quality hardening

## Trigger

Real visual output showed that the geometric structure was improved but many internal mosaic borders looked fragmented, rough, doubled, or sketch-like. Dense micro-triangle intersections also created visual noise and reduced print quality.

## Root-cause analysis

The issue was not only image resolution. Main causes:
1. excessive micro-tile density
2. too many short segments and high-degree junctions
3. generative raster line rendering behaving like sketch/rough line art
4. topology being left partly to image generation instead of deterministic geometry
5. accidental main-art tint leakage in a monochrome worksheet

## Remediation decisions

### A. Crisp-line policy
Added `policies/LINE_RENDERING_POLICY.md` with:
- `LINE_RENDER_STYLE = CLEAN_VECTOR_LIKE`
- `STROKE_WIDTH = UNIFORM_MEDIUM`
- no sketch/rough/fuzzy/double/broken lines
- minimum practical tile/segment size
- controlled junction complexity
- `CRISP_LINES > MICRO_TILE_DENSITY`
- pure monochrome main-art rule

### B. Geometry policy hardening
`policies/GEOMETRY_LAYOUT_POLICY.md` v1.3.0 now:
- reduces micro density before preserving unnecessary detail
- prohibits hairline micro-segments
- discourages starburst junctions
- requires print-readable tile size
- adds `PRINT_LINE_CLARITY_QA = CRITICAL`

### C. Render architecture change
Added `policies/RENDER_PIPELINE_POLICY.md`.

Production preference:

```text
BEST   = deterministic/vector final geometry + deterministic text
GOOD   = AI-assisted composition + deterministic vector finalization
FALLBACK = strict image prompt + iterative visual QA
```

The image model is no longer treated as the preferred source of final printable boundaries when a deterministic renderer is available.

### D. Iterative fallback
For image-prompt-only rendering:
1. render
2. audit line clarity
3. if FAIL, reduce micro-tile density by about 20–35%
4. simplify contours and junctions
5. regenerate
6. stop after bounded rounds and escalate to vector/hybrid when available

## Internal proof tests

### Test 1 — deterministic SVG/vector-style line graph
Result:
- crisp continuous tile borders: PASS
- uniform line weight: PASS
- no fuzzy/sketch line: PASS
- no accidental color in main art: PASS
- Thai glyph fallback in first SVG renderer: FAIL

The font failure was correctly treated as a separate Critical QA issue rather than accepting the artifact.

### Test 2 — deterministic Thai font rendering
A Thai-capable font with mixed Thai/Latin/digit support was tested in the environment.

Result:
- Thai text: PASS
- Latin digits/punctuation in same line: PASS
- vowel/tone rendering: PASS at visual inspection

This led to `THAI_FONT_RENDER_QA = CRITICAL` in the render policy.

## New regression coverage

Added tests for:
- sketch-like fragmented lines
- excessive micro-density
- hairline segment misuse
- starburst junction noise
- main-art tint leakage
- wrong detail-vs-crispness tradeoff

## Closure criteria

Line-quality hardening is considered complete when the pipeline enforces:

```text
PASS — clean vector-like line style
PASS — uniform medium internal borders
PASS — no broken/double/fuzzy/sketch strokes
PASS — controlled micro density
PASS — no unusable sliver cells
PASS — simple readable junctions
PASS — pure monochrome main activity
PASS — deterministic/vector finalization preferred when available
PASS — Thai font/glyph validation for deterministic rendering
```

## Conclusion

The root cause cannot be solved reliably by adding adjectives to an image prompt alone. Production quality requires controlling geometry complexity and, when available, moving final worksheet boundaries/text to a deterministic/vector renderer. The Gem documentation and QA now encode this architecture.
