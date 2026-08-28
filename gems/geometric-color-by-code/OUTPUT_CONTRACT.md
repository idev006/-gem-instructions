# Geometric Color-by-Code — Output Contract

Version: 1.8.0

## Required output blocks

ทุกงานต้องมีอย่างน้อย:

1. `NORMALIZED_WORKSHEET_SPEC`
2. `ANSWER_CODE_COLOR_PLAN`
3. `VERIFIED_CONTENT_BLUEPRINT`
4. `GEOMETRY_LAYOUT_BLUEPRINT`
5. `NATURAL_HARMONY_BLUEPRINT`
6. `OUTPUT_RENDER_PLAN`
7. `RENDER_QUALITY_PLAN`
8. `FINAL_RENDER_PLAN_OR_PROMPT`

ถ้ามีไฟล์จริงค่อยเพิ่ม `ARTIFACTS`; ห้ามอ้างว่า artifact ถูกสร้างแล้วถ้ายังไม่มีจริง

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
COMPOSITION_SYSTEM
PAGE_SIZE
ORIENTATION
RENDER_MODE
STUDENT_WORKSHEET_REQUIRED
ANSWER_KEY
```

## 2. ANSWER_CODE_COLOR_PLAN

ต้องเกิดก่อน generated questions และต้องระบุ:

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
usage_count_per_answer_or_category
usage_count_per_color
focus_category
resolved_focus_share
legend_entries
legend_usage_count
legend_coverage_check
answer_frequency_check
out_of_legend_answer_count = 0
```

Academic text/mapping ที่ verified แล้วห้ามถูก image model rewrite.

## 4. GEOMETRY_LAYOUT_BLUEPRINT

ต้องระบุ master geometry, primary shape, tiling, shape dominance, region grammar, minimum colorable area, stroke hierarchy, topology rules, page size/orientation, safe margins, legend position และ question placement.

## 5. NATURAL_HARMONY_BLUEPRINT

เมื่อ active ต้องระบุ composition system, balance, symmetry, focal hierarchy, golden-section/Fibonacci/phyllotaxis usage, natural scale hierarchy, question flow และ truthfulness note.

## 6. OUTPUT_RENDER_PLAN

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

## 7. RENDER_QUALITY_PLAN

อย่างน้อย:

```text
render_mode
production_final_render_mode
vector_rendering_required
deterministic_text_placement
deterministic_region_topology
deterministic_shared_edges
line_render_style
thai_font_render_qa
print_line_clarity_qa
raster_preview_source
```

## 8. FINAL_RENDER_PLAN_OR_PROMPT

ต้องยืนยัน:
- exact question count
- active answer/code set resolved before question generation
- exact mapping/legend
- no answer/code outside active legend
- all regions have a color mapping
- color usage counts reconcile to question count
- math/topic constraints validated
- primary shape = construction grammar
- main Student worksheet activity area is unfilled/monochrome
- Answer Key behavior follows user instruction
- no sliver cells / no starburst / clean stroke hierarchy
- deterministic Thai/text in final print
- final printable boundaries are deterministic/vector
- raster previews derive from vector master

## Integrity rules

```text
TARGET ANSWER/CODE PLAN
= VERIFIED QUESTION ANSWERS
= MAPPING SOURCE
= LEGEND SOURCE
= REGION COLOR SOURCE
```

Critical invariant:

```text
FOR EACH question/region:
  normalized_answer_code IN active_legend
  color_id = active_legend[normalized_answer_code]
```

Out-of-legend answer count must be zero. ไม่ตรงแม้ 1 ข้อ = Critical FAIL และห้าม render final.

## Production-final rule

Generative raster linework **ห้าม** เป็น production-final coloring boundary source และ image model ห้าม invent/rewrite academic questions after mapping freeze.

อ่านร่วมกับ:
- `policies/ANSWER_FIRST_GENERATION_POLICY.md`
- `policies/COLOR_MAPPING_POLICY.md`
- `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`
