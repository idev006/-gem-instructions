# Actual Weight-Dial Visible Subdivision Regression — 2026-09-01

## Evidence
A rendered Primary worksheet showed canonical integer labels `0,1,2,3,4,5`, but the visible minor graduations between adjacent whole-kilogram labels were sparsified. In particular, the 0→1 kg span did not visibly preserve all 0.1 kg graduation positions.

## Correct academic geometry
For canonical 0–5 kg at 0.1 kg resolution:
- 1 ขีด = 0.1 kg = 100 g;
- every 1 kg span = exactly 10 equal intervals;
- every 1 kg span = exactly 11 endpoint-inclusive positions;
- every 1 kg span = exactly 9 interior graduation positions;
- +0.5 kg is the fifth interval and is an existing intermediate position;
- the midpoint tick is longer/more prominent than ordinary 0.1 ticks but does not add a new physical position.

For 0→1 kg the mandatory visible angles are:
`0°,6°,12°,18°,24°,30°,36°,42°,48°,54°,60°`.

## Root cause
Global 50/51 topology and prose-level `INTERVALS_PER_KG=10` were present, but the downstream prompt contract did not force an explicit visible tick-set list for each local kilogram span. A renderer could therefore preserve labels while visually simplifying minor graduations.

## Permanent repair
Introduce `policies/WEIGHT_DIAL_VISIBLE_TICK_SET_PROFILE.md` and embed it into W03/W07/W08/W09/W10 runtime bundles. Final prompt must serialize both numeric counts and explicit per-span visible tick offsets/angles.

## Release rule
Any rendered whole-kilogram span that does not contain exactly 10 spaces and 9 interior graduation marks is a critical academic defect:

`ARTIFACT_WEIGHT_PER_KG_SUBDIVISION_QA=FAIL`
`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

This defect must remain protected by an additive executable regression suite.
