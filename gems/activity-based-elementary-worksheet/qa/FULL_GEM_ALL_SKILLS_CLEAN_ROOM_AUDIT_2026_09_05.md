# Full GEM + All Skills Clean-Room Audit — 2026-09-05

Status: PROMPT/KNOWLEDGE HARDENING COMPLETE — ARTIFACT QUALIFICATION STILL SEPARATE
Release family: 2.6.3-LTS
Scope: architecture, routing, all 15 skills, shared policies, page semantics, renderer escape paths, QA/release and package integration.

## Audit objective

Re-review the entire multi-skill Gem after repeated real-artifact defects involving clock hour-hand placement, incomplete/incorrect instrument scales, tick hierarchy, and unnecessary pagination despite A4 Portrait feasibility.

## Reviewed skill set

ACADEMIC_ARITHMETIC_THAI; TIME_CALCULATION; ANALOG_CLOCK; WEIGHT_SCALE; RULER_LENGTH; DISTANCE; SPEEDOMETER; ANGLE_PROTRACTOR; PERIMETER_AREA; TEMPERATURE; CAPACITY; VOLUME; MONEY; CALENDAR; DATA_READING.

## Clean-room findings

### F1 — Registry version drift
DOMAIN_REGISTRY.md was still marked 2.6.2-LTS while the active release family is 2.6.3-LTS.
Resolution: update registry to 2.6.3-LTS.

### F2 — W10 missing from registry learner-read route text
Registry text said learner-read instruments require W07 + W08 + W09, omitting W10 even though current architecture requires independent metrology.
Resolution: OWNER -> W07 -> W10 -> W08 -> W09.

### F3 — Page-policy semantic drift
Generic ONE_PAGE_LOCK=OFF wording allowed pagination even after a named canonical profile had already proved one-page A4 feasibility.
Resolution: ordinary unlocked profile paginates only when one-page proof fails; a named canonical profile with passed numeric proof uses FEASIBILITY_CONFIRMED_ONE_PAGE_LAYOUT_REQUIRED=YES.

### F4 — Correct formulas were not enough to prevent renderer escape
Clock formula existed, but actual artifacts still showed wrong short-hand placement.
Resolution: minute-hand-driven displacement is explicit, exact vector endpoints remain mandatory, layout cannot independently move hands, and the artifact defect remains a permanent regression.

### F5 — Skill metric packs lacked a uniform runtime-state declaration
Skill packs contained oracle/metrics/repair information but did not all explicitly state the canonical-state-to-visible-state runtime invariant.
Resolution: add ALL_SKILLS_RUNTIME_INVARIANT_PROFILE.md, add RUNTIME_INVARIANT to all 15 skill metric packs, and bind routing/output/release to canonical-state-first execution.

## Cross-skill invariant

Every skill now follows:
CANONICAL_STATE -> INDEPENDENT_VERIFY -> STUDENT_VIEW_DERIVATION -> LAYOUT -> RELEASE

For learner-read geometry:
OWNER -> W07 -> W10 -> W08 -> W09

## Skill review verdict

All 15 prompt/Knowledge skill packs now contain owner, canonical oracle, prompt metrics, artifact metrics, critical defects, repair protocol, regression hooks, PASS_THRESHOLD=95, and an explicit runtime invariant/canonical-state requirement.

Prompt/Knowledge target: >=95 per skill. Critical academic defects remain non-compensatory.

## High-risk instrument verdict

ANALOG_CLOCK: 60 minute positions, common pivot, minute-first driver, continuous hour interpolation, exact vector endpoints, anti-snap, exact :15/:30/:45 relations, and P3 half-hour 10-item A4 Portrait canonical one-page proof.

WEIGHT_SCALE: 0–5 kg @0.1, 50/51 global topology, 10 intervals /11 positions per kg, midpoint 0.5 hierarchy, explicit active tick set, label order, inactive gap, common center and target pointer.

RULER_LENGTH: 10/11/9 per cm, 5 mm hierarchy, physical edge is not zero tick, zero/nonzero reference and endpoint projection guides.

SPEEDOMETER: 12/13, 240° active /120° inactive, target angle formula, common center, major/minor hierarchy.

ANGLE_PROTRACTOR: 180/181, perfect semicircle, common origin, radial ticks, 10°/5°/1° hierarchy and print-size oracle.

TEMPERATURE: exact 50/51 canonical profile, major/intermediate/minor hierarchy, local-span recount and endpoint alignment.

CAPACITY: 20/21, exact local 100 mL span grammar, meniscus/read point and no pseudo ticks.

DATA_READING: dataset-first, exact data-to-visual mapping, scale/tick inheritance for numeric axes, no 3D distortion or decorative data marks.

## Non-instrument skills verdict

TIME_CALCULATION, DISTANCE, PERIMETER_AREA, VOLUME, MONEY, CALENDAR and ACADEMIC_ARITHMETIC_THAI now explicitly require canonical internal state, independent verification and state-first repair. Their visible layouts may not become an alternate source of academic truth.

## Remaining boundary

This audit certifies prompt/Knowledge architecture only. It does NOT certify future rendered pixels.

Before rendered inspection:
ARTIFACT_QA=NOT_YET_TESTED
CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA

Any actual scale/hand/pointer/ray/level/data mismatch remains CRITICAL_ACADEMIC_DEFECT and blocks classroom release.

## Continuing discipline

Every newly observed systemic artifact defect must be recorded as actual defect evidence, traced to canonical/integration root cause, update SSOT rather than only a prompt, add permanent executable regression, and pass full CI before package release.