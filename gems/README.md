# Gems Index

Each production Gem lives in its own folder under this directory.

## Folder convention

`gems/<gem-id>/`

Each Gem should keep its canonical instruction at:

`gems/<gem-id>/GEM_INSTRUCTIONS_PRODUCTION.md`

Optional supporting directories:

- `policies/` — Gem-specific policies
- `examples/` — user prompt / usage examples
- `qa/` — acceptance and regression tests
- `schemas/` — machine-readable schemas
- `assets/` — Gem-specific supporting assets

Optional supporting files:

- `CONVERSATION_STARTERS.md`
- `OUTPUT_CONTRACT.md`
- `README.md`

## Current Gem IDs

- `worksheet-generator`
- `color-by-code`

When adding a new Gem, create a new sibling folder. Do not place its canonical files directly at repository root or mix them with another Gem.
