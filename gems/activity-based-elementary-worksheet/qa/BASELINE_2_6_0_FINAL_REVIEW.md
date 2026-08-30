# Baseline 2.6.0-LTS — Final Review Record

Status: FINAL REVIEW COMPLETED
Product: `activity-based-elementary-worksheet`
Product role: `PRODUCTION_WORKSHEET_PROMPT_GENERATOR`
Primary deliverable: `FINAL_IMAGE_GENERATION_PROMPT`

## 1. Review scope

The 2.6.0-LTS consolidation reviewed and aligned:

- Gem Orchestrator instructions
- Specialist Worker architecture and ownership
- compact 9-Knowledge installation model
- runtime Knowledge dependency bundling
- output/visibility contract
- prompt-vs-artifact QA semantics
- render-path resolution
- one-page-first behavior
- Thai/text/print constraints
- P1–P6 measurement capability/progression
- measurement formulas/unit conversion
- instrument topology/geometry
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

## 3. Runtime packaging repair

A critical installation-design risk was identified during final review: uploading only nine raw Worker files would leave references to supporting repository files such as domain engines, registry, policy and QA suites that are not separately uploaded to Gemini Knowledge.

This was repaired by `tools/build_install_package.py`.

The compact runtime package now bundles supporting SSOT into the appropriate Knowledge worker:

- W02 bundle includes Time + Clock engines
- W03 bundle includes Scale engine
- W04 bundle includes Length engine
- W05 bundle includes Temperature + Capacity engines
- W06 bundle includes Money + Calendar + Table/Graph engines
- W07 bundle includes shared Instrument engine
- W09 bundle includes Output Contract, Architecture, Router, Manifest, Parameter Policy, Domain Registry, Measurement Coverage and critical QA/regression/release files

Repository filenames inside generated Knowledge are treated as provenance/logical references, not missing runtime dependencies.

Result: the 9-file compact installation is runtime-complete without requiring the repository `.md` files to be uploaded separately.

## 4. Formal P1–P6 measurement coverage

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
- semicircular protractor reading
- exact origin/baseline/target graduation
- explicit left-zero/right-zero and inner/outer scale direction

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

## 5. Critical deterministic relations

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

## 6. High-risk visual regressions retained

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
- active inner/outer scale unambiguous

### Thermometer / capacity
- discrete target exactly representable
- endpoint/read point exactly on target graduation
- no hidden target-number annotation

## 7. Visibility/release semantics

Three scopes are mandatory:

1. `INTERNAL_VERIFIED_STATE`
2. `TEACHER_VISIBLE_PROMPT_METADATA`
3. `STUDENT_VISIBLE_WORKSHEET`

Renderer state is marked `RENDER_ONLY_NOT_FOR_WORKSHEET`.

Student Blueprint must not expose target answers, target times, weights, lengths, angles, tick indices, ray angles, liquid levels or renderer relation strings.

Before actual artifact inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Prompt correctness is not a claim that third-party rendered pixels are correct.

## 8. Automated validation/build

Added:

- `tools/validate_ssot.py`
- `tools/build_install_package.py`
- `.github/workflows/activity-based-elementary-worksheet-gem-ssot.yml`

CI validates SSOT, builds the compact installation package, verifies ZIP integrity and uploads the package artifact.

GitHub Actions run `33307276108` completed successfully for commit `b1adf021b2f22271b400b99819fb0121ae3811ab`:

- Validate Gem SSOT: PASS
- Build compact installation package: PASS
- Verify ZIP: PASS
- Upload installation artifact: PASS

Generated artifact:

`activity-based-elementary-worksheet_Gem_v2.6.0_LTS_9WORKERS_TXT`

Artifact digest recorded by GitHub:

`sha256:37eac6e0e4ddb8c727e6fc2952c821d3538f29fa266b9946e0895a2f4eed3c91`

## 9. Domain maturity decision

Documentation/rule expansion does not by itself prove downstream-render maturity.

All expanded measurement domains remain conservatively `PRODUCTION_CANDIDATE` until `qa/DOMAIN_RELEASE_MATRIX.md` promotion evidence is met.

No domain is promoted merely because this review added deterministic formulas or prompt-level regression.

## 10. Known boundaries

The following are intentionally not claimed as specialized deterministic 2.6 coverage:

- speed/rate/velocity as an automatic extension of distance
- arbitrary complex 3D solids outside rectangular-prism/simple composite grammar
- a universal mandatory curriculum sequence for every school
- guaranteed correctness of nondeterministic downstream image pixels without artifact inspection

These boundaries are explicit to prevent unsupported confidence.

## 11. Final release decision

### Prompt-generation baseline

`BASELINE_2_6_0_LTS=READY`

Conditions satisfied:

- Orchestrator architecture aligned
- 9 Worker contracts aligned
- full P1–P6 measurement capability specification present
- route/manifest/policy/registry/release-matrix aligned
- regression suite expanded
- no runtime dangling-KB dependency in generated compact package
- automated SSOT validator present
- automated package builder present
- CI validation/build/ZIP verification successful

### Artifact/classroom status

`ARTIFACT_QA=NOT_YET_TESTED` for any newly generated worksheet until its actual rendered artifact is inspected.

This final review approves the **Gem prompt-generation baseline** for installation/UAT, not every future downstream worksheet image for automatic classroom release.
