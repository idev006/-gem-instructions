# System-Wide Quality Profile — Activity-Based Elementary Worksheet Generator

Version: 2.6.3 shared runtime contract
Applies to: Orchestrator + W01–W10 + every production prompt

This profile is inherited by every base worker. Domain truth remains owned by specialists; cross-worker safety is shared.

Companion mandatory profiles:
- `policies/SCALE_LINE_INTEGRITY_PROFILE.md`
- `policies/INSTRUMENT_REVIEW_REVISE_PROFILE.md`
- `policies/METROLOGY_ASSURANCE_PROFILE.md`
- `policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md` (mandatory learner-facing contract packaged with every worker)

## 1. Ownership integrity

- Only the owning specialist creates or changes domain truth.
- W07 audits learner-read geometry/scale integrity.
- W10 independently audits metrology, print feasibility, reference correctness and quantitative scale evidence.
- W08 owns layout/render/text and review-protocol serialization.
- W09 owns integration/release.
- W10 may reject unsafe geometry but may not invent academic targets or override W02–W06 formulas.

Gate: `SYSTEM_OWNERSHIP_INTEGRITY_QA`.

## 2. Complete normalization and provenance

Every material non-default mode, lock, precision, range, curriculum override, answer-key behavior or page constraint records provenance as USER_EXPLICIT, PROFILE_DERIVED, DOMAIN_DEFAULT or SYSTEM_DEFAULT.

Do not invent restrictions merely to simplify generation.

Gate: `SYSTEM_PARAMETER_PROVENANCE_QA`.

## 3. Independent academic verification

Every generated target/answer/data state must be checked by an independent relation, known-answer oracle, inverse operation, boundary rule or separately recomputed canonical state. A formula compared only with itself is insufficient.

Examples:
- arithmetic: independent recomputation;
- exact division: quotient × divisor;
- clock: semantic time ↔ numeric angles ↔ relational position;
- ruler: 1 cm @1 mm ↔ 10 intervals ↔ 11 positions ↔ 9 interior positions;
- speedometer: target ↔ tick index ↔ represented value ↔ angle;
- thermometer: target ↔ tick index ↔ represented temperature ↔ liquid endpoint;
- protractor/radial scale: topology plus independent printed arc-spacing oracle;
- container: target ↔ scale index ↔ read convention;
- graph: canonical data ↔ numeric scale ↔ physical mapping.

For learner-read instruments, W10 supplies an additional independent metrology recomputation; copying W07's PASS is not evidence.

Gate: `SYSTEM_INDEPENDENT_ORACLE_QA`.

## 4. Exact item count and atomic completeness

The requested question/region count is hard unless explicitly changed. N learner-read questions require exactly N student item objects and N renderer-state objects.

No hidden state via `same as above`, `etc.`, omitted rows or ambiguous continuation.

Gate: `SYSTEM_ITEM_COUNT_QA`.

## 5. Difficulty fidelity

Do not weaken/inflate difficulty for layout convenience. A minor-tick skill must actually exercise minor ticks; nonzero-start ruler tasks use nonzero starts; strict half-hour stays :30; discrete targets must be representable.

Gate: `SYSTEM_DIFFICULTY_FIDELITY_QA`.

## 6. Distribution and anti-degeneracy

Avoid accidental identical targets, unused legend codes or trivial-only sets unless requested. Variety never changes curriculum intent.

Gate: `SYSTEM_TARGET_DISTRIBUTION_QA` when applicable.

## 7. Student/teacher visibility isolation

Student Blueprint contains learner-visible semantics only. Hidden targets, answers, indices, angles, liquid levels, renderer relations, W07 audit data and W10 `METROLOGY_AUDIT_STATE` remain internal/teacher metadata.

Renderer metadata is marked `RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT.`

No sanitizer may convert a leaked blueprint into PASS.

Gate: `SYSTEM_VISIBILITY_ISOLATION_QA`.

## 8. Atomic renderer-state serialization

High-risk renderer state is one atomic structured block per item:
- `ITEM_ID`
- `SEMANTIC_TARGET`
- `EXACT_RENDER_STATE`
- `RELATIONAL_VERIFICATION`
- `ITEM_SPECIFIC_HARD_NEGATIVE`

Do not use a wide Markdown table for high-risk per-item renderer state when wrapping/column drift can change field meaning. A correct value under the wrong field is failure.

Gate: `PROMPT_RENDER_STATE_SERIALIZATION_QA`.

## 9. Page-policy semantic consistency

`TARGET_PAGE_COUNT=1` and `ONE_PAGE_PREFERRED=YES` are preferences, not hard locks.

When `ONE_PAGE_LOCK=OFF`, final prompt preserves safe pagination. Hard one-page wording is forbidden unless `ONE_PAGE_LOCK=ON` has explicit user provenance.

When lock is ON but W07/W10 minimum geometry cannot fit, release is blocked rather than shrinking academic scales.

Gate: `PROMPT_PAGE_POLICY_WORDING_QA`.

## 10. Self-contained final prompt

`FINAL_IMAGE_GENERATION_PROMPT` is independently copy-ready and contains every renderer-required academic value/state without external conversation dependencies.

Gate: `SYSTEM_FINAL_PROMPT_SELF_CONTAINED_QA`.

## 11. Evidence-consistent QA

QA status derives from compiled structures, not intended behavior. Malformed renderer state, wrong page semantics, missing item state, target leak, unresolved render path, missing `SCALE_LINE_SPEC`, missing review protocol, or missing W10 audit evidence = FAIL.

