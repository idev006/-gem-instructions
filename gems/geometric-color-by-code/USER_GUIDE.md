# Geometric Color-by-Code — คู่มือการใช้งาน

Version: 1.2.0

## Gem นี้ใช้ทำอะไร

ใช้สร้าง prompt/blueprint สำหรับใบงาน Color by Code ที่สร้างภาพจากรูปทรงเรขาคณิตแบบ mosaic / tessellation ตามรูปทรงที่ผู้ใช้กำหนด เช่น สามเหลี่ยม สี่เหลี่ยม หกเหลี่ยม หรือรูปหลายเหลี่ยม

## จุดเด่น

รูปทรงที่กำหนดจะเป็น **ภาษาหลักของภาพ** ไม่ใช่ของตกแต่ง ภาพธีม เช่น สวนดอกไม้ อวกาศ ใต้ทะเล หรือฟาร์ม ต้องเกิดจากการจัดกลุ่มกระเบื้องรูปทรงนั้น

หลักสำคัญ:

```text
รูปทรง → กระเบื้อง → กลุ่มกระเบื้อง → รูปภาพธีม
```

ไม่ใช่:

```text
วาดภาพปกติ → ตีเส้นรูปทรงทับทีหลัง
```

## ผู้ใช้ควรกำหนดอะไร

ขั้นต่ำที่แนะนำ:
- ระดับชั้น
- วิชา
- หัวข้อ
- จำนวนข้อ
- จำนวนสี
- รูปทรงหลัก
- ธีม
- รูปแบบ mosaic/tessellation

ค่าอื่นไม่ระบุได้ Gem จะใช้ default

## ค่าเริ่มต้น

```text
A4 แนวตั้ง
24 ข้อ
6 สี
PRIMARY_SHAPE = TRIANGLE
TILING_MODE = TESSELLATION
SHAPE_DOMINANCE = HIGH
PRIMARY_SHAPE_COVERAGE_TARGET ≈ 85%
TILE_SCALE_VARIATION = CONTROLLED
QUESTION_REGION_MODE = GROUPED_TILES
QUESTION_REGION_SHAPE_GRAMMAR = PRIMARY_SHAPE_GROUP
FREEFORM_MAJOR_OBJECTS = PROHIBITED_WHEN_HIGH
MAIN_ART_COLOR_MODE = MONOCHROME
LEGEND_COLOR_PREVIEW = YES
ANSWER_KEY = YES
```

## ตัวอย่างคำสั่งสั้น

```text
ป.3 คณิต การบวกเลข 1 หลัก 30 ข้อ 6 สี ธีมสวนดอกไม้ ใช้สามเหลี่ยม ทำเป็น mosaic
```

