# KB Manifest — Activity-Based Elementary Worksheet Generator

Manifest version: 2.6.3-LTS
Gem baseline: 2.6.x
Worker schema: 1
Status: Canonical production installation inventory

## 1. Production installation model

Gemini Knowledge file limit is treated as 10 files. Baseline 2.6.3-LTS uses **10 base Knowledge workers**. W10 is the independent measurement/metrology engineer, not a hotfix override.

The main Gem Instructions field uses generated Orchestrator Instructions and is not counted as one of the ten Knowledge workers.

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

## 3. Mandatory runtime profiles

Every W01–W10 Knowledge bundle embeds five technical safety profiles:

1. `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
3. `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `policies/METROLOGY_ASSURANCE_PROFILE.md`
5. `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Every bundle also embeds the mandatory learner-facing profile:

6. `policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`

The architecture continues to refer to the first five as the **five mandatory technical shared profiles**. The pedagogy profile is a separate mandatory cross-cutting learner contract, not a sixth base worker.

Missing any required runtime profile from a built worker bundle is `KB_COMPATIBILITY_QA=FAIL`.

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

Academic geometry additionally requires:
`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES`
`CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES`
`POST_LAYOUT_GEOMETRY_TRANSFORM=UNIFORM_SCALE_AND_TRANSLATE_ONLY`

## 5. Primary-school learner-safety contract

Every production route is subject to `PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md` whether or not it contains an instrument.

It checks grade appropriateness, instruction clarity, ambiguity, typography, response writing space, visual load, decoration isolation, item progression, answer-format alignment, print contrast and child-view artifact simulation.

Default page format when the user gives no override is A4 Portrait. Pagination may use multiple A4 Portrait pages when unlocked.

## 6. Repository support files

Installable bundles include/derive from:
- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `OUTPUT_CONTRACT.md`
- `ARCHITECTURE.md`
- `KB_ROUTER.md`
- `KB_MANIFEST.md`
- all five technical shared profiles
- `PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`
- deterministic domain engines
- actual artifact regression evidence
- clean-room pedagogy root-cause audit
- full metrology, geometry, physical-page, pedagogy and repository full-line regression tools.

## 7. Compatibility rule

`KB_COMPATIBILITY_QA=PASS` requires:
1. W01..W10 all exist and are unique;
2. each declares baseline2.6.x and schema1;
3. W08/W09 available for every production request;
4. W07+W10 both available whenever learner-read geometry is selected;
5. all five technical profiles and the pedagogy profile embedded in every generated worker bundle;
6. route/ownership matches `KB_ROUTER.md` and registry;
7. speedometer engine embedded with W04;
8. thermometer/capacity engines embedded with W05;
9. W10 includes metrology and instrument context;
10. all critical QA/regression files are coherent.

## 8. Measurement capability requirements

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

## 9. Known hardening requirements

- clock: 60 minute positions, shared pivot, continuous hour hand and deterministic vector endpoint;
- weight dial: top-zero clockwise,50/51, exactly10 intervals/9 interior marks per kg, +0.5kg intermediate hierarchy, inactive gap clean, pivot=center;
- ruler: 10/11/9 per cm, edge not tick, endpoint projections;
- speedometer:12/13,240° active/120° gap,pivot=center,radial pointer;
- protractor: perfect upper semicircle,180/181,single active scale default,common origin,radial ticks,width>=70mm,shape-aware height;
- thermometer:50/51,6 major/5 intermediate/40 minor,local-span count,endpoint aligned;
- graduated container: global and local span counts exact;
- graph: canonical data mapped to exact 2D axis geometry;
- renderer target/audit data stays out of Student Blueprint;
- final render path resolves to one value;
- academic geometry uses locked vector primitives;
- numeric shape-aware page proof before page-fit PASS;
- learner typography/writability/visual-load gates before prompt release;
- renderer self-review and W10 prompt audit never masquerade as artifact QA.

## 10. Update policy

Architecture/routing/visibility/shared-profile/pedagogy/domain-geometry/critical measurement changes require base SSOT update + permanent regression + full CI + reinstall.

## 11. Installation artifact

Distributed ZIP must contain:
- one main Instructions `.txt`;
- exactly ten worker `.txt` Knowledge files;
- all five technical profiles plus mandatory pedagogy profile embedded in main/worker bundles;
- install/health-check guide;
- static SSOT validation report;
- all current regression reports including primary-school pedagogy and repository full-line audit;
- clean-room pedagogy audit;
- checksum manifest;
- ZIP integrity PASS.

Package is generated from GitHub SSOT/CI and never maintained as competing specification.
