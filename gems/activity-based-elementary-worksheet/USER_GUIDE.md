# คู่มือสำหรับครู — Activity-Based Elementary Worksheet Generator

Version: 2.6.3-LTS
Status: Teacher-facing guide for Orchestrator + 10 Specialist Workers

## Gem นี้ทำอะไร

Gem นี้สร้าง **Prompt สำหรับใบงาน** ที่ตรวจเนื้อหา เครื่องมือวัด layout และข้อกำหนดก่อนส่งต่อให้ระบบสร้างภาพ ไม่รับประกันว่าภาพปลายทางถูกต้องโดยอัตโนมัติจนกว่าจะตรวจ artifact จริง

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

เมื่อเด็กต้องอ่านเครื่องมือวัด route คือ:

`OWNING WORKER → W07 → W10 → W08 → W09`

## Five safety profiles

ระบบใช้ shared profiles 5 ชุด:

- System-Wide Quality
- Scale-Line Integrity
- Instrument Review–Revise
- Metrology Assurance
- Physical Page Feasibility

หลักสำคัญ:

`ONE WRONG INSTRUCTIONAL SCALE = RELEASE BLOCKER`

`NO NUMERIC PACKING PROOF = NO PAGE-FEASIBILITY PASS`

## เครื่องมือวัด = เนื้อหาการเรียน

### ไม้บรรทัด
1 cm @1 mm ต้องมี 10 intervals /11 positions /9 interior positions และขอบไม้บรรทัดไม่ใช่ขีดเพิ่ม

### ตราชั่ง 0–5 kg
Canonical classroom template:

- 0 อยู่ด้านบน
- ค่าเพิ่มตามเข็มนาฬิกา
- 0,1,2,3,4,5 อยู่ที่ 0°,60°,120°,180°,240°,300°
- 50 intervals /51 positions
- gap 60° ระหว่าง 5→0 ต้องไม่มีขีดหรือเส้น radial ที่ดูเหมือนสเกล
- จุดหมุนเข็มต้องตรงศูนย์กลางหน้าปัดจริง

### Speedometer 0–120 km/h
- 12 intervals /13 positions
- active 240° / inactive 120°
- `target_angle=(240+2*speed) mod 360`
- 60 km/h ชี้ตรงขึ้นบนตาม coordinate convention ของ engine
- จุดปักเข็ม = ศูนย์กลาง arc/ring และเข็มต้องเป็น radial line จริง

### Thermometer 0–50°C @1°C
- 50 intervals /51 positions
- major: 0,10,20,30,40,50 =6
- intermediate: 5,15,25,35,45 =5
- ordinary minor =40
- ทุกช่วง 10°C มี 10 intervals /9 interior positions
- ปลายของเหลวต้องตรงขีดเป้าหมาย

### Protractor 0–180° @1°
สำหรับใบงานอ่านมุมพื้นฐาน:

- ใช้ perfect upper semicircle
- 180 intervals /181 positions
- 0° ด้านขวา, 90° ด้านบน, 180° ด้านซ้าย
- single active numeric scale เป็น default
- 10° major /5° intermediate /1° minor
- center ของ arc = midpoint ของ baseline = origin ของ ray
- ทุก tick/ray เป็น radial จาก center เดียวกัน
- ห้าม ellipse, skew, shear, perspective หรือ non-uniform stretch
- width ขั้นต่ำ 70 mm ที่ spacing floor 0.60 mm

Dual-scale ใช้เฉพาะเมื่อ **จุดประสงค์การเรียนคือการเลือกอ่านสเกลคู่โดยตรง** เท่านั้น ไม่ใช่ default ของใบงานอ่านมุมพื้นฐาน

## Page layout

Default:

`ONE_PAGE_PREFERRED=YES`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_LOCK=OFF`

หนึ่งหน้าเป็นเพียง preference ไม่ใช่คำสั่งบังคับ ระบบต้องคำนวณพื้นที่จริงก่อน

Shape-aware rule:

- วงกลม diameter D ใช้พื้นที่ตัวเครื่อง D×D
- protractor ครึ่งวงกลม width W มี body height W/2 ก่อนเพิ่ม label/answer space
- thermometer ใช้ selected vertical scale length จริง

ดังนั้น protractor กว้าง 70 mm มี semicircle body สูง 35 mm ไม่ใช่ 70 mm

ถ้า layout ที่ต้องการไม่พอดีและ lock=OFF ให้ paginate ไม่ลดขีด ไม่ย่อจนอ่านไม่ได้ และไม่ตัดพื้นที่ตอบ

## Output มาตรฐาน

1. `NORMALIZED_WORKSHEET_SPEC`
2. `STUDENT_CONTENT_BLUEPRINT`
3. `LAYOUT_BLUEPRINT`
4. `RENDER_CONSTRAINTS`
5. `QA_REPORT`
6. `FINAL_IMAGE_GENERATION_PROMPT`

ส่วนที่ 6 ต้อง copy-ready ด้วยตัวเอง

## Student Blueprint กับ renderer metadata

Student Blueprint มีเฉพาะสิ่งที่เด็กเห็นจริง ห้ามมี target answer, tick index, ray angle, needle angle, liquid level หรือ W07/W10 audit data

ข้อมูลจำเป็นสำหรับการวาดอยู่ใน renderer metadata และทำเครื่องหมาย:

`RENDER_ONLY_NOT_FOR_WORKSHEET — USE TO DRAW; DO NOT PRINT AS TEXT`

## Renderer review loop

ทุกเครื่องมือวัดต้องมี:

`NO_FIRST_PASS_RELEASE_FOR_LEARNER_READ_INSTRUMENTS=ON`

และ:

`GENERATE → SELF_REVIEW → VERIFY_AGAINST_CANONICAL_STATE → REVISE_IF_NEEDED → RECHECK → FINALIZE_ONLY_IF_PASS`

ต้องนับขีด ตรวจ center/origin, label order, target alignment, shape integrity และ gap จริง ไม่ใช่เพียง `looks correct`

## Prompt QA ไม่ใช่ Artifact QA

แม้ prompt ผ่าน:

`PROMPT_RELEASE=APPROVED`

ก่อนตรวจภาพจริงยังต้องเป็น:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

ภาพจริงที่มีขีดผิด ตัวเลขเรียงผิด จุดปักเข็มเยื้อง หรือโปรแทรกเตอร์เบี้ยว ต้อง `ARTIFACT_QA=FAIL` และนำ defect กลับมาเป็น permanent regression
