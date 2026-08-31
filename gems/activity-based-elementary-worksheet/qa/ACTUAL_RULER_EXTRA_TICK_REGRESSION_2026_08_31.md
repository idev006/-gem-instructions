# Actual Render Regression — Ruler Extra Tick / Wrong 1 cm Subdivision

Date: 2026-08-31
Source: user-supplied rendered worksheet crop
Severity: `CRITICAL_ACADEMIC`
Applies to: ruler / linear scale reading
Owning worker: `W04_LENGTH_DISTANCE`
Auditors: `W07_INSTRUMENT_AUDITOR + W08_LAYOUT_RENDER_THAI + W09_QA_RELEASE`

## Observed defect

A rendered ruler-like scale showed too many short graduation lines within what should represent a 1 cm span at 1 mm resolution.

This is not cosmetic. A child may infer the wrong relationship between centimetres and millimetres from the image.

## Canonical oracle

`1 cm = 10 mm`

For one 1 cm span with smallest graduation 1 mm:

- exactly 10 equal intervals;
- exactly 11 physical graduation positions including the two endpoint positions;
- exactly 9 interior positions strictly between the two endpoint positions;
- the physical ruler border/outline is not an additional graduation;
- any 5 mm intermediate hierarchy mark occupies one of those existing positions and does not add a new position;
- the next centimetre endpoint is the 11th position, not an extra minor tick after 10 mm.

## Required prompt prevention

The canonical ruler template must explicitly serialize:

`CM_INTERVAL_MM=10`
`INTERVALS_PER_CM=10`
`POSITIONS_PER_CM_SPAN=11`
`INTERIOR_POSITIONS_PER_CM_SPAN=9`
`PHYSICAL_EDGE_IS_GRADUATION=NO`

The renderer-side review protocol must recount every 1 cm span before finalization.

## Required artifact inspection

For every rendered ruler using 1 mm resolution:

1. choose at least one complete adjacent-centimetre span;
2. identify the two centimetre endpoint graduations;
3. count exactly 10 spaces between them;
4. confirm exactly 9 interior graduation positions;
5. confirm no border, label stroke, decoration, or detached line acts as an extra graduation;
6. confirm spacing is uniform;
7. repeat across the canonical template if visual deformation is suspected.

Any mismatch:

`ARTIFACT_SCALE_INTERVAL_COUNT_QA=FAIL`
`ARTIFACT_SCALE_POSITION_COUNT_QA=FAIL`
`ARTIFACT_RULER_SUBDIVISION_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

## Permanent regression requirement

This defect must remain represented in executable regression coverage. Release counts may only increase; do not remove the regression to restore a green build.
