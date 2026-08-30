# KAN-V2-01 — Scale Reading Render Audit

Date: 2026-08-30
Gem: `activity-based-elementary-worksheet`
Domain: `MEASUREMENT_WEIGHT / DIAL_SCALE_READING`
Status: PARTIAL PASS — deterministic overlay path passes; generative-only fallback still not promoted

## Objective

Produce and audit 10 rendered scale-reading worksheets × 10 questions = 100 instructional dials.

Audit criteria per dial:

1. true circle
2. center pivot
3. one needle
4. labels 0–5 present and ordered
5. 51 tick positions for 0–5 kg at 0.1 kg resolution
6. uniform tick spacing
7. exact target tick
8. minimum readable size
9. no overlap/cropping
10. blank student answer

## Attempt A — nondeterministic image render

Result: FAIL.

The renderer produced a QA/audit dashboard rather than the requested set of student worksheets.

Classification: `RENDER_OBJECTIVE_FAILURE`.

Root cause: meta-QA context was allowed to dominate the artifact objective.

Repair applied:

- Gem v2.1 adds explicit `RENDER_OBJECTIVE` lock.
- Normal worksheet generation sets `RENDER_OBJECTIVE=STUDENT_WORKSHEET`.
- Hard negatives prohibit audit dashboards, QA panels, meta-reports, and production notes from appearing as the student artifact.
- Acceptance tests 79 and 81 added.

## Attempt B — deterministic production-path render

Architecture used:

`DETERMINISTIC CONTENT → DETERMINISTIC DIAL GEOMETRY → DETERMINISTIC TEXT → COMPOSITE → VISUAL AUDIT`

Ten themes were rendered:

1. สวนผักของหนู
2. ตลาดผลไม้
3. ร้านเบเกอรี
4. ตลาดอาหารทะเล
5. ร้านเครื่องเขียน
6. ค่ายนักสำรวจ
7. ร้านของเล่น
8. ร้านดอกไม้
9. ครัวเชฟน้อย
10. นักธรณีวิทยา

Each worksheet uses A4 portrait, 2 columns × 5 rows, 10 questions, 0–5 kg, 0.1 kg minor divisions, 300° active scale sweep, exact center pivot, and blank `........ กิโลกรัม ........ ขีด` response.

## Intermediate text-render failure

The first deterministic text path used a Thai font that did not provide reliable visible coverage for all required Arabic numerals/symbols in the rendered result. Missing-glyph boxes appeared.

Result: FAIL.

Classification: `GLYPH_COVERAGE_FAILURE`.

Repair applied:

- Added `GLYPH_COVERAGE_QA` to canonical Gem v2.1.
- Deterministic text path must visibly support Thai + Arabic numerals + decimal points + punctuation + unit symbols.
- Missing-glyph boxes/tofu are now a critical readability blocker.
- Acceptance test 80 added.

A compatible Thai/Latin font path was then used and the suite was rerendered.

## Final deterministic suite results

Total rendered worksheets: 10
Total instructional dials: 100

Programmatic geometry audit:

| Gate | Result |
|---|---:|
| TRUE_CIRCLE | 100/100 PASS |
| CENTER_PIVOT | 100/100 PASS |
| TICK_COUNT | 100/100 PASS |
| LABEL_COUNT_0_TO_5 | 100/100 PASS |
| EXACT_TARGET_TICK | 100/100 PASS |
| MINIMUM_DIAL_SIZE | 100/100 PASS |

Visual contact-sheet audit:

- 10/10 sheets preserve 2×5 structure.
- 100/100 dials remain circular at rendered output.
- Center hubs visibly anchor the needles.
- Labels 0–5 remain visible and consistent.
- No dial is squeezed by layout.
- Thai worksheet text and Arabic numerals are visibly readable after font-path repair.
- Answer fields remain blank.
- No answer leakage observed.

## Important limitation

These 10 renders validate the preferred deterministic instrument-overlay path. They do NOT prove that a fully generative image model can reliably draw 100 mathematically exact dials unaided.

Therefore:

`DETERMINISTIC_OVERLAY_PATH = PASS`

`GENERATIVE_ONLY_FALLBACK = NOT_HARDENED`

The domain remains `PRODUCTION_CANDIDATE` until promotion criteria are satisfied across the complete production composition path and failure/repair evidence is judged sufficient.

## New regression defects captured

1. `RENDER_OBJECTIVE_FAILURE` — renderer creates meta-report instead of worksheet.
2. `GLYPH_COVERAGE_FAILURE` — deterministic text path shows tofu/missing glyphs.

Both are now critical release checks.

## KANBAN status

- KAN-V2-01A Nondeterministic worksheet render: FAILED, defect captured.
- KAN-V2-01B Deterministic 10-sheet render: DONE.
- KAN-V2-01C 100-dial geometry audit: DONE, 100/100 critical geometry checks pass.
- KAN-V2-01D Text glyph repair: DONE.
- KAN-V2-01E Full generative-context + deterministic-dial composite audit: NEXT.

## Release decision

Do not promote `MEASUREMENT_WEIGHT` solely from this run.

This run provides strong evidence that the preferred deterministic educational-geometry architecture works, while also demonstrating why generative-only artifact rendering requires additional objective locking and post-render QA.