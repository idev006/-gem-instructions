# Architecture — Activity-Based Elementary Worksheet Generator

Version: 2.6.2-LTS
Status: Production Orchestrator + Specialist Worker + Instrument-Safety architecture

## 1. System model

The Gem is an Orchestrator over nine logical Specialist Workers.

1. `INTERACTION/NORMALIZATION` — parse teacher language and resolve safe defaults/provenance.
2. `WORKER_ROUTING` — select owning academic workers plus universal W08/W09 and W07 when learner-read geometry exists.
3. `ACADEMIC_WORKER_LAYER` — deterministic content/rules owned by W01–W06.
4. `INSTRUMENT_GEOMETRY_LAYER` — owning worker creates canonical visual state; W07 audits topology, scale-line integrity and review checklist.
5. `VISIBILITY_LAYER` — separate INTERNAL, TEACHER_VISIBLE_PROMPT_METADATA and STUDENT_VISIBLE_WORKSHEET.
6. `LAYOUT_RENDER_LAYER` — W08 resolves one render path, page feasibility, Thai/text, print/theme, and serializes mandatory instrument review/revise protocol.
7. `PROMPT_COMPILER` — compile one self-contained final downstream prompt.
8. `QA_RELEASE_LAYER` — W09 runs conjunctive compatibility, ownership, academic, leak, scale-line, review-protocol and regression gates.
9. `DOWNSTREAM_RENDER_PREVENTION_LOOP` — renderer generates, self-reviews canonical learner-read instruments, repairs/regenerates mismatches, rechecks, then finalizes.
10. `DOWNSTREAM_ARTIFACT_PHASE` — actual image/document exists outside the Gem and requires separate artifact inspection.

The production endpoint of the Gem is the verified generation prompt/package. Renderer self-review is a prevention layer, not proof that pixels are correct.

## 2. Worker registry

- `W01_ACADEMIC_CONTENT`
- `W02_TIME_CLOCK`
- `W03_WEIGHT_SCALE`
- `W04_LENGTH_DISTANCE`
- `W05_TEMPERATURE_CAPACITY_VOLUME`
- `W06_MONEY_CALENDAR_DATA`
- `W07_INSTRUMENT_AUDITOR`
- `W08_LAYOUT_RENDER_THAI`
- `W09_QA_RELEASE`

Optional slot 10: `W10_HOTFIX_OVERRIDE`.

Every worker contract defines:

`ACCEPTS | OWNS | RETURNS | MUST_NOT_DECIDE | QA`

Ownership prevents cross-domain contamination.

## 3. Mandatory shared runtime profiles

Every W01–W09 generated Knowledge bundle inherits:

