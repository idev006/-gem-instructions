# Instrument Review–Revise Profile — Mandatory Renderer Self-Check

Version: 1.2.0
Status: Mandatory cross-domain runtime profile
Compatible Gem baseline: 2.6.x
Applies to: every learner-read instrument/scale and every final image-generation prompt
Primary auditors: `W07_INSTRUMENT_AUDITOR + W10_METROLOGY_ENGINEER + W08_LAYOUT_RENDER_THAI + W09_QA_RELEASE`
Companion independent audit: `policies/METROLOGY_ASSURANCE_PROFILE.md`
Companion page audit: `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

## 1. Educational safety principle

The learner may infer a measurement rule directly from the rendered instrument. Therefore an incorrect graduation, tick count, scale direction, label order, pointer pivot, hand/ray origin, endpoint, liquid level, graph-axis mapping, or distorted instrument shape can teach a false concept.

`ACADEMIC_INSTRUMENT_CORRECTNESS > VISUAL_STYLE > DECORATION > DENSITY > ONE_PAGE_EFFICIENCY`

One known-wrong learner-read instrument is a release blocker.

## 2. Mandatory renderer-side loop

Every final prompt containing learner-read geometry must instruct:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Do not intentionally return a known-invalid first-pass instrument. Self-review is prevention, not a substitute for later artifact inspection.

## 3. No-first-pass release rule

Required statement or exact semantic equivalent:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Gate: `PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`.

## 4. Deterministic self-review checklist

For each learner-read instrument, review visible construction against canonical state:

1. topology family and active range;
2. exact interval count;
3. exact physical tick/position count;
4. scale direction and endpoint behavior;
5. common baseline/ring/arc anchoring;
6. authoritative common center/origin for radial/angular instruments;
7. uniform spacing;
8. mutually exclusive major/intermediate/minor hierarchy;
9. labels aligned to intended ticks and in correct monotonic order;
10. no missing/extra/merged/duplicated/floating pseudo-ticks;
11. no physical border/edge accidentally counted as graduation;
12. pointer/hand/ray/level/object endpoint aligned exactly to target;
13. pointer/ray origin coincident with common center and radial/collinear where applicable;
14. inactive/non-scale region integrity;
15. no decorative competing scale-like marks;
16. shape/aspect ratio is canonical: no ellipse/skew/shear/non-uniform stretch;
17. repeated templates remain geometrically identical;
18. minimum print/readability rules remain satisfied.

Gate: `PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`.

## 5. Independent recount rule

Do not validate a scale only by restating its intended formula. Recount/rederive expected physical positions from canonical definition.

Endpoint-inclusive linear:

`intervals=(MAX-MIN)/MINOR_INTERVAL`
`positions=intervals+1`
`interior_positions=max(positions-2,0)`

Canonical ruler 1 cm @1 mm:
- 10 intervals;
- 11 total positions;
- 9 interior positions;
- physical ruler border is not an extra graduation.

W10 performs a second independent metrology recomputation rather than copying W07.

Gate: `PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`.

## 6. Repair behavior

If any self-review item fails, repair the instrument rather than preserve an attractive but wrong drawing.

Repair order:
1. restore canonical topology/count;
2. restore authoritative center/origin and shape;
3. restore spacing/anchoring/hierarchy;
4. restore labels and order;
5. restore target alignment and radial collinearity;
6. remove conflicting decoration;
7. enlarge instrument or paginate if readability is the cause;
8. re-run complete self-review.

Never fix density by deleting required graduations or changing academic values.

Gate: `PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`.

## 7. Confidence/uncertainty rule

If the renderer cannot reconcile visible construction with canonical count/state, it must regenerate/reconstruct instead of guessing. A vague `looks correct` review is insufficient.

Gate: `PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`.

## 8. Domain-specific review minimums

### Ruler
- each 1 cm span @1mm: 10 intervals / 11 positions / 9 interior;
- zero graduation distinct from physical edge;
- no extra short border/label lines.

### Thermometer
For 0–50°C @1°C:
- exactly 50 intervals /51 positions;
- exactly 6 major positions at multiples of10;
- exactly 5 intermediate positions at 5,15,25,35,45;
- exactly 40 ordinary minor positions;
- each 10°C span has 10 intervals /9 interior positions;
- liquid endpoint exactly on target graduation;
- bottom-to-top direction and labels correct.

### Speedometer / open-arc speed dial
- canonical 0–120 @10 =12 intervals/13 positions;
- active sweep and inactive region exact;
- `NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`;
- needle is radial/collinear from center to target tick;
- exact value-to-angle mapping;
- no value/pseudo-ticks in inactive gap;
- no full-circle substitution.

### Clock
- 60 distinct minute positions when required;
- no duplicate wrap tick;
- both hands share exact pivot;
- hand angles and continuous hour-hand placement match semantic time.

### Weight dial
Canonical 0–5 kg @0.1:
- angle convention 0° top, clockwise positive;
- label map `0@0°,1@60°,2@120°,3@180°,4@240°,5@300°`;
- clockwise major-label sequence `[0,1,2,3,4,5]`;
- 50 intervals/51 positions;
- inactive open gap `(300°,360°)` with zero radial scale-like marks;
- `NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`;
- needle mapping matches target.

### Protractor
For 0–180° @1°:
- perfect upper semicircle;
- 180 intervals/181 positions;
- one active numeric scale by default;
- 0° right,90° top,180° left;
- 10° major/5° intermediate/1° minor reuse existing positions;
- `ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`;
- every tick and target ray radial from common center;
- no ellipse, perspective, shear, non-uniform stretch or warped arc;
- printed arc spacing verified by W10;
- target ray intersects intended graduation.

### Graduated container
- exact interval/position count;
- target level/meniscus read point exact;
- no decorative competing reading line.

### Graph axis
- exact axis interval count/direction;
- equal numeric increments map to equal physical spacing;
- bars/data marks map exactly to canonical dataset.

## 9. Shape-aware page review

Renderer review must not confuse horizontal width with vertical body height. For a semicircular protractor of width `W=2R`, body height is `R=W/2` before labels/answer reserves. Page packing must use the complete item box from `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`.

Gate: `PROMPT_SHAPE_AWARE_BOUNDING_BOX_QA`.

## 10. Final-prompt mandatory block

When learner-read instruments exist, final prompt must include a compact `INSTRUMENT_REVIEW_REVISE_PROTOCOL` communicating:
- instruments are academic data;
- no blind first-pass release;
- deterministic recount/recheck;
- common-center/origin check where applicable;
- shape-integrity check;
- repair/regenerate on mismatch;
- finalization only after all instruments pass;
- downstream self-review does not claim artifact QA passed.

Gate: `PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`.

## 11. W07 / W10 / W08 / W09 ownership

- W07 defines/audits canonical geometry and review checklist.
- W10 independently verifies metrology, common center/origin, printed spacing, references, representability, label order, shape integrity and measurement/page feasibility.
- W08 ensures layout/render decisions preserve both audits and serializes review protocol.
- W09 verifies W07/W10 evidence is present and consistent; any contradiction blocks prompt release.

Mandatory learner-read route includes `W07 + W10 + W08 + W09` in addition to owning worker.

## 12. Artifact boundary

Even when renderer self-review and W10 audit are mandatory:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

until actual worksheet is inspected.

If artifact contains incorrect scale/pivot/label order/distorted instrument:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and defect becomes permanent regression.

## 13. Mandatory QA family

`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`
`PROMPT_INSTRUMENT_COMMON_CENTER_QA` when radial/angular
`PROMPT_POINTER_ORIGIN_COINCIDENCE_QA` when pointer/ray exists
`PROMPT_RADIAL_COLLINEARITY_QA` when radial/angular
`PROMPT_INSTRUMENT_SHAPE_INTEGRITY_QA`
`PROMPT_SHAPE_AWARE_BOUNDING_BOX_QA` when applicable
`PROMPT_METROLOGY_AUDIT_REQUIRED_QA`
`PROMPT_METROLOGY_INDEPENDENCE_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED`.
