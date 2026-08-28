# Render Content Fidelity Remediation Report

Date: 2026-08-28
Gem: `geometric-color-by-code`
Resulting version: 1.8.1

## Trigger

หลังปรับ Gem เป็น v1.8.0 แบบ Answer-First ได้ทดสอบเคส:
- ป.3 คณิตศาสตร์
- การหารลงตัว ตัวตั้ง 2 หลัก ÷ ตัวหาร 1 หลัก
- 40–50 ข้อ
- ธีมยานอวกาศ
- A4 Portrait
- Student only

ภาพที่สร้างสวยและโดยรวมเข้าใจง่าย แต่ inspection พบว่า **rendered academic content ยังสามารถ drift จาก verified plan ได้เมื่อ image model เป็นผู้วาดโจทย์/หมายเลข/legend เอง**.

ตัวอย่างความเสี่ยงที่สังเกตได้:
- สมการบางข้ออาจให้ผลลัพธ์นอก active legend แม้ blueprint ตั้งใจจำกัด domain
- หมายเลขข้อสามารถซ้ำ/หาย/ไม่เรียง
- จำนวนข้อ visible อาจไม่ตรง request
- legend สามารถเปลี่ยนค่าหรือ label ระหว่าง image generation

## Root cause

v1.8.0 แก้ **generation-time mapping integrity** แล้ว แต่ execution path ยังสามารถใช้:

```text
verified blueprint
→ full-page image generation including academic text
```

จึงยังมี stochastic text/content generation หลัง mapping freeze.

สรุป root cause:

```text
PRE-RENDER CORRECTNESS != VISIBLE OUTPUT CORRECTNESS
```

เมื่อ final academic text ยังถูกวาดโดย generative image model.

## Corrective design

แยก rendering เป็น 2 responsibilities:

```text
ARTWORK/THEME LAYER
= image model allowed

ACADEMIC CONTENT + QUESTION IDS + LEGEND
= deterministic/vector renderer only
```

Canonical pipeline ใหม่:

```text
Verified Content + Mapping
→ Master Geometry
→ Artwork Layer
→ Deterministic Academic Overlay
→ Deterministic Legend Overlay
→ Final Composite
→ Post-Render Content Parity QA
```

## Development changes

1. Added `policies/DETERMINISTIC_CONTENT_RENDER_POLICY.md`.
2. Promoted canonical Gem to v1.8.1.
3. Added `ACADEMIC_TEXT_RENDER_MODE = DETERMINISTIC_OVERLAY`.
4. Added explicit render sources for academic text, question IDs, legend and color swatches.
5. Added `POST_RENDER_CONTENT_PARITY = REQUIRED`.
6. Added visible-output invariants for exact question count, unique/complete question IDs, prompt-text parity and legend parity.
7. Updated Output Contract, User Guide, README, Acceptance Tests and Regression Tests.
8. Defined image-model-only academic-text pages as concept previews, not production/test-conformance proof.

## Closure criteria

A future production/test-conformance run passes only when:

```text
rendered_question_count == QUESTION_COUNT
rendered_question_ids == expected_question_ids
rendered_prompt_text[id] == verified_prompt_text[id]
rendered_legend_domain == active_legend_domain
out_of_legend_answer_count == 0
post_render_content_parity == PASS
```

Additionally:
- exact division constraints pass
- mapping is frozen before render
- image model does not create final academic content
- vector/deterministic geometry and print QA pass

## Status

Root cause documented: PASS
Policy added: PASS
Canonical instruction updated: PASS
Output contract updated: PASS
Acceptance/regression coverage added: PASS

Next validation target: rerun a 40–50 item A4 stress case using deterministic academic overlay rather than image-model-rendered questions.
