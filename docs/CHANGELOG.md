# Changelog

All notable changes to the canonical Gem instructions are recorded here.

## Geometric Color-by-Code 1.8.1 — 2026-08-28

- Hardened the Gem after a 40–50 item Grade 3 exact-division space-theme stress test showed that **pre-render Answer-First correctness does not guarantee visible output correctness when the image model redraws academic text**.
- Identified render-time academic drift as a separate root cause from v1.8.0 mapping drift: image generation can alter equations, question numbers, visible question count, and legend values even after the verified mapping is frozen.
- Added `policies/DETERMINISTIC_CONTENT_RENDER_POLICY.md`.
- Set `ACADEMIC_TEXT_RENDER_MODE = DETERMINISTIC_OVERLAY` and required final question text, question IDs, legend values, and academic labels to come from verified deterministic sources rather than image-model text generation.
- Added the hard invariant: `RENDERED CONTENT MUST MATCH VERIFIED CONTENT 100%`.
- Added `POST_RENDER_CONTENT_PARITY = REQUIRED` with exact checks for rendered question count, unique/complete question IDs, prompt-text parity, and legend-domain parity.
- Classified image-model-only full-page academic-text renders as **concept previews / non-conformance renders**, not valid proof that the Gem passed production QA.
- Added high-density rules prohibiting use of generative text placement as a shortcut for fitting 40–50 items on one page.
- Updated canonical instructions, output contract, user guide, README, acceptance tests and regression tests to v1.8.1 behavior.
- Added `qa/RENDER_CONTENT_FIDELITY_REMEDIATION_REPORT_2026-08-28.md` documenting the observed failure mode, root cause, corrective architecture, and closure criteria.

## Geometric Color-by-Code 1.8.0 — 2026-08-28

- Promoted the Gem to **v1.8.0 — Answer-First Generation Integrity** after a real Grade 3 exact-division test produced some correct arithmetic answers that were not represented in the active color legend.
- Identified the root cause as a question-first generation path (`generate question → compute answer → try to map color`) that could escape the active legend domain.
- Added the hard invariant: `NO QUESTION MAY PRODUCE AN ANSWER/CODE OUTSIDE THE ACTIVE LEGEND`.
- Added `CONTENT_GENERATION_MODE = ANSWER_FIRST`, active answer/code-set resolution, preplanned color-usage counts, target answer/code assignment per region, and pre-render mapping freeze.
- Required generated math questions to be constructed from target answers/codes and independently validated against grade/topic constraints; exact division must also pass dividend/divisor digit constraints and remainder = 0.
- Added mandatory `ANSWER_CODE_COLOR_PLAN` to the output contract and required each question/region to retain target answer/code, verified answer, normalized code, color ID, legend entry and validation status.
- Added `policies/ANSWER_FIRST_GENERATION_POLICY.md` and upgraded `policies/COLOR_MAPPING_POLICY.md` to v1.2.0.
- Strengthened acceptance/regression QA to block rendering when any answer is outside the legend, any region lacks a color, usage counts do not reconcile to question count, or image generation alters academic content after mapping freeze.
- Clarified that `ANSWER_KEY = NO` suppresses only the answer-key output; hidden verified answer/color mapping is still mandatory for Student worksheet QA.
- Added `qa/ANSWER_FIRST_REMEDIATION_REPORT_2026-08-28.md` documenting root cause, development plan, implementation and closure criteria.
- Updated canonical instructions, output contract, user guide and README to v1.8.0 behavior.

## Geometric Color-by-Code 1.7.1 — 2026-08-28

