# Changelog

All notable changes to the canonical Gem instructions are recorded here.

## Geometric Color-by-Code 1.4.0 — 2026-08-27

- Promoted the canonical Gem to v1.4.0 after visual review of the improved triangle-garden worksheet.
- Added `MIN_COLORABLE_CELL_SIZE`, `MIN_SEGMENT_LENGTH`, `MICRO_TILE_DENSITY_POLICY`, and `FREEFORM_DETAIL_BUDGET` to protect practical coloring usability.
- Added a three-level stroke hierarchy: outer frame > theme/object silhouette > internal tile boundary.
- Added strict avoidance rules for hairlines, fuzzy/sketch strokes, double strokes, broken joins, and accidental starburst junctions.
- Added render-quality parameters and made deterministic/vector rendering the production preference when available.
- Added `THAI_FONT_RENDER_QA` and deterministic text-placement expectations for production output.
- Added `policies/GOLDEN_REFERENCE_STANDARD.md`; Golden Reference is defined as a quality target rather than a fixed composition template.
- Hardened geometry policy around minimum colorable area, freeform-detail budget, controlled tile density, and starburst reduction.
- Updated `USER_GUIDE.md`, `OUTPUT_CONTRACT.md`, `README.md`, `qa/ACCEPTANCE_TESTS.md`, and `qa/REGRESSION_TESTS.md` to v1.4 behavior.

## Geometric Color-by-Code 1.2.0 — 2026-08-27

- Hardened the Gem from the latest real visual audit of the triangle-garden worksheet.
- Raised the HIGH primary-shape target to approximately >=85% of visible structural tiling rhythm.
- Added `PRIMARY_SHAPE_COVERAGE_TARGET`, `QUESTION_REGION_SHAPE_GRAMMAR`, `TILE_SCALE_VARIATION`, `FREEFORM_MAJOR_OBJECTS`, `VISUAL_LANGUAGE_CONSISTENCY`, `ANSWER_FREQUENCY_PLAN`, `COLOR_USAGE_TARGET`, and `LINE_TOPOLOGY_QA`.
- Defined `QUESTION_REGION_SHAPE_GRAMMAR = PRIMARY_SHAPE_GROUP` so answer regions remain part of the mosaic instead of becoming large freeform circles/leaves.
- Added `FREEFORM_MAJOR_OBJECTS = PROHIBITED_WHEN_HIGH` to prevent conventional flower, leaf, butterfly, cloud, animal, or other major silhouettes from replacing the geometric construction grammar.
- Added controlled tile-scale policy to prevent different parts of a page from looking like unrelated geometric systems.
- Added deterministic answer/color frequency planning; for 30 questions / 6 colors the normal balanced target is approximately 5 regions per color when content-valid.
- Added critical line/topology QA for accidental double lines, broken joins, ambiguous shared borders, unintended open regions, border/text collisions, and unusable sliver cells.
- Expanded the triangle-garden reference rules so flowers, leaves, butterflies, clouds, hills and ground bands are constructed primarily from triangle clusters.
- Updated canonical instructions, output contract, user guide, usage examples, geometry policy, acceptance tests and regression tests to v1.2.0.
- Added `qa/VISUAL_AUDIT_REMEDIATION_PLAN_2026-08-27.md` with findings, design decisions and closure criteria.

## Geometric Color-by-Code 1.1.0 — 2026-08-27

