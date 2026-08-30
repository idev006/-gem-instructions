# SCALE_READING_ENGINE — Deterministic Dial-Scale Worksheet Rules

Version: 1.0.0
Status: Mandatory production domain profile
Applies when: `DOMAIN = MEASUREMENT_WEIGHT` and `QUESTION_TYPE = DIAL_SCALE_READING`

## 1. Learning goal

The worksheet exists to teach a child to READ A SCALE, not merely look at a themed picture.

Primary student action:

`identify numbered kilogram mark → count minor divisions → locate needle endpoint → convert to kg/ticks → write answer`

For Thai Grade 3 defaults:

- `DIAL_MAX_KG = 5`
- `MAJOR_DIVISION_KG = 1`
- `MINOR_DIVISION_KG = 0.1`
- `MINOR_DIVISIONS_PER_KG = 10`
- `1 ขีด = 0.1 กิโลกรัม = 100 กรัม`
- answer format: `........ กิโลกรัม ........ ขีด`

The scale dial is instructional data. It has higher priority than decorative art.

## 2. Critical geometry invariants

Every dial rendered for a student question MUST satisfy all of these.

### 2.1 True circle

The dial face must be a true circle, never an oval or perspective ellipse.

- `DIAL_ASPECT_RATIO = 1:1`
- front-facing orthographic view
- no tilt, perspective, foreshortening, skew, squeeze, stretch, or 3D rotation
- reserve a square bounding box for every dial before layout composition

A distorted dial is a critical failure because tick spacing becomes visually invalid.

### 2.2 Fixed center pivot

The needle MUST originate from the exact geometric center of the dial.

Let the dial center be `(cx, cy)` and radius be `r`.

- pivot/hub center = `(cx, cy)`
- needle start = `(cx, cy)`
- needle may never float, detach, start off-center, or connect to a decorative point
- draw a clearly visible central hub/dot on top of the needle root
- `CENTER_PIVOT_TOLERANCE <= 1% of dial diameter` conceptually

If the needle root is not centered, reject the render.

### 2.3 Single needle

Exactly one instructional needle per enlarged dial.

Do not add a second hand, shadow-hand, decorative pointer, arrow, or duplicate needle.

### 2.4 Needle endpoint

The needle must end near the tick ring but must not cover the numeric label.

Recommended conceptual geometry:

- needle length = `0.70r–0.82r`
- hub radius = `0.035r–0.06r`
- needle width high enough for photocopy readability
- endpoint terminates at the intended tick, not between ticks

## 3. Canonical scale construction

For a 0–5 kg dial with 0.1 kg minor divisions:

- 5 kg total capacity
- 50 equal minor intervals across the full dial progression
- exactly 10 equal minor intervals between consecutive kilogram labels
- integer kilogram marks must be visibly stronger/longer than minor ticks
- all minor ticks must be evenly spaced in angle
- the sequence of labels must follow one consistent clockwise scale direction

### 3.1 No clock grammar

A weight dial is NOT a clock.

Never use clock positions merely because they look familiar. The image model must not improvise a `12/3/6/9` clock-like grammar.

Use only the specified kilogram scale labels: `0, 1, 2, 3, 4, 5`.

### 3.2 Canonical angle mapping

The prompt compiler must explicitly define a single mapping for the entire worksheet.

Default mapping for a full-circle 5 kg teaching dial:

- value `0.0 kg` begins at a fixed start angle `A0`
- value increases clockwise
- `50` minor steps complete the defined scale sweep
- every question uses the SAME `A0`, direction, sweep, label positions, and tick geometry

The exact visual start angle may be chosen by the layout engine, but after selection it is LOCKED for all questions on that worksheet.

For target weight `w`:

`tick_index = round(w / MINOR_DIVISION_KG)`

Require:

`abs(w - tick_index * MINOR_DIVISION_KG) < tolerance`

The needle endpoint must coincide with `tick_index` exactly.

The image prompt should describe the target as both value and tick relation, for example:

