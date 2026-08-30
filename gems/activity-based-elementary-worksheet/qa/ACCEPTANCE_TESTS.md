# Acceptance Tests — Activity-Based Elementary Worksheet Generator

Version: 2.2.2
Status: Critical QA / Regression Suite

A production release passes only when all applicable critical tests pass. Weighted score never overrides a critical blocker.

## A. Core request / normalization

### Test 1 — Minimum teacher input
`ป.3 การอ่านตราชั่ง 10 ข้อ` resolves grade, topic, count, subject, domain, defaults, and no answer key.

### Test 2 — No silent undefined
Every normalized parameter is explicit, defaulted, auto-derived, or NONE.

### Test 3 — Exact question count
Internal blueprint, student blueprint, and render instructions contain exactly requested count.

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
Verified answer is absent from visible worksheet text in final render instructions.

### Test 10 — Render-only geometry exception
Target geometry needed to draw an instrument may exist as render-only metadata but is never rendered as answer text.

### Test 11 — Separate answer key
When key is on, default is unsolved student sheet + separate answer key.

### Test 12 — Whole-response sanitizer
When key is off, the complete visible response contains no active answer vector/list/internal solved note anywhere, including QA prose and parentheticals.

## C. Layout / readability / print

### Test 13 — Safe margins
No essential content enters unsafe print margins.

### Test 14 — No cropping
All question regions fit.

### Test 15 — Writable answer area
Student can physically write the expected response.

### Test 16 — Decoration priority
Decorative art never covers instructional text/diagram/answer area.

### Test 17 — Capacity repair when unlocked
If one page cannot preserve minimum readability and `ONE_PAGE_LOCK=OFF`, optimize layout first, then paginate rather than shrink below minimum.

### Test 18 — Monochrome readability
Black-and-white output does not rely on color coding.

### Test 19 — Stable repeated structure
Equivalent question cards/rows have consistent dimensions and hierarchy.

## D. Thai / text QA

### Test 20 — Canonical Thai text
Title, instructions, units, and labels are correctly spelled in canonical data.

### Test 21 — Unit consistency
Unit shown matches expected answer type.

### Test 22 — Hybrid text readiness
Thai-heavy layout preserves clean text zones for deterministic correction.

## E. TIME_ENGINE

### Test 23 — Whole hour
08:15→10:15 = 120 min.

### Test 24 — Mixed minutes
08:15→09:45 = 90 min.

### Test 25 — Invalid minute rejected
08:75 is invalid.

### Test 26 — Midnight guard
20:00→08:00 rejected when crossing disabled.

### Test 27 — Midnight enabled
23:30→00:30 = 60 min when explicitly enabled.

### Test 28 — Zero duration guard
08:00→08:00 rejected unless explicitly allowed.

### Test 29 — Unit rendering
1h30m task must not provide only an hours-only response field.

## F. SCALE_READING_ENGINE

### Test 30 — True circle
Instructional dial is not oval/skewed.

### Test 31 — Center pivot
Needle root equals geometric center.

### Test 32 — One needle
Exactly one instructional pointer.

### Test 33 — Correct labels
0–5 labels are complete and consistently ordered.

### Test 34 — Minor division count
Exactly 10 equal intervals per kilogram for 0.1 kg mode.

### Test 35 — Uniform tick spacing
Minor tick spacing is visually uniform.

### Test 36 — Exact target
2.4 kg points exactly to fourth minor tick after 2.

### Test 37 — Template lock
All dials share identical scale geometry; only needle changes.

### Test 38 — No clock grammar
No accidental clock-style scale substitution.

### Test 39 — Minimum dial size
Dial is not reduced below configured printable minimum.

### Test 40 — Decorative scale separation
Tiny context scale is not the authoritative student-reading instrument.

### Test 41 — Scale answer format
Thai Grade 3 kg/tick mode uses `........ กิโลกรัม ........ ขีด` unless overridden.

## G. CLOCK_READING_ENGINE

### Test 42 — True clock circle
Clock face preserves circle geometry.

### Test 43 — Two hands
Exactly hour + minute hands unless seconds requested.

### Test 44 — Hand lengths
Minute hand is visibly longer.

### Test 45 — Minute mapping
7:35 minute hand points to 35-minute mark.

### Test 46 — Hour interpolation
At 7:30, hour hand is halfway between 7 and 8.

### Test 47 — Standard label orientation
12 top, 3 right, 6 bottom, 9 left.

### Test 48 — Day/night one-clock structure
In `CLOCK_READING_MODE=DAY_NIGHT_PAIR`, one question contains exactly one instructional clock face and exactly two blank answer fields.

### Test 49 — Day/night mapping for 1–5
Analog 2:30 maps internally to daytime 14:30 and nighttime 02:30.

### Test 50 — Day/night mapping for 6–11
Analog 7:45 maps internally to daytime 07:45 and nighttime 19:45.

### Test 51 — Twelve/zero mapping
Analog 12:15 maps internally to daytime 12:15 and nighttime 00:15.

