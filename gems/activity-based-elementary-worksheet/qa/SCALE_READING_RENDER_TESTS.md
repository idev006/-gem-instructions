# Scale Reading Render Regression Tests

Version: 1.0.0
Status: Mandatory for `DIAL_SCALE_READING`

These tests were added after observed render defects including off-center needle roots, unclear/incorrect scale grammar, distorted dials caused by layout compression, ambiguous minor ticks, and excessive decoration.

A worksheet fails if ANY critical geometry test fails, even if the page looks attractive.

## Critical dial geometry

### SR-01 — Perfect circle
Every large instructional dial must be a true circle. Any oval, squeeze, perspective ellipse, skew, or non-uniform scale = FAIL.

### SR-02 — Square dial container
Every dial is placed in a square reserved layout zone. Width and height of the dial zone must match conceptually.

### SR-03 — Center pivot
Needle root/hub must be visually at exact geometric center of the circle. Off-center, floating, detached, or displaced root = CRITICAL FAIL.

### SR-04 — Visible hub
A visible center pivot dot/hub must cover the needle root clearly.

### SR-05 — One needle
Exactly one instructional needle per large dial. Duplicate/shadow/second hand = FAIL.

### SR-06 — Needle endpoint
Needle endpoint must land exactly on the intended tick, not between ticks and not on a label.

## Scale grammar

### SR-07 — Label set
Dial contains exactly the intended kilogram labels `0,1,2,3,4,5` and no clock numbers.

### SR-08 — Consistent label order
All questions use identical label positions/order/direction.

### SR-09 — Ten minor intervals per kilogram
Between each adjacent whole-kilogram mark, there are exactly ten equal minor intervals for `MINOR_DIVISION_KG=0.1`.

### SR-10 — Uniform tick spacing
Minor ticks are evenly spaced. Irregular clustering or missing ticks = FAIL.

### SR-11 — Major/minor distinction
Whole-kilogram ticks are visibly longer/thicker than 0.1 kg ticks.

### SR-12 — Template lock
All dials use the same start angle, sweep, direction, labels, radius, tick construction, and visual grammar. Only needle angle may change.

### SR-13 — No clock grammar
The dial must not visually behave like a clock face. Any `12,3,6,9` pattern or clock-hand convention = FAIL.

## Numeric accuracy

### SR-14 — Representable target
Every target weight is inside 0–5 kg and exactly representable in 0.1 kg steps.

### SR-15 — Tick-index mapping
For each target `w`, verify `tick_index = round(w/0.1)` and that the needle points to that exact tick.

### SR-16 — Redundant target instruction
Prompt for every item contains value + tick index + relative description, e.g. `2.4 kg; tick 24; 2 kg + 4 minor ticks; fourth tick after 2`.

### SR-17 — Internal answer mapping
Internal blueprint correctly maps decimal kilograms to kg-and-ticks. Example: `2.4 kg → 2 กิโลกรัม 4 ขีด`.

### SR-18 — Answer leak guard
When answer key is off, verified answer is not printed as visible worksheet text.

## Readability and layout

### SR-19 — Minimum dial size
At intended A4 print size, each enlarged dial is at least 30 mm diameter for 0.1 kg resolution. Preferred 32–42 mm.

### SR-20 — 10-item default layout
For 10 questions on A4 portrait, default layout is 2 columns × 5 rows unless another layout demonstrably preserves equal or better dial readability.

### SR-21 — No single-column squeeze
A 10-row single-column table that forces dial shrink/distortion must be rejected or paginated.

### SR-22 — Equal dial zones
All instructional dial zones have equal dimensions and padding.

### SR-23 — Clearance
No object, card border, answer blank, decoration, or text overlaps the dial circle/tick band.

### SR-24 — No cropping
No dial, label, tick, or answer area is clipped by card/page boundaries.

### SR-25 — Decoration subordinate
Decorative art cannot reduce dial size, distort the dial, or compete with scale readability.

### SR-26 — Instructional dial dominance
The separate large dial is visually more readable than any tiny contextual dial on an illustrated kitchen scale.

### SR-27 — Decorative dial non-conflict
If a tiny decorative dial exists on the scale illustration, it must not show a contradictory readable value. Prefer neutral/simplified depiction.

## Pedagogy

### SR-28 — Tick meaning
For Thai Grade 3 default, the normalized spec contains `1 ขีด = 0.1 กิโลกรัม = 100 กรัม`.

### SR-29 — Answer format
Default student response format is `........ กิโลกรัม ........ ขีด` unless user asks otherwise.

### SR-30 — Progressive difficulty
A 10-item set should progress from easier landmark positions to varied minor-tick positions rather than use decoration as difficulty.

### SR-31 — One objective
All questions practice reading the scale. Avoid unrelated arithmetic or object-counting tasks unless requested.

## Prompt-level negative constraints

### SR-32 — Explicit center lock
Final prompt explicitly says needle is anchored to exact geometric center.

### SR-33 — Explicit circle lock
Final prompt explicitly prohibits oval, tilt, skew, stretch, squeeze, and perspective distortion.

### SR-34 — Explicit tick lock
Final prompt explicitly states ten equal minor intervals per 1 kg and 0.1 kg per minor interval.

### SR-35 — Explicit template lock
Final prompt explicitly says same dial template across all questions, only needle angle changes.

### SR-36 — Explicit no-clock rule
Final prompt explicitly prohibits clock-face grammar.

## Recommended deterministic overlay

### SR-37 — Vector overlay preferred
When SVG/vector/programmatic overlay capability exists, the plan should choose deterministic dial rendering instead of relying solely on image generation.

### SR-38 — Generative-only warning
When deterministic overlay is unavailable, QA report must flag that the generated dials require visual inspection before classroom use.

## Release gate

Required PASS statuses:

```text
DIAL_CIRCLE_QA = PASS
CENTER_PIVOT_QA = PASS
TICK_COUNT_QA = PASS
TICK_SPACING_QA = PASS
LABEL_ORDER_QA = PASS
NEEDLE_TARGET_QA = PASS
DIAL_SIZE_QA = PASS
DIAL_CLEARANCE_QA = PASS
CARD_GEOMETRY_QA = PASS
SCALE_READING_PEDAGOGY_QA = PASS
```

Zero critical blockers are allowed.

A worksheet with even one ambiguous or incorrect instructional dial is NOT classroom-ready.