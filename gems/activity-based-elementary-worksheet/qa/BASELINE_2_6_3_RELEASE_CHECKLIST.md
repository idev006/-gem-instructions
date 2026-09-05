# Baseline 2.6.3-LTS Release Checklist

Status: Critical educational-instrument + primary learner-safety release checklist
Release family: 2.6.3-LTS
Compatible worker baseline: 2.6.x / schema 1

## Release principles

`ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER`

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

`PHYSICAL_FIT != PRIMARY_LEARNER_USABILITY`

Passing this checklist qualifies the **prompt/package system**. It never proves downstream pixels. Actual worksheets still require Artifact QA before classroom release.

## Base architecture

Exactly 10 base workers:

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

Five mandatory technical shared runtime profiles:
1. `SYSTEM_WIDE_QUALITY_PROFILE.md`
2. `SCALE_LINE_INTEGRITY_PROFILE.md`
3. `INSTRUMENT_REVIEW_REVISE_PROFILE.md`
4. `METROLOGY_ASSURANCE_PROFILE.md`
5. `PHYSICAL_PAGE_FEASIBILITY_PROFILE.md`

Mandatory cross-cutting learner profile:
`PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`

Mandatory capability-quality profile:
`CAPABILITY_QUALITY_GATE.md`

Mandatory learner-read chain:
`OWNING DOMAIN → W07 GEOMETRY AUDIT → W10 INDEPENDENT METROLOGY AUDIT → W08 LAYOUT/RENDER → W09 RELEASE`

`NO WORKER MAY SELF-CERTIFY ITS OWN HIGH-RISK OUTPUT.`

## Primary-school learner safety

Unless a valid explicit teacher requirement safely overrides them:
- implicit page default = A4 Portrait;
- P1–P3 body text target >=14 pt;
- P4–P6 body text target >=12 pt;
- primary title target >=18 pt;
- learner-read numerals target >=12 pt;
- handwritten response clear height P1–P3 >=8 mm; P4–P6 >=6 mm;
- concise grade-appropriate directions;
- one unambiguous response zone per item;
- no essential meaning encoded by color alone;
- no decoration competing with text/academic geometry;
- no unrelated complexity added merely to increase difficulty;
- physical page fit does not override readability/writability.

Academic geometry uses:
`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES`
`CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES`
`POST_LAYOUT_GEOMETRY_TRANSFORM=UNIFORM_SCALE_AND_TRANSLATE_ONLY`

## Correct canonical instrument oracles

### Analog clock
`minute_angle=6*m`
`hour_displacement=minute_angle/12`
`hour_angle=30*(h mod 12)+hour_displacement`
Equivalent: `hour_angle=30*(h mod 12)+0.5*m`
Nonzero minutes require continuous displacement. :15=25%, :30=50%, :45=75%. Renderer-only state includes exact angle plus deterministic vector endpoint. 3:30 hour hand=105°, never 90°; 9:30=285°, never270°.

### Weight dial 0–5 kg @0.1 kg
- 0°=top, clockwise positive;
- labels `{0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`;
- 50 intervals /51 active positions;
- each 1 kg span = exactly 10 intervals /11 endpoint-inclusive positions /9 interior marks;
- +0.5 kg is existing index5 intermediate tick, longer than ordinary minor and shorter/weaker than whole-kg major;
- inactive gap `(300°,360°)` with zero radial scale-like marks;
- needle pivot=dial/reading-ring center;
- visible tick set must be serialized explicitly; `10 divisions` prose alone is insufficient.

### Speedometer 0–120 km/h @10
12 intervals/13 positions; 240° active/120° inactive; `target_angle=(240+2*target_kmh) mod 360`; pivot=center; pointer radial.

### Ruler 1 cm @1 mm
10 intervals/11 positions/9 interior; physical edge not graduation; 5 mm hierarchy reuses position. Object-on-ruler tasks require start/end dashed projections. ZERO_START aligns object start with zero graduation; NONZERO uses END-START.

### Thermometer 0–50°C @1°C
50/51; major=6, intermediate=5, ordinary minor=40; each10°C span=10 intervals/9 interior; liquid endpoint on target centerline.

### Graduated container 0–1000 mL @50 mL
20/21 globally; each100mL span=2 intervals/3 positions with exactly one +50mL interior tick; no extra local pseudo-ticks.

### Protractor 0–180° @1°
Perfect upper semicircle;180/181; one active scale default;0° right/90° top/180° left; 10° major/5° intermediate/1° minor; common center=baseline midpoint=ray origin; all ticks/rays radial; no distortion; width>=70mm at0.60mm floor; body height=width/2 before label/answer reserves.