- Hardened the Gem from a real-output audit of a Thai category worksheet.
- Added `LEGEND_COVERAGE_POLICY = NO_ORPHAN_LEGEND_ENTRY`; every student-facing legend entry must be used by at least one question/region by default.
- Added category/focus planning parameters: `CATEGORY_SET`, `FOCUS_CATEGORY`, `CATEGORY_FOCUS_MODE`, `FOCUS_SHARE_TARGET`, and `CATEGORY_DISTRIBUTION`.
- Defined focus semantics so phrases such as `เน้นแม่กง` resolve to an intentionally higher question share for the focus category, normally targeting about 40–60% when the user does not provide a custom ratio.
- Added `PREFER_ATOMIC_RESPONSE = YES` for vocabulary/classification tasks to prefer clear single words over unnecessary phrases.
- Strengthened `SHAPE_DOMINANCE = HIGH`: target approximately >=80% structural tiling rhythm from the primary shape and restrict large freeform structural areas to a minor role (target approximately <=15–20%).
- Added explicit FAIL rule for conventional freeform object silhouettes with geometric patterns merely overlaid on top.
- Expanded the Verified Content Blueprint to include category usage counts, focus share, legend entries, legend usage counts, and legend coverage validation before rendering.
- Updated `OUTPUT_CONTRACT.md`, `policies/COLOR_MAPPING_POLICY.md`, `policies/GEOMETRY_LAYOUT_POLICY.md`, `qa/ACCEPTANCE_TESTS.md`, and `qa/REGRESSION_TESTS.md` to v1.1.0.
- Added `qa/AUDIT_REMEDIATION_PLAN_2026-08-27.md` documenting the audit findings, decisions, and closure criteria.

## Geometric Color-by-Code 1.0.0 — 2026-08-27

- Added new production Gem at `gems/geometric-color-by-code/`.
- Defined `PRIMARY_SHAPE` as the construction grammar of the main image, not a decorative overlay.
- Added tessellation/mosaic architecture: shape grammar → theme silhouette → question regions → answer/code/color mapping.
- Separated `MICRO_TILE_COUNT` from `QUESTION_REGION_COUNT` so visually rich mosaics can contain many small tiles while preserving readable question regions.
- Added `QUESTION_REGION_MODE = GROUPED_TILES` as the default.
- Added theme-silhouette construction by tile grouping and minimized freeform curves.
- Added explicit exact/approximate tessellation truthfulness rules for different shape families.
- Added multi-subject response types and normalized answer codes.
- Added verified content blueprint, mapping integrity, geometry blueprint, and final prompt contracts.
- Added `USER_GUIDE.md`, `OUTPUT_CONTRACT.md`, geometry policy, usage examples, acceptance tests, regression tests, and a 9-round dry-run report.
- Dry run converted failures involving shape-as-decoration, text density, mapping conflicts, theme recognizability, image-model text invention, revision drift, and open-ended content into regression rules.

## Themed Hub Worksheet 1.1.0 — 2026-08-27

- Hardened `gems/themed-hub-worksheet/GEM_INSTRUCTIONS_PRODUCTION.md` from v1.0.0 to v1.1.0.
- Added explicit `USE_CASES` and `NON_GOALS` to satisfy repository production standards.
- Reworked the architecture to require `Normalized Worksheet Spec → Learning Objective → Verified Content Blueprint → Slot Blueprint → Layout Blueprint → Final Prompt`.
- Added explicit parameter semantics for `ACTIVITY_TYPE`, `RESPONSE_TYPE`, `SLOT_LABEL_MODE`, `SLOT_CONTENT_MODE`, `CENTER_CONTENT_MODE`, and `DIFFICULTY`.
- Added a true multi-subject adapter that resolves subject/topic/grade into learning objective, activity type, response type, slot-content rules, and validation rules.
- Added a Verified Content Blueprint contract so important academic text, slot roles, answers, and counts are locked before visual prompt assembly.
- Added pagination-over-compression policy for requests above the recommended 4–16 slots per page.
- Added print-layout requirements including default 10 mm margin target, 10–12 mm safe-margin guidance, writing-space priority, and decoration reduction before compression.
- Added edge-case handling for long text, unsuitable objects, open-ended topics, missing theme/object, and missing critical academic information.
- Added output honesty rules and strengthened QA gates.
- Added `gems/themed-hub-worksheet/OUTPUT_CONTRACT.md`.
- Expanded `examples/USAGE_EXAMPLES.md` with minimal, detailed, revision, and edge-case prompts.
- Expanded `qa/ACCEPTANCE_TESTS.md` and added `qa/REGRESSION_TESTS.md`.
- Updated `USER_GUIDE.md` to v1.1.0 with production workflow, slot-count policy, pagination guidance, edge cases, and validation checklist.

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
