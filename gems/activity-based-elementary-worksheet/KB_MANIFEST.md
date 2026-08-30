# KB Manifest — Activity-Based Elementary Worksheet Generator

Manifest version: 1.0.0
Gem baseline: 2.3.2
Status: Canonical KB installation inventory

## 1. Purpose

Use this manifest when installing/updating the Gem Knowledge Base. It records which files are required, which are conditional, and which versions are known compatible with Gem baseline 2.3.2.

The manifest prevents accidental installation of a new core with stale or missing supporting rules.

## 2. Required core files

| File | Required | Compatibility expectation |
|---|---:|---|
| `GEM_INSTRUCTIONS_PRODUCTION.md` | YES | version 2.3.2 |
| `OUTPUT_CONTRACT.md` | YES | version 2.3.2 |
| `ARCHITECTURE.md` | recommended | version 2.3.2 |
| `KB_ROUTER.md` | YES | version 1.0.0; baseline 2.3.2 |
| `KB_MANIFEST.md` | YES | version 1.0.0; baseline 2.3.2 |
| `policies/PARAMETER_POLICY.md` | YES | version 2.3.2 |
| `domains/DOMAIN_REGISTRY.md` | YES | version 2.3.2 |

## 3. Domain-engine files

All files below are recommended in the installed KB so the same Gem can route across all supported worksheet families. Their independent engine versions do not need to equal the Gem version; compatibility is controlled by behavior and this manifest.

| Domain | File(s) | Installation |
|---|---|---|
| shared instrument | `domains/INSTRUMENT_READING_ENGINE.md` | REQUIRED for any learner-read visual instrument |
| TIME | `domains/TIME_ENGINE.md` | recommended |
| TIME_CLOCK | `domains/CLOCK_READING_ENGINE.md` | recommended |
| MEASUREMENT_WEIGHT | `domains/SCALE_READING_ENGINE.md` | recommended |
| MEASUREMENT_LENGTH | `domains/LENGTH_READING_ENGINE.md` | recommended |
| MEASUREMENT_TEMPERATURE | `domains/TEMPERATURE_READING_ENGINE.md` | recommended |
| MEASUREMENT_CAPACITY | `domains/CAPACITY_READING_ENGINE.md` | recommended |
| MONEY | `domains/MONEY_ENGINE.md` | recommended |
| CALENDAR | `domains/CALENDAR_ENGINE.md` | recommended |
| DATA_READING | `domains/TABLE_GRAPH_READING_ENGINE.md` | recommended |

Known hardening expectations for baseline 2.3.2:

- clock engine must use continuous hour-hand interpolation;
- scale engine must lock canonical 300° active / 60° inactive gap for default 0–5 kg teaching dial;
- thermometer engine must require exact target representability/alignment for discrete scales;
- capacity engine must define explicit scientific meniscus read point and target-value leak protection;
- instrument engine must distinguish interval count from tick/graduation-position count.

## 4. QA / regression files

| File | Required condition |
|---|---|
| `qa/ACCEPTANCE_TESTS.md` | REQUIRED for production installation |
| `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md` | REQUIRED for production installation |
| `qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md` | REQUIRED for current visual-instrument production baseline |
| `qa/DOMAIN_RELEASE_MATRIX.md` | REQUIRED when reporting maturity/release readiness |
| domain-specific render tests | REQUIRED when applicable to a release claim |

## 5. Teacher/documentation files

These files improve maintenance and usability but do not override canonical academic rules:

- `USER_GUIDE.md`
- `README.md`
- `GEM_INSTALLATION_GUIDE.md`

## 6. Compatibility rule

`KB_COMPATIBILITY_QA=PASS` requires:

1. all required core files exist;
2. their declared baseline is compatible with Gem 2.3.2;
3. selected domain engine(s) exist;
4. `INSTRUMENT_READING_ENGINE.md` exists when a visual instrument domain is selected;
5. required QA/regression files exist;
6. no known stale core/output/parameter/registry file overrides the current baseline.

A lower independent domain-engine version number is not automatically incompatible. Judge against required behaviors listed in this manifest and the selected regression tests.

## 7. Installation profile — full supported Gem

Recommended full Knowledge upload set:

```text
OUTPUT_CONTRACT.md
ARCHITECTURE.md
KB_ROUTER.md
KB_MANIFEST.md
policies/PARAMETER_POLICY.md
domains/DOMAIN_REGISTRY.md
domains/INSTRUMENT_READING_ENGINE.md
domains/TIME_ENGINE.md
domains/CLOCK_READING_ENGINE.md
domains/SCALE_READING_ENGINE.md
domains/LENGTH_READING_ENGINE.md
domains/TEMPERATURE_READING_ENGINE.md
domains/CAPACITY_READING_ENGINE.md
domains/MONEY_ENGINE.md
domains/CALENDAR_ENGINE.md
domains/TABLE_GRAPH_READING_ENGINE.md
qa/ACCEPTANCE_TESTS.md
qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md
qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md
qa/DOMAIN_RELEASE_MATRIX.md
USER_GUIDE.md
```

`GEM_INSTRUCTIONS_PRODUCTION.md` is preferably used as the Gem's main Instructions. If the platform also stores it in Knowledge, the Instructions copy remains authoritative for core behavior.

## 8. Upgrade procedure

When changing the Gem baseline:

1. review core, output contract, architecture, parameter policy, registry, router and manifest together;
2. preserve independent domain rules unless intentionally changed;
3. update/extend regression tests before declaring the new baseline ready;
4. update this manifest;
5. update teacher/install documentation;
6. synchronize external command catalogs that explicitly name the Gem baseline.

Do not change the baseline number merely because a single domain engine received an independent patch.