A QA report may not declare PASS merely because a source policy exists.

Gate: `PROMPT_QA_EVIDENCE_CONSISTENCY_QA`.

## 12. Prompt vs artifact boundary

Prompt QA validates specification/math/state/serialization/release logic only.

Before rendered worksheet inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

No prompt-level success, W10 audit or renderer self-review proves actual tick count/glyph/alignment/crop/classroom readiness.

Gate: `SYSTEM_PHASE_BOUNDARY_QA`.

## 13. Revision discipline

A UAT defect is traced to owning rule/worker/integration gate, fixed in canonical SSOT, converted to permanent regression, then fully rebuilt. Never repair only final prose when architecture/state is wrong.

Gate: `SYSTEM_REGRESSION_DISCIPLINE_QA`.

## 14. Mandatory learner-read scale-line integrity

Whenever a skill contains a learner-read clock, dial, ruler, speedometer, thermometer, graduated container, protractor or graph axis, `SCALE_LINE_INTEGRITY_PROFILE.md` applies.

Responsibilities:
- owning worker defines values/topology/target;
- W07 audits geometry;
- W10 independently audits metrology and print feasibility;
- W08 preserves dimensions/spacing/labels/decoration isolation;
- W09 treats all applicable gates as release-blocking.

Final prompt serializes resolved `SCALE_LINE_SPEC`; vague `draw clear ticks` is insufficient.

Gate family: `PROMPT_SCALE_LINE_SPEC_QA` plus all applicable scale-line gates.

## 15. Mandatory instrument review–revise behavior

Whenever learner-read geometry exists, `INSTRUMENT_REVIEW_REVISE_PROFILE.md` applies.

Final prompt communicates:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

and:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

Renderer independently recounts/rederives, repairs any mismatch and reruns the full checklist.

Gate family:
`PROMPT_NO_FIRST_PASS_INSTRUMENT_RELEASE_QA`
`PROMPT_INSTRUMENT_SELF_REVIEW_CHECKLIST_QA`
`PROMPT_INSTRUMENT_INDEPENDENT_RECOUNT_QA`
`PROMPT_INSTRUMENT_REVISE_UNTIL_PASS_QA`
`PROMPT_INSTRUMENT_REVIEW_EVIDENCE_QA`
`PROMPT_INSTRUMENT_REVIEW_PROTOCOL_SERIALIZATION_QA`

## 16. Mandatory independent metrology assurance

Every learner-read instrument additionally requires `METROLOGY_ASSURANCE_PROFILE.md` and W10 `METROLOGY_AUDIT_STATE`.

W10 independently verifies interval/position count, reference/origin, physical spacing, hierarchy, labels, target alignment, inactive region, template consistency and print/page feasibility.

Required gates include:
`PROMPT_METROLOGY_AUDIT_REQUIRED_QA`
`PROMPT_METROLOGY_INDEPENDENCE_QA`
`PROMPT_METROLOGY_SPACING_ORACLE_QA`
`PROMPT_METROLOGY_TARGET_ALIGNMENT_QA`
`PROMPT_METROLOGY_RENDER_PATH_QA`
`PROMPT_METROLOGY_PAGE_FEASIBILITY_QA`

Any applicable FAIL or NOT_RUN blocks release.

## 17. Actual artifact failure semantics

W07/W10/renderer checks are prevention, not acceptance evidence.

If a supplied worksheet contains one wrong learner-read scale:

`ARTIFACT_QA=FAIL`
`CLASSROOM_RELEASE=BLOCKED`

The defect becomes a permanent regression before the next accepted release artifact. The 2026-08-31 ruler extra-tick defect remains a canonical example.

## 18. Mandatory primary-school learner quality

Every production worksheet also inherits `policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`.

This makes the child's visible experience a release concern, not an aesthetic afterthought. Applicable checks include:

`SYSTEM_PRIMARY_GRADE_APPROPRIATENESS_QA`
`PROMPT_LEARNER_INSTRUCTION_CLARITY_QA`
`PROMPT_LEARNER_AMBIGUITY_QA`
`PROMPT_LEARNER_TYPOGRAPHY_QA`
`PROMPT_LEARNER_WRITING_SPACE_QA`
`PROMPT_LEARNER_VISUAL_LOAD_QA`
`PROMPT_LEARNER_DECORATION_ISOLATION_QA`
`PROMPT_LEARNER_ITEM_PROGRESSION_QA`
`PROMPT_TEACHING_INSTRUMENT_SIMPLICITY_QA`
`PROMPT_LEARNER_ANSWER_FORMAT_QA`
`PROMPT_LEARNER_PRINT_CONTRAST_QA`

When geometry is academic data, the pedagogy profile additionally requires:

`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES`
`CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES`
`POST_LAYOUT_GEOMETRY_TRANSFORM=UNIFORM_SCALE_AND_TRANSLATE_ONLY`

Physical fit is not sufficient if typography, writing space or visual load is unsafe. If pagination is unlocked, paginate before degrading learner-facing readability or instructional geometry.

For Artifact QA, also run `ARTIFACT_LEARNER_SIMULATION_QA`: the item must be understandable and solvable from visible student information alone.

Any applicable pedagogy FAIL/NOT_RUN blocks prompt release; any learner-visible ambiguity in the actual artifact blocks classroom release.