### Test 52 — Minute preservation
Day/night paired answers preserve the same minute value as the analog face.

### Test 53 — Paired-answer leak guard
When answer key is off, neither verified day nor verified night time appears anywhere in the visible package.

### Test 54 — Sun/moon cue is not computation
Decorative day/night icons may support labels but cannot replace deterministic mapping or be the sole source of answer semantics.

## H. LENGTH_READING_ENGINE

### Test 55 — Zero alignment
Beginner object begins at zero graduation, not merely ruler edge.

### Test 56 — Uniform ruler ticks
1 cm and 1 mm spacing are consistent.

### Test 57 — Endpoint mapping
6.7 cm endpoint maps to 67 mm from zero under the 1 mm profile.

### Test 58 — Nonzero-start arithmetic
Length = end mark - start mark.

## I. TEMPERATURE_READING_ENGINE

### Test 59 — Uniform thermometer scale
Major/minor intervals are consistent.

### Test 60 — Level mapping
Column top aligns exactly with target temperature.

### Test 61 — Unit consistency
°C/°F is consistent with configured domain.

## J. CAPACITY_READING_ENGINE

### Test 62 — Container not distorted
Scale-reading geometry remains front-facing and readable.

### Test 63 — Uniform graduations
Graduation intervals are correct.

### Test 64 — Liquid-level mapping
Surface/meniscus aligns with target graduation.

### Test 65 — Meniscus convention
When scientific mode is active, reading convention is explicit and consistent.

## K. MONEY_ENGINE

### Test 66 — Total arithmetic
Sum of item prices recomputes correctly.

### Test 67 — Change arithmetic
`change = paid-total` and paid>=total.

### Test 68 — Price association
Each price label belongs unambiguously to one item.

## L. CALENDAR_ENGINE

### Test 69 — Valid date
No 31 April.

### Test 70 — Leap year
February length is correct for configured year.

### Test 71 — Weekday mapping
Dates align to correct weekday.

### Test 72 — Seven columns
Monthly calendar has exactly seven weekday columns.

## M. TABLE_GRAPH_READING_ENGINE

### Test 73 — Dataset first
Visualization values exactly match canonical dataset.

### Test 74 — Bar height
Every bar height maps to configured axis scale/value.

### Test 75 — No perspective distortion
No 3D bar treatment that changes perceived magnitude.

### Test 76 — Pictograph key
Icon count × key equals canonical value.

### Test 77 — Table alignment
Headers and cells map unambiguously.

## N. Revision / impact analysis

### Test 78 — Theme-only revision
Academic content remains unchanged when user requests only theme change.

### Test 79 — Difficulty revision
Affected academic values regenerate and revalidate.

### Test 80 — Orientation revision
Content preserved; one-page/layout/print QA reruns.

### Test 81 — Instrument resolution change
All target relations and geometry regenerate.

### Test 82 — Dataset revision
Graph/table visualization and dependent questions rebuild.

### Test 83 — Clock mode revision
Changing SINGLE↔DAY_NIGHT_PAIR rebuilds response schema/layout and reruns clock/answer-leak QA without silently changing intended hand geometry.

## O. Post-render QA

### Test 84 — Prompt pass is not artifact pass
A rendered artifact can fail even if prompt passes.

### Test 85 — Per-instrument inspection
Every instructional instrument is inspected individually.

### Test 86 — One wrong instrument blocks release
One incorrect needle/hand/endpoint/level causes FAIL.

### Test 87 — Photocopy test
Educational marks remain distinguishable in monochrome print.

### Test 88 — Render-objective lock
A student worksheet request must not produce an audit dashboard, QA poster, report, rubric, prompt summary, or meta-document.

### Test 89 — Thai + numeral glyph coverage
When deterministic text overlay is used, selected font/render path visibly supports required Thai text, Arabic numerals, punctuation, decimal point, and unit symbols. Missing-glyph boxes/tofu fail release.

### Test 90 — Render recovery after artifact-type failure
If renderer returns wrong artifact type, mark FAIL, strengthen/route the render path, and rerun. Never count the failed meta-artifact as worksheet evidence.

### Test 91 — Paired clock post-render structure
For DAY_NIGHT_PAIR, each rendered question visibly contains one readable clock and two clearly labelled blank response fields associated with that same clock.

## P. v2.2.1 global page / render / governance regression

### Test 92 — One-page preferred default
A normal request with no page count resolves `TARGET_PAGE_COUNT=1`, `ONE_PAGE_PREFERRED=YES`, `ONE_PAGE_LOCK=OFF`.

### Test 93 — One-page optimization before pagination
When initial layout does not fit, system attempts a more efficient layout and removes nonessential decoration before creating page 2.

### Test 94 — Explicit one-page lock
`A4 หน้าเดียวเท่านั้น` resolves `ONE_PAGE_LOCK=ON`, `PAGE_COUNT=1`, and page 2 is prohibited.

