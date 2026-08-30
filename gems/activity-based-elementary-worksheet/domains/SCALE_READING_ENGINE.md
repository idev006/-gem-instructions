# SCALE_READING_ENGINE — Deterministic Dial-Scale Worksheet Rules

Version: 1.1.1
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`
Applies to: `DOMAIN=MEASUREMENT_WEIGHT`, `QUESTION_TYPE=DIAL_SCALE_READING`
Registry authority: `domains/DOMAIN_REGISTRY.md`

## 1. Learning goal

The learner must read weight from a clear graduated dial:

`identify kilogram labels → count minor divisions → follow needle endpoint → express kg + ขีด`

Thai Grade 3 defaults:

- `DIAL_MAX_KG = 5`
- `MAJOR_DIVISION_KG = 1`
- `MINOR_DIVISION_KG = 0.1`
- `MINOR_DIVISIONS_PER_KG = 10`
- `1 ขีด = 0.1 กิโลกรัม = 100 กรัม`
- answer: `........ กิโลกรัม ........ ขีด`

The instructional dial is academic data and has priority over theme art.

## 2. Mandatory geometry

### True circle
- dial face = perfect 1:1 circle
- front-facing orthographic view
- reserved square box
- no perspective, tilt, ellipse, stretch, squeeze, skew, or crop

### Center pivot
- needle root = exact geometric center
- visible central hub/dot
- no floating/off-center pointer
- exactly one instructional needle

Recommended needle length: 70–82% of radius, ending at the tick ring without covering labels.

Any off-center needle or distorted circle is a critical blocker.

## 3. Canonical 5 kg teaching dial

Do **not** use a 360° value sweep. The default teaching dial uses a **300° active sweep** and a **60° inactive gap** so 0 and 5 have distinct endpoints.

Angle convention: `0° = top`, increasing clockwise.

Locked label mapping:

- `0 kg = 240°`
- `1 kg = 300°`
- `2 kg = 0°`
- `3 kg = 60°`
- `4 kg = 120°`
- `5 kg = 180°`

Therefore:

- 1 kg interval = 60°
- 0.1 kg interval = 6°
- active sweep 0→5 = 300°
- inactive gap 5→0 = 60° with no value ticks

### Target mapping

For `0 <= w <= 5`:

`tick_index = round(w / 0.1)`

`angle = (240° + tick_index * 6°) mod 360°`

Require exact representability:

`abs(w - tick_index*0.1) < tolerance`

Examples:

- 0.5 kg → tick 5 → 270°
- 1.0 kg → tick 10 → 300°
- 2.4 kg → tick 24 → 24°
- 5.0 kg → tick 50 → 180°

## 4. Tick construction

- 50 equal minor intervals
- 51 tick positions including both endpoints 0 and 5
- exactly 10 equal intervals between adjacent whole-kilogram labels
- major kilogram ticks longer/thicker
- minor ticks uniform and clearly separated
- no value ticks in the inactive 60° gap
- labels `0,1,2,3,4,5` aligned with major ticks

Do not improvise tick counts.

## 5. No clock confusion

This is not a clock. Never add 12/3/6/9 clock labels, hour/minute hands, or 60-minute semantics. Use only kilogram labels 0–5 and weight units.

## 6. Target instruction redundancy

For each item compile semantic target value, global tick index, kg component + minor-tick component, exact target angle, and relational wording.

Example render-only metadata:

`TARGET 2.4 kg; tick_index=24; 2 kg + 4 minor ticks; target_angle=24° clockwise from top; needle starts at exact center and terminates exactly on fourth minor tick after 2.`

This metadata is render-only and must not appear as visible answer text.

## 7. Blueprint

### Internal verified object

```text
{
 id: 1,
 object: "กะหล่ำปลี",
 target_weight_kg: 2.4,
 tick_index: 24,
 target_angle_deg: 24,
 kg_component: 2,
 tick_component: 4,
 verified_answer: "2 กิโลกรัม 4 ขีด",
 validation: PASS
}
```

### Student render object

```text
{
 id: 1,
 object: "กะหล่ำปลี",
 dial_template_id: "TH_G3_5KG_0P1_V1",
 needle_target_relation: "RENDER_ONLY_NOT_VISIBLE: tick 24 / angle 24°",
 answer_render: "........ กิโลกรัม ........ ขีด"
}
```

## 8. Layout + one-page behavior

Preferred card anatomy:

`NUMBER | CONTEXT OBJECT | LARGE INSTRUCTIONAL DIAL | ANSWER`

For 10 questions on A4 portrait, first attempt 2 columns × 5 rows.

Preferred printed dial diameter: 32–42 mm. Absolute minimum for 0.1 kg reading: 30 mm.

Apply global `ONE_PAGE_PREFERRED` policy before pagination. Reduce decoration and use a more efficient layout before reducing dial size.

If minimum dial size cannot fit:

- `ONE_PAGE_LOCK=OFF` → paginate;
- `ONE_PAGE_LOCK=ON` → `ONE_PAGE_FEASIBILITY_QA=FAIL` and `LAYOUT_QA=FAIL`; do not create page 2 and do not shrink below 30 mm.

## 9. Decorative context scale

A small illustrated kitchen scale is optional context only. The child reads the large separate dial. A decorative dial must not contradict the instructional dial and should avoid detailed competing ticks.

## 10. Mandatory prompt block

```text
DIAL GEOMETRY — CRITICAL
- perfect front-facing circular dial in a square reserved zone
- exact center pivot with one needle and visible hub
- canonical 300° active sweep, not a 360° value sweep
- labels: 0@240°, 1@300°, 2@0°, 3@60°, 4@120°, 5@180°
- 10 equal minor intervals per kg; each 0.1 kg = 6°
- no scale ticks in the 60° inactive gap between 5 and 0
- identical template for every question; only needle angle changes
- endpoint lands exactly on target tick
- no clock labels/clock semantics
- no overlap, skew, ellipse, crop, or perspective
```

## 11. Hard negatives

Critical failures include off-center/floating needle, oval/distorted dial, wrong 0–5 order/positions, 360° overlapping endpoint scale, ticks in inactive gap, unequal spacing, wrong minor interval count, multiple needles, endpoint between ticks, changed template, clock-face substitution, unreadably small dial, or text/art covering the tick band.

## 12. QA gates

`DIAL_CIRCLE_QA`
`CENTER_PIVOT_QA`
`SINGLE_NEEDLE_QA`
`ACTIVE_SWEEP_QA`
`ENDPOINT_DISTINCT_QA`
`TICK_COUNT_QA`
`TICK_SPACING_QA`
`LABEL_POSITION_QA`
`NEEDLE_TARGET_QA`
`TEMPLATE_LOCK_QA`
`DIAL_SIZE_QA`
`DIAL_CLEARANCE_QA`
`SCALE_READING_PEDAGOGY_QA`
`ONE_PAGE_FEASIBILITY_QA`

Inspect every dial individually after render. One incorrect dial blocks release.

## 13. Preferred implementation

Best production path:

`AI THEME ART/LAYOUT → DETERMINISTIC SVG DIAL → THAI TEXT OVERLAY → COMPOSITE → VISUAL QA`

Generative image output alone is never treated as mathematically guaranteed.

## 14. Maturity note

The deterministic-overlay path has strong regression evidence, but the **overall domain remains `PRODUCTION_CANDIDATE`** until the promotion criteria in `qa/DOMAIN_RELEASE_MATRIX.md` are satisfied. Do not report this engine as overall hardened merely because its deterministic geometry rules are mature.
