# Domain Release Matrix

Version: 1.0.0

| Domain | Deterministic academic rules | Geometry/data rules | Domain QA | Post-render evidence | Current status |
|---|---:|---:|---:|---:|---|
| TIME | YES | N/A | YES | YES/dry-run history | PRODUCTION_HARDENED |
| MEASUREMENT_WEIGHT | YES | YES | YES | YES + scale regressions required continuously | PRODUCTION_HARDENED |
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

## Demotion rule

A hardened domain is demoted if a newly discovered systemic defect can produce academically wrong worksheets without being caught by current QA.

## Current priority backlog

1. strengthen actual-render regression for analog clocks;
2. validate ruler minimum printed tick spacing;
3. validate thermometer/capacity scale rendering;
4. test graph/table deterministic overlays;
5. add automated SVG reference templates for all instrument domains.