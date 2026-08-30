# Architecture — Activity-Based Elementary Worksheet Generator

Version: 2.2.1
Status: Production architecture reference

## 1. System model

The Gem is organized as eight cooperating layers:

1. `INTERACTION_LAYER` — understands teacher language and asks minimal clarifications.
2. `NORMALIZATION_LAYER` — resolves required/default/auto parameters.
3. `DOMAIN_LAYER` — generates and validates academic data.
4. `BLUEPRINT_LAYER` — separates internal verified data from student-facing data.
5. `RENDER_PATH_LAYER` — selects DOCUMENT_FIRST, HYBRID, DETERMINISTIC_VECTOR, or IMAGE_ONLY.
6. `ONE_PAGE_LAYOUT_LAYER` — attempts a valid one-page solution, then resolves pagination/lock behavior.
7. `RENDER_LAYER` — builds deterministic text/geometry zones and optional generative art.
8. `QA_RELEASE_LAYER` — sanitizes visible output, checks the prompt/artifact, and blocks incorrect or unreadable releases.

## 2. Canonical state objects

### REQUEST_CONTEXT
Raw teacher request + references + revision instructions.

### NORMALIZED_WORKSHEET_SPEC
Single source of truth for all resolved parameters, including `DOMAIN`, `DOMAIN_MATURITY`, `RENDER_PATH`, `ONE_PAGE_PREFERRED`, `ONE_PAGE_LOCK`, and target page count.

### INTERNAL_VERIFIED_BLUEPRINT
Hidden academic content, verified answers, formulas, target geometry/data relations, IDs, and QA metadata.

### STUDENT_RENDER_BLUEPRINT
Sanitized student-visible givens, required diagrams/instruments, blank response areas, and render-only geometry metadata that must never appear as answer text.

### RENDER_PATH_DECISION
Resolved rendering architecture and rationale:

- `DOCUMENT_FIRST`
- `HYBRID`
- `DETERMINISTIC_VECTOR`
- `IMAGE_ONLY`

### LAYOUT_BLUEPRINT
Page regions, one-page feasibility result, repeated-card/table geometry, minimum sizes, text/art zones, and pagination fallback when unlocked.

### RENDER_PLAN
Deterministic text/vector instructions, generative-art instructions when applicable, composition order, locks, and hard negatives.

### QA_REPORT
Global + domain-specific gate status, registry maturity, render-path status, one-page status, and release decision.

## 3. Canonical process

`Teacher request`
→ parse explicit requirements
→ detect domain
→ resolve defaults
→ create normalized spec
→ generate academic targets
→ derive source values/diagram geometry
→ independently validate
→ build internal verified blueprint
→ sanitize student view
→ resolve render path
→ run one-page feasibility
→ build layout
→ create render plan
→ compile final render instructions
→ visible-output sanitizer
→ pre-render QA
→ render if requested/available
→ post-render QA
→ release or repair

## 4. Domain plugin contract

Every domain engine should define:

- trigger phrases / routing
- learning-objective patterns
- parameters/defaults
- deterministic formulas/rules
- valid/invalid invariants
- content-generation strategy
- internal/student schemas
- layout minimums
- preferred render paths
- render constraints
- domain QA gates
- hard negatives
- maturity evidence dependencies

The overall maturity value comes from `domains/DOMAIN_REGISTRY.md`, not from an engine's self-description.

## 5. Instrument plugin contract

Instrument domains additionally define:

- canonical template geometry
- scale/tick mapping
- target-to-geometry transformation
- minimum printed size
- template lock
- one-page footprint constraints
- deterministic-vector/hybrid preference
- per-instrument post-render inspection rubric

Educational geometry outranks theme art and one-page density.

## 6. Global one-page contract

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

The system attempts a valid one-page layout before pagination.

Optimization is allowed only on nonessential layout cost: decoration, ornamental whitespace, repeated decorative labels, verbose instructions, and inefficient layout choice.

The system may not trade away:

- academic correctness
- exact requested question count
- domain minimum instrument/diagram size
- readable text
- required answer fields
- safe margins
- answer integrity

When unlocked and one page is impossible, pagination is valid. When locked and one page is impossible, return `ONE_PAGE_FEASIBILITY_QA=FAIL` and do not silently create page 2 or unsafe content.

## 7. Render-path contract

`RENDER_PATH=AUTO` resolves from academic risk:

- text/table/numeric heavy → DOCUMENT_FIRST or HYBRID
- exact educational geometry with theme art → HYBRID
- geometry-dominant/minimal-art → DETERMINISTIC_VECTOR
- IMAGE_ONLY only when nondeterminism does not threaten required fidelity or the user explicitly requests it

Thai text-heavy pages and exact measurement instruments must not default to IMAGE_ONLY.

A path decision does not change canonical academic data; it changes only rendering/composition strategy.

## 8. Change impact matrix

| Change | Preserve | Rebuild | QA rerun |
|---|---|---|---|
| Theme | academic blueprint | art/render plan | render-path, one-page/layout, readability |
| Difficulty | theme if possible | academic targets | domain, calculation, one-page/layout |
| Count | style/theme | content IDs/distribution | count, domain, one-page/layout |
| Orientation | academic data | layout/render | one-page, layout, print |
| Explicit 1-page lock | academic data | layout | feasibility, page count, readability |
| Answer key | givens | student/key views | visible sanitizer, leak, prompt |
| Instrument capacity/resolution | context theme | all target geometry | complete domain + one-page geometry QA |
| Clock SINGLE↔DAY_NIGHT_PAIR | clock targets where valid | response schema/layout | clock, answer leak, one-page |
| Dataset | theme | graph/table + questions | data + visualization + layout QA |
| Render path | academic data | render plan | render-path, layout, post-render QA |

## 9. Error policy

Errors are classified:

- `CRITICAL_ACADEMIC` — wrong answer/value/geometry; blocks release.
- `CRITICAL_ANSWER_INTEGRITY` — active solution leaked into visible output; blocks release.
- `CRITICAL_READABILITY` — impossible/ambiguous to read; blocks release.
- `CRITICAL_ARTIFACT_TYPE` — wrong artifact, wrong locked page count, or missing required response structure; blocks release.
- `MAJOR_LAYOUT` — overlap/crowding/cropping; repair required.
- `MAJOR_GOVERNANCE` — maturity/version/SSOT conflict; blocks a production claim until repaired.
- `MINOR_VISUAL` — aesthetic imperfection that does not affect learning.

Never trade a critical academic/readability defect for visual attractiveness or one-page density.

## 10. Production rendering strategy

Preferred architecture is content-dependent rather than image-model-first.

For text-heavy worksheets:

`DETERMINISTIC TEXT/TABLE LAYOUT → OPTIONAL LINE ART → EXPORT → QA`

For educational instruments/graphs:

`OPTIONAL AI CONTEXT ART → DETERMINISTIC VECTOR GEOMETRY → DETERMINISTIC TEXT → COMPOSITE → QA`

Fallback:

`strong prompt + explicit locks + mandatory visual inspection`

The fallback must never be described as mathematically or geometrically guaranteed.

## 11. Release governance

A production claim requires:

- registry-sourced maturity
- applicable acceptance tests passing
- zero critical blockers
- documented render-path behavior
- one-page behavior tested
- actual-render evidence according to `qa/DOMAIN_RELEASE_MATRIX.md`

Deterministic academic maturity alone does not imply overall `PRODUCTION_HARDENED` status.