### Test 95 — Locked infeasibility fails safely
If required content cannot fit one page above minimum readability, return `ONE_PAGE_FEASIBILITY_QA=FAIL` and `LAYOUT_QA=FAIL`; do not shrink below domain minimum, crop, reduce question count, or silently paginate.

### Test 96 — Instrument policy obeys page lock
An instrument worksheet cannot use the old unconditional “paginate” rule when `ONE_PAGE_LOCK=ON`; it must fail feasibility instead.

### Test 97 — Text-heavy render-path selection
A Thai 10-row elapsed-time table under `RENDER_PATH=AUTO` resolves to `DOCUMENT_FIRST` or `HYBRID`, not IMAGE_ONLY by default.

### Test 98 — Exact-instrument render-path selection
Scale/clock/ruler/thermometer/capacity tasks under AUTO resolve to HYBRID or DETERMINISTIC_VECTOR when exact geometry is required, unless another deterministic path is explicitly justified.

### Test 99 — Registry maturity is authoritative
If an engine header and `DOMAIN_REGISTRY.md` disagree, `DOMAIN_MATURITY_QA=FAIL`; teacher-visible output uses registry status and the repository must repair the mismatch before release.

### Test 100 — Academic maturity is not overall maturity
A deterministic academic calculation layer may be reported as mature, but overall `DOMAIN_MATURITY` remains the registry value until release-matrix evidence is satisfied.

## Q. v2.2.2 cross-domain graduation-count regression

### Test 101 — Interval/tick distinction
For an endpoint-inclusive linear scale, `EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`. The system must not confuse intervals with tick positions.

### Test 102 — Exact representability
A graduated scale whose `(MAX-MIN)/MINOR_INTERVAL` is non-integer is rejected or normalized before render; renderer never approximates a nonrepresentable graduation system.

### Test 103 — Ruler 1 cm topology
A 0–1 cm span at 1 mm resolution contains exactly 10 equal intervals and 11 endpoint-inclusive graduation positions.

### Test 104 — Clock cyclic topology
A full minute-mark analog clock contains exactly 60 equal intervals and 60 distinct minute positions; minute 0 and minute 60 share the same 12-o'clock location and must not create a duplicate tick.

### Test 105 — Thermometer count
A 0–50°C thermometer with 1°C minor interval contains exactly 50 intervals and 51 endpoint-inclusive graduation positions.

### Test 106 — Thermometer zero placement
A -10–40°C thermometer with 1°C interval places 0°C exactly 10 intervals above -10°C and preserves 50 intervals/51 positions overall.

### Test 107 — Capacity count 100 mL
A 0–1000 mL scale with 100 mL minor interval contains exactly 10 intervals and 11 endpoint-inclusive graduation positions.

### Test 108 — Capacity count 50 mL
A 0–1000 mL scale with 50 mL minor interval contains exactly 20 intervals and 21 endpoint-inclusive graduation positions.

### Test 109 — No missing/extra graduation
Any missing, duplicated, merged, or extra instructional graduation in a learner-read scale is `CRITICAL_ACADEMIC` and blocks release even if spacing otherwise looks regular.

### Test 110 — No graduation outside active scale
No value tick may appear in an inactive or non-scale region. This includes the 60° inactive gap of the canonical 0–5 kg teaching dial.

### Test 111 — Major/minor ratio
When both major and minor intervals exist, each major interval contains exactly `MAJOR_INTERVAL / MINOR_INTERVAL` equal minor intervals.

### Test 112 — Per-instrument graduation audit
Post-render QA verifies graduation count for every instructional instrument individually; a page-level spot check is insufficient.

## Release gates

Global required statuses:

```text
INTENT_QA
PARAMETER_QA
DOMAIN_ROUTE_QA
DOMAIN_MATURITY_QA
ACADEMIC_QA
CALCULATION_QA
CONSTRAINT_QA
ANSWER_LEAK_QA
VISIBLE_OUTPUT_SANITIZER_QA
DUPLICATE_QA
THAI_QA
GLYPH_COVERAGE_QA when deterministic text is rendered
RENDER_PATH_QA
ONE_PAGE_FEASIBILITY_QA
PAGE_COUNT_QA
RENDER_OBJECTIVE_QA
LAYOUT_QA
READABILITY_QA
PRINT_QA
PROMPT_QA
INTERVAL_COUNT_QA when graduated instruments are present
TICK_POSITION_COUNT_QA/GRADUATION_COUNT_QA when graduated instruments are present
NO_MISSING_TICK_QA when graduated instruments are present
NO_EXTRA_TICK_QA when graduated instruments are present
```

Plus all applicable domain-specific geometry/data gates.

Critical blockers include wrong academic result, invalid data/geometry, wrong graduation count, missing/extra instructional marks, ambiguous instrument, answer leakage anywhere in visible output, wrong count, wrong artifact type, incorrect maturity claim, unsafe page-lock override, missing glyphs/tofu, unreadable/cropped layout, or malformed canonical text.

Dry-run score target: >=95/100 AND zero critical blockers. Actual classroom release additionally requires post-render inspection when nondeterministic rendering is used.
