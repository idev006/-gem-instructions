# Artifact Qualification Protocol

Version: 1.0.0
Status: Mandatory for classroom release

## Purpose

Qualify the actual worksheet children will see, not only the prompt that requested it.

## Minimum process

For each skill:
1. generate representative worksheets across easy/medium/hard and boundary cases;
2. inspect every learner-read instrument/data object individually;
3. compare visible state against canonical oracle;
4. run child-view readability/writability simulation;
5. record defects;
6. convert every systemic or repeated defect into permanent regression;
7. re-render after repair.

## Instrument audit rule

One wrong instructional instrument makes the worksheet fail.

Do not sample only one item from a 10-item worksheet.

## Recommended promotion evidence

For `PRODUCTION_HARDENED`:
- >=20 diverse dry-run prompt cases;
- >=10 actual rendered worksheets for the claimed render path;
- every instrument/item inspected;
- >=95 artifact score;
- zero unresolved critical defects.

## Required evidence fields

`SKILL_ID`
`RENDER_PATH`
`WORKSHEET_COUNT`
`ITEM_COUNT_INSPECTED`
`CRITICAL_DEFECT_COUNT`
`SKILL_ARTIFACT_SCORE`
`ARTIFACT_QA`
`CLASSROOM_RELEASE`

## Boundary

Self-review by a renderer is prevention evidence only. It is not independent Artifact QA.
