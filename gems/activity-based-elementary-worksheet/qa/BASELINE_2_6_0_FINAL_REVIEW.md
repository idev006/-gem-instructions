# Baseline 2.6.0-LTS — Final Review Record

Status: ACTIVE LTS REVIEW RECORD — REFRESHED AFTER RUNTIME UAT HARDENING
Product: `activity-based-elementary-worksheet`
Product role: `PRODUCTION_WORKSHEET_PROMPT_GENERATOR`
Primary deliverable: `FINAL_IMAGE_GENERATION_PROMPT`

## 1. Review scope

The 2.6.0-LTS consolidation and subsequent hardening reviewed and aligned:

- Gem Orchestrator instructions
- Specialist Worker architecture and ownership
- compact 9-Knowledge installation model
- runtime Knowledge dependency bundling
- output/visibility contract
- prompt-vs-artifact QA semantics
- render-path resolution
- one-page-first behavior and explicit lock provenance
- Thai/text/print constraints
- P1–P6 measurement capability/progression
- measurement formulas/unit conversion
- instrument topology/geometry
- Thai Grade 3 analog-clock runtime behavior
- real-UAT-to-regression workflow
- regression and release-evidence governance
- installation/build pipeline
- automated SSOT validation and CI

## 2. Final architecture

The runtime architecture is:

`USER REQUEST → ORCHESTRATOR → OWNING SPECIALIST WORKER(S) → W07 INSTRUMENT AUDIT WHEN VISUAL → W08 LAYOUT/RENDER/THAI → W09 QA/RELEASE → FINAL_IMAGE_GENERATION_PROMPT`

Base workers:

1. `W01_ACADEMIC_CONTENT`
2. `W02_TIME_CLOCK`
3. `W03_WEIGHT_SCALE`
4. `W04_LENGTH_DISTANCE`
5. `W05_TEMPERATURE_CAPACITY_VOLUME`
6. `W06_MONEY_CALENDAR_DATA`
7. `W07_INSTRUMENT_AUDITOR`
8. `W08_LAYOUT_RENDER_THAI`
9. `W09_QA_RELEASE`

Knowledge slot 10 remains reserved for a narrow compatible `W10_HOTFIX_OVERRIDE`.

## 3. Runtime packaging model

`tools/build_install_package.py` derives the compact installation package from GitHub SSOT.

The compact runtime package bundles supporting SSOT into the appropriate Knowledge worker:

- W02 bundle includes Time + Clock engines and clock runtime profiles/specs
- W03 bundle includes Scale engine
- W04 bundle includes Length engine
- W05 bundle includes Temperature + Capacity engines
- W06 bundle includes Money + Calendar + Table/Graph engines
- W07 bundle includes shared Instrument engine
- W09 bundle includes Output Contract, Architecture, Router, Manifest, Parameter Policy, Domain Registry, Measurement Coverage and critical QA/regression/release files

Repository filenames inside generated Knowledge are provenance/logical references, not missing runtime dependencies.

The generated package contains one Orchestrator Instructions file plus exactly nine Knowledge TXT files; slot 10 remains free for a compatible narrow hotfix.

## 4. Current executable release gate

The historical 449-case core suite alone is **not** considered full release coverage.

Current minimum executable prompt-system gate:

- core deterministic/policy suite: `449/449 PASS`
- declared-skill extended matrix: `360/360 PASS`
- real-runtime UAT regression suite: `12/12 PASS`
- combined minimum: `821/821 PASS`

The package builder must block when any current suite fails or is not run.

A real UAT defect must be converted into a permanent regression before a subsequent release artifact is accepted. Test counts must not be reduced merely to obtain a passing release.

These suites validate prompt-system rules and deterministic policy; they do not replace downstream rendered-artifact inspection.

## 5. Runtime UAT hardening — Thai P3 analog clock

A real installed-Gem UAT exposed behavior that static/deterministic suites did not initially catch: a generic Thai P3 half-hour analog-clock command could regress to one answer field, infer `ONE_PAGE_LOCK=ON`, omit exact numeric angles, or degrade clock topology.

The canonical runtime profile is now elevated to Orchestrator-level instructions and protected by a dedicated runtime UAT regression suite.

For:

`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ไม่มีเฉลย`

required behavior is:

- Thai P3 analog-clock `AUTO → DAY_NIGHT_PAIR` unless explicit SINGLE intent
- exactly one analog clock face per question
- exactly two blank response fields: `กลางวัน` and `กลางคืน`
- strict half-hour intent means minute `30` only unless mixed whole-hour items are explicitly requested
- deterministic day/night mapping
- one shared hand state for both interpretations
- every high-risk clock item includes semantic target + exact numeric angles + relational wording + item-specific hard negative
- Student Blueprint contains no target time, answer pair or angles
- `ONE_PAGE_LOCK=OFF` unless the user explicitly requires exactly one page
- canonical instructional topology must not be degraded to force page fit

Any violation is a runtime regression and must block prompt release when applicable.

## 6. Formal P1–P6 measurement coverage

Baseline 2.6.x formally covers, when grade/objective appropriate:

