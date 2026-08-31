# Actual Measurement-Reference Defects — 2026-08-31

Status: PERMANENT REGRESSION EVIDENCE
Severity: P0_CRITICAL_ACADEMIC when visible to learners
Baseline family: 2.6.x

## Why this document exists

User-supplied rendered worksheets exposed four instructional-geometry defects that can misteach measurement even when global interval formulas are correct. These defects are retained as permanent regression evidence and must not be normalized away as cosmetic variation.

`ONE WRONG INSTRUCTIONAL REFERENCE = CLASSROOM RELEASE BLOCKER`

## D1 — Analog clock continuous hour-hand interpolation

Observed artifact: a 14:45 / 2:45 clock can render the short hour hand directly on the numeral 2.

Canonical rule:

`minute_hand_angle_deg = 6*m`
`hour_hand_angle_deg = 30*(h mod 12) + 0.5*m`

Therefore 2:45:

- minute hand = 270° clockwise from 12;
- hour hand = 82.5° clockwise from 12;
- hour hand = 75% of the way from 2 to 3;
- hard negative: hour hand must not remain directly on numeral 2.

Required gates:

`PROMPT_CLOCK_QUARTER_HOUR_INTERPOLATION_QA`
`PROMPT_NONZERO_MINUTE_HOUR_DISPLACEMENT_QA`
`ARTIFACT_CLOCK_HOUR_HAND_INTERPOLATION_QA`

## D2 — Canonical 0–5 kg / 0.1 kg subdivision hierarchy

Each 1 kg span contains exactly 10 equal 0.1 kg intervals and 11 endpoint-inclusive positions when both kilogram endpoints are counted.

Within each 1 kg major span:

- major endpoints at whole kilograms;
- one intermediate position at +0.5 kg;
- the +0.5 kg tick is longer than ordinary 0.1 kg ticks but shorter/weaker than the whole-kilogram major tick;
- remaining ordinary minor positions are +0.1,+0.2,+0.3,+0.4,+0.6,+0.7,+0.8,+0.9 kg.

`INTERVALS_PER_KG=10`
`INTERIOR_POSITIONS_PER_KG_SPAN=9`
`HALF_KG_INTERMEDIATE_OFFSET=0.5`
`HALF_KG_INTERMEDIATE_TICK_REUSES_EXISTING_POSITION=YES`

No extra tick may be created for the intermediate hierarchy.

Required gates:

`PROMPT_WEIGHT_PER_KG_SUBDIVISION_QA`
`PROMPT_WEIGHT_HALF_KG_INTERMEDIATE_QA`
`ARTIFACT_WEIGHT_SUBDIVISION_HIERARCHY_QA`

## D3 — Ruler object endpoint projection/reference

Observed artifact: an object can visually start at the physical border/edge of the ruler rather than the zero graduation, making the intended measurement origin ambiguous.

For object-on-ruler elementary worksheets, both object endpoints require projection/reference guides whenever the object does not physically touch the graduation line itself.

Canonical geometry:

`OBJECT_START_X == START_GRADUATION_X`
`OBJECT_END_X == END_GRADUATION_X`

Projection guides:

`START_PROJECTION_GUIDE_X = OBJECT_START_X`
`END_PROJECTION_GUIDE_X = OBJECT_END_X`

The guides are thin dashed vertical lines from the exact object endpoint to the ruler reading line. They are helper geometry, not ruler graduations.

For `ZERO_START_MODE`:

`START_GRADUATION_VALUE=0`
`OBJECT_START_X == ZERO_GRADUATION_X`

The physical ruler edge is never substituted for the zero graduation unless it is explicitly defined to coincide exactly with that graduation.

For `NONZERO_START_MODE`:

`TARGET_LENGTH = END_VALUE - START_VALUE`

Required gates:

`PROMPT_RULER_ENDPOINT_PROJECTION_GUIDE_QA`
`PROMPT_RULER_ZERO_START_ALIGNMENT_QA`
`PROMPT_RULER_NONZERO_START_RELATION_QA`
`ARTIFACT_RULER_REFERENCE_ALIGNMENT_QA`

## D4 — Graduated container 0–1000 mL @50 mL local-span topology

Observed artifact: labels 0,100,...,1000 can look plausible while multiple extra minor ticks are drawn between adjacent 100 mL labels.

Canonical global topology:

`RANGE=0..1000 mL`
`MINOR_INTERVAL=50 mL`
`MAJOR_INTERVAL=100 mL`
`EXPECTED_INTERVAL_COUNT=20`
`EXPECTED_POSITION_COUNT=21`

Canonical local topology for every adjacent 100 mL major span:

`INTERVALS_PER_100ML=2`
`INTERIOR_POSITIONS_PER_100ML_SPAN=1`
`INTERIOR_VALUE_OFFSET=50 mL`

Thus each major span such as 300→400 has exactly one interior graduation at 350 mL. There must not be 4, 5, or any other number of minor marks inside that span.

Major ticks are at multiples of 100 mL; the single 50 mL interior tick is shorter/weaker and unlabeled unless the objective explicitly requests otherwise.

Required gates:

`PROMPT_CAPACITY_PER_100ML_SUBDIVISION_QA`
`PROMPT_CAPACITY_LOCAL_SPAN_RECOUNT_QA`
`PROMPT_CAPACITY_MAJOR_MINOR_HIERARCHY_QA`
`ARTIFACT_CAPACITY_LOCAL_SPAN_QA`

## Cross-worker ownership and non-self-certification

- W02 owns clock formulas and renderer relations.
- W03 owns weight-dial subdivision semantics.
- W04 owns ruler start/end measurement semantics.
- W05 owns graduated-container topology.
- W07 independently audits visible geometry.
- W10 independently recomputes quantitative/local-span oracles.
- W08 serializes the verified constraints into the final rendering prompt.
- W09 blocks release if any applicable gate is FAIL or NOT_RUN.

`NO WORKER MAY SELF-CERTIFY ITS OWN HIGH-RISK OUTPUT.`

## Release semantics

The supplied defective artifacts remain:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

Future rendered samples are `ARTIFACT_QA=NOT_YET_TESTED` until visually audited against these invariants.
