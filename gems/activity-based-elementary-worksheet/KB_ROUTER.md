# KB Router — Activity-Based Elementary Worksheet Generator

Version: 1.0.0
Compatible Gem baseline: 2.3.2
Status: Canonical knowledge-routing policy

## 1. Purpose

This file tells the Gem which uploaded Knowledge files are authoritative for each request. Do not treat every KB file as equally relevant. Select the smallest complete dependency set that preserves correctness.

## 2. Always-required KB

Every production request uses:

1. `GEM_INSTRUCTIONS_PRODUCTION.md` — core mission, pipeline, global release rules
2. `OUTPUT_CONTRACT.md` — visible package/final-prompt contract
3. `KB_ROUTER.md` — dependency routing and precedence
4. `KB_MANIFEST.md` — compatibility/version inventory
5. `policies/PARAMETER_POLICY.md` — normalization/default policy
6. `domains/DOMAIN_REGISTRY.md` — domain routing + overall maturity SSOT

If any required file is missing or known incompatible, set `KB_COMPATIBILITY_QA=FAIL` and do not claim production-ready prompt release.

## 3. Domain route table

| Detected domain | Load/apply |
|---|---|
| TIME | `domains/TIME_ENGINE.md` |
| TIME_CLOCK | `domains/CLOCK_READING_ENGINE.md` + `domains/INSTRUMENT_READING_ENGINE.md` |
| MEASUREMENT_WEIGHT | `domains/SCALE_READING_ENGINE.md` + `domains/INSTRUMENT_READING_ENGINE.md` |
| MEASUREMENT_LENGTH | `domains/LENGTH_READING_ENGINE.md` + `domains/INSTRUMENT_READING_ENGINE.md` |
| MEASUREMENT_TEMPERATURE | `domains/TEMPERATURE_READING_ENGINE.md` + `domains/INSTRUMENT_READING_ENGINE.md` |
| MEASUREMENT_CAPACITY | `domains/CAPACITY_READING_ENGINE.md` + `domains/INSTRUMENT_READING_ENGINE.md` |
| MONEY | `domains/MONEY_ENGINE.md` |
| CALENDAR | `domains/CALENDAR_ENGINE.md` |
| DATA_READING | `domains/TABLE_GRAPH_READING_ENGINE.md` |
| WORD_PROBLEM_GENERIC | core files only unless another domain is actually present |

## 4. Conditional QA KB

Always apply:

- `qa/ACCEPTANCE_TESTS.md`
- `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md`

Apply `qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md` whenever the request contains a learner-read visual instrument or any failure family covered by that suite.

Apply domain-specific render/regression files when they exist and match the selected domain, e.g. scale-reading render tests for `MEASUREMENT_WEIGHT`.

`qa/DOMAIN_RELEASE_MATRIX.md` is required whenever maturity/release-readiness is reported.

## 5. Routing sequence

Use this order:

`REQUEST → CORE/PARAMETER POLICY → DOMAIN_REGISTRY → SELECT DOMAIN ENGINE(S) → INSTRUMENT ENGINE IF REQUIRED → SELECT QA/REGRESSION KB → COMPILE/QA`

Do not ask the teacher to choose technical engine filenames when the domain is unambiguous.

## 6. Precedence rules

When rules conflict, use this precedence:

1. explicit valid user requirement, unless academically unsafe or contradictory
2. `GEM_INSTRUCTIONS_PRODUCTION.md` for product mission/global safety
3. `domains/DOMAIN_REGISTRY.md` for domain route and overall maturity
4. selected domain engine for domain-specific academic rules
5. `domains/INSTRUMENT_READING_ENGINE.md` for cross-instrument geometry rules
6. `policies/PARAMETER_POLICY.md` for defaults/normalization
7. `OUTPUT_CONTRACT.md` for visible packaging/final-prompt serialization
8. applicable QA/regression suites for release gating
9. `USER_GUIDE.md` / README for explanatory guidance only

Special rule: if a domain engine and `DOMAIN_REGISTRY.md` disagree on overall maturity, the registry wins.

Special rule: QA/regression files may make a release condition stricter; they do not redefine academic formulas owned by the domain engine.

## 7. Mixed-domain requests

If a worksheet genuinely combines multiple domains:

- select every necessary domain engine;
- include `INSTRUMENT_READING_ENGINE.md` if any selected domain is a visual instrument;
- keep one canonical normalized spec;
- validate each item against its owning domain;
- run all applicable QA suites;
- do not let one domain's defaults silently overwrite another's units/geometry.

If mixed-domain complexity threatens readability or one-page feasibility, correctness/readability outrank one-page density.

## 8. High-risk visual route

For clocks, dial scales, rulers, thermometers, capacity vessels, and educational graphs whose visual state encodes the question:

`PER_ITEM_RENDER_STATE_REQUIRED=YES`
`TARGET_ALIGNMENT_REQUIRED=YES`

Each item state must serialize:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`.

## 9. KB routing QA

`KB_ROUTE_QA=PASS` only if:

- primary domain is correctly selected;
- all required engines are available;
- visual instrument tasks include the instrument engine;
- applicable QA/regression KB is selected;
- no irrelevant engine overrides the selected domain;
- precedence is respected.

`KB_COMPATIBILITY_QA=PASS` only if the installed file set is compatible according to `KB_MANIFEST.md`.