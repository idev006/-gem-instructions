# Geometric Color-by-Code — Usage Examples

## 1. Minimal prompt — คณิตศาสตร์

```text
ป.3 คณิต การบวกเลข 1 หลัก 30 ข้อ 6 สี ธีมสวนดอกไม้ ใช้สามเหลี่ยม ทำเป็น mosaic
```

Expected resolution:
- A4 Portrait
- 30 questions
- 6 colors
- triangle-dominant mosaic
- garden silhouette from triangle groups
- monochrome worksheet + colored legend preview

## 2. Detailed prompt

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

## 4. Hexagon mosaic — วิทยาศาสตร์

```text
ป.4 วิทยาศาสตร์ การจำแนกสัตว์ 30 ข้อ 6 สี ใช้หกเหลี่ยม ธีมธรรมชาติ ทำเป็น honeycomb mosaic
```

## 5. English vocabulary

```text
ป.3 English Animals vocabulary 24 questions 6 colors use diamond tiles zoo mosaic
```

## 6. Revision — preserve content

```text
คงโจทย์และคำตอบเดิมทั้งหมด เปลี่ยนจากสามเหลี่ยมเป็นหกเหลี่ยม และคงธีมสวนดอกไม้
```

Expected: regenerate geometry/layout only; do not regenerate question set.

## 7. Revision — preserve geometry

```text
คงรูปสามเหลี่ยมและ mosaic เดิม แต่เปลี่ยนธีมจากสวนดอกไม้เป็นโลกใต้ทะเล
```

## 8. More questions

```text
ป.4 คณิต การคูณ 1 หลัก × 1 หลัก 60 ข้อ 8 สี ใช้สามเหลี่ยม low-poly mosaic A4
```

Expected: evaluate readability and paginate if required; do not force all 60 question regions onto one page.

## 9. Circle cells edge case

```text
ป.2 คณิต บวกเลข 1 หลัก 20 ข้อ 5 สี ใช้วงกลมเป็นหลัก ธีมฟองสบู่
```

Expected: use repeated circle-cell packing; do not falsely call it exact tessellation if gaps remain.

## 10. Open-ended topic edge case

```text
ป.5 วิทยาศาสตร์ ให้อธิบายการอนุรักษ์สิ่งแวดล้อมแบบ Color by Code 30 ข้อ
```

Expected: convert to clear factual choice/category/true-false style before mapping; do not create long written responses inside mosaic regions.
