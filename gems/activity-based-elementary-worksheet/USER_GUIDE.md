# คู่มือสำหรับครู — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
Status: Teacher-facing guide for Orchestrator + 10 Specialist Workers

## Gem นี้ทำอะไร

Gem นี้สร้าง **Prompt สำหรับใบงานระดับประถม** โดยตรวจทั้งเนื้อหา เครื่องมือวัด layout ความเหมาะสมกับวัย พื้นที่เขียน และข้อกำหนดก่อนส่งต่อให้ระบบสร้างภาพ ไม่รับประกันว่าภาพปลายทางถูกต้องโดยอัตโนมัติจนกว่าจะตรวจ Artifact QA จริง

ตัวอย่างคำสั่ง:
- `ป.3 อ่านนาฬิกาเข็ม 10 ข้อ`
- `ป.3 อ่านไม้บรรทัด เซนติเมตรและมิลลิเมตร 10 ข้อ`
- `ป.3 อ่านตราชั่ง 0–5 กก. ขีดละ 0.1 กก. 10 ข้อ`
- `ป.4 อ่านหน้าปัดความเร็วรถ 0–120 km/h ขีดละ 10 km/h 10 ข้อ`
- `ป.4 อ่านมุมจากโพรแทรกเตอร์ 0–180° ขีดละ 1° 10 ข้อ`
- `ป.4 อ่านเทอร์โมมิเตอร์ 0–50°C ขีดละ 1°C 10 ข้อ`
- `ป.4 อ่านปริมาตรจากภาชนะตวง 0–1000 mL ขีดละ 50 mL 10 ข้อ`
- `ป.4 อ่านกราฟแท่งที่แกนตั้งเพิ่มทีละ 5 จำนวน 10 ข้อ`

## สถาปัตยกรรม

Main Instructions เป็น Orchestrator และมี Knowledge Worker 10 ไฟล์:
1. W01 — คณิตศาสตร์ทั่วไป / color-by-code / ภาษาไทย
2. W02 — เวลาและนาฬิกา
3. W03 — น้ำหนักและตราชั่ง
4. W04 — ไม้บรรทัด ความยาว ระยะทาง speedometer มุม/โพรแทรกเตอร์ รอบรูป พื้นที่
5. W05 — อุณหภูมิ ความจุ เมนิสคัส ปริมาตร
6. W06 — เงิน ปฏิทิน ตาราง/กราฟ
7. W07 — ตรวจ geometry/topology
8. W08 — layout/render/ภาษาไทย/งานพิมพ์
9. W09 — QA/release
10. W10 — วิศวกร metrology ตรวจซ้ำอย่างอิสระ

เมื่อเด็กต้องอ่านเครื่องมือวัด:
`OWNING WORKER → W07 → W10 → W08 → W09`

## Safety profiles

ระบบใช้ technical safety profiles 5 ชุด:
- System-Wide Quality
- Scale-Line Integrity
- Instrument Review–Revise
- Metrology Assurance
- Physical Page Feasibility

และใช้ learner-facing profile อีก 1 ชุดกับทุกใบงาน:
- Primary-School Worksheet Pedagogy & Usability

หลักสำคัญ:
`ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER`
`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`
`PHYSICAL_FIT != PRIMARY_LEARNER_USABILITY`

## ค่าเริ่มต้นสำหรับเด็กประถม

ถ้าครูไม่ได้ระบุขนาด/แนวกระดาษ ระบบใช้ **A4 แนวตั้ง** ทุกหน้า

ค่าการอ่านง่ายสำหรับงานพิมพ์:
- ป.1–ป.3: ตัวเนื้อหาตั้งเป้าอย่างน้อย 14 pt
- ป.4–ป.6: ตัวเนื้อหาตั้งเป้าอย่างน้อย 12 pt
- หัวเรื่องหลักอย่างน้อย 18 pt
- ตัวเลขบนเครื่องมือ/กราฟที่เด็กต้องอ่าน ตั้งเป้าอย่างน้อย 12 pt
- พื้นที่เขียนต่อบรรทัด ป.1–ป.3 สูงอย่างน้อย 8 mm; ป.4–ป.6 อย่างน้อย 6 mm

ถ้าหน้าเดียวแน่นเกินไป ระบบควรลดของตกแต่งก่อน แล้วแบ่งหน้า A4 แนวตั้ง ไม่ลดขนาดสิ่งสำคัญจนอ่านยาก

## Academic geometry ต้อง deterministic

