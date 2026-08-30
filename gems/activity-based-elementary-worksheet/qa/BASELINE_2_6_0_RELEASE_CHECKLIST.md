# Baseline 2.6.0-LTS Release Checklist

Status: Critical integration checklist
Applies to: `activity-based-elementary-worksheet` baseline 2.6.x

## Required SSOT set

- `GEM_INSTRUCTIONS_PRODUCTION.md` — 2.6.0-LTS
- `OUTPUT_CONTRACT.md` — 2.6.0-LTS
- `ARCHITECTURE.md` — 2.6.0-LTS
- `KB_ROUTER.md` — 2.6.0-LTS
- `KB_MANIFEST.md` — 2.6.0-LTS
- `policies/PARAMETER_POLICY.md` — 2.6.0-LTS
- `domains/DOMAIN_REGISTRY.md` — 2.6.0-LTS
- `domains/MEASUREMENT_COVERAGE_P1_P6.md`
- W01..W09 worker contracts
- `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md`
- `qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md`
- applicable older actual-render regressions

## Worker audit

Exactly 9 base workers:

`W01_ACADEMIC_CONTENT`
`W02_TIME_CLOCK`
`W03_WEIGHT_SCALE`
`W04_LENGTH_DISTANCE`
`W05_TEMPERATURE_CAPACITY_VOLUME`
`W06_MONEY_CALENDAR_DATA`
`W07_INSTRUMENT_AUDITOR`
`W08_LAYOUT_RENDER_THAI`
`W09_QA_RELEASE`

Each declares:

`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

Worker IDs must be unique.

## Core architecture audit

Verify core contains:

- Orchestrator role
- worker-routing model
- worker ownership contract
- three visibility scopes
- Student Blueprint target-leak prohibition
- measurement coverage
- exact unit conversion rules
- high-risk visual serialization
- canonical-label preservation
- single render-path rule
- one-page-first policy
- Thai/theme policy
- answer-key behavior
- prompt/artifact QA distinction
- health check
- hotfix slot 10 policy

Missing a major contract = FAIL.

## Measurement audit

Verify deterministic rules for:

- clock reading
- elapsed time
- ruler zero/nonzero start
- length arithmetic/conversion
- distance total/difference/round trip/multi-segment
- weight arithmetic/conversion
- canonical dial topology
- thermometer representability/alignment specification
- mL/L arithmetic/conversion
- meniscus convention
- rectangular-prism volume
- simple composite rectangular-prism volume

## Required integration gates

`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`WORKER_OWNERSHIP_QA`
`PROMPT_ACADEMIC_DATA_QA`
`PROMPT_UNIT_COMPATIBILITY_QA` when applicable
`PROMPT_UNIT_CONVERSION_QA` when applicable
`RENDER_PATH_RESOLVED_QA`
`PROMPT_ONE_PAGE_FEASIBILITY_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`NO_PLACEHOLDER_QA`
`STUDENT_VISIBLE_ANSWER_LEAK_QA`
`STUDENT_VISIBLE_TARGET_TEXT_LEAK_QA`
`CANONICAL_LABEL_PRESERVATION_QA`
plus all owning-worker/domain gates.

## High-risk smoke tests

1. 10:30 clock → minute 180°, hour 315°, midpoint 10–11, not on 10.
2. Canonical 0–5 kg dial → 300° active +60° gap, 50/51 topology, no 360° substitution.
3. Ruler 1 cm @1 mm → 10 intervals/11 positions.
4. Nonzero ruler start → `end-start`.
5. Distance round trip → double only when same route is explicit.
6. 20–120°F @2°F → only 20+2k discrete targets.
7. Bottom/top meniscus → designated read point exact and no target-number annotation.
8. Rectangular prism → compatible units before `l×w×h`.
9. Student Blueprint → no renderer target values.
10. Final prompt → one resolved render path.

## Prompt/artifact boundary

Passing this checklist means the **prompt-generation baseline** is internally coherent.

It does not mean third-party rendered worksheets are classroom-ready.

Before artifact inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

## Installation package audit

Compact package must contain:

- one main Instructions `.txt`
- exactly nine worker `.txt` Knowledge files
- no `.md` dependency required for Gemini upload
- install/health-check guide
- smoke tests
- static lint report
- checksum manifest

Knowledge slot 10 remains free unless an approved narrow hotfix is shipped.

## Release decision

Baseline 2.6.0 prompt-generation release may be marked READY only when static consistency, worker compatibility, regression suite, package integrity and SSOT/package coherence pass with zero critical blockers.