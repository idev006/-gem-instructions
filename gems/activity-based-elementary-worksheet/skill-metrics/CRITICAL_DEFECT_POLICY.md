# Critical Defect Policy

Version: 1.0.0
Status: Mandatory project release policy

## Rule

Any defect that can teach a child a false academic model is a `CRITICAL_ACADEMIC_DEFECT`.

Critical defects are non-compensatory:
`CRITICAL_ACADEMIC_DEFECT => ARTIFACT_QA=FAIL => CLASSROOM_RELEASE=BLOCKED`

## Universal critical classes

1. wrong answer or formula;
2. missing/extra scale graduation;
3. wrong interval/value mapping;
4. pointer/hand/ray/liquid endpoint does not align with canonical target;
5. wrong zero/reference/center;
6. label order/value mismatch;
7. graph/table visual does not match canonical data;
8. answer leakage when key is disabled;
9. ambiguity that allows two academically different readings;
10. layout transformation distorts academic geometry.

## Instrument examples

Clock:
- 15:30 with hour hand exactly at 3 is critical.
- Correct: minute hand at 6; hour hand exactly halfway between 3 and 4.

Weight dial 0–5 kg @0.1 kg:
- any 1 kg span not having exactly 10 intervals is critical;
- +0.5 kg midpoint hierarchy missing or misleading is critical.

Ruler 1 cm @1 mm:
- not exactly 10 intervals per cm is critical;
- ruler border substituted for zero graduation is critical.

Thermometer:
- liquid endpoint on wrong graduation is critical.

Protractor:
- wrong center/baseline/ray origin or distorted semicircle is critical.

Capacity:
- extra local graduations that imply a false interval are critical.

Graph:
- bar height inconsistent with dataset/axis is critical.

## Repair

Critical defects must be repaired at the canonical owner state and fully rechecked. Visual nudging alone is not an acceptable repair.
