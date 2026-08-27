# Changelog

All notable changes to the canonical Gem instructions are recorded here.

## Color-by-Code 1.2.0 — 2026-08-27

- Added `QUESTION_LAYOUT` as a canonical parameter.
- Changed the default math presentation inside Color-by-Code regions to horizontal / inline expressions.
- Clarified that wording such as `การคูณแนวตั้ง` describes the math topic unless the user explicitly asks to render the problems vertically.
- Vertical calculation layout is now opt-in only for Color-by-Code worksheets.
- Added validation to confirm rendered question layout matches the resolved `QUESTION_LAYOUT` value.
- Preserved A4 Portrait, black-and-white, Thai-first, coloring-friendly, 10–100 question, and 1–12 color defaults/policies.
- Canonical file: `gem/COLOR_BY_CODE_GEM_INSTRUCTIONS_PRODUCTION.md`.

## Color-by-Code 1.1.0 — 2026-08-27

- Expanded the canonical parameter model for the Color-by-Code Gem.
- Added explicit support for grade, subject, topic, question type, 10–100 questions, difficulty, language, 1–12 colors, custom colors, theme, visual complexity, page size, orientation, pagination, region sizing, worksheet fields, output controls, QA, seeds, worksheet IDs, batch generation, and duplicate policies.
- Defined teacher-facing core parameters as: grade, subject, topic, question count, difficulty, color count, theme, and page size/orientation.
- Locked default page to A4 Portrait while preserving A3/A4/A5/Letter/Legal/Custom and Portrait/Landscape support.
- Clarified that changing page size or orientation requires layout recalculation rather than stretching an existing layout.
- Strengthened answer-group, color-distribution, answer-key SSOT, and validation rules.
- Canonical file: `gem/COLOR_BY_CODE_GEM_INSTRUCTIONS_PRODUCTION.md`.

## Worksheet Gem 1.2.0 — 2026-08-27

- Promoted Thai-first visible-language behavior to a canonical default.
- Added critical Thai-language QA: spelling, vowel/tone marks, spacing, clarity, terminology consistency, and age appropriateness.
- Changed the default worksheet visual mode from accent-color styling to monochrome / black-and-white print-friendly output.
- Added a no-color-fill default policy and photocopy-safe requirement.
- Added coloring-friendly illustration rules: simple black-and-white line art, bold clear outlines, minimal detail, and child-friendly shapes suitable for coloring.
- Added explicit prohibition on dense shading, highly detailed cartoon rendering, and image complexity that reduces instructional usability.
- Added monochrome and illustration checks to final critical QA.
- Updated `gem/OUTPUT_CONTRACT.md` to match the canonical v1.2.0 behavior.

## Worksheet Gem 1.1.0 — 2026-08-27

- Promoted the full Teacher-First Gem V3 instruction into the canonical SSOT file.
- Canonical file: `gem/GEM_INSTRUCTIONS_PRODUCTION.md`.
- Expanded the canonical instruction to include all Teacher-First sections agreed in the design conversation.
- Preserved A4 print-ready behavior, adaptive calculation grids, mathematical validation, answer-key single-source rules, auto-pagination, teacher-friendly revisions, batch behavior, and final QA gates.
- Added explicit honest-capability rules: never claim a PDF or print-ready artifact exists unless it was actually produced and checked.

## Worksheet Gem 1.0.0 — 2026-08-27

- Established the initial canonical production Gem instruction.
- Added teacher-first natural-language interaction, A4 defaults, multiplication digit constraints, math validation, adaptive layout, answer-key generation, and QA behavior.
