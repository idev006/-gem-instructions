# Geometric Color-by-Code — Output Contract

Version: 1.8.1

## Required output blocks

ทุกงานต้องมีอย่างน้อย:

1. `NORMALIZED_WORKSHEET_SPEC`
2. `ANSWER_CODE_COLOR_PLAN`
3. `VERIFIED_CONTENT_BLUEPRINT`
4. `GEOMETRY_LAYOUT_BLUEPRINT`
5. `NATURAL_HARMONY_BLUEPRINT`
6. `CONTENT_RENDER_PLAN`
7. `OUTPUT_RENDER_PLAN`
8. `RENDER_QUALITY_PLAN`
9. `FINAL_QA_REPORT`

ถ้ามีไฟล์จริงค่อยเพิ่ม `ARTIFACTS`; ห้ามอ้างว่า artifact ถูกสร้างแล้วถ้ายังไม่มีจริง.

## 1. NORMALIZED_WORKSHEET_SPEC

อย่างน้อย:

```text
GRADE_LEVEL
SUBJECT
TOPIC
QUESTION_COUNT
COLOR_COUNT
CONTENT_GENERATION_MODE
PRIMARY_SHAPE
TILING_MODE
THEME
PAGE_SIZE
ORIENTATION
STUDENT_WORKSHEET_REQUIRED
ANSWER_KEY
```

## 2. ANSWER_CODE_COLOR_PLAN

ต้องเกิดก่อน generated questions:

```text
content_generation_mode = ANSWER_FIRST
active_answer_or_code_set
active_legend_domain
legend_entries
usage_count_per_color
target_answer_or_code_per_question_or_region
coverage_check
usage_sum_check
mapping_freeze_status
```

Required invariants:

```text
sum(usage_count_per_color) == QUESTION_COUNT
all target answers/codes belong to active legend
all displayed legend entries have usage >= 1 by default
```

## 3. VERIFIED_CONTENT_BLUEPRINT

ต่อ question:

```text
question_id
region_id
target_answer_or_code
prompt_text
response_type
verified_correct_answer
normalized_answer_code
category_id
color_id
legend_entry_id
validation_status
```

Required:

```text
target_answer_or_code == normalized_answer_code
color_id == active_legend[normalized_answer_code]
validation_status == PASS
```

Aggregate:

```text
usage_count_per_color
legend_coverage_check
answer_frequency_check
out_of_legend_answer_count = 0
expected_question_ids
```

Academic text/mapping ที่ verified แล้วห้ามถูก image model rewrite.

## 4. GEOMETRY_LAYOUT_BLUEPRINT

ต้องระบุ master geometry, primary shape, tiling, shape dominance, region grammar, minimum colorable area, stroke hierarchy, topology rules, page size/orientation, safe margins, legend position และ question placement.

## 5. NATURAL_HARMONY_BLUEPRINT

เมื่อ active ต้องระบุ composition system, balance, symmetry, focal hierarchy, golden-section/Fibonacci/phyllotaxis usage, natural scale hierarchy, question flow และ truthfulness note.

## 6. CONTENT_RENDER_PLAN

Production/test-conformance output ต้องระบุ:

```text
artwork_render_source = IMAGE_MODEL_OR_VECTOR_AS_AVAILABLE
academic_text_render_mode = DETERMINISTIC_OVERLAY
academic_text_render_source = VERIFIED_CONTENT_BLUEPRINT
question_number_render_source = VERIFIED_CONTENT_BLUEPRINT
legend_render_source = VERIFIED_MAPPING
color_swatch_render_source = VERIFIED_PALETTE
post_render_content_parity = REQUIRED
```

Hard rules:
- image model may assist artwork/composition
- image model may not invent/rewrite final questions, question numbers, legend answer values, or academic labels
- image-model-only full-page text rendering is concept preview only, not Gem-conformance proof

## 7. OUTPUT_RENDER_PLAN

Student default:

```text
student_color_mode = MONOCHROME
student_region_fill = NONE
mapping_source = VERIFIED_MAPPING
```

เมื่อ `ANSWER_KEY = YES`:

```text
ONE MASTER GEOMETRY
ONE VERIFIED MAPPING
TWO RENDER VIEWS
answer_key_geometry_source = STUDENT_MASTER_GEOMETRY
answer_key_text_source = VERIFIED_CONTENT_BLUEPRINT
answer_key_fill_source = VERIFIED_COLOR_MAPPING
answer_key_layout_match = EXACT
```

เมื่อ `ANSWER_KEY = NO` ให้ suppress answer-key output เท่านั้น; hidden verified answers/mapping ยังต้องใช้สำหรับ QA.

## 8. RENDER_QUALITY_PLAN

อย่างน้อย:

```text
production_final_render_mode = VECTOR_FIRST_REQUIRED
vector_rendering_required = YES_FOR_FINAL_PRINT
deterministic_region_topology = YES
deterministic_shared_edges = YES
line_render_style = CLEAN_VECTOR
thai_font_render_qa = CRITICAL
print_line_clarity_qa = CRITICAL
raster_preview_source = VERIFIED_COMPOSITE
```

## 9. FINAL_QA_REPORT

ต้องยืนยันอย่างน้อย:

```text
requested_question_count
rendered_question_count
expected_question_ids
rendered_question_ids
question_id_uniqueness
question_id_sequence_check
prompt_text_parity_check
active_legend_domain
rendered_legend_domain
legend_parity_check
out_of_legend_answer_count
mapping_coverage_check
post_render_content_parity_status
print_qa_status
```

Required parity:

```text
rendered_question_count == QUESTION_COUNT
rendered_question_ids == expected_question_ids
rendered_prompt_text[id] == verified_prompt_text[id]
rendered_legend_domain == active_legend_domain
out_of_legend_answer_count == 0
post_render_content_parity_status == PASS
```

## Integrity rules

```text
TARGET ANSWER/CODE PLAN
= VERIFIED QUESTION ANSWERS
= MAPPING SOURCE
= LEGEND SOURCE
= REGION COLOR SOURCE
```

และ:

```text
VERIFIED CONTENT BLUEPRINT
= VISIBLE ACADEMIC CONTENT IN FINAL OUTPUT
```

Critical FAIL เมื่อไม่ตรงแม้ 1 ข้อ.

## Production-final rule

Generative raster linework **ห้าม** เป็น production-final coloring boundary source และ generative image model **ห้าม** เป็น final academic-text renderer.

อ่านร่วมกับ:
- `policies/ANSWER_FIRST_GENERATION_POLICY.md`
- `policies/COLOR_MAPPING_POLICY.md`
- `policies/DETERMINISTIC_CONTENT_RENDER_POLICY.md`
- `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`
