# Twin Output & Answer-Key Integrity Policy

Version: 1.1.0
Status: Production policy

## Purpose

กำหนดให้ Color-by-Code production output แยกเป็น 2 ชุดที่มาจาก source เดียวกัน แต่ **ต้องไม่วาง Student Worksheet และ Answer Key อยู่บนหน้าเดียวกันหรือใน canvas เดียวกันโดย default**:

1. `STUDENT_WORKSHEET` — ขาว-ดำ ยังไม่เติมสีในพื้นที่กิจกรรม
2. `COLORED_ANSWER_KEY` — layout/region เดียวกัน เติมสีตาม verified mapping เท่านั้น

เป้าหมายคือป้องกันทั้ง mapping drift และปัญหาการใช้งานจริงที่เฉลยปรากฏพร้อมโจทย์ให้นักเรียนเห็น

## Hard principles

```text
ONE MASTER GEOMETRY
ONE VERIFIED MAPPING
TWO RENDER VIEWS
SEPARATE OUTPUT SURFACES
```

ห้ามสร้าง Student Sheet และ Answer Key ด้วย geometry/composition คนละชุด และห้ามจัดสองชุดไว้ side-by-side บนหน้าเดียวกันโดย default.

## Canonical pipeline

```text
Verified Content Blueprint
→ Verified Answer/Code/Color Mapping
→ Deterministic Master Region Graph
→ Deterministic Master Text Layout
→ STUDENT_WORKSHEET render view
→ COLORED_ANSWER_KEY render view
→ Separate-page / separate-file packaging
→ Pair Integrity QA
```

## Student Worksheet

Default:

```text
STUDENT_WORKSHEET_COLOR_MODE = MONOCHROME
STUDENT_REGION_FILL = NONE
SHOW_REGION_CODES = YES_WHEN_ACTIVITY_REQUIRES
SHOW_COLOR_LEGEND = YES
LEGEND_COLOR_PREVIEW = YES
```

สีจริงใน legend เป็น controlled exception; พื้นที่ที่นักเรียนต้องระบายต้องยังไม่ถูกเติมสี

## Colored Answer Key

Default:

```text
ANSWER_KEY_REQUIRED = YES
ANSWER_KEY_RENDER_MODE = COLORED_SOLUTION
ANSWER_KEY_GEOMETRY_SOURCE = STUDENT_MASTER_GEOMETRY
ANSWER_KEY_TEXT_SOURCE = VERIFIED_CONTENT_BLUEPRINT
ANSWER_KEY_FILL_SOURCE = VERIFIED_COLOR_MAPPING
ANSWER_KEY_LAYOUT_MATCH = EXACT
ANSWER_KEY_PRESENTATION = SEPARATE_PAGE_OR_FILE
```

แต่ละ region ต้องเติมสีด้วย deterministic rule:

```text
region_id
→ mapped question/code
→ color_id
→ canonical fill value
```

ห้าม image model เลือกสีโดยตีความโจทย์เอง

## Presentation / packaging rule

Default:

```text
PAIR_PRESENTATION_MODE = SEPARATE
STUDENT_AND_ANSWER_ON_SAME_PAGE = NO
STUDENT_AND_ANSWER_SIDE_BY_SIDE = NO
ANSWER_KEY_AFTER_STUDENT = YES_WHEN_PACKAGED_AS_MULTI_PAGE_DOCUMENT
```

รูปแบบที่ยอมรับ:
- Student worksheet เป็นไฟล์/หน้าแยก และ Answer Key เป็นไฟล์/หน้าแยก
- PDF เดียวหลายหน้าได้ โดย Student มาก่อน และ Answer Key อยู่หน้าถัดไปหรือส่วนท้าย
- Batch หลายหน้าได้ แต่ทุก answer-key page ต้องแยกจาก student page ที่สอดคล้องกัน

รูปแบบที่ไม่ยอมรับโดย default:
- Student ซ้าย + Answer Key ขวาในหน้าเดียว
- Student ด้านบน + Answer Key ด้านล่างในหน้าเดียว
- thumbnail เฉลยอยู่ใน Student worksheet

ข้อยกเว้นมีได้เฉพาะผู้ใช้สั่งชัดเจนว่าให้ทำ comparison/proof sheet สำหรับครูหรือ QA และต้องไม่เรียก output นั้นว่า student-facing worksheet.

## Pair identity requirements

Student และ Answer Key ต้องตรงกันใน:
- page size/orientation
- region IDs
- region boundaries/topology
- question IDs
- prompt text
- legend mapping
- title/topic metadata เว้นแต่ Answer Key เพิ่มคำว่า `เฉลย`

อนุญาตความต่างเฉพาะ:
- fill colors
- Answer-Key label/badge
- optional teacher-only annotations

## Mapping QA

Critical checks:

```text
FOR EACH region_id:
  worksheet.region_id == key.region_id
  worksheet.question_id == key.question_id
  expected_color_id = verified_mapping[question_id]
  key.fill_color_id == expected_color_id
```

ถ้าข้อใดไม่ตรง = Critical FAIL

## Render policy

Production preferred:

```text
MASTER = deterministic SVG/vector/region graph
Student = render(master, fill=none)
Answer = render(master, fill=mapping[color_id])
Package = separate(student, answer)
```

ห้ามสร้าง Answer Key ด้วย generative image call ใหม่จากศูนย์ เพราะอาจเปลี่ยน geometry, text, หรือ color assignment

## Line-quality rule

Student และ Answer Key ต้องใช้ line master เดียวกัน เพื่อให้:
- เส้นคมเท่ากัน
- shared edges ไม่เปลี่ยน
- ไม่มีเส้นแตกเพิ่มเฉพาะฝั่งเฉลย
- raster preview ทั้งสองชุดมาจาก vector/deterministic master เดียวกัน

## Critical FAIL cases

FAIL เมื่อ:
- student worksheet ถูกเติมสีใน main activity area โดยไม่ได้ขอ
- answer key มี region สีผิด mapping แม้เพียง 1 region
- answer key regenerate geometry ใหม่
- question/region IDs ระหว่างสองชุดไม่ตรง
- legend ของสองชุดไม่ตรงกัน
- answer key ใช้ image model ตีความคำตอบ/สีใหม่
- line topology ต่างกันระหว่าง student และ answer key
- Student และ Answer Key ถูกวางอยู่หน้าเดียวกันโดย default
- Answer Key ปรากฏเป็นส่วนหนึ่งของ student-facing worksheet โดยไม่ได้รับคำสั่งชัดเจน

## Output naming

แนะนำ:

```text
<worksheet_id>_student
<worksheet_id>_answer_key
```

ถ้ามีหลายหน้า:

```text
<worksheet_id>_student_p01
<worksheet_id>_answer_key_p01
```

## Priority

```text
MAPPING ACCURACY
> PAIR TOPOLOGY IDENTITY
> STUDENT/ANSWER SEPARATION
> TEXT IDENTITY
> LINE QUALITY
> COLOR FIDELITY
> DECORATION
```
