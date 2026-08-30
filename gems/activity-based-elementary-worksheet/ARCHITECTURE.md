# Architecture — Activity-Based Elementary Worksheet Generator

Version: 2.0.0

## 1. System model

The Gem is organized as six cooperating layers:

1. `INTERACTION_LAYER` — understands teacher language and asks minimal clarifications.
2. `NORMALIZATION_LAYER` — resolves required/default/auto parameters.
3. `DOMAIN_LAYER` — generates and validates academic data.
4. `BLUEPRINT_LAYER` — separates internal verified data from student-facing data.
5. `LAYOUT_RENDER_LAYER` — plans page geometry, educational diagrams, text zones, and art.
6. `QA_RELEASE_LAYER` — blocks incorrect or unreadable outputs.

## 2. Canonical state objects

### REQUEST_CONTEXT
Raw teacher request + references + revision instructions.

### NORMALIZED_WORKSHEET_SPEC
Single source of truth for all resolved parameters.

### INTERNAL_VERIFIED_BLUEPRINT
Canonical hidden academic content, answers, formulas, target geometry, IDs, and QA metadata.

### STUDENT_RENDER_BLUEPRINT
Sanitized student-visible givens and blank answer fields plus render-only geometry metadata.

### LAYOUT_BLUEPRINT
Page regions, repeated-card geometry, minimum sizes, pagination, text/art zones.

### RENDER_PLAN
Prompt/vector/text-overlay instructions and hard negatives.

### QA_REPORT
Global + domain-specific gate status and maturity.

## 3. Process

`Teacher request`
→ parse explicit requirements
→ detect domain
→ resolve defaults
→ create normalized spec
→ generate academic targets
→ derive source values/diagram geometry
→ independently validate
→ build internal blueprint
→ sanitize answers
→ build student blueprint
→ calculate page capacity
→ apply domain minimum-size constraints
→ create render plan
→ compile prompt/overlay instructions
→ pre-render QA
→ render
→ post-render QA
→ release or repair

## 4. Domain plugin contract

Every domain engine should define:

- trigger phrases / routing
- learning objective patterns
- parameters/defaults
- deterministic formulas/rules
- valid/invalid invariants
- content-generation strategy
- student/internal schemas
- layout minimums
- render constraints
- domain QA gates
- hard negatives
- maturity status

## 5. Instrument plugin contract

Instrument domains additionally define:

- canonical template geometry
- scale/tick mapping
- target-to-geometry transformation
- minimum printed size
- template lock
- per-render inspection rubric

## 6. Change impact matrix

| Change | Preserve | Rebuild | QA rerun |
|---|---|---|---|
| Theme | academic blueprint | art/render plan | layout, readability, prompt |
| Difficulty | theme if possible | academic targets | domain, calculation, layout |
| Count | style/theme | content IDs/distribution | count, domain, layout |
| Orientation | academic data | layout/render | layout, print |
| Answer key | givens | student/key views | leak, prompt |
| Instrument capacity/resolution | context theme | all target geometry | complete domain geometry QA |
| Dataset | theme | graph/table + questions | data + visualization QA |

## 7. Error policy

Errors are classified:

- `CRITICAL_ACADEMIC` — wrong answer/value/geometry; blocks release.
- `CRITICAL_READABILITY` — impossible/ambiguous to read; blocks release.
- `MAJOR_LAYOUT` — overlap/crowding/cropping; repair required.
- `MINOR_VISUAL` — aesthetic imperfection that does not affect learning.

Never trade a critical academic/readability defect for visual attractiveness.

## 8. Production rendering strategy

Best quality path:

`AI theme illustration + deterministic educational diagram + deterministic Thai text + composition + QA`

Fallback path:

`strong prompt + geometry locks + visual inspection`

The fallback must never be described as mathematically guaranteed.