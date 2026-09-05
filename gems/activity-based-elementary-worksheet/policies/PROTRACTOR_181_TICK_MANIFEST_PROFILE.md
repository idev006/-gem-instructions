# Protractor 181-Position Deterministic Tick Manifest Profile

Version: 1.0.0
Status: Mandatory for learner-read 0–180° protractors at 1° resolution
Compatible Gem baseline: 2.6.x

## Purpose

Prevent missing/extra/merged graduations and duplicate/missing labels in rendered semicircular protractors.

A statement such as "draw 181 ticks" is insufficient. The final renderer state MUST serialize the complete canonical position set.

## Canonical topology

`RANGE_MIN_DEG=0`
`RANGE_MAX_DEG=180`
`MINOR_INTERVAL_DEG=1`
`EXPECTED_INTERVAL_COUNT=180`
`EXPECTED_TICK_POSITION_COUNT=181`
`EXPECTED_INTERIOR_POSITION_COUNT=179`

Canonical positions:
`TICK_POSITION_DEGREES=[0,1,2,...,180]`

There are no omitted, duplicated, merged or decorative pseudo-positions.

## Tick classification

For every integer degree d in 0..180:

- if `d % 10 == 0` → `TICK_CLASS=MAJOR`
- else if `d % 5 == 0` → `TICK_CLASS=INTERMEDIATE`
- else → `TICK_CLASS=MINOR`

Counts:
- `MAJOR_TICK_COUNT=19` at 0,10,...,180
- `INTERMEDIATE_TICK_COUNT=18` at 5,15,...,175
- `MINOR_TICK_COUNT=144`
- total = 19+18+144 = 181

Hierarchy:
`MAJOR_TICK_LENGTH > INTERMEDIATE_TICK_LENGTH > MINOR_TICK_LENGTH`

Hierarchy changes only line length/weight. It MUST NOT add scale positions.

## Deterministic radial geometry

Let common origin `C=(cx,cy)` and reading radius `R`.

For degree d:
`ux=cos(radians(d))`
`uy=-sin(radians(d))`

Outer endpoint:
`OUTER_d=(cx+R*ux, cy+R*uy)`

Let inner radii depend only on class:
- `r_major < r_intermediate < r_minor < R`

Inner endpoint:
`INNER_d=(cx+r_class*ux, cy+r_class*uy)`

Tick d is the exact segment:
`INNER_d -> OUTER_d`

Every tick is radial from the same origin.

## Numeric labels

Default single active scale:
`EXPECTED_LABEL_VALUES=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180]`

Required:
`EXPECTED_LABEL_COUNT=19`
`LABEL_VALUES_UNIQUE=YES`
`LABEL_DUPLICATE_COUNT=0`
`LABEL_MISSING_COUNT=0`

Every label value v MUST associate with major tick v.

Default direction:
- 0° at right baseline
- 90° at top
- 180° at left baseline

No duplicate 170, no missing 100, no skipped 10-degree label.

## Mandatory renderer-only manifest

Each protractor item MUST serialize:

`PROTRACTOR_TICK_MANIFEST`

with exactly 181 records. Each record contains:
- `degree`
- `tick_class`
- `outer_endpoint`
- `inner_endpoint`

And:

`PROTRACTOR_LABEL_MANIFEST`

with exactly 19 records:
- `label_value`
- `associated_major_tick_degree`
- `label_anchor`

Natural-language-only scale descriptions are forbidden for 1° learner-read protractors.

## Mandatory QA

`PROMPT_PROTRACTOR_181_POSITION_MANIFEST_QA`
`PROMPT_PROTRACTOR_TICK_CLASS_COUNT_QA`
`PROMPT_PROTRACTOR_LABEL_SET_QA`
`PROMPT_PROTRACTOR_LABEL_UNIQUENESS_QA`
`PROMPT_PROTRACTOR_NO_MISSING_TICK_QA`
`PROMPT_PROTRACTOR_NO_EXTRA_TICK_QA`
`PROMPT_PROTRACTOR_RADIAL_MANIFEST_QA`

Any failure is `CRITICAL_ACADEMIC`.

## Artifact QA

Post-render inspection MUST recount all 181 visible graduation positions and verify the 19-label set.

One missing/extra/merged tick or duplicate/missing numeric label:
`ARTIFACT_PROTRACTOR_TICK_MANIFEST_QA=FAIL`
`ARTIFACT_PROTRACTOR_LABEL_SET_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`
