# Geometric Color-by-Code — Golden Reference Standard

Version: 1.0.0
Status: Production quality policy

## Purpose

กำหนดเกณฑ์สำหรับภาพตัวอย่างที่ใช้เป็น **Golden Reference** ของ Gem โดยเน้นคุณภาพใช้งานจริง ไม่ใช่เพียงความสวยงาม

## Required gates

ภาพจะเป็น Golden Reference ได้เมื่อ PASS ทั้งหมด:

### Academic
- จำนวนข้อถูกต้อง
- คำตอบถูกต้อง
- mapping คำตอบ/code/สีถูกต้อง
- legend ไม่มี orphan entry
- answer key ตรง source เดียวกัน

### Geometry
- primary shape อ่านออกได้ทันที
- shape เป็น construction grammar จริง
- question regions ยังเป็นสมาชิกของ tiling grammar
- tile scale มีระบบและ transition สมเหตุสมผล
- ไม่มี major freeform object ที่แย่ง visual grammar

### Colorability
- ไม่มี sliver cell / needle-like cell ที่เล็กเกินระบาย
- ไม่มี region ที่ตีความขอบเขตไม่ได้
- shared border เป็นเส้นเดียวชัดเจน
- พื้นที่ระบายเหมาะกับระดับชั้น

### Line quality
- clean vector-like line
- no broken line
- no double stroke
- no fuzzy/sketch edge
- no hairline
- no accidental starburst junction
- stroke hierarchy ชัด: frame > silhouette > internal tile

### Text
- ภาษาไทยถูกต้อง
- glyph ไทยครบ
- สระ/วรรณยุกต์ไม่หายหรือชน
- โจทย์/ตัวเลขไม่ชน border

### Print
- A4/A3/etc. ตรงที่ resolved
- margin ปลอดภัย
- main artwork monochrome เมื่อ default
- สีจริงจำกัดไว้ใน legend เมื่อกำหนดเช่นนั้น
- ภาพยังอ่านดีเมื่อพิมพ์ขาว-ดำ

## Golden reference is not a fixed template

Golden Reference เป็น **quality target** ไม่ใช่ composition template ที่ต้องลอกทุกครั้ง

งานใหม่สามารถเปลี่ยน:
- theme
- primary shape
- number of questions
- color count
- layout composition

แต่ต้องรักษา quality gates เดียวกัน

## Reference comparison checklist

ก่อน promote candidate:
1. เส้นคมกว่า/เทียบเท่า reference หรือไม่
2. primary shape ชัดกว่า/เทียบเท่า reference หรือไม่
3. academic correctness 100% หรือไม่
4. colorability ดีพอสำหรับเด็กจริงหรือไม่
5. text อ่านง่ายและไม่ชนเส้นหรือไม่
6. visual hierarchy สะอาดหรือไม่
7. มี freeform drift หรือไม่
8. มี micro-detail ที่ไม่สร้างประโยชน์หรือไม่

ถ้าข้อใดเป็น critical fail ห้าม promote.
