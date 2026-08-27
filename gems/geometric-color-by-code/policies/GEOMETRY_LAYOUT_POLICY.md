# Geometry Layout Policy

Version: 1.0.0

## Objective

รักษาความสวยงามแบบปูกระเบื้อง/โมเสก โดยไม่ลดความอ่านง่ายและความถูกต้องของใบงาน

## Primary-shape dominance

เมื่อผู้ใช้กำหนดรูปทรงหลัก:
- อย่างน้อย ~70% ของเส้นแบ่ง/เซลล์ใน main activity area ควรสอดคล้องกับ geometry ของรูปทรงหลัก
- ห้ามใช้ freeform illustration เป็นโครงสร้างหลัก
- รายละเอียดเสริมที่ไม่ใช่รูปทรงหลักใช้ได้เฉพาะเพื่อช่วย recognizability/readability

## Tiling validity

- TRIANGLE, SQUARE, RECTANGLE, RHOMBUS, HEXAGON: สามารถใช้ tessellation โดยตรงเมื่อ layout เหมาะสม
- CIRCLE_CELL: ใช้ cell packing / repeated circular cells ไม่ควรเรียกว่า exact tessellation หากมีช่องว่าง
- CUSTOM shape: ต้องระบุว่า exact tessellation, approximate tessellation หรือ decorative cell pattern

## Question readability

- จำนวน micro tiles อาจมากกว่าจำนวนข้อ
- default: `QUESTION_REGION_MODE = GROUPED_TILES`
- คำถามอยู่ในพื้นที่ที่มี contrast และขนาดพออ่าน
- ห้ามวางข้อความทับเส้นหลายเส้นหรือบริเวณที่แคบ

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

กฎ: theme recognizability ต้องไม่มาก่อน readability

## Print rule

Default A4 Portrait, print-safe margin, white background, black outlines, low ink. Colored preview จำกัดไว้ที่ legend เว้นแต่ผู้ใช้สั่งเป็นอย่างอื่น