## Page feasibility

Implicit default: A4 Portrait, 210×297mm before margins. `ONE_PAGE_PREFERRED != ONE_PAGE_LOCKED`.

A PASS requires numeric `PHYSICAL_PAGE_STATE` including margins, header/title/directions, complete shape-aware item boxes, response zones and gaps. When lock=OFF, paginate rather than deleting/merging graduations, shrinking required text below learner defaults, or reducing response space.

## Permanent actual defects retained

- ruler extra graduation;
- ruler physical-edge start / missing endpoint projections;
- weight-dial inactive-gap radial marks;
- weight-dial label order / coordinate drift;
- weight-dial missing/sparsified 0.1kg graduations and missing midpoint hierarchy;
- speedometer off-center pivot;
- clock hour hand snap for nonzero minutes;
- thermometer wrong subdivisions/hierarchy;
- graduated-container extra local subdivisions;
- distorted/misregistered protractor;
- physical-page feasibility contradictions;
- learner-facing ambiguity/readability risks discovered in clean-room pedagogy audit.

## Executable release gate

All prior tests remain; counts only increase.

1. core dry-run: 449
2. declared-skill matrix: 360
3. runtime UAT: 12
4. semantic oracle: 20
5. system-wide quality: 30
6. scale-line integrity: 40
7. instrument review/speedometer: 60
8. protractor scale safety: 24
9. full metrology audit: 80
10. actual weight-dial inactive-gap regression: 32
11. physical page feasibility regression: 48
12. actual instrument geometry regression: 64
13. measurement reference artifact regression: 66
14. clock hand endpoint regression: 32
15. clock half-hour formula regression: 96
16. clock P3 half-hour one-page regression: 100
17. weight dial visible subdivision regression: 32
18. primary-school pedagogy regression: 64
19. repository full-line audit: 81
20. capability quality scorecard: 15 capabilities × 20 criteria = 300 scored criteria
21. skill metric pack governance: 161
22. scale tick standard governance: 120
23. all-skills clean-room audit: 180

Combined mandatory effective gate:

`1494/1494 PASS`

Additional mandatory clock hardening gates:
`96/96 CLOCK HALF-HOUR FORMULA PASS`
`100/100 CLOCK P3 HALF-HOUR ONE-PAGE PASS`

Additional mandatory skill-metric gate:
`161/161 SKILL METRIC PACK GOVERNANCE PASS`
`15/15 SKILL METRIC PACKS PRESENT`
`CRITICAL_ACADEMIC_DEFECT => RELEASE BLOCKED`

Additional mandatory all-skills gate:
`180/180 ALL-SKILLS CLEAN-ROOM AUDIT PASS`
`15/15 SKILLS CANONICAL_STATE_REQUIRED=YES`

Additional mandatory capability gate:
`300/300 SCORED CRITERIA PASS`
`15/15 CAPABILITIES >=95%`
`OVERALL_CAPABILITY_SCORE >=95%`

Current iteration result: all 15 capabilities = 100%; overall = 100.00%.

Repository full-line audit still scans every UTF-8 text/code line in the Gem SSOT plus workflow and executes its fixed 81 semantic cases.

## Package audit

Package name:
`activity-based-elementary-worksheet_Gem_v2.6.3_LTS_10WORKERS_TXT`

Must contain:
- one main Instructions TXT;
- exactly ten worker Knowledge TXT files;
- five technical shared profiles embedded in every worker bundle;
- mandatory primary-school pedagogy profile embedded in every worker bundle;
- W10 metrology worker;
- current actual-defect evidence and clean-room pedagogy audit;
- reports for all established regression suites including clock 96/100, plus the 161-case skill-metric and 120-case scale-tick governance suites and capability-quality scorecard;
- classroom Artifact UAT guide;
- checksum manifest;
- ZIP integrity PASS.

Use the exact GitHub Actions artifact only after every gate passes.

## Prompt / artifact boundary

Passing `1494/1494 PASS` plus `SKILL_METRIC_PACK_REGRESSION=161/161 PASS` plus `CAPABILITY_QUALITY_GATE=PASS` means the prompt/package is eligible for `PROMPT_RELEASE=APPROVED`.

Before actual worksheet inspection:
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Artifact inspection includes metrology plus `ARTIFACT_LEARNER_SIMULATION_QA`. One incorrect instructional instrument, unreadable required content, or learner-visible ambiguity means:
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`
and the defect becomes permanent regression before the next accepted release.
