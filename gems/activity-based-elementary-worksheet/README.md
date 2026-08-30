# activity-based-elementary-worksheet

Version: 2.3.2

Modular production Gem for generating **copy-ready worksheet image prompts** for primary-school learning materials.

## Product role

`PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

Primary deliverable:

`FINAL_IMAGE_GENERATION_PROMPT`

The Gem verifies educational content, geometry, layout, and prompt completeness, then outputs a self-contained prompt for a downstream AI/image-generation system. It does not need to render the worksheet image itself.

## Canonical files

- `GEM_INSTRUCTIONS_PRODUCTION.md` — main Gem Instructions / full production core
- `OUTPUT_CONTRACT.md` — visible package and final-prompt contract
- `ARCHITECTURE.md` — system/process architecture
- `KB_ROUTER.md` — selects required KB by domain and defines precedence
- `KB_MANIFEST.md` — installation/version compatibility inventory
- `policies/PARAMETER_POLICY.md` — required/default/auto parameter rules
- `domains/DOMAIN_REGISTRY.md` — SSOT for routing and overall domain maturity
- `qa/DOMAIN_RELEASE_MATRIX.md` — SSOT for maturity promotion evidence
- `USER_GUIDE.md` — teacher-facing guide
- `GEM_INSTALLATION_GUIDE.md` — Gem installation steps

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

## KB routing

Use `GEM_INSTRUCTIONS_PRODUCTION.md` as the primary Gem Instructions. Upload supporting Knowledge according to `KB_MANIFEST.md`. The Gem selects applicable domain/QA files according to `KB_ROUTER.md`.

Visual instrument domains always require `INSTRUMENT_READING_ENGINE.md` in addition to the selected domain engine.

## Global product behavior

Default page intent:

`A4 → PORTRAIT → ONE_PAGE_PREFERRED=YES → TARGET_PAGE_COUNT=1`

Default output:

`OUTPUT_MODE=PROMPT_PACKAGE → PRIMARY_DELIVERABLE=FINAL_IMAGE_GENERATION_PROMPT`

Render strategy is content-aware:

`RENDER_PATH=AUTO → DOCUMENT_FIRST | HYBRID | DETERMINISTIC_VECTOR | IMAGE_ONLY`

Render path is guidance for the downstream AI, not a requirement that this Gem produce image pixels itself.

## Actual-render hardening

For high-risk visual questions the final prompt must serialize:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Current observed failure guards include:

- clock: continuous hour-hand interpolation, especially :30 midpoint;
- thermometer: exact target-tick alignment, no accidental between-tick endpoint;
- capacity: explicit top/bottom meniscus read point + target-value leak guard;
- canonical 0–5 kg dial: 300° active sweep + visible 60° inactive gap, no 360° substitution.

## QA

Core suite set:

- `qa/ACCEPTANCE_TESTS.md`
- `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md`
- `qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md`
- `qa/BASELINE_2_3_2_RELEASE_CHECKLIST.md`
- `qa/DOMAIN_RELEASE_MATRIX.md`
- applicable domain-specific render tests

Important distinction:

`PROMPT_QA != ARTIFACT_QA`

A prompt may be internally correct while a nondeterministic downstream image generator still produces a wrong hand, needle, graduation, liquid level, or Thai glyph. Classroom use therefore requires inspection of the actual rendered worksheet.

## Core rule

`Correct educational data → correct KB/domain route → verified internal blueprint → sanitized student blueprint → render-path selection → one-page feasibility → readable layout → exact per-item renderer state → copy-ready final prompt → downstream artifact inspection`

A visually attractive prompt or worksheet that contains an incorrect value, leaked answer/target, wrong instrument geometry, missing/extra graduation, or unsafe compression is a failed educational product.