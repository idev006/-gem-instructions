# Instrument Scale Defect Taxonomy

Version: 1.0.0
Status: Mandatory defect taxonomy
Scope: learner-read instruments, scales, graph axes, pointers, hands, rays and levels

## 1. Severity model

`CRITICAL_ACADEMIC`: can teach a false reading model or produce a wrong answer.
`MAJOR_USABILITY`: does not change the canonical answer but likely confuses primary learners.
`MINOR_PRESENTATION`: cosmetic only and cannot change the reading.

Critical academic defects are non-compensatory:
`CRITICAL_ACADEMIC => ARTIFACT_QA=FAIL => CLASSROOM_RELEASE=BLOCKED`

## 2. Defect classes

### D1 Missing tick
Expected graduation is absent.

Examples:
- weight dial omits one or more 0.1 kg marks;
- ruler omits a millimeter mark;
- thermometer omits a 1°C graduation;
- protractor lacks required 1° marks.

Severity: CRITICAL_ACADEMIC when the omitted mark is part of the reading scale.

### D2 Extra tick
Unexpected graduation is present.

Examples:
- ruler edge is treated as an extra zero tick;
- inactive dial gap contains scale-like marks;
- container has local pseudo-ticks not in canonical scale.

Severity: CRITICAL_ACADEMIC when it can change counting/reading.

### D3 Wrong interval count
Number of intervals differs from canonical truth.

Examples:
- 1 kg span has fewer/more than 10 intervals for a 0.1 kg scale;
- 1 cm span has fewer/more than 10 mm intervals.

Severity: CRITICAL_ACADEMIC.

### D4 Wrong position count
Endpoint-inclusive positions do not match canonical count.

Severity: CRITICAL_ACADEMIC for learner-read scale.

### D5 Tick hierarchy failure
Major/intermediate/minor lengths are absent, reversed, or inconsistent.

Examples:
- 0.5 kg tick not longer than minor ticks;
- 5 mm tick not distinguishable from ordinary 1 mm ticks when needed;
- 10° protractor ticks are not visibly major.

Severity: CRITICAL_ACADEMIC when the hierarchy supports the intended reading; otherwise MAJOR_USABILITY.

### D6 Label-to-tick mismatch
Numeric label is offset from or associated with the wrong tick.

Severity: CRITICAL_ACADEMIC.

### D7 Reference origin/center error
Zero, center, baseline midpoint, pivot, or ray origin is wrong.

Examples:
- speedometer needle does not originate from center;
- protractor ray does not start at true center;
- object measurement starts from ruler border instead of zero graduation.

Severity: CRITICAL_ACADEMIC.

### D8 Target alignment error
Pointer/hand/ray/liquid endpoint/bar height does not align with canonical target.

Examples:
- 15:30 hour hand points exactly at 3 instead of halfway to 4;
- scale pointer lands between ticks without intended fractional target;
- bar height misses the intended gridline.

Severity: CRITICAL_ACADEMIC.

### D9 Nonuniform spacing
Equal-value subdivisions are not equally spaced.

Severity: CRITICAL_ACADEMIC when the student reads by counting scale steps.

### D10 Decorative pseudo-scale
Decoration resembles tick marks, axis marks, pointers, labels, or extra data.

Severity: CRITICAL_ACADEMIC if it can be read as academic data; otherwise MAJOR_USABILITY.

### D11 Layout-induced distortion
Scaling, perspective, cropping, compression, or rotation changes the academic geometry.

Severity: CRITICAL_ACADEMIC.

### D12 Artifact boundary violation
Prompt QA or renderer self-review is reported as if it were Artifact QA.

Severity: process critical; classroom release blocked until actual artifact is inspected.

## 3. Mandatory defect record fields

Every recorded defect must identify:
- `SKILL_ID`
- `ITEM_INDEX`
- `DEFECT_CLASS`
- `SEVERITY`
- `CANONICAL_EXPECTED_STATE`
- `VISIBLE_OBSERVED_STATE`
- `LEARNER_RISK`
- `OWNER_WORKER`
- `REPAIR_REQUIRED`
- `REGRESSION_REQUIRED`

## 4. Promotion rule

Any repeated or systemic CRITICAL_ACADEMIC defect becomes a permanent regression before the next accepted prompt/package release.
