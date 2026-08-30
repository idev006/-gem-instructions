# Architecture — Activity-Based Elementary Worksheet Generator

Version: 2.3.2
Status: Production prompt-generator architecture reference

## 1. System model

The Gem is organized as nine cooperating layers:

1. `INTERACTION_LAYER` — understands teacher language and asks minimal clarifications.
2. `NORMALIZATION_LAYER` — resolves required/default/auto parameters.
3. `KB_ROUTING_LAYER` — selects mandatory core, domain, instrument, policy, and QA knowledge files; checks compatibility.
4. `DOMAIN_LAYER` — generates and validates academic data.
5. `BLUEPRINT_LAYER` — separates internal verified data from student-facing data.
6. `RENDER_PATH_LAYER` — selects downstream DOCUMENT_FIRST, HYBRID, DETERMINISTIC_VECTOR, or IMAGE_ONLY architecture.
7. `ONE_PAGE_LAYOUT_LAYER` — attempts a valid one-page solution, then resolves pagination/lock behavior.
8. `PROMPT_COMPILER_LAYER` — serializes exact content, layout, visual geometry, art constraints, hard negatives, and per-item renderer states into a self-contained downstream image-generation prompt.
9. `QA_RELEASE_LAYER` — sanitizes visible output, checks KB compatibility, prompt completeness/copy-readiness, and blocks unsafe or incomplete prompt release.

The Gem's production endpoint is the prompt, not the final rendered pixels.

## 2. Canonical state objects

### REQUEST_CONTEXT
Raw teacher request + references + revision instructions.

### NORMALIZED_WORKSHEET_SPEC
Single source of truth for all resolved parameters, including `DOMAIN`, `DOMAIN_MATURITY`, `RENDER_PATH`, `ONE_PAGE_PREFERRED`, `ONE_PAGE_LOCK`, target page count, and `OUTPUT_MODE`.

### KB_ROUTE_DECISION
Selected knowledge dependencies, precedence, compatibility result, and affected QA suites. Built from `KB_ROUTER.md` + `KB_MANIFEST.md` + `domains/DOMAIN_REGISTRY.md`.

### INTERNAL_VERIFIED_BLUEPRINT
Hidden academic content, verified answers, formulas, target geometry/data relations, IDs, and QA metadata.

### STUDENT_RENDER_BLUEPRINT
Sanitized student-visible givens, required diagrams/instruments, blank response areas, and renderer-only geometry references that must not appear as answer or target-value text.

### RENDER_PATH_DECISION
Resolved downstream rendering architecture and rationale:

- `DOCUMENT_FIRST`
- `HYBRID`
- `DETERMINISTIC_VECTOR`
- `IMAGE_ONLY`

### LAYOUT_BLUEPRINT
Page regions, one-page feasibility result, repeated-card/table geometry, minimum sizes, text/art zones, and pagination fallback when unlocked.

### RENDER_PLAN
Deterministic text/data/geometry instructions, optional generative-art instructions, composition order, locks, hard negatives, and per-item visual states.

### FINAL_IMAGE_GENERATION_PROMPT
Primary user deliverable. One consolidated, self-contained prompt that can be copied directly into a downstream AI/image-generation system without relying on hidden state or other sections.

### QA_REPORT
Global + domain-specific gate status, KB compatibility, registry maturity, render-path status, one-page status, prompt completeness, copy-readiness, target-leak status, placeholder status, and release decision.

## 3. Canonical process

`Teacher request`
→ parse explicit requirements
→ normalize parameters
→ resolve KB route/compatibility
→ detect domain
→ generate academic targets
→ derive source values/diagram geometry
→ independently validate
→ build internal verified blueprint
→ sanitize student view
→ resolve downstream render path
→ run one-page feasibility
→ build layout
→ create render plan
→ serialize every visual item with redundant state
→ compile final image-generation prompt
→ prompt completeness/copy-readiness checks
→ dual leak sanitizer
→ pre-release QA
→ release prompt
→ downstream render occurs outside the Gem
→ optional post-render QA/evidence