1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`

When learner-read geometry exists, `INSTRUMENT_READING_ENGINE.md` is the shared geometry engine and the owning domain engine defines numeric truth.

These are base-architecture contracts. They are not optional theme/style hints and are not broad W10 hotfix material.

## 4. Canonical state objects

### REQUEST_CONTEXT
Raw teacher request + references + revision instructions.

### NORMALIZED_WORKSHEET_SPEC
Resolved parameters, provenance, domain/subdomain, grade, curriculum profile, render-path input and page policy.

### WORKER_ROUTE_DECISION
Selected worker IDs, reason, compatibility, ownership map and applicable QA.

### INTERNAL_VERIFIED_STATE
Hidden academic content, answers, formulas, normalized-unit values, target geometry/data and independent verification state.

### STUDENT_CONTENT_BLUEPRINT
Only learner-visible givens, canonical labels/template IDs and blank responses. It never exposes hidden renderer targets, angles, indices, levels, speeds or solved answers.

### SCALE_LINE_SPEC
Required when the learner reads ticks/graduations/axis intervals. Contains at least:

`TOPOLOGY_FAMILY`
`ACTIVE_RANGE`
`MINOR_INTERVAL`
`MAJOR_INTERVAL`
`EXPECTED_INTERVAL_COUNT`
`EXPECTED_POSITION_COUNT`
`SCALE_DIRECTION`
`REFERENCE_BASELINE_OR_RING`
`TICK_ANCHOR_MODE`
`MAJOR_MINOR_HIERARCHY`
`ENDPOINT_BEHAVIOR`
`MIN_PRINTED_INSTRUMENT_SIZE`
`MIN_TICK_CENTER_SPACING_MM`

plus `INACTIVE_REGION_RULE` when applicable.

### TEACHER_VISIBLE_RENDER_STATE
Renderer-only metadata needed to draw visuals correctly; marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

For learner-read items, state is atomic:

`ITEM_ID + SEMANTIC_TARGET + EXACT_RENDER_STATE + RELATIONAL_VERIFICATION + ITEM_SPECIFIC_HARD_NEGATIVE`

### INSTRUMENT_REVIEW_REVISE_PROTOCOL
Required in Final Prompt whenever learner-read instruments exist. Includes deterministic recount/recheck/repair instructions and:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

### LAYOUT_BLUEPRINT
Page regions, minimum sizes, scale/tick readability requirements, one-page feasibility and pagination decision.

### FINAL_IMAGE_GENERATION_PROMPT
Primary self-contained copy-ready downstream prompt.

### QA_REPORT
Prompt-phase gates + explicit artifact phase status.

## 5. Canonical process

`Teacher request`
→ normalize + provenance
→ route workers
→ generate/independently verify academic state
→ build student-safe blueprint
→ build canonical learner-read instrument state if applicable
→ resolve `SCALE_LINE_SPEC`
→ W07 topology/scale/review audit
→ resolve one render path
→ one-page feasibility
→ W08 layout + atomic renderer-state serialization + review-protocol serialization
→ compile Final Prompt
→ W09 conjunctive prompt QA/regression gates
→ prompt release
→ downstream render
→ renderer self-review against canonical state
→ repair/regenerate on mismatch
→ full recheck
→ renderer finalization
→ actual artifact inspection

## 6. Renderer prevention loop

Mandatory whenever learner-read geometry exists:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

The review must deterministically check:

- exact topology/range;
- interval and physical-position count;
- anchoring/baseline/ring/arc;
- spacing and major/minor hierarchy;
- label alignment/clearance;
- missing/extra/merged/floating ticks;
- physical border/edge accidentally acting as a graduation;
- target hand/needle/ray/level/endpoint alignment;
- inactive-region integrity;
- decoration isolation;
- canonical-template consistency;
- print readability.

`Looks correct` is not sufficient review evidence.

If the renderer cannot reconcile its visible construction with canonical state, it reconstructs the instrument rather than guessing.

## 7. Visibility architecture

Three scopes are mandatory:

1. `INTERNAL_VERIFIED_STATE` — hidden calculations, answers and canonical target state.
2. `TEACHER_VISIBLE_PROMPT_METADATA` — renderer-only state in Final Prompt.
3. `STUDENT_VISIBLE_WORKSHEET` — actual learner-facing content.

Answer/target leak rules apply to scope 3. Necessary renderer metadata is allowed in scope 2 but explicitly says not to print it.

## 8. Measurement subsystem ownership

Formal coverage is documented in `domains/MEASUREMENT_COVERAGE_P1_P6.md`.

- W02: time units, elapsed time, schedules, analog clocks
- W03: weight arithmetic/conversion and dial scales
- W04: ruler, length, distance, **direct speedometer reading**, angle/protractor, perimeter, area
- W05: thermometer, capacity, meniscus, solid volume and cubic-unit conversion
- W06: money/calendar/data; graph-axis data semantics
- W07: shared instrument topology, scale-line and review/recount auditor
- W08: layout/render/Thai + review-protocol serializer
- W09: conjunctive integration/release gate

Direct speedometer reading does not silently activate `speed=distance/time` calculation.

## 9. Measurement coverage and smoke oracles

### Time / clock
- `60 s=1 min`, `60 min=1 h`, `24 h=1 day`
- full minute clock = 60 intervals /60 distinct positions
- 10:30 = minute 180°, hour 315°

### Length / ruler / distance
- `10 mm=1 cm`, `100 cm=1 m`, `1000 m=1 km`
- 1 cm @1 mm = 10 intervals /11 positions /9 interior positions
- physical ruler edge is not a graduation
- nonzero measurement = end-start
- distance route rules do not silently become speed-rate math

### Speedometer
Canonical elementary direct-reading profile:

- domain `MEASUREMENT_SPEEDOMETER`
- 0–120 km/h
- `OPEN_ARC_BOUNDED`
- 240° active sweep starting at 240°, clockwise
- 20 km/h major, 10 km/h minor
- 12 active intervals /13 positions
- 120° inactive gap
- one instructional needle
- `target_angle=(240+2*target_kmh) mod 360`

### Angle
- semicircular protractor 0–180° @1° = 180 intervals /181 positions
- explicit selected 0° baseline/direction

### Perimeter / area
- perimeter = boundary side sum once
- correct supported formulas
- squared-unit conversion uses squared linear factors
- one consistent `PI_POLICY` for circles

### Weight
- kg/g/ขีด arithmetic/conversion
- canonical 0–5 kg dial = 300° active +60° gap, 50 intervals /51 positions at 0.1 kg

### Temperature / capacity
- thermometer exact topology, representability, direction and endpoint alignment
- 0–50°C @1°C = 50/51
- mL/L reading/conversion/arithmetic
- explicit meniscus convention when requested

### Volume
- rectangular prism and simple non-overlapping composite prisms
- cubic conversion uses cubed factors

### Data
- graph axis equal numeric intervals map to equal geometric spacing
- canonical dataset controls plotted values

## 10. Instrument topology contract

Topology families:

- `LINEAR_ENDPOINT_INCLUSIVE`: N intervals, N+1 positions.
- `CYCLIC_FULL_CIRCLE`: N intervals, N unique positions.
- `OPEN_ARC_BOUNDED`: active intervals + endpoint-inclusive active positions; inactive gap has zero value ticks unless explicitly defined.
- `PROTRACTOR_HALF_CIRCLE`: endpoint-inclusive half-circle topology.

For endpoint-inclusive linear scales:

`EXPECTED_INTERIOR_POSITION_COUNT=max(EXPECTED_POSITION_COUNT-2,0)`

High-risk item serialization is atomic and never relies on wide drifting tables.

## 11. Scale-line print contract

Default lower bounds at final print size unless an owning domain requires more:

- minor tick stroke >=0.25 mm
- major tick stroke >=0.35 mm
- major tick length >=1.5× minor tick length
- adjacent smallest tick-center spacing >=0.60 mm

If density threatens these requirements, reduce decoration/instruction padding or paginate. Never delete/merge required graduations.

## 12. Render-path contract

Final prompt contains exactly one of:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

`AUTO` is normalization-only. Unresolved alternatives are invalid.

## 13. One-page contract

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

Correctness, exact scale geometry, minimum educational size, Thai readability and answer space outrank page count.

When lock is OFF, final prompt preserves safe pagination. Locked infeasibility blocks release rather than unsafe scale compression.

## 14. Change impact

| Change | Preserve | Rebuild |
|---|---|---|
| Theme | academic state | W08 art/layout language |
| Difficulty/grade | theme where possible | owning-worker data + layout |
| Count | skill/theme | item distribution + layout |
| Orientation/page lock | academic state | W08 layout |
| Answer key | givens | visibility/output package |
| Unit/range/resolution | context | owning calculations + canonical scale state + W07 review |
| Instrument type | learning intent if compatible | route + owning engine + W07/W08/W09 |
| Speedometer profile | theme | W04 target/tick/angle + W07 scale audit + layout |
| Thermometer profile | theme | W05 scale/target state + W07 audit + layout |
| Render path | academic state | W08 renderer architecture |
| Shared scale/review profile | user intent | full base package + regression/CI |
| Worker/hotfix version | intent | route/affected worker output + W09 QA |

## 15. Error classes

- `CRITICAL_ACADEMIC`
- `CRITICAL_SCALE_GEOMETRY`
- `CRITICAL_ANSWER_INTEGRITY`
- `CRITICAL_TARGET_LEAK`
- `CRITICAL_READABILITY`
- `CRITICAL_PROMPT_COMPLETENESS`
- `CRITICAL_PLACEHOLDER`
- `CRITICAL_KB_COMPATIBILITY`
- `CRITICAL_WORKER_OWNERSHIP`
- `MAJOR_LAYOUT`
- `MAJOR_GOVERNANCE`
- `MINOR_VISUAL`

Critical errors block prompt release. One known-wrong learner-read instrument blocks classroom release.

## 16. QA phase boundary

Before downstream image exists, only prompt-phase checks may be PASS.

Always report:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Renderer self-review never changes this status.

If actual artifact contains a wrong scale:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and the defect becomes permanent regression evidence.

## 17. LTS maintenance

Baseline 2.6.x reserves Knowledge slot 10 for a narrow hotfix.

Broad routing, visibility, worker-schema, cross-domain scale safety, renderer review-loop or new deterministic domain changes require a new base release and full installation package rebuild.

2.6.2-LTS is such a base-architecture release, driven in part by the actual 2026-08-31 ruler extra-tick defect.