`1.3 kg = 1 kilogram + 3 minor ticks; needle rooted at exact center and ending exactly on the third minor tick after 1`.

This redundancy is mandatory because generative image models often misplace needles when given only a decimal number.

## 4. Tick readability rules

The enlarged instructional dial is the most important visual element inside a question card.

Required:

- strong outer circle
- integer labels large and high contrast
- major ticks visibly longer/thicker
- minor ticks clearly separated
- no decorative lines inside the tick band
- no vegetable, object, border, text, or scale body overlaps the dial
- sufficient white space around the dial

For 0.1 kg resolution, the final printed dial must be large enough that adjacent minor ticks are distinguishable by a primary-school learner.

### 4.1 Minimum visual size heuristic

For an A4 portrait worksheet:

- preferred enlarged dial diameter: `32–42 mm` printed
- absolute minimum for 0.1 kg reading: `30 mm` printed
- if the chosen layout would reduce it below the minimum, paginate or change layout

Do NOT solve density by shrinking the dial.

## 5. Instructional vs decorative scale

A themed object may sit on a small illustrated kitchen/market scale. That small scale is decorative/contextual only.

The enlarged separate dial is the authoritative instructional instrument.

Rules:

- do not require the child to read a tiny decorative dial
- decorative scale dial may be simplified
- decorative dial must not contradict the enlarged dial
- preferably keep the decorative dial neutral/simple so the child knows which dial to read

Prompt wording should say:

`The large separate close-up dial is the only instructional dial the student must read.`

## 6. Question card anatomy

For dial-reading worksheets, do NOT use the generic TIME row anatomy.

Preferred card anatomy:

`QUESTION NUMBER | CONTEXT OBJECT ON SCALE | LARGE INSTRUCTIONAL DIAL | ANSWER BLANK`

For 10 questions on A4 portrait, default to:

`2 columns × 5 rows`

because it allows larger dials than a 10-row single-column table.

Each card needs:

- clear number badge
- one object illustration
- one enlarged dial in a square reserved zone
- answer line beneath or beside it
- generous internal padding

### 6.1 Layout lock

Every large dial zone must use the same width and height.

- no auto-stretch per card
- no dial touching card border
- no row-height compression that changes circle geometry
- no cropping
- no dial partially outside its reserved square

If 10 large readable dials cannot fit, use 2 pages rather than distort them.

## 7. Content generation

Each target weight must be generated and validated before prompt compilation.

Default progression for Grade 3 should move from easy-to-read locations toward more varied minor-tick positions.

Example 10-item progression:

`0.5, 0.8, 1.0, 1.3, 1.6, 2.0, 2.4, 2.8, 3.5, 4.2 kg`

But values may vary if user-defined.

Validation for every weight:

1. `0 <= weight <= DIAL_MAX_KG`
2. weight is exactly representable by `MINOR_DIVISION_KG`
3. no unintended duplicate unless allowed
4. derive kilogram component and tick component
5. derive exact `tick_index`
6. include exact relation in INTERNAL blueprint

For Thai kg-and-ticks format:

- `kg_component = floor(weight)`
- `tick_component = round((weight - kg_component) / 0.1)`

Example:

`2.4 kg → 2 กิโลกรัม 4 ขีด`

Keep this verified answer internal when answer key is off.

## 8. Two-view blueprint for scale reading

### INTERNAL_VERIFIED_BLUEPRINT

```text
{
  id: 1,
  object: "กะหล่ำปลี",
  target_weight_kg: 1.3,
  tick_index: 13,
  kg_component: 1,
  tick_component: 3,
  verified_answer_display: "1 กิโลกรัม 3 ขีด",
  needle_rule: "third minor tick after 1 kg",
  validation_status: PASS
}
```

### STUDENT_RENDER_BLUEPRINT

```text
{
  id: 1,
  object: "กะหล่ำปลี",
  dial_max_kg: 5,
  minor_division_kg: 0.1,
  needle_target_relation: "third minor tick after 1 kg",
  answer_render: "........ กิโลกรัม ........ ขีด"
}
```

