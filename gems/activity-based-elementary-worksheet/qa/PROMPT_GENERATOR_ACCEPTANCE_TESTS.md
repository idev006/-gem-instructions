# Prompt Generator Acceptance Tests

Version: 1.0.0
Applies to Gem baseline: 2.3.0+
Status: Critical regression suite

Purpose: verify that `activity-based-elementary-worksheet` behaves as a production worksheet **prompt generator**, not as a renderer and not as a blueprint-only assistant.

A critical failure in this suite blocks production prompt release.

## PG-01 — Primary deliverable exists

Input:

`ป.3 อ่านนาฬิกาเข็มชั่วโมงเต็ม 10 ข้อ A4 ขาวดำ ไม่มีเฉลย`

Expected:

- visible response contains `FINAL_IMAGE_GENERATION_PROMPT`;
- final prompt is not empty;
- response does not stop after student content/blueprint.

Failure class: `CRITICAL_PROMPT_COMPLETENESS`.

## PG-02 — Copy-ready standalone prompt

Copy only the contents of `FINAL_IMAGE_GENERATION_PROMPT` into a new context.

Expected: the downstream renderer has enough information to determine learner, subject, topic, page size, orientation, color mode, exact count, layout, student text, response blanks, visual states, constraints, and hard negatives without reading any earlier Gem section.

Forbidden dependencies:

- `see above`
- `use the blueprint above`
- `ตามตารางด้านบน`
- `ตามข้อมูลข้างต้น`
- unresolved external references.

Failure class: `CRITICAL_PROMPT_COMPLETENESS`.

## PG-03 — No pseudo-image placeholders

For visual worksheets, final prompt must contain no unresolved placeholders such as:

- `[ภาพ...]`
- `[รูป...]`
- `[insert clock]`
- `<draw here>`
- `TBD`
- `same as above`

Expected: every required visual is serialized as renderer-ready instructions.

Failure class: `CRITICAL_PLACEHOLDER`.

## PG-04 — Clock per-item serialization

For 10 analog-clock questions, define one canonical clock template and exactly 10 item states.

Each item state must contain enough renderer geometry to place both hands correctly. For minute-level faces, include required minute-mark topology.

A list such as `[ภาพนาฬิกา: เข็มสั้นชี้ 3]` without final renderer instructions fails.

## PG-05 — Scale per-item serialization

For canonical 0–5 kg / 0.1 kg scale reading:

- prompt defines 300° active sweep;
- 60° inactive gap;
- 50 active intervals;
- 51 active tick positions;
- no value ticks in inactive gap;
- one canonical dial template;
- exactly N needle/item states for N questions.

No state may be left for the renderer to invent.

## PG-06 — Linear graduation serialization

Ruler, thermometer, and graduated-capacity prompts must provide scale range + minor interval + expected interval/tick-position topology, or equivalent exact deterministic instructions.

Examples that must be representable:

- 1 cm at 1 mm resolution = 10 intervals / 11 endpoint-inclusive positions;
- 0–50°C at 1°C = 50 / 51;
- 0–1000 mL at 100 mL = 10 / 11.

## PG-07 — Student-visible answer integrity

When `SHOW_ANSWER_KEY=NO`:

- answer blanks remain blank;
- no solved answer list/key appears;
- no QA prose reveals answers;
- renderer-only geometry may exist only as instructions needed to draw the visual and must not be printed as worksheet answer text.

## PG-08 — Exact question-count serialization

For a request of N questions:

- blueprint has N items;
- final prompt has N student question regions/states;
- no `etc.`, `repeat similarly`, or implicit omitted remainder is allowed.

Failure class: `CRITICAL_PROMPT_COMPLETENESS`.

## PG-09 — Layout is explicit

Final prompt specifies a concrete layout suitable for the requested count, such as table rows or a 2×5 card grid.

It must include page orientation, title/header/instruction zones, response space, and minimum instrument size when applicable.

The downstream renderer must not have to infer how 10 questions fit on A4.

## PG-10 — Render path is downstream guidance

For `DOCUMENT_FIRST`, `HYBRID`, or `DETERMINISTIC_VECTOR`, final prompt explains how the downstream system should preserve deterministic text/data/geometry.

The Gem must not claim that it rendered the artifact itself merely because a render path was selected.

## PG-11 — No meta worksheet artifact

The requested downstream image target is a student worksheet.

Final prompt must prohibit rendering:

- QA dashboard;
- prompt poster;
- rubric;
- production notes;
- blueprint labels;
- hidden metadata;
- internal answers.

Use `RENDER_OBJECTIVE=STUDENT_WORKSHEET`.

## PG-12 — Prompt-release gate

Before release all must PASS:

`PROMPT_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`PLACEHOLDER_VISUAL_QA`
`VISIBLE_OUTPUT_SANITIZER_QA`
`ANSWER_LEAK_QA`
`QUESTION_COUNT_QA`
`LAYOUT_QA`

Plus applicable domain/geometry/topology gates.

One critical failure blocks final prompt release.

## Reference regression — the failure we must prevent

This output is **not sufficient** as the final deliverable:

```text
1.
[ภาพหน้าปัดนาฬิกา: เข็มสั้นชี้เลข 3, เข็มยาวชี้เลข 12]
ตอบ: ........ นาฬิกา
```

It may appear as an intermediate student-content representation, but production mode must continue to compile a standalone `FINAL_IMAGE_GENERATION_PROMPT` containing the canonical clock template, exact item geometry, page/layout instructions, visual constraints, and hard negatives.

## Release rule

A prompt that is academically correct but requires the user to manually convert placeholders/blueprints into renderer instructions is **incomplete**.

A production-ready prompt must be:

`VERIFIED + STUDENT-SAFE + SELF-CONTAINED + PLACEHOLDER-FREE + COPY-READY`.