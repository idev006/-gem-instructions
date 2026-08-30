# คู่มือสำหรับครู — Activity-Based Elementary Worksheet Generator

Version: 2.6.0-LTS
Status: Teacher-facing guide for Orchestrator + Specialist Worker baseline

## Gem นี้ทำอะไร

Gem นี้มีหน้าที่หลักคือ **สร้าง Prompt สำหรับใบงาน** ที่ตรวจเนื้อหาและข้อกำหนดก่อนส่งต่อให้ AI สร้างภาพ ไม่ใช่รับประกันว่าภาพปลายทางถูกต้องโดยอัตโนมัติ

ครูบอกเพียงระดับชั้น เรื่อง/ทักษะ และจำนวนข้อเป็นหลัก เช่น:

- `ป.3 อ่านนาฬิกาเข็ม 10 ข้อ`
- `ป.3 อ่านไม้บรรทัด เซนติเมตรและมิลลิเมตร 10 ข้อ`
- `ป.4 คำนวณระยะทางไปกลับ 10 ข้อ`
- `ป.3 อ่านตราชั่ง 0–5 กก. ขีดละ 0.1 กก. 10 ข้อ`
- `ป.4 แปลงลิตรกับมิลลิลิตร 10 ข้อ`

Gem จะ normalize คำสั่ง, route ไปยัง Specialist Worker, ตรวจค่าภายใน, วาง layout และสร้าง `FINAL_IMAGE_GENERATION_PROMPT` ที่ copy ไปใช้ได้ทันที

## สถาปัตยกรรมแบบใหม่

Main Instructions ทำหน้าที่เป็น **Orchestrator** ส่วน Knowledge 9 ไฟล์เป็น Specialist Workers:

1. W01 — คณิตศาสตร์ทั่วไป / color-by-code / ภาษาไทย
2. W02 — เวลาและนาฬิกา
3. W03 — น้ำหนักและตราชั่ง
4. W04 — ไม้บรรทัด ความยาว ระยะทาง และการแปลงหน่วย
5. W05 — อุณหภูมิ ความจุ ปริมาตร และเมนิสคัส
6. W06 — เงิน ปฏิทิน ตาราง/กราฟ
7. W07 — ตรวจ geometry/topology ของมาตรวัด
8. W08 — layout/render/ภาษาไทย/งานพิมพ์
9. W09 — QA/release

ช่อง Knowledge ที่ 10 เว้นไว้สำหรับ hotfix ขนาดเล็กในอนาคต เพื่อลดความจำเป็นในการติดตั้งทั้งชุดใหม่

## Measurement ที่รองรับอย่างเป็นทางการ

### เวลา
- อ่านนาฬิกาเข็ม
- ชั่วโมงเต็ม/ครึ่งชั่วโมง/ช่วง 15, 5, 1 นาทีตามระดับ
- กลางวัน/กลางคืน
- เวลาเริ่มต้น + ระยะเวลา → เวลาสิ้นสุด
- เวลาสิ้นสุด − ระยะเวลา → เวลาเริ่มต้น
- เวลาเริ่ม/สิ้นสุด → ระยะเวลา
- ตารางเวลาและการเปรียบเทียบเวลา

### ความยาวและไม้บรรทัด
- อ่านไม้บรรทัดจาก 0
- อ่านจากจุดเริ่มที่ไม่ใช่ 0
- mm / cm / m / km
- บวก ลบ หาผลต่าง เปรียบเทียบ
- แปลงหน่วย

### ระยะทาง
- ระยะทางรวม
- ไป-กลับ
- หลายช่วง
- เปรียบเทียบเส้นทาง
- m/km conversion

Gem จะไม่แอบเปลี่ยนโจทย์ระยะทางให้เป็นเรื่องความเร็ว ถ้าไม่ได้ขอ

### น้ำหนัก
- อ่านตราชั่ง
- kg / g / kg+g / kg+ขีด
- บวก ลบ เปรียบเทียบ แปลงหน่วย
- `1000 g = 1 kg`
- บริบทไทยที่เกี่ยวข้อง: `1 ขีด = 100 g = 0.1 kg`

