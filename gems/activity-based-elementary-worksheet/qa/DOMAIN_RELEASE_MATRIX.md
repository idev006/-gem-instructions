# Domain Release Matrix

Version: 1.1.0

| Domain | Deterministic academic rules | Geometry/data rules | Domain QA | Post-render evidence | Current status |
|---|---:|---:|---:|---:|---|
| TIME | YES | N/A | YES | YES/dry-run history | PRODUCTION_HARDENED |
| MEASUREMENT_WEIGHT | YES | YES | YES | INSUFFICIENT after newly observed real-render defects; repaired engine awaiting ≥10 clean audited renders | PRODUCTION_CANDIDATE |
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

## Demotion rule

A hardened domain is demoted if a newly discovered systemic defect can produce academically wrong worksheets without being caught by current QA.

This rule was applied to `MEASUREMENT_WEIGHT` after actual examples exposed off-center needles, malformed scales, and layout-induced dial distortion. Documentation repairs do not automatically restore hardened status.

## Current priority backlog

1. produce and audit ≥10 repaired scale-reading renders;
2. strengthen actual-render regression for analog clocks;
3. validate ruler minimum printed tick spacing;
4. validate thermometer/capacity scale rendering;
5. test graph/table deterministic overlays;
6. add automated SVG reference templates for all instrument domains.