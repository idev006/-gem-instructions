# activity-based-elementary-worksheet

Version: 2.6.3-LTS

Production Gem for generating **verified, copy-ready worksheet image prompts** for primary-school learning materials.

## Product role

`PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

Primary deliverable:
`FINAL_IMAGE_GENERATION_PROMPT`

The Gem is an Orchestrator over exactly ten Specialist Workers. It validates academic rules, learner-read geometry, independent metrology, primary-school pedagogy/usability, shape-aware page feasibility, visibility isolation, and release evidence before compiling a downstream prompt. It never claims final pixels are correct until an actual artifact is inspected.

## Ten Specialist Workers

- `W01_ACADEMIC_CONTENT`
- `W02_TIME_CLOCK`
- `W03_WEIGHT_SCALE`
- `W04_LENGTH_DISTANCE`
- `W05_TEMPERATURE_CAPACITY_VOLUME`
- `W06_MONEY_CALENDAR_DATA`
- `W07_INSTRUMENT_AUDITOR`
- `W08_LAYOUT_RENDER_THAI`
- `W09_QA_RELEASE`
- `W10_METROLOGY_ENGINEER`

W10 is a permanent production worker, not a hotfix slot.

Learner-read route:
`OWNING WORKER → W07 → W10 → W08 → W09`

`NO WORKER MAY SELF-CERTIFY ITS OWN HIGH-RISK OUTPUT.`

## Runtime safety profiles

Five mandatory technical shared profiles:
1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `METROLOGY_ASSURANCE_PROFILE.md`
5. `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Mandatory learner-facing cross-cutting profile:
`PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`

## Current release gate

All prior executable suites remain and counts only increase:

- core deterministic/policy: 449
- declared-skill matrix: 360
- runtime UAT: 12
- semantic oracle: 20
- system-wide quality: 30
- scale-line integrity: 40
- instrument review/speedometer: 60
- protractor safety: 24
- full metrology: 80
- actual weight-dial gap: 32
- physical page feasibility: 48
- actual instrument geometry: 64
- measurement reference artifact: 66
- clock hand endpoint: 32
- weight dial visible subdivision: 32
- primary-school pedagogy/usability: 64
- repository full-line audit: 81

Combined effective gate:

`1494/1494 PASS`

CI must also pass SSOT validation, package build, ZIP integrity and artifact upload.

## Primary-school learner defaults

When no safe explicit override is provided:
- page = A4 Portrait;
- one page is preferred but not forced (`ONE_PAGE_LOCK=OFF`);
- P1–P3 body text target >=14 pt;
- P4–P6 body text target >=12 pt;
- title target >=18 pt;
- learner-read instrument/graph numerals target >=12 pt;
- handwritten response clear height P1–P3 >=8 mm and P4–P6 >=6 mm;
- concise, age-appropriate directions;
- one clear response zone per item;
- no essential meaning by color alone;
- no decoration competing with instructional information;
- paginate before degrading required geometry, text or response space.

## Academic geometry ownership

For learner-read instruments/axes:

`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES`
`CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES`
`POST_LAYOUT_GEOMETRY_TRANSFORM=UNIFORM_SCALE_AND_TRANSLATE_ONLY`

The downstream prompt must provide deterministic formulas or primitive/position manifests for high-risk academic geometry. Generative art is decoration only.

## Critical educational geometry

### Clock
`minute_angle=6*m`
`hour_angle=30*(h mod 12)+0.5*m`
Hour hand moves continuously. Nonzero-minute clock state includes exact vector endpoint; e.g. 3:30=105° not90°, 9:30=285° not270°.

### Ruler
1cm @1mm=10 intervals/11 positions/9 interior. Physical edge is not graduation. Object-on-ruler tasks use dashed start/end projections; ZERO_START aligns with zero graduation.

### Weight dial
Canonical 0–5kg @0.1kg:
- labels 0–5 at 0°,60°,120°,180°,240°,300°;
- 50 intervals/51 positions;
- each1kg span exactly10 intervals /11 endpoint positions /9 interior marks;
- +0.5kg index5 is longer than ordinary minor and shorter/weaker than major;
- explicit visible tick set serialized;
- inactive gap `(300°,360°)` has zero radial marks;
- needle pivot=center.

### Speedometer
0–120 @10:12/13,240° active/120° inactive,pivot=center,radial pointer.

### Thermometer
0–50°C @1:50/51,6 major/5 intermediate/40 minor,each10°C span10/9,endpoint exact.

### Graduated container
0–1000mL @50 with100mL majors:20/21 globally; each100mL span exactly2 intervals with one +50mL interior tick.

### Protractor
0–180° @1: perfect upper semicircle,180/181,single active scale default,0 right/90 top/180 left,common origin,radial ticks/ray,no distortion,width>=70mm at0.60mm spacing floor.

## Page policy

`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

Physical fit is conjunctive with learner readability/writability. When unlocked, paginate rather than shrinking below safe geometry or learner-facing defaults.

## Prompt vs Artifact QA

Before actual downstream artifact inspection:
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Actual artifact inspection includes metrology plus `ARTIFACT_LEARNER_SIMULATION_QA`. A real artifact defect becomes permanent regression before the next accepted release.

## Installation

See `GEM_INSTALLATION_GUIDE.md`. Production installation uses one Orchestrator Instructions text plus exactly ten Knowledge worker TXT files generated from GitHub SSOT by CI.
