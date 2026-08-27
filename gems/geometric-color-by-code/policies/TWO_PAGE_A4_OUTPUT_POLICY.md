# Two-Page A4 Output Policy

Version: 1.0.0
Status: Production policy

## Purpose

กำหนดรูปแบบ output มาตรฐานของ Geometric Color-by-Code ให้ใช้งานจริงในห้องเรียนได้สะดวก:

1. **หน้า 1 — Student Worksheet**: กระดาษ A4 แนวตั้ง 1 หน้า ขาว-ดำ ยังไม่ระบายสีในพื้นที่กิจกรรม
2. **หน้า 2 — Answer Key**: กระดาษ A4 แนวตั้ง 1 หน้า ระบายสีแล้วตาม verified mapping

ทั้งสองหน้าต้องมาจาก master geometry / verified content / verified mapping เดียวกัน

## Default production contract

```text
STUDENT_PAGE_SIZE = A4
STUDENT_ORIENTATION = PORTRAIT
STUDENT_PAGE_COUNT_TARGET = 1

ANSWER_KEY_PAGE_SIZE = A4
ANSWER_KEY_ORIENTATION = PORTRAIT
ANSWER_KEY_PAGE_COUNT_TARGET = 1

PAIR_PACKAGING = TWO_SEPARATE_A4_PAGES
STUDENT_PAGE_ORDER = 1
ANSWER_KEY_PAGE_ORDER = 2
SAME_PAGE_COMPARISON = NO
```

## Single-page density rule

เมื่อผู้ใช้ขอ 40–50 ข้อ/คำในใบงานหนึ่งหน้า ให้พยายามรักษา Student Worksheet ไว้ที่ 1 หน้า A4 แนวตั้งก่อน โดยใช้ลำดับการแก้ไขดังนี้:

1. ลด decoration ที่ไม่จำเป็น
2. ลด micro-detail
3. ใช้ region grouping ที่ประหยัดพื้นที่
4. ใช้ข้อความ/คำตอบแบบ atomic เมื่อเหมาะสม
5. ปรับ visual hierarchy และ negative space
6. ลดขนาด illustration supporting motifs ก่อนลดขนาดข้อความ

ห้ามแก้ด้วยการ:
- ทำตัวหนังสือเล็กจนอ่านยาก
- ทำเส้นบางจนพิมพ์แตก
- ทำช่องระบายสีเล็กเกินใช้งาน
- ลด safe margin จนไม่ print-safe

ถ้า 1 หน้าไม่สามารถผ่าน readability / colorability / print QA ได้จริง ให้ระบบรายงานว่า single-page constraint ไม่ผ่านและเสนอ pagination แทน แต่ห้ามอ้างว่า 1 หน้า production-ready ถ้า QA ไม่ผ่าน

## Answer-key page rule

Answer Key ต้องเป็น A4 Portrait แยกอีก 1 หน้าโดย default และต้อง:
- ใช้ geometry เดียวกับ Student
- ใช้ question IDs/text เดียวกัน
- ใช้ verified mapping เดียวกัน
- เติมสีแบบ deterministic
- ไม่เพิ่ม content จนทำให้ layout เปลี่ยน

เพิ่มได้เฉพาะ label `เฉลย` หรือ teacher-only annotation เล็กน้อยที่ไม่เปลี่ยน topology

## Packaging

ถ้าส่งเป็น PDF เดียว:

```text
Page 1 = Student Worksheet
Page 2 = Colored Answer Key
```

ถ้าส่งเป็นไฟล์แยก:

```text
<worksheet_id>_student_A4_portrait
<worksheet_id>_answer_key_A4_portrait
```

## Critical QA

PASS เมื่อ:
- Student = A4 Portrait 1 page
- Answer Key = A4 Portrait 1 page
- ไม่มี Student/Answer อยู่ใน canvas/page เดียวกัน
- Student main activity ยังไม่เติมสี
- Answer Key ใช้สีตรง verified mapping ทุก region
- topology/text/mapping identity ระหว่างสองหน้าตรงกัน
- 40–50 item single-page stress case ยังอ่านง่ายและระบายสีได้จริง หากระบบยืนยันว่า PASS

FAIL เมื่อ:
- รวม Student + Answer Key ในหน้าเดียวกันโดย default
- Answer Key เปลี่ยน composition เพื่อให้พอดี
- ลด text/stroke/cell usability เพื่อฝืน 1 หน้า
- claim single-page success ทั้งที่ print/readability QA ไม่ผ่าน

## Priority

```text
CORRECTNESS
> MAPPING INTEGRITY
> TWO-PAGE SEPARATION
> READABILITY
> COLORING USABILITY
> PRINT QUALITY
> SINGLE-PAGE DENSITY
> DECORATION
```
