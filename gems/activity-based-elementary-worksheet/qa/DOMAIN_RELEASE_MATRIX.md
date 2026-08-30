# Domain Release Matrix

Version: 1.2.0

| Domain | Deterministic academic rules | Geometry/data rules | Domain QA | Post-render evidence | Current status |
|---|---:|---:|---:|---:|---|
| TIME | YES | N/A | YES | YES/dry-run history | PRODUCTION_HARDENED |
| MEASUREMENT_WEIGHT | YES | YES | YES | 10/10 deterministic-overlay worksheets audited; 100/100 dials pass critical geometry; generative-only objective failure still open as fallback evidence | PRODUCTION_CANDIDATE |
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

1. all acceptance tests pass;
2. at least 20 diverse dry-run cases pass with zero critical blockers;
3. at least 10 actual rendered worksheets are visually audited;
4. no unresolved critical geometry/data defect remains;
5. teacher usability examples exist;
6. domain-specific prompt patterns are regression-tested;
7. failure/repair examples are documented.

For instrument-reading domains, the 10 render audits must inspect every instructional instrument individually; one wrong instrument makes that worksheet a failed render case.

For domains that use multiple rendering paths, hardened status should identify which path is hardened. A deterministic-overlay path may be production-ready even while a generative-only fallback remains candidate; do not imply equivalent reliability.

## Demotion rule

A hardened domain is demoted if a newly discovered systemic defect can produce academically wrong worksheets without being caught by current QA.

This rule was applied to `MEASUREMENT_WEIGHT` after actual examples exposed off-center needles, malformed scales, and layout-induced dial distortion. Documentation repairs alone do not restore hardened status.

## Current MEASUREMENT_WEIGHT evidence

KAN-V2-01 (2026-08-30):

- 10 deterministic rendered worksheets audited;
- 100 instructional dials inspected through programmatic geometry checks plus visual contact-sheet review;
- 100/100 pass circle, center pivot, tick count, label count, exact target tick, and minimum-size checks;
- text glyph regression found and repaired;
- one nondeterministic render produced an audit dashboard rather than student worksheets, creating a new `RENDER_OBJECTIVE_QA` blocker and regression test;
- deterministic-overlay path evidence is strong; generative-only fallback remains unproven.

See `qa/KAN_V2_01_SCALE_RENDER_AUDIT_2026-08-30.md`.

## Current priority backlog

1. KAN-V2-01E: full generative-context art + deterministic-dial composite audit;
2. strengthen actual-render regression for analog clocks;
3. validate ruler minimum printed tick spacing;
4. validate thermometer/capacity scale rendering;
5. test graph/table deterministic overlays;
6. add reusable SVG reference templates for all instrument domains.