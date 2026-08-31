# Domain Release Matrix

Version: 1.6.0
Compatible Gem baseline: 2.6.x
Status: Release-evidence SSOT

| Domain | Deterministic academic rules | Geometry/data rules | Domain QA | Actual-render evidence | Current overall status |
|---|---:|---:|---:|---:|---|
| ACADEMIC_CONTENT | YES for supported arithmetic/literacy branches | varies | YES | not systematic | PRODUCTION_CANDIDATE |
| TIME | YES / mature | N/A | YES | threshold not yet documented under 2.6.x | PRODUCTION_CANDIDATE |
| TIME_CLOCK | YES | YES | YES | LIMITED | PRODUCTION_CANDIDATE |
| MEASUREMENT_WEIGHT | YES | YES | YES | 10 deterministic-overlay worksheets; 100/100 dials pass; full hybrid/generative evidence incomplete | PRODUCTION_CANDIDATE |
| MEASUREMENT_LENGTH | YES | YES | YES | LIMITED; actual 2026-08-31 extra-tick ruler defect recorded and converted to regression | PRODUCTION_CANDIDATE |
| MEASUREMENT_DISTANCE | YES | contextual geometry optional | YES | no systematic 2.6 artifact audit yet | PRODUCTION_CANDIDATE |
| MEASUREMENT_SPEEDOMETER | YES for direct dial reading | YES, open-arc scale + needle | YES | no systematic actual-render audit yet | PRODUCTION_CANDIDATE |
| MEASUREMENT_ANGLE | YES | YES for protractor | YES | no systematic 2.6 artifact audit yet | PRODUCTION_CANDIDATE |
| MEASUREMENT_PERIMETER_AREA | YES for supported figure grammar | diagram/data rules | YES | no systematic 2.6 artifact audit yet | PRODUCTION_CANDIDATE |
| MEASUREMENT_TEMPERATURE | YES | YES | YES | LIMITED; renderer review/revise hardening added in 2.6.2 | PRODUCTION_CANDIDATE |
| MEASUREMENT_CAPACITY | YES | YES | YES | LIMITED | PRODUCTION_CANDIDATE |
| MEASUREMENT_VOLUME | YES for rectangular-prism/simple composite grammar | diagram/data rules | YES | no systematic 2.6 artifact audit yet | PRODUCTION_CANDIDATE |
| MONEY | YES | data association rules | YES | LIMITED | PRODUCTION_CANDIDATE |
| CALENDAR | YES | calendar grid rules | YES | LIMITED | PRODUCTION_CANDIDATE |
| DATA_READING | YES | graph/table mapping rules | YES | LIMITED; scale-line integrity applies to learner-read axes | PRODUCTION_CANDIDATE |
| WORD_PROBLEM_GENERIC | partial by selected skill | varies | core only | not systematic | SUPPORTED_GENERIC |

## Promotion rule

To promote a candidate domain to `PRODUCTION_HARDENED`:

1. all applicable acceptance/regression tests pass;
2. at least 20 diverse dry-run cases pass with zero critical blockers;
3. at least 10 actual rendered worksheets are audited for the claimed render path;
4. no unresolved critical academic/geometry/data/layout defect remains;
5. teacher usability examples exist;
6. domain-specific prompt/render patterns are regression-tested;
7. failure/repair examples are documented;
8. one-page policy and render-path behavior are covered by regression.

For instrument-reading domains, every instructional instrument in the 10 render audits must be inspected individually. One wrong instrument makes that worksheet a failed render case.

Renderer-side self-review/revise is required as a prevention layer for learner-read instruments but does not count as actual-render evidence.

## Academic maturity vs overall maturity

Do not conflate:

`PROMPT/ACADEMIC RULE MATURITY`
with
`OVERALL DOMAIN MATURITY`
with
`ARTIFACT RELEASE STATUS`.

