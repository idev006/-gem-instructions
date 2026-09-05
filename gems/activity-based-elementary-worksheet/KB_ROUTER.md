# KB Router — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
Compatible Gem baseline: 2.6.x
Status: Canonical worker-routing policy

## 1. Purpose

Route each request to the smallest complete Specialist Worker set. Do not blend every Knowledge file indiscriminately.

Every production request also inherits `PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`; learner-read geometry adds the technical instrument safety chain.

## 2. Base worker set

Required production installation:
`W01_ACADEMIC_CONTENT`
`W02_TIME_CLOCK`
`W03_WEIGHT_SCALE`
`W04_LENGTH_DISTANCE`
`W05_TEMPERATURE_CAPACITY_VOLUME`
`W06_MONEY_CALENDAR_DATA`
`W07_INSTRUMENT_AUDITOR`
`W08_LAYOUT_RENDER_THAI`
`W09_QA_RELEASE`
`W10_METROLOGY_ENGINEER`

W08 and W09 apply to every production request. W07 and W10 both apply whenever learner-read geometry/axis/instrument state carries academic meaning.

## 3. Route table

| Request family | Worker route |
|---|---|
| arithmetic / number operations | W01 + W08 + W09 |
| color-by-code arithmetic | W01 + W08 + W09 |
| Thai literacy / spelling | W01 + W08 + W09 |
| elapsed time / start-end-duration / time-unit conversion | W02 + W08 + W09 |
| analog clock reading | W02 + W07 + W10 + W08 + W09 |
| weight arithmetic/comparison/conversion | W03 + W08 + W09 |
| dial scale reading | W03 + W07 + W10 + W08 + W09 |
| length arithmetic/conversion | W04 + W08 + W09 |
| distance total/difference/round trip/multi-segment | W04 + W08 + W09 |
| ruler reading | W04 + W07 + W10 + W08 + W09 |
| direct speedometer reading | W04 + W07 + W10 + W08 + W09 |
| angle/protractor reading | W04 + W07 + W10 + W08 + W09 |
| perimeter/area/circle measurement | W04 + W08 + W09; add W07+W10 when learner-read geometry is part of question |
| temperature calculation/change | W05 + W08 + W09 |
| thermometer reading | W05 + W07 + W10 + W08 + W09 |
| capacity arithmetic/conversion | W05 + W08 + W09 |
| graduated container / meniscus | W05 + W07 + W10 + W08 + W09 |
| rectangular-prism/simple composite volume | W05 + W08 + W09 |
| money / calendar / tables | W06 + W08 + W09 |
| pictograph / bar graph | W06 + W08 + W09; add W07+W10 when exact visual scale is learner-read |

Mixed-domain worksheets select all owning academic workers, then W08/W09, plus W07+W10 if any item contains learner-read academic geometry.

## 4. Academic ownership

- W01 general content not owned by specialist.
- W02 time/clock.
- W03 weight/dial formulas and units.
- W04 ruler/length/distance/direct speedometer/protractor/perimeter/area.
- W05 temperature/capacity/volume.
- W06 money/calendar/data mappings.
- W07 shared topology/geometry audit; does not invent domain targets.
- W10 independent metrology/common-center/shape/page audit; does not invent domain targets.
- W08 shape-aware layout/render/Thai/print/theme and review serialization.
- W09 integration/release QA.

`WORKER_OWNERSHIP_QA=FAIL` if a worker overrides another worker's owned academic rule.

## 5. Mandatory runtime profile routing

Every production route inherits:
- `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
- `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`
- `policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`

When learner-read geometry is present, additionally require:
- `domains/INSTRUMENT_READING_ENGINE.md`
- `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
- `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `policies/METROLOGY_ASSURANCE_PROFILE.md`

Required learner-read semantics:
`PER_ITEM_RENDER_STATE_REQUIRED=YES`
`TARGET_ALIGNMENT_REQUIRED=YES`
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`
`METROLOGY_AUDIT_REQUIRED=YES`
`PHYSICAL_PAGE_STATE_REQUIRED=YES`
`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES`

Every high-risk item state:
`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL/ENDPOINT + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

Radial/angular state additionally serializes authoritative center/origin identity.

Mandatory chain:
`OWNING WORKER → W07 → W10 → W08 → W09`

## 6. Learner-facing routing responsibilities

The pedagogy profile is cross-cutting and does not create an 11th worker.

- owning worker/W01: grade/objective appropriateness;
- W08: student typography, writing space, visual load and Thai presentation;
- W09: conjunctive learner-quality release checks;
- Artifact QA: `ARTIFACT_LEARNER_SIMULATION_QA`.

If page format is not explicit, normalize to A4 Portrait. If an A4 Portrait page is too dense and lock=OFF, paginate rather than degrading learner readability.

## 7. Precedence

When rules conflict:
1. explicit valid user requirement unless academically/readability unsafe or contradictory
2. `GEM_INSTRUCTIONS_PRODUCTION.md`
3. `domains/DOMAIN_REGISTRY.md`
4. owning Specialist Worker/domain engine
5. `policies/SCALE_LINE_INTEGRITY_PROFILE.md` + W07 when applicable
6. `policies/METROLOGY_ASSURANCE_PROFILE.md` + W10 when applicable
7. `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`
8. `policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`
9. `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md` when applicable
10. `policies/PARAMETER_POLICY.md`
11. W08 layout/render/Thai/print
12. `OUTPUT_CONTRACT.md`
13. W09/QA suites

QA may make release stricter but may not redefine an owning worker formula.

## 8. Base-update policy

Architecture, scale-safety, pedagogy, visibility, routing, geometry or metrology changes require base SSOT + permanent regression + full CI + reinstall.

## 9. Routing QA

`KB_ROUTE_QA=PASS` only if:
- primary/mixed domains correctly detected;
- all owning workers selected;
- W07 and W10 present for learner-read geometry;
- W08/W09 present;
- mandatory runtime profiles apply;
- pedagogy profile applies to every production route;
- no unrelated worker overrides route;
- precedence respected.

`KB_COMPATIBILITY_QA=PASS` only if worker IDs/schema/baseline and runtime profiles match `KB_MANIFEST.md`.


## Skill Metric routing overlay

After domain/worker routing, resolve the corresponding `SKILL_ID` and metric pack.

- W01 → ACADEMIC_ARITHMETIC_THAI
- W02 time calculation → TIME_CALCULATION
- W02 analog clock → ANALOG_CLOCK
- W03 → WEIGHT_SCALE
- W04 ruler/length → RULER_LENGTH
- W04 distance → DISTANCE
- W04 speedometer → SPEEDOMETER
- W04 angle/protractor → ANGLE_PROTRACTOR
- W04 perimeter/area → PERIMETER_AREA
- W05 temperature → TEMPERATURE
- W05 capacity → CAPACITY
- W05 volume → VOLUME
- W06 money → MONEY
- W06 calendar → CALENDAR
- W06 table/graph/pictograph → DATA_READING

Mixed-domain requests resolve multiple skill packs. W09 must not average skill scores across skills.
