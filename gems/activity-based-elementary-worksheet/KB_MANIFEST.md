# KB Manifest — Activity-Based Elementary Worksheet Generator

Manifest version: 2.6.3-LTS
Gem baseline: 2.6.x
Worker schema: 1
Status: Canonical production installation inventory

## 1. Production installation model

Gemini Knowledge file limit is treated as 10 files. Baseline 2.6.3-LTS uses **10 base Knowledge workers**. Slot 10 is now the independent measurement/metrology engineer, not a hotfix override.

The main Gem Instructions field uses `GEM_INSTRUCTIONS_PRODUCTION.md` and is not counted as one of the ten Knowledge workers.

## 2. Required workers

| Worker ID | Repository SSOT | Installation role |
|---|---|---|
| W01_ACADEMIC_CONTENT | `workers/W01_ACADEMIC_CONTENT.md` | arithmetic/color-by-code/Thai literacy/generic content |
| W02_TIME_CLOCK | `workers/W02_TIME_CLOCK.md` | time units/calculation + analog clock |
| W03_WEIGHT_SCALE | `workers/W03_WEIGHT_SCALE.md` | weight + dial scale |
| W04_LENGTH_DISTANCE | `workers/W04_LENGTH_DISTANCE.md` | ruler + length + distance + speedometer + angle/protractor + perimeter/area |
| W05_TEMPERATURE_CAPACITY_VOLUME | `workers/W05_TEMPERATURE_CAPACITY_VOLUME.md` | thermometer + capacity + meniscus + solid volume |
| W06_MONEY_CALENDAR_DATA | `workers/W06_MONEY_CALENDAR_DATA.md` | money + calendar + data reading |
| W07_INSTRUMENT_AUDITOR | `workers/W07_INSTRUMENT_AUDITOR.md` | shared geometry/topology/scale-line audit |
| W08_LAYOUT_RENDER_THAI | `workers/W08_LAYOUT_RENDER_THAI.md` | layout/render/Thai/print/theme + review serialization |
| W09_QA_RELEASE | `workers/W09_QA_RELEASE.md` | integration QA/release |
| W10_METROLOGY_ENGINEER | `workers/W10_METROLOGY_ENGINEER.md` | independent metrology, printed scale feasibility and measurement second-opinion audit |

Every base worker declares:

`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## 3. Mandatory shared runtime profiles

Every W01–W10 Knowledge bundle embeds before worker/domain-specific SSOT:

1. `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
3. `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `policies/METROLOGY_ASSURANCE_PROFILE.md`

Missing any mandatory shared profile from a built worker bundle is `KB_COMPATIBILITY_QA=FAIL`.

## 4. Independent instrument-safety chain

Whenever a student reads a visual scale:

`OWNING DOMAIN → W07 GEOMETRY AUDIT → W10 METROLOGY AUDIT → W08 LAYOUT/RENDER → W09 RELEASE`

W10 must independently recompute quantitative evidence. It may not merely echo W07 PASS.

Mandatory learner-read state includes:

`SCALE_LINE_SPEC`
`INSTRUMENT_REVIEW_REVISE_PROTOCOL`
`METROLOGY_AUDIT_STATE`
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

## 5. Repository support files

Installable bundles include/derive from:

- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `OUTPUT_CONTRACT.md`
- `ARCHITECTURE.md`
- `KB_ROUTER.md`
- `KB_MANIFEST.md`
- all four mandatory shared profiles
- `domains/DOMAIN_REGISTRY.md`
- `domains/MEASUREMENT_COVERAGE_P1_P6.md`
- `domains/INSTRUMENT_READING_ENGINE.md`
- deterministic domain engines including speedometer, thermometer and capacity
- actual-render regressions
- `tools/metrology_full_audit_regression_suite.py`

## 6. Compatibility rule

`KB_COMPATIBILITY_QA=PASS` requires:

1. W01..W10 all exist and are unique;
2. each declares baseline 2.6.x and schema 1;
3. W08/W09 are available for every production request;
4. W07 + W10 are both available whenever learner-read geometry is selected;
5. all four mandatory shared profiles are embedded in every generated worker bundle;
6. route/ownership rules match `KB_ROUTER.md` and `DOMAIN_REGISTRY.md`;
7. speedometer engine is embedded with W04;
8. thermometer/capacity engines are embedded with W05;
9. W10 includes metrology assurance profile and instrument engine context;
10. all critical QA/regression files are coherent.

## 7. Measurement capability requirements

Baseline 2.6.x supports, when grade/objective appropriate:

- clock reading;
- weight/dial reading;
- ruler and nonzero-start reading;
- direct speedometer reading;
- angle/protractor reading;
- thermometer reading;
- capacity/meniscus reading;
- learner-read graph axes;
- related arithmetic/conversions owned by W02–W06.

Direct speedometer reading does not automatically enable speed-rate calculation.

## 8. Known hardening requirements

- clock: 60 minute intervals / 60 distinct positions and continuous hour-hand interpolation;
- weight dial: canonical 0–5 kg = 50/51 active topology + 60° gap;
- ruler 1 cm @1 mm:
  - `INTERVALS_PER_CM=10`
  - `POSITIONS_PER_CM_SPAN=11`
  - `INTERIOR_POSITIONS_PER_CM_SPAN=9`
  - `PHYSICAL_EDGE_IS_GRADUATION=NO`
- speedometer canonical 0–120 km/h = 12/13 active topology, 240° active arc, 120° gap;
- protractor 0–180° @1° = 180/181, independent print-spacing oracle, production width 70 mm at 0.60 mm spacing floor;
- thermometer exact interval/position count and endpoint alignment;
- graduated-container exact read convention and no competing scale lines;
- graph-axis equal-value interval → equal physical interval;
- renderer-only target and audit data stays out of Student Blueprint;
- final render path resolves to one value;
- no blind first-pass release;
- W10 independent evidence required before W09 approval;
- renderer self-review and W10 prompt audit never masquerade as artifact QA.

## 9. Update policy

Architecture/routing changes, visibility/output changes, shared profile changes, new deterministic engines, or critical cross-domain measurement changes require base SSOT update + permanent regression + full CI + reinstall.

## 10. Installation artifact

The distributed ZIP must contain:

- one main Instructions `.txt`;
- exactly ten worker `.txt` Knowledge files;
- all four mandatory shared profiles embedded in main instructions and every worker bundle;
- install/health-check guide;
- static SSOT validation report;
- all regression reports including full metrology audit;
- checksum manifest;
- ZIP integrity PASS.

The package is generated from GitHub SSOT and CI, not maintained as a separate competing specification.
