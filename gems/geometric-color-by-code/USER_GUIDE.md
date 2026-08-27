# Geometric Color-by-Code — คู่มือการใช้งาน

Version: 1.5.0

## ใช้ทำอะไร

ใช้สร้างใบงาน Color by Code ที่ภาพหลักเกิดจากรูปทรงเรขาคณิตแบบ mosaic / tessellation เช่น สามเหลี่ยม สี่เหลี่ยม ข้าวหลามตัด หรือหกเหลี่ยม โดยเน้นความถูกต้อง ความสวยงาม ความอ่านง่าย และคุณภาพงานพิมพ์จริง

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

ค่าอื่นปล่อย AUTO ได้

## ค่าเริ่มต้นสำคัญ

```text
A4 แนวตั้ง
24 ข้อ
6 สี
PRIMARY_SHAPE = TRIANGLE
SHAPE_DOMINANCE = HIGH
PRIMARY_SHAPE_COVERAGE_TARGET ≈ 85%
QUESTION_REGION_MODE = GROUPED_TILES
TILE_SCALE_VARIATION = CONTROLLED
MAIN_ART_COLOR_MODE = MONOCHROME
LEGEND_COLOR_PREVIEW = YES
PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED
```

## ตัวอย่างคำสั่งพื้นฐาน

```text
สร้างใบงาน Color by Code
ระดับชั้น ป.3
วิชา คณิตศาสตร์
หัวข้อ การบวกเลข 1 หลัก
30 ข้อ 6 สี
ธีม สวนดอกไม้
ใช้รูปสามเหลี่ยมเป็นรูปทรงหลัก
ทำเป็น mosaic
A4 แนวตั้ง
```

## Natural Proportion / Natural Harmony

หากต้องการ composition ที่มีจังหวะเหมือนธรรมชาติ สามารถสั่งเพิ่มได้ เช่น:

```text
ใช้ Natural Proportion
ให้จุดเด่นของภาพวางตาม golden-section guide
ให้ดอกไม้ใช้ radial symmetry และ Fibonacci-inspired rhythm
ถ้ามีดอกทานตะวัน ให้ใช้ phyllotaxis / golden-angle-inspired arrangement
รักษาพื้นที่โจทย์ให้อ่านง่ายและระบายสีได้จริง
```

ระบบรองรับแนวคิด:
- Golden ratio / golden section เป็น composition guide
- Golden-angle-inspired spacing ประมาณ 137.5°
- Fibonacci-inspired repetition เช่น 3, 5, 8, 13 เมื่อเหมาะสม
- Radial symmetry
- Natural scale hierarchy
- Phyllotaxis-inspired seed/petal grouping

ข้อสำคัญ: สิ่งเหล่านี้เป็น **guide** ไม่ใช่ข้อบังคับให้ทุกองค์ประกอบต้องมีค่า exact ทางคณิตศาสตร์ ความอ่านง่ายและความถูกต้องมาก่อนเสมอ

อ่านเพิ่ม: `policies/NATURAL_PROPORTION_POLICY.md`

## Reference Versions

มี reference baseline 3 ระดับ:

```text
REFERENCE_WOW
= benchmark ด้านความประทับใจ ความมีชีวิตชีวา และ theme richness

REFERENCE_BEAUTIFUL
= benchmark ด้านความสะอาด balance negative space และ readability

REFERENCE_NATURAL_HARMONY_V3
= เป้าหมายรวมข้อดีของสองแบบ + natural proportion/rhythm
```

อ่านเพิ่ม: `policies/REFERENCE_VERSION_POLICY.md`

## สิ่งที่ระบบทำอัตโนมัติ

1. ตรวจหัวข้อและระดับชั้น
2. สร้างและตรวจคำถาม/คำตอบ
3. วาง distribution ของคำตอบ/สี
4. ล็อก mapping และ legend
5. สร้าง tile grammar
6. เลือก composition system
7. ถ้าเหมาะสม วาง natural proportion / focal hierarchy
8. สร้าง theme จาก tile clusters
9. รวม micro tiles เป็น question regions
10. ตรวจ minimum colorable area
11. กำหนด stroke hierarchy
12. final geometry/text แบบ deterministic/vector สำหรับ production print
13. ตรวจ Thai/text rendering
14. ตรวจ line/topology/visual/print QA

## หลักการคุณภาพเส้น

```text
CRISP_LINES > MICRO_TILE_DENSITY
READABILITY > GEOMETRIC_DETAIL
```

ถ้า micro mosaic แน่นจนเส้นเสีย ระบบต้องลดความหนาแน่นก่อน ไม่ใช่ทำเส้นให้บางจนพิมพ์ไม่ชัด

## Stroke hierarchy

```text
กรอบหลัก = หนาสุด
silhouette ของวัตถุ/ธีม = ปานกลาง
เส้นแบ่ง tile = บางกว่าเล็กน้อยแต่ยังคม
```

## พื้นที่ระบายสีขั้นต่ำ

ระบบต้องหลีกเลี่ยง:
- sliver cell
- รูปแหลมเล็กมาก
- segment สั้นถี่ ๆ
- จุด starburst ที่เส้นหลายเส้นชนกัน

ถ้าพบให้ merge/simplify geometry ก่อน render

## Freeform detail

อนุญาตรายละเอียด freeform เล็กน้อยเพื่อให้ภาพอ่านออก เช่น หนวดผีเสื้อ ตา หรือข้อต่อก้านดอก แต่ห้ามใช้ freeform เป็นโครงสร้างหลักของภาพเมื่อ `SHAPE_DOMINANCE = HIGH`

## Production render mode

สำหรับ final print ใช้ deterministic/vector-first เพื่อให้:
- เส้นคม
- shared border เป็นเส้นเดียว
- จำนวน region deterministic
- ภาษาไทยไม่ถูก image model rewrite
- raster preview มาจาก vector master

Image model ใช้ช่วยคิด composition/style ได้ แต่ไม่ใช่ source ของ final printable boundaries

## ตรวจงานก่อนใช้จริง

- จำนวนข้อถูก
- คำตอบถูก
- จำนวนสีถูก
- legend/mapping ตรง
- ไม่มีสีใน legend ที่ไม่ได้ใช้
- primary shape เห็นชัดทันที
- composition ดูสมดุล
- natural rhythm ไม่ฝืน usability
- ไม่มีเส้นแตก/ซ้อน/ขาด
- ไม่มีช่องเล็กเกินระบาย
- stroke hierarchy ชัด
- ภาษาไทยและ glyph ถูกต้อง
- main art ขาว-ดำตาม default
- print-safe

## Golden Reference

งานที่ผ่าน QA ระดับสูงสามารถใช้เป็น Golden Reference ได้ แต่ Golden Reference เป็น **มาตรฐานคุณภาพ** ไม่ใช่แม่แบบ composition ที่ต้องลอกทุกครั้ง

อ่านเพิ่มเติม:
- `policies/GOLDEN_REFERENCE_STANDARD.md`
- `policies/REFERENCE_VERSION_POLICY.md`
