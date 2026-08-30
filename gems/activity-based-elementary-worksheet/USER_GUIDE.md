# คู่มือสำหรับครู — Activity-Based Elementary Worksheet Generator

Version: 2.3.2
Status: Teacher-facing guide aligned with production prompt-generator baseline

## Gem นี้ทำอะไร

Gem นี้มีหน้าที่ **สร้าง Prompt สำหรับใบงาน** ไม่ใช่สร้างภาพใบงานเองเป็นค่าเริ่มต้น

ครูบอกความต้องการด้วยภาษาธรรมดา แล้ว Gem จะ:

- วิเคราะห์ระดับชั้น/เรื่อง/จำนวนข้อ;
- route ไปยัง Domain Engine ที่ถูกต้อง;
- สร้างและตรวจโจทย์/คำตอบภายในแบบ deterministic เมื่อทำได้;
- แยกคำตอบภายในออกจากสิ่งที่เด็กเห็น;
- คำนวณ geometry/ขีด/เข็ม/ระดับของมาตรวัดที่เป็นข้อมูลการเรียน;
- วางแผน A4 และพยายามจัด 1 หน้าเป็นอันดับแรก;
- เลือก render-path ที่เหมาะกับ downstream AI;
- สร้าง `FINAL_IMAGE_GENERATION_PROMPT` ที่พร้อม COPY ไปสั่ง AI สร้างภาพอื่นได้ทันที.

แนวคิดหลัก:

`คำสั่งครู → route KB/domain → ตรวจเนื้อหา → ตรวจ geometry → วาง layout → compile prompt → QA → prompt พร้อมใช้`

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

**ส่วนที่ 6 คือผลลัพธ์หลัก** และต้องสามารถ copy ไปใช้เดี่ยว ๆ ได้

## Final Prompt ต้องมีอะไร

อย่างน้อยต้องมี:

- A4 / orientation / color mode;
- ระดับชั้น วิชา เรื่อง จุดประสงค์;
- จำนวนข้อแน่นอน;
- หัวกระดาษ ชื่อ-ชั้น-เลขที่;
- คำชี้แจงและข้อความนักเรียน;
- layout ชัดเจน;
- ช่องตอบว่าง;
- canonical visual/instrument template;
- รายละเอียดภาพ/มาตรวัดของ **ทุกข้อ**;
- geometry/tick topology และขนาดขั้นต่ำเมื่อเกี่ยวข้อง;
- theme/art style;
- hard negatives;
- downstream `RENDER_PATH` guidance;
- `RENDER_OBJECTIVE=STUDENT_WORKSHEET`.

## ห้าม Final Prompt หยุดที่ placeholder

สิ่งเหล่านี้ใช้เป็น intermediate blueprint ได้ แต่ไม่ใช่ Final Prompt:

> `[ภาพหน้าปัดนาฬิกา: เข็มสั้นชี้เลข 3]`

> `[ใส่รูปตราชั่ง]`

> `<draw clock>`

> `TBD`

> `ทำข้ออื่นเหมือนตัวอย่างด้านบน`

Final Prompt ต้องแปลงเป็น renderer-ready instructions ก่อนส่งให้ครู

## เครื่องมือวัด = ข้อมูลทางการเรียน

ถ้าเด็กต้องอ่านนาฬิกา ตราชั่ง ไม้บรรทัด เทอร์โมมิเตอร์ หรือภาชนะตวง รูปร่าง สเกล ขีด เข็ม ระดับ และตำแหน่งต่าง ๆ เป็น academic data

กฎกลางสำหรับ linear endpoint-inclusive scale:

`EXPECTED_INTERVAL_COUNT = (MAX - MIN) / MINOR_INTERVAL`

`EXPECTED_TICK_POSITION_COUNT = EXPECTED_INTERVAL_COUNT + 1`

นาฬิกาเป็น cyclic topology: 60 minute intervals / 60 distinct positions

## Actual-render hardening

เนื่องจาก AI สร้างภาพอาจวาดภาพที่ดูสวยแต่ผิดทางวิชาการ Gem v2.3.2 กำหนดให้ visual item ที่เสี่ยงสูงต้องมี:

`SEMANTIC TARGET + EXACT INDEX/ANGLE/LEVEL + RELATIONAL WORDING + ITEM-SPECIFIC HARD NEGATIVE`

ตัวอย่าง:

