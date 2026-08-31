# Baseline 2.6.2-LTS Release Checklist

Status: Critical integration + instrument-safety release checklist
Applies to: `activity-based-elementary-worksheet` baseline 2.6.x
Release family: 2.6.2-LTS

## 1. Release intent

2.6.2-LTS is a base-architecture release, not a W10 hotfix.

Primary hardening goals:

- preserve all prior 2.6.x academic/visibility/layout contracts;
- make scale-line integrity mandatory for every learner-read scale;
- require a renderer-side review/revise loop before finalizing learner-read instruments;
- convert the 2026-08-31 actual ruler extra-tick defect into permanent regression evidence;
- add deterministic direct speedometer reading without silently introducing speed=distance/time calculation;
- strengthen thermometer deterministic reading/self-review behavior.

## 2. Required SSOT set

Core/governance:

- `GEM_INSTRUCTIONS_PRODUCTION.md`
- `OUTPUT_CONTRACT.md`
- `ARCHITECTURE.md`
- `KB_ROUTER.md`
- `KB_MANIFEST.md`
- `policies/PARAMETER_POLICY.md`
- `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
- `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
- `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md`
- `domains/DOMAIN_REGISTRY.md`
- `domains/MEASUREMENT_COVERAGE_P1_P6.md`
- `domains/INSTRUMENT_READING_ENGINE.md`

Deterministic instrument engines:

- `domains/CLOCK_READING_ENGINE.md`
- `domains/SCALE_READING_ENGINE.md`
- `domains/LENGTH_READING_ENGINE.md`
- `domains/SPEEDOMETER_READING_ENGINE.md`
- `domains/TEMPERATURE_READING_ENGINE.md`
- `domains/CAPACITY_READING_ENGINE.md`
- `domains/TABLE_GRAPH_READING_ENGINE.md`

Workers:

- W01..W09 worker contracts

Regression/QA:

- `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md`
- `qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md`
- `qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md`
- `qa/RUNTIME_UAT_CLOCK_REGRESSION_V2_6_X.md`
- `qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md`
- `qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md`
- `qa/DOMAIN_RELEASE_MATRIX.md`
- `tools/full_dry_run_suite.py`
- `tools/full_skill_matrix_suite.py`
- `tools/runtime_uat_regression_suite.py`
- `tools/semantic_oracle_regression_suite.py`
- `tools/system_wide_quality_regression_suite.py`
- `tools/scale_line_integrity_regression_suite.py`
- `tools/instrument_review_speedometer_regression_suite.py`

## 3. Worker/installation audit

Exactly nine base workers remain installed:

`W01_ACADEMIC_CONTENT`
`W02_TIME_CLOCK`
`W03_WEIGHT_SCALE`
`W04_LENGTH_DISTANCE`
`W05_TEMPERATURE_CAPACITY_VOLUME`
`W06_MONEY_CALENDAR_DATA`
`W07_INSTRUMENT_AUDITOR`
`W08_LAYOUT_RENDER_THAI`
`W09_QA_RELEASE`

Each declares:

`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

Every generated W01–W09 Knowledge bundle must embed, before worker/domain-specific SSOT:

1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`

Missing any mandatory shared profile = `KB_COMPATIBILITY_QA=FAIL`.

W04 bundle must include `SPEEDOMETER_READING_ENGINE.md`.
W05 bundle must include `TEMPERATURE_READING_ENGINE.md` and `CAPACITY_READING_ENGINE.md`.
W09 bundle must include the actual ruler extra-tick regression record.

## 4. Instrument academic-safety architecture

For every learner-read instrument/axis:

`INSTRUMENT_GEOMETRY > CONTEXT_ART > DECORATION`

Required architecture:

`OWNING DOMAIN STATE → W07 GEOMETRY/SCALE AUDIT → W08 LAYOUT + REVIEW-PROTOCOL SERIALIZATION → W09 CONJUNCTIVE RELEASE GATE`

Final prompt must include one resolved `SCALE_LINE_SPEC` when graduations/ticks/axis intervals are read.

Final prompt must include an `INSTRUMENT_REVIEW_REVISE_PROTOCOL` or exact semantic equivalent and:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Mandatory renderer-side logical loop:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

