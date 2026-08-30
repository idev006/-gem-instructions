# SCALE_READING_ENGINE — Deterministic Dial-Scale Worksheet Rules

Version: 1.1.0
Status: PRODUCTION_HARDENED
Requires: `INSTRUMENT_READING_ENGINE.md`
Applies to: `DOMAIN=MEASUREMENT_WEIGHT`, `QUESTION_TYPE=DIAL_SCALE_READING`

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

The large instructional dial is academic data and has priority over theme art.

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

Recommended needle length: 70–82% of radius, ending at tick ring without covering label.

Any off-center needle or distorted circle is a critical blocker.

## 3. Canonical 5 kg teaching dial

### Critical correction: DO NOT use a 360° value sweep

A 0–5 kg scale needs distinct positions for both 0 and 5. Therefore the default teaching dial uses a **300° active sweep**, leaving a 60° inactive gap between endpoints.

Use angle convention: `0° = top`, increasing clockwise.

Default locked label mapping:

- `0 kg = 240°` (lower-left)
- `1 kg = 300°` (upper-left)
- `2 kg =   0°` (top)
- `3 kg =  60°` (upper-right)
- `4 kg = 120°` (lower-right)
- `5 kg = 180°` (bottom)

Thus:

- each 1 kg interval = 60°
- each 0.1 kg interval = 6°
- total active sweep from 0→5 clockwise = 300°
- inactive gap from 5→0 = 60° and contains NO value ticks

This mapping is locked across every question on the worksheet.

### Target mapping

For weight `w` where `0 <= w <= 5`:

`tick_index = round(w / 0.1)`

`angle = (240° + tick_index * 6°) mod 360°`

Examples:

- 0.5 kg → tick 5 → 270°
- 1.0 kg → tick 10 → 300°
- 2.4 kg → tick 24 → 24°
- 5.0 kg → tick 50 → 180°

Require exact representability:

`abs(w - tick_index*0.1) < tolerance`

## 4. Tick construction

For the active 300° scale:

- 50 equal minor intervals
- 51 tick positions including both endpoints 0 and 5
- exactly 10 equal minor intervals between each adjacent whole-kilogram label
- major kilogram ticks longer/thicker
- minor ticks uniform and clearly separated
- no value ticks in the inactive 60° gap
- labels `0,1,2,3,4,5` aligned with their major ticks

Do not improvise tick counts.

## 5. No clock confusion

The circular geometry uses six-degree minor spacing, but this is NOT a clock.

Never add 12/3/6/9 clock labels, hour/minute hands, or 60-minute semantics. Use only kilogram labels 0–5 and weight units.

## 6. Target instruction redundancy

For each item compile all of:

- semantic target value
- global tick index
- kg component + minor-tick component
- exact target angle
- relational wording

Example:

`TARGET 2.4 kg; tick_index=24; 2 kg + 4 minor ticks; target_angle=24° clockwise from top; needle starts at exact center and terminates exactly on fourth minor tick after 2.`

This metadata is render-only and must not appear as visible answer text.

## 7. Blueprint

### Internal

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

### Student render

```text
{
 id: 1,
 object: "กะหล่ำปลี",
 dial_template_id: "TH_G3_5KG_0P1_V1",
 needle_target_relation: "RENDER_ONLY: tick 24 / angle 24°",
 answer_render: "........ กิโลกรัม ........ ขีด"
}
```

## 8. Layout

Preferred card anatomy:

`NUMBER | CONTEXT OBJECT | LARGE INSTRUCTIONAL DIAL | ANSWER`

For 10 questions A4 portrait, prefer 2 columns × 5 rows if each dial remains readable.

Preferred printed dial diameter: 32–42 mm.
Absolute minimum for 0.1 kg reading: 30 mm.

If this cannot fit, paginate. Never compress circle geometry.

## 9. Decorative context scale

A small illustrated kitchen scale beneath a vegetable/object is optional context only.

- child reads the large separate dial
- small decorative dial may be neutral/simplified
- it must not contradict the large dial
- ideally remove detailed ticks from the decorative dial to avoid competing readings

## 10. Mandatory prompt block

```text
DIAL GEOMETRY — CRITICAL
- perfect front-facing circular dial in a square reserved zone
- exact center pivot with one needle and visible hub
- use canonical 300° active sweep, not a 360° value sweep
- labels: 0@240°, 1@300°, 2@0°, 3@60°, 4@120°, 5@180°
- 10 equal minor intervals per kg; each 0.1 kg = 6°
- no scale ticks in the 60° inactive gap between 5 and 0
- identical template for every question; only needle angle changes
- endpoint must land exactly on target tick
- no clock labels/clock semantics
- no overlap, skew, ellipse, crop, or perspective
```

## 11. Hard negatives

Critical failures:

- off-center/floating needle
- oval/distorted dial
- wrong 0–5 label order/positions
- 360° scale that causes 0 and 5 to overlap
- ticks in inactive gap
- unequal minor spacing
- wrong number of minor intervals
- multiple needles
- endpoint between ticks
- changed template between questions
- clock-face substitution
- dial too small to distinguish 0.1 kg marks
- object/text covering tick band

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

Inspect every dial individually after render. One incorrect dial blocks release.

## 13. Preferred implementation

Best production path:

`AI THEME ART/LAYOUT → DETERMINISTIC SVG DIAL → THAI TEXT OVERLAY → COMPOSITE → VISUAL QA`

For SVG/vector generation, construct all ticks and the needle from the formulas above. Generative image output alone is never treated as mathematically guaranteed.