# activity-based-elementary-worksheet

Version: 2.2.1

Modular production Gem for primary-school activity-based worksheets.

## Canonical files

- `GEM_INSTRUCTIONS_PRODUCTION.md` — core behavior, global one-page policy, render-path policy, release rules
- `ARCHITECTURE.md` — system/process architecture
- `OUTPUT_CONTRACT.md` — output schemas, visible-output sanitizer, render/page QA contract
- `USER_GUIDE.md` — teacher-facing guide
- `policies/PARAMETER_POLICY.md` — required/default/auto parameter rules
- `domains/DOMAIN_REGISTRY.md` — SSOT for routing and overall domain maturity
- `qa/DOMAIN_RELEASE_MATRIX.md` — SSOT for promotion evidence

## Domain engines

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

## Global product behavior

Default page intent:

`A4 → PORTRAIT → ONE_PAGE_PREFERRED=YES → TARGET_PAGE_COUNT=1`

The Gem attempts a readable one-page solution before pagination. Explicit `1 หน้าเท่านั้น` sets `ONE_PAGE_LOCK=ON`; if impossible without violating readability/correctness, the artifact fails safely instead of silently shrinking or creating page 2.

Render strategy is content-aware:

`RENDER_PATH=AUTO → DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

Text-heavy Thai worksheets must not default to image-only rendering. Exact measurement/graph geometry should use deterministic geometry when possible.

## Important clock mode

`CLOCK_READING_MODE=DAY_NIGHT_PAIR` supports:

`1 question = 1 analog clock + 2 blank answers (กลางวัน / กลางคืน)`

Day/night 24-hour values are computed internally and remain hidden when the answer key is off.

## QA

- `qa/ACCEPTANCE_TESTS.md`
- `qa/SCALE_READING_RENDER_TESTS.md`
- `qa/TEACHER_USABILITY_TESTS.md`
- `qa/DOMAIN_RELEASE_MATRIX.md`
- professional review and historical dry-run reports under `qa/`

Overall maturity must come from `domains/DOMAIN_REGISTRY.md`. A domain may have mature deterministic academic rules while its overall artifact pipeline remains `PRODUCTION_CANDIDATE` until release evidence is complete.

## Core product rule

`Correct educational data → verified internal blueprint → sanitized student blueprint → render-path selection → one-page feasibility → readable layout → controlled rendering → visible-output sanitizer → post-render QA`

A visually attractive worksheet that contains an incorrect value, leaked answer, wrong instrument/graph, unreadable layout, or unsafe page compression is a failed artifact.
