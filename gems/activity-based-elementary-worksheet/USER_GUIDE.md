# คู่มือสำหรับครู — Activity-Based Elementary Worksheet Generator

Version: 2.3.0
Status: Teacher-facing guide aligned with production prompt-generator baseline

## Gem นี้ทำอะไร

Gem นี้มีหน้าที่ **สร้าง Prompt สำหรับใบงาน** ไม่ใช่จำเป็นต้องสร้างภาพใบงานเอง

ครูบอกความต้องการด้วยภาษาธรรมดา แล้ว Gem จะ:

- วิเคราะห์ระดับชั้น/เรื่อง/จำนวนข้อ;
- เลือก Domain Engine ที่เหมาะสม;
- สร้างและตรวจโจทย์/คำตอบภายในแบบ deterministic เมื่อทำได้;
- แยกคำตอบภายในออกจากสิ่งที่จะพิมพ์ให้นักเรียน;
- คำนวณ geometry/ขีด/เข็ม/ระดับของมาตรวัดที่เป็นข้อมูลการเรียน;
- วางแผน A4 และพยายามจัด 1 หน้าเป็นอันดับแรก;
- เลือก render-path ที่เหมาะกับงาน;
- สร้าง `FINAL_IMAGE_GENERATION_PROMPT` ที่พร้อม COPY ไปสั่ง AI สร้างภาพอื่นได้ทันที.

แนวคิดหลัก:

`คำสั่งครู → ตรวจเนื้อหา → ตรวจ geometry → วาง layout → compile prompt → QA → prompt พร้อมใช้`

## บอกเพียง 3 อย่างก็เริ่มได้

โดยทั่วไปครูระบุเพียง:

1. ระดับชั้น
2. เรื่อง/ทักษะ
3. จำนวนข้อ

ตัวอย่าง:

> ป.3 การอ่านตราชั่ง 10 ข้อ

> ป.3 อ่านนาฬิกาเข็ม 10 ข้อ

> ป.3 หาระยะเวลาจากเวลาเริ่มต้นและเวลาสิ้นสุด 10 ข้อ

Gem จะเติมค่าที่ปลอดภัยจาก policy/domain ให้อัตโนมัติ

## Output ที่ควรได้รับ

ค่าเริ่มต้นคือ `PROMPT_PACKAGE` 6 ส่วน:

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

**ส่วนที่ 6 คือผลลัพธ์หลัก**

ครูสามารถคัดลอกเฉพาะ `FINAL_IMAGE_GENERATION_PROMPT` แล้วนำไปสั่ง AI สร้างภาพได้เลย โดยไม่ควรต้องรวมข้อความจากส่วนอื่นเอง

## สิ่งที่ Final Prompt ต้องมี

Final Prompt ที่ผ่าน production QA ต้องระบุครบอย่างน้อย:

- A4 / orientation / ขาวดำหรือสี;
- ระดับชั้น วิชา เรื่อง และจุดประสงค์;
- จำนวนข้อที่แน่นอน;
- หัวกระดาษ ชื่อ-ชั้น-เลขที่;
- คำชี้แจงและข้อความที่นักเรียนเห็นจริง;
- layout ที่ชัดเจน เช่น 2×5 หรือ table 10 rows;
- ช่องตอบที่เว้นว่าง;
- รายละเอียดภาพ/มาตรวัดของ **แต่ละข้อ**;
- geometry/tick topology ที่จำเป็น;
- ขนาดขั้นต่ำของเครื่องมือ;
- theme/art style;
- hard negatives เช่น ห้ามเฉลย ห้ามตัดขอบ ห้ามเพิ่มโจทย์;
- downstream `RENDER_PATH` guidance.

## ห้าม Final Prompt หยุดที่ placeholder

สิ่งต่อไปนี้อาจใช้เป็น intermediate blueprint ได้ แต่ **ไม่ใช่ Final Prompt ที่พร้อมใช้**:

> `[ภาพหน้าปัดนาฬิกา: เข็มสั้นชี้เลข 3]`

> `[ใส่รูปตราชั่ง]`

> `<draw clock>`

> `TBD`

> `ทำข้ออื่นเหมือนตัวอย่างด้านบน`

Final Prompt ต้องแปลง placeholder เหล่านี้เป็น renderer-ready instructions ก่อนส่งให้ครู

## งานภาพซ้ำหลายข้อ

ถ้ามีหน้าปัด/มาตรวัด 10 ข้อ ระบบควรใช้โครงสร้าง:

`CANONICAL TEMPLATE + ITEM 1 STATE + ITEM 2 STATE + ... + ITEM 10 STATE`

เช่น นาฬิกา:

- template: วงกลมจริง, pivot กลาง, เลข 1–12, เข็มยาว/สั้นตามกฎ;
- item state: ตำแหน่งเข็มของแต่ละข้อ.

ตราชั่ง:

- template: active sweep, inactive gap, จำนวน interval/tick ที่ถูกต้อง;
- item state: ตำแหน่งเข็มแต่ละข้อ.

ไม้บรรทัด/เทอร์โมมิเตอร์/ภาชนะตวงก็ใช้หลักเดียวกัน

## เครื่องมือวัด = ข้อมูลทางการเรียน

