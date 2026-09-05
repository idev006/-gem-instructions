# Actual Protractor Missing-Tick / Duplicate-Label Artifact Regression — 2026-09-05

Status: CRITICAL_ACADEMIC
Source: user-supplied rendered protractor artifact

## Observed defects

The artifact visually shows an unreliable/incomplete 1° graduation field and a duplicated numeric label "170" on the left side.

This is not cosmetic. A learner can infer false angular spacing or read an incorrect angle.

## Canonical truth

For a 0–180° protractor at 1° resolution:
- 180 intervals;
- 181 visible graduation positions;
- 19 major ticks at multiples of 10°;
- 18 intermediate ticks at 5° offsets;
- 144 ordinary minor ticks;
- label set exactly 0,10,...,180 once each;
- 90° at top;
- 0° right baseline;
- 180° left baseline;
- all ticks radial from the common origin.

## Root cause

Count-level prose was present but the final renderer contract did not require an explicit 181-record tick manifest and 19-record unique label manifest.

This allowed generative approximation, omission, duplication and label hallucination.

## Required repair

- serialize every integer-degree tick position 0..180;
- serialize tick class for each position;
- serialize exact radial endpoints;
- serialize unique 19-value label manifest;
- recount/classify before prompt release;
- recount visible artifact after render.

## Verdict for supplied artifact

`ARTIFACT_PROTRACTOR_TICK_MANIFEST_QA=FAIL`
`ARTIFACT_PROTRACTOR_LABEL_SET_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

Future renders remain `ARTIFACT_QA=NOT_YET_TESTED` until inspected.
