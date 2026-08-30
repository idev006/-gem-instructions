# Baseline 2.3.2 Release Checklist

Status: Critical integration checklist
Applies to: `activity-based-elementary-worksheet` Gem baseline 2.3.2

This file ties independent QA suites together. Individual suite version numbers do not need to equal the Gem baseline.

## Required suite set

Before claiming baseline 2.3.2 prompt-generation readiness, apply:

1. `qa/ACCEPTANCE_TESTS.md` — core/domain regression
2. `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md` — prompt-generator contract + KB routing
3. `qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md` — observed high-risk visual failure patterns
4. applicable domain-specific render/regression tests
5. `qa/DOMAIN_RELEASE_MATRIX.md` only when making maturity/release-evidence claims

## Integration gates

All applicable must pass:

`INTENT_QA`
`PARAMETER_QA`
`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`DOMAIN_ROUTE_QA`
`DOMAIN_MATURITY_QA`
`ACADEMIC_QA`
`CALCULATION_QA`
`ANSWER_LEAK_QA`
`TARGET_VALUE_LEAK_QA` when renderer-only targets exist
`VISIBLE_OUTPUT_SANITIZER_QA`
`RENDER_PATH_QA`
`ONE_PAGE_FEASIBILITY_QA`
`LAYOUT_QA`
`READABILITY_QA`
`PROMPT_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`PLACEHOLDER_VISUAL_QA`
`PER_ITEM_RENDER_STATE_QA` for visual questions
`TARGET_REPRESENTABILITY_QA` when applicable
`TARGET_ALIGNMENT_QA` when applicable

Graduated instruments additionally require exact interval/tick/graduation count and no-missing/no-extra QA.

## Core completeness audit

Baseline 2.3.2 specifically protects against accidental core truncation. Verify `GEM_INSTRUCTIONS_PRODUCTION.md` still contains:

- product role + primary deliverable
- full canonical pipeline
- maturity policy
- teacher interaction + parameter policy
- two-view answer separation
- KB/domain routing
- instrument topology rules
- actual-render hardening
- render-path resolution
- one-page policy
- layout engine
- Thai/text policy
- prompt compiler + no-placeholder rule
- render-objective lock
- reference-image policy
- dual leak sanitizer
- QA framework
- downstream artifact-QA distinction
- revision policy
- prompt release contract

Missing a major contract = FAIL.

## KB installation audit

Verify required files from `KB_MANIFEST.md` exist in the Gem installation and routing follows `KB_ROUTER.md`.

For a full supported-domain installation, test at least one request for:

- TIME
- CLOCK
- SCALE
- LENGTH
- TEMPERATURE
- CAPACITY
- MONEY
- CALENDAR
- DATA_READING

## High-risk visual smoke tests

Minimum smoke tests:

- clock 10:30 → hour hand midpoint 10–11, never directly on 10
- discrete thermometer → endpoint exactly on a valid tick
- top/bottom meniscus → designated read point exactly on target graduation with no target-number annotation
- canonical 0–5 kg dial → 300° active + visible 60° inactive gap, no 360° substitution

## Prompt/artifact boundary

Passing this checklist means the **prompt-generation baseline** is internally consistent. It does not mean a third-party rendered worksheet has passed classroom release QA. Actual rendered artifacts must be inspected separately.