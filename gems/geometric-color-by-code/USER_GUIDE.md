# Geometric Color-by-Code — คู่มือการใช้งาน

Version: 1.7.1

## ใช้ทำอะไร
ใช้สร้างใบงาน Color by Code ที่ภาพหลักเกิดจากรูปทรงเรขาคณิตแบบ mosaic / tessellation และสามารถใช้ Natural Harmony ช่วยจัดองค์ประกอบให้สวย สมดุล และมีจังหวะคล้ายธรรมชาติ โดยยังคงความถูกต้อง ความอ่านง่าย และคุณภาพงานพิมพ์

Production default ตอนนี้สร้างเป็น **2 หน้า A4 แนวตั้งจาก master เดียวกัน**:
1. `STUDENT_WORKSHEET` — หน้า 1, A4 Portrait, ขาว-ดำ ยังไม่เติมสีในพื้นที่กิจกรรม
2. `COLORED_ANSWER_KEY` — หน้า 2, A4 Portrait, geometry เดียวกัน เติมสีตาม verified mapping

ห้ามรวมโจทย์และเฉลยไว้ในหน้าเดียวกันโดย default.

## สิ่งที่ผู้ใช้ควรกำหนด
ขั้นต่ำที่แนะนำ:
- ระดับชั้น
- วิชา
- หัวข้อ
- จำนวนข้อ/คำ
- จำนวนสี
- รูปทรงหลัก
- ธีม
- mosaic/tessellation style

กำหนดเพิ่มได้:
- Natural Harmony
- golden-section guide
- Fibonacci rhythm
- phyllotaxis/golden-angle-inspired rhythm
- symmetry/balance mode
- focal hierarchy
- question flow
- ไม่เอาเฉลย (`ANSWER_KEY = NO`)

## Defaults
```text
PAGE_SIZE = A4
ORIENTATION = PORTRAIT
STUDENT_PAGE_COUNT_TARGET = 1
ANSWER_KEY_PAGE_COUNT_TARGET = 1
PAIR_PACKAGING = TWO_SEPARATE_A4_PORTRAIT_PAGES
STUDENT_PAGE_ORDER = 1
ANSWER_KEY_PAGE_ORDER = 2

24 questions
6 colors
PRIMARY_SHAPE = TRIANGLE
SHAPE_DOMINANCE = HIGH
QUESTION_REGION_MODE = GROUPED_TILES
STUDENT_WORKSHEET_COLOR_MODE = MONOCHROME
STUDENT_REGION_FILL = NONE
LEGEND_COLOR_PREVIEW = YES
ANSWER_KEY = YES
ANSWER_KEY_RENDER_MODE = COLORED_SOLUTION
ANSWER_KEY_LAYOUT_MATCH = EXACT
COMPOSITION_SYSTEM = AUTO
NATURAL_SCALE_HIERARCHY = YES
QUESTION_FLOW = FOLLOW_VISUAL_RHYTHM
PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED
```

## ตัวอย่างคำสั่ง
```text
สร้างใบงาน Color by Code
ป.3 คณิตศาสตร์ การบวกเลข 1 หลัก
50 ข้อ 6 สี
ธีมทะเลและประภาคาร
ใช้สามเหลี่ยมเป็นรูปทรงหลัก
ทำเป็น mosaic
A4 แนวตั้ง

ขอผลลัพธ์ 2 หน้า:
หน้า 1 = ใบงานนักเรียนขาว-ดำ 1 หน้า A4
หน้า 2 = เฉลยระบายสี 1 หน้า A4
ห้ามรวมโจทย์และเฉลยไว้ในหน้าเดียวกัน
```

## 40–50 items ในใบงานหน้าเดียว
รองรับเป็น stress-case target โดยระบบต้องพยายามจัด Student Worksheet ให้จบใน A4 Portrait 1 หน้า **ตราบใดที่ยังผ่าน QA**.

ลำดับการปรับพื้นที่:
1. ลด decoration
2. ลด micro-detail
3. ใช้ grouped regions ที่มีประสิทธิภาพ
4. prefer คำ/คำตอบสั้นแบบ atomic เมื่อเหมาะสม
5. รักษา visual hierarchy และ negative space

ห้าม:
- ลดตัวอักษรจนอ่านยาก
- ลด stroke จนเส้นแตก
- ทำช่องระบายสีเล็กเกินไป
- ลด safe margin จนไม่ print-safe

ถ้า 1 หน้าไม่สามารถผ่าน readability / colorability / print QA ได้จริง ระบบต้องบอกข้อจำกัดและเสนอ pagination แทน ไม่ควรฝืนแล้วเรียกว่า production-ready.

## Twin Output Logic
หลักสำคัญ:

