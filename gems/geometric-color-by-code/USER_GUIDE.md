# Geometric Color-by-Code — คู่มือการใช้งาน

Version: 1.6.0

## ใช้ทำอะไร
ใช้สร้างใบงาน Color by Code ที่ภาพหลักเกิดจากรูปทรงเรขาคณิตแบบ mosaic / tessellation และสามารถใช้ Natural Harmony ช่วยจัดองค์ประกอบให้สวย สมดุล และมีจังหวะคล้ายธรรมชาติ โดยยังคงความถูกต้อง ความอ่านง่าย และคุณภาพงานพิมพ์

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

## Defaults
```text
A4 Portrait
24 questions
6 colors
PRIMARY_SHAPE = TRIANGLE
SHAPE_DOMINANCE = HIGH
PRIMARY_SHAPE_COVERAGE_TARGET ≈ 85%
QUESTION_REGION_MODE = GROUPED_TILES
MAIN_ART_COLOR_MODE = MONOCHROME
LEGEND_COLOR_PREVIEW = YES
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
ให้ดอกหลักเป็น focal point
ใช้ golden-section guide และ Fibonacci/radial rhythm เมื่อเหมาะสม
ให้ question regions ไหลตามจังหวะของภาพ
A4 แนวตั้ง
```

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

## Question Flow
`QUESTION_FLOW = FOLLOW_VISUAL_RHYTHM`

ตำแหน่งโจทย์ต้องสนับสนุนสายตาและ composition แต่ห้ามเปลี่ยนจำนวนข้อ คำตอบ mapping หรือ readability

## Production Quality
```text
CRISP_LINES > MICRO_TILE_DENSITY
READABILITY > GEOMETRIC_DETAIL
```

Production final ต้องใช้ deterministic/vector boundaries; image model ใช้เป็น concept/mockup ได้แต่ไม่ใช่ final coloring boundary source

## Stroke hierarchy
```text
กรอบหลัก = หนาสุด
silhouette = ปานกลาง
internal tile = บางกว่าเล็กน้อยแต่ยังคม
```

## สิ่งที่ต้องหลีกเลี่ยง
- sliver/needle cells
- short-segment noise
- starburst junction
- fuzzy/double/broken strokes
- freeform major object เมื่อ SHAPE_DOMINANCE=HIGH
- orphan legend entry
- false claim ว่า exact golden ratio/Fibonacci/phyllotaxis

## Reference Levels
- `REFERENCE_WOW` — visual impact / richness
- `REFERENCE_BEAUTIFUL` — cleanliness / balance / readability
- `REFERENCE_NATURAL_HARMONY_V3` — รวมข้อดีสองแบบ + natural rhythm

Reference เป็น quality benchmark ไม่ใช่ composition template

## ตรวจงานก่อนใช้จริง
- จำนวนข้อ/คำตอบ/สีถูก
- mapping/legend ตรงและไม่มี orphan
- primary shape เห็นชัด
- natural hierarchy สวยแต่ไม่ฝืน
- question flow สมดุล
- ไม่มีเส้นแตก/ซ้อน/ขาด
- ไม่มีช่องเล็กเกินระบาย
- Thai glyph ถูกต้อง
- A4/orientation/margins ถูกต้อง
- production raster ถ้ามีต้องมาจาก vector master

อ่านเพิ่ม:
- `policies/NATURAL_PROPORTION_POLICY.md`
- `policies/REFERENCE_VERSION_POLICY.md`
- `policies/GOLDEN_REFERENCE_STANDARD.md`
