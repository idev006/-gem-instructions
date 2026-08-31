# Baseline 2.6.3-LTS Release Checklist

Status: Critical educational-instrument safety release checklist
Release family: 2.6.3-LTS
Compatible worker baseline: 2.6.x / schema 1

## Release intent

2.6.3-LTS promotes independent metrology engineering into the base architecture. The objective is educational safety: every learner-read measuring instrument must be quantitatively correct before prompt release, and actual rendered pixels still require artifact inspection before classroom release.

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

## Mandatory learner-read chain

`OWNING DOMAIN → W07 GEOMETRY AUDIT → W10 INDEPENDENT METROLOGY AUDIT → W08 LAYOUT/RENDER → W09 RELEASE`

W10 must independently recompute quantitative evidence rather than repeat W07.

Required W10 state: `METROLOGY_AUDIT_STATE` with count, spacing, reference, target alignment, label association, inactive region when applicable, print feasibility and independent verdict.

Missing W10 evidence = `PROMPT_METROLOGY_AUDIT_REQUIRED_QA=FAIL` and `PROMPT_RELEASE=BLOCKED`.

## Universal scale audit

For every learner-read clock, dial, ruler, speedometer, protractor, thermometer, graduated container or graph axis verify:

- topology and active range;
- exact interval count;
- exact position count;
- zero/origin/reference/baseline;
- direction/monotonicity;
- uniform geometric spacing;
- print spacing at actual scale;
- major/intermediate/minor hierarchy without extra positions;
- common tick anchoring;
- label association/clearance;
- target representability;
- pointer/hand/ray/liquid/meniscus/bar endpoint alignment;
- inactive-region integrity;
- decoration isolation;
- canonical-template consistency;
- print/photocopy readability;
- page feasibility.

`ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER`.

## Known-answer metrology oracles

Clock:
- 60 intervals / 60 distinct positions;
- 6° per minute position;
- 10:30 → minute 180°, hour 315°.

Weight dial:
- 0–5 kg @0.1 kg → 50 active intervals / 51 positions;
- canonical active sweep 300°, inactive gap 60°.

Ruler:
- 1 cm @1 mm → 10 intervals / 11 positions / 9 interior positions;
- `PHYSICAL_EDGE_IS_GRADUATION=NO`;
- 5 mm hierarchy mark is an existing position.

Speedometer:
- 0–120 km/h @10 → 12 intervals / 13 positions;
- 240° active / 120° inactive gap;
- 60 km/h → 0° in canonical mapping;
- 35 km/h is not representable in discrete 10 km/h mode.

Protractor:
- 0–180° @1° → 180 intervals / 181 positions;
- `tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)`;
- 0.60 mm floor → minimum radius ≈34.38 mm, diameter ≈68.76 mm, production width 70 mm;
- 65 mm is rejected;
- final render path must use deterministic instrument geometry;
- mirrored competing scale forbidden unless dual-scale interpretation is explicitly taught.

Thermometer:
- 0–50°C @1°C → 50/51;
- 0–100°C @5°C → 20/21;
- -10–40°C @1°C → zero index 10;
- liquid endpoint on target graduation centerline.

Graduated container:
- endpoint-inclusive count from configured range/interval;
- target level/meniscus read convention exact;
- no decorative competing scale.

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

Applicable metrology gates include:

`PROMPT_METROLOGY_AUDIT_REQUIRED_QA`
`PROMPT_METROLOGY_INDEPENDENCE_QA`
`PROMPT_METROLOGY_INTERVAL_COUNT_QA`
`PROMPT_METROLOGY_POSITION_COUNT_QA`
`PROMPT_METROLOGY_REFERENCE_QA`
`PROMPT_METROLOGY_SPACING_ORACLE_QA`
`PROMPT_METROLOGY_HIERARCHY_QA`
`PROMPT_METROLOGY_LABEL_ASSOCIATION_QA`
`PROMPT_METROLOGY_TARGET_ALIGNMENT_QA`
`PROMPT_METROLOGY_INACTIVE_REGION_QA`
`PROMPT_METROLOGY_TEMPLATE_CONSISTENCY_QA`
`PROMPT_METROLOGY_RENDER_PATH_QA`
`PROMPT_METROLOGY_PAGE_FEASIBILITY_QA`
`PROMPT_METROLOGY_PRINT_FEASIBILITY_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED`.

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

Combined:

`1075/1075 PASS`

The new suite is `tools/metrology_full_audit_regression_suite.py` and audits all learner-read scale families plus W10/package integration.

## Package audit

Release package:

`activity-based-elementary-worksheet_Gem_v2.6.3_LTS_10WORKERS_TXT`

Must contain:
- one main Instructions TXT;
- exactly ten worker Knowledge TXT files;
- all four mandatory shared profiles embedded in main and worker bundles;
- W10 metrology worker;
- full metrology audit report;
- all previous regression reports;
- checksum manifest;
- ZIP integrity PASS.

Build only from GitHub SSOT after all gates pass. Use the exact CI artifact; do not rebuild locally and call it the CI artifact.

## Prompt/artifact boundary

Passing `1075/1075` establishes prompt-system/package coherence only.

Before actual rendered image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

One incorrect learner-read scale in an actual worksheet means:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and the defect becomes a permanent regression before the next accepted release.
