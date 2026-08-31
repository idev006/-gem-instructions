# KB Manifest — Activity-Based Elementary Worksheet Generator

Manifest version: 2.6.2-LTS
Gem baseline: 2.6.x
Worker schema: 1
Status: Canonical production installation inventory

## 1. Production installation model

Gemini Knowledge file limit is treated as 10 files. Baseline 2.6.x intentionally uses **9 base Knowledge workers** and reserves slot 10 for a narrow hotfix.

The main Gem Instructions field uses `GEM_INSTRUCTIONS_PRODUCTION.md` and is not counted as one of the nine Knowledge workers.

## 2. Required workers

| Worker ID | Repository SSOT | Installation role |
|---|---|---|
| W01_ACADEMIC_CONTENT | `workers/W01_ACADEMIC_CONTENT.md` | arithmetic/color-by-code/Thai literacy/generic content |
| W02_TIME_CLOCK | `workers/W02_TIME_CLOCK.md` | time units/calculation + analog clock |
| W03_WEIGHT_SCALE | `workers/W03_WEIGHT_SCALE.md` | weight + dial scale |
| W04_LENGTH_DISTANCE | `workers/W04_LENGTH_DISTANCE.md` | ruler + length + distance + speedometer + angle/protractor + perimeter/area |
| W05_TEMPERATURE_CAPACITY_VOLUME | `workers/W05_TEMPERATURE_CAPACITY_VOLUME.md` | thermometer + capacity + meniscus + solid volume |
| W06_MONEY_CALENDAR_DATA | `workers/W06_MONEY_CALENDAR_DATA.md` | money + calendar + data reading |
| W07_INSTRUMENT_AUDITOR | `workers/W07_INSTRUMENT_AUDITOR.md` | shared geometry/topology/scale-line/review audit |
| W08_LAYOUT_RENDER_THAI | `workers/W08_LAYOUT_RENDER_THAI.md` | layout/render/Thai/print/theme + review-protocol serialization |
| W09_QA_RELEASE | `workers/W09_QA_RELEASE.md` | integration QA/release |

Every base worker must declare:

`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## 3. Mandatory shared runtime profiles

Every W01–W09 Knowledge bundle must embed these profiles before worker/domain-specific SSOT:

1. `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
3. `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`

The scale/review profiles become operational when learner-read instruments/axes are present. They remain available to every worker so ownership and release semantics are consistent system-wide.

Missing any mandatory shared profile from a built worker bundle is `KB_COMPATIBILITY_QA=FAIL`.

## 4. Optional hotfix

Knowledge slot 10 may contain `W10_HOTFIX_OVERRIDE` only.

Required declaration:

`APPLIES_TO_BASELINE=2.6.x`
`TARGET_WORKER`
`SCOPE`
`REPLACED_RULE`
`NEW_RULE`
`REGRESSION_TEST`

Do not use slot 10 for broad architecture, cross-domain instrument safety, routing, visibility or review-loop changes. Those require base SSOT changes and full reinstall.

## 5. Repository support files

SSOT/supporting references merged into the installable worker package where appropriate include:

- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `OUTPUT_CONTRACT.md`
- `ARCHITECTURE.md`
- `KB_ROUTER.md`
- `KB_MANIFEST.md`
- `policies/PARAMETER_POLICY.md`
- all mandatory shared profiles
- `domains/DOMAIN_REGISTRY.md`
- `domains/MEASUREMENT_COVERAGE_P1_P6.md`
- `domains/INSTRUMENT_READING_ENGINE.md`
- domain engines including `SPEEDOMETER_READING_ENGINE.md`
- QA/regression files including actual-render regressions
- command examples/guides

These repository files do not need to be uploaded separately when using the compact 9-worker installation package.

## 6. Compatibility rule

`KB_COMPATIBILITY_QA=PASS` requires:

1. W01..W09 all exist;
2. each worker ID is unique;
3. each declares baseline 2.6.x and schema 1;
4. W08/W09 are available for every production request;
5. W07 is available whenever learner-read geometry is selected;
6. all 3 mandatory shared profiles are embedded in every generated worker bundle;
7. route/ownership rules match `KB_ROUTER.md` and `DOMAIN_REGISTRY.md`;
8. speedometer engine is embedded with W04;
9. thermometer engine is embedded with W05;
10. baseline-critical QA/regression files are coherent with the same capability set;
11. no incompatible W10 override is active.

## 7. Measurement capability requirements

Baseline 2.6.x supports, when grade/objective appropriate:

### Time
- analog clock reading
- elapsed/start/end/duration calculation
- exact time-unit relations

### Length / distance / speedometer / geometry
- ruler zero/nonzero reading
- exact mm/cm ruler subdivisions
- length arithmetic/comparison/conversion
- distance total/difference/round trip/multi-segment/route comparison
- **direct speedometer reading** with deterministic open-arc topology and needle mapping
- angle/protractor reading
- perimeter and supported area formulas
- squared-unit conversion and consistent `PI_POLICY`

Direct speedometer reading does not automatically enable speed-rate calculation.

### Weight
- dial reading
- g/kg/ขีด arithmetic/conversion

### Temperature / capacity / volume
- deterministic thermometer reading with exact graduation count/endpoint alignment
- mL/L reading/arithmetic/conversion
- meniscus convention when requested
- rectangular-prism/simple composite volume
- cm³/dm³/m³ conversion

### Money/calendar/data
- exact arithmetic/date/data mapping
- learner-read graph axes inherit scale-line/review profiles

## 8. Known hardening requirements

- clock continuous hour-hand interpolation and exact minute-mark topology
- canonical 0–5 kg dial active sweep/gap, no gap ticks
- ruler 1 cm @1 mm canonical serialization:
  - `INTERVALS_PER_CM=10`
  - `POSITIONS_PER_CM_SPAN=11`
  - `INTERIOR_POSITIONS_PER_CM_SPAN=9`
  - `PHYSICAL_EDGE_IS_GRADUATION=NO`
- speedometer canonical 0–120 km/h = 12 intervals / 13 positions, 240° active arc, 120° inactive gap
- protractor exact origin/baseline/direction
- thermometer exact interval/position count, scale direction and target endpoint
- graduated-container exact read point and no competing scale lines
- graph-axis uniform scale mapping
- canonical labels survive leak guards
- renderer-only target data stays out of Student Blueprint
- final render path resolves to one value
- `INSTRUMENT_REVIEW_REVISE_PROTOCOL` required for learner-read instruments
- no blind first-pass release of learner-read instruments
- renderer self-review never masquerades as artifact QA

## 9. Update policy

Require full base reinstall for architecture/routing changes, visibility/output-contract changes, shared scale/review profile changes, new deterministic domain engines, or multi-worker critical changes.

Use W10 only for genuinely narrow baseline-compatible defects.

## 10. Installation artifact

The distributed ZIP must contain:

- one main Instructions `.txt`
- exactly nine worker `.txt` Knowledge files
- mandatory shared profiles embedded in main instructions and every worker bundle
- install/health-check guide
- smoke tests/regression reports
- static SSOT validation report
- checksum manifest

The package is generated from GitHub SSOT and CI, not maintained as a separate competing specification.
