# Architecture — Activity-Based Elementary Worksheet Generator

Version: 2.6.0-LTS
Status: Production Orchestrator + Specialist Worker architecture

## 1. System model

The Gem is an Orchestrator over nine logical Specialist Workers.

1. `INTERACTION/NORMALIZATION` — parse teacher language and resolve safe defaults.
2. `WORKER_ROUTING` — select only relevant academic workers plus universal layout/release workers.
3. `ACADEMIC_WORKER_LAYER` — deterministic content/rules owned by W01–W06.
4. `INSTRUMENT_AUDITOR_LAYER` — W07 cross-checks learner-read visual geometry/topology when applicable.
5. `VISIBILITY_LAYER` — separate INTERNAL, TEACHER_VISIBLE_PROMPT_METADATA, and STUDENT_VISIBLE_WORKSHEET.
6. `LAYOUT_RENDER_LAYER` — W08 resolves one render path, page capacity, Thai/text, print/theme.
7. `PROMPT_COMPILER` — compile self-contained final downstream prompt.
8. `QA_RELEASE_LAYER` — W09 validates compatibility, ownership, leaks, regressions, and release phase.
9. `DOWNSTREAM_ARTIFACT_PHASE` — image exists outside the Gem and requires separate inspection.

The production endpoint of the Gem is the prompt, not the final rendered pixels.

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

## 3. Canonical state objects

### REQUEST_CONTEXT
Raw teacher request + references + revision instructions.

### NORMALIZED_WORKSHEET_SPEC
Resolved parameters, domain/subdomain, grade, curriculum profile, render-path input, page policy.

### WORKER_ROUTE_DECISION
Selected worker IDs, reason, compatibility, ownership map, applicable QA.

### INTERNAL_VERIFIED_STATE
Hidden academic content, answers, formulas, normalized-unit values, target geometry/data and QA state.

### STUDENT_CONTENT_BLUEPRINT
Only learner-visible givens, canonical labels/template IDs and blank responses. It must not expose renderer targets, angles, tick indices, levels or solved answers.

### TEACHER_VISIBLE_RENDER_STATE
Renderer-only metadata needed to draw visuals correctly; marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

### LAYOUT_BLUEPRINT
Page regions, minimum sizes, one-page feasibility and pagination decision.

### FINAL_IMAGE_GENERATION_PROMPT
Primary self-contained copy-ready downstream prompt.

### QA_REPORT
Prompt-phase gates + explicit artifact phase status.

## 4. Canonical process

`Teacher request`
→ normalize
→ route workers
→ generate/verify academic state
→ build student-safe blueprint
→ audit instrument geometry when needed
→ resolve one render path
→ run one-page feasibility
→ build layout
→ serialize renderer-only item states
→ compile final prompt
→ run integration/regression/leak QA
→ release prompt
→ downstream image generation
→ artifact inspection

## 5. Visibility architecture

Three scopes are mandatory:

1. `INTERNAL_VERIFIED_STATE` — hidden calculations and answers.
2. `TEACHER_VISIBLE_PROMPT_METADATA` — renderer-only state in the final prompt.
3. `STUDENT_VISIBLE_WORKSHEET` — actual learner-facing content.

Answer/target leak rules apply to scope 3. Necessary renderer metadata is allowed in scope 2 but must explicitly say not to print it.

## 6. Measurement subsystem ownership

Formal coverage is documented in `domains/MEASUREMENT_COVERAGE_P1_P6.md`.

- W02: time units, elapsed time, schedules, analog clocks
- W03: weight arithmetic/conversion and dial scales
- W04: ruler, length, distance, angle/protractor, perimeter, area
- W05: thermometer, capacity, meniscus, solid volume and cubic-unit conversion
- W07: shared instrument topology auditor

Measurement calculations normalize to exact compatible units before arithmetic/formulas.

## 7. Measurement coverage

### Time
- `60 s=1 min`, `60 min=1 h`, `24 h=1 day`
- clock reading; start/end/duration; schedules; day/night; controlled midnight crossing

### Length & distance
- ruler zero/nonzero start
- mm/cm/m/km conversion
- sum/difference/comparison
- multi-segment/round trip/route comparison
- no implicit speed/rate

### Angle
- semicircular protractor 0–180°
- explicit selected 0° baseline and scale direction
- 1° resolution ⇒ 180 intervals / 181 positions

### Perimeter & area
- perimeter = boundary side sum once
- rectangle/square/triangle/parallelogram/trapezoid formulas when grade/objective supports
- circle area/circumference with one consistent `PI_POLICY`
- squared-unit conversion uses squared linear factors

### Weight
- kg/g/ขีด arithmetic/conversion
- canonical dial topology for 0–5 kg teaching scale

### Capacity/temperature
- thermometer discrete target mapping
- mL/L reading/conversion/arithmetic
- explicit meniscus convention when requested

### Volume
- rectangular prism and simple non-overlapping composite rectangular prisms
- cm³/dm³/m³ conversion uses cubed linear factors
- capacity-volume relations only when explicitly taught

## 8. Instrument contract

Learner-read geometry is academic data.

Topology families:

- `LINEAR_ENDPOINT_INCLUSIVE`: N intervals, N+1 positions.
- `CYCLIC_FULL_CIRCLE`: N intervals, N unique positions.
- `OPEN_ARC_BOUNDED`: active intervals + endpoint-inclusive active positions; inactive gap has zero value ticks unless defined otherwise.

High-risk item serialization:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

## 9. Render-path contract

Final prompt contains exactly one of:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

`AUTO` is normalization-only. Unresolved alternatives are invalid.

## 10. One-page contract

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

Correctness, minimum educational geometry, Thai readability and answer space outrank page count. Locked infeasibility blocks prompt release instead of unsafe compression.

## 11. Change impact

| Change | Preserve | Rebuild |
|---|---|---|
| Theme | academic state | W08 art/layout language |
| Difficulty/grade | theme where possible | owning worker data + layout |
| Count | skill/theme | item distribution + layout |
| Orientation/page lock | academic state | W08 layout |
| Answer key | givens | visibility/output package |
| Unit/range/resolution | context | owning measurement calculations + geometry |
| Figure/formula type | theme | W04/W05 academic state + diagram instructions |
| Render path | academic state | W08 renderer architecture |
| Worker/hotfix version | intent | route/affected worker output + W09 QA |

## 12. Error classes

- `CRITICAL_ACADEMIC`
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

Critical errors block prompt release.

## 13. QA phase boundary

Before downstream image exists, only `PROMPT_*` checks may be PASS.

Always report:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Actual artifact QA begins only after the image/document is supplied.

## 14. LTS maintenance

Baseline 2.6.x reserves Knowledge slot 10 for a narrow hotfix. Broad routing, visibility, worker-schema or multi-domain academic changes require a new base release rather than accumulating overrides.