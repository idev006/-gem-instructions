# Baseline 2.6.3-LTS Release Checklist

Status: Critical educational-instrument safety release checklist
Release family: 2.6.3-LTS
Compatible worker baseline: 2.6.x / schema 1

## Release intent

2.6.3-LTS promotes independent metrology engineering into the base architecture. The objective is educational safety: every learner-read measuring instrument must be quantitatively correct before prompt release, and actual rendered pixels still require artifact inspection before classroom release.

The 2026-08-31 actual weight-dial inactive-gap defect is permanent negative evidence. The later consolidated UAT reports also established a second systemic invariant: a locally readable instrument does not prove that the full worksheet physically fits the claimed page.

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`.

## Required base workers

Exactly 10:

`W01_ACADEMIC_CONTENT`
`W02_TIME_CLOCK`
`W03_WEIGHT_SCALE`
`W04_LENGTH_DISTANCE`
`W05_TEMPERATURE_CAPACITY_VOLUME`
`W06_MONEY_CALENDAR_DATA`
`W07_INSTRUMENT_AUDITOR`
`W08_LAYOUT_RENDER_THAI`
`W09_QA_RELEASE`
`W10_METROLOGY_ENGINEER`

Every worker declares `BASELINE_COMPATIBILITY=2.6.x` and `WORKER_SCHEMA_VERSION=1`.

## Mandatory profiles

Every W01–W10 runtime bundle embeds:

1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `METROLOGY_ASSURANCE_PROFILE.md`
5. `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

## Mandatory learner-read chain

`OWNING DOMAIN → W07 GEOMETRY AUDIT → W10 INDEPENDENT METROLOGY AUDIT → W08 LAYOUT/RENDER → W09 RELEASE`

W10 must independently recompute quantitative evidence rather than repeat W07.

Required W10 state includes count, spacing, reference, target alignment, label association, inactive region when applicable, true minimum size, selected render size, numeric `PHYSICAL_PAGE_STATE`, print feasibility and independent verdict.

Missing W10 evidence = `PROMPT_METROLOGY_AUDIT_REQUIRED_QA=FAIL` and `PROMPT_RELEASE=BLOCKED`.

## Universal scale audit

For every learner-read clock, dial, ruler, speedometer, protractor, thermometer, graduated container or graph axis verify topology/range, exact interval/position counts, reference, direction, spacing, hierarchy, anchoring, labels, target alignment, inactive region, decoration isolation, template consistency, print readability and numeric page feasibility.

`ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER`.

## Physical page feasibility audit

For A4 portrait use physical page dimensions 210 × 297 mm before margins.

Before one-page feasibility can PASS, serialize numeric proof for margins, header/title/directions reserve, complete item bounding boxes, rows/columns, row/column gaps, answer zones, usable width/height and required grid width/height.

PASS requires:

`REQUIRED_GRID_WIDTH_MM <= USABLE_WIDTH_MM`

and

`REQUIRED_GRID_HEIGHT_MM <= USABLE_HEIGHT_MM`.

`ONE_PAGE_PREFERRED != ONE_PAGE_LOCKED`.

If `ONE_PAGE_LOCK=OFF` and the preferred one-page plan fails, paginate and re-audit. Do not hard-code `1 PAGE` or `2×5` after a failed packing proof.

Permanent lower-bound regression examples:
- weight dial: 5×80 mm = 400 mm → impossible on A4 portrait;
- protractor: 5×70 mm = 350 mm → impossible;
- thermometer: 5×60 mm = 300 mm before other content → impossible;
- graduated container: 5×50 mm = 250 mm before gaps/header/margins → requires full proof, no assumed PASS;
- graph worksheet: axis height alone never proves full-page fit because graph titles and ten question/answer lines also consume height.

W10 must distinguish `METROLOGY_MINIMUM_SIZE_MM` from `SELECTED_RENDER_SIZE_MM` and provide `SIZE_ORACLE_SOURCE`.

## Known-answer metrology oracles

Clock:
- 60 intervals / 60 distinct positions;
- 6° per minute position;
- 10:30 → minute 180°, hour 315°.

