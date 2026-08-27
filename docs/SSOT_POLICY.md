# SSOT Policy

## Canonical authority

`gem/GEM_INSTRUCTIONS_PRODUCTION.md` is the canonical instruction for the production Gem.

## Precedence

When documents conflict, use this precedence:

1. `gem/GEM_INSTRUCTIONS_PRODUCTION.md`
2. `specs/*`
3. `gem/OUTPUT_CONTRACT.md`
4. `gem/TEACHER_UX_RULES.md`
5. `qa/*`
6. `examples/*`
7. `README.md`

A lower-precedence document must never silently override a higher-precedence document.

## Change control

Any change that affects worksheet behavior must update, when applicable:

- canonical Gem instruction
- affected specification
- acceptance/regression tests
- changelog

## Quality gates

No release is considered production-ready unless critical gates pass:

- mathematical correctness
- requested digit counts
- place-value alignment
- question count
- difficulty policy
- duplicate control
- answer-key consistency
- A4 layout safety
- print usability

## Honest completion

The Gem must not claim that a PDF, DOCX, preview, or other downloadable artifact exists unless an actual file was created in the current environment.

## Design priority

1. Mathematical correctness
2. Specification compliance
3. Curriculum appropriateness
4. Place-value correctness
5. Student usability
6. Difficulty correctness
7. Print readability
8. Layout consistency
9. Theme consistency
10. Decoration
