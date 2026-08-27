# Geometric Color-by-Code — Output Contract

Version: 1.7.0

## Required output blocks

ทุกงานต้องมีอย่างน้อย:

1. `NORMALIZED_WORKSHEET_SPEC`
2. `VERIFIED_CONTENT_BLUEPRINT`
3. `GEOMETRY_LAYOUT_BLUEPRINT`
4. `NATURAL_HARMONY_BLUEPRINT`
5. `TWIN_OUTPUT_RENDER_PLAN`
6. `RENDER_QUALITY_PLAN`
7. `FINAL_RENDER_PLAN_OR_PROMPT`

ถ้ามีไฟล์จริงค่อยเพิ่ม `ARTIFACTS`; ห้ามอ้างว่า artifact ถูกสร้างแล้วถ้ายังไม่มีจริง

## 1. NORMALIZED_WORKSHEET_SPEC

อย่างน้อย:

```text
GRADE_LEVEL
SUBJECT
TOPIC
QUESTION_COUNT
COLOR_COUNT
PRIMARY_SHAPE
TILING_MODE
THEME
COMPOSITION_SYSTEM
PAGE_SIZE
ORIENTATION
RENDER_MODE
STUDENT_WORKSHEET_REQUIRED
ANSWER_KEY
ANSWER_KEY_RENDER_MODE
```

## 2. VERIFIED_CONTENT_BLUEPRINT

ต่อ question:

```text
question_id
prompt_text
response_type
correct_answer
normalized_answer_code
category_id
color_id
question_region_id
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
```

Academic text/mapping ที่ verified แล้วห้ามถูก image model rewrite

## 3. GEOMETRY_LAYOUT_BLUEPRINT

ต้องระบุ:

```text
master_geometry_id
master_geometry_version
primary_shape
tiling_mode
shape_dominance_target
primary_shape_coverage_target
tile_scale_variation
micro_tile_count_target_or_range
question_region_count
question_region_mode
question_region_shape_grammar
min_colorable_cell_size
min_segment_length
micro_tile_density_policy
freeform_area_limit
freeform_detail_budget
theme_silhouette_mode
stroke_hierarchy
topology_rules
page_size
orientation
safe_margin
legend_position
question_placement
```

## 4. NATURAL_HARMONY_BLUEPRINT

เมื่อ active ต้องระบุ:

```text
composition_system
composition_balance
symmetry_mode
focal_point_placement
golden_section_guide
fibonacci_rhythm
phyllotaxis_mode
radial_symmetry
petal_count_logic
natural_scale_hierarchy
natural_pattern_strength
question_flow
question_distribution_balance
truthfulness_note
```

`truthfulness_note` ต้องแยก exact/calculated/approximate/inspired/not-used ให้ชัด

## 5. TWIN_OUTPUT_RENDER_PLAN

Production default:

```text
ONE MASTER GEOMETRY
ONE VERIFIED MAPPING
TWO RENDER VIEWS
```

ต้องระบุอย่างน้อย:

```text
student_output_id
answer_key_output_id
master_geometry_id
student_color_mode = MONOCHROME
student_region_fill = NONE
answer_key_geometry_source = STUDENT_MASTER_GEOMETRY
answer_key_text_source = VERIFIED_CONTENT_BLUEPRINT
answer_key_fill_source = VERIFIED_COLOR_MAPPING
answer_key_layout_match = EXACT
pair_topology_identity = REQUIRED
pair_text_identity = REQUIRED
pair_mapping_identity = REQUIRED
```

Student Sheet และ Answer Key ต้องใช้ region IDs และ geometry เดียวกัน 100%; Answer Key แตกต่างได้เฉพาะ fill color, label `เฉลย`, และ teacher-only annotation ที่ไม่เปลี่ยนกิจกรรม

## 6. RENDER_QUALITY_PLAN

อย่างน้อย:

```text
render_mode
production_final_render_mode
vector_rendering_required
deterministic_text_placement
deterministic_region_topology
deterministic_shared_edges
line_render_style
outer_frame_stroke
object_silhouette_stroke
internal_tile_stroke
thai_font_render_qa
print_line_clarity_qa
raster_preview_source
```

## 7. FINAL_RENDER_PLAN_OR_PROMPT

ต้องยืนยัน:
- exact question count
- exact mapping/legend
- primary shape = construction grammar
- natural harmony controls placement/scale/rhythm only
- main Student worksheet activity area is unfilled/monochrome
- Answer Key uses identical master geometry
- Answer Key fills every region deterministically from verified mapping
- no answer/color reinterpretation by image model
- no sliver cells / no starburst / clean stroke hierarchy
- deterministic Thai/text in final print
- final printable boundaries are deterministic/vector
- raster previews derive from vector master
- no overlap / print-safe

## Integrity rules

```text
WORKSHEET QUESTIONS
= ANSWER KEY QUESTIONS
= MAPPING SOURCE
= LEGEND SOURCE
```

และ:

```text
STUDENT REGION TOPOLOGY
= ANSWER KEY REGION TOPOLOGY
```

สำหรับทุก `region_id`:

```text
expected_color_id = verified_mapping[question_id]
answer_key.fill_color_id == expected_color_id
```

ไม่ตรงแม้ 1 region = Critical FAIL

## Production-final rule

Generative raster linework **ห้าม** เป็น production-final coloring boundary source และห้ามสร้าง Answer Key ใหม่จาก independent image generation.

อ่านร่วมกับ `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`.
