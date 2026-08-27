# Twin Output & Answer-Key Integrity Policy

Version: 1.2.0
Status: Production policy

## Purpose

กำหนดให้ Color-by-Code production output แยกเป็น 2 ชุดที่มาจาก source เดียวกัน และ **ต้องไม่วาง Student Worksheet และ Answer Key อยู่บนหน้าเดียวกันหรือใน canvas เดียวกันโดย default**:

1. `STUDENT_WORKSHEET` — ขาว-ดำ ยังไม่เติมสีในพื้นที่กิจกรรม
2. `COLORED_ANSWER_KEY` — layout/region เดียวกัน เติมสีตาม verified mapping เท่านั้น

Production default ที่อนุมัติแล้วคือ:

```text
PAGE 1 = STUDENT_WORKSHEET = A4 PORTRAIT
PAGE 2 = COLORED_ANSWER_KEY = A4 PORTRAIT
```

เป้าหมายคือป้องกันทั้ง mapping drift ปัญหาการใช้งานจริงที่เฉลยปรากฏพร้อมโจทย์ และการเสียพื้นที่ A4 เพราะนำสองหน้ามารวมไว้ใน canvas เดียวกัน

## Hard principles

```text
ONE MASTER GEOMETRY
ONE VERIFIED MAPPING
TWO RENDER VIEWS
TWO SEPARATE A4 PORTRAIT PAGES
```

ห้ามสร้าง Student Sheet และ Answer Key ด้วย geometry/composition คนละชุด และห้ามจัดสองชุดไว้ side-by-side / top-bottom บนหน้าเดียวกันโดย default.

## Canonical pipeline

```text
Verified Content Blueprint
→ Verified Answer/Code/Color Mapping
→ Deterministic Master Region Graph
→ Deterministic Master Text Layout
→ STUDENT_WORKSHEET A4 Portrait render
→ COLORED_ANSWER_KEY A4 Portrait render
→ Separate-page / separate-file packaging
→ Pair Integrity QA
```

## Student Worksheet

Default:

```text
STUDENT_PAGE_SIZE = A4
STUDENT_ORIENTATION = PORTRAIT
STUDENT_PAGE_COUNT_TARGET = 1
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
ANSWER_KEY_PAGE_SIZE = A4
ANSWER_KEY_ORIENTATION = PORTRAIT
ANSWER_KEY_PAGE_COUNT_TARGET = 1
ANSWER_KEY_REQUIRED = YES
ANSWER_KEY_RENDER_MODE = COLORED_SOLUTION
ANSWER_KEY_GEOMETRY_SOURCE = STUDENT_MASTER_GEOMETRY
ANSWER_KEY_TEXT_SOURCE = VERIFIED_CONTENT_BLUEPRINT
ANSWER_KEY_FILL_SOURCE = VERIFIED_COLOR_MAPPING
ANSWER_KEY_LAYOUT_MATCH = EXACT
ANSWER_KEY_PRESENTATION = SEPARATE_A4_PAGE_OR_FILE
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
PAIR_PACKAGING = TWO_SEPARATE_A4_PORTRAIT_PAGES
STUDENT_AND_ANSWER_ON_SAME_PAGE = NO
STUDENT_AND_ANSWER_SIDE_BY_SIDE = NO
STUDENT_PAGE_ORDER = 1
ANSWER_KEY_PAGE_ORDER = 2
```

รูปแบบที่ยอมรับ:
- Student worksheet เป็น A4 Portrait 1 หน้า และ Answer Key เป็น A4 Portrait 1 หน้าแยกกัน
- PDF เดียว 2 หน้าได้ โดยหน้า 1 = Student และหน้า 2 = Answer Key
- ส่งเป็นไฟล์แยก 2 ไฟล์ได้
- Batch หลายหน้าได้เมื่อจำเป็น แต่ทุก answer-key page ต้องแยกจาก student page ที่สอดคล้องกัน

รูปแบบที่ไม่ยอมรับโดย default:
- Student ซ้าย + Answer Key ขวาในหน้าเดียว
- Student ด้านบน + Answer Key ด้านล่างในหน้าเดียว
- thumbnail เฉลยอยู่ใน Student worksheet
- A3/landscape canvas ที่เอา A4 สองหน้ามาวางรวมกันเพื่อแสดงคู่

ข้อยกเว้นมีได้เฉพาะผู้ใช้สั่งชัดเจนว่าให้ทำ comparison/proof sheet สำหรับครูหรือ QA และต้องไม่เรียก output นั้นว่า student-facing worksheet.

## Single-page stress behavior

เมื่อผู้ใช้ต้องการ 40–50 ข้อ/คำใน Student A4 Portrait 1 หน้า:
- พยายามรักษา 1 หน้าโดยลด decoration และ micro-detail ก่อน
- รักษาขนาดข้อความ เส้น safe margin และพื้นที่ระบายสีให้อยู่ในเกณฑ์ใช้งานจริง
- ห้ามฝืน 1 หน้าโดยทำ text/strokes/cells เล็กเกิน QA
- ถ้าไม่สามารถผ่าน QA ได้จริง ให้แจ้งว่า single-page constraint ไม่ผ่านและเสนอ pagination

Answer Key ต้องใช้หน้า A4 Portrait แยกอีกหน้า และห้ามเปลี่ยน geometry เพื่อบีบให้พอดี

อ่านร่วมกับ `TWO_PAGE_A4_OUTPUT_POLICY.md`.

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
Student = render(master, fill=none, page=A4 portrait)
Answer = render(master, fill=mapping[color_id], page=A4 portrait)
Package = page1(student) + page2(answer)
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
- หน้าใดหน้าหนึ่งไม่ใช่ A4 Portrait โดยไม่มีคำสั่ง override จากผู้ใช้
- ฝืน 40–50 items ลงหน้าเดียวจน readability / colorability / print QA ไม่ผ่าน

## Output naming

แนะนำ:

```text
<worksheet_id>_student_A4_portrait
<worksheet_id>_answer_key_A4_portrait
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
> A4 PORTRAIT PAGE INTEGRITY
> TEXT IDENTITY
> LINE QUALITY
> COLOR FIDELITY
> DECORATION
```
