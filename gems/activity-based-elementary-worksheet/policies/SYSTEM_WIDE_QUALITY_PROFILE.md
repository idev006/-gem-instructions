# System-Wide Quality Profile — Activity-Based Elementary Worksheet Generator

Version: 2.6.2 shared runtime contract
Applies to: Orchestrator + W01–W09 + every production prompt

This profile is inherited by every base worker. Domain rules remain owned by their specialist; this profile defines cross-worker quality behavior that must be consistent everywhere.

Companion mandatory profiles:

- `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
- `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`

## 1. Ownership integrity

- Only the owning specialist creates or changes domain truth.
- W07 audits learner-read geometry/scale integrity; W08 owns layout/render/text and review-protocol serialization; W09 owns release.
- Integration may combine verified states but must not silently override them.
- A conflict between worker outputs is resolved by ownership and SSOT precedence, never by ad-hoc final-prompt wording.

Gate: `SYSTEM_OWNERSHIP_INTEGRITY_QA`.

## 2. Complete normalization and provenance

Every material non-default mode, lock, precision, range, curriculum override, answer-key behavior or page constraint must record provenance as USER_EXPLICIT, PROFILE_DERIVED, DOMAIN_DEFAULT or SYSTEM_DEFAULT.

Do not invent a material restriction merely to simplify generation. If a request is safely resolvable by canonical defaults, resolve it; otherwise preserve ambiguity explicitly in internal state rather than fabricating user intent.

Gate: `SYSTEM_PARAMETER_PROVENANCE_QA`.

## 3. Independent academic verification

Every generated target/answer/data state must be verified against an independent relation, known-answer oracle, inverse operation, boundary rule or separately recomputed canonical state.

A tautology or formula compared only with itself is not sufficient evidence.

Examples:
- arithmetic: recompute result independently;
- exact division: quotient × divisor back to dividend;
- clock: semantic time ↔ numeric angles ↔ relational hand position;
- ruler: 1 cm @1 mm ↔ 10 intervals ↔ 11 positions ↔ 9 interior positions;
- speedometer: target speed ↔ tick index ↔ represented value ↔ target angle;
- thermometer: target ↔ tick index ↔ represented temperature ↔ liquid endpoint;
- scale/protractor/container: target ↔ index ↔ represented value ↔ geometry;
- calendar: date validity + independent Gregorian relation;
- graph: canonical data ↔ scale/key ↔ plotted representation.

Gate: `SYSTEM_INDEPENDENT_ORACLE_QA`.

## 4. Exact item count and atomic completeness

The requested question/region count is a hard academic constraint unless the user explicitly changes it.

For N questions there must be exactly N student-facing item objects and, when visuals are learner-read, exactly N renderer-state objects.

No item may inherit hidden target state through `same as above`, `etc.`, omitted rows or ambiguous table continuation.

Gate: `SYSTEM_ITEM_COUNT_QA`.

## 5. Difficulty fidelity

Do not silently weaken or inflate difficulty to make layout, generation or QA easier.

Difficulty is expressed through legitimate academic dimensions owned by the specialist: operand size, regrouping, granularity, conversion complexity, target resolution, route complexity, distractor quality, reading precision or reasoning steps.

A worksheet advertised as a specific skill must contain enough non-degenerate items to exercise that skill. Examples: a minor-tick scale worksheet must not collapse to whole-unit targets only; a nonzero-start ruler objective must actually include nonzero starts; a strict half-hour clock task must not introduce `:00`; a speedometer minor-tick task must include valid minor-tick targets rather than labelled values only.

Gate: `SYSTEM_DIFFICULTY_FIDELITY_QA`.

## 6. Distribution and anti-degeneracy

Unless the teacher requests a fixed repeated target, item generation should avoid accidental degenerate sets such as identical answers, one repeated target class, unused legend codes or only trivial boundary values.

Distribution remains subordinate to curriculum and explicit user constraints; variety never alters the requested skill.

Gate: `SYSTEM_TARGET_DISTRIBUTION_QA` when applicable.

## 7. Student/teacher visibility isolation

Student Blueprint contains only learner-visible semantics and blanks. Hidden targets, answers, indices, angles, exact liquid levels and renderer relations remain internal or teacher-visible renderer metadata.

Renderer metadata must be marked `RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

No sanitizer may convert a structurally leaked Student Blueprint into PASS after the fact.

Gate: `SYSTEM_VISIBILITY_ISOLATION_QA`.

## 8. Atomic renderer-state serialization

High-risk renderer state must be serialized as one atomic structured block per item:

- `ITEM_ID`
- `SEMANTIC_TARGET`
- `EXACT_RENDER_STATE`
- `RELATIONAL_VERIFICATION`
- `ITEM_SPECIFIC_HARD_NEGATIVE`

Do not use a wide Markdown table for high-risk per-item renderer state when wrapping, embedded line breaks or column drift can change field meaning. Prefer repeated labeled blocks or a machine-stable key/value list.

A correct number under the wrong semantic field is still a serialization failure.

Gate: `PROMPT_RENDER_STATE_SERIALIZATION_QA`.

## 9. Page-policy semantic consistency

`TARGET_PAGE_COUNT=1` and `ONE_PAGE_PREFERRED=YES` are preferences, not hard locks.

When `ONE_PAGE_LOCK=OFF`, final prompt wording must preserve safe pagination, e.g. `1 page preferred; paginate if minimum readability/geometry cannot be preserved`.

Hard one-page wording is forbidden unless `ONE_PAGE_LOCK=ON` has explicit user provenance.

Gate: `PROMPT_PAGE_POLICY_WORDING_QA`.

## 10. Self-contained final prompt

`FINAL_IMAGE_GENERATION_PROMPT` must be independently copy-ready. It cannot depend on earlier sections, omitted states, hidden tables, external files or conversational memory.

Every academic value required by the renderer must be serialized explicitly while remaining marked non-printable when hidden from students.

Gate: `SYSTEM_FINAL_PROMPT_SELF_CONTAINED_QA`.

## 11. Evidence-consistent QA

QA status is derived from actual compiled structures, not intended behavior.

If final output contradicts a gate — malformed renderer state, hard one-page wording while lock is OFF, missing item state, leaked target, unresolved render path, missing SCALE_LINE_SPEC, missing review protocol — the applicable gate is FAIL and `PROMPT_RELEASE=BLOCKED`.

A QA report may not declare PASS merely because a source policy exists.

Gate: `PROMPT_QA_EVIDENCE_CONSISTENCY_QA`.

## 12. Prompt vs artifact boundary

Prompt QA validates specification, math, state, serialization and release logic only.

Before inspection of a rendered worksheet:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

No prompt-level success or renderer self-review may be described as proof of actual tick count, glyph quality, alignment, crop safety or classroom readiness.

Gate: `SYSTEM_PHASE_BOUNDARY_QA`.

## 13. Revision discipline

A defect found in UAT must be traced to its owning rule/worker/integration gate. Fix canonical SSOT first, add a permanent regression reproducing the defect, then rebuild the package.

Do not repair only emitted final prose when the defect originates in architecture, normalization, ownership, scale topology, serialization or release logic.

Gate: `SYSTEM_REGRESSION_DISCIPLINE_QA`.

## 14. Mandatory learner-read scale-line integrity

Whenever a routed skill contains a learner-read clock face, dial, ruler, speedometer, thermometer, graduated container, protractor or graph axis, the complete `policies/SCALE_LINE_INTEGRITY_PROFILE.md` applies in addition to owning-domain rules.

Cross-worker responsibilities:

- owning academic worker defines scale values/topology and target state;
- W07 audits scale-line integrity;
- W08 preserves printed size, tick separation, label clearance and decoration isolation;
- W09 treats every applicable scale-line gate as release-blocking.

The final prompt serializes a resolved `SCALE_LINE_SPEC` for each canonical learner-read scale template. Vague instructions such as `draw clear ticks` or `standard scale marks` are insufficient.

No layout/theme optimization may merge, omit, thin below print-safe minimum, detach, reverse, compress, or visually obscure required graduations.

Gate family: `PROMPT_SCALE_LINE_SPEC_QA` plus all applicable gates defined in `SCALE_LINE_INTEGRITY_PROFILE.md`.

## 15. Mandatory instrument review–revise behavior

Whenever learner-read geometry exists, the complete `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md` applies.

The final prompt must communicate:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

and the logical loop:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

The renderer must independently recount/rederive the scale rather than simply repeat the intended formula. It must repair/regenerate any known mismatch and re-run the entire checklist before finalization.

This rule exists because a child may learn a false measurement concept from one extra/missing graduation. A visually attractive but academically wrong instrument is not acceptable.

Gate family:

`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`

Any applicable FAIL or NOT_RUN blocks release.

## 16. Actual artifact failure semantics

Renderer self-review is prevention, not acceptance evidence.

If a supplied worksheet artifact contains one wrong learner-read scale:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

The defect must become a permanent regression before the next accepted release artifact. The 2026-08-31 ruler extra-tick defect is the canonical 2.6.2 example of this discipline.