ถ้าเด็กต้องอ่านนาฬิกา ตราชั่ง ไม้บรรทัด เทอร์โมมิเตอร์ หรือภาชนะตวง รูปร่าง สเกล ขีด เข็ม ระดับ และตำแหน่งต่าง ๆ เป็น academic data

ขีดหาย/เกิน/ซ้ำหรืออยู่ผิดบริเวณไม่ใช่ข้อผิดพลาดตกแต่ง แต่เป็นความผิดพลาดทางการเรียน

กฎกลาง:

`EXPECTED_INTERVAL_COUNT = (MAX - MIN) / MINOR_INTERVAL`

สำหรับ linear endpoint-inclusive scale:

`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

ตัวอย่าง:

- 1 ซม. ที่ละเอียด 1 มม. = 10 intervals / 11 positions;
- เทอร์โมมิเตอร์ 0–50°C ขีดละ 1°C = 50 / 51;
- ภาชนะ 0–1000 mL ขีดละ 100 mL = 10 / 11;
- นาฬิกาเป็น cyclic topology: 60 minute intervals / 60 distinct positions.

## One-page-first

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

Gem จะพยายามออกแบบ prompt ให้ลง A4 หน้าเดียวก่อน โดยไม่ลดความถูกต้อง ขนาดมาตรวัด ความอ่านง่าย หรือพื้นที่เขียนตอบ

ถ้าครูสั่ง `A4 หน้าเดียวเท่านั้น` จะใช้ `ONE_PAGE_LOCK=ON` และถ้าจัดอย่างปลอดภัยไม่ได้ Gem ต้อง FAIL feasibility แทนการบีบจนอ่านไม่ได้

## Render path คือคำแนะนำให้ AI ปลายทาง

- `DOCUMENT_FIRST` — งานข้อความ/ตาราง/ตัวเลขมาก ให้รักษา text/table แบบ deterministic เป็นหลัก
- `HYBRID` — แยก deterministic text/geometry ออกจาก generative theme art
- `DETERMINISTIC_VECTOR` — geometry สำคัญมาก ให้ใช้รูปทรง/vector ที่แน่นอน
- `IMAGE_ONLY` — ใช้เมื่อความเสี่ยงต่อข้อมูลต่ำหรือผู้ใช้ระบุ และต้องตรวจภาพหลังสร้าง

Gem เองยังคงส่งออกเป็น Prompt Package ไม่ว่าจะเลือก render path ใด

## ไม่มีเฉลย

เมื่อ `SHOW_ANSWER_KEY=NO`:

- ช่องตอบของนักเรียนต้องว่าง;
- ห้ามมีเฉลย/answer list;
- ห้าม QA prose เปิดเผยคำตอบ;
- renderer-only geometry สามารถอยู่ใน prompt เพื่อวาดภาพถูกต้องได้ แต่ห้ามพิมพ์เป็นคำตอบบนใบงาน.

## ตัวอย่างคำสั่ง

> ป.3 อ่านนาฬิกาเข็มชั่วโมงเต็ม 10 ข้อ A4 ขาวดำ ไม่มีเฉลย ธีมชีวิตประจำวัน

> ป.3 อ่านตราชั่ง 0–5 กก. 10 ข้อ ขีดละ 0.1 กก. ตอบเป็นกิโลกรัมและขีด ขาวดำ ไม่มีเฉลย

> ป.3 อ่านไม้บรรทัด 10 ข้อ ซม.และมม. ธีมเครื่องเขียน

> ป.3 อ่านเทอร์โมมิเตอร์ 10 ข้อ °C ขาวดำ

> ป.3 อ่านระดับน้ำจากภาชนะตวง 10 ข้อ 0–1000 mL

> ป.3 หาระยะเวลาจากเวลาเริ่มต้นและเวลาสิ้นสุด 10 ข้อ ชั่วโมงเต็ม

## การขอแก้งาน

สั่งได้ตามภาษาปกติ เช่น:

> เปลี่ยนธีมเป็นอวกาศ แต่ห้ามเปลี่ยนโจทย์

> ทำให้เป็น A4 หน้าเดียวเท่านั้น

> เปลี่ยนเป็นแนวนอน แต่ใช้ข้อมูลเดิม

> ทำให้ยากขึ้น

Gem ต้องแก้ canonical state ก่อน แล้ว compile Final Prompt ใหม่ ไม่ควร patch เฉพาะคำปลายทางแบบขัดกับข้อมูลเดิม

## เกณฑ์ Prompt พร้อมใช้

ก่อนส่ง Final Prompt ต้องผ่านอย่างน้อย:

`PROMPT_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`PLACEHOLDER_VISUAL_QA`
`VISIBLE_OUTPUT_SANITIZER_QA`
`ANSWER_LEAK_QA`

รวมทั้ง domain-specific QA ที่เกี่ยวข้อง

จำง่าย ๆ:

> **Final Prompt ต้องถูกต้อง + ครบ + ปลอด placeholder + copy ไปใช้ได้ทันที**

ภาพที่ AI ปลายทางสร้างยังควรตรวจอีกครั้งก่อนใช้จริง โดยเฉพาะใบงานมาตรวัด เพราะ third-party renderer อาจวาด geometry ผิดแม้ prompt ถูกต้อง.