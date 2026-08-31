# Actual Weight-Dial Inactive-Gap Artifact Regression — 2026-08-31

Status: PERMANENT NEGATIVE EVIDENCE
Severity: `P0_CRITICAL_ACADEMIC`
Affected domain: `MEASUREMENT_WEIGHT`
Owning worker: `W03_WEIGHT_SCALE`
Independent auditors: `W07_INSTRUMENT_AUDITOR + W10_METROLOGY_ENGINEER`
Release owner: `W09_QA_RELEASE`

## 1. Observed defect

A rendered learner worksheet showed a nominal 0–5 kg circular dial with repeated radial tick marks continuing through the intended 5→0 non-scale region. The result visually suggested a continuous 360° graduated scale.

The artifact also used a visually familiar 0-at-top label rotation rather than the repository's canonical label-angle template, while the canonical target mapping remained defined elsewhere. This creates a coordinate-system drift risk: labels, ticks and pointer mapping can appear individually plausible while no longer describing the same instrument.

This is not a cosmetic issue. A learner can infer a false measurement topology directly from the picture.

## 2. Canonical oracle

For the repository canonical 0–5 kg teaching dial at 0.1 kg resolution:

`ACTIVE_START_ANGLE=240°`
`ACTIVE_SWEEP_DEG=300°`
`ACTIVE_END_ANGLE=180°`
`INACTIVE_GAP_START_ANGLE=180°`
`INACTIVE_GAP_END_ANGLE=240°`
`INACTIVE_GAP_SWEEP_DEG=60°`
`INACTIVE_GAP_TICK_COUNT=0`
`INACTIVE_GAP_RADIAL_MARK_COUNT=0`

Active intervals/positions:

`(5-0)/0.1 = 50 intervals`
`50+1 = 51 endpoint-inclusive active positions`

Active tick-angle set:

`A={ (240+6*i) mod 360 | i=0..50 }`

Canonical label-angle set:

`LABEL_ANGLES={0:240°,1:300°,2:0°,3:60°,4:120°,5:180°}`

## 3. Important distinction

The circular outline may continue through the inactive gap. It is not a graduation.

What is forbidden inside the open gap is any **radial scale-like mark**, including:

- minor/major ticks;
- unlabeled short radial strokes;
- decorative hatching/rays;
- duplicated endpoint marks displaced into the gap;
- border decoration that visually extends the active graduation sequence.

Therefore checking only `value_tick_count=0` is insufficient. Artifact inspection must also assert `radial_scale_like_mark_count=0`.

## 4. Artifact verdict for the supplied evidence

`ARTIFACT_DIAL_INACTIVE_GAP_QA=FAIL`
`ARTIFACT_SCALE_TOPOLOGY_QA=FAIL`
`ARTIFACT_DIAL_CANONICAL_LABEL_ANGLE_QA=FAIL` when evaluated against the current repository canonical template
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

The artifact must be regenerated; do not repair only the needle or answer text.

## 5. Permanent release rules

For every canonical 0–5 kg dial prompt:

1. serialize active start/end/sweep;
2. serialize inactive gap start/end/sweep;
3. serialize `INACTIVE_GAP_TICK_COUNT=0`;
4. serialize `INACTIVE_GAP_RADIAL_MARK_COUNT=0`;
5. serialize canonical label angles;
6. derive all active ticks only from the canonical tick-angle formula;
7. W07 audits geometry and explicitly searches the gap for radial marks;
8. W10 independently recomputes active/gap geometry and verifies zero gap radial marks;
9. W09 treats any applicable gap/label FAIL or NOT_RUN as release-blocking;
10. rendered artifacts remain unqualified until visually inspected.

## 6. Required prompt gates

`PROMPT_DIAL_GAP_GEOMETRY_SERIALIZATION_QA`
`PROMPT_DIAL_GAP_RADIAL_MARK_ZERO_QA`
`PROMPT_DIAL_ACTIVE_TICK_SET_QA`
`PROMPT_DIAL_CANONICAL_LABEL_ANGLE_QA`
`PROMPT_DIAL_GAP_DECORATION_ISOLATION_QA`
`PROMPT_METROLOGY_DIAL_ACTIVE_TICK_SET_QA`
`PROMPT_METROLOGY_DIAL_GAP_RADIAL_MARK_ZERO_QA`
`PROMPT_METROLOGY_DIAL_LABEL_ANGLE_QA`

Any applicable FAIL/NOT_RUN forces:

`PROMPT_RELEASE=BLOCKED`

## 7. Artifact gates

`ARTIFACT_DIAL_INACTIVE_GAP_QA`
`ARTIFACT_SCALE_TOPOLOGY_QA`
`ARTIFACT_DIAL_CANONICAL_LABEL_ANGLE_QA`

One radial scale-like mark in the inactive gap is sufficient for `ARTIFACT_QA=FAIL` and `CLASSROOM_RELEASE=BLOCKED`.

## 8. Regression discipline

This file records an actual user-supplied rendered defect. Future refactors must preserve this negative oracle. Do not weaken it to a generic `looks correct` requirement or remove the zero-radial-mark condition.