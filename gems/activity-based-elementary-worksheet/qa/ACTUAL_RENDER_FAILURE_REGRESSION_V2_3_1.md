# Actual-Render Failure Regression — v2.3.1

Status: Critical prompt-hardening regression
Applies to: `activity-based-elementary-worksheet` prompt generation

This suite is based on observed downstream worksheet render failures. It does not claim those rendered artifacts are production evidence; it converts observed failure modes into prompt-level regression requirements.

## AR-01 — Clock 10:30 midpoint
Final prompt for 10:30 must state all of:
- minute hand at 6 / 180°
- hour hand angle 315°
- hour hand exactly halfway between 10 and 11
- explicit negative: hour hand must not point directly at 10

Missing any relational redundancy = FAIL.

## AR-02 — Nonzero-minute hour displacement
For every clock with `m != 00`, final prompt must serialize hour-hand displacement `0.5*m` degrees beyond the hour numeral. A prompt that only says “show h:m” is insufficient for high-risk clock rendering.

## AR-03 — Half-hour batch audit
For a 10-item :30 worksheet, every item must independently include midpoint relation. Repeating one global statement without item states = FAIL.

## AR-04 — Thermometer exact tick alignment
For discrete graduated reading, liquid endpoint must coincide with target tick centerline. Prompt must explicitly prohibit between-tick placement.

## AR-05 — Thermometer representability
If minor interval=2°F, every generated target must be `MIN + k*2`. Nonrepresentable target generation = CRITICAL_ACADEMIC.

## AR-06 — Thermometer target-value leak
Renderer-only target numeric value must not be printed as an additional scale label, annotation, caption, or completed response.

## AR-07 — Scientific top meniscus
`READ_TOP_MENISCUS` must define a visibly curved meniscus and specify the highest designated reading point as the exact target-alignment point. Ambiguous near-flat line = FAIL.

## AR-08 — Scientific bottom meniscus
`READ_BOTTOM_MENISCUS` must define a concave meniscus and specify the lowest point as the exact target-alignment point.

## AR-09 — Meniscus target-label leak
Target value may control geometry but must not appear beside an arrow or as an added scale number. Example failure pattern: renderer adds a target-specific number such as “76” next to the scale.

## AR-10 — Meniscus instruction placement
Default worksheet should explain the meniscus convention once in instruction/example space. Repeating a reading arrow beside every item is discouraged unless explicitly required; any repeated annotation must not expose target values or obscure graduations.

## AR-11 — Canonical scale no-full-circle substitution
0–5 kg teaching dial final prompt must explicitly say `DO NOT draw a 360-degree value scale`.

## AR-12 — Inactive gap visibility
Prompt must require a clearly visible 60° inactive gap from 5→0 with zero value ticks in the gap interior.

## AR-13 — Canonical scale topology
Exactly 50 active intervals / 51 active tick positions. No continuous tick ring through inactive gap.

## AR-14 — Scale item-state serialization
Each dial item must include renderer-only target tick index + target angle + relational wording. Whole-page semantic labels alone = FAIL.

## AR-15 — Minor-tick pedagogy
When answer format includes `กิโลกรัม + ขีด`, item distribution must include sufficient non-whole-kilogram targets unless whole-kilogram-only practice is explicitly requested.

## AR-16 — Target alignment global gate
For every learner-read instrument, final prompt must encode `TARGET_ALIGNMENT_REQUIRED=YES` and downstream visual-QA language.

## AR-17 — Dual leak model
Both `ANSWER_LEAK_QA` and `TARGET_VALUE_LEAK_QA` must pass. Blank student answers do not compensate for renderer-only target numbers printed elsewhere.

## AR-18 — Per-item visual state
Every visual question must serialize `SEMANTIC TARGET + EXACT GEOMETRY + RELATIONAL WORDING + HARD NEGATIVE`. Missing item-specific state is prompt-incomplete.

## Release rule
Any AR-01..AR-18 critical failure blocks prompt release for the applicable domain.
