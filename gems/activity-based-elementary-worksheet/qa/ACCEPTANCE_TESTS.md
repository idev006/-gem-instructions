# Acceptance Tests — Activity-Based Elementary Worksheet Generator

Version: 1.1.0
Status: Critical QA / Regression Suite

A production release passes only when all critical tests pass. Critical answer-leak, mathematical, count, and layout failures block release regardless of weighted score.

## Core intent and structure

### Test 1 — Intent normalization
Input: `สร้างใบงาน ป.3 คณิตศาสตร์ เรื่องการหาระยะเวลา 10 ข้อ ธีมกิจกรรมประจำวัน A4 แนวตั้ง ขาวดำ ไม่ต้องมีเฉลย`
Expected: ป.3, คณิตศาสตร์, TIME, 10 questions, A4 portrait, monochrome, no answer key, daily-activity context.

### Test 2 — Exact question count
For `QUESTION_COUNT = 10`, internal blueprint, student blueprint, and final prompt must each contain exactly 10 unique question IDs/rows.

### Test 3 — Student header
Default Thai student worksheet contains `ชื่อ ... ชั้น ... เลขที่ ...` unless disabled.

### Test 4 — Prompt package completeness
Default output contains: normalized spec, student content blueprint, layout blueprint, render constraints, QA report, final image prompt.

### Test 5 — Prompt-only still validates
`PROMPT_ONLY` hides intermediate sections but still executes all internal validation.

## TIME_ENGINE correctness

### Test 6 — Whole-hour correctness
With EASY + whole-hour-only, every tuple satisfies `(end-start) % 60 == 0`.
Must pass: 08:15→10:15 = 2h; 06:45→07:45 = 1h.

### Test 7 — Mixed minutes correctness
08:15→09:45 validates as 1h30m.

### Test 8 — Same-day ordering
When midnight crossing is disabled, end must be later than start.

### Test 9 — Midnight guard
20:00→08:00 is rejected/repaired when crossing midnight is disabled.

### Test 10 — Explicit midnight crossing
When crossing midnight is enabled, 23:30→00:30 validates as 60 minutes, not a negative duration.

### Test 11 — Zero duration guard
08:00→08:00 is rejected unless zero duration is explicitly allowed.

### Test 12 — Minute range validation
Times such as 08:75 or 10:60 must be rejected/repaired.

### Test 13 — Duration bounds
Generated duration must remain within active MIN_DURATION/MAX_DURATION.

### Test 14 — Minute interval constraint
If MINUTE_INTERVAL=15, generated minute values relevant to the task must respect the active 15-minute granularity policy.

### Test 15 — Answer unit consistency
A mixed duration such as 1h30m must not render only `ชั่วโมง` if the expected response requires minutes too.

## Answer integrity

### Test 16 — Empty student blank
When `SHOW_ANSWER_KEY = NO`, student response areas remain blank.

### Test 17 — Internal/student separation
Internal verified blueprint may contain answers; student content blueprint must not.

### Test 18 — Final prompt answer-leak guard
When answer key is disabled, verified answers MUST NOT appear anywhere in the final student image prompt, including comments, tables, hidden annotations, examples, or decorative text.

### Test 19 — Separate answer key
When answer key is enabled, student worksheet remains unsolved and answers appear in a separate key/page by default.

### Test 20 — Answer-key toggle revision
Switching key NO→YES preserves givens and rebuilds only output views/key data; switching YES→NO removes all answer values from student-facing output.

## Diversity and semantics

### Test 21 — Duplicate full-question prevention
Accidental identical tuples are prohibited unless explicitly requested.

### Test 22 — Intentional activity repetition
`ใช้ 5 กิจกรรมนี้อย่างละ 2 ข้อ` permits repeated activity names while requiring distinct source tuples.

### Test 23 — Semantic icon mapping
Book↔reading, football↔football, watering can/plant↔watering plants. Contradictory icons fail.

### Test 24 — Balanced answer distribution
`ANSWER_DISTRIBUTION=BALANCED` should not collapse all questions to one identical answer unless the objective explicitly asks for that drill.

## Thai and instructional QA

### Test 25 — Canonical Thai terminology
Verify: `เวลาเริ่มต้น`, `เวลาสิ้นสุด`, `ใช้เวลา`, `ชั่วโมง`, `นาที`, plus title/instruction/activity labels.

### Test 26 — `น.` consistency
When Thai time notation uses `น.`, it is applied consistently across all rows.

### Test 27 — Grade appropriateness
Difficulty and wording must match the requested grade; decoration may not be used as a substitute for instructional appropriateness.

### Test 28 — Single learning objective
All questions practice the declared objective unless the user explicitly requests mixed skills.

## Layout / print / reference QA

### Test 29 — Layout capacity
25 detailed rows on one A4 portrait page triggers a density warning/repair and preferably pagination unless the user explicitly insists on one page.

### Test 30 — Auto-pagination
When capacity is exceeded and AUTO_PAGINATION=YES, split without cropping or microscopic text.

### Test 31 — Answer-space usability
Multi-component answers receive enough blank space for both hours and minutes.

### Test 32 — Decoration priority
Characters, stars, hearts, clocks, borders, and icons may not overlap text or answer areas.

### Test 33 — Monochrome print usability
Black-and-white mode uses white background, high-contrast line art, safe margins, and no essential color coding.

### Test 34 — Reference-image independence
Reference image informs information architecture/design grammar but does not make its numeric data canonical unless explicitly requested.

### Test 35 — No unsupported exact-copy behavior
Do not claim pixel-perfect recreation or reproduce creator marks/watermarks/proprietary characters without authorization.

## Revision and render robustness

### Test 36 — Theme-only revision preserves content
Changing theme while saying `ห้ามเปลี่ยนโจทย์` preserves activities/times and only changes visual plan; dependent layout/render QA reruns.

### Test 37 — Difficulty revision regenerates content
EASY→MEDIUM updates question tuples as needed and recalculates all answers; it must not merely change prompt wording.

### Test 38 — Orientation revision
Portrait→landscape preserves content but reruns layout/print/prompt QA.

### Test 39 — Hybrid text mode
For Thai-heavy worksheets, HYBRID mode reserves clean text zones and does not claim guaranteed perfect model-native Thai rendering.

### Test 40 — Student render source
Final prompt must compile from STUDENT_RENDER_BLUEPRINT when answer key is disabled, never from INTERNAL_VERIFIED_BLUEPRINT.

## Release gate

All applicable statuses must be PASS:

```text
INTENT_QA = PASS
DOMAIN_QA = PASS
ACADEMIC_QA = PASS
CALCULATION_QA = PASS
CONSTRAINT_QA = PASS
ANSWER_LEAK_QA = PASS
DUPLICATE_QA = PASS
THAI_QA = PASS
LAYOUT_QA = PASS
PRINT_QA = PASS
PROMPT_QA = PASS
```

Critical blockers: wrong count, incorrect mathematics, forbidden crossing, malformed canonical data, answer leakage, or unreadable/cropped layout.

Weighted score target for dry-run release: >=95/100 AND zero critical blockers.