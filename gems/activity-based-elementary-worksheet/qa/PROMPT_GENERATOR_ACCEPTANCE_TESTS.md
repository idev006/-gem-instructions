# Prompt Generator Acceptance Tests

Version: 1.1.0
Applies to Gem baseline: 2.3.2+
Status: Critical regression suite

Purpose: verify that `activity-based-elementary-worksheet` behaves as a production worksheet **prompt generator**, not as a renderer and not as a blueprint-only assistant.

A critical failure in this suite blocks production prompt release.

## PG-01 — Primary deliverable exists
Input: `ป.3 อ่านนาฬิกาเข็มชั่วโมงเต็ม 10 ข้อ A4 ขาวดำ ไม่มีเฉลย`

Expected:
- visible response contains `FINAL_IMAGE_GENERATION_PROMPT`;
- final prompt is not empty;
- response does not stop after student content/blueprint.

## PG-02 — Copy-ready standalone prompt
Copy only `FINAL_IMAGE_GENERATION_PROMPT` into a new context.

Expected: downstream renderer can determine learner, subject, topic, page size, orientation, color mode, exact count, layout, student text, response blanks, visual states, constraints, and hard negatives without reading earlier Gem sections.

Forbidden dependencies: `see above`, `use the blueprint above`, `ตามตารางด้านบน`, `ตามข้อมูลข้างต้น`, unresolved external references.

## PG-03 — No pseudo-image placeholders
Final prompt contains none of: `[ภาพ...]`, `[รูป...]`, `[insert clock]`, `<draw here>`, `TBD`, `same as above`.

Every required visual is renderer-ready.

## PG-04 — Clock per-item serialization
For N analog-clock questions, define one canonical clock template and exactly N item states. Each state contains minute angle/relationship, continuous hour-hand angle/relationship, and an item-specific negative when minutes are nonzero.

## PG-05 — Scale per-item serialization
For canonical 0–5 kg / 0.1 kg scale reading:
- 300° active sweep;
- visible 60° inactive gap;
- 50 active intervals;
- 51 active tick positions;
- no value ticks in inactive gap;
- explicit `DO NOT draw a 360-degree value scale`;
- one canonical dial template;
- exactly N needle/item states.

## PG-06 — Linear graduation serialization
Ruler, thermometer, and capacity prompts provide scale range + minor interval + exact interval/tick-position topology or equivalent deterministic instructions.

## PG-07 — Student-visible answer integrity
When `SHOW_ANSWER_KEY=NO`, answer blanks remain blank; no answer list/key or QA prose reveals answers.

## PG-08 — Exact question-count serialization
For N questions, blueprint and final prompt both contain exactly N question states. No `etc.` or implicit omitted remainder.

## PG-09 — Layout is explicit
Final prompt specifies concrete page/layout structure, zones, response space, and minimum instrument size when applicable.

## PG-10 — Render path is downstream guidance
Gem does not claim it rendered an artifact merely because a render path was selected.

## PG-11 — No meta worksheet artifact
Final prompt requires `RENDER_OBJECTIVE=STUDENT_WORKSHEET` and prohibits QA dashboard, prompt poster, rubric, hidden metadata, internal answers.

## PG-12 — Prompt-release gate
Before release all applicable critical gates pass, including prompt, placeholder, sanitizer, count, layout, domain and geometry gates.

## PG-13 — KB route is explicit and complete
For each supported domain, `KB_ROUTE_QA` selects the required engine set defined by `DOMAIN_REGISTRY.md` and `KB_ROUTER.md`.

Visual instrument domain without `INSTRUMENT_READING_ENGINE.md` = FAIL.

## PG-14 — KB compatibility gate
If required core KB is missing or known incompatible with `KB_MANIFEST.md`, `KB_COMPATIBILITY_QA=FAIL` and the Gem must not claim a production-ready prompt.

## PG-15 — Core completeness regression
A baseline upgrade must not silently remove major production contracts. Core must retain at least:
- mission/product boundary;
- parameter policy link;
- two-view separation;
- domain/KB routing;
- instrument rules;
- render-path guidance;
- one-page policy;
- layout policy;
- Thai/text policy;
- prompt compiler/no-placeholder rule;
- render-objective lock;
- visible-output sanitizer;
- QA framework;
- downstream artifact-QA distinction;
- revision/release policy.

A shortened replacement that drops these contracts = `CRITICAL_GOVERNANCE`.

## PG-16 — Dual leak guard
For visual instruments with renderer-only targets, both `ANSWER_LEAK_QA` and `TARGET_VALUE_LEAK_QA` must pass. Blank student answer fields do not compensate for a target number printed beside a scale/arrow.

## PG-17 — Redundant high-risk visual state
Every high-risk visual item contains:
`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`.

Semantic-only state such as `show 10:30` is insufficient for a clock :30 regression case.

## PG-18 — Prompt QA vs artifact QA distinction
The Gem may report prompt QA after prompt compilation. It must not report actual rendered artifact QA as PASS unless the actual downstream artifact has been inspected.

## Reference regressions

Insufficient final deliverable:

```text
1.
[ภาพหน้าปัดนาฬิกา: เข็มสั้นชี้เลข 3, เข็มยาวชี้เลข 12]
ตอบ: ........ นาฬิกา
```

Required production principle:

`VERIFIED + STUDENT-SAFE + SELF-CONTAINED + PLACEHOLDER-FREE + COPY-READY + KB-COMPATIBLE + PER-ITEM-EXACT`

## Release rule

A prompt that is academically correct but requires manual conversion from placeholders/blueprints is incomplete. A prompt that uses missing/incompatible KB or leaves high-risk geometry to renderer inference is also incomplete.