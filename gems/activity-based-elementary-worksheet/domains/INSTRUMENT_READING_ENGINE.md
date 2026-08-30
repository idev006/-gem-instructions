# INSTRUMENT_READING_ENGINE — Shared Geometry Rules

Version: 1.1.0
Status: Mandatory base engine for visual instrument-reading worksheets

Applies to dial scales, analog clocks, rulers, thermometers, and graduated capacity instruments.

## 1. Core principle

If the learner must read a visual instrument, the instrument is academic data.

`INSTRUMENT GEOMETRY > CONTEXT ART > DECORATION`

A distorted, ambiguous, tiny, or incorrectly marked instrument is a critical academic failure.

## 2. Three-layer model

Every instrument-reading question must separate:

1. `CONTEXT_LAYER` — themed object/scene; decorative/supportive.
2. `INSTRUCTIONAL_INSTRUMENT_LAYER` — authoritative instrument the child reads.
3. `RESPONSE_LAYER` — blank/student answer area.

Never require the child to read a tiny decorative instrument if a separate enlarged teaching instrument is present.

## 3. Template lock

Within one worksheet, all instruments of the same type use one canonical template.

Lock outer geometry, orientation, scale direction, labels, tick count and spacing, font sizing, stroke hierarchy, and reserved bounding box. Only the pedagogically intended variable changes, e.g. needle angle, clock-hand position, liquid level, endpoint, or bar height.

## 4. Geometry invariants

- reserve a fixed-size geometry box before placing art/text;
- never stretch an instrument to fill a card;
- preserve aspect ratio;
- use front/orthographic view when perspective would alter reading;
- no cropping;
- no overlap with decorative art;
- no extra pointer/hand/marker that could be mistaken for data;
- instructional marks must remain distinct after monochrome printing.

## 5. Scale/tick invariants

For any graduated instrument:

- `MAJOR_INTERVAL` and `MINOR_INTERVAL` must be defined before render;
- minor divisions must be uniform;
- stronger marks identify major intervals;
- labels must align to their intended marks;
- the target indicator must coincide with a valid mark/level when exact reading is expected;
- no decorative strokes inside the scale band.

## 6. Minimum readability + global page policy

The subtype engine must define or derive a printed minimum size for the active reading task.

When layout pressure threatens that minimum, apply the global page policy in this order:

1. change to a more efficient valid layout;
2. reduce/remove nonessential decoration;
3. shorten nonessential instructions without changing meaning;
4. reduce nonessential padding/whitespace within safe print limits;
5. preserve instrument size, answer space, text legibility, and question count.

If a valid one-page solution still does not fit:

- when `ONE_PAGE_LOCK=OFF`: paginate;
- when `ONE_PAGE_LOCK=ON`: do **not** paginate and do **not** shrink below the minimum. Return `ONE_PAGE_FEASIBILITY_QA=FAIL` and `LAYOUT_QA=FAIL`.

Never solve density by shrinking, clipping, overlapping, or distorting the educational instrument.

## 7. Redundant render instruction

Do not send only a semantic value such as `2.4 kg` or `7:35`.

Compile target metadata redundantly, using value + relational geometry. Examples:

- weight: `2.4 kg = fourth minor tick after 2 kg`
- clock: `minute hand at minute 35/seventh 5-minute mark; hour hand between 7 and 8`
- ruler: `endpoint at 6.7 cm = 67 mm from zero`
- thermometer: `level at 28°C = 8 minor marks above 20°C` when scale supports it

Render-only target metadata must never become visible answer text.

## 8. Preferred rendering architecture

When available:

`AI CONTEXT ART/LAYOUT → VECTOR/SVG INSTRUMENT OVERLAY → DETERMINISTIC TEXT OVERLAY → COMPOSITE → VISUAL QA`

For text-heavy worksheets with a small instrument component, prefer deterministic document/text layout first and overlay the instrument geometry into reserved zones.

If deterministic overlay is unavailable, add hard geometry constraints and mark `VISUAL_QA_REQUIRED=YES`.

## 9. Mandatory QA

Every instrument-reading domain adds:

- `INSTRUMENT_TEMPLATE_QA`
- `GEOMETRY_QA`
- `SCALE_QA`
- `TARGET_PLACEMENT_QA`
- `MINIMUM_SIZE_QA`
- `CLEARANCE_QA`
- `VISUAL_AMBIGUITY_QA`
- `ONE_PAGE_FEASIBILITY_QA`

Inspect every individual instrument after rendering. One incorrect instructional instrument blocks classroom release.
