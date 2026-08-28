# Geometric Color-by-Code — คู่มือการใช้งาน

Version: 1.8.1

## ใช้ทำอะไร
ใช้สร้างใบงาน Color by Code แบบหลายวิชา โดยวางแผน **คำตอบ/รหัสสีล่วงหน้า** แล้วสร้างโจทย์ให้ตรงกับ target นั้น จากนั้นจึงสร้าง artwork/geometry และวางข้อความวิชาการด้วย deterministic overlay เพื่อไม่ให้ image model เปลี่ยนโจทย์ หมายเลขข้อ หรือ legend ระหว่าง render.

Production default:
- Student Worksheet = A4 Portrait ขาว-ดำ
- Answer Key = แยก A4 Portrait เมื่อผู้ใช้ต้องการ
- Answer First = default academic generation
- Deterministic Academic Overlay = default final text render
- production final ใช้ deterministic/vector boundaries

## 1. Answer First

```text
กำหนดจำนวนสี
→ กำหนด active answer/code set
→ map สี ↔ answer/code
→ วางจำนวนข้อของแต่ละสี
→ แจก target ให้แต่ละ region
→ สร้างโจทย์จาก target
→ ตรวจคำตอบ
→ freeze mapping
```

Hard rule:

```text
NO QUESTION MAY PRODUCE AN ANSWER/CODE OUTSIDE THE ACTIVE LEGEND.
```

ถ้ามีแม้ 1 ข้อไม่มีสีรองรับ = FAIL ก่อน render.

## 2. Deterministic Content Render

บทเรียนจาก stress test ล่าสุดคือ แม้ blueprint ถูกต้อง แต่ถ้าให้ image model วาดสมการ/หมายเลข/legend เอง ภาพอาจสวยแต่ข้อความจริงเปลี่ยนได้.

ดังนั้น production/test-conformance ต้องทำ:

```text
Verified Content + Mapping
→ Artwork/Theme Layer
→ Deterministic Question/Text Overlay
→ Deterministic Legend Overlay
→ Final Composite
→ Post-Render Parity QA
```

Image model ใช้ได้กับ:
- artwork/theme
- decorative icons
- composition suggestions
- blank region design

ห้าม image model เป็น final source ของ:
- โจทย์
- หมายเลขข้อ
- ค่าคำตอบใน legend
- color mapping
- academic labels

ถ้าสร้างภาพทั้งหน้าด้วย image model และมีข้อความวิชาการในภาพ ให้ถือเป็น **concept preview** ไม่ใช่หลักฐานว่า Gem ผ่าน production QA.

## 3. สิ่งที่ผู้ใช้ควรกำหนด

ขั้นต่ำที่แนะนำ:
- ระดับชั้น
- วิชา
- หัวข้อ
- จำนวนข้อ/คำ
- จำนวนสี ถ้าต้องการควบคุม
- ธีม
- รูปทรงหลัก ถ้าต้องการ
- ขนาด/แนวกระดาษ
- ต้องการเฉลยหรือไม่

## 4. Defaults

```text
PAGE_SIZE = A4
ORIENTATION = PORTRAIT
QUESTION_COUNT = 24
COLOR_COUNT = 6
CONTENT_GENERATION_MODE = ANSWER_FIRST
COLOR_USAGE_PLAN = FREEZE_BEFORE_QUESTION_GENERATION
ACADEMIC_TEXT_RENDER_MODE = DETERMINISTIC_OVERLAY
ACADEMIC_TEXT_RENDER_SOURCE = VERIFIED_CONTENT_BLUEPRINT
LEGEND_RENDER_SOURCE = VERIFIED_MAPPING
POST_RENDER_CONTENT_PARITY = REQUIRED
PRIMARY_SHAPE = TRIANGLE
SHAPE_DOMINANCE = HIGH
STUDENT_WORKSHEET_COLOR_MODE = MONOCHROME
STUDENT_REGION_FILL = NONE
LEGEND_COLOR_PREVIEW = YES
ANSWER_KEY = YES
PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED
```

## 5. ตัวอย่าง: การหารลงตัว

คำสั่ง:

