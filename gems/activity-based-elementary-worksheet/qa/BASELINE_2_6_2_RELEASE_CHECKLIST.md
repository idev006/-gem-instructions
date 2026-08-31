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
- strengthen thermometer deterministic reading/self-review behavior;
- harden protractor printed tick spacing, render-path resolution, active-scale isolation and intermediate-mark consistency.

## 2. Required SSOT and executable QA

Required governance/runtime files include `GEM_INSTRUCTIONS_PRODUCTION.md`, `OUTPUT_CONTRACT.md`, `ARCHITECTURE.md`, `KB_ROUTER.md`, `KB_MANIFEST.md`, parameter/system/scale/review profiles, domain registry/measurement coverage, W01–W09 contracts, and deterministic instrument engines.

Required executable suites:

- `tools/full_dry_run_suite.py`
- `tools/full_skill_matrix_suite.py`
- `tools/runtime_uat_regression_suite.py`
- `tools/semantic_oracle_regression_suite.py`
- `tools/system_wide_quality_regression_suite.py`
- `tools/scale_line_integrity_regression_suite.py`
- `tools/instrument_review_speedometer_regression_suite.py`
- `tools/protractor_scale_safety_regression_suite.py`

Permanent actual-render evidence includes `qa/ACTUAL_RULER_EXTRA_TICK_REGRESSION_2026_08_31.md`.

## 3. Worker/installation audit

Exactly nine base workers remain installed: W01 through W09. Each declares `BASELINE_COMPATIBILITY=2.6.x` and `WORKER_SCHEMA_VERSION=1`.

Every generated worker Knowledge bundle embeds:

1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`

Missing a mandatory profile is a compatibility failure.

## 4. Instrument academic-safety architecture

For every learner-read instrument:

`INSTRUMENT_GEOMETRY > CONTEXT_ART > DECORATION`

Required chain:

`OWNING DOMAIN STATE → W07 GEOMETRY/SCALE AUDIT → W08 LAYOUT + REVIEW-PROTOCOL SERIALIZATION → W09 CONJUNCTIVE RELEASE GATE`

Final prompt requires resolved `SCALE_LINE_SPEC`, `INSTRUMENT_REVIEW_REVISE_PROTOCOL`, and:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

Required renderer loop:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Renderer review is prevention, not artifact proof.

## 5. Shared scale-line integrity audit

Every learner-read scale resolves topology, range, minor/major intervals, interval/position counts, direction, authoritative baseline/ring/arc, anchoring, hierarchy, endpoint behavior, inactive region if applicable, minimum printed size, minimum tick-center spacing and a computed print-spacing oracle for dense scales.

Default print lower bounds:

- minor stroke ≥ 0.25 mm;
- major stroke ≥ 0.35 mm;
- major length ≥ 1.5× minor;
- adjacent smallest instructional tick centers ≥ 0.60 mm.

Reject missing/extra/merged/floating ticks, nonuniform spacing, reversed direction, ambiguous labels, fake decorative ticks, target misalignment, inactive-region ticks, template drift, or any layout compression that violates the resolved spacing oracle.

## 6. Permanent ruler regression

Canonical relation:

`1 cm = 10 mm`

At 1 mm resolution:

`INTERVALS_PER_CM=10`
`POSITIONS_PER_CM_SPAN=11`
`INTERIOR_POSITIONS_PER_CM_SPAN=9`
`PHYSICAL_EDGE_IS_GRADUATION=NO`

A 5 mm hierarchy mark reuses an existing 1 mm position. It never adds a new position. The actual 2026-08-31 extra-tick defect remains a permanent blocker regression.

## 7. Protractor scale-placement safety — mandatory

For a semicircular 0–180° protractor at 1° resolution:

- 180 equal intervals;
- 181 endpoint-inclusive positions;
- exact origin and baseline;
- exact target ray;
- one clearly active reading direction unless dual-scale interpretation is explicitly taught;
- no perspective/skew;
- smallest instructional graduation remains 1°.

Printed spacing oracle:

`tick_center_spacing_mm = reading_radius_mm × radians(minor_interval_deg)`

At 1° and `MIN_TICK_CENTER_SPACING_MM=0.60`:

`MIN_READING_RADIUS_MM≈34.38`
`MIN_READING_RING_DIAMETER_MM≈68.76`
`PRODUCTION_MIN_PROTRACTOR_WIDTH_MM=70`

A 65 mm diameter protractor is invalid because 1° spacing is only about 0.567 mm.

A learner-read 1° protractor must use deterministic vector instrument geometry. Final prompt may not contain unresolved `RENDER_PATH=AUTO` for that instrument.

A mirrored competing inner scale is forbidden by default. If per-item verification references 5° ticks, 5° intermediate marks are REQUIRED and must reuse existing 1° positions.

If explicit `ONE_PAGE_LOCK=ON` cannot preserve 70 mm minimum width, labels, margins and answer space, `PROMPT_ONE_PAGE_FEASIBILITY_QA=FAIL` and `PROMPT_RELEASE=BLOCKED`. Never shrink below the verified minimum.

Required gates include:

`PROMPT_PROTRACTOR_TOPOLOGY_QA`
`PROMPT_PROTRACTOR_BASELINE_QA`
`PROMPT_PROTRACTOR_DIRECTION_QA`
`PROMPT_PROTRACTOR_PRINT_SPACING_QA`
`PROMPT_PROTRACTOR_ACTIVE_SCALE_QA`
`PROMPT_PROTRACTOR_RENDER_PATH_QA`
`PROMPT_PROTRACTOR_INTERMEDIATE_HIERARCHY_QA`
`PROMPT_SCALE_PRINT_SPACING_ORACLE_QA`

## 8. Speedometer capability audit

Direct speedometer reading remains W04 + W07 + W08 + W09. Canonical default: 0–120 km/h, 240° active open arc, 20 km/h major, 10 km/h minor, 12 intervals / 13 positions, 120° inactive gap, one needle, `target_angle=(240+2*target_kmh) mod 360`. Do not silently introduce `speed=distance/time`.

## 9. Thermometer capability audit

W05 + W07 must preserve exact range topology, representability, monotonic direction, labels and exact liquid-endpoint alignment. Canonical smoke cases include 0–50°C @1°C = 50/51 and 0–100°C @5°C = 20/21. No between-tick endpoint unless interpolation is explicitly taught.

## 10. Other learner-read smoke oracles

- Clock: 60 minute positions; 10:30 → minute 180°, hour 315°.
- Weight dial: canonical 0–5 kg = 300° active +60° gap; 50/51 at 0.1 kg.
- Graduated container: exact intervals/positions and exact liquid/meniscus read point.
- Graph axis: equal numeric intervals map to equal geometry; bars/data align to canonical dataset.

## 11. Mandatory scale/review QA gates

Scale family includes:

`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_SCALE_PRINT_SPACING_ORACLE_QA`
`PROMPT_SCALE_UNIFORM_SPACING_QA`
`PROMPT_SCALE_DIRECTION_QA`
`PROMPT_SCALE_LABEL_ALIGNMENT_QA`
`PROMPT_SCALE_LABEL_CLEARANCE_QA`
`PROMPT_SCALE_TARGET_ALIGNMENT_QA`
`PROMPT_SCALE_INACTIVE_REGION_QA`
`PROMPT_SCALE_DECORATION_ISOLATION_QA`
`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA`
`PROMPT_SCALE_LINE_SERIALIZATION_QA`

Review family includes:

`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`

Any applicable FAIL or NOT_RUN blocks release.

## 12. Global release gates

Global applicable gates include route, compatibility, ownership, academic data, Student Blueprint isolation, grade appropriateness, unit/formula checks, page-lock provenance, `RENDER_PATH_RESOLVED_QA`, `PROMPT_ONE_PAGE_FEASIBILITY_QA`, completeness, copy-ready, no placeholders, leak guards and canonical-label preservation.

Critical QA is conjunctive.

## 13. Executable release gate

A 2.6.2-LTS build candidate is eligible only when all current suites pass:

1. `full_dry_run_suite.py` → 449/449
2. `full_skill_matrix_suite.py` → 360/360
3. `runtime_uat_regression_suite.py` → 12/12
4. `semantic_oracle_regression_suite.py` → 20/20
5. `system_wide_quality_regression_suite.py` → 30/30
6. `scale_line_integrity_regression_suite.py` → 40/40
7. `instrument_review_speedometer_regression_suite.py` → 60/60
8. `protractor_scale_safety_regression_suite.py` → 24/24

Combined minimum:

`995/995 PASS`

Regression counts may only increase. Never lower the count to make a release pass.

## 14. Package audit

Package remains:

`activity-based-elementary-worksheet_Gem_v2.6.2_LTS_9WORKERS_TXT`

It must contain one main Instructions file, exactly nine worker Knowledge files, all mandatory embedded profiles, deterministic domain engines, actual ruler regression evidence, all executable regression reports including the protractor 24-case report, manifest/checksums and ZIP integrity PASS.

Build only from GitHub SSOT after all 995 gates pass.

## 15. Prompt/artifact boundary and release decision

Passing `995/995 PASS` establishes prompt-system/package coherence only.

Before actual rendered worksheet inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

One wrong learner-read scale in an actual worksheet yields:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

2.6.2-LTS prompt-generation package may be marked READY only when static SSOT validation, all 995 executable regressions, build, ZIP integrity and exact CI artifact/HEAD correspondence pass with zero critical prompt blockers.
