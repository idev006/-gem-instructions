# Geometric Color-by-Code — Output Contract

Version: 1.0.0

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

## 2. VERIFIED_CONTENT_BLUEPRINT

ต้องมี source-of-truth ต่อ question:

```text
question_id
prompt_text
response_type
correct_answer
normalized_answer_code
color_id
question_region_id
```

ห้ามให้ final image prompt เปลี่ยน `prompt_text`, `correct_answer`, `normalized_answer_code`, `color_id`

## 3. GEOMETRY_LAYOUT_BLUEPRINT

ต้องระบุ:

```text
primary_shape
tiling_mode
tessellation_family
shape_dominance
micro_tile_count_target_or_range
question_region_count
question_region_mode
theme_silhouette_mode
theme_recognizability
freeform_curve_policy
page_size
orientation
safe_margin
legend_position
question_placement
```

## 4. FINAL_WORKSHEET_PROMPT

Prompt ต้องประกาศชัดว่า:
- primary shape เป็น construction grammar
- theme ถูกสร้างจากการจัดกลุ่ม tiles
- ห้ามสร้าง freeform scene ก่อนแล้ว overlay shape pattern
- exact question count มาจาก verified blueprint
- main worksheet monochrome
- legend preview color ได้เมื่อเปิดใช้งาน
- no-overlap
- print-safe
- ห้าม image model แต่งโจทย์ คำตอบ หรือรหัสสีใหม่

## Integrity rule

```text
WORKSHEET QUESTIONS
= ANSWER KEY QUESTIONS
= MAPPING SOURCE
```

ข้อมูลทั้งหมดต้องมาจาก data source เดียวกัน
