# KB Manifest — Activity-Based Elementary Worksheet Generator

Manifest version: 2.6.0-LTS
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
| W04_LENGTH_DISTANCE | `workers/W04_LENGTH_DISTANCE.md` | ruler + length + distance + angle/protractor + perimeter/area |
| W05_TEMPERATURE_CAPACITY_VOLUME | `workers/W05_TEMPERATURE_CAPACITY_VOLUME.md` | thermometer + capacity + meniscus + solid volume |
| W06_MONEY_CALENDAR_DATA | `workers/W06_MONEY_CALENDAR_DATA.md` | money + calendar + data reading |
| W07_INSTRUMENT_AUDITOR | `workers/W07_INSTRUMENT_AUDITOR.md` | shared geometry/topology audit |
| W08_LAYOUT_RENDER_THAI | `workers/W08_LAYOUT_RENDER_THAI.md` | layout/render/Thai/print/theme |
| W09_QA_RELEASE | `workers/W09_QA_RELEASE.md` | integration QA/release |

Every base worker must declare:

`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## 3. Optional hotfix

Knowledge slot 10 may contain `W10_HOTFIX_OVERRIDE` only.

Required declaration:

`APPLIES_TO_BASELINE=2.6.x`
`TARGET_WORKER`
`SCOPE`
`REPLACED_RULE`
`NEW_RULE`
`REGRESSION_TEST`

Do not use slot 10 for a second full worker set or broad architecture override.

## 4. Repository support files

SSOT/supporting references merged/translated into the installable worker package where appropriate:

- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `OUTPUT_CONTRACT.md`
- `ARCHITECTURE.md`
- `KB_ROUTER.md`
- `KB_MANIFEST.md`
- `policies/PARAMETER_POLICY.md`
- `domains/DOMAIN_REGISTRY.md`
- `domains/MEASUREMENT_COVERAGE_P1_P6.md`
- domain engines
- QA/regression files
- `examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md`

These repository files do not need to be uploaded separately when using the compact 9-worker installation package.

## 5. Compatibility rule

`KB_COMPATIBILITY_QA=PASS` requires:

1. W01..W09 all exist;
2. each worker ID is unique;
3. each declares baseline 2.6.x;
4. each declares schema 1;
5. W08/W09 are available for every production request;
6. W07 is available whenever learner-read visual geometry is selected;
7. no incompatible W10 override is active;
8. route/ownership rules match `KB_ROUTER.md`;
9. baseline-critical QA/regression files are coherent with the same capability set.

## 6. Measurement expansion requirements

Baseline 2.6.x must support, when grade/objective appropriate:

### Time
- analog clock reading
- elapsed/start/end/duration calculation
- `60 s=1 min`, `60 min=1 h`, `24 h=1 day`
- second precision only when explicitly requested/warranted

### Length / distance / measurement geometry
- ruler zero/nonzero reading
- length arithmetic/comparison
- mm/cm/m/km conversion
- distance total/difference/round trip/multi-segment/route comparison
- angle reading with a protractor
- perimeter
- supported elementary area formulas
- squared-unit conversion
- one consistent `PI_POLICY` for circle tasks

### Weight
- dial reading
- g/kg/ขีด arithmetic/conversion
- optional metric tonne only when explicitly requested

### Temperature / capacity / volume
- thermometer reading
- mL/L capacity reading/arithmetic/conversion
- meniscus convention when explicitly requested
- rectangular-prism/simple composite rectangular-prism volume
- cm³/dm³/m³ conversion
- capacity-volume relations only when explicitly taught

See `domains/MEASUREMENT_COVERAGE_P1_P6.md`.

## 7. Known hardening requirements

- clock continuous hour-hand interpolation; 10:30 = 315° midpoint 10–11
- seconds hand only when the lesson explicitly includes seconds
- canonical 0–5 kg dial = 300° active + 60° inactive gap; no 360° substitution
- ruler 1 cm @1 mm = 10 intervals / 11 positions
- nonzero ruler measurement = end-start
- protractor vertex at exact origin, baseline on selected 0°, active scale direction explicit
- area conversion uses squared linear factors; cubic conversion uses cubed linear factors
- thermometer discrete target must be representable and align to a graduation
- scientific meniscus read point explicit and unambiguous
- renderer-only target data must not appear in Student Blueprint or learner-visible worksheet
- canonical labels must survive leak guards
- final render path must resolve to one value
- prompt QA must not masquerade as artifact QA

## 8. Update policy

For baseline-compatible narrow defects, prefer one W10 hotfix.

Require full base reinstall only for:

- worker schema change
- architecture/routing change
- visibility/output-contract change
- cross-domain critical rule change
- changes to multiple base workers that cannot safely be expressed as one narrow override

## 9. Installation artifact

The distributed ZIP should contain:

- `01_MAIN_INSTRUCTIONS/GEM_ORCHESTRATOR_INSTRUCTIONS.txt`
- `02_UPLOAD_9_WORKER_KNOWLEDGE_TXT/` with exactly nine `.txt` workers
- installation/health-check guide
- smoke tests
- static lint report
- manifest/checksums

The package is generated from GitHub SSOT, not maintained as a separate competing specification.