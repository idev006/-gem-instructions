# System-Wide Quality Profile — Activity-Based Elementary Worksheet Generator

Version: 2.6.x shared runtime contract
Applies to: Orchestrator + W01–W09 + every production prompt

This profile is inherited by every base worker. Domain rules remain owned by their specialist; this profile defines cross-worker quality behavior that must be consistent everywhere.

## 1. Ownership integrity

- Only the owning specialist creates or changes domain truth.
- W07 audits learner-read geometry; W08 owns layout/render/text; W09 owns release.
- Integration may combine verified states but must not silently override them.
- A conflict between worker outputs is resolved by ownership and SSOT precedence, never by ad-hoc final-prompt wording.

Gate: `SYSTEM_OWNERSHIP_INTEGRITY_QA`.

## 2. Complete normalization and provenance

Every material non-default mode, lock, precision, range, curriculum override, answer-key behavior or page constraint must record provenance as USER_EXPLICIT, PROFILE_DERIVED, DOMAIN_DEFAULT or SYSTEM_DEFAULT.

Do not invent a material restriction merely to simplify generation. If a request is safely resolvable by canonical defaults, resolve it; otherwise preserve the ambiguity explicitly in internal state rather than fabricating user intent.

Gate: `SYSTEM_PARAMETER_PROVENANCE_QA`.

## 3. Independent academic verification

Every generated target/answer/data state must be verified against an independent relation, known-answer oracle, inverse operation, boundary rule or separately recomputed canonical state.

A tautology or formula compared only with itself is not sufficient evidence of correctness.

Examples:
- arithmetic: recompute result independently;
- exact division: multiply quotient × divisor back to dividend;
- clock: semantic time ↔ numeric angles ↔ relational hand position;
- scale/ruler/protractor/container: target ↔ index ↔ represented value ↔ geometry;
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

A worksheet advertised as a specific skill must contain enough non-degenerate items to exercise that skill. Examples: a minor-tick scale worksheet must not collapse to whole-unit targets only; a nonzero-start ruler objective must actually include nonzero starts; a strict half-hour clock task must not introduce `:00`.

Gate: `SYSTEM_DIFFICULTY_FIDELITY_QA`.

## 6. Distribution and anti-degeneracy

Unless the teacher requests a fixed repeated target, item generation should avoid accidental degenerate sets such as identical answers, one repeated target class, unused legend codes or only trivial boundary values.

Distribution must remain subordinate to curriculum and explicit user constraints; variety must never alter the requested skill.

Gate: `SYSTEM_TARGET_DISTRIBUTION_QA` when applicable.

## 7. Student/teacher visibility isolation

Student Blueprint contains only learner-visible semantics and blanks. Hidden targets, answers, indices, angles, exact liquid levels and renderer relations remain internal or teacher-visible renderer metadata.

Renderer metadata must be marked `RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

No sanitizer may convert a structurally leaked Student Blueprint into PASS after the fact.

Gate: `SYSTEM_VISIBILITY_ISOLATION_QA`.

## 8. Atomic renderer-state serialization

High-risk renderer state must be serialized as one atomic structured block per item. Each block must keep field ownership unambiguous:

- `ITEM_ID`
- `SEMANTIC_TARGET` (renderer-only)
- `EXACT_RENDER_STATE` (index/angle/level/endpoints as applicable)
- `RELATIONAL_VERIFICATION`
- `ITEM_SPECIFIC_HARD_NEGATIVE`

Do not use a wide Markdown table for high-risk per-item renderer state when wrapping, embedded line breaks or column drift can change field meaning. Prefer repeated labeled blocks or a machine-stable key/value list.

A value placed under the wrong semantic field is a serialization failure even if the numeric value itself is correct.

Gate: `PROMPT_RENDER_STATE_SERIALIZATION_QA`.

## 9. Page-policy semantic consistency

`TARGET_PAGE_COUNT=1` and `ONE_PAGE_PREFERRED=YES` are preferences, not hard locks.

When `ONE_PAGE_LOCK=OFF`, final prompt wording must preserve safe pagination, e.g. `1 page preferred; paginate if minimum readability/geometry cannot be preserved`.

Phrases such as `exactly 1 page`, `must be one page`, or equivalent are forbidden unless `ONE_PAGE_LOCK=ON` has explicit user provenance.

Gate: `PROMPT_PAGE_POLICY_WORDING_QA`.

## 10. Self-contained final prompt

`FINAL_IMAGE_GENERATION_PROMPT` must be independently copy-ready. It cannot depend on earlier sections, omitted states, hidden tables, external files or conversational memory.

Every academic value required by the renderer must be serialized explicitly in the final prompt while remaining marked non-printable when hidden from students.

Gate: `SYSTEM_FINAL_PROMPT_SELF_CONTAINED_QA`.

## 11. Evidence-consistent QA

QA status must be derived from the actual compiled structures, not from intended behavior.

If final output structurally contradicts a gate — for example malformed renderer-state fields, hard one-page wording while lock is OFF, missing item state, leaked target, unresolved render path — the applicable gate is FAIL and `PROMPT_RELEASE=BLOCKED`.

A QA report may not declare PASS merely because the source policy exists.

Gate: `PROMPT_QA_EVIDENCE_CONSISTENCY_QA`.

## 12. Prompt vs artifact boundary

Prompt QA validates specification, math, state, serialization and release logic only.

Before inspection of a rendered worksheet:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

No prompt-level success may be described as proof of actual tick count, glyph quality, alignment, crop safety or classroom readiness.

Gate: `SYSTEM_PHASE_BOUNDARY_QA`.

## 13. Revision discipline

A defect found in UAT must be traced to its owning rule/worker/integration gate. Fix canonical SSOT first, add a permanent regression reproducing the defect, then rebuild the package.

Do not repair only the emitted final prompt when the defect originates in architecture, normalization, ownership, serialization or release logic.

Gate: `SYSTEM_REGRESSION_DISCIPLINE_QA`.

## 14. Mandatory learner-read scale-line integrity

Whenever any routed skill contains a learner-read clock face, dial, ruler, thermometer, graduated container, protractor, or graph axis, the complete `policies/SCALE_LINE_INTEGRITY_PROFILE.md` applies in addition to the owning domain rules.

This requirement is cross-worker:

- owning academic worker defines scale values/topology and target state;
- W07 audits scale-line integrity;
- W08 preserves minimum printed size, tick separation, label clearance and decoration isolation during layout;
- W09 treats every applicable scale-line gate as release-blocking.

The final prompt must serialize a resolved `SCALE_LINE_SPEC` for each canonical learner-read scale template. Vague instructions such as `draw clear ticks` or `standard scale marks` are insufficient.

No layout/theme optimization may merge, omit, thin below print-safe minimum, detach, reverse, compress, or visually obscure required scale graduations.

Gate family: `PROMPT_SCALE_LINE_SPEC_QA` plus all applicable gates defined in `SCALE_LINE_INTEGRITY_PROFILE.md`.