### ปริมาตร/ความจุ
- อ่านภาชนะตวง
- mL / L
- บวก ลบ เปรียบเทียบ แปลงหน่วย
- meniscus เมื่อระบุ
- ปริมาตรทรงสี่เหลี่ยมมุมฉาก
- รูปทรงประกอบจากทรงสี่เหลี่ยมมุมฉากแบบง่ายเมื่อเหมาะกับระดับ

## Grade progression ป.1–ป.6

Gem มี `CURRICULUM_PROFILE=AUTO` ซึ่งใช้ progression แบบอนุรักษ์นิยมจาก `domains/MEASUREMENT_COVERAGE_P1_P6.md` ไม่ได้ถือว่าโรงเรียนทุกแห่งใช้ลำดับเดียวกัน

โดยสรุป:

- ป.1: เปรียบเทียบ/อ่านหน่วยง่าย ไม่เน้น conversion ซับซ้อน
- ป.2: อ่านมาตรวัดพื้นฐานและคำนวณหนึ่งขั้น
- ป.3: cm/mm, kg/ขีด, mL/L, duration และระยะทางพื้นฐาน
- ป.4: mixed units, nonzero ruler start, multi-segment distance, conversion แบบจำนวนเต็ม
- ป.5: mixed/decimal units เมื่อเหมาะสม, rectangular-prism volume
- ป.6: multi-step measurement reasoning และ composite rectangular-prism volume แบบง่าย

ครูสามารถกำหนดความยาก/หน่วย/ชนิดโจทย์เองได้เสมอ

## Output มาตรฐาน

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

ส่วนที่ 6 คือผลลัพธ์หลัก

## Student Blueprint กับข้อมูล renderer ต่างกัน

Student Blueprint ต้องมีเฉพาะสิ่งที่เด็กเห็นจริง จึงไม่ควรมี target time, target weight, angle, tick index หรือ liquid level

แต่ Final Prompt สามารถมีข้อมูลเหล่านี้เพื่อสั่ง AI วาดภาพให้ถูก โดยจะถูกทำเครื่องหมาย:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT`

## เครื่องมือวัด = ข้อมูลทางการเรียน

กฎกลางของ linear scale:

`EXPECTED_INTERVAL_COUNT=(MAX-MIN)/MINOR_INTERVAL`

`EXPECTED_TICK_POSITION_COUNT=EXPECTED_INTERVAL_COUNT+1`

ตัวอย่างสำคัญ:

- ไม้บรรทัด 1 cm @1 mm = 10 intervals / 11 positions
- นาฬิกา 10:30 → เข็มนาที 180°, เข็มชั่วโมง 315°, กึ่งกลาง 10–11
- ตราชั่ง 0–5 kg canonical → 300° active + 60° inactive gap
- thermometer แบบ discrete → endpoint ต้องตรงขีดที่แทนค่าได้จริง

## One-page-first

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

Gem จะพยายามหนึ่งหน้าก่อน แต่ไม่ยอมแลกกับความถูกต้อง ขนาดมาตรวัด ความอ่านง่าย หรือพื้นที่เขียนตอบ

ถ้าครูสั่ง `A4 หน้าเดียวเท่านั้น` แล้วทำอย่างปลอดภัยไม่ได้ Gem ต้องแจ้ง feasibility FAIL แทนการบีบจนผิด

## Prompt QA ไม่ใช่ Artifact QA

เมื่อ Gem สร้าง prompt เสร็จ สามารถรายงาน `PROMPT_RELEASE=APPROVED` ได้หาก prompt ผ่าน

แต่ก่อนตรวจภาพจริงต้องยังเป็น:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

ภาพปลายทาง โดยเฉพาะนาฬิกา ตราชั่ง ไม้บรรทัด เทอร์โมมิเตอร์ และภาชนะตวง ต้องตรวจ visual artifact ก่อนใช้กับเด็ก

## ตรวจสุขภาพ Gem

หลังติดตั้งหรือสงสัยว่า Knowledge ขาด ให้พิมพ์:

`ตรวจสุขภาพ Gem`

Gem จะตรวจ baseline, W01–W09, schema, route, visibility model, render-path rule และสถานะ hotfix โดยไม่ต้องสร้างใบงาน

## จำง่าย ๆ

> Gem ต้องสร้าง Prompt ที่ **ถูกต้อง + worker ถูกตัว + หน่วยถูก + student-safe + geometry ชัด + copy-ready** และต้องไม่อ้างว่าภาพจริงผ่านก่อนเห็นภาพจริง