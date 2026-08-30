# activity-based-elementary-worksheet

Modular production Gem for primary-school activity-based worksheets.

## Canonical files

- `GEM_INSTRUCTIONS_PRODUCTION.md` — core behavior and release rules
- `ARCHITECTURE.md` — system/process architecture
- `OUTPUT_CONTRACT.md` — output schemas and QA contract
- `USER_GUIDE.md` — teacher-facing guide
- `policies/PARAMETER_POLICY.md` — required/default/auto parameter rules

## Domain engines

- `domains/DOMAIN_REGISTRY.md`
- `domains/INSTRUMENT_READING_ENGINE.md`
- `domains/TIME_ENGINE.md`
- `domains/SCALE_READING_ENGINE.md`
- `domains/CLOCK_READING_ENGINE.md`
- `domains/LENGTH_READING_ENGINE.md`
- `domains/TEMPERATURE_READING_ENGINE.md`
- `domains/CAPACITY_READING_ENGINE.md`
- `domains/MONEY_ENGINE.md`
- `domains/CALENDAR_ENGINE.md`
- `domains/TABLE_GRAPH_READING_ENGINE.md`

## QA

- `qa/ACCEPTANCE_TESTS.md`
- `qa/SCALE_READING_RENDER_TESTS.md`
- `qa/TEACHER_USABILITY_TESTS.md`
- `qa/DOMAIN_RELEASE_MATRIX.md`
- historical dry-run reports remain under `qa/`

## Examples

- `examples/USAGE_EXAMPLES.md`
- `examples/MULTI_DOMAIN_EXAMPLES.md`

## Core product rule

`Correct educational data → verified blueprint → readable layout → controlled rendering → post-render QA`

A visually attractive worksheet that contains an incorrect instrument, graph, value, answer, or unreadable layout is a failed artifact.