```text
ONE MASTER GEOMETRY
ONE VERIFIED MAPPING
TWO RENDER VIEWS
TWO SEPARATE A4 PORTRAIT PAGES
```

ระบบต้องสร้าง Student master ก่อน แล้วใช้ geometry/region IDs เดิมไปสร้างเฉลยโดยเติมสีจาก mapping เท่านั้น

### Student Worksheet — Page 1
- A4 Portrait 1 หน้าโดย default
- main activity area ขาว-ดำ
- ไม่เติมสีคำตอบ
- มี question/code/legend ตามกิจกรรม
- สีจริงใน legend อนุญาตได้ตาม default

### Colored Answer Key — Page 2
- A4 Portrait 1 หน้าโดย default
- layout และ region boundaries เหมือน Student 100%
- question IDs/text เหมือน Student
- สีของแต่ละ region = verified mapping เท่านั้น
- เพิ่มคำว่า `เฉลย` ได้ แต่ห้ามแก้ geometry/content

ถ้ารวมเป็น PDF เดียว:
```text
Page 1 = Student Worksheet
Page 2 = Colored Answer Key
```

ห้ามสร้างเฉลยเป็นภาพใหม่แบบอิสระ เพราะอาจเกิดกรณีโจทย์ถูกแต่สีผิด region

## Pair QA
ก่อนส่ง final ต้องตรวจทุก `region_id`:

```text
student.region_id == answer.region_id
student.question_id == answer.question_id
expected_color = verified_mapping[question_id]
answer.fill_color == expected_color
```

ผิดแม้ 1 region = Critical FAIL

## Natural Harmony
Natural Harmony ใช้กับ placement, scale, rhythm, focal hierarchy และ balance เท่านั้น

```text
NATURAL HARMONY = composition guide
PRIMARY SHAPE = construction grammar
```

- Golden section ใช้เป็น guide ไม่บังคับ exact 1.618
- Fibonacci ใช้เป็นจังหวะ 3/5/8/13 เมื่อเหมาะสม
- Phyllotaxis/golden-angle ~137.5° ใช้เป็น inspiration ได้
- ห้ามสร้าง micro-detail เล็กจนระบายสีไม่ได้
- `SYMMETRY_MODE = AUTO` อาจเลือก bilateral, radial, approximate natural balance หรือ none

## Production Quality
```text
CRISP_LINES > MICRO_TILE_DENSITY
READABILITY > GEOMETRIC_DETAIL
```

Production final ต้องใช้ deterministic/vector boundaries; Student และ Answer Key ต้องใช้ line master เดียวกัน

## สิ่งที่ต้องหลีกเลี่ยง
- sliver/needle cells
- short-segment noise
- starburst junction
- fuzzy/double/broken strokes
- freeform major object เมื่อ SHAPE_DOMINANCE=HIGH
- orphan legend entry
- Student worksheet ถูกเติมสีโดยไม่ได้ขอ
- Answer Key สีผิด mapping
- Student/Answer geometry ต่างกัน
- Student + Answer Key อยู่หน้าเดียวกันโดย default
- ฝืน 40–50 items จน readability/print QA ไม่ผ่าน
- false claim ว่า exact golden ratio/Fibonacci/phyllotaxis

## Reference Levels
- `REFERENCE_WOW` — visual impact / richness
- `REFERENCE_BEAUTIFUL` — cleanliness / balance / readability
- `REFERENCE_NATURAL_HARMONY_V3` — รวมข้อดีสองแบบ + natural rhythm
- High-density 40–50 item single-page output ใช้เป็น stress-test benchmark เพิ่มเติม

## ตรวจงานก่อนใช้จริง
- จำนวนข้อ/คำตอบ/สีถูก
- mapping/legend ตรงและไม่มี orphan
- Student = A4 Portrait หน้า 1
- Answer Key = A4 Portrait หน้า 2
- ไม่มีเฉลยอยู่บนหน้า Student
- Student main art ยังไม่เติมสี
- Answer Key มีสีครบและตรงทุก region
- Student/Answer topology และ text ตรงกัน
- primary shape เห็นชัด
- ไม่มีเส้นแตก/ซ้อน/ขาด
- ไม่มีช่องเล็กเกินระบาย
- Thai glyph ถูกต้อง
- margins print-safe
- production raster ถ้ามีต้องมาจาก vector master

อ่านเพิ่ม:
- `policies/TWO_PAGE_A4_OUTPUT_POLICY.md`
- `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`
- `policies/NATURAL_PROPORTION_POLICY.md`
- `policies/REFERENCE_VERSION_POLICY.md`
- `policies/GOLDEN_REFERENCE_STANDARD.md`