## 4. Product boundary

Default role:

`PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

Default output:

`OUTPUT_MODE=PROMPT_PACKAGE`
`PRIMARY_DELIVERABLE=FINAL_IMAGE_GENERATION_PROMPT`

The Gem must not confuse a worksheet content preview with the final deliverable. A Markdown table or placeholder description can be useful as an intermediate blueprint, but default production output is incomplete until the final copy-ready prompt is emitted.

`PROMPT_ONLY` may suppress supporting sections while retaining all hidden validation. `BLUEPRINT_ONLY` is explicit opt-in only.

## 5. KB routing contract

Mandatory core references:

- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `OUTPUT_CONTRACT.md`
- `KB_ROUTER.md`
- `KB_MANIFEST.md`
- `policies/PARAMETER_POLICY.md`
- `domains/DOMAIN_REGISTRY.md`

Conditional references are selected by domain. Visual instrument domains additionally require `domains/INSTRUMENT_READING_ENGINE.md`. QA suites are selected by task risk and domain.

Precedence is defined in `KB_ROUTER.md`; compatibility is defined in `KB_MANIFEST.md`. The registry remains SSOT for domain maturity.

## 6. Domain plugin contract

Every domain engine should define:

- trigger phrases / routing
- learning-objective patterns
- parameters/defaults
- deterministic formulas/rules
- valid/invalid invariants
- content-generation strategy
- internal/student schemas
- layout minimums
- preferred downstream render paths
- prompt-serialization constraints
- domain QA gates
- hard negatives
- maturity evidence dependencies

The overall maturity value comes from `domains/DOMAIN_REGISTRY.md`, not from an engine's self-description.

## 7. Instrument plugin contract

Instrument domains additionally define:

- canonical template geometry
- scale/tick topology and mapping
- target-to-geometry transformation
- exact target representability rules
- minimum printed size
- template lock
- one-page footprint constraints
- deterministic-vector/hybrid preference
- per-item prompt serialization schema
- downstream post-render inspection rubric

Educational geometry outranks theme art and one-page density.

Every high-risk visual item serializes:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`.

## 8. Final-prompt contract

The final prompt must be self-contained. A downstream renderer must not need to read earlier Gem sections.

Mandatory characteristics:

- exact page size/orientation/color mode;
- exact question count;
- exact student-visible text/data;
- explicit layout structure;
- exact blank answer formats;
- per-item visual state for every visual question;
- canonical instrument/graph template when applicable;
- renderer geometry/topology and minimum-size constraints;
- target alignment/representability rules;
- theme/art instructions separated from academic geometry;
- Thai/numeric fidelity locks;
- hard negatives;
- no solved answer key unless requested;
- no target-value leakage;
- no pseudo-image placeholders.

Repeated visual objects compile as:

`CANONICAL TEMPLATE + ITEM 1 STATE + ITEM 2 STATE + ... + ITEM N STATE`

not as vague prose placeholders.

## 9. Actual-render failure classes

Observed downstream failure patterns are treated as architecture-level risks:

- clock: nonzero-minute hour hand pinned to hour numeral; :30 not midpoint;
- thermometer: liquid endpoint between discrete ticks;
- capacity: wrong/ambiguous meniscus read point or target-number annotation;
- canonical 0–5 kg dial: full-circle 360° substitution or ticks through inactive gap.

Applicable prompts must encode both positive geometry and explicit negative constraints. See `qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md`.

## 10. Global one-page contract

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

The system attempts a valid one-page layout plan before pagination.

Optimization may reduce only nonessential layout cost. It may not trade away academic correctness, requested question count, domain minimum size, readable text, required answer fields, safe margins, answer integrity, or graduation count/topology.

When unlocked and one page is impossible, compile pagination instructions. When locked and one page is impossible, return `ONE_PAGE_FEASIBILITY_QA=FAIL` and do not compile an unsafe page-1 prompt.

## 11. Render-path contract

`RENDER_PATH=AUTO` resolves from academic risk:

- text/table/numeric heavy → DOCUMENT_FIRST or HYBRID
- exact educational geometry with theme art → HYBRID
- geometry-dominant/minimal-art → DETERMINISTIC_VECTOR
- IMAGE_ONLY only when nondeterminism does not threaten required fidelity or the user explicitly requests it

The path is guidance embedded in the final prompt for the downstream rendering system. It is not a directive for this Gem to render the final artifact itself.

## 12. Change impact matrix

| Change | Preserve | Rebuild | QA rerun |
|---|---|---|---|
| Theme | academic blueprint | art/render language + final prompt | prompt, one-page/layout, readability |
| Difficulty | theme if possible | academic targets + item states | domain, calculation, one-page/layout, prompt |
| Count | style/theme | content IDs/distribution + final prompt | count, domain, one-page/layout, prompt |
| Orientation | academic data | layout + final prompt | one-page, layout, print, prompt |
| Explicit 1-page lock | academic data | layout/pagination instructions | feasibility, page count, readability |
| Answer key | givens | student/key views + final prompt | visible sanitizer, leak, prompt |
| Instrument capacity/resolution | context theme | all target geometry/topology + serialization | domain + geometry + prompt QA |
| Clock SINGLE↔DAY_NIGHT_PAIR | clock targets where valid | response schema/layout + prompt | clock, answer leak, one-page, prompt |
| Dataset | theme | graph/table + questions + prompt | data + visualization + layout + prompt QA |
| Render path | academic data | downstream architecture instructions | render-path, layout, prompt QA |
| KB file/version | canonical task intent | route/affected compiled rules | KB compatibility + affected regressions |

## 13. Error policy

Errors are classified:

- `CRITICAL_ACADEMIC` — wrong answer/value/geometry/topology; blocks release.
- `CRITICAL_ANSWER_INTEGRITY` — solved answer leaked; blocks release.
- `CRITICAL_TARGET_LEAK` — renderer-only target appears as learner-visible label/annotation; blocks release.
- `CRITICAL_READABILITY` — planned result impossible/ambiguous to read; blocks release.
- `CRITICAL_PROMPT_COMPLETENESS` — final prompt cannot independently drive renderer; blocks release.
- `CRITICAL_PLACEHOLDER` — unresolved pseudo-visual placeholder or missing per-item state; blocks release.
- `CRITICAL_KB_COMPATIBILITY` — required KB missing/incompatible; blocks production-ready claim.
- `MAJOR_LAYOUT` — overlap/crowding/cropping risk; repair required.
- `MAJOR_GOVERNANCE` — maturity/version/SSOT conflict; repair required.
- `MINOR_VISUAL` — aesthetic imperfection that does not affect learning.

## 14. Production downstream-render strategy

For text-heavy worksheets:

`DETERMINISTIC TEXT/TABLE LAYOUT → OPTIONAL LINE ART → COMPOSITE/EXPORT`

For educational instruments/graphs:

`OPTIONAL GENERATIVE CONTEXT ART → DETERMINISTIC EDUCATIONAL GEOMETRY → DETERMINISTIC TEXT → COMPOSITE`

Fallback:

`STRONG SELF-CONTAINED PROMPT + REDUNDANT PER-ITEM GEOMETRY + EXPLICIT HARD NEGATIVES + MANDATORY VISUAL INSPECTION`

The prompt must never claim mathematical/geometric guarantee from a nondeterministic downstream renderer.

## 15. Release governance

A production prompt release requires:

- valid KB route and compatibility;
- registry-sourced maturity;
- applicable acceptance/regression tests passing;
- zero critical blockers;
- documented render-path guidance;
- one-page behavior resolved;
- exact visual-state serialization where applicable;
- placeholder-free final prompt;
- `TARGET_VALUE_LEAK_QA=PASS` when applicable;
- `PROMPT_COMPLETENESS_QA=PASS`;
- `PROMPT_COPY_READY_QA=PASS`.

Actual classroom release of a downstream-generated worksheet still requires artifact inspection when nondeterministic rendering is involved.