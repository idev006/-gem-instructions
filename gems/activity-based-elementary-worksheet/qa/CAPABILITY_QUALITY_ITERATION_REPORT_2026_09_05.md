# Capability Quality Iteration Report — 2026-09-05

Status: PASS
Scope: Activity-Based Elementary Worksheet Generator prompt/knowledge capability quality
Artifact boundary: rendered worksheet pixels are not certified by this report.

## Acceptance target

User-defined target:
- overall capability score >=95%
- every individual capability score >=95%

Scoring SSOT: `policies/CAPABILITY_QUALITY_GATE.md`
Executable: `tools/capability_quality_scorecard.py`

Each capability uses the same 20-criterion / 100-point rubric covering:
academic correctness, primary pedagogy, rendering/data fidelity, QA/repairability, and usability/evidence.

## Iteration 1

Overall: **97.67%**

| Capability | Score |
|---|---:|
| ACADEMIC_ARITHMETIC_THAI | 95% |
| TIME_CALCULATION | 90% |
| ANALOG_CLOCK | 95% |
| WEIGHT_SCALE | 100% |
| RULER_LENGTH | 100% |
| DISTANCE | 100% |
| SPEEDOMETER | 100% |
| ANGLE_PROTRACTOR | 100% |
| PERIMETER_AREA | 100% |
| TEMPERATURE | 100% |
| CAPACITY | 100% |
| VOLUME | 100% |
| MONEY | 95% |
| CALENDAR | 95% |
| DATA_READING | 95% |

Gate: FAIL because TIME_CALCULATION <95.

Root cause:
- visual/decorative separation contract not explicit enough for time-calculation worksheets;
- repair protocol did not explicitly require complete canonical relation recomputation.

Remediation:
- added `TIME_ITEM_STATE`;
- added visual-data hard negatives;
- added `TIME_REPAIR_REQUIRES_FULL_RELATION_RECHECK=YES`.

## Iteration 2

Overall: **98.33%**
Every capability >=95: YES.

TIME_CALCULATION improved 90% -> 100%.

Gate: PASS.

Five capabilities remained at exactly 95 because repair guidance was less explicit than the strongest domain contracts:
ACADEMIC_ARITHMETIC_THAI, ANALOG_CLOCK, MONEY, CALENDAR, DATA_READING.

## Iteration 3

Added owner-level canonical repair/recheck protocols for all five remaining capabilities.

Final score:

| Capability | Score |
|---|---:|
| ACADEMIC_ARITHMETIC_THAI | 100% |
| TIME_CALCULATION | 100% |
| ANALOG_CLOCK | 100% |
| WEIGHT_SCALE | 100% |
| RULER_LENGTH | 100% |
| DISTANCE | 100% |
| SPEEDOMETER | 100% |
| ANGLE_PROTRACTOR | 100% |
| PERIMETER_AREA | 100% |
| TEMPERATURE | 100% |
| CAPACITY | 100% |
| VOLUME | 100% |
| MONEY | 100% |
| CALENDAR | 100% |
| DATA_READING | 100% |

**OVERALL_CAPABILITY_SCORE=100.00%**
**EVERY_CAPABILITY_SCORE>=95=YES**
**CAPABILITY_QUALITY_GATE=PASS**

## Interpretation boundary

This score certifies the structure/completeness of Gem instructions and Knowledge SSOT against the capability rubric.

It does not certify downstream rendered pixels.

Therefore:
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Actual classroom qualification still requires rendered Artifact QA.
