# Geometric Color-by-Code — คู่มือการใช้งาน

Version: 1.8.0

## ใช้ทำอะไร
ใช้สร้างใบงาน Color by Code แบบหลายวิชา โดยวางแผน **คำตอบ/รหัสสีล่วงหน้า** แล้วจึงสร้างโจทย์ให้ตรงกับคำตอบนั้น เพื่อให้ทุกข้อมีสีที่นักเรียนสามารถระบายได้แน่นอน ก่อนนำไปจัดเป็นภาพ geometric mosaic / tessellation.

Production default:
- Student Worksheet = A4 Portrait ขาว-ดำ
- Answer Key = แยก A4 Portrait เมื่อผู้ใช้ต้องการ
- mapping/legend/region ใช้ source เดียวกัน
- production final ใช้ deterministic/vector boundaries

## หลักสำคัญใหม่: Answer First

```text
กำหนดจำนวนสี
→ กำหนดคำตอบ/รหัสที่ใช้จริง
→ map สี ↔ คำตอบ/รหัส
→ วางจำนวนข้อของแต่ละสี
→ แจก target answer/code ให้แต่ละ region
→ สร้างโจทย์จาก target
→ ตรวจคำตอบ
→ freeze mapping
→ render
```

ห้ามใช้วิธี:

```text
สร้างโจทย์ก่อน
→ คำนวณคำตอบ
→ ค่อยหาสีทีหลัง
```

เพราะอาจเกิดคำตอบที่ไม่มีใน legend.

Hard rule:

```text
NO QUESTION MAY PRODUCE AN ANSWER/CODE OUTSIDE THE ACTIVE LEGEND.
```

ถ้ามีแม้ 1 ข้อที่ไม่มีสีรองรับ ระบบต้อง FAIL ก่อน render.

## สิ่งที่ผู้ใช้ควรกำหนด
ขั้นต่ำที่แนะนำ:
- ระดับชั้น
- วิชา
- หัวข้อ
- จำนวนข้อ/คำ
- จำนวนสี (ถ้าไม่ระบุใช้ default)
- รูปทรงหลัก (ถ้าต้องการควบคุม)
- ธีม
- ขนาด/แนวกระดาษ
- ต้องการเฉลยหรือไม่

## Defaults
```text
PAGE_SIZE = A4
ORIENTATION = PORTRAIT
QUESTION_COUNT = 24
COLOR_COUNT = 6
CONTENT_GENERATION_MODE = ANSWER_FIRST
ACTIVE_CODE_SET = RESOLVE_BEFORE_QUESTION_GENERATION
COLOR_USAGE_PLAN = FREEZE_BEFORE_QUESTION_GENERATION
QUESTION_GENERATION_SOURCE = TARGET_ANSWER_OR_CODE
PRIMARY_SHAPE = TRIANGLE
SHAPE_DOMINANCE = HIGH
STUDENT_WORKSHEET_COLOR_MODE = MONOCHROME
STUDENT_REGION_FILL = NONE
LEGEND_COLOR_PREVIEW = YES
ANSWER_KEY = YES
PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED
```

## ตัวอย่าง: คณิตศาสตร์การหาร
คำสั่ง:

```text
สร้างใบงาน Color by Code ป.3
เรื่องการหารลงตัว ตัวตั้ง 2 หลัก ตัวหาร 1 หลัก
48 ข้อ 6 สี
ธีมยานอวกาศ
A4 แนวตั้ง
ไม่ต้องมีเฉลย
```

ระบบควรวางแผนก่อน เช่น:

```text
คำตอบ 2 → สีแดง
คำตอบ 3 → สีส้ม
คำตอบ 4 → สีเหลือง
คำตอบ 5 → สีเขียว
คำตอบ 6 → สีฟ้า
คำตอบ 7 → สีม่วง
48 ข้อ → target 8 ข้อต่อสี
```

แล้วจึงสร้างโจทย์จาก target answer เช่น target = 5:

```text
20 ÷ 4
25 ÷ 5
30 ÷ 6
35 ÷ 7
40 ÷ 8
45 ÷ 9
```

เลือกเฉพาะโจทย์ที่ผ่านเงื่อนไขตัวตั้ง 2 หลัก, ตัวหาร 1 หลัก, หารลงตัว, เหมาะกับระดับชั้น และไม่ขัด duplicate policy.

