# Domain Release Matrix

Version: 1.4.0
Compatible Gem baseline: 2.6.x
Status: Release-evidence SSOT

| Domain | Deterministic academic rules | Geometry/data rules | Domain QA | Actual-render evidence | Current overall status |
|---|---:|---:|---:|---:|---|
| ACADEMIC_CONTENT | YES for supported arithmetic/literacy branches | varies | YES | not systematic | PRODUCTION_CANDIDATE |
| TIME | YES / mature | N/A | YES | threshold not yet documented under 2.6.x | PRODUCTION_CANDIDATE |
| TIME_CLOCK | YES | YES | YES | LIMITED | PRODUCTION_CANDIDATE |
| MEASUREMENT_WEIGHT | YES | YES | YES | 10 deterministic-overlay worksheets; 100/100 dials pass; full hybrid/generative evidence incomplete | PRODUCTION_CANDIDATE |
| MEASUREMENT_LENGTH | YES | YES | YES | LIMITED; 2.6 nonzero-start/conversion expansion not yet fully audited | PRODUCTION_CANDIDATE |
| MEASUREMENT_DISTANCE | YES | contextual geometry optional | YES | no systematic 2.6 artifact audit yet | PRODUCTION_CANDIDATE |
| MEASUREMENT_TEMPERATURE | YES | YES | YES | LIMITED | PRODUCTION_CANDIDATE |
| MEASUREMENT_CAPACITY | YES | YES | YES | LIMITED | PRODUCTION_CANDIDATE |
| MEASUREMENT_VOLUME | YES for rectangular-prism/simple composite grammar | diagram/data rules | YES | no systematic 2.6 artifact audit yet | PRODUCTION_CANDIDATE |
| MONEY | YES | data association rules | YES | LIMITED | PRODUCTION_CANDIDATE |
| CALENDAR | YES | calendar grid rules | YES | LIMITED | PRODUCTION_CANDIDATE |
| DATA_READING | YES | graph/table mapping rules | YES | LIMITED | PRODUCTION_CANDIDATE |
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

For instrument-reading domains, every instructional instrument in the 10 render audits must be inspected individually; one wrong instrument makes that worksheet a failed render case.

For text-heavy/calculation domains, artifact audit checks page count, Thai/numeral fidelity, exact values/givens, answer leakage, writable response space, cropping and print usability.

## Academic maturity vs overall maturity

A domain may have deterministic mature academic rules while overall status remains `PRODUCTION_CANDIDATE` because artifact evidence is incomplete.

Do not conflate:

`PROMPT/ACADEMIC RULE MATURITY`
with
`OVERALL DOMAIN MATURITY`
with
`ARTIFACT RELEASE STATUS`.

## Render-path evidence

Evidence must name the tested path:

- `DOCUMENT_FIRST`
- `HYBRID`
- `DETERMINISTIC_VECTOR`
- `IMAGE_ONLY`

A strong path does not harden untested paths automatically.

## Demotion rule

A hardened domain is demoted if a new systemic defect can produce academically wrong/unusable output without being caught by current QA, or if the claimed maturity cannot be supported by documented evidence.

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

## Baseline 2.6 expansion evidence note

The following 2.6 capabilities have deterministic prompt rules/regressions but **must not be promoted solely from documentation changes**:

- mixed-unit length conversion/arithmetic
- nonzero ruler starts
- multi-segment/round-trip/route-comparison distance
- weight arithmetic/conversion
- capacity arithmetic/conversion
- rectangular-prism/simple composite rectangular-prism volume

They remain `PRODUCTION_CANDIDATE` until the promotion evidence above is recorded.

## Current priority backlog

1. TIME: audit ≥10 actual DOCUMENT_FIRST/HYBRID worksheets under 2.6.x.
2. CLOCK: actual-render audit including half-hour, 5-minute and DAY_NIGHT_PAIR cases.
3. SCALE: full hybrid generative-context + deterministic-dial audit.
4. LENGTH: print/audit ruler 1 mm spacing, zero/nonzero starts and mixed-unit prompt outputs.
5. DISTANCE: audit 10 text/document worksheets including asymmetric round trips and route comparison.
6. TEMPERATURE/CAPACITY: actual graduation/level/meniscus audits.
7. VOLUME: audit diagrams, dimension-label fidelity and composite decomposition prompts/artifacts.
8. DATA_READING: deterministic graph/table overlay audits.
9. reusable deterministic reference templates for learner-read instruments.