- Locked the approved production presentation to **two separate A4 Portrait pages** by default: Page 1 = Student Worksheet, Page 2 = Colored Answer Key.
- Added `policies/TWO_PAGE_A4_OUTPUT_POLICY.md`.
- Updated `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md` to v1.2.0 with explicit page size, orientation, page-order, and same-page prohibition rules.
- Added a 40–50 item single-page stress policy: preserve one Student A4 page only when readability, colorability, line quality, safe margins, and print QA still pass.
- Defined the density-reduction order: reduce decoration and micro-detail before text size, stroke quality, safe margins, or colorable-cell size.
- Required the Answer Key to remain a separate A4 Portrait page using identical geometry/text/mapping.
- Updated `USER_GUIDE.md`, `README.md`, and `qa/ACCEPTANCE_TESTS.md` to document and test the two-page A4 default.

## Geometric Color-by-Code 1.7.0 — 2026-08-27

- Promoted the Gem to **v1.7.0 — Twin Output Integrity** after review of the Student/Answer-Key pair revealed that independently generated colored solutions can contain region-color mismatches even when the worksheet content is correct.
- Made the production default a paired output: `STUDENT_WORKSHEET` (monochrome/unfilled activity regions) + `COLORED_ANSWER_KEY` (fully colored solution).
- Added the hard rule `ONE MASTER GEOMETRY + ONE VERIFIED MAPPING → TWO RENDER VIEWS`.
- Added canonical parameters for Student/Answer pair identity, answer-key geometry/text/fill sources, exact layout matching, and critical pair QA.
- Required Student and Answer Key to share identical region IDs, boundaries, question IDs, text, legend mapping, and line master.
- Required Answer-Key fills to come only from `VERIFIED_COLOR_MAPPING`; a single incorrectly colored region is now a Critical FAIL.
- Prohibited independently regenerating the Answer Key with stochastic image generation or allowing the image model to reinterpret answers/colors.
- Added `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`.
- Updated canonical instructions, output contract, user guide, README, acceptance tests and regression tests to v1.7.0 behavior.

## Geometric Color-by-Code 1.6.0 — 2026-08-27

- Finalized the Geometric Color-by-Code Gem as **v1.6.0 — Natural Harmony Integration**.
- Promoted Natural Harmony into the canonical parameter model with `COMPOSITION_SYSTEM`, `GOLDEN_SECTION_GUIDE`, `FIBONACCI_RHYTHM`, `PHYLLOTAXIS_MODE`, `RADIAL_SYMMETRY`, `PETAL_COUNT_LOGIC`, `FOCAL_POINT_PLACEMENT`, `NATURAL_SCALE_HIERARCHY`, `COMPOSITION_BALANCE`, `SYMMETRY_MODE`, `QUESTION_FLOW`, and `QUESTION_DISTRIBUTION_BALANCE`.
- Defined Natural Harmony as a composition guide for placement, scale, rhythm, focal hierarchy and balance; primary shape remains the construction grammar.
- Added truthfulness rules distinguishing exact/calculated natural proportions from approximate/inspired use.
- Added question-flow planning so question regions follow visual rhythm without mutating verified content or mapping.
- Hardened cross-theme behavior to prevent mechanical reuse of flower symmetry for unrelated themes.
- Final production rendering remains `VECTOR_FIRST_REQUIRED`; generative raster is concept/mockup only for final printable boundaries.
- Updated `GEM_INSTRUCTIONS_PRODUCTION.md`, `USER_GUIDE.md`, `OUTPUT_CONTRACT.md`, `README.md`, Natural Proportion and Reference Version policies, usage examples, acceptance tests and regression tests.
- Added `qa/V1_6_FINALIZATION_CHECKLIST.md` as the final production hardening checklist.

## Geometric Color-by-Code 1.5.0 — 2026-08-27

- Made deterministic/vector geometry mandatory for production-final coloring boundaries.
- Added deterministic shared-edge topology and deterministic Thai/text placement expectations for final print.
- Restricted image-model-only raster output to preview/mockup status for line-quality purposes.
- Required production raster previews/exports to derive from the vector master.

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
- Added teacher-first natural-language interaction, A4 defaults, multiplication digit constraints, math validation, answer-key generation, and QA behavior.
