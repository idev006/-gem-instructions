# Actual Weight-Dial Inactive-Gap Artifact Regression — 2026-08-31

Status: PERMANENT NEGATIVE EVIDENCE
Severity: `P0_CRITICAL_ACADEMIC`
Affected domain: `MEASUREMENT_WEIGHT`
Owning worker: `W03_WEIGHT_SCALE`
Independent auditors: `W07_INSTRUMENT_AUDITOR + W10_METROLOGY_ENGINEER`
Release owner: `W09_QA_RELEASE`

## 1. Observed defect

A rendered learner worksheet showed a nominal 0–5 kg dial with repeated radial tick marks continuing through the intended 5→0 non-scale region. The picture suggested a continuous 360° graduated value scale.

A later full-SSOT audit discovered an additional repository defect: the then-current canonical label rotation placed 0 away from the top. That rotated SSOT was inconsistent with the intended elementary classroom dial and has been corrected. Permanent regression must preserve the actual gap defect while using the corrected top-zero clockwise canonical state.

## 2. Correct canonical oracle

Angle convention:

`0° = top / 12 o'clock`
`CLOCKWISE_POSITIVE=YES`

For 0–5 kg @0.1 kg:

`ACTIVE_START_ANGLE=0°`
`ACTIVE_SWEEP_DEG=300°`
`ACTIVE_END_ANGLE=300°`
`INACTIVE_GAP_START_ANGLE=300°`
`INACTIVE_GAP_END_ANGLE=360°/0°`
`INACTIVE_GAP_SWEEP_DEG=60°`
`INACTIVE_GAP_TICK_COUNT=0`
`INACTIVE_GAP_RADIAL_MARK_COUNT=0`

Active intervals/positions:

`(5-0)/0.1 = 50 intervals`
`50+1 = 51 endpoint-inclusive active positions`

Active tick-angle set:

`A={ (6*i) mod 360 | i=0..50 }`

Canonical labels:

`LABEL_ANGLES={0:0°,1:60°,2:120°,3:180°,4:240°,5:300°}`
`CLOCKWISE_MAJOR_LABEL_SEQUENCE=[0,1,2,3,4,5]`

Common center:

`NEEDLE_PIVOT == DIAL_CENTER == READING_RING_CENTER`

## 3. Important distinction

The housing/outer outline may continue through the inactive gap. It is not a graduation.

Forbidden inside open gap `(300°,360°)`:

- minor/major ticks;
- unlabeled short radial strokes;
- decorative hatching/rays;
- duplicated/displaced endpoint marks;
- border decoration that visually extends active graduations.

Checking only `value_tick_count=0` is insufficient. Artifact inspection also asserts `radial_scale_like_mark_count=0`.

## 4. Artifact verdict for supplied evidence

`ARTIFACT_DIAL_INACTIVE_GAP_QA=FAIL`
`ARTIFACT_SCALE_TOPOLOGY_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

If label order/pivot also violates corrected canonical state:

`ARTIFACT_DIAL_LABEL_ORDER_QA=FAIL`
`ARTIFACT_DIAL_COMMON_CENTER_QA=FAIL`

Artifact must be regenerated; do not repair only needle or answer text.

## 5. Permanent release rules

For every canonical 0–5 kg dial prompt:

1. serialize active start/end/sweep;
2. serialize inactive gap start/end/sweep;
3. serialize `INACTIVE_GAP_TICK_COUNT=0`;
4. serialize `INACTIVE_GAP_RADIAL_MARK_COUNT=0`;
5. serialize corrected canonical label angles/order;
6. derive all active ticks only from `active_tick_angle(i)=(6*i) mod 360`;
7. serialize `NEEDLE_PIVOT=DIAL_CENTER`;
8. W07 audits gap, label order and common center;
9. W10 independently recomputes all of them;
10. W09 blocks applicable FAIL/NOT_RUN;
11. rendered artifacts remain unqualified until visually inspected.

## 6. Required prompt gates

`PROMPT_DIAL_GAP_GEOMETRY_SERIALIZATION_QA`
`PROMPT_DIAL_GAP_RADIAL_MARK_ZERO_QA`
`PROMPT_DIAL_ACTIVE_TICK_SET_QA`
`PROMPT_DIAL_CANONICAL_LABEL_ANGLE_QA`
`PROMPT_DIAL_LABEL_ORDER_QA`
`PROMPT_DIAL_COMMON_CENTER_QA`
`PROMPT_DIAL_GAP_DECORATION_ISOLATION_QA`
`PROMPT_METROLOGY_DIAL_ACTIVE_TICK_SET_QA`
`PROMPT_METROLOGY_DIAL_GAP_RADIAL_MARK_ZERO_QA`
`PROMPT_METROLOGY_DIAL_LABEL_ANGLE_QA`
`PROMPT_METROLOGY_LABEL_ORDER_QA`
`PROMPT_METROLOGY_COMMON_CENTER_QA`

Any applicable FAIL/NOT_RUN forces `PROMPT_RELEASE=BLOCKED`.

## 7. Regression discipline

This file records an actual user-supplied rendered defect plus the subsequent SSOT root-cause correction. Future refactors must preserve the zero-radial-gap oracle and corrected top-zero clockwise label/order/common-center canonical. Do not weaken these to a generic `looks correct` requirement.
