# Changelog

All notable changes to the canonical Gem instructions are recorded here.

## Color-by-Code 1.4.0 — 2026-08-27

- Hardened the Gem into a true multi-subject Color-by-Code engine.
- Defined “supports every subject/topic” as support for topics that can be converted into short, unambiguous, mappable responses.
- Added `CONTENT_RESPONSE_TYPE` with NUMERIC, WORD, SHORT_TEXT, CHOICE, CATEGORY, TRUE_FALSE, MATCH_CODE, and AUTO modes.
- Added a universal Subject/Topic Adapter to select suitable question form, response type, validation method, and color-mapping strategy by subject.
- Added normalized answer codes so non-math subjects do not need numeric answer ranges.
- Defined strict mapping integrity: one color may represent many answers/codes, but one normalized answer/code may map to only one color.
- Replaced the ambiguous `BLACK_WHITE_MODE` concept with separate `MAIN_ART_COLOR_MODE = MONOCHROME` and `LEGEND_COLOR_PREVIEW = YES` defaults.
- Clarified that only legend color samples may be colored by default; the main worksheet remains black-and-white for student coloring.
- Renamed the default palette to the brand-neutral `BASIC_12_COLORED_PENCIL_PALETTE`; do not attribute it to a specific SKU/brand without verified source data.
- Added explicit open-ended-topic conversion rules and subject-specific validation for mathematics, languages, science, social studies, health, and other factual subjects.
- Preserved A4 Portrait as the default page and horizontal inline math as the default Color-by-Code math layout.
- Canonical file: `gem/COLOR_BY_CODE_GEM_INSTRUCTIONS_PRODUCTION.md`.

## Color-by-Code 1.3.0 — 2026-08-27

- Added `LEGEND_COLOR_PREVIEW` and `LEGEND_PREVIEW_STYLE` parameters.
- Default Color-by-Code worksheet remains black-and-white in the main coloring area.
- Allowed small real-color previews inside the color legend so children can see which color to use.
- Colored preview may be a swatch, circle, pencil tip, or small colored-pencil icon.
- Clarified that `BLACK_WHITE_MODE = YES` can coexist with `LEGEND_COLOR_PREVIEW = YES` because the legend preview is a controlled exception.
- Added an explicit full-monochrome override when the user requests no color anywhere, including the legend.
- Added QA to verify that color-name labels match the displayed preview colors and that no unintended color appears in the main coloring area.
- Canonical file: `gem/COLOR_BY_CODE_GEM_INSTRUCTIONS_PRODUCTION.md`.

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
