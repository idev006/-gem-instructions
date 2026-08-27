# Geometric Color-by-Code — Output Contract

Version: 1.2.0

## Required output blocks

ทุกการสร้างงานต้องได้อย่างน้อย 4 บล็อกตามลำดับ:

1. `NORMALIZED_WORKSHEET_SPEC`
2. `VERIFIED_CONTENT_BLUEPRINT`
3. `GEOMETRY_LAYOUT_BLUEPRINT`
4. `FINAL_WORKSHEET_PROMPT`

ถ้าระบบสร้างไฟล์จริงได้ จึงค่อยมี `ARTIFACTS` เพิ่มภายหลัง ห้ามอ้างว่าไฟล์ถูกสร้างแล้วถ้ายังไม่ได้สร้างจริง

## 1. NORMALIZED_WORKSHEET_SPEC

ต้องระบุอย่างน้อย:

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
ANSWER_KEY
```

ถ้าเป็น category/focus activity ต้องเพิ่ม:

```text
CATEGORY_SET
FOCUS_CATEGORY
CATEGORY_FOCUS_MODE
FOCUS_SHARE_TARGET
LEGEND_COVERAGE_POLICY
PREFER_ATOMIC_RESPONSE
```

ถ้าเป็น numeric/multi-color activity ต้อง resolve:

```text
ANSWER_FREQUENCY_PLAN
COLOR_USAGE_TARGET
```

## 2. VERIFIED_CONTENT_BLUEPRINT

ต้องมี source-of-truth ต่อ question:

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

Aggregate block ต้องรองรับ:

```text
category_set
usage_count_per_category
usage_count_per_answer_or_code
usage_count_per_color
focus_category
resolved_focus_share
legend_entries
legend_usage_count_per_entry
legend_coverage_check
answer_frequency_check
```

ห้ามให้ final image prompt เปลี่ยน `prompt_text`, `correct_answer`, `normalized_answer_code`, `category_id`, `color_id`

Critical rules:
- ทุก student-facing legend entry ต้องมี usage count >= 1 โดย default
- focus distribution ต้องผ่าน validation ก่อน visual prompt assembly
- answer/color frequency plan ต้องถูก freeze ก่อน render เมื่อทำได้

## 3. GEOMETRY_LAYOUT_BLUEPRINT

ต้องระบุ:

```text
primary_shape
tiling_mode
tessellation_family
shape_dominance
primary_shape_coverage_target
tile_scale_variation
freeform_area_limit
freeform_major_objects
micro_tile_count_target_or_range
question_region_count
question_region_mode
question_region_shape_grammar
theme_silhouette_mode
theme_recognizability
visual_language_consistency
freeform_curve_policy
line_topology_rules
page_size
orientation
safe_margin
legend_position
question_placement
```

เมื่อ `SHAPE_DOMINANCE = HIGH` ให้ blueprint ระบุเป้าหมายเชิงโครงสร้าง เช่น:

```text
primary_shape_coverage_target = approximately >= 85% structural tiling rhythm
freeform_area_limit = approximately <= 15–20% structural area
freeform_major_objects = prohibited
question_region_shape_grammar = primary-shape group
```

ค่าดังกล่าวเป็น design target เพื่อ audit ไม่ใช่ข้ออ้างให้ลด readability

### Topology rules required

```text
NO accidental double lines
NO broken joins
NO ambiguous shared borders
NO unintended open regions
NO unusable sliver cells
NO border/text collisions
```

## 4. FINAL_WORKSHEET_PROMPT

Prompt ต้องประกาศชัดว่า:
- primary shape เป็น construction grammar
- theme ถูกสร้างจากการจัดกลุ่ม tiles
- ห้ามสร้าง freeform scene ก่อนแล้ว overlay shape pattern
- question regions ต้อง derive จาก primary-shape grouping
- tile-scale variation ต้องอยู่ใน visual language เดียวกัน
- exact question count มาจาก verified blueprint
- exact legend entries มาจาก verified mapping
- no orphan legend category/color
- focus category ต้องคง distribution ที่ verified แล้ว
- answer/color frequency plan ต้องคงตาม verified blueprint
- main worksheet monochrome
- legend preview color ได้เมื่อเปิดใช้งาน
- no double lines / broken joins / sliver cells
- no-overlap
- print-safe
- ห้าม image model แต่งโจทย์ คำตอบ หมวด หรือรหัสสีใหม่

## Integrity rule

```text
WORKSHEET QUESTIONS
= ANSWER KEY QUESTIONS
= CATEGORY/ANSWER DISTRIBUTION SOURCE
= LEGEND/MAPPING SOURCE
```

ข้อมูลทั้งหมดต้องมาจาก data source เดียวกัน