## ตัวอย่างคำสั่งละเอียด

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
ให้ดอกไม้ ใบไม้ ผีเสื้อ เมฆ ภูเขา และพื้นสวนเกิดจากการรวมกลุ่มสามเหลี่ยมเป็นหลัก
ห้ามวาดวัตถุ freeform ขนาดใหญ่แล้วค่อยตีเส้นสามเหลี่ยมทับ
ให้พื้นที่โจทย์เกิดจากกลุ่มสามเหลี่ยม
ควบคุมขนาด tile ให้ทั้งหน้าเป็น visual language เดียวกัน
ขนาดกระดาษ: A4
แนวกระดาษ: แนวตั้ง
ภาพหลักขาว-ดำ
แสดงตัวอย่างสีจริงใน legend
มีเฉลย
```

## สิ่งที่ Gem จะทำอัตโนมัติ

1. ตรวจว่าหัวข้อเหมาะกับ Color by Code หรือไม่
2. สร้าง/ตรวจชุดคำถามและคำตอบ
3. วาง answer/category frequency plan
4. normalize คำตอบเป็น code
5. map code ไปสี
6. ตรวจว่า legend ทุกสี/หมวดถูกใช้งานจริง
7. สร้าง geometric tiling grammar
8. จัดกลุ่ม micro tiles เป็น question regions
9. สร้าง silhouette ของธีมจาก tiles
10. ตรวจ tile-scale consistency
11. ตรวจ line topology เช่น เส้นซ้อน เส้นขาด ช่องจิ๋ว
12. สร้าง final prompt
13. ตรวจ correctness, mapping, geometry, Thai และ print QA

## Micro tiles และ question regions ต่างกันอย่างไร

จำนวนโจทย์ไม่จำเป็นต้องเท่ากับจำนวนกระเบื้องเล็ก

เช่น 30 ข้อ อาจใช้ 120–180 สามเหลี่ยมเล็ก แล้วจัดกลุ่มเป็น 30 question regions เพื่อให้ภาพสวยและข้อความยังอ่านได้

## การกระจายคำตอบ/สี

ถ้าไม่มีเหตุผลเชิงเนื้อหาที่ต้องกระจายไม่เท่ากัน ระบบจะวางแผนให้ค่อนข้างสมดุลก่อน render

ตัวอย่าง:

```text
30 ข้อ / 6 สี ≈ 5 ข้อต่อสี
```

ระบบต้อง freeze distribution ก่อนสร้างภาพ ไม่ปล่อยให้ image model สุ่มเอง

## รองรับรูปทรง

- สามเหลี่ยม
- สี่เหลี่ยม
- สี่เหลี่ยมผืนผ้า
- ข้าวหลามตัด / rhombus
- หกเหลี่ยม
- trapezoid
- kite
- circle-based cells
- mixed polygons
- custom

## รองรับหลายวิชา

- คณิตศาสตร์: numeric
- ภาษาไทย: word/category/choice
- อังกฤษ: vocabulary/phonics/category
- วิทยาศาสตร์: choice/category/true-false
- สังคม/สุขศึกษา: choice/category/short-text ที่ชัดเจน

## การแก้งานต่อเนื่อง

```text
คงโจทย์เดิม เปลี่ยนสามเหลี่ยมเป็นหกเหลี่ยม
```

```text
คงทุกอย่างเดิม แต่เปลี่ยนธีมเป็นโลกใต้ทะเล
```

```text
เพิ่มเป็น 8 สี แต่คง 30 ข้อ
```

```text
ให้ mosaic แน่นขึ้น แต่ตัวเลขต้องใหญ่เท่าเดิม
```

```text
ลดเส้นโค้ง ให้ใบไม้และดอกไม้สร้างจากสามเหลี่ยมมากขึ้น
```

## วิธีตรวจผลลัพธ์

ก่อนนำไปใช้จริงตรวจ:
1. จำนวนข้อถูก
2. คำตอบถูก
3. จำนวนสีถูก
4. legend ตรง mapping และไม่มีสีที่ไม่ถูกใช้
5. รูปทรงหลักครองภาพจริง
6. ธีมเกิดจาก tile grouping ไม่ใช่ freeform illustration
7. question regions ยัง derive จากรูปทรงหลัก
8. tile scale ทั้งหน้าสอดคล้องกัน
9. ไม่มีเส้นซ้อน เส้นขาด หรือช่องจิ๋วที่ระบายสีไม่ได้
10. ตัวเลข/ข้อความอ่านง่าย
11. กระดาษและ orientation ถูกต้อง
12. ขาว-ดำพิมพ์ได้ดี
13. เฉลยตรงกับ worksheet

## ข้อจำกัด

- image model อาจสะกดไทยหรือทำจำนวน region ผิด จึงต้องใช้ verified blueprint และ deterministic text placement เมื่อทำได้
- ไม่เหมาะกับคำตอบยาว
- ถ้าจำนวนข้อสูงมาก ต้อง paginate แทนการย่อข้อความ
- รูปทรงบางชนิดไม่ tessellate แบบบริสุทธิ์ได้ทุกกรณี Gem อาจใช้ cell-based approximation แต่ต้องแจ้งใน blueprint

## หลักสำคัญ

```text
CORRECTNESS
> MAPPING
> SHAPE GRAMMAR
> TOPOLOGY QUALITY
> READABILITY
> THEME
> DECORATION
```
