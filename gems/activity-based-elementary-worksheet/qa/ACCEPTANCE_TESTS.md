# Acceptance Tests — Activity-Based Elementary Worksheet Generator

Version: 2.0.0
Status: Critical QA / Regression Suite

A production release passes only when all applicable critical tests pass. Weighted score never overrides a critical blocker.

## A. Core request / normalization

### Test 1 — Minimum teacher input
`ป.3 การอ่านตราชั่ง 10 ข้อ` resolves grade, topic, count, subject, domain, defaults, and no answer key.

### Test 2 — No silent undefined
Every normalized parameter is explicit, defaulted, auto-derived, or NONE.

### Test 3 — Exact question count
Internal blueprint, student blueprint, and prompt contain exactly requested count.

### Test 4 — Correct domain routing
Scale→MEASUREMENT_WEIGHT; analog clock→TIME_CLOCK; ruler→MEASUREMENT_LENGTH; thermometer→MEASUREMENT_TEMPERATURE; capacity→MEASUREMENT_CAPACITY; money→MONEY; calendar→CALENDAR; graph/table→DATA_READING.

### Test 5 — Domain maturity transparency
Candidate domain must not be reported as hardened.

### Test 6 — Teacher-friendly interaction
System does not ask for technical parameter names when safe defaults exist.

## B. Two-view / answer integrity

### Test 7 — Internal answer retained
Internal verified blueprint stores answer and QA metadata.

### Test 8 — Student answer removed
When key is off, student blueprint contains no visible answer value.

### Test 9 — Prompt answer-leak guard
Verified answer is absent from visible worksheet text in final prompt.

### Test 10 — Render-only geometry exception
Target geometry needed to draw an instrument may exist as render-only metadata but is never rendered as answer text.

### Test 11 — Separate answer key
When key is on, default is unsolved student sheet + separate answer key.

## C. Layout / readability / print

### Test 12 — Safe margins
No essential content enters unsafe print margins.

### Test 13 — No cropping
All question regions fit.

### Test 14 — Writable answer area
Student can physically write the expected response.

### Test 15 — Decoration priority
Decorative art never covers instructional text/diagram/answer area.

### Test 16 — Capacity repair
If one page makes content too small, paginate rather than shrink below domain minimum.

### Test 17 — Monochrome readability
Black-and-white output does not rely on color coding.

### Test 18 — Stable repeated structure
Equivalent question cards/rows have consistent dimensions and hierarchy.

## D. Thai / text QA

### Test 19 — Canonical Thai text
Title, instructions, units, and labels are correctly spelled in canonical data.

### Test 20 — Unit consistency
Unit shown matches expected answer type.

### Test 21 — Hybrid text readiness
Thai-heavy layout preserves clean text zones for deterministic correction.

## E. TIME_ENGINE

### Test 22 — Whole hour
08:15→10:15 = 120 min.

### Test 23 — Mixed minutes
08:15→09:45 = 90 min.

### Test 24 — Invalid minute rejected
08:75 is invalid.

### Test 25 — Midnight guard
20:00→08:00 rejected when crossing disabled.

### Test 26 — Midnight enabled
23:30→00:30 = 60 min when explicitly enabled.

### Test 27 — Zero duration guard
08:00→08:00 rejected unless explicitly allowed.

### Test 28 — Unit rendering
1h30m task must not provide only an hours-only response field.

## F. SCALE_READING_ENGINE

### Test 29 — True circle
Instructional dial is not oval/skewed.

### Test 30 — Center pivot
Needle root equals geometric center.

### Test 31 — One needle
Exactly one instructional pointer.

### Test 32 — Correct labels
0–5 labels are complete and consistently ordered.

### Test 33 — Minor division count
Exactly 10 equal intervals per kilogram for 0.1 kg mode.

### Test 34 — Uniform tick spacing
Minor tick spacing is visually uniform.

### Test 35 — Exact target
2.4 kg points exactly to fourth minor tick after 2.

### Test 36 — Template lock
All dials share identical scale geometry; only needle changes.

### Test 37 — No clock grammar
No accidental clock-style scale substitution.

### Test 38 — Minimum dial size
Dial is not reduced below configured printable minimum.

### Test 39 — Decorative scale separation
Tiny context scale is not the authoritative student-reading instrument.

