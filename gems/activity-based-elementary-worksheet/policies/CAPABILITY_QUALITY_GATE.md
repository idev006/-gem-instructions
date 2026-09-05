# Capability Quality Gate — Primary Worksheet Generator

Version: 1.0.0
Compatible Gem baseline: 2.6.x
Status: Mandatory prompt/knowledge capability score SSOT

## Purpose

A green aggregate regression count is not enough. Every declared worksheet capability must independently demonstrate production-quality instructions and knowledge.

Target:
- OVERALL_CAPABILITY_SCORE >= 95%
- EVERY_CAPABILITY_SCORE >= 95%
- no critical academic/safety blocker
- Artifact QA remains separate and cannot be inferred from this score.

## Scored capabilities

1. ACADEMIC_ARITHMETIC_THAI
2. TIME_CALCULATION
3. ANALOG_CLOCK
4. WEIGHT_SCALE
5. RULER_LENGTH
6. DISTANCE
7. SPEEDOMETER
8. ANGLE_PROTRACTOR
9. PERIMETER_AREA
10. TEMPERATURE
11. CAPACITY
12. VOLUME
13. MONEY
14. CALENDAR
15. DATA_READING

## Uniform 100-point rubric

Each capability is scored on 20 independently auditable criteria, 5 points each:

### A. Academic correctness — 25
A1 explicit scope and non-scope
A2 deterministic canonical rules/formulas
A3 target/answer representability or validity
A4 independent recomputation/verification
A5 explicit critical failure conditions

### B. Primary pedagogy — 20
B1 grade progression or conservative grade rule
B2 learner-visible wording/answer format contract
B3 difficulty changes academic complexity, not visual ambiguity
B4 child-readable/writable layout inherits primary pedagogy profile

### C. Rendering/data fidelity — 20
C1 canonical renderer/data state
C2 explicit geometry/data mapping when visual
C3 decoration cannot alter/imitate academic data
C4 deterministic/vector/document render ownership is stated when applicable

### D. QA and repairability — 25
D1 domain-specific QA gates
D2 negative/hard-negative rules
D3 known failure modes or repair guidance
D4 regression evidence/executable test coverage
D5 route/owner integration is explicit

### E. Usability/evidence — 10
E1 worked/example command or canonical example exists
E2 teacher usability/output behavior is documented

Score = passed criteria / 20 * 100.
A capability with any CRITICAL blocker is capped below 95 regardless of raw score.

## Release rule

`CAPABILITY_QUALITY_GATE=PASS` only when:
- every capability >=95;
- overall arithmetic mean >=95;
- no critical blocker;
- the scoring executable emits a per-capability matrix;
- CI runs the executable before package build.

This gate measures prompt/knowledge-system capability only.

It does NOT mean:
`ARTIFACT_QA=PASS`
or
`CLASSROOM_RELEASE=READY`.

Actual rendered worksheets still require Artifact QA.


## Skill-specific metric authority

The generic 20-criterion capability rubric is necessary but not sufficient.

Every declared capability MUST also comply with its skill-specific pack under:
`skill-metrics/*_SKILL_METRICS.md`

Mandatory governance:
`SKILL_METRIC_PACK_QA=PASS`
`SKILL_METRIC_PACK_REGRESSION=161/161 PASS`

The skill pack is authoritative for domain-specific critical defects and canonical instrument/data indicators. A generic 100% capability score cannot compensate for a failed skill-specific critical metric.
