# Baseline 2.6.0-LTS Release Checklist

Status: Critical integration checklist
Applies to: `activity-based-elementary-worksheet` baseline 2.6.x

## Required SSOT set

- `GEM_INSTRUCTIONS_PRODUCTION.md` — 2.6.0-LTS
- `OUTPUT_CONTRACT.md` — 2.6.0-LTS
- `ARCHITECTURE.md` — 2.6.0-LTS
- `KB_ROUTER.md` — 2.6.0-LTS
- `KB_MANIFEST.md` — 2.6.0-LTS
- `policies/PARAMETER_POLICY.md` — 2.6.0-LTS
- `policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md`
- `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
- `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
- `domains/INSTRUMENT_READING_ENGINE.md`
- `domains/DOMAIN_REGISTRY.md` — 2.6.0-LTS
- `domains/MEASUREMENT_COVERAGE_P1_P6.md`
- W01..W09 worker contracts
- `qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md`
- `qa/MEASUREMENT_EXPANSION_REGRESSION_V2_6_0.md`
- `qa/CLOCK_DAY_NIGHT_SINGLE_FACE_REGRESSION_V2_6_X.md`
- `qa/RUNTIME_UAT_CLOCK_REGRESSION_V2_6_X.md`
- `qa/DOMAIN_RELEASE_MATRIX.md`
- applicable older actual-render regressions
- `tools/full_dry_run_suite.py`
- `tools/full_skill_matrix_suite.py`
- `tools/runtime_uat_regression_suite.py`
- `tools/semantic_oracle_regression_suite.py`
- `tools/system_wide_quality_regression_suite.py`
- `tools/scale_line_integrity_regression_suite.py`
- `examples/MEASUREMENT_COMMAND_CATALOG_P1_P6.md`

## Worker audit

Exactly 9 base workers:

`W01_ACADEMIC_CONTENT`
`W02_TIME_CLOCK`
`W03_WEIGHT_SCALE`
`W04_LENGTH_DISTANCE`
`W05_TEMPERATURE_CAPACITY_VOLUME`
`W06_MONEY_CALENDAR_DATA`
`W07_INSTRUMENT_AUDITOR`
`W08_LAYOUT_RENDER_THAI`
`W09_QA_RELEASE`

Each declares `BASELINE_COMPATIBILITY=2.6.x` and `WORKER_SCHEMA_VERSION=1`. Worker IDs must be unique.

At runtime every W01–W09 bundle must inherit both `policies/SYSTEM_WIDE_QUALITY_PROFILE.md` and `policies/SCALE_LINE_INTEGRITY_PROFILE.md` before worker/domain-specific SSOT.

## Core architecture audit

Verify core contains Orchestrator role, worker routing/ownership, three visibility scopes, Student Blueprint target isolation, measurement P1–P6 coverage, exact relations/formulas, high-risk visual serialization, canonical-label preservation, single render path, one-page-first semantics, Thai/theme separation, answer-key behavior, prompt/artifact QA distinction, health check and hotfix policy.

Missing a major contract = FAIL.

## System-wide quality audit

All production skills inherit the shared quality profile. Verify:

- ownership conflicts are resolved by SSOT ownership, not final-prose overrides;
- material non-default parameters have provenance;
- generated academic states have independent verification, not tautological checks only;
- exact requested item count is preserved in student and renderer states;
- difficulty is not silently weakened to simplify layout/generation;
- accidental degenerate target sets are rejected when variety is part of the objective;
- Student Blueprint and renderer metadata remain structurally isolated;
- high-risk per-item renderer state is serialized atomically with explicit fields;
- wide Markdown tables are not used where wrapping/column drift can change renderer-state meaning;
- `ONE_PAGE_LOCK=OFF` never compiles to hard `exactly one page` wording;
- final prompt is self-contained;
- QA PASS must match the actual compiled structure;
- prompt QA never claims downstream artifact correctness.

Applicable shared gates:

`SYSTEM_OWNERSHIP_INTEGRITY_QA`
`SYSTEM_PARAMETER_PROVENANCE_QA`
`SYSTEM_INDEPENDENT_ORACLE_QA`
`SYSTEM_ITEM_COUNT_QA`
`SYSTEM_DIFFICULTY_FIDELITY_QA`
`SYSTEM_TARGET_DISTRIBUTION_QA`
`SYSTEM_VISIBILITY_ISOLATION_QA`
`PROMPT_RENDER_STATE_SERIALIZATION_QA`
`PROMPT_PAGE_POLICY_WORDING_QA`
`SYSTEM_FINAL_PROMPT_SELF_CONTAINED_QA`
`PROMPT_QA_EVIDENCE_CONSISTENCY_QA`
`SYSTEM_PHASE_BOUNDARY_QA`

Any applicable FAIL blocks prompt release.