### Test 40 — Scale answer format
Thai Grade 3 kg/tick mode uses `........ กิโลกรัม ........ ขีด` unless overridden.

## G. CLOCK_READING_ENGINE

### Test 41 — True clock circle
Clock face preserves circle geometry.

### Test 42 — Two hands
Exactly hour + minute hands unless seconds requested.

### Test 43 — Hand lengths
Minute hand is visibly longer.

### Test 44 — Minute mapping
7:35 minute hand points to 35-minute mark.

### Test 45 — Hour interpolation
At 7:30, hour hand is halfway between 7 and 8.

### Test 46 — Standard label orientation
12 top, 3 right, 6 bottom, 9 left.

## H. LENGTH_READING_ENGINE

### Test 47 — Zero alignment
Beginner object begins at zero graduation, not merely ruler edge.

### Test 48 — Uniform ruler ticks
1 cm and 1 mm spacing are consistent.

### Test 49 — Endpoint mapping
6.7 cm endpoint maps to 67 mm from zero.

### Test 50 — Nonzero-start arithmetic
Length = end mark - start mark.

## I. TEMPERATURE_READING_ENGINE

### Test 51 — Uniform thermometer scale
Major/minor intervals are consistent.

### Test 52 — Level mapping
Column top aligns exactly with target temperature.

### Test 53 — Unit consistency
°C/°F is consistent with configured domain.

## J. CAPACITY_READING_ENGINE

### Test 54 — Container not distorted
Scale-reading geometry remains front-facing and readable.

### Test 55 — Uniform graduations
Graduation intervals are correct.

### Test 56 — Liquid-level mapping
Surface/meniscus aligns with target graduation.

### Test 57 — Meniscus convention
When scientific mode is active, reading convention is explicit and consistent.

## K. MONEY_ENGINE

### Test 58 — Total arithmetic
Sum of item prices recomputes correctly.

### Test 59 — Change arithmetic
`change = paid-total` and paid>=total.

### Test 60 — Price association
Each price label belongs unambiguously to one item.

## L. CALENDAR_ENGINE

### Test 61 — Valid date
No 31 April.

### Test 62 — Leap year
February length is correct for configured year.

### Test 63 — Weekday mapping
Dates align to correct weekday.

### Test 64 — Seven columns
Monthly calendar has exactly seven weekday columns.

## M. TABLE_GRAPH_READING_ENGINE

### Test 65 — Dataset first
Visualization values exactly match canonical dataset.

### Test 66 — Bar height
Every bar height maps to configured axis scale/value.

### Test 67 — No perspective distortion
No 3D bar treatment that changes perceived magnitude.

### Test 68 — Pictograph key
Icon count × key equals canonical value.

### Test 69 — Table alignment
Headers and cells map unambiguously.

## N. Revision / impact analysis

### Test 70 — Theme-only revision
Academic content remains unchanged when user requests only theme change.

### Test 71 — Difficulty revision
Affected academic values regenerate and revalidate.

### Test 72 — Orientation revision
Content preserved; layout/print QA reruns.

### Test 73 — Instrument resolution change
All target relations and geometry regenerate.

### Test 74 — Dataset revision
Graph/table visualization and dependent questions rebuild.

## O. Post-render QA

### Test 75 — Prompt pass is not artifact pass
A rendered image can fail even if prompt passes.

### Test 76 — Per-instrument inspection
Every instructional instrument is inspected individually.

### Test 77 — One wrong instrument blocks release
One incorrect needle/hand/endpoint/level causes FAIL.

### Test 78 — Photocopy test
Educational marks remain distinguishable in monochrome print.

## Release gates

Global required statuses:

```text
INTENT_QA
PARAMETER_QA
DOMAIN_ROUTE_QA
ACADEMIC_QA
CALCULATION_QA
CONSTRAINT_QA
ANSWER_LEAK_QA
DUPLICATE_QA
THAI_QA
LAYOUT_QA
READABILITY_QA
PRINT_QA
PROMPT_QA
```

Plus all applicable domain-specific geometry/data gates.

Critical blockers include wrong academic result, invalid data/geometry, ambiguous instrument, answer leakage, wrong count, unreadable/cropped layout, or malformed canonical text.

Dry-run score target: >=95/100 AND zero critical blockers. Actual classroom release additionally requires post-render inspection when nondeterministic rendering is used.