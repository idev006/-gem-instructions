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

The production endpoint of the Gem is the prompt, not the final pixels.

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

Every worker has contract fields:

`ACCEPTS | OWNS | RETURNS | MUST_NOT_DECIDE | QA`

Ownership prevents cross-domain contamination.

## 3. Canonical state objects

### REQUEST_CONTEXT
Raw teacher request + references + revision instructions.

### NORMALIZED_WORKSHEET_SPEC
Resolved parameters, domain/subdomain, grade, curriculum profile, render path input, page policy.

### WORKER_ROUTE_DECISION
Selected worker IDs, reason, compatibility, ownership map, applicable QA.

### INTERNAL_VERIFIED_STATE
Hidden answers/calculations/target values/geometry.

### STUDENT_CONTENT_BLUEPRINT
Only learner-visible givens, canonical labels/template IDs and blank responses. It must not expose renderer target values, angles, tick indices, levels, or solved answers.

### TEACHER_VISIBLE_RENDER_STATE
Renderer-only metadata needed to draw visuals correctly; marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

### LAYOUT_BLUEPRINT
Page zones, minimum sizes, one-page feasibility and pagination decision.

### FINAL_IMAGE_GENERATION_PROMPT
Self-contained copy-ready downstream prompt.

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

1. `INTERNAL_VERIFIED_STATE` — hidden system calculations.
2. `TEACHER_VISIBLE_PROMPT_METADATA` — renderer-only state in the final prompt.
3. `STUDENT_VISIBLE_WORKSHEET` — actual learner-facing content.

Answer/target leak rules apply to scope 3. Necessary renderer metadata is allowed in scope 2 but must explicitly say not to print it.

## 6. Measurement subsystem

Formal measurement coverage is documented in `domains/MEASUREMENT_COVERAGE_P1_P6.md` and owned across:

- W02: time/clock
- W03: weight/scale
- W04: ruler/length/distance/unit conversion
- W05: temperature/capacity/volume
- W07: shared instrument topology auditor

Measurement calculations normalize to exact base units before arithmetic.

## 7. Instrument contract

Learner-read geometry is academic data.

Topology families:

- `LINEAR_ENDPOINT_INCLUSIVE`: N intervals, N+1 positions.
- `CYCLIC_FULL_CIRCLE`: N intervals, N unique positions.
- `OPEN_ARC_BOUNDED`: active intervals + endpoint-inclusive active positions; inactive gap has zero value ticks unless defined otherwise.

High-risk item serialization:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

## 8. Render-path contract

Final prompt must contain exactly one of:

`DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

`AUTO` is normalization-only. Unresolved alternatives are invalid.

## 9. One-page contract

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

Correctness, minimum educational geometry, Thai readability, and answer space outrank page count. Locked infeasibility blocks prompt release instead of unsafe compression.

## 10. Measurement expansion ownership

### Time
Clock reading; start/end/duration; schedules; 12/24-hour relations; controlled midnight crossing.

### Length/Distance
Ruler reading; nonzero starts; length sum/difference/comparison; mm/cm/m/km conversion; multi-segment distance; round trip; route comparison.

### Weight
Dial reading; kg/g/ขีด; comparison; arithmetic/conversion.

### Capacity/Volume
mL/L reading/conversion/arithmetic; meniscus; rectangular-prism volume and simple composite volume when grade-appropriate.

Speed/rate is not silently implied by distance.

## 11. Change impact

| Change | Preserve | Rebuild |
|---|---|---|
| Theme | academic state | W08 art/layout language |
| Difficulty/grade | theme where possible | owning academic worker data + layout |
| Count | skill/theme | item distribution + layout |
| Orientation/page lock | academic state | W08 layout |
| Answer key | givens | visibility/output package |
| Unit/range/resolution | context | owning measurement calculations + geometry |
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

Before a downstream image exists, only `PROMPT_*` checks may be PASS.

Always report:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Actual artifact QA begins only after the image/document is supplied.

## 14. LTS maintenance

Baseline 2.6.x reserves Knowledge slot 10 for a narrow hotfix. Broad routing, visibility, worker-schema, or multi-domain academic changes require a new base release rather than accumulating overrides.