- 10:30 → เข็มยาว 180°, เข็มสั้น 315°, กึ่งกลาง 10–11, ห้ามชี้ 10 ตรง ๆ;
- thermometer → liquid top ต้องตรง valid graduation, ห้ามอยู่ระหว่างขีดโดยไม่ได้ตั้งใจ;
- meniscus → ระบุ top/bottom read point ให้แน่นอน และห้าม target number หลุดเป็น annotation;
- ตราชั่ง 0–5 กก. → 300° active + 60° inactive gap, ห้าม full-circle 360° substitution.

## One-page-first

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

Gem จะพยายามออกแบบ prompt ให้ลง A4 หน้าเดียวก่อน โดยไม่ลดความถูกต้อง ขนาดมาตรวัด ความอ่านง่าย หรือพื้นที่เขียนตอบ

ถ้าสั่ง `A4 หน้าเดียวเท่านั้น` แล้วจัดอย่างปลอดภัยไม่ได้ Gem ต้อง FAIL feasibility แทนการบีบจนผิด

## Render path คือคำแนะนำให้ AI ปลายทาง

- `DOCUMENT_FIRST` — งานข้อความ/ตาราง/ตัวเลขมาก
- `HYBRID` — deterministic text/geometry + generative theme art
- `DETERMINISTIC_VECTOR` — geometry สำคัญมาก
- `IMAGE_ONLY` — ใช้เมื่อความเสี่ยงต่ำหรือผู้ใช้ระบุ และควรตรวจภาพหลังสร้าง

Gem เองยังคงส่งออก Prompt Package

## ไม่มีเฉลย = ต้องกัน 2 แบบ

เมื่อ `SHOW_ANSWER_KEY=NO`:

1. `ANSWER_LEAK_GUARD` — ห้ามเฉลย/answer vector/QA prose เปิดคำตอบ
2. `TARGET_VALUE_LEAK_GUARD` — target ที่ใช้ควบคุม geometry ห้ามกลายเป็น extra scale label, arrow annotation หรือ completed answer

## Knowledge Base ที่แนะนำ

ใช้ `GEM_INSTRUCTIONS_PRODUCTION.md` เป็น Instructions หลักของ Gem และอัปโหลด KB ตาม `KB_MANIFEST.md`

ไฟล์หลักที่ควรมี:

- `OUTPUT_CONTRACT.md`
- `KB_ROUTER.md`
- `KB_MANIFEST.md`
- `policies/PARAMETER_POLICY.md`
- `domains/DOMAIN_REGISTRY.md`
- domain engines ทั้งหมดที่ต้องการรองรับ
- `domains/INSTRUMENT_READING_ENGINE.md`
- QA/regression files ที่ manifest ระบุ

Gem จะ route ตาม `KB_ROUTER.md` ไม่ใช่เอากฎจากทุกไฟล์มาปนกันโดยไม่มีลำดับ

## การขอแก้งาน

สั่งได้ตามภาษาปกติ เช่น:

> เปลี่ยนธีมเป็นอวกาศ แต่ห้ามเปลี่ยนโจทย์

> ทำให้เป็น A4 หน้าเดียวเท่านั้น

> เปลี่ยนเป็นแนวนอน แต่ใช้ข้อมูลเดิม

> ทำให้ยากขึ้น

Gem ต้องแก้ canonical state ก่อนแล้ว compile Final Prompt ใหม่

## เกณฑ์ Prompt พร้อมใช้

ก่อนส่ง Final Prompt ต้องผ่านอย่างน้อย:

`KB_ROUTE_QA`
`KB_COMPATIBILITY_QA`
`PROMPT_QA`
`PROMPT_COMPLETENESS_QA`
`PROMPT_COPY_READY_QA`
`PLACEHOLDER_VISUAL_QA`
`VISIBLE_OUTPUT_SANITIZER_QA`
`ANSWER_LEAK_QA`
`TARGET_VALUE_LEAK_QA` เมื่อมี renderer-only target

รวมทั้ง domain-specific QA ที่เกี่ยวข้อง

จำง่าย ๆ:

> **Final Prompt ต้องถูกต้อง + ครบ + KB ถูกชุด + ไม่มี placeholder + ไม่มีเฉลย/target leak + copy ไปใช้ได้ทันที**

ภาพที่ AI ปลายทางสร้างยังต้องตรวจอีกครั้งก่อนใช้จริง โดยเฉพาะใบงานมาตรวัด เพราะ Prompt QA ไม่ใช่ Artifact QA.