Weight dial:
- 0–5 kg @0.1 kg → 50 active intervals / 51 positions;
- canonical active sweep 300°, inactive gap 60°;
- inactive open arc 180°→240°;
- `INACTIVE_GAP_TICK_COUNT=0`;
- `INACTIVE_GAP_RADIAL_MARK_COUNT=0`;
- canonical label angles `{0:240°,1:300°,2:0°,3:60°,4:120°,5:180°}`.

Ruler:
- 1 cm @1 mm → 10 intervals / 11 positions / 9 interior positions;
- `PHYSICAL_EDGE_IS_GRADUATION=NO`.

Speedometer:
- 0–120 km/h @10 → 12 intervals / 13 positions;
- 240° active / 120° inactive gap;
- canonical convention has 0° at top; 60 km/h → 0° → straight up;
- 35 km/h is not representable in discrete 10 km/h mode.

Protractor:
- 0–180° @1° → 180 intervals / 181 positions;
- `tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)`;
- production width 70 mm; 65 mm rejected.

Thermometer:
- 0–50°C @1°C → 50/51;
- 60 mm / 50 = exactly 1.20 mm spacing;
- liquid endpoint on target graduation centerline.

Graduated container:
- endpoint-inclusive count from configured range/interval;
- target level/read convention exact.

Graph axis:
- equal numeric increments → equal physical increments;
- bars/data endpoints map exactly to canonical data.

## Renderer prevention loop

Final prompt includes:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

and:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Renderer self-review is prevention only, not artifact proof.

## Release gates

Applicable gates include the existing academic/scale/metrology gates plus:

`PROMPT_METROLOGY_SIZE_ORACLE_QA`
`PROMPT_PHYSICAL_PAGE_STATE_QA`
`PROMPT_PHYSICAL_WIDTH_FEASIBILITY_QA`
`PROMPT_PHYSICAL_HEIGHT_FEASIBILITY_QA`
`PROMPT_ITEM_BOUNDING_BOX_QA`
`PROMPT_ANSWER_ZONE_PRESERVATION_QA`
`PROMPT_PAGINATION_FALLBACK_QA`
`PROMPT_PAGE_POLICY_SERIALIZATION_QA`
`PROMPT_NUMERIC_INEQUALITY_CONSISTENCY_QA`
`PROMPT_OUTPUT_MODE_QA`
`PROMPT_FIELD_SEMANTICS_QA`
`PROMPT_QA_EVIDENCE_CONSISTENCY_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED` for the current compiled plan.

## Executable release gate

All prior tests remain. Counts may only increase.

1. core dry-run: 449
2. declared-skill matrix: 360
3. runtime UAT: 12
4. semantic oracle: 20
5. system-wide quality: 30
6. scale-line integrity: 40
7. instrument review/speedometer: 60
8. protractor scale safety: 24
9. full metrology audit: 80
10. actual weight-dial inactive-gap regression: 32
11. physical page feasibility regression: 48

Combined:

`1155/1155 PASS`

The newest suite is `tools/physical_page_feasibility_regression_suite.py`, derived directly from the consolidated user-supplied UAT reports. It must never be removed or weakened into a generic visual check.

## Package audit

Release package:

`activity-based-elementary-worksheet_Gem_v2.6.3_LTS_10WORKERS_TXT`

Must contain:
- one main Instructions TXT;
- exactly ten worker Knowledge TXT files;
- all five mandatory shared profiles embedded in main and worker bundles;
- W10 metrology worker;
- all regression reports including 32-case weight-gap and 48-case physical-page suites;
- actual-defect evidence documents;
- classroom artifact UAT guide;
- checksum manifest;
- ZIP integrity PASS.

Build only from GitHub SSOT after all gates pass. Use the exact CI artifact; do not rebuild locally and call it the CI artifact.

## Prompt/artifact boundary

Passing `1155/1155` establishes prompt-system/package coherence only.

Before actual rendered image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

One incorrect learner-read scale in an actual worksheet means:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and the defect becomes a permanent regression before the next accepted release.
