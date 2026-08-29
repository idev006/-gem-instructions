# Teacher Usability Tests — Activity-Based Elementary Worksheet Generator

Version: 1.2.0
Status: Required usability regression suite

Purpose: verify that the Gem remains usable by teachers who do not know technical prompt syntax or parameter names.

## TU-01 — Minimum three-item request

Input:

> ป.3 เรื่องหาระยะเวลา 10 ข้อ

Expected:
- accept without a technical questionnaire;
- resolve subject, language, page, design, answer-key, and render-safety defaults;
- proceed to content planning.

PASS if the teacher can proceed with only grade + skill + count.

## TU-02 — Missing grade

Input:

> เรื่องหาระยะเวลา 10 ข้อ

Expected: ask one concise question for grade level.

FAIL if the Gem asks for unrelated technical parameters at the same time.

## TU-03 — Missing question count

Input:

> ป.3 เรื่องหาระยะเวลา

Expected: ask one short question such as `ต้องการประมาณกี่ข้อครับ เช่น 8, 10 หรือ 12 ข้อ?`

FAIL if a production question count is silently invented.

## TU-04 — Ambiguous time skill

Input:

> ป.3 เรื่องเวลา 10 ข้อ

Expected: if the exact skill is not safely inferable, ask one simple choice-oriented question such as reading clocks vs elapsed time.

FAIL if the system exposes internal enum names.

## TU-05 — Natural-language difficulty

Input:

> ขอแบบง่าย ๆ เด็กคิดไม่ยาก คำตอบเป็นชั่วโมงเต็ม

Expected internal resolution:
- EASY
- whole-hour duration
- no unnecessary minute component in response

FAIL if the user must provide technical parameter syntax.

## TU-06 — Natural-language design revision

Input:

> ทำให้น่ารักขึ้น แต่ไม่เอารูปเยอะจนบังโจทย์

Expected: modify visual theme/decoration only; preserve academic content unless explicitly requested.

## TU-07 — Optional parameters always resolve

For every optional parameter in a released normalized spec, state must be one of:
- concrete DEFAULT;
- AUTO/DERIVED resolved value;
- intentional NONE.

FAIL on silent undefined values.

## TU-08 — Explicit user value overrides default

Input:

> A4 แนวนอน แบบสี

Expected:
- orientation LANDSCAPE
- color mode COLOR

FAIL if default portrait/monochrome silently overrides explicit teacher request.

## TU-09 — Internal safety parameters hidden from ordinary users

Normal teacher request must not ask the teacher to choose:
- CONTENT_LOCK
- THAI_TEXT_LOCK
- NUMERIC_VALUE_LOCK
- QUESTION_COUNT_LOCK
- ANSWER_LEAK_GUARD

These resolve internally unless the user explicitly asks for advanced settings.

## TU-10 — Teacher-friendly response language

The Gem should prefer phrases such as:

> ได้ครับ ผมจะใช้ A4 แนวตั้ง ขาวดำ และไม่ใส่เฉลยให้โดยอัตโนมัติ

rather than dumping internal parameter names unless technical output is requested.

## TU-11 — Copy-and-edit examples

Documentation must provide examples that a teacher can copy and modify with ordinary Thai words.

PASS threshold: at least 20 varied natural-language examples covering creation, revision, layout, theme, answer key, difficulty, and edge cases.

## TU-12 — Follow-up simplicity

Input after a generated set:

> เอาหมายเลขข้อออก

Expected: update only the relevant normalized field and layout, then rerun dependent QA.

FAIL if the Gem asks the teacher to restate the entire worksheet specification.

## TU-13 — Explain defaults without jargon

When the teacher asks `ถ้าไม่บอกอะไรเพิ่มจะได้แบบไหน`, explain practical defaults in teacher-facing language first. Technical names may be shown only as optional detail.

## TU-14 — No needless clarification

Input:

> ป.3 เรื่องหาระยะเวลา 10 ข้อ ขาวดำ

Expected: do not ask subject, page size, orientation, answer key, or theme unless needed; use documented defaults.

## TU-15 — Default policy traceability

Every default used by the current production Gem must be documented in `policies/PARAMETER_POLICY.md` or an explicitly referenced domain policy.

FAIL if behavior depends on an undocumented hidden default.
