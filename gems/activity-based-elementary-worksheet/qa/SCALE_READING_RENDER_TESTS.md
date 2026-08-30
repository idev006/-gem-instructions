# Scale Reading Render Regression Tests

Version: 1.1.0
Status: Mandatory for `DIAL_SCALE_READING`

These tests protect against observed defects: off-center needles, distorted circles, wrong scale grammar, endpoint overlap, ticks in the inactive gap, ambiguous minor divisions, page compression, answer leakage, and wrong render path.

A worksheet fails if ANY critical geometry test fails, even if the page looks attractive.

## Critical dial geometry

### SR-01 — Perfect circle
Every instructional dial is a true circle. Oval, squeeze, skew, perspective ellipse, non-uniform scaling, or crop = FAIL.

### SR-02 — Square dial container
Each dial is placed in a reserved square zone so layout cannot distort the face.

### SR-03 — Center pivot
Needle root/hub equals exact geometric center. Off-center, floating, detached, or displaced root = CRITICAL FAIL.

### SR-04 — Visible hub
A visible center hub covers the needle root clearly.

### SR-05 — One needle
Exactly one instructional needle per dial.

### SR-06 — Needle endpoint
Needle endpoint lands exactly on the target tick and does not terminate on a label or between ticks.

## Canonical scale grammar

### SR-07 — Label set
Canonical Grade-3 5 kg dial contains kilogram labels `0,1,2,3,4,5` only.

### SR-08 — Locked label positions
Verify `0@240°, 1@300°, 2@0°, 3@60°, 4@120°, 5@180°` under the convention 0°=top, clockwise positive.

### SR-09 — Active sweep
Value sweep from 0 kg to 5 kg is exactly 300°.

### SR-10 — Distinct endpoints
0 kg and 5 kg occupy distinct positions; a 360° value sweep that overlaps the endpoints = CRITICAL FAIL.

### SR-11 — Inactive gap
The remaining 60° arc from 5 back to 0 contains no value ticks or value labels.

### SR-12 — Tick count
For 0–5 kg with 0.1 kg minor divisions, there are exactly 50 equal intervals and 51 tick positions including endpoints.

### SR-13 — Ten intervals per kilogram
Exactly ten equal minor intervals occur between adjacent whole-kilogram labels.

### SR-14 — Uniform angular spacing
Every 0.1 kg step equals 6° within rendering tolerance.

### SR-15 — Major/minor distinction
Whole-kilogram marks are visibly stronger than minor marks without obscuring labels.

### SR-16 — Template lock
All dials use the same circle, start angle, active sweep, gap, labels, tick geometry, radius, and stroke hierarchy. Only the pedagogically intended variable changes.

### SR-17 — No clock grammar
No 12/3/6/9 clock substitution, hour/minute semantics, or second hand.

## Numeric accuracy

### SR-18 — Representable target
Every target is within capacity and exactly representable by the configured minor division.

### SR-19 — Tick-index mapping
For default profile, verify `tick_index=round(w/0.1)`.

### SR-20 — Angle mapping
Verify `angle=(240 + tick_index*6) mod 360`.

### SR-21 — Known vector 0.5 kg
0.5 kg → tick 5 → 270°.

### SR-22 — Known vector 1.0 kg
1.0 kg → tick 10 → 300°.

### SR-23 — Known vector 2.4 kg
2.4 kg → tick 24 → 24° and fourth minor tick after 2 kg.

### SR-24 — Known vector 5.0 kg
5.0 kg → tick 50 → 180°; it must not overlap 0 kg.

### SR-25 — Redundant render metadata
Each internal render target contains semantic value + tick index + target angle + relative tick wording.

### SR-26 — Internal kg/tick answer mapping
Example: `2.4 kg → 2 กิโลกรัม 4 ขีด` in the internal verified view.

### SR-27 — Answer leak guard
When key is off, target weight/verified kg+tick answer is not printed as visible answer text.

## Readability and layout

### SR-28 — Minimum dial size
At intended A4 print scale, dial diameter >=30 mm for 0.1 kg reading; preferred 32–42 mm.

