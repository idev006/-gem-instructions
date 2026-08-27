# Geometric Color-by-Code — Audit Remediation Plan

Date: 2026-08-27
Status: Implemented

## Trigger

Audit of a generated Thai Color-by-Code worksheet exposed two production-level weaknesses:

1. legend/category coverage could be incomplete while still rendering all legend entries;
2. a requested geometric primary shape could appear mainly as surface pattern while large freeform silhouettes remained dominant.

## Audit findings

### A. Category/legend integrity

Observed pattern:

```text
legend categories = 5
question distribution = 4, 4, 2, 0, 0
```

This is invalid when all five categories are shown to students because two legend entries can never be used.

If the worksheet also says a category is “เน้น” (focused), tying another category for the highest count does not express a meaningful focus.

### B. Shape grammar fidelity

Observed pattern:

```text
freeform elephant/bird/house silhouette
→ geometric rhombus/diamond lines placed inside or around it
```

This does not satisfy `SHAPE_DOMINANCE = HIGH`.

Required construction:

```text
primary-shape grid/cells
→ grouped tile clusters
→ body parts / object parts
→ complete recognizable silhouette
```

## Remediation decisions

### 1. No orphan legend entries

Default policy:

```text
LEGEND_COVERAGE_POLICY = NO_ORPHAN_LEGEND_ENTRY
```

Every student-facing legend category/color must have at least one mapped question/region unless the user explicitly requests an informational inactive entry.

### 2. Focus-category planning

Added explicit focus semantics:

```text
FOCUS_CATEGORY
CATEGORY_FOCUS_MODE
FOCUS_SHARE_TARGET
CATEGORY_DISTRIBUTION
```

For `EMPHASIZED` with no custom ratio, target approximately 40–60% of questions for the focus category while retaining coverage for displayed secondary categories.

### 3. Atomic-response preference

Added:

```text
PREFER_ATOMIC_RESPONSE = YES
```

For vocabulary/classification activities, prefer a clear single word over a phrase when both test the same objective.

### 4. Stronger shape dominance

For `SHAPE_DOMINANCE = HIGH`:
- target approximately >=80% structural tiling rhythm from the primary shape;
- large freeform silhouettes are forbidden;
- target freeform structural area approximately <=15–20%;
- freeform details are limited to small recognizability/readability corrections.

### 5. Verified blueprint expansion

Category worksheets now freeze before rendering:
- category set;
- usage counts;
- focus category/share;
- legend entries;
- legend usage counts;
- legend coverage result;
- verified question/category mapping.

## Files updated

- `GEM_INSTRUCTIONS_PRODUCTION.md` → v1.1.0
- `OUTPUT_CONTRACT.md` → v1.1.0
- `policies/COLOR_MAPPING_POLICY.md` → v1.1.0
- `policies/GEOMETRY_LAYOUT_POLICY.md` → v1.1.0
- `qa/ACCEPTANCE_TESTS.md` → v1.1.0
- `qa/REGRESSION_TESTS.md` → v1.1.0

## Production gates added

```text
PASS — no orphan legend entry
PASS — focus-category distribution
PASS — atomic item preference when appropriate
PASS — primary-shape dominance
PASS — freeform-area limit
PASS — category plan frozen before rendering
```

## Closure

The audited failure modes are now explicit canonical rules and regression tests. Future generated worksheets that repeat the same failure should be rejected before release.