## Scale-line integrity audit — mandatory for every learner-read scale

Applies to clock marks, dial scales, rulers, thermometers, graduated containers, protractors and numeric graph axes.

Verify the final prompt resolves one canonical `SCALE_LINE_SPEC` per learner-read scale template with:

- topology family and active range;
- minor/major interval;
- exact interval and physical position count;
- scale direction;
- one authoritative baseline/ring/arc;
- tick anchor mode;
- major/minor hierarchy;
- endpoint behavior;
- inactive-region rule when applicable;
- minimum printed instrument size;
- `MIN_TICK_CENTER_SPACING_MM`.

Scale-line physical/print constraints:

- no floating or detached ticks;
- equal value intervals use equal spacing;
- no missing, extra, duplicated or merged graduation;
- major marks remain consistently stronger than minor marks;
- default minor stroke >= 0.25 mm at final print size;
- default major stroke >= 0.35 mm;
- major tick length >= 1.5× minor tick length;
- adjacent smallest instructional tick centers >= 0.60 mm unless a stronger domain minimum applies;
- labels align to intended major marks and never cover/shift scale lines;
- target pointer/hand/ray/level/endpoint intersects the exact reading position;
- inactive gaps contain no value ticks;
- theme/decorative strokes do not resemble graduations, pointers, rays, grid lines or continuation of the scale;
- repeated instruments sharing one scale use identical scale-line geometry.

Mandatory applicable gates:

`PROMPT_SCALE_LINE_SPEC_QA`
`PROMPT_SCALE_TICK_ANCHOR_QA`
`PROMPT_SCALE_MAJOR_MINOR_HIERARCHY_QA`
`PROMPT_SCALE_PRINT_SEPARATION_QA`
`PROMPT_SCALE_UNIFORM_SPACING_QA`
`PROMPT_SCALE_DIRECTION_QA`
`PROMPT_SCALE_LABEL_ALIGNMENT_QA`
`PROMPT_SCALE_LABEL_CLEARANCE_QA`
`PROMPT_SCALE_TARGET_ALIGNMENT_QA`
`PROMPT_SCALE_INACTIVE_REGION_QA`
`PROMPT_SCALE_DECORATION_ISOLATION_QA`
`PROMPT_SCALE_TEMPLATE_CONSISTENCY_QA`
`PROMPT_SCALE_LINE_SERIALIZATION_QA`

Any applicable FAIL or NOT_RUN forces `PROMPT_RELEASE=BLOCKED`.

## Thai P3 analog-clock runtime audit

For Thai Grade 3 analog-clock AUTO requests, verify:

- AUTO resolves to `DAY_NIGHT_PAIR` unless explicit SINGLE intent
- one question = exactly one analog clock
- exactly two blank student response fields, `กลางวัน` and `กลางคืน`
- strict half-hour intent = minute `30` only unless mixed whole-hour request is explicit
- deterministic day/night mapping
- exact numeric hand angles per renderer item
- relational wording + item-specific hard negative
- Student Blueprint contains no target time, answer pair or angles
- `ONE_PAGE_LOCK=OFF` unless exact-one-page intent is explicit
- canonical clock topology is not degraded to force page fit
- renderer state uses atomic per-item blocks so angle/relation/hard-negative fields cannot drift across columns
- clock minute/hour scale marks also satisfy the mandatory scale-line integrity profile

Any violation = FAIL and `PROMPT_RELEASE=BLOCKED`.

## Measurement capability audit

Verify deterministic rules for time/clock, length/distance, angle/perimeter/area, weight/scale, temperature/capacity/volume, money/calendar/data and every declared visual/data mapping. Grade progression and explicit user objective control difficulty; layout pressure never changes academic meaning.

## Required integration gates

`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`WORKER_OWNERSHIP_QA`
`PROMPT_ACADEMIC_DATA_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`
`PROMPT_UNIT_COMPATIBILITY_QA` when applicable
`PROMPT_UNIT_CONVERSION_QA` when applicable
`PROMPT_TIME_UNIT_CONVERSION_QA` when applicable
`PROMPT_CLOCK_MODE_RESOLUTION_QA` when clock mode applies
`PROMPT_HALF_HOUR_INTENT_QA` when strict half-hour applies
`PROMPT_DAY_NIGHT_MAPPING_QA` when paired mode applies
`PROMPT_DAY_NIGHT_SINGLE_FACE_QA` when paired mode applies
`PROMPT_DAY_NIGHT_TWO_BLANKS_QA` when paired mode applies
`PROMPT_PER_ITEM_RENDER_STATE_QA` for learner-read visuals
`PROMPT_PAGE_LOCK_PROVENANCE_QA`
`PROMPT_PROTRACTOR_TOPOLOGY_QA` when applicable
`PROMPT_PROTRACTOR_BASELINE_QA` when applicable
`PROMPT_AREA_FORMULA_QA` when applicable
`PROMPT_AREA_UNIT_CONVERSION_QA` when applicable
`PROMPT_PI_POLICY_QA` when applicable
`PROMPT_CUBIC_UNIT_CONVERSION_QA` when applicable
`RENDER_PATH_RESOLVED_QA`
`PROMPT_ONE_PAGE_FEASIBILITY_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`NO_PLACEHOLDER_QA`
`STUDENT_VISIBLE_ANSWER_LEAK_QA`
`STUDENT_VISIBLE_TARGET_TEXT_LEAK_QA`
`CANONICAL_LABEL_PRESERVATION_QA`
plus all applicable system-wide, scale-line and owning-worker/domain gates.