### Time / clock
- analog clock reading
- start/end/duration calculation
- schedules/day-night
- hour/minute/second conversion
- controlled midnight crossing
- seconds-hand guard

### Length / ruler / distance
- zero/nonzero ruler reading
- mm/cm/m/km
- length arithmetic/comparison/conversion
- distance total/difference/round trip/multi-segment/route comparison
- no implicit speed/rate conversion

### Angle / protractor
- angle classification
- semicircular and supported full-circle protractor reading
- exact origin/baseline/target graduation
- explicit scale direction where applicable

### Perimeter / area
- polygon perimeter
- rectangle/square perimeter and area
- triangle/parallelogram/trapezoid area when grade/objective supports
- circle area/circumference when explicitly requested
- one consistent `PI_POLICY`
- squared-unit conversion

### Weight / dial
- g/kg arithmetic/conversion
- Thai `ขีด` relation when applicable
- canonical 0–5 kg dial reading

### Temperature
- thermometer reading
- exact discrete target representability/alignment

### Capacity
- mL/L reading/arithmetic/conversion
- flat level
- explicit top/bottom scientific meniscus when requested

### Solid volume
- rectangular prism
- simple composite non-overlapping rectangular prisms
- cm³/dm³/m³ conversion
- capacity-volume relations only when explicitly taught

Canonical progression: `domains/MEASUREMENT_COVERAGE_P1_P6.md`.

## 7. Critical deterministic relations

Time:
- `60 s=1 min`
- `60 min=1 h`
- `24 h=1 day`

Length:
- `10 mm=1 cm`
- `100 cm=1 m`
- `1000 m=1 km`

Area:
- `1 m²=10,000 cm²`
- `1 km²=1,000,000 m²`

Weight:
- `1000 g=1 kg`
- Thai context: `1 ขีด=100 g=0.1 kg`

Capacity:
- `1000 mL=1 L`

Volume:
- `1000 cm³=1 dm³`
- `1000 dm³=1 m³`
- `1 m³=1,000,000 cm³`

When explicitly taught:
- `1 cm³=1 mL`
- `1 dm³=1 L`
- `1 m³=1000 L`

Squared/cubic unit conversions must use squared/cubed linear factors respectively.

## 8. High-risk visual regressions retained

### Clock
10:30:
- minute hand 180°
- hour hand 315°
- exact midpoint 10–11
- never directly on 10

### Canonical 0–5 kg dial
- 300° active sweep
- 60° inactive gap
- 50 intervals / 51 positions
- zero ticks inside gap
- no 360° substitution

### Ruler
1 cm @1 mm:
- 10 intervals
- 11 endpoint-inclusive positions
- physical edge is not automatically zero

### Protractor
0–180° @1°:
- 180 intervals
- 181 positions
- exact origin
- selected 0° baseline
- active scale unambiguous

### Thermometer / capacity
- discrete target exactly representable
- endpoint/read point exactly on target graduation
- no hidden target-number annotation

## 9. Visibility/release semantics

Three scopes are mandatory:

1. `INTERNAL_VERIFIED_STATE`
2. `TEACHER_VISIBLE_PROMPT_METADATA`
3. `STUDENT_VISIBLE_WORKSHEET`

Renderer state is marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

Student Blueprint must not expose target answers, target times, weights, lengths, angles, tick indices, ray angles, liquid levels or renderer relation strings.

Before actual artifact inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Prompt correctness is not a claim that downstream rendered pixels/glyphs/geometry are correct.

## 10. Automated validation/build

Required release workflow runs:

1. `tools/validate_ssot.py`
2. `tools/full_dry_run_suite.py`
3. `tools/full_skill_matrix_suite.py`
4. `tools/runtime_uat_regression_suite.py`
5. `tools/build_install_package.py`
6. ZIP integrity verification
7. installation-artifact upload

`.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml` is the CI release gate.

The authoritative release evidence is the successful GitHub Actions run for the current candidate HEAD. Do not rely on an older hard-coded workflow run or artifact digest after SSOT changes.

## 11. Domain maturity decision

Documentation/rule expansion does not by itself prove downstream-render maturity.

Expanded measurement domains remain conservatively governed by `qa/DOMAIN_RELEASE_MATRIX.md` until promotion evidence is met.

No domain is promoted merely because deterministic formulas or prompt-level regression are present.

## 12. Known boundaries

The following are intentionally not claimed as specialized deterministic 2.6 coverage:

- speed/rate/velocity as an automatic extension of distance
- arbitrary complex 3D solids outside rectangular-prism/simple composite grammar
- a universal mandatory curriculum sequence for every school
- guaranteed correctness of nondeterministic downstream image pixels without artifact inspection

## 13. Release decision

### Prompt-generation baseline

`BASELINE_2_6_0_LTS=READY_FOR_INSTALLATION_UAT` only when the **current candidate HEAD** has a successful CI run with all current gates, including `821/821` minimum regression cases and package/ZIP checks.

### Artifact/classroom status

`ARTIFACT_QA=NOT_YET_TESTED` for any newly generated worksheet until its actual rendered artifact is inspected.

This review approves the Gem prompt-generation architecture and release process; it does not grant automatic classroom release to every downstream worksheet image.
