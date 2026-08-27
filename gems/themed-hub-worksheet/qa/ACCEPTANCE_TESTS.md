# Themed Hub Worksheet — Acceptance Tests

Version: 1.1.0

## Critical gates

1. Default page is A4 Portrait when not specified.
2. Default slot count is 8 when not specified.
3. Subject/topic/grade remain academically correct after theme/object adaptation.
4. Main artwork is monochrome by default.
5. Thai visible text passes spelling, vowel/tone-mark, spacing, terminology, meaning, and age-appropriateness checks.
6. Slot count equals requested/resolved `SLOT_COUNT` per page plan.
7. Center content does not overlap answer slots.
8. Slots are large enough for real student writing.
9. Decorations do not overlap academic text or answer areas.
10. Selected object/theme does not distort the intended learning objective.
11. Open-ended topics are converted to short-answer-compatible subtasks when appropriate.
12. Final prompt explicitly states page size, orientation, subject, grade, topic, learning objective, instruction, slot count, object/theme, layout, monochrome rules, safe margins, writing-space priority, and no-overlap constraints.
13. A Verified Content Blueprint exists before final prompt assembly.
14. Important academic text is not delegated to the image model to invent or rewrite.
15. If `ANSWER_KEY = YES`, answer key data comes from the same verified blueprint.
16. Gem never claims a PDF/PNG/DOCX exists unless one was actually created.

## Parameter semantics tests

- `RESPONSE_TYPE=AUTO` resolves to a valid explicit response type.
- `SLOT_LABEL_MODE` resolves to BLANK, PROMPT, NUMBERED, or BLANK_OR_PROMPT.
- `CENTER_CONTENT_MODE` resolves to a supported mode.
- `GRADE_LEVEL` overrides difficulty when difficulty would exceed grade appropriateness.

## Pagination tests

### 8 slots on A4 Portrait
Expected: one page when content length is normal.

### 16 short-answer slots
Expected: one page only if writing usability remains acceptable; otherwise paginate.

### 24 slots on A4 Portrait
Expected: multiple pages. FAIL if slots are squeezed to unusable size.

## Revision preservation tests

Given an existing resolved specification:

```text
ป.1 ภาษาไทย สระอา 8 ช่อง พิซซ่า A4 แนวตั้ง
```

Follow-up:
```text
เปลี่ยนเป็นดอกไม้
```

PASS only if grade, subject, topic, slot count, page size, and orientation remain unchanged.

Follow-up:
```text
เพิ่มเป็น 10 ช่อง
```

PASS only if only slot-related layout is recalculated while unrelated parameters remain unchanged.

## Long-text handling

Input requests long paragraph responses inside 8 radial slots.

PASS when Gem either:
- converts to a valid short-response activity without changing the learning intent, or
- changes layout/pagination to provide sufficient writing space.

FAIL when Gem only shrinks text/slots until unreadable.

## Object/theme mismatch

Input:
```text
วิทยาศาสตร์ ระบบสุริยะ 8 ช่อง ใช้พิซซ่า
```

PASS when pizza remains only a visual container and scientific facts stay unchanged.
FAIL if academic content is altered to fit the food theme.

## AUTO resolution

When object/theme/layout are omitted:
- resolve without unnecessary clarification
- choose an age-appropriate and layout-compatible option
- do not invent academic content

## Multi-subject regression set

- Thai: ป.1 สระอา, 8 slots, pizza
- Thai: ป.3 มาตราตัวสะกด, 10 slots, flower
- Thai: ป.4 ควบกล้ำ, 8 slots, wheel
- Math: ป.2 แม่ 4, 12 slots, wheel
- Math: ป.3 number bonds 20, 8 slots, sun
- English: Animals vocabulary, 10 slots, zoo
- English: -at word family, 8 slots, flower
- Science: plant parts, 6 slots, flower
- Science: solar system, 8 slots, orbit
- Social studies: continents, 7 slots, world-map theme

## Visual regression

PASS when:
- simple line art
- white background
- clean outline
- low ink
- child-friendly
- coloring-friendly
- no dense shading
- no clutter
- no text collisions
- no tiny unusable slots
- safe margin approximately 10–12 mm by default

## Prompt integrity regression

FAIL if final prompt contains instructions such as:
- invent suitable Thai words yourself
- add any facts you think are correct
- choose random educational answers

PASS when important text/content is supplied from the verified blueprint or explicitly constrained.
