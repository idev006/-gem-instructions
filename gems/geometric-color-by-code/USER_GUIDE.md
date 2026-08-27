# Geometric Color-by-Code — คู่มือการใช้งาน

Version: 1.4.0

## ใช้ทำอะไร

ใช้สร้างใบงาน Color by Code ที่ภาพหลักเกิดจากรูปทรงเรขาคณิตแบบ mosaic / tessellation เช่น สามเหลี่ยม สี่เหลี่ยม ข้าวหลามตัด หรือหกเหลี่ยม โดยเน้นความถูกต้องและคุณภาพงานพิมพ์จริง

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
RENDER_MODE = AUTO
VECTOR_RENDERING_PREFERRED = YES
LINE_RENDER_STYLE = CLEAN_VECTOR_LIKE
```

## ตัวอย่างคำสั่ง

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

## สิ่งที่ระบบทำอัตโนมัติ

1. ตรวจหัวข้อและระดับชั้น
2. สร้างและตรวจคำถาม/คำตอบ
3. วาง distribution ของคำตอบ/สี
4. ล็อก mapping และ legend
5. สร้าง tile grammar
6. สร้าง theme จาก tile clusters
7. รวม micro tiles เป็น question regions
8. ตรวจ minimum colorable area
9. กำหนด stroke hierarchy
10. เลือก render mode
11. ตรวจ Thai/text rendering
12. ตรวจ line/topology/print QA

## หลักการคุณภาพเส้น

```text
CRISP_LINES > MICRO_TILE_DENSITY
READABILITY > GEOMETRIC_DETAIL
```

ถ้า micro mosaic แน่นจนเส้นแตก ระบบต้องลดความหนาแน่นก่อน ไม่ใช่ทำเส้นให้บางลงจนพิมพ์ไม่ชัด

## Stroke hierarchy

ควรเห็น 3 ระดับ:

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

อนุญาตรายละเอียด freeform เล็กน้อยเพื่อให้ภาพอ่านออก เช่น หนวดผีเสื้อ ตา หรือข้อต่อก้านดอก

แต่ห้ามใช้ freeform เป็นโครงสร้างหลักของดอกไม้ เมฆ ใบไม้ ปีก หรือวัตถุใหญ่ เมื่อ `SHAPE_DOMINANCE = HIGH`

## Render mode

### VECTOR_FIRST
เหมาะที่สุดสำหรับงานขาย/พิมพ์จริง เพราะเส้นและข้อความ deterministic

### HYBRID
ใช้ image model ช่วยคิด composition แต่ final geometry/text ต้อง render แบบ deterministic เมื่อทำได้

### IMAGE_PROMPT_ONLY
เป็น fallback ต้องมี iterative QA และลด geometry complexity เมื่อเส้น fail

## ตรวจงานก่อนใช้จริง

- จำนวนข้อถูก
- คำตอบถูก
- จำนวนสีถูก
- legend/mapping ตรง
- ไม่มีสีใน legend ที่ไม่ได้ใช้
- primary shape เห็นชัดทันที
- ไม่มี major freeform drift
- ไม่มีเส้นแตก/ซ้อน/ขาด
- ไม่มีช่องเล็กเกินระบาย
- stroke hierarchy ชัด
- ภาษาไทยและ glyph ถูกต้อง
- main art ขาว-ดำตาม default
- print-safe

## Golden Reference

งานที่ผ่าน QA ระดับสูงสามารถใช้เป็น Golden Reference ได้ แต่ Golden Reference เป็นเพียง **มาตรฐานคุณภาพ** ไม่ใช่แม่แบบ composition ที่ระบบต้องลอกทุกครั้ง

อ่านเพิ่มเติม: `policies/GOLDEN_REFERENCE_STANDARD.md`
