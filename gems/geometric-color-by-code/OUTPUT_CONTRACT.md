# Geometric Color-by-Code — Output Contract

Version: 1.6.0

## Required output blocks

ทุกงานต้องมีอย่างน้อย:

1. `NORMALIZED_WORKSHEET_SPEC`
2. `VERIFIED_CONTENT_BLUEPRINT`
3. `GEOMETRY_LAYOUT_BLUEPRINT`
4. `NATURAL_HARMONY_BLUEPRINT`
5. `RENDER_QUALITY_PLAN`
6. `FINAL_RENDER_PLAN_OR_PROMPT`

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

## 4. NATURAL_HARMONY_BLUEPRINT

ต้องระบุเมื่อ `COMPOSITION_SYSTEM` resolve เป็น NATURAL_HARMONY หรือ AUTO เลือกใช้ natural composition:

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

`truthfulness_note` ต้องแยกให้ชัดว่า exact, calculated, approximate, inspired หรือ not-used; ห้ามเรียก exact golden ratio/Fibonacci/golden-angle หากไม่ได้คำนวณและตรวจจริง

## 5. RENDER_QUALITY_PLAN

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

## 6. FINAL_RENDER_PLAN_OR_PROMPT

ต้องยืนยัน:
- exact question count
- exact mapping/legend
- primary shape = construction grammar
- natural harmony controls placement/scale/rhythm only
- theme = tile grouping
- no freeform major object when HIGH
- min colorable area protected
- no sliver cells
- no accidental starburst junction
- clean 3-level stroke hierarchy
- question flow supports visual rhythm when active
- main art monochrome by default
- deterministic Thai/text in final print
- final printable boundaries are deterministic/vector
- raster preview derives from vector master when production output is claimed
- no overlap / print-safe

## Integrity rule

```text
WORKSHEET QUESTIONS
= ANSWER KEY QUESTIONS
= MAPPING SOURCE
= LEGEND SOURCE
```

Natural composition may move regions, but may not mutate verified questions, answers, codes or colors.

## Production-final rule

Generative raster linework **ห้าม** เป็น production-final coloring boundary source.

If image-model output is used, it is concept/mockup input and must be reconstructed/finalized through the deterministic/vector pipeline before promotion to production final or Golden Reference.
