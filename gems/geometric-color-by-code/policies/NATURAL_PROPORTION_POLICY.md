# Natural Proportion Policy

Version: 1.1.0
Status: Canonical companion policy for Geometric Color-by-Code v1.6.0

## Purpose
ใช้สัดส่วนและจังหวะที่ได้รับแรงบันดาลใจจากธรรมชาติช่วยจัด composition โดยไม่ลด correctness, mapping integrity, readability, colorability หรือ print quality

```text
CORRECTNESS
> READABILITY
> COLORING USABILITY
> LINE CLARITY
> GEOMETRIC GRAMMAR
> NATURAL HARMONY
> DECORATION
```

Natural proportion เป็น **composition guide** ไม่ใช่ข้อบังคับให้ทุกระยะ/มุมเป็นค่าทางคณิตศาสตร์ exact

## Supported parameters
```text
COMPOSITION_SYSTEM = AUTO | STANDARD | NATURAL_HARMONY | CUSTOM
GOLDEN_SECTION_GUIDE = AUTO | YES | NO
FIBONACCI_RHYTHM = AUTO | YES | NO
PHYLLOTAXIS_MODE = AUTO | OFF | GOLDEN_ANGLE_INSPIRED | RADIAL_SPIRAL
RADIAL_SYMMETRY = AUTO | OFF | LIGHT | HIGH
PETAL_COUNT_LOGIC = AUTO | NATURAL_PATTERN | USER_DEFINED
FOCAL_POINT_PLACEMENT = AUTO | CENTER | GOLDEN_SECTION | RULE_OF_THIRDS | CUSTOM
NATURAL_SCALE_HIERARCHY = YES | NO
NATURAL_PATTERN_STRENGTH = SUBTLE | MODERATE | STRONG
COMPOSITION_BALANCE = AUTO | SYMMETRIC | NATURAL_BALANCED
SYMMETRY_MODE = AUTO | BILATERAL | RADIAL | APPROXIMATE_NATURAL | NONE
QUESTION_FLOW = FOLLOW_VISUAL_RHYTHM | GRID | CUSTOM
QUESTION_DISTRIBUTION_BALANCE = REQUIRED | RELAXED
```

## Golden section
- ใช้ช่วยวาง focal hierarchy/พื้นที่หลัก
- ใช้ช่วยกำหนดสัดส่วนใหญ่-กลาง-เล็ก
- ห้ามบีบ content หรือ legend เพื่อไล่ ~1.618 แบบเคร่งครัด
- ห้ามเรียก exact golden ratio หากไม่ได้คำนวณและตรวจ

## Fibonacci rhythm
- ใช้ 3, 5, 8, 13 เป็นกลุ่ม/จังหวะเมื่อเหมาะสม
- ใช้กับ petals, radial bands, leaf groups, scale hierarchy ได้
- ไม่ต้องใช้ทุกองค์ประกอบ
- question count และ colorability มี precedence

## Phyllotaxis / golden-angle-inspired rhythm
- ใช้กับดอกไม้ เมล็ด radial motifs ได้
- golden-angle ~137.5° เป็น guide/inspiration
- ถ้ารายละเอียดจริงแน่นเกินไป ให้ใช้ grouped wedges / grouped spiral bands
- ห้ามสร้าง micro-seed/petal cells เล็กกว่า `MIN_COLORABLE_CELL_SIZE`

## Balance / symmetry
`SYMMETRY_MODE = AUTO` ต้องเลือกให้เหมาะกับธีม:
- BILATERAL
- RADIAL
- APPROXIMATE_NATURAL
- NONE

เป้าหมายคือ dynamic balance ไม่ใช่ mirror symmetry 100% ทุกงาน

## Natural scale hierarchy
- focal element หลัก 1 จุด/กลุ่ม
- secondary elements ขนาดรอง
- supporting motifs ขนาดเล็กกว่า
- scale transition ต้องสัมพันธ์กับ `TILE_SCALE_VARIATION = CONTROLLED`

## Question flow
เมื่อ `QUESTION_FLOW = FOLLOW_VISUAL_RHYTHM`:
- question regions ต้องกระจายตามสายตา/จังหวะ composition
- ห้ามเปลี่ยน verified question count, answers, codes หรือ colors
- readability และ text-safe area มี precedence เหนือ natural rhythm

## Interaction with primary shape
```text
NATURAL HARMONY controls placement / scale / rhythm
PRIMARY SHAPE controls construction grammar
```

ถ้า PRIMARY_SHAPE=TRIANGLE กลีบ/เมล็ด/ใบไม้ที่ใช้ natural rhythm ยังต้องสร้างจาก triangle-derived clusters เป็นหลัก

## Truthfulness
Natural Harmony Blueprint ต้องบอกว่าแต่ละหลักเป็น:
- EXACT/CALCULATED
- APPROXIMATE
- INSPIRED
- NOT_USED

ห้ามใช้คำว่า exact หากไม่มีการคำนวณและตรวจ

## QA PASS
- focal hierarchy ชัด
- visual rhythm ช่วย composition
- primary-shape grammar ยังชัด
- question flow อ่านง่าย
- minimum colorable area ผ่าน
- ไม่มี micro-detail excess
- ไม่มี forced-ratio distortion
- symmetry/balance เหมาะกับธีม

## QA FAIL
- natural system ทำให้โจทย์อ่านยาก
- exact claim ไม่มีหลักฐาน
- phyllotaxis detail เล็กเกินระบาย
- natural pattern ทำลาย primary-shape grammar
- question distribution ถูกบิดเพื่อความสวยจน mapping/usability เสีย

## Recommended defaults
```text
COMPOSITION_SYSTEM = AUTO
GOLDEN_SECTION_GUIDE = AUTO
FIBONACCI_RHYTHM = AUTO
PHYLLOTAXIS_MODE = AUTO
RADIAL_SYMMETRY = AUTO
PETAL_COUNT_LOGIC = AUTO
FOCAL_POINT_PLACEMENT = AUTO
NATURAL_SCALE_HIERARCHY = YES
NATURAL_PATTERN_STRENGTH = MODERATE
COMPOSITION_BALANCE = AUTO
SYMMETRY_MODE = AUTO
QUESTION_FLOW = FOLLOW_VISUAL_RHYTHM
QUESTION_DISTRIBUTION_BALANCE = REQUIRED
```
