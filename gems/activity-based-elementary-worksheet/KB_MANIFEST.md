# KB Manifest — Activity-Based Elementary Worksheet Generator

Manifest version: 2.6.3-LTS
Gem baseline: 2.6.x
Worker schema: 1
Status: Canonical production installation inventory

## 1. Production installation model

Gemini Knowledge file limit is treated as 10 files. Baseline 2.6.3-LTS uses **10 base Knowledge workers**. W10 is the independent measurement/metrology engineer, not a hotfix override.

The main Gem Instructions field uses `GEM_INSTRUCTIONS_PRODUCTION.md` and is not counted as one of the ten Knowledge workers.

## 2. Required workers

| Worker ID | Repository SSOT | Installation role |
|---|---|---|
| W01_ACADEMIC_CONTENT | `workers/W01_ACADEMIC_CONTENT.md` | arithmetic/color-by-code/Thai literacy/generic content |
| W02_TIME_CLOCK | `workers/W02_TIME_CLOCK.md` | time units/calculation + analog clock |
| W03_WEIGHT_SCALE | `workers/W03_WEIGHT_SCALE.md` | weight + dial scale |
| W04_LENGTH_DISTANCE | `workers/W04_LENGTH_DISTANCE.md` | ruler + length + distance + speedometer + protractor + perimeter/area |
| W05_TEMPERATURE_CAPACITY_VOLUME | `workers/W05_TEMPERATURE_CAPACITY_VOLUME.md` | thermometer + capacity + meniscus + solid volume |
| W06_MONEY_CALENDAR_DATA | `workers/W06_MONEY_CALENDAR_DATA.md` | money + calendar + data reading |
| W07_INSTRUMENT_AUDITOR | `workers/W07_INSTRUMENT_AUDITOR.md` | shared geometry/topology/scale-line/common-center audit |
| W08_LAYOUT_RENDER_THAI | `workers/W08_LAYOUT_RENDER_THAI.md` | shape-aware layout/render/Thai/print/theme + review serialization |
| W09_QA_RELEASE | `workers/W09_QA_RELEASE.md` | integration QA/release |
| W10_METROLOGY_ENGINEER | `workers/W10_METROLOGY_ENGINEER.md` | independent metrology, common-center/shape/print/page audit |

Every base worker declares:

`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## 3. Five mandatory shared runtime profiles

Every W01–W10 Knowledge bundle embeds before worker/domain-specific SSOT:

1. `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
3. `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `policies/METROLOGY_ASSURANCE_PROFILE.md`
5. `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Missing any mandatory shared profile from a built worker bundle is `KB_COMPATIBILITY_QA=FAIL`.

## 4. Independent instrument-safety chain

Whenever a student reads a visual scale:

`OWNING DOMAIN → W07 GEOMETRY AUDIT → W10 METROLOGY AUDIT → W08 LAYOUT/RENDER → W09 RELEASE`

W10 independently recomputes quantitative evidence and may not echo W07 PASS.

Mandatory learner-read state includes:

`SCALE_LINE_SPEC`
`INSTRUMENT_REVIEW_REVISE_PROTOCOL`
`METROLOGY_AUDIT_STATE`
`PHYSICAL_PAGE_STATE`
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

For radial/angular instruments it also includes authoritative common-center/origin evidence.

## 5. Repository support files

Installable bundles include/derive from:

- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `OUTPUT_CONTRACT.md`
- `ARCHITECTURE.md`
- `KB_ROUTER.md`
- `KB_MANIFEST.md`
- all five mandatory shared profiles
- deterministic domain engines
- actual artifact regression evidence
- full metrology, instrument geometry, physical-page and repository full-line regression tools.

## 6. Compatibility rule

`KB_COMPATIBILITY_QA=PASS` requires:

1. W01..W10 all exist and are unique;
2. each declares baseline2.6.x and schema1;
3. W08/W09 available for every production request;
4. W07+W10 both available whenever learner-read geometry is selected;
5. all five mandatory shared profiles embedded in every generated worker bundle;
6. route/ownership matches `KB_ROUTER.md` and registry;
7. speedometer engine embedded with W04;
8. thermometer/capacity engines embedded with W05;
9. W10 includes metrology and instrument context;
10. all critical QA/regression files are coherent.

## 7. Measurement capability requirements

Baseline2.6.x supports, grade/objective permitting:

- analog clock reading;
- weight/dial reading;
- ruler/nonzero-start reading;
- direct speedometer reading;
- angle/protractor reading;
- thermometer reading;
- capacity/meniscus reading;
- learner-read graph axes;
- related arithmetic/conversions owned by W02–W06.

Direct speedometer reading does not automatically enable speed-rate calculation.

## 8. Known hardening requirements

- clock: 60 minute positions and shared hand pivot;
- weight dial: top-zero clockwise labels `{0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`, 50/51 active, gap `(300°,360°)`, pivot=center;
- ruler 1cm @1mm: 10 intervals/11 positions/9 interior; edge not tick;
- speedometer 0–120 @10: 12/13, 240° active,120° gap, pivot=center, radial needle;
- protractor 0–180 @1°: perfect upper semicircle, 180/181, single active scale default, common center/origin, radial ticks, width70mm at0.60mm floor, shape-aware body height=W/2;
- thermometer 0–50 @1: 50/51, 6 major/5 intermediate/40 minor, 10 intervals per10°C, endpoint aligned;
- graduated container: exact read convention/no competing scale;
- graph axis: equal-value interval→equal physical interval;
- renderer target/audit data stays out of Student Blueprint;
- final render path resolves to one value;
- no blind first-pass release;
- numeric shape-aware page proof before page-fit PASS;
- renderer self-review and W10 prompt audit never masquerade as artifact QA.

## 9. Update policy

Architecture/routing/visibility/shared-profile/domain-geometry/critical measurement changes require base SSOT update + permanent regression + full CI + reinstall.

## 10. Installation artifact

Distributed ZIP must contain:

- one main Instructions `.txt`;
- exactly ten worker `.txt` Knowledge files;
- all five mandatory profiles embedded in main and every worker bundle;
- install/health-check guide;
- static SSOT validation report;
- all regression reports including actual instrument geometry and repository full-line audit;
- checksum manifest;
- ZIP integrity PASS.

Package is generated from GitHub SSOT/CI and never maintained as competing specification.
