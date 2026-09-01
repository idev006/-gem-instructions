# Actual Analog Clock Hand Endpoint Regression — 2026-09-01

Status: `CRITICAL_ACADEMIC`
Source: user-supplied rendered worksheet artifact after prior interpolation hardening.

## Observed defect

The artifact still showed short/hour hands at incorrect visual positions even though the prompt-side semantic time and continuous-hour formula were already present in SSOT.

Representative failure pattern:
- minute hand correctly indicates the minute value;
- hour hand is visually snapped toward a whole-hour numeral or placed on an approximate ray;
- the rendered hour-hand endpoint does not reliably equal the vector implied by `hour_angle=30*(h mod 12)+0.5*m`.

This demonstrates that **formula + angle + prose relation are not sufficient** for a downstream renderer. The render contract must carry the exact radial endpoint.

## Root cause

The previous prompt contract allowed the downstream renderer to infer the hand endpoint from an angle or qualitative relation. Generative approximation can therefore preserve the semantic intent while violating exact clock geometry.

## Canonical fix

For angle `θ`, 0° at 12 o'clock and clockwise-positive:

`direction=(sin θ,-cos θ)`

Use one exact center `C` and normalized radius `R`:

`minute_endpoint=C+0.78R*(sin(minute_angle),-cos(minute_angle))`

`hour_endpoint=C+0.55R*(sin(hour_angle),-cos(hour_angle))`

Each hand is the straight segment from `C` to its computed endpoint. Independent snapping/repositioning is forbidden.

## Permanent anti-snap checkpoints

- 01:15 → hour angle 37.5°
- 03:30 → hour angle 105°; MUST NOT be 90°
- 09:30 → hour angle 285°; MUST NOT be 270°
- 02:45 → hour angle 82.5°; MUST NOT be 60°
- 08:45 → hour angle 262.5°; MUST NOT be 240°
- 11:45 → hour angle 352.5°; MUST NOT be 330°

## Required prompt state

Every analog-clock item now requires:
- exact shared center;
- exact minute/hour angles;
- exact normalized minute/hour endpoints;
- hand length ratios;
- relational verification;
- item-specific hard negative.

## Release semantics

Any future rendered analog clock whose hand endpoint is not collinear with the formula-derived ray is:

`ARTIFACT_CLOCK_HAND_ENDPOINT_QA=FAIL`
`ARTIFACT_CLOCK_ANTI_SNAP_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

This defect is retained permanently and may not be removed from regression coverage.