## Executable release gate

A build candidate is eligible only when all current suites pass:

1. `tools/full_dry_run_suite.py` → `449/449 PASS`
2. `tools/full_skill_matrix_suite.py` → `360/360 PASS`
3. `tools/runtime_uat_regression_suite.py` → `12/12 PASS`
4. `tools/semantic_oracle_regression_suite.py` → `20/20 PASS`
5. `tools/system_wide_quality_regression_suite.py` → `30/30 PASS`
6. `tools/scale_line_integrity_regression_suite.py` → `40/40 PASS`

The semantic-oracle suite uses fixed known-answer expectations so the release gate is not composed only of token or formula-vs-itself checks. The system-wide suite validates cross-worker contracts. The scale-line suite verifies that every learner-read scale family is covered by one mandatory runtime profile and release-blocking CI gate.

Combined minimum:

`911/911 PASS`

A real UAT, domain, scale-line or QA-architecture defect must be represented by a permanent regression before the next accepted release artifact. Never lower the case count to make a release pass.

## High-risk smoke tests

1. Thai P3 half-hour clock AUTO → DAY_NIGHT_PAIR, one face, two blanks, minute 30 only, page lock OFF unless explicit.
2. 10:30 clock → minute 180°, hour 315°, midpoint 10–11, not on 10.
3. Clock full minute face → 60 distinct positions, common reference ring, no merged/floating ticks.
4. Time conversion → 2 h 5 min 30 s = 7530 s; no automatic seconds hand.
5. Canonical 0–5 kg dial → 300° active +60° gap, 50/51 topology, no gap ticks or 360° substitution.
6. Ruler 1 cm @1 mm → 10 intervals/11 positions; cm marks stronger than mm marks; common baseline.
7. Nonzero ruler start → `end-start`.
8. Distance round trip → double only when same route explicit.
9. Protractor 0–180° @1° → 180 intervals/181 positions; exact origin/baseline/direction; scale marks readable.
10. Triangle area → use perpendicular height.
11. 1 m² → 10,000 cm²; reject ×100.
12. Discrete thermometer target → represented exactly on a valid graduation; labels aligned; scale lines uniform.
13. Bottom/top meniscus → designated read point exact and no target-number annotation; container scale has no competing decorative lines.
14. Rectangular prism → compatible units before `l×w×h`.
15. 1 m³ → 1,000,000 cm³; reject linear-factor conversion.
16. Bar graph axis → uniform value interval maps to uniform tick spacing; bar height aligns to axis mapping.
17. Student Blueprint → no renderer target values.
18. Final prompt → one resolved render path and every required item state.
19. High-risk item serialization → atomic labeled block, no column drift.
20. `ONE_PAGE_LOCK=OFF` → preferred-one-page wording with safe pagination preserved.
21. QA report → cannot PASS a gate contradicted by compiled prompt structure.
22. Before image inspection → `ARTIFACT_QA=NOT_YET_TESTED`.

## Prompt/artifact boundary

Passing this checklist means the prompt-generation baseline is internally coherent. It does not mean third-party rendered worksheets are classroom-ready.

Before artifact inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Actual scale-line correctness remains artifact QA until every rendered instructional scale is visually inspected.

## Installation package audit

Compact package must contain:

- one main Instructions `.txt`
- exactly nine worker `.txt` Knowledge files
- mandatory system-wide quality profile embedded in main instructions and every worker Knowledge bundle
- mandatory scale-line integrity profile embedded in main instructions and every worker Knowledge bundle
- no `.md` dependency required for Gemini upload
- install/health-check guide
- SSOT validation report
- core dry-run report
- full skill-matrix report
- runtime UAT regression report
- semantic-oracle regression report
- system-wide quality regression report
- scale-line integrity regression report
- checksum manifest

Knowledge slot 10 remains free unless an approved narrow hotfix is shipped.

## Release decision

Baseline 2.6.0 prompt-generation release may be marked READY only when static consistency, worker compatibility, all `911` current regression cases, package integrity and SSOT/package coherence pass with zero critical blockers.
