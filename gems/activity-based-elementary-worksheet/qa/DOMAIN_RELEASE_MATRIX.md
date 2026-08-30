# Domain Release Matrix

Version: 1.3.0
Status: Release-evidence SSOT

| Domain | Deterministic academic rules | Geometry/data rules | Domain QA | Actual-render evidence | Current overall status |
|---|---:|---:|---:|---:|---|
| TIME | YES / mature | N/A | YES | threshold not yet documented | PRODUCTION_CANDIDATE |
| MEASUREMENT_WEIGHT | YES | YES | YES | 10 deterministic-overlay worksheets; 100/100 dials pass; full hybrid/generative evidence incomplete | PRODUCTION_CANDIDATE |
| TIME_CLOCK | YES | YES | YES | LIMITED | PRODUCTION_CANDIDATE |
| MEASUREMENT_LENGTH | YES | YES | YES | LIMITED | PRODUCTION_CANDIDATE |
| MEASUREMENT_TEMPERATURE | YES | YES | YES | LIMITED | PRODUCTION_CANDIDATE |
| MEASUREMENT_CAPACITY | YES | YES | YES | LIMITED | PRODUCTION_CANDIDATE |
| MONEY | YES | data association rules | YES | LIMITED | PRODUCTION_CANDIDATE |
| CALENDAR | YES | calendar grid rules | YES | LIMITED | PRODUCTION_CANDIDATE |
| DATA_READING | YES | graph/table mapping rules | YES | LIMITED | PRODUCTION_CANDIDATE |
| WORD_PROBLEM_GENERIC | partial by selected skill | varies | core only | not systematic | SUPPORTED_GENERIC |

## Promotion rule

To promote a candidate domain to `PRODUCTION_HARDENED`:

1. all applicable acceptance tests pass;
2. at least 20 diverse dry-run cases pass with zero critical blockers;
3. at least 10 actual rendered worksheets are audited;
4. no unresolved critical academic/geometry/data/layout defect remains;
5. teacher usability examples exist;
6. domain-specific prompt/render patterns are regression-tested;
7. failure/repair examples are documented;
8. one-page policy and render-path behavior are covered by regression for the domain.

For instrument-reading domains, every instructional instrument in the 10 render audits must be inspected individually; one wrong instrument makes that worksheet a failed render case.

For text-heavy/non-instrument domains, actual-render audit still checks page count, Thai/numeral fidelity, exact values, answer leakage, writable response space, cropping, and print usability.

## Academic maturity vs overall maturity

A domain may report:

`ACADEMIC_RULES = DETERMINISTIC_MATURE`

while overall:

`DOMAIN_MATURITY = PRODUCTION_CANDIDATE`

This is valid when calculation/data logic is mature but the complete artifact pipeline has not met release evidence. Do not conflate the two.

## Render-path evidence

Evidence must identify the tested path:

- `DOCUMENT_FIRST`
- `HYBRID`
- `DETERMINISTIC_VECTOR`
- `IMAGE_ONLY`

A strong path does not automatically harden all other paths. Teacher-facing QA may describe a production-ready path while the overall domain remains candidate.

## Demotion rule

A hardened domain is demoted if a newly discovered systemic defect can produce academically wrong or unusable worksheets without being caught by current QA, or if previous maturity cannot be supported by the documented release-evidence rule.

## TIME evidence note

TIME calculation rules are deterministic and mature. However, the matrix does not currently document ≥10 actual rendered worksheet audits under the current output contract, one-page policy, visible-output sanitizer, and render-path policy. Overall TIME status is therefore conservatively `PRODUCTION_CANDIDATE` until that audit is completed.

## MEASUREMENT_WEIGHT evidence

KAN-V2-01 (2026-08-30):

- 10 deterministic rendered worksheets audited;
- 100 instructional dials checked;
- 100/100 pass circle, center pivot, tick count, label count, exact target tick, and minimum-size checks;
- glyph regression found and repaired;
- one nondeterministic render produced an audit dashboard rather than a worksheet, leading to `RENDER_OBJECTIVE_QA` regression coverage;
- deterministic-overlay evidence is strong;
- full hybrid/generative fallback evidence remains incomplete.

See `qa/KAN_V2_01_SCALE_RENDER_AUDIT_2026-08-30.md`.

## v2.2.1 governance repairs

The 2.2.0 professional review identified and repaired:

1. one-page policy conflict between Core, Output Contract, and Instrument Engine;
2. SCALE engine header claiming HARDENED while registry said CANDIDATE;
3. TIME overall HARDENED claim without documented actual-render threshold evidence;
4. version/status drift across canonical files;
5. image-prompt-centric output behavior for text-heavy worksheets;
6. missing explicit render-path QA and page-lock regression.

## Current priority backlog

1. TIME: audit ≥10 actual DOCUMENT_FIRST/HYBRID worksheets under v2.2.1;
2. CLOCK: actual-render regression including DAY_NIGHT_PAIR and one-page layouts;
3. SCALE: full generative-context + deterministic-dial hybrid composite audit;
4. LENGTH: validate minimum printed 1 mm tick spacing;
5. TEMPERATURE/CAPACITY: actual scale/level render audits;
6. DATA_READING: deterministic graph/table overlay audits;
7. reusable SVG reference templates for instrument domains.
