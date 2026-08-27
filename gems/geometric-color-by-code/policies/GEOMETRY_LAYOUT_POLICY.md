# Geometry Layout Policy

Version: 1.1.0

## Objective

รักษาความสวยงามแบบปูกระเบื้อง/โมเสก โดยไม่ลดความอ่านง่ายและความถูกต้องของใบงาน และต้องทำให้รูปทรงที่ผู้ใช้กำหนดเป็น **โครงสร้างที่สร้างภาพจริง** ไม่ใช่ pattern overlay บนภาพ freeform

## Primary-shape dominance

เมื่อผู้ใช้กำหนดรูปทรงหลัก:
- `SHAPE_DOMINANCE = HIGH` ตั้งเป้าให้ประมาณ 80% หรือมากกว่าของ structural cell boundaries / visible tiling rhythm ใน main activity area derive จาก geometry ของรูปทรงหลัก
- ห้ามใช้ freeform illustration เป็นโครงสร้างหลัก
- รายละเอียดเสริมที่ไม่ใช่รูปทรงหลักใช้ได้เฉพาะเพื่อช่วย recognizability/readability
- ถ้ามองภาพรวมจากระยะไกล ต้องเห็นได้ทันทีว่าภาพถูกประกอบจากรูปทรงหลัก

### Construction test

PASS:

```text
primary shape
→ repeated/varied tiles
→ grouped clusters
→ object silhouette
→ complete themed composition
```

FAIL:

```text
freeform animal/object drawing
→ geometric lines/pattern added on top
```

## Freeform-area limit

เมื่อ `SHAPE_DOMINANCE = HIGH`:
- ห้ามมี freeform object ขนาดใหญ่ครอง silhouette หลัก
- freeform detail ใช้สำหรับตา ปาก label anchor ข้อต่อ หรือ contour correction เล็กน้อยได้
- target freeform structural area ควรต่ำประมาณ 15–20% ของ main composition และต้องไม่ทำลาย tile rhythm
- หากต้องใช้ freeform มากกว่านี้เพื่อให้ธีมอ่านออก ให้ downgrade `SHAPE_DOMINANCE` อย่างซื่อสัตย์ หรือ redesign geometry แทนการแอบละเมิดค่า HIGH

## Tiling validity

- TRIANGLE, SQUARE, RECTANGLE, RHOMBUS, HEXAGON: สามารถใช้ tessellation โดยตรงเมื่อ layout เหมาะสม
- CIRCLE_CELL: ใช้ cell packing / repeated circular cells ไม่ควรเรียกว่า exact tessellation หากมีช่องว่าง
- CUSTOM shape: ต้องระบุว่า exact tessellation, approximate tessellation หรือ decorative cell pattern

## Question readability

- จำนวน micro tiles อาจมากกว่าจำนวนข้อ
- default: `QUESTION_REGION_MODE = GROUPED_TILES`
- คำถามอยู่ในพื้นที่ที่มี contrast และขนาดพออ่าน
- ห้ามวางข้อความทับเส้นหลายเส้นหรือบริเวณที่แคบ
- question region ใหญ่ได้ แต่ขอบ/พื้นฐานของ region ยังควร derive จาก primary-shape grid หรือ grouped cells มากที่สุด

## Density resolution

เมื่อโจทย์/ข้อความแน่นเกินไป:
1. ลด decoration
2. รวม tiles เป็น question regions ใหญ่ขึ้น
3. ย้ายคำถามไป anchor zone
4. ปรับ orientation
5. paginate
6. ห้ามย่อตัวอักษรจนอ่านยาก

## Theme construction

Theme silhouette ต้องเกิดจาก tile grouping เช่น:
- flower = symmetric clusters
- leaf = tapered tile clusters
- butterfly = mirrored clusters
- mountain = triangular bands
- waves = stepped/angled bands
- elephant = grouped rhombus/triangle cells forming head, body, ears, trunk and legs
- bird = mirrored/stacked polygon cells forming body, head, wing and tail

กฎ: theme recognizability ต้องไม่มาก่อน readability แต่ recognizability ห้ามถูกแก้ด้วยการกลับไปวาด freeform object ขนาดใหญ่

## Shape audit checklist

ก่อน PASS ให้ถาม:
1. ถ้าลบเส้น freeform ออก ภาพยังคงอ่านเป็น mosaic จาก primary shape หรือไม่
2. silhouette หลักเกิดจาก tile clusters จริงหรือไม่
3. มีวัตถุหลักใดที่เป็น conventional drawing แล้วเพียงเติม pattern ภายหลังหรือไม่
4. primary-shape rhythm ต่อเนื่องพอหรือไม่
5. question regions ยังสัมพันธ์กับ grid/tiling หรือถูกตัดเป็น freeform ขนาดใหญ่เกินไปหรือไม่

ถ้าข้อ 2 = ไม่ หรือข้อ 3 = ใช่ → Critical FAIL สำหรับ `SHAPE_DOMINANCE = HIGH`

## Print rule

Default A4 Portrait, print-safe margin, white background, black outlines, low ink. Colored preview จำกัดไว้ที่ legend เว้นแต่ผู้ใช้สั่งเป็นอย่างอื่น
