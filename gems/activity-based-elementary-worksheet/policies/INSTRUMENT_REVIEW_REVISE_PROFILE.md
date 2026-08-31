# Instrument Review–Revise Profile — Mandatory Renderer Self-Check

Version: 1.0.0
Status: Mandatory cross-domain runtime profile
Compatible Gem baseline: 2.6.x
Applies to: every learner-read instrument/scale and every final image-generation prompt
Primary auditors: `W07_INSTRUMENT_AUDITOR + W08_LAYOUT_RENDER_THAI + W09_QA_RELEASE`

## 1. Educational safety principle

The learner may infer a measurement rule directly from the rendered instrument. Therefore an incorrect graduation, tick count, scale direction, label, pointer, hand, ray, endpoint, liquid level, or graph-axis mapping can teach a false mathematical/scientific concept.

`ACADEMIC_INSTRUMENT_CORRECTNESS > VISUAL_STYLE > DECORATION > DENSITY > ONE_PAGE_EFFICIENCY`

One known-wrong learner-read instrument is a release blocker.

## 2. Mandatory renderer-side loop

Every final prompt containing learner-read geometry must instruct the downstream renderer to execute this logical loop before returning its final worksheet:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Do not intentionally return a known-invalid first-pass instrument.

The self-review is not a substitute for later artifact inspection. It is an additional prevention layer.

## 3. No-first-pass release rule

For high-risk instruments, the prompt must explicitly prohibit blind first-pass release.

Required statement or exact semantic equivalent:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

The renderer must check every instructional instrument after composition and revise any item that does not match its canonical state.

Gate: `PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`.

## 4. Deterministic self-review checklist

For each learner-read instrument, review the visible construction against the supplied canonical template/state:

1. topology family and active range;
2. exact interval count;
3. exact physical tick/position count;
4. scale direction and endpoint behavior;
5. common baseline/ring/arc anchoring;
6. uniform spacing;
7. major/minor hierarchy;
8. labels aligned to intended major ticks;
9. no missing/extra/merged/duplicated/floating pseudo-ticks;
10. no physical border/edge accidentally counted as a graduation;
11. pointer/hand/ray/level/object endpoint aligned exactly to target;
12. inactive/non-scale region integrity;
13. no decorative competing scale-like marks;
14. repeated templates remain geometrically identical;
15. minimum print/readability rules remain satisfied.

Gate: `PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`.

## 5. Independent recount rule

Do not validate a scale only by restating its intended formula. Recount/rederive the expected physical positions from the canonical scale definition and compare against the intended rendered construction.

For endpoint-inclusive linear scales:

`intervals=(MAX-MIN)/MINOR_INTERVAL`
`positions=intervals+1`
`interior_positions=max(positions-2,0)`

Canonical ruler example, 1 cm at 1 mm:

- 10 equal intervals
- 11 total positions including both cm endpoints
- exactly 9 interior graduation positions between the two endpoint positions
- the physical ruler border is not an extra graduation

Gate: `PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`.

## 6. Repair behavior

If any self-review item fails, the renderer must repair the instrument rather than preserve an attractive but wrong drawing.

Repair order:

1. restore canonical topology/count;
2. restore spacing/anchoring/hierarchy;
3. restore labels;
4. restore target alignment;
5. remove conflicting decoration;
6. enlarge instrument or paginate if readability is the cause;
7. re-run the complete self-review.

Never fix density by deleting required graduations or changing academic values.

Gate: `PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`.

## 7. Confidence/uncertainty rule

If the renderer cannot confidently reconcile its visible construction with the canonical count/state, it must regenerate/reconstruct that instrument instead of guessing.

A vague `looks correct` review is insufficient. Review must refer to count, topology, alignment, and scale-line rules.

Gate: `PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`.

## 8. Domain-specific review minimums

### Ruler
- verify each 1 cm span independently when 1 mm resolution is used;
- 10 intervals / 11 positions / 9 interior positions;
- zero graduation distinct from physical edge;
- no extra short lines near labels or border.

### Thermometer
- verify exact range and interval/position count;
- target is representable;
- liquid endpoint is exactly on the intended graduation centerline;
- no between-tick endpoint unless interpolation is explicitly taught;
- scale direction and zero/minus labels are correct.

### Speedometer / open-arc dial
- verify active sweep and inactive region;
- exact value-to-angle mapping;
- exact active interval/position count;
- needle terminates on the reading ring at the target tick;
- no value ticks in inactive region;
- do not silently convert open arc to full circle.

### Clock
- 60 distinct minute positions when full minute marks are required;
- no duplicate wrap tick;
- hand angles and continuous hour-hand placement match semantic time.

### Weight dial
- active sweep/gap preserved;
- no gap ticks;
- needle mapping matches target.

### Protractor
- origin/baseline/direction exact;
- expected graduation count exact;
- target ray intersects the intended graduation.

### Graduated container
- exact interval/position count;
- target level/meniscus read point exact;
- no decorative competing reading line.

### Graph axis
- exact axis interval count and direction;
- tick spacing uniform for equal values;
- bars/data marks map exactly to canonical dataset.

## 9. Final-prompt mandatory block

When learner-read instruments exist, the standalone final prompt must include a compact `INSTRUMENT_REVIEW_REVISE_PROTOCOL` that communicates:

- instruments are academic data;
- no blind first-pass release;
- deterministic recount/recheck;
- repair/regenerate on any mismatch;
- finalization only after all instructional instruments pass the renderer-side checklist;
- downstream self-review does not claim artifact QA has passed.

Gate: `PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`.

## 10. W07 / W08 / W09 ownership

- W07 defines/audits the canonical geometry and review checklist.
- W08 ensures layout/render decisions do not make the checklist impossible and serializes the review protocol into the final prompt.
- W09 verifies the protocol is present and consistent with all applicable instrument gates; any missing/contradictory review instruction blocks prompt release.

## 11. Artifact boundary

Even when renderer self-review is mandatory:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

until the actual rendered worksheet is supplied and inspected.

If an artifact visibly contains an incorrect scale, set:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and convert the defect into a permanent regression before the next accepted release artifact.

## 12. Mandatory QA family

`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED`.
