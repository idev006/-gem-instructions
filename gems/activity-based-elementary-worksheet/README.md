# activity-based-elementary-worksheet

Version: 2.6.3-LTS

Production Gem for generating **verified, copy-ready worksheet image prompts** for primary-school learning materials.

## Product role

`PRODUCTION_WORKSHEET_PROMPT_GENERATOR`

Primary deliverable:

`FINAL_IMAGE_GENERATION_PROMPT`

The Gem is an Orchestrator over exactly ten Specialist Workers. It validates academic rules, learner-read instrument geometry, independent metrology, shape-aware page feasibility, visibility isolation, and release evidence before compiling a downstream prompt. It never claims final pixels are correct until an actual artifact is inspected.

## Ten Specialist Workers

- `W01_ACADEMIC_CONTENT` — arithmetic, color-by-code, Thai literacy, generic content
- `W02_TIME_CLOCK` — time and analog clocks
- `W03_WEIGHT_SCALE` — weight and dial scales
- `W04_LENGTH_DISTANCE` — ruler, length, distance, speedometer, protractor, perimeter, area
- `W05_TEMPERATURE_CAPACITY_VOLUME` — thermometer, capacity, meniscus, volume
- `W06_MONEY_CALENDAR_DATA` — money, calendar, tables/graphs
- `W07_INSTRUMENT_AUDITOR` — shared geometry/topology audit
- `W08_LAYOUT_RENDER_THAI` — layout, render path, Thai/text, print/theme
- `W09_QA_RELEASE` — conjunctive integration/release
- `W10_METROLOGY_ENGINEER` — independent metrology, common-center, print and page-feasibility audit

W10 is a permanent production worker, not a hotfix slot.

## Five mandatory shared profiles

Every generated worker bundle embeds:

1. `policies/SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
3. `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `policies/METROLOGY_ASSURANCE_PROFILE.md`
5. `policies/PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Learner-read route:

`OWNING WORKER → W07 → W10 → W08 → W09`

## Current release gate

All prior executable suites remain and counts only increase. Current target release baseline:

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
- repository full-line audit: 81

Combined:

`1300/1300 PASS`

CI must also pass SSOT validation, package build, ZIP integrity and artifact upload.

## Critical educational geometry

### Ruler
1 cm @1 mm = 10 intervals / 11 positions / 9 interior positions. Physical ruler edge is not an extra graduation.

### Weight dial
Canonical 0–5 kg @0.1 kg:

- 0° is top, clockwise positive;
- labels `0@0°,1@60°,2@120°,3@180°,4@240°,5@300°`;
- clockwise sequence `[0,1,2,3,4,5]`;
- 50 active intervals /51 positions;
- inactive open gap `(300°,360°)` with zero scale-like radial marks;
- needle pivot equals dial/reading-ring center.

### Speedometer
Canonical 0–120 km/h @10:

- 12 intervals /13 positions;
- 240° active /120° inactive;
- `target_angle=(240+2*target_kmh) mod 360`;
- 60 km/h→0°→straight up;
- needle pivot equals dial/reading-ring center and needle is radial.

Direct speedometer reading does not silently enable `speed=distance/time`.

### Thermometer
Canonical 0–50°C @1°C:

- 50 intervals /51 positions;
- 6 major positions at 0,10,20,30,40,50;
- 5 intermediate positions at 5,15,25,35,45;
- 40 ordinary minor positions;
- each 10°C span has 10 intervals /9 interior positions;
- liquid endpoint exactly on target graduation.

### Protractor
Canonical 0–180° @1°:

- perfect upper semicircle;
- 180 intervals /181 positions;
- one active numeric scale by default;
- 0° right,90° top,180° left;
- 10° major/5° intermediate/1° minor;
- common center = arc center = baseline midpoint = ray origin;
- all ticks/rays radial;
- no ellipse/skew/shear/non-uniform transform;
- minimum production width 70 mm at default 0.60 mm arc-spacing floor.

A semicircle of width 70 mm has 35 mm geometric body height before labels/answer space. Page packing is shape-aware.

## One-page policy

Defaults:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

When unlocked and a candidate page does not fit, paginate instead of shrinking below safe geometry, deleting ticks, or removing answer space.

## Visibility and phase boundary

Three scopes:

- `INTERNAL_VERIFIED_STATE`
- `TEACHER_VISIBLE_PROMPT_METADATA`
- `STUDENT_VISIBLE_WORKSHEET`

Renderer-only target geometry never belongs in the Student Blueprint.

Before actual downstream artifact inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

`PROMPT_QA != ARTIFACT_QA`.

A real artifact defect is converted into permanent regression before the next accepted release.

## Installation

See `GEM_INSTALLATION_GUIDE.md`. Production installation uses one Orchestrator Instructions text plus exactly ten Knowledge worker TXT files generated from GitHub SSOT by CI.
