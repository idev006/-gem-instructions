# Geometric Color-by-Code — Usage Examples

Version: 1.6.0

## 1. Minimal — คณิตศาสตร์
```text
ป.3 คณิต การบวกเลข 1 หลัก 30 ข้อ 6 สี ธีมสวนดอกไม้ ใช้สามเหลี่ยม ทำเป็น mosaic
```

## 2. Natural Harmony — สวนดอกไม้
```text
สร้างใบงาน Color by Code
ป.3 คณิตศาสตร์ การบวกเลข 1 หลัก
30 ข้อ 6 สี
ธีมสวนดอกไม้
ใช้สามเหลี่ยมเป็นรูปทรงหลัก
ทำเป็น mosaic
ใช้ Natural Harmony
ให้มี focal flower หลัก
ใช้ golden-section guide และ Fibonacci/radial rhythm เมื่อเหมาะสม
ให้ question regions ไหลตามจังหวะของภาพ
A4 แนวตั้ง
```
Expected: 30 verified questions, about 5 regions per color when valid, triangle-built theme, balanced question flow, no micro-detail below colorable threshold, deterministic/vector final boundaries.

## 3. Natural Harmony — ระบบสุริยะ
```text
ป.4 วิทยาศาสตร์ ระบบสุริยะ 24 ข้อ 6 สี
ใช้หกเหลี่ยมเป็นหลัก
ธีมอวกาศ
Natural Harmony
ใช้ radial balance ที่เหมาะกับวงโคจร แต่ห้ามลอก composition ดอกไม้
A4 แนวนอน
```

## 4. Natural Harmony — ใต้ทะเล
```text
ป.3 ภาษาอังกฤษ Sea Animals vocabulary 24 questions 6 colors
PRIMARY_SHAPE = RHOMBUS
ธีมโลกใต้ทะเล
ใช้ natural balanced composition
ใช้ scale hierarchy จากสัตว์หลักไปองค์ประกอบรอง
```

## 5. ภาษาไทยแบบเน้นหมวด
```text
ป.3 ภาษาไทย มาตราตัวสะกด เน้นแม่กง 10 ข้อ 5 สี ใช้ข้าวหลามตัด ธีมสัตว์ป่า mosaic
```
Expected: focus distribution resolved before generation, all legend categories used, clear single-word items preferred.

## 6. Revision — preserve content
```text
คงโจทย์และคำตอบเดิมทั้งหมด เปลี่ยนจากสามเหลี่ยมเป็นหกเหลี่ยม
```

## 7. Revision — composition only
```text
คง content mapping สี และรูปทรงเดิม เปลี่ยน composition เป็น Natural Harmony แบบ approximate natural balance
```

## 8. Revision — reduce detail
```text
คงทุกอย่างเดิม ลด phyllotaxis detail และ micro tiles เพื่อให้ช่องระบายสีใหญ่ขึ้น
```

## 9. High question count
```text
ป.4 คณิต การคูณ 1 หลัก × 1 หลัก 60 ข้อ 8 สี ใช้สามเหลี่ยม low-poly mosaic A4
```
Expected: simplify/paginate before shrinking text or line weight.

## 10. Circle-cell edge case
```text
ป.2 คณิต บวกเลข 1 หลัก 20 ข้อ 5 สี ใช้วงกลมเป็นหลัก ธีมฟองสบู่
```
Expected: circle packing/cell pattern; do not falsely claim exact tessellation.

## 11. Open-ended edge case
```text
ป.5 วิทยาศาสตร์ ให้อธิบายการอนุรักษ์สิ่งแวดล้อมแบบ Color by Code 30 ข้อ
```
Expected: adapt to factual choice/category/true-false before mapping; do not place long essays in regions.
