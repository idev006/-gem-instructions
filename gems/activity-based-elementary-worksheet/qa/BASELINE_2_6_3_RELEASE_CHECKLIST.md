# Baseline 2.6.3-LTS Release Checklist

Status: Critical educational-instrument safety release checklist
Release family: 2.6.3-LTS
Compatible worker baseline: 2.6.x / schema 1

## Release principle

`ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER`

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

Passing this checklist qualifies the **prompt/package system**. It never proves downstream pixels. Actual worksheets still require Artifact QA before classroom release.

## Base architecture

Exactly 10 base workers:

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

Five mandatory shared runtime profiles:

1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `METROLOGY_ASSURANCE_PROFILE.md`
5. `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Mandatory learner-read chain:

`OWNING DOMAIN → W07 GEOMETRY AUDIT → W10 INDEPENDENT METROLOGY AUDIT → W08 LAYOUT/RENDER → W09 RELEASE`

## Correct canonical instrument oracles

### Weight dial 0–5 kg @0.1 kg

- angle convention: `0° = top`, clockwise positive;
- 50 active intervals / 51 endpoint-inclusive active positions;
- 300° active sweep from 0° to 300°;
- inactive open gap `(300°,360°)`;
- `INACTIVE_GAP_TICK_COUNT=0`;
- `INACTIVE_GAP_RADIAL_MARK_COUNT=0`;
- `LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`;
- `CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]`;
- `active_tick_angle(i)=(6*i) mod 360`;
- `NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`.

The superseded rotated label map is forbidden in current authoritative SSOT.

### Speedometer 0–120 km/h @10

- 12 intervals / 13 positions;
- 240° active /120° inactive gap;
- `target_angle=(240+2*target_kmh) mod 360`;
- 60 km/h →0°→straight up under this family convention;
- `NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`;
- pointer ray is collinear center→target tick.

### Ruler 1 cm @1 mm

- 10 intervals /11 endpoint-inclusive positions /9 interior positions;
- physical ruler edge is not an additional graduation;
- 5 mm hierarchy mark reuses an existing position.

### Thermometer 0–50°C @1°C

- 50 intervals /51 positions;
- 6 major positions: 0,10,20,30,40,50;
- 5 intermediate positions: 5,15,25,35,45;
- 40 ordinary minor positions;
- each complete 10°C span =10 intervals /9 interior positions;
- liquid endpoint equals target graduation centerline;
- a selected 60 mm scale has exactly 1.20 mm tick-center spacing.

### Protractor 0–180° @1°

- perfect upper semicircle;
- 180 intervals /181 positions;
- one active numeric scale by default unless dual-scale reading is explicitly taught;
- 0° right /90° top /180° left;
- 10° major /5° intermediate /1° minor, all reusing the 181 positions;
- `ARC_CENTER == BASELINE_MIDPOINT == RAY_ORIGIN == TICK_RADIAL_CENTER`;
- ticks and target ray radial from the common center;
- no ellipse, shear, perspective, skew, or non-uniform stretch;
- radial print-spacing oracle at 1° and 0.60 mm floor gives minimum reading-ring diameter≈68.76 mm and production width 70 mm; 65 mm fails;
- **shape-aware page rule:** width 70 mm means semicircle geometric body height 35 mm before labels/answer/clearance reserves. Do not infer item height as 70 mm merely from width.

## Physical page feasibility

For A4 portrait: 210×297 mm before margins.

A PASS requires numeric `PHYSICAL_PAGE_STATE` covering margins, header/title/directions, rows/columns, complete shape-aware item bounding boxes, answer zones, row/column gaps, usable dimensions and required dimensions.

`ONE_PAGE_PREFERRED != ONE_PAGE_LOCKED`.

When `ONE_PAGE_LOCK=OFF`, an infeasible preferred plan is recomputed or paginated. No worker may delete/merge/compress scale marks to force one page.

Examples:
- five 80 mm circular dials require at least 400 mm body height → impossible on A4 portrait;
- five 60 mm vertical thermometer scales require at least 300 mm before other content → impossible;
- five 50 mm container boxes consume 250 mm before header/gaps → full proof required;
- protractor uses **shape-aware** semicircle height `W/2` plus explicit reserves, never `height=W` by assumption;
- graph axis height alone never proves full worksheet fit.

## Required prompt/artifact invariants

- `OUTPUT_MODE=PROMPT_PACKAGE` is distinct from `RENDER_PATH`;
- exact learner-read geometry uses deterministic geometry;
- all radial/angular instruments require common-center/common-origin evidence;
- all scale labels require label-to-tick association and monotonic order where applicable;
- renderer prevention loop:
  `GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`;
- `NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`;
- renderer self-review is prevention, never artifact proof.

## Permanent actual defects retained

- ruler extra graduation;
- weight-dial inactive-gap radial marks;
- weight-dial label-order/coordinate drift;
- speedometer off-center pivot;
- thermometer incorrect subdivision/hierarchy;
- distorted/misregistered protractor;
- physical page feasibility contradictions.

See:
- `ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md`
- `ACTUAL_WEIGHT_DIAL_INACTIVE_GAP_REGRESSION_2026_08_31.md`
- `ACTUAL_INSTRUMENT_GEOMETRY_DEFECTS_2026_08_31.md`
- `CONSOLIDATED_PHYSICAL_PAGE_FEASIBILITY_REGRESSION_2026_08_31.md`

## Executable release gate

All prior tests remain; counts only increase.

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
12. actual instrument geometry regression: 64
13. repository full-line audit: 81

Combined mandatory gate:

`1300/1300 PASS`

The repository full-line audit scans every UTF-8 text/code line in the Gem SSOT plus its GitHub workflow for encoding/control/merge-marker hazards and applies 81 semantic coherence assertions. It is additive to, not a replacement for, domain regression suites.

## Package audit

Release package name:

`activity-based-elementary-worksheet_Gem_v2.6.3_LTS_10WORKERS_TXT`

Must contain:
- one main Instructions TXT;
- exactly ten worker Knowledge TXT files;
- all five shared profiles embedded in main and worker bundles;
- W10 metrology worker;
- actual defect evidence;
- reports for all 13 regression suites including 64-case actual instrument geometry and 81-case repository full-line audit;
- classroom Artifact UAT guide;
- checksum manifest;
- ZIP integrity PASS.

Use the exact GitHub Actions artifact only after all gates pass.

## Prompt / artifact boundary

Passing `1300/1300 PASS` means:

`PROMPT_RELEASE=APPROVED`

Before actual rendered worksheet inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

One incorrect learner-read instrument in an actual worksheet means:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and that defect becomes a permanent regression before the next accepted release.
