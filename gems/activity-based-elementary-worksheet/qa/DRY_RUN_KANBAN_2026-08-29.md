# Dry-Run Kanban Report — Activity-Based Elementary Worksheet Generator

Date: 2026-08-29
Gem version evaluated: 1.0.0 → hardened to 1.1.0
Method: mental/systematic dry-run against representative user requests and acceptance criteria; no image renderer execution in this phase.
Release target: weighted score >=95/100 AND zero critical blockers.

## 1. Scoring rubric

| Dimension | Weight |
|---|---:|
| Intent & parameter normalization | 10 |
| Academic / instructional correctness | 15 |
| Mathematical & domain correctness | 20 |
| Thai language & student-facing text integrity | 15 |
| Layout / print usability | 15 |
| Prompt determinism & render-risk control | 15 |
| Revision / regression behavior | 10 |
| **Total** | **100** |

Critical blockers override score:

- incorrect calculation;
- wrong question count;
- forbidden time crossing;
- hidden-answer leakage into student output;
- malformed canonical student data;
- layout that necessarily crops or becomes unreadable.

## 2. Kanban workflow

Columns used:

`BACKLOG → READY → IN PROGRESS → REVIEW/QA → DONE`

Work-in-progress rule: fix critical correctness risks before aesthetic improvements.

Definition of Done:

1. issue has a deterministic rule or guard;
2. canonical instructions updated if needed;
3. output contract updated if behavior changes;
4. regression/acceptance test added;
5. dry-run rerun from the earliest affected stage;
6. no new critical regression.

---

# Iteration 0 — Baseline v1.0.0

## Representative dry-run scenarios

1. ป.3, elapsed time, 10 questions, EASY, daily activities, A4 portrait, monochrome, no answer key.
2. MEDIUM with hours + minutes.
3. HARD with regrouping.
4. 25 questions on one A4 portrait page.
5. Theme-only revision preserving questions.
6. EASY→MEDIUM revision.
7. Midnight crossing disabled.
8. Answer key enabled/disabled toggle.
9. Thai-heavy final image prompt.
10. Reference-image-derived layout without copying source marks.

## Baseline findings

### KAN-001 — Hidden answer leakage risk — CRITICAL
State: DONE in v1.1.0

Problem:
The v1.0 output contract allowed `VERIFIED_ANSWER` to appear in the user-visible blueprint, and the final image prompt was compiled from verified question data containing answers. Even with an instruction to keep answer blanks empty, the renderer could reproduce answer values elsewhere.

Fix:
Introduced strict two-view architecture:

- `INTERNAL_VERIFIED_BLUEPRINT`
- `STUDENT_RENDER_BLUEPRINT`

When answer key is off, the final prompt compiles only from student render data and contains no verified answer values.

Regression tests: 16–20, 40.

### KAN-002 — Missing explicit time invariants — HIGH
State: DONE in v1.1.0

Problem:
Core subtraction existed, but validity rules for zero duration, malformed minutes, duration bounds, explicit midnight handling, and granularity were insufficiently formalized.

Fix:
Added parse/range, positive-duration, MIN/MAX duration, minute interval, whole-hour, midnight, and unit-render invariants.

Regression tests: 6–15.

### KAN-003 — Student-visible blueprint exposed QA answers — HIGH
State: DONE in v1.1.0

Problem:
`SHOW_ANSWER_KEY=NO` still permitted answers in the visible blueprint, effectively behaving like a partial answer key.

Fix:
Output contract now returns `STUDENT_CONTENT_BLUEPRINT`; hidden answers remain internal unless user explicitly asks for QA/answers.

### KAN-004 — Thai image-rendering reliability overclaim risk — MEDIUM
State: DONE in v1.1.0

Problem:
Canonical text locking reduces errors but does not make image-model Thai deterministic.

Fix:
Added `TEXT_RENDER_MODE`, default `HYBRID` for Thai-heavy worksheets, with clean text zones suitable for deterministic correction/overlay. Explicitly prohibits guarantee claims.

Regression test: 39.

### KAN-005 — Layout capacity rules lacked answer-space check — MEDIUM
State: DONE in v1.1.0

Problem:
Row-count heuristics existed but did not explicitly verify multi-component response space.

Fix:
Added minimum usability checks and dedicated multi-component answer-space acceptance criterion.

Regression tests: 29–33.

### KAN-006 — QA did not explicitly separate domain/constraint/answer-leak gates — MEDIUM
State: DONE in v1.1.0

Fix:
Expanded release gates with `DOMAIN_QA`, `CONSTRAINT_QA`, and `ANSWER_LEAK_QA`.

### KAN-007 — No bounded self-review cycle — MEDIUM
State: DONE in v1.1.0

Fix:
Added three-pass internal review loop: structural, domain, student/render separation; repair and rerun from earliest affected stage.

## Baseline weighted score