The review must be deterministic, referring to count/topology/alignment rather than a vague `looks correct` judgment.

Renderer self-review is prevention only; it never changes the prompt/artifact boundary.

## 5. Scale-line integrity audit

Every learner-read scale must resolve:

- topology family;
- active range;
- minor and major interval;
- exact interval count;
- exact physical position count;
- scale direction;
- authoritative baseline/ring/arc;
- tick anchoring mode;
- major/minor hierarchy;
- endpoint behavior;
- inactive-region rule when applicable;
- minimum printed instrument size;
- minimum tick-center spacing.

Default print lower bounds unless a domain requires more:

- minor tick stroke >= 0.25 mm;
- major tick stroke >= 0.35 mm;
- major tick length >= 1.5× minor tick length;
- adjacent smallest instructional tick centers >= 0.60 mm.

Reject:

- missing/extra/duplicated/merged/floating/detached ticks;
- nonuniform spacing for equal values;
- reversed local scale direction;
- labels that cover or displace scale lines;
- fake graduations created by borders, decoration or text strokes;
- pointer/hand/ray/level endpoints that do not meet the target reading position;
- value ticks in inactive/non-scale regions;
- scale-template drift across repeated instruments.

## 6. Permanent actual ruler UAT regression

The user-supplied 2026-08-31 rendered ruler crop exposed extra graduation marks in a one-centimetre span.

Canonical oracle:

`1 cm = 10 mm`

At 1 mm resolution, one complete adjacent-centimetre span must contain:

`INTERVALS_PER_CM=10`
`POSITIONS_PER_CM_SPAN=11`
`INTERIOR_POSITIONS_PER_CM_SPAN=9`
`PHYSICAL_EDGE_IS_GRADUATION=NO`

The 5 mm intermediate hierarchy mark occupies one existing 1 mm position and does not add a new position.

The renderer-side self-review must independently recount each canonical 1 cm span before finalization.

Any actual-render mismatch:

`ARTIFACT_SCALE_INTERVAL_COUNT_QA=FAIL`
`ARTIFACT_SCALE_POSITION_COUNT_QA=FAIL`
`ARTIFACT_RULER_SUBDIVISION_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

This regression is permanent. Never remove or weaken it to restore a green build.

## 7. Speedometer capability audit

Domain: `MEASUREMENT_SPEEDOMETER`
Owner: W04
Visual auditor: W07
Route: `W04 + W07 + W08 + W09`

Direct speedometer reading is an instrument-reading skill. It must not silently activate `speed=distance/time` calculation.

Canonical elementary default:

- range 0–120 km/h;
- topology `OPEN_ARC_BOUNDED`;
- 240° active sweep;
- start angle 240°;
- clockwise;
- major interval 20 km/h;
- minor interval 10 km/h;
- 12 active intervals;
- 13 active positions;
- 120° inactive gap with zero value ticks;
- exactly one instructional needle;
- `target_angle=(240+2*target_kmh) mod 360`.

Known-answer smoke oracles:

- 0 km/h → 240°
- 30 km/h → 300°
- 60 km/h → 0°
- 90 km/h → 60°
- 120 km/h → 120°

35 km/h is nonrepresentable in the default 10 km/h discrete profile.

## 8. Thermometer capability audit

Thermometer reading remains owned by W05 and audited by W07.

Required deterministic behavior:

- exact scale range and interval/position count;
- exact representability in discrete mode;
- monotonic direction;
- clear zero/minus/unit labels where applicable;
- liquid endpoint exactly on the target graduation centerline;
- no between-tick endpoint unless interpolation is explicitly taught;
- mandatory renderer self-review/revise protocol.

Canonical smoke profiles:

- 0–50°C @1°C → 50 intervals / 51 positions;
- 0–100°C @5°C → 20 / 21;
- -10–40°C @1°C → 50 / 51, zero index=10;
- 20–120°F @2°F → 50 / 51.

## 9. Other learner-read instrument smoke oracles

Clock:
- full minute face = 60 intervals / 60 distinct positions;
- 10:30 = minute 180°, hour 315°;
- nonzero-minute hour hand moves continuously.

Weight dial:
- canonical 0–5 kg = 300° active +60° inactive gap;
- 50 intervals /51 active positions at 0.1 kg;
- no gap ticks/full-circle substitution.

Protractor:
- 0–180° @1° = 180 intervals /181 positions;
- exact origin/baseline/direction;
- no wrong inner/outer scale interpretation.

Graduated container:
- exact interval/position count;
- exact level/meniscus reading point;
- no decorative competing reading line.

Graph axis:
- equal numeric intervals map to equal geometric spacing;
- bars/data marks map to canonical dataset;
- grid lines, if present, correspond to configured ticks and remain subordinate.

## 10. Mandatory review/revise QA gates

`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED`.

## 11. Mandatory scale-line QA gates

`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_SCALE_UNIFORM_SPACING_QA`
`PROMPT_SCALE_DIRECTION_QA`
`PROMPT_SCALE_LABEL_ALIGNMENT_QA`
`PROMPT_SCALE_LABEL_CLEARANCE_QA`
`PROMPT_SCALE_TARGET_ALIGNMENT_QA`
`PROMPT_SCALE_INACTIVE_REGION_QA` when applicable
`PROMPT_SCALE_DECORATION_ISOLATION_QA`
`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA`
`PROMPT_SCALE_LINE_SERIALIZATION_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED`.

## 12. Global release gates

Required applicable global gates include:

`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`WORKER_OWNERSHIP_QA`
`PROMPT_ACADEMIC_DATA_QA`
`PROMPT_STUDENT_BLUEPRINT_ISOLATION_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`
`PROMPT_UNIT_COMPATIBILITY_QA`
`PROMPT_UNIT_CONVERSION_QA`
`PROMPT_PAGE_LOCK_PROVENANCE_QA`
`RENDER_PATH_RESOLVED_QA`
`PROMPT_ONE_PAGE_FEASIBILITY_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`NO_PLACEHOLDER_QA`
`STUDENT_VISIBLE_ANSWER_LEAK_QA`
`STUDENT_VISIBLE_TARGET_TEXT_LEAK_QA`
`CANONICAL_LABEL_PRESERVATION_QA`

plus all applicable worker/domain/scale/review gates.

Critical QA is conjunctive. One applicable FAIL or NOT_RUN blocks release.

## 13. Executable release gate

A 2.6.2-LTS build candidate is eligible only when all current suites pass:

1. `tools/full_dry_run_suite.py` → 449/449
2. `tools/full_skill_matrix_suite.py` → 360/360
3. `tools/runtime_uat_regression_suite.py` → 12/12
4. `tools/semantic_oracle_regression_suite.py` → 20/20
5. `tools/system_wide_quality_regression_suite.py` → 30/30
6. `tools/scale_line_integrity_regression_suite.py` → 40/40
7. `tools/instrument_review_speedometer_regression_suite.py` → 60/60

Combined minimum:

`971/971 PASS`

The 60-case suite includes independent known-answer oracles for ruler, thermometer and speedometer plus architecture/runtime integration checks.

Regression counts may only increase. Never lower the count to make a release pass.

## 14. Package audit

Release package name:

`activity-based-elementary-worksheet_Gem_v2.6.2_LTS_9WORKERS_TXT`

Package must contain:

- one main Instructions `.txt`;
- exactly nine worker `.txt` Knowledge files;
- all three mandatory shared profiles embedded in main instructions and every worker bundle;
- W04 speedometer engine;
- W05 thermometer/capacity engines;
- actual ruler extra-tick regression record;
- SSOT validation report;
- all executable regression reports including 60-case review/speedometer report;
- checksum manifest;
- ZIP integrity PASS.

Build only from GitHub SSOT after all release gates pass.

## 15. Prompt/artifact boundary

Passing `971/971` establishes prompt-system/release-package coherence only.

Before actual rendered image inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Renderer self-review does not change this.

One incorrect learner-read scale in an actual worksheet:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

and requires a permanent regression before the next accepted release.

## 16. Release decision

2.6.2-LTS prompt-generation package may be marked READY only when:

- static SSOT validation passes;
- worker/route/profile compatibility passes;
- all 971 current executable regressions pass;
- package build and ZIP integrity pass;
- exact CI artifact corresponds to the passing HEAD commit;
- zero critical prompt blockers remain.

Actual classroom readiness still requires artifact inspection.