A domain can have deterministic rules while remaining `PRODUCTION_CANDIDATE` because artifact evidence is incomplete.

## Render-path evidence

Evidence must name the tested path:

- `DOCUMENT_FIRST`
- `HYBRID`
- `DETERMINISTIC_VECTOR`
- `IMAGE_ONLY`

A strong path does not harden untested paths automatically.

## Demotion rule

A hardened domain is demoted if a new systemic defect can produce academically wrong/unusable output without being caught by current QA, or if claimed maturity cannot be supported by documented evidence.

## Existing weight evidence

KAN-V2-01 (2026-08-30):

- 10 deterministic rendered worksheets audited;
- 100 instructional dials checked;
- 100/100 passed circle, center pivot, tick count, label count, target tick and minimum-size checks for that tested path;
- glyph regression was found/repaired;
- one nondeterministic render produced an audit dashboard rather than a worksheet, motivating `RENDER_OBJECTIVE_QA` coverage;
- deterministic-overlay evidence is strong;
- full hybrid/generative fallback evidence remains incomplete.

See `qa/KAN_V2_01_SCALE_RENDER_AUDIT_2026-08-30.md`.

## 2.6.2 instrument-safety evidence

### Ruler actual-render regression

A user-supplied 2026-08-31 artifact showed too many graduation lines in a 1 cm span at 1 mm resolution. The defect is classified `CRITICAL_ACADEMIC` and documented in:

`qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md`

Canonical oracle:

- 10 intervals per cm;
- 11 endpoint-inclusive positions;
- 9 interior positions;
- physical ruler edge is not a graduation.

This actual defect does not harden the domain; it provides negative evidence and a permanent regression requirement.

### Speedometer

`SPEEDOMETER_READING_ENGINE.md` adds deterministic direct speedometer reading in 2.6.2. Prompt/regression evidence exists, but no production-hardening claim is allowed until ≥10 actual rendered worksheets for the claimed render path pass instrument-by-instrument inspection.

### Thermometer

2.6.2 strengthens exact graduation topology, representability, endpoint alignment and mandatory renderer review/revise. Artifact maturity remains LIMITED until the promotion threshold is met.

## Baseline 2.6 expansion evidence note

The following capabilities have deterministic prompt rules/regressions but must not be promoted solely from documentation changes:

- seconds/time conversion tasks
- mixed-unit length conversion/arithmetic
- nonzero ruler starts and 1 mm subdivision integrity
- multi-segment/round-trip/route-comparison distance
- direct speedometer reading
- angle/protractor reading
- perimeter/area/circle measurement and squared-unit conversion
- weight arithmetic/conversion
- thermometer reading
- capacity arithmetic/conversion/meniscus
- rectangular-prism/simple composite volume
- cubic-unit conversion/capacity-volume relations
- learner-read graph axes

They remain `PRODUCTION_CANDIDATE` until promotion evidence is recorded.

## Current priority backlog

1. LENGTH: audit ≥10 actual ruler worksheets, including 1 mm subdivisions and explicit recount of 10 intervals /11 positions /9 interior positions.
2. SPEEDOMETER: audit ≥10 actual open-arc speedometer worksheets, including major/minor ticks, inactive gap and needle alignment.
3. TEMPERATURE: audit ≥10 actual thermometer worksheets across canonical profiles and endpoint positions.
4. CLOCK: actual-render audit including half-hour, 5-minute and DAY_NIGHT_PAIR cases.
5. SCALE: full hybrid generative-context + deterministic-dial audit.
6. ANGLE: 10 protractor worksheets covering baseline/direction/dual-scale ambiguity.
7. CAPACITY: actual graduation/level/meniscus audits.
8. DATA_READING: deterministic graph-axis/table overlay audits.
9. TIME/DISTANCE/PERIMETER/AREA/VOLUME: complete path-specific artifact evidence thresholds.
10. reusable deterministic reference templates for every learner-read instrument.
