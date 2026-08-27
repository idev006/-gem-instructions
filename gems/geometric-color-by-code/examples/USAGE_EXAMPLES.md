# Geometric Color-by-Code — Usage Examples

Version: 1.2.0

## 1. Minimal prompt — คณิตศาสตร์

```text
ป.3 คณิต การบวกเลข 1 หลัก 30 ข้อ 6 สี ธีมสวนดอกไม้ ใช้สามเหลี่ยม ทำเป็น mosaic
```

Expected resolution:
- A4 Portrait
- 30 questions
- 6 colors
- answer/color frequency plan before render
- triangle-dominant mosaic
- primary-shape coverage target about 85%
- garden silhouette from triangle groups
- question regions from grouped triangle tiles
- monochrome worksheet + colored legend preview

## 2. Detailed prompt — production reference

```text
สร้างใบงาน Color by Code
ระดับชั้น: ป.3
วิชา: คณิตศาสตร์
หัวข้อ: การบวกเลข 1 หลัก
จำนวนข้อ: 30
จำนวนสี: 6
รูปทรงหลัก: สามเหลี่ยม
รูปแบบ: mosaic tessellation
ธีม: สวนดอกไม้

ให้ใช้รูปสามเหลี่ยมเป็นภาษาหลักของภาพทั้งหน้า
ให้ดอกไม้ ใบไม้ ผีเสื้อ เมฆ ภูเขา และพื้นสวนเกิดจากการรวมกลุ่มสามเหลี่ยม
ห้ามวาดวัตถุเหล่านี้แบบ freeform ขนาดใหญ่แล้วค่อยตีเส้นสามเหลี่ยมทับ
ให้พื้นที่โจทย์เกิดจากกลุ่มสามเหลี่ยมเป็นหลัก
ควบคุมขนาด tile ให้ภาพทั้งหน้าเป็นระบบเดียวกัน
ตรวจไม่ให้มีเส้นซ้อน เส้นขาด ช่องเปิด หรือช่องจิ๋วที่ระบายสีไม่ได้

ขนาดกระดาษ: A4
แนวกระดาษ: แนวตั้ง
ภาพหลักขาว-ดำ
แสดงตัวอย่างสีจริงใน legend
มีเฉลย
```

## 3. Square mosaic — ภาษาไทย

```text
ป.2 ภาษาไทย เรื่องคำที่มีสระอา 24 ข้อ 6 สี ใช้สี่เหลี่ยมจัตุรัส ธีมตลาดผลไม้ mosaic
```

## 4. Diamond / rhombus — ภาษาไทยแบบเน้นหมวด

```text
ป.3 ภาษาไทย มาตราตัวสะกด เน้นแม่กง 10 ข้อ 5 สี ใช้ข้าวหลามตัด ธีมสัตว์ป่า mosaic
```

Expected:
- resolve focus distribution before word generation
- all 5 legend categories used
- แม่กง has highest count
- prefer single-word items
- animal silhouettes built from rhombus clusters

## 5. Hexagon mosaic — วิทยาศาสตร์

```text
ป.4 วิทยาศาสตร์ การจำแนกสัตว์ 30 ข้อ 6 สี ใช้หกเหลี่ยม ธีมธรรมชาติ ทำเป็น honeycomb mosaic
```

## 6. English vocabulary

```text
ป.3 English Animals vocabulary 24 questions 6 colors use diamond tiles zoo mosaic
```

## 7. Revision — preserve content

```text
คงโจทย์และคำตอบเดิมทั้งหมด เปลี่ยนจากสามเหลี่ยมเป็นหกเหลี่ยม และคงธีมสวนดอกไม้
```

Expected: regenerate geometry/layout/topology only; do not regenerate question set.

## 8. Revision — improve geometric fidelity

```text
คงโจทย์และสีเดิม ลดเส้นโค้ง ให้ดอกไม้ ใบไม้ ผีเสื้อ และเมฆสร้างจากสามเหลี่ยมมากขึ้น และคงพื้นที่อ่านข้อความให้ชัด
```

## 9. Revision — fix topology

```text
คงทุกอย่างเดิม แก้เส้นซ้อน เส้นขาด และช่องสามเหลี่ยมจิ๋ว ให้ขอบแต่ละ region ปิดและอ่านง่ายขึ้น
```

## 10. More questions

```text
ป.4 คณิต การคูณ 1 หลัก × 1 หลัก 60 ข้อ 8 สี ใช้สามเหลี่ยม low-poly mosaic A4
```

Expected: evaluate readability and paginate if required; do not force all 60 question regions onto one page.

## 11. Circle cells edge case

```text
ป.2 คณิต บวกเลข 1 หลัก 20 ข้อ 5 สี ใช้วงกลมเป็นหลัก ธีมฟองสบู่
```

Expected: use repeated circle-cell packing; do not falsely call it exact tessellation if gaps remain.

## 12. Open-ended topic edge case

```text
ป.5 วิทยาศาสตร์ ให้อธิบายการอนุรักษ์สิ่งแวดล้อมแบบ Color by Code 30 ข้อ
```

Expected: convert to clear factual choice/category/true-false style before mapping; do not create long written responses inside mosaic regions.