### SR-29 — Ten-item one-page attempt
For 10 questions on A4 portrait, first attempt 2 columns × 5 rows when the 30 mm minimum and answer space can be preserved.

### SR-30 — One-page optimization before pagination
Reduce decoration and nonessential spacing or choose a more efficient valid layout before adding a second page.

### SR-31 — Explicit one-page lock
When user requests one page only, set `ONE_PAGE_LOCK=ON`; page 2 is prohibited.

### SR-32 — Locked infeasibility fails safely
If 10 dials cannot fit above minimum readability under a locked one-page request, return feasibility/layout FAIL rather than shrinking below 30 mm, cropping, overlapping, or reducing count.

### SR-33 — No single-column squeeze
Reject a dense 10-row single-column layout that makes dials unreadable or distorted.

### SR-34 — Equal dial zones
All instructional dial zones have equal dimensions and consistent padding.

### SR-35 — Clearance
No art/text/border/answer blank overlaps circle, labels, tick band, or needle endpoint.

### SR-36 — No cropping
No dial, label, tick, hub, needle, or answer area is clipped.

### SR-37 — Decoration subordinate
Decorative art may not reduce instructional dial readability.

### SR-38 — Instructional dial dominance
Authoritative dial is visually more readable than any decorative contextual scale.

### SR-39 — Decorative dial non-conflict
Any small decorative scale must be neutral/simplified and not show a contradictory readable value.

## Pedagogy

### SR-40 — Tick meaning
Thai Grade 3 default includes `1 ขีด = 0.1 กิโลกรัม = 100 กรัม`.

### SR-41 — Answer format
Default response is `........ กิโลกรัม ........ ขีด` unless overridden.

### SR-42 — Progressive difficulty
Question set progresses through increasingly varied target positions rather than decoration-driven difficulty.

### SR-43 — One learning objective
All questions practice reading weight unless another skill is explicitly requested.

## Prompt/render constraints

### SR-44 — Center lock in render instructions
Render plan explicitly anchors needle at exact center.

### SR-45 — Circle lock
Render instructions prohibit oval, tilt, skew, stretch, squeeze, and perspective distortion.

### SR-46 — Sweep/gap lock
Render instructions explicitly state 300° active sweep + 60° inactive gap.

### SR-47 — Tick lock
Render instructions state 10 equal intervals per kg / 0.1 kg per interval / 6° per interval under default profile.

### SR-48 — Template lock
Render instructions require identical dial template across items.

### SR-49 — No-clock rule
Render instructions explicitly prohibit clock-face grammar.

### SR-50 — Render path
Under AUTO, exact scale geometry resolves to HYBRID or DETERMINISTIC_VECTOR when available; generative image-only is not the preferred correctness path.

### SR-51 — Generative-only warning
If IMAGE_ONLY/nondeterministic geometry is used, `VISUAL_QA_REQUIRED=YES` and no mathematical guarantee may be claimed.

## Post-render inspection

### SR-52 — Inspect every dial
Every instructional dial is inspected individually after render.

### SR-53 — One wrong dial blocks worksheet
One incorrect circle/pivot/tick/label/needle makes the complete worksheet FAIL for classroom release.

### SR-54 — Page count QA
Actual rendered page count matches resolved one-page preference/lock outcome.

### SR-55 — Monochrome print check
Minor/major ticks, labels, needle, and hub remain distinguishable after black-and-white printing/photocopying.

## Release gate

Required statuses include:

```text
DIAL_CIRCLE_QA
CENTER_PIVOT_QA
ACTIVE_SWEEP_QA
ENDPOINT_DISTINCT_QA
INACTIVE_GAP_QA
TICK_COUNT_QA
TICK_SPACING_QA
LABEL_POSITION_QA
NEEDLE_TARGET_QA
TEMPLATE_LOCK_QA
DIAL_SIZE_QA
DIAL_CLEARANCE_QA
ONE_PAGE_FEASIBILITY_QA
PAGE_COUNT_QA
RENDER_PATH_QA
ANSWER_LEAK_QA
SCALE_READING_PEDAGOGY_QA
```

Zero critical blockers are allowed. A worksheet with even one ambiguous or incorrect instructional dial is not classroom-ready.