Important exception to ordinary answer-leak handling:

The final image prompt MUST contain enough target geometry to place the needle correctly, but it MUST NOT render the numeric answer as visible worksheet text. Therefore target metadata may be present as render instructions, not as student-visible labels.

## 9. Prompt compiler — mandatory dial block

For every scale-reading prompt, include a hard-constraint block equivalent to:

```text
DIAL GEOMETRY — CRITICAL:
- Each instructional dial is a perfect front-facing circle in a square reserved box; never oval, tilted, skewed, or perspective-distorted.
- The black needle is mechanically anchored to the exact geometric center of the circle with a visible central pivot dot.
- Exactly one needle per instructional dial.
- Major labels are exactly 0,1,2,3,4,5 in a single consistent clockwise scale.
- Between each adjacent whole-kilogram mark are exactly 10 equal minor intervals; 1 minor interval = 0.1 kg = 1 ขีด.
- Major ticks are longer/thicker than minor ticks.
- Needle endpoint must land exactly on the specified minor tick, not approximately between ticks.
- Use the identical dial template, label placement, tick count, start angle, direction and scale sweep for all 10 questions. Only the needle angle changes.
- Do not use clock-face grammar.
- Do not let any illustration, border, text, or answer line touch or cover the dial.
```

For each item, append a redundant target relation:

`TARGET: 2.4 kg; tick index 24 from zero; 2 kg + 4 minor ticks; needle from exact center to exactly fourth minor tick after label 2.`

This target relation is an internal render instruction, never visible text on the worksheet.

## 10. Hard negatives

Reject or explicitly prohibit:

- off-center needle root
- floating needle
- needle originating from a point other than center
- oval dial
- stretched or squeezed dial
- perspective/3D dial
- irregular minor-tick spacing
- wrong number of minor divisions
- clock numbers or clock-face grammar
- missing 0–5 labels
- reordered labels between questions
- different scale geometry between cards
- multiple needles
- needle ending between ticks
- needle covering labels
- object overlapping dial
- tiny unreadable dial
- decorative clutter inside dial
- answer printed beside/in the dial
- answer-key leakage

Any one of the first 13 failures is a critical release blocker.

## 11. Render QA gates

Add these mandatory gates for `DIAL_SCALE_READING`:

```text
DIAL_CIRCLE_QA
CENTER_PIVOT_QA
TICK_COUNT_QA
TICK_SPACING_QA
LABEL_ORDER_QA
NEEDLE_TARGET_QA
DIAL_SIZE_QA
DIAL_CLEARANCE_QA
CARD_GEOMETRY_QA
SCALE_READING_PEDAGOGY_QA
```

Release only when all are PASS.

### 11.1 Visual inspection rubric

Inspect each of the 10 dials individually.

For each dial score binary PASS/FAIL:

1. circle is not distorted
2. pivot at exact visual center
3. one needle only
4. 0–5 labels present and consistently ordered
5. ten minor intervals per kg visibly represented
6. major/minor ticks distinguishable
7. endpoint sits on intended tick
8. dial is large enough to read
9. nothing overlaps dial
10. answer remains blank

A worksheet with any incorrect needle or ambiguous scale cannot be released, regardless of aesthetic quality.

## 12. Recommended deterministic-overlay strategy

Image generation alone is not reliable enough for mathematically exact dial geometry.

Preferred production architecture:

`GENERATIVE ART/LAYOUT → DETERMINISTIC DIAL OVERLAY → TEXT OVERLAY (if needed) → VISUAL QA`

When the execution environment supports SVG/vector or programmatic overlay:

- generate the context illustrations and card layout with AI
- render each dial deterministically as SVG/vector using the verified weight
- place the dial in the reserved square zone
- overlay Thai text deterministically where possible

If deterministic overlay is unavailable, strengthen the prompt with the mandatory dial block and mark the result as requiring visual QA before classroom use.

The Gem must never imply that an uninspected generative dial is mathematically guaranteed correct.