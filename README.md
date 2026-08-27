# Gem Instructions — Worksheet Generation SSOT

This repository is the **Single Source of Truth (SSOT)** for the teacher-first Gem instructions and supporting engineering specifications used to generate print-ready A4 mathematics worksheets.

## Project scope

Initial scope: configurable multiplication worksheets for Thai primary-school teachers, including:

- grade level
- multiplicand digit count
- multiplier digit count
- difficulty
- question count
- theme
- A4 print-ready layout requirements
- answer-key generation
- mathematical validation
- QA and audit rules

## Canonical source

The canonical Gem instruction is:

`gem/GEM_INSTRUCTIONS_PRODUCTION.md`

Supporting specifications must not contradict the canonical instruction. Any intentional behavior change should update the canonical file and the changelog in the same change set.

## Repository structure

```text
.
├── README.md
├── docs/
│   ├── SSOT_POLICY.md
│   ├── PRODUCT_VISION.md
│   ├── ARCHITECTURE.md
│   └── CHANGELOG.md
├── gem/
│   ├── GEM_INSTRUCTIONS_PRODUCTION.md
│   ├── CONVERSATION_STARTERS.md
│   ├── TEACHER_UX_RULES.md
│   └── OUTPUT_CONTRACT.md
├── specs/
│   ├── multiplication-rules.md
│   ├── difficulty-model.md
│   ├── adaptive-grid.md
│   ├── a4-print-spec.md
│   └── worksheet-spec.schema.json
├── qa/
│   ├── ACCEPTANCE_TESTS.md
│   ├── REGRESSION_TESTS.md
│   └── QA_CHECKLIST.md
└── examples/
    └── teacher-prompts.md
```

## Engineering principle

```text
Teacher request
→ normalized worksheet specification
→ mathematical generation
→ validation
→ adaptive A4 layout
→ answer key
→ QA
→ print-ready output
```

Mathematical correctness, curriculum fit, place-value correctness, and student usability always take priority over decoration.
