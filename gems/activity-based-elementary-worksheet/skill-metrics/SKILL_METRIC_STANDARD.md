# Skill Metric Standard — Activity-Based Elementary Worksheet Generator

Version: 1.0.0
Status: Project SSOT — mandatory
Applies to: every declared worksheet-generation skill in this Gem

## 1. Purpose

This Gem is a multi-skill educational system. A high aggregate score must never hide a weak or unsafe skill.

Every skill MUST therefore have:
- a named owner;
- canonical academic truth;
- measurable prompt/knowledge indicators;
- measurable rendered-artifact indicators;
- explicit critical defects;
- regression hooks;
- a 100-point skill score;
- independent release evidence.

## 2. Mandatory score model

Every skill score is 100 points:

1. Academic correctness — 25
2. Canonical data/geometry fidelity — 25
3. Primary-school pedagogy/usability — 20
4. QA + independent verification + repairability — 20
5. Artifact evidence/readability — 10

Pass requirements:
- SKILL_PROMPT_SCORE >= 95
- SKILL_ARTIFACT_SCORE >= 95 for classroom qualification
- SKILL_TOTAL_SCORE >= 95
- no CRITICAL_ACADEMIC_DEFECT
- all mandatory skill gates PASS

A critical defect overrides numeric score:
`CRITICAL_ACADEMIC_DEFECT => SKILL_RELEASE=BLOCKED`

## 3. Critical truth rule

For any learner-read instrument or graph:
- scale topology is academic data;
- labels are academic data;
- pointer/hand/ray/liquid endpoint alignment is academic data;
- reference origin/center is academic data;
- missing/extra graduation is academic data;
- a visually attractive but academically false instrument is a release blocker.

## 4. Prompt vs artifact boundary

Prompt/Knowledge scoring and rendered Artifact scoring are separate.

A 100% prompt score does NOT imply a 100% rendered worksheet.

Required states:
`PROMPT_QA`
`SKILL_PROMPT_SCORE`
`ARTIFACT_QA`
`SKILL_ARTIFACT_SCORE`
`CLASSROOM_RELEASE`

Before actual inspection:
`ARTIFACT_QA=NOT_YET_TESTED`

## 5. Independent audit chain

Instrument/data skills:
`OWNER -> W07 when geometry/data scale is learner-read -> W10 when metrology applies -> W08 -> W09`

No owner may self-certify a high-risk artifact.

## 6. Default page policy

Unless the user explicitly overrides:
`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`

Pagination is preferred over degrading instructional geometry, typography, writing space or scale readability.

## 7. Scoring discipline

A metric may be marked:
- PASS
- FAIL
- NOT_APPLICABLE with documented reason

Do not award points for unsupported evidence.
Do not replace a failed critical metric by averaging with unrelated strong metrics.

## 8. Required metric-pack sections

Every skill metric pack MUST contain:
- SKILL_ID
- OWNER
- CANONICAL_ORACLE
- PROMPT_METRICS
- ARTIFACT_METRICS
- CRITICAL_DEFECTS
- REPAIR_PROTOCOL
- REGRESSION_HOOKS
- PASS_THRESHOLD=95
