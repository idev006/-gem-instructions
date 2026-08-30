# INSTRUMENT_READING_ENGINE — Shared Geometry Rules

Version: 1.2.0
Status: Mandatory base engine for visual instrument-reading worksheets

Applies to dial scales, analog clocks, rulers, thermometers, and graduated capacity instruments.

## 1. Core principle

If the learner must read a visual instrument, the instrument is academic data.

`INSTRUMENT GEOMETRY > CONTEXT ART > DECORATION`

A distorted, ambiguous, tiny, incorrectly marked, missing-tick, or extra-tick instrument is a critical academic failure.

## 2. Three-layer model

Every instrument-reading question must separate:

1. `CONTEXT_LAYER` — themed object/scene; decorative/supportive.
2. `INSTRUCTIONAL_INSTRUMENT_LAYER` — authoritative instrument the child reads.
3. `RESPONSE_LAYER` — blank/student answer area.

Never require the child to read a tiny decorative instrument if a separate enlarged teaching instrument is present.

## 3. Template lock

Within one worksheet, all instruments of the same type use one canonical template.

Lock outer geometry, orientation, scale direction, labels, **active range, interval count, tick-position count**, tick spacing, font sizing, stroke hierarchy, and reserved bounding box. Only the pedagogically intended variable changes, e.g. needle angle, clock-hand position, liquid level, endpoint, or bar height.

## 4. Geometry invariants

- reserve a fixed-size geometry box before placing art/text;
- never stretch an instrument to fill a card;
- preserve aspect ratio;
- use front/orthographic view when perspective would alter reading;
- no cropping;
- no overlap with decorative art;
- no extra pointer/hand/marker that could be mistaken for data;
- instructional marks must remain distinct after monochrome printing.

## 5. Deterministic graduation arithmetic — mandatory

For every instrument whose active scale runs from `SCALE_MIN` to `SCALE_MAX` with smallest instructional interval `d`:

`EXPECTED_INTERVAL_COUNT = (SCALE_MAX - SCALE_MIN) / d`

Require exact representability within numerical tolerance:

`abs(EXPECTED_INTERVAL_COUNT - round(EXPECTED_INTERVAL_COUNT)) < tolerance`

Then:

`EXPECTED_INTERVAL_COUNT = round(EXPECTED_INTERVAL_COUNT)`

For a linear or endpoint-inclusive active scale:

`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

The subtype engine may define a different topology only when academically necessary and must state it explicitly. Example: a clock is cyclic and uses 60 minute positions/60 equal intervals; a dial scale with an inactive gap counts only positions on its active sweep.

### Mandatory distinction

A **division/interval** is the space between two adjacent graduation positions.
A **tick position** is a marked boundary/location.

Do not confuse “10 divisions” with “10 tick positions”. For example, 0–1 cm at 1 mm resolution has 10 intervals and 11 endpoint-inclusive tick positions.

### Critical rule

A renderer must not improvise graduation count. If one instructional interval/tick is missing, duplicated, added, or placed in an inactive/non-scale region, the instrument fails.

## 6. Scale/tick invariants

For any graduated instrument:

- `MAJOR_INTERVAL` and `MINOR_INTERVAL` must be defined before render;
- active range endpoints must be explicit;
- expected interval/tick counts must be computed before render;
- minor divisions must be uniform;
- stronger marks identify major intervals;
- labels must align to their intended marks;
- the target indicator must coincide with a valid mark/level when exact reading is expected;
- no decorative strokes inside the scale band;
- no value ticks may appear outside the declared active scale;
- repeated instruments must use identical graduation topology unless the task explicitly changes the scale.

## 7. Post-render graduation verification

For **every instructional instrument**, verify after render:

1. active range endpoints;
2. interval count;
3. tick/graduation-position count according to topology;
4. uniform spacing;
5. major/minor hierarchy;
6. label-to-tick alignment;
7. no missing ticks;
8. no duplicate/extra ticks;
9. no ticks in inactive/non-scale regions;
10. target marker/level/endpoint maps to the intended graduation.

A page-level visual impression is not sufficient. Each instrument must be inspected individually.

## 8. Minimum readability + global page policy

The subtype engine must define or derive a printed minimum size for the active reading task.

When layout pressure threatens that minimum, apply the global page policy in this order:

1. change to a more efficient valid layout;
2. reduce/remove nonessential decoration;
3. shorten nonessential instructions without changing meaning;
4. reduce nonessential padding/whitespace within safe print limits;
5. preserve instrument size, answer space, text legibility, question count, and graduation distinguishability.

If a valid one-page solution still does not fit:

- when `ONE_PAGE_LOCK=OFF`: paginate;
- when `ONE_PAGE_LOCK=ON`: do **not** paginate and do **not** shrink below the minimum. Return `ONE_PAGE_FEASIBILITY_QA=FAIL` and `LAYOUT_QA=FAIL`.

Never solve density by shrinking, clipping, overlapping, distorting, or visually merging graduation marks.

## 9. Redundant render instruction

Do not send only a semantic value such as `2.4 kg` or `7:35`.

Compile target metadata redundantly, using value + interval/tick index + relational geometry. Examples:

- weight: `2.4 kg = active tick index 24 = fourth minor tick after 2 kg`
- clock: `minute hand at minute 35/seventh 5-minute mark; hour hand between 7 and 8`
- ruler: `endpoint at 6.7 cm = 67 mm from zero`
- thermometer: `level at 28°C = 8 minor intervals above 20°C` when scale supports it
- capacity: `650 mL at tick index 13 on a 50 mL scale`

Render-only target metadata must never become visible answer text.

## 10. Preferred rendering architecture

When available:

`AI CONTEXT ART/LAYOUT → VECTOR/SVG INSTRUMENT OVERLAY → DETERMINISTIC TEXT OVERLAY → COMPOSITE → VISUAL QA`

For text-heavy worksheets with a small instrument component, prefer deterministic document/text layout first and overlay the instrument geometry into reserved zones.

If deterministic overlay is unavailable, add hard geometry + graduation-count constraints and mark `VISUAL_QA_REQUIRED=YES`.

## 11. Mandatory QA

Every instrument-reading domain adds:

- `INSTRUMENT_TEMPLATE_QA`
- `GEOMETRY_QA`
- `SCALE_RANGE_QA`
- `INTERVAL_COUNT_QA`
- `TICK_POSITION_COUNT_QA` or subtype-equivalent `GRADUATION_COUNT_QA`
- `TICK_SPACING_QA`
- `MAJOR_MINOR_QA`
- `NO_MISSING_TICK_QA`
- `NO_EXTRA_TICK_QA`
- `NON_SCALE_REGION_QA` when applicable
- `TARGET_PLACEMENT_QA`
- `MINIMUM_SIZE_QA`
- `CLEARANCE_QA`
- `VISUAL_AMBIGUITY_QA`
- `ONE_PAGE_FEASIBILITY_QA`

Inspect every individual instrument after rendering. One incorrect instructional instrument blocks classroom release.

## 12. Child-learning rationale

Incorrect graduation count is not a minor drawing defect. It can teach the child a false unit relationship, for example that 1 cm has the wrong number of millimetre intervals or that a scale contains an extra value interval. Therefore graduation-count errors are classified as `CRITICAL_ACADEMIC`.
