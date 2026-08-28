# Deterministic Content Render Policy

Version: 1.0.0
Status: Production policy

## Purpose

ป้องกันปัญหา **render-time academic drift** ซึ่งเกิดเมื่อ verified question/mapping ถูกต้องก่อน render แต่ image model สร้างหรือแก้ข้อความ ตัวเลข สมการ ลำดับข้อ หรือ legend ใหม่เองระหว่างสร้างภาพ ทำให้ output ที่มองเห็นจริงไม่ตรงกับ SSOT.

## Root cause

แม้ระบบจะใช้ Answer-First และ freeze mapping แล้ว การส่ง academic text ทั้งหมดให้ image model วาดเป็นส่วนหนึ่งของภาพยังเปิดโอกาสให้เกิด:
- สมการเปลี่ยนค่า
- คำตอบหลุด active legend
- หมายเลขข้อซ้ำ/หาย/ไม่เรียง
- จำนวนข้อที่เห็นจริงไม่ตรง `QUESTION_COUNT`
- legend value/label เปลี่ยน
- Thai text เพี้ยน

ดังนั้น **pre-render correctness อย่างเดียวไม่พอ**; production/test-conformance output ต้องควบคุม visible academic text ด้วย deterministic layer.

## Hard principle

```text
VERIFIED CONTENT IS DATA, NOT GENERATIVE ART.
IMAGE MODEL MAY DESIGN ARTWORK/COMPOSITION.
DETERMINISTIC RENDERER MUST PLACE ACADEMIC TEXT + LEGEND.
```

## Canonical render split

```text
VERIFIED_CONTENT_BLUEPRINT
+ VERIFIED_MAPPING
+ DETERMINISTIC_REGION_GEOMETRY
        ↓
ARTWORK / THEME LAYER
  image model allowed for concept/background only
        +
ACADEMIC CONTENT OVERLAY
  deterministic/vector only
        +
LEGEND OVERLAY
  deterministic/vector only
        ↓
FINAL COMPOSITE
        ↓
POST-RENDER PARITY QA
```

## Image-model role

Allowed:
- theme exploration
- decorative artwork
- composition suggestions
- blank region silhouettes
- non-academic icons/ornaments

Prohibited for production/test-conformance visible academic data:
- inventing question text
- drawing final arithmetic expressions from memory
- choosing or rewriting question numbers
- writing final answer-code values
- writing final legend answer values
- remapping colors
- deciding region/question IDs

If an image-model-only preview contains academic text, it must be labeled **concept preview / non-conformance render** and must not be used to claim Gem correctness.

## Deterministic content sources

```text
ACADEMIC_TEXT_RENDER_SOURCE = VERIFIED_CONTENT_BLUEPRINT
QUESTION_NUMBER_RENDER_SOURCE = VERIFIED_CONTENT_BLUEPRINT
LEGEND_RENDER_SOURCE = VERIFIED_MAPPING
COLOR_SWATCH_RENDER_SOURCE = VERIFIED_PALETTE
REGION_ID_RENDER_SOURCE = MASTER_REGION_GRAPH
```

## Required visible parity

For every final Student page:

```text
rendered_question_count == QUESTION_COUNT
rendered_question_ids == expected_question_ids
rendered_question_ids are unique
rendered_question_ids are contiguous/sequential when numbering is required
rendered_prompt_text[question_id] == verified_prompt_text[question_id]
rendered_legend_domain == active_legend_domain
```

For Color-by-Code:

```text
FOR EACH rendered question:
  verified_answer = recompute_or_lookup(question_id)
  verified_answer IN active_legend_domain
  color_id = verified_mapping[verified_answer]
```

## Post-render parity QA

Production/test-conformance output must run a parity check against source data before PASS.

Preferred verification method:
1. compare renderer input records to renderer output objects directly
2. verify vector/text objects by IDs/metadata
3. verify raster export is derived from the already-verified vector composite

Do not rely on OCR as the primary correctness mechanism when deterministic object metadata is available.

## High-density 40–50 item rule

For 40–50 items on one A4 page:
- never delegate text placement to the image model to save space
- deterministic layout must preserve unique question IDs and exact text
- if all records cannot fit legibly, reduce decoration/micro-detail or paginate
- a visually beautiful page with missing/duplicated/changed questions is FAIL

## Critical FAIL cases

FAIL immediately when:
- any visible problem differs from the verified blueprint
- any visible answer result is outside the active legend
- any question number is missing, duplicated, or unexpectedly changed
- rendered question count differs from `QUESTION_COUNT`
- rendered legend differs from `VERIFIED_MAPPING`
- image model creates final academic text in a production/test-conformance render
- post-render parity was skipped but output is claimed production-ready or Gem-conformant

## Priority

```text
VISIBLE ACADEMIC FIDELITY
> ANSWER-FIRST MAPPING INTEGRITY
> QUESTION-ID INTEGRITY
> LEGEND PARITY
> READABILITY
> ARTWORK BEAUTY
```
