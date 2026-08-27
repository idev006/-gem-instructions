# Gem Instructions Repository

This repository is the **Single Source of Truth (SSOT)** for multiple production Gem instruction sets.

## Scalable repository structure

Each Gem owns its own canonical instruction and supporting files under `gems/<gem-id>/`.

```text
.
├── README.md
├── docs/
│   ├── SSOT_POLICY.md
│   └── CHANGELOG.md
└── gems/
    ├── README.md
    ├── worksheet-generator/
    │   ├── GEM_INSTRUCTIONS_PRODUCTION.md
    │   ├── CONVERSATION_STARTERS.md
    │   ├── OUTPUT_CONTRACT.md
    │   └── qa/
    │       └── ACCEPTANCE_TESTS.md
    └── color-by-code/
        ├── GEM_INSTRUCTIONS_PRODUCTION.md
        ├── policies/
        │   └── PAGE_FORMAT_POLICY.md
        └── examples/
            └── USAGE_EXAMPLES.md
```

## Naming rule for future Gems

Create one folder per Gem:

`gems/<gem-id>/`

Recommended internal structure:

```text
GEM_INSTRUCTIONS_PRODUCTION.md
CONVERSATION_STARTERS.md        # optional
OUTPUT_CONTRACT.md              # optional
policies/                       # optional
examples/                       # optional
qa/                             # optional
schemas/                        # optional
assets/                         # optional
```

Do not mix files from different Gems in the same folder.

## Current Gems

### Worksheet Generator
Canonical instruction:
`gems/worksheet-generator/GEM_INSTRUCTIONS_PRODUCTION.md`

### Color by Code
Canonical instruction:
`gems/color-by-code/GEM_INSTRUCTIONS_PRODUCTION.md`

Repository-wide governance is kept in `docs/`.

Any behavior-changing update should modify the relevant Gem's canonical file and update `docs/CHANGELOG.md` when appropriate.