เครื่องมือวัดที่เด็กต้องอ่านใช้หลัก:
`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`

ระบบภาพอิสระใช้ทำ illustration/decoration ได้ แต่ **ห้ามวาดสเกล เข็ม ขีด รังสี แกน หรือระดับของเหลวแทน geometry ที่คำนวณไว้**

อนุญาตให้ย้าย/ย่อ-ขยาย geometry ทั้งชุดแบบ uniform เท่านั้น ไม่บิด/skew/stretch รายส่วน

## เครื่องมือวัด = เนื้อหาการเรียน

### นาฬิกา
เข็มชั่วโมงต้องเคลื่อนต่อเนื่องตามนาที
`hour_angle=30*(h mod 12)+0.5*m`
และใช้ exact vector endpoint เพื่อป้องกันการ snap เช่น 3:30 ต้องอยู่ครึ่งทาง 3→4 ไม่ชี้เลข3ตรง ๆ

### ไม้บรรทัด
1cm @1mm =10 intervals/11 positions/9 interior positions; ขอบไม้บรรทัดไม่ใช่ขีด0 ถ้าตำแหน่งไม่ตรงกัน

โจทย์วัดวัตถุใช้เส้นประแนวดิ่งจากหัว/ท้ายวัตถุลงสู่ graduation ที่ตรงกัน

### ตราชั่ง 0–5kg @0.1kg
- 0 ด้านบน ค่าเพิ่มตามเข็มนาฬิกา
- 50 intervals/51 active positions
- **ทุก 1kg มี 10 ช่องเท่ากันและ 9 ขีดภายใน**
- ขีดที่ 5 หรือ +0.5kg ยาวกว่าขีดย่อยทั่วไป แต่สั้น/อ่อนกว่าขีดเลขเต็ม
- renderer ต้องได้รับรายการตำแหน่งขีดจริง ไม่ใช่เพียงคำว่า `10 divisions`
- gap5→0 ไม่มีขีด radial
- จุดหมุนเข็มตรงศูนย์กลาง

### Speedometer
0–120km/h @10 =12 intervals/13 positions; active240°/gap120°; pivot=center; เข็ม radial

### Thermometer
0–50°C @1°C =50/51; major6 + intermediate5 + minor40; ทุก10°C มี10 intervals/9 interior; ปลายของเหลวตรงขีด

### Protractor
0–180° @1° ใช้ perfect upper semicircle,180/181,single active scale เป็น default,0ขวา/90บน/180ซ้าย,common origin,ทุก tick/ray radial,ห้ามบิดรูป

### Graduated container
0–1000mL @50mL:20/21 globally; ทุก100mL มี2 intervals และขีดกลาง +50mL เพียงหนึ่งขีด

### Graph
สร้าง dataset ก่อน แล้ววาดกราฟ 2D จากข้อมูล canonical; แกนต้องเท่ากันจริงและ bar endpoint ตรงค่า

## Page layout

Default:
`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`
`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

หน้าเดียวเป็น preference ไม่ใช่คำสั่งบังคับ ต้องคำนวณพื้นที่จริงและตรวจความเหมาะสมกับเด็กด้วย

## Student Blueprint กับ renderer metadata

Student Blueprint มีเฉพาะสิ่งที่เด็กเห็นจริง ห้ามมี target answer, tick index, angle, liquid level หรือ W07/W10 audit data

ข้อมูลวาดภาพใช้ `RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT`

## Renderer review loop

ทุกเครื่องมือวัดต้องมี:
`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

ต้องนับขีด ตรวจ center/origin, label order, target alignment, vector manifest, shape integrity และ gap จริง ไม่ใช่เพียง `looks correct`

## Prompt QA ไม่ใช่ Artifact QA

แม้ prompt ผ่าน ก่อนตรวจภาพจริงยังต้องเป็น:
`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

Artifact QA ต้องตรวจทั้ง metrology และ `ARTIFACT_LEARNER_SIMULATION_QA`: เด็กต้องมองเห็นว่าโจทย์ให้ทำอะไร ต้องอ่านตรงไหน และเขียนตรงไหน โดยคำตอบต้องอนุมานได้จากข้อมูลที่เด็กเห็นเท่านั้น

ภาพจริงที่มีขีดผิด ตัวเลขผิด จุดหมุนผิด ตัวหนังสืออ่านไม่ได้ พื้นที่ตอบไม่พอ หรือมีความกำกวม ต้อง `ARTIFACT_QA=FAIL` และนำ defect กลับมาเป็น permanent regression