```text
สร้างใบงาน Color by Code ป.3
เรื่องการหารลงตัว ตัวตั้ง 2 หลัก ตัวหาร 1 หลัก
48 ข้อ 6 สี
ธีมยานอวกาศ
A4 แนวตั้ง
ไม่ต้องมีเฉลย
```

ระบบควรกำหนด legend domain ก่อน เช่น:

```text
5 → สีแดง
6 → สีส้ม
7 → สีเหลือง
8 → สีเขียว
9 → สีฟ้า
10 → สีม่วง
48 ข้อ → 8 ข้อต่อสี
```

จากนั้นแต่ละข้อจะถูกสร้างจาก target answer เท่านั้น และต้องตรวจ:
- ตัวตั้ง 2 หลัก
- ตัวหาร 1 หลัก
- หารลงตัว ไม่มีเศษ
- ผลหารอยู่ใน 5–10 เท่านั้น
- จำนวนข้อครบ/ไม่ซ้ำตาม policy

## 6. 40–50 items ใน A4 หน้าเดียว

รองรับเป็น stress case เมื่อ QA ผ่าน.

ลำดับการลดความหนาแน่น:
1. ลด decoration
2. ลด micro-detail
3. ใช้ grouped regions ให้มีประสิทธิภาพ
4. ปรับ negative space / anchors
5. paginate ถ้ายังอ่านไม่ออก

ห้ามแก้ด้วยการให้ image model ย่อ/วาง academic text เอง เพราะอาจเกิดหมายเลขข้อซ้ำ หาย หรือโจทย์เปลี่ยน.

## 7. Student / Answer Key

### Student Worksheet
- ขาว-ดำในพื้นที่กิจกรรม
- legend แสดงสีตัวอย่างได้
- mapping ต้องครบแม้ `ANSWER_KEY = NO`

### Answer Key
เมื่อ `ANSWER_KEY = YES`:
- แยกหน้า A4 โดย default
- geometry/text/region IDs เดียวกับ Student
- เติมสีจาก verified mapping เท่านั้น

## 8. Post-Render QA

ก่อนถือว่าผ่าน ต้องตรวจว่า:

```text
rendered_question_count == QUESTION_COUNT
rendered_question_ids == expected_question_ids
question IDs ไม่ซ้ำ/ไม่หาย
rendered_prompt_text == verified_prompt_text
rendered_legend_domain == active_legend_domain
```

ถ้า visible output ต่างจาก blueprint แม้ 1 ข้อ = Critical FAIL.

## 9. สิ่งที่ต้องหลีกเลี่ยง

- answer/code ที่ไม่มีสีใน legend
- orphan legend entry
- สร้างโจทย์ก่อนแล้วค่อยหาสี
- image model เปลี่ยนโจทย์หลัง verify
- หมายเลขข้อซ้ำ/หาย
- rendered question count ไม่ตรงคำสั่ง
- legend ที่ render ไม่ตรง verified mapping
- exact division ที่มีเศษ
- sliver/needle cells
- fuzzy/double/broken strokes
- Student ถูกเติมสีโดยไม่ได้ขอ
- Answer Key สีผิด mapping
- ฝืน 40–50 items จน readability/print QA ไม่ผ่าน

## 10. ตรวจงานก่อนใช้จริง

- จำนวนข้อ/สีตรงคำสั่ง
- active answer/code set ถูกกำหนดก่อนโจทย์
- usage plan รวมเท่าจำนวนข้อ
- ทุกข้อมี target + verified answer
- ทุก answer/code มีสี
- visible question IDs ครบ/ไม่ซ้ำ
- visible prompt text ตรง blueprint
- rendered legend ตรง mapping
- post-render parity = PASS
- primary shape/theme/layout ถูกต้อง
- ไม่มีเส้นแตก/ซ้อน/ขาด
- Thai glyph ถูกต้อง
- margins print-safe

อ่านเพิ่ม:
- `policies/ANSWER_FIRST_GENERATION_POLICY.md`
- `policies/COLOR_MAPPING_POLICY.md`
- `policies/DETERMINISTIC_CONTENT_RENDER_POLICY.md`
- `policies/TWO_PAGE_A4_OUTPUT_POLICY.md`
- `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`
