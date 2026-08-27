# SSOT Policy

## Repository model

This repository contains multiple production Gems. Each Gem has its own canonical instruction under:

`gems/<gem-id>/GEM_INSTRUCTIONS_PRODUCTION.md`

Repository-wide governance belongs in `docs/`.

## Canonical authority

For any Gem, the highest authority is that Gem's own canonical file:

`gems/<gem-id>/GEM_INSTRUCTIONS_PRODUCTION.md`

A supporting policy, example, QA file, schema, or README must not silently override the canonical instruction.

## Precedence within a Gem

1. `gems/<gem-id>/GEM_INSTRUCTIONS_PRODUCTION.md`
2. Gem-specific `policies/*`
3. `OUTPUT_CONTRACT.md` when present
4. Gem-specific `qa/*`
5. Gem-specific `examples/*`
6. Gem-specific `README.md`
7. Repository `README.md`

Repository-wide policy in `docs/` governs structure, SSOT ownership, and change control, but should not redefine Gem behavior without updating that Gem's canonical instruction.

## Change control

Any change that affects a Gem's behavior should update, when applicable:

- the relevant canonical Gem instruction
- affected Gem-specific policy
- acceptance/regression tests
- usage examples
- `docs/CHANGELOG.md`

## New Gem rule

Every new Gem must receive a unique folder under `gems/`. Do not place multiple Gems' production instructions in one shared flat folder.

Recommended structure:

```text
gems/<gem-id>/
├── GEM_INSTRUCTIONS_PRODUCTION.md
├── CONVERSATION_STARTERS.md   # optional
├── OUTPUT_CONTRACT.md         # optional
├── policies/                  # optional
├── examples/                  # optional
├── qa/                        # optional
├── schemas/                   # optional
└── assets/                    # optional
```

## Honest completion

A Gem must not claim that a PDF, DOCX, preview, image, or other downloadable artifact exists unless that artifact was actually created in the active environment.

## Quality principle

Content correctness, specification compliance, learner appropriateness, usability, and output integrity take priority over decoration.
