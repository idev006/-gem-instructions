# Geometric Color-by-Code — คู่มือการใช้งาน

Version: 1.7.0

## ใช้ทำอะไร
ใช้สร้างใบงาน Color by Code ที่ภาพหลักเกิดจากรูปทรงเรขาคณิตแบบ mosaic / tessellation และสามารถใช้ Natural Harmony ช่วยจัดองค์ประกอบให้สวย สมดุล และมีจังหวะคล้ายธรรมชาติ โดยยังคงความถูกต้อง ความอ่านง่าย และคุณภาพงานพิมพ์

Production default ตอนนี้สร้างเป็น **2 ชุดจาก master เดียวกัน**:
1. `STUDENT_WORKSHEET` — ขาว-ดำ ยังไม่เติมสีในพื้นที่กิจกรรม
2. `COLORED_ANSWER_KEY` — geometry เดียวกัน เติมสีตาม verified mapping

## สิ่งที่ผู้ใช้ควรกำหนด
ขั้นต่ำที่แนะนำ:
- ระดับชั้น
- วิชา
- หัวข้อ
- จำนวนข้อ
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
A4 Portrait
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
30 ข้อ 6 สี
ธีมสวนดอกไม้
ใช้สามเหลี่ยมเป็นรูปทรงหลัก
ทำเป็น mosaic
ใช้ Natural Harmony
A4 แนวตั้ง

ขอ 2 ชุด:
1) ใบงานนักเรียนขาว-ดำ ยังไม่ระบายสี
2) เฉลยแบบระบายสีเรียบร้อยแล้ว
```

## Twin Output Logic
หลักสำคัญ:

```text
ONE MASTER GEOMETRY
ONE VERIFIED MAPPING
TWO RENDER VIEWS
```

ระบบต้องสร้าง Student master ก่อน แล้วใช้ geometry/region IDs เดิมไปสร้างเฉลยโดยเติมสีจาก mapping เท่านั้น

ห้ามสร้างเฉลยเป็นภาพใหม่แบบอิสระ เพราะอาจเกิดกรณีโจทย์ถูกแต่สีผิด region

### Student Worksheet
- main activity area ขาว-ดำ
- ไม่เติมสีคำตอบ
- มี question/code/legend ตามกิจกรรม
- สีจริงใน legend อนุญาตได้ตาม default

### Colored Answer Key
- layout และ region boundaries เหมือน Student 100%
- question IDs/text เหมือน Student
- สีของแต่ละ region = verified mapping เท่านั้น
- เพิ่มคำว่า `เฉลย` ได้ แต่ห้ามแก้ geometry/content

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
- false claim ว่า exact golden ratio/Fibonacci/phyllotaxis

## Reference Levels
- `REFERENCE_WOW` — visual impact / richness
- `REFERENCE_BEAUTIFUL` — cleanliness / balance / readability
- `REFERENCE_NATURAL_HARMONY_V3` — รวมข้อดีสองแบบ + natural rhythm

## ตรวจงานก่อนใช้จริง
- จำนวนข้อ/คำตอบ/สีถูก
- mapping/legend ตรงและไม่มี orphan
- Student main art ยังไม่เติมสี
- Answer Key มีสีครบและตรงทุก region
- Student/Answer topology และ text ตรงกัน
- primary shape เห็นชัด
- ไม่มีเส้นแตก/ซ้อน/ขาด
- ไม่มีช่องเล็กเกินระบาย
- Thai glyph ถูกต้อง
- A4/orientation/margins ถูกต้อง
- production raster ถ้ามีต้องมาจาก vector master

อ่านเพิ่ม:
- `policies/TWIN_OUTPUT_ANSWER_KEY_POLICY.md`
- `policies/NATURAL_PROPORTION_POLICY.md`
- `policies/REFERENCE_VERSION_POLICY.md`
- `policies/GOLDEN_REFERENCE_STANDARD.md`
