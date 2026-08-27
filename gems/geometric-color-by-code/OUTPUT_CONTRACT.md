# Geometric Color-by-Code — Output Contract

Version: 1.4.0

## Required output blocks

ทุกงานต้องมีอย่างน้อย:

1. `NORMALIZED_WORKSHEET_SPEC`
2. `VERIFIED_CONTENT_BLUEPRINT`
3. `GEOMETRY_LAYOUT_BLUEPRINT`
4. `RENDER_QUALITY_PLAN`
5. `FINAL_WORKSHEET_PROMPT_OR_RENDER_SPEC`

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
PAGE_SIZE
ORIENTATION
RENDER_MODE
ANSWER_KEY
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

## 4. RENDER_QUALITY_PLAN

อย่างน้อย:

```text
render_mode
vector_rendering_preferred
deterministic_text_placement
deterministic_region_topology
line_render_style
outer_frame_stroke
object_silhouette_stroke
internal_tile_stroke
thai_font_render_qa
print_line_clarity_qa
max_visual_regen_rounds
```

## 5. FINAL_WORKSHEET_PROMPT_OR_RENDER_SPEC

ต้องยืนยัน:
- exact question count
- exact mapping/legend
- primary shape = construction grammar
- theme = tile grouping
- no freeform major object when HIGH
- min colorable area protected
- no sliver cells
- no accidental starburst junction
- clean 3-level stroke hierarchy
- main art monochrome by default
- deterministic Thai/text when available
- no overlap / print-safe

## Integrity rule

```text
WORKSHEET QUESTIONS
= ANSWER KEY QUESTIONS
= MAPPING SOURCE
= LEGEND SOURCE
```

## Production-final rule

Raster/image candidate ที่เส้นแตก ฟุ้ง ซ้อน หรือขาด **ห้าม** ถูกระบุเป็น production-final

ถ้า deterministic/vector renderer มี ให้ prefer vector-first or hybrid finalization.