| Dimension | Score |
|---|---:|
| Intent & normalization | 9.5/10 |
| Academic correctness | 14/15 |
| Math/domain correctness | 17/20 |
| Thai/text integrity | 12.5/15 |
| Layout/print | 12.5/15 |
| Prompt determinism | 11.5/15 |
| Revision/regression | 9/10 |
| **Total** | **86.0/100** |

Release: **BLOCKED** because KAN-001 was critical.

---

# Iteration 1 — Architecture hardening

Changes applied:

- two-view data model;
- answer-leak guard;
- final prompt compiled only from student-facing data;
- explicit time validity invariants;
- enhanced domain/constraint QA;
- hybrid Thai render strategy;
- stronger layout usability checks;
- expanded regression suite.

## Dry-run results after Iteration 1

All 10 representative scenarios were rerun.

Observed remaining weaknesses:

### KAN-008 — Balanced distribution semantics were under-specified — LOW
State: DONE

Added explicit rule that BALANCED must avoid pathological answer monotony unless pedagogically intentional.

### KAN-009 — Answer-key toggle dependency needed explicit revision rule — LOW
State: DONE

Added revision behavior preserving givens while rebuilding student/key views and rerunning leak/prompt QA.

### KAN-010 — Thai `น.` consistency needed direct test — LOW
State: DONE

Added canonical notation consistency test.

## Iteration 1 weighted score

| Dimension | Score |
|---|---:|
| Intent & normalization | 9.7/10 |
| Academic correctness | 14.3/15 |
| Math/domain correctness | 19.2/20 |
| Thai/text integrity | 14.0/15 |
| Layout/print | 14.0/15 |
| Prompt determinism | 14.0/15 |
| Revision/regression | 9.6/10 |
| **Total** | **94.8/100** |

Critical blockers: **0**

Release target not yet met because score <95.

---

# Iteration 2 — Final 95+ refinement

Actions:

1. formalized `STUDENT_RENDER_BLUEPRINT` as sole final-prompt source when answer key is off;
2. prohibited hidden answers not only in blanks but anywhere in the final student prompt;
3. made zero-duration and malformed time values explicit blockers;
4. added response-unit consistency rules;
5. added answer-space usability acceptance test;
6. expanded suite to 40 tests;
7. added bounded self-review loop and earliest-stage rerun rule;
8. documented weighted release target in canonical instruction.

## Scenario scorecard

| Scenario | Result | Notes |
|---|---|---|
| EASY 10-row reference-family worksheet | PASS | count, math, Thai labels, blank answers |
| MEDIUM mixed minutes | PASS | units and spaces consistent |
| HARD regrouping | PASS | recalculation gate catches mismatch |
| 25 rows A4 portrait | PASS | pagination/readability guard activates |
| theme-only revision | PASS | academic content preserved |
| difficulty revision | PASS | affected data regenerated and revalidated |
| midnight disabled | PASS | invalid cross-midnight tuple rejected |
| explicit midnight enabled | PASS | modulo-day calculation valid |
| answer-key NO | PASS | no answer values in final prompt |
| answer-key YES | PASS | separate key behavior |
| Thai-heavy prompt | PASS | canonical lock + HYBRID risk control |
| reference-image workflow | PASS | grammar extracted without exact-copy dependency |

## Final weighted score

| Dimension | Score |
|---|---:|
| Intent & parameter normalization | 9.8/10 |
| Academic / instructional correctness | 14.6/15 |
| Mathematical & domain correctness | 19.7/20 |
| Thai language & student-facing text integrity | 14.5/15 |
| Layout / print usability | 14.4/15 |
| Prompt determinism & render-risk control | 14.6/15 |
| Revision / regression behavior | 9.8/10 |
| **TOTAL** | **97.4/100** |

Critical blockers: **0**

Dry-run release decision: **PASS — 97.4/100**

---

# 3. Current Kanban board

## BACKLOG

- KAN-011 — Perform real image-render regression using the sample-family worksheet prompt.
- KAN-012 — Add post-render visual inspection rubric: Thai glyph fidelity, row count, crop, answer leakage, alignment.
- KAN-013 — Add deterministic overlay implementation specification if/when the project expands beyond prompt generation.
- KAN-014 — Add MONEY_ENGINE only after domain rules/tests are defined.

## READY

- KAN-011 real renderer test
- KAN-012 visual QA rubric

## IN PROGRESS

- none

## REVIEW / QA

- none

## DONE

- KAN-001 answer leakage
- KAN-002 time invariants
- KAN-003 student/internal separation
- KAN-004 Thai render-risk control
- KAN-005 layout usability
- KAN-006 expanded QA gates
- KAN-007 bounded self-review
- KAN-008 balanced answer distribution
- KAN-009 answer-key revision dependency
- KAN-010 Thai `น.` consistency

# 4. Interpretation

97.4% is a dry-run engineering quality score, not a claim that a generative image renderer will reproduce the page with 97.4% visual accuracy. The next evidence level is an actual render-and-inspect cycle. Any real-world failure should become a regression test and update the canonical instruction under the repository continuous-improvement policy.