## 40–50 items ในใบงานหน้าเดียว
รองรับเป็น stress case หาก A4 Portrait 1 หน้ายังผ่าน QA.

ก่อนบีบ layout ระบบต้องลด decoration/micro-detail และใช้ grouped regions อย่างมีประสิทธิภาพ ห้ามลดตัวอักษร, stroke, safe margin หรือพื้นที่ระบายสีจนใช้งานไม่ได้.

สำหรับ 48 ข้อ / 6 สี ควรวาง distribution 8 ข้อต่อสีก่อนสร้างโจทย์. สำหรับจำนวนที่หารไม่ลงตัว ให้กระจายใกล้เคียงกันที่สุดโดยผลรวมต้องเท่ากับจำนวนข้อ.

## Student / Answer Key

### Student Worksheet
- ขาว-ดำในพื้นที่กิจกรรม
- legend แสดงสีตัวอย่างได้ตาม default
- ทุก region ต้องมี mapping ครบ แม้ผู้ใช้สั่งไม่เอาเฉลย

### Answer Key
เมื่อ `ANSWER_KEY = YES`:
- แยกหน้า A4 โดย default
- geometry/text/region IDs เดียวกับ Student
- เติมสีจาก verified mapping เท่านั้น

เมื่อ `ANSWER_KEY = NO`:
- ไม่สร้างหน้าเฉลย
- แต่ระบบยังต้องเก็บ correct answers + mapping ภายในเพื่อ QA

## Natural Harmony
Natural Harmony ใช้กับ placement, scale, rhythm, focal hierarchy และ balance เท่านั้น; ไม่เปลี่ยน question count หรือ mapping.

```text
NATURAL HARMONY = composition guide
PRIMARY SHAPE = construction grammar
ANSWER FIRST = academic/mapping generation rule
```

## Production Quality
```text
ACADEMIC CORRECTNESS
> COMPLETE LEGEND COVERAGE
> MAPPING INTEGRITY
> READABILITY
> COLORING USABILITY
> LINE QUALITY
> DECORATION
```

Production final ต้องใช้ deterministic/vector boundaries. Image model ใช้ช่วย concept/composition ได้ แต่ห้าม invent หรือ rewrite โจทย์หลัง mapping freeze.

## สิ่งที่ต้องหลีกเลี่ยง
- คำตอบที่ไม่มีสีใน legend
- สีใน legend ที่ไม่มีข้อใช้งานโดยไม่ตั้งใจ
- สร้างโจทย์ก่อนแล้วค่อยแก้สีทีหลัง
- math problem ที่ผิด topic constraints
- exact division ที่มีเศษ
- image model เปลี่ยนโจทย์หลัง verify
- sliver/needle cells
- fuzzy/double/broken strokes
- Student worksheet ถูกเติมสีโดยไม่ได้ขอ
- Answer Key สีผิด mapping
- Student/Answer geometry ต่างกัน
- ฝืน 40–50 items จน readability/print QA ไม่ผ่าน

## ตรวจงานก่อนใช้จริง
- จำนวนข้อและจำนวนสีตรงคำสั่ง
- active answer/code set ถูกกำหนดก่อนสร้างโจทย์
- color usage plan รวมแล้วเท่ากับจำนวนข้อ
- ทุกข้อมี target answer/code
- ทุกคำตอบ verified และตรง target
- ทุกคำตอบ/code มีสีใน legend
- ไม่มี orphan legend / question / region
- เงื่อนไขวิชาถูกต้อง
- Student main art ไม่เติมสี
- เฉลยถูก suppress เมื่อผู้ใช้ไม่ต้องการ
- primary shape / theme / layout ถูกต้อง
- ไม่มีเส้นแตก/ซ้อน/ขาด
- Thai glyph ถูกต้อง
- margins print-safe

อ่านเพิ่ม:
- `policies/ANSWER_FIRST_GENERATION_POLICY.md`
- `policies/COLOR_MAPPING_POLICY.md`
- `policies/TWO_PAGE_A4_OUTPUT_POLICY.md`
- `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`
- `policies/NATURAL_PROPORTION_POLICY.md`
