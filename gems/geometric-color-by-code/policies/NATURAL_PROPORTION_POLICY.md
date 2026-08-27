# Natural Proportion Policy

Version: 1.0.0
Status: Gem-specific production policy

## Purpose

เพิ่มจังหวะและสัดส่วนที่พบในธรรมชาติเข้าสู่การจัดองค์ประกอบของ Geometric Color-by-Code โดยไม่ลดความถูกต้อง ความอ่านง่าย ความสามารถในการระบายสี หรือความคมของเส้น

แนวคิดหลัก:

```text
ACADEMIC CORRECTNESS
→ COLOR/MAPPING INTEGRITY
→ GEOMETRIC GRAMMAR
→ USABLE COLORING AREAS
→ NATURAL PROPORTION / RHYTHM
→ DECORATION
```

Natural proportion เป็น **composition guide** ไม่ใช่ข้อบังคับให้ทุกระยะหรือทุกมุมต้องเท่าค่าทางคณิตศาสตร์แบบ exact.

## Supported composition systems

```text
COMPOSITION_SYSTEM = AUTO | BALANCED | NATURAL_PROPORTION | SYMMETRIC | RADIAL | CUSTOM
GOLDEN_RATIO_GUIDE = YES | NO | AUTO
PHYLLOTAXIS_MODE = OFF | AUTO | GOLDEN_ANGLE_INSPIRED | RADIAL_SPIRAL
FIBONACCI_RHYTHM = OFF | AUTO | ENABLED
RADIAL_SYMMETRY = OFF | AUTO | ENABLED
PETAL_COUNT_LOGIC = AUTO | NATURAL_PATTERN | USER_DEFINED
FOCAL_POINT_PLACEMENT = AUTO | CENTER | GOLDEN_SECTION | RULE_OF_THIRDS | CUSTOM
SCALE_PROGRESSION = UNIFORM | CONTROLLED | NATURAL_HIERARCHY
NATURAL_PATTERN_STRENGTH = SUBTLE | MODERATE | STRONG
```

## Golden ratio guidance

เมื่อ `GOLDEN_RATIO_GUIDE = YES` หรือ AUTO แล้วเหมาะกับ composition:
- ใช้ golden section เพื่อช่วยวาง focal hierarchy หรือแบ่งสัดส่วนพื้นที่หลัก
- ใช้เป็น guide สำหรับขนาดสัมพัทธ์ขององค์ประกอบใหญ่-กลาง-เล็ก
- ห้ามบีบพื้นที่คำถามหรือ legend เพียงเพื่อให้ได้ค่า ~1.618 แบบเคร่งครัด
- ห้ามอ้างว่า composition เป็น exact golden ratio หากไม่ได้คำนวณและตรวจจริง

## Golden-angle / phyllotaxis guidance

เมื่อเหมาะกับธีม เช่น ทานตะวัน ดอกไม้ เมล็ด ใบไม้ หรือ radial motif:
- ใช้ golden-angle-inspired spacing ประมาณ 137.5° เป็นแนวทางในการกระจายองค์ประกอบรอบจุดศูนย์กลาง
- สามารถ approximate ด้วย primary-shape tile groups ได้
- ห้ามสร้าง micro tiles เล็กเกิน `MIN_COLORABLE_CELL_SIZE` เพื่อเลียนแบบเมล็ดจำนวนมาก
- ถ้าความละเอียดไม่พอ ให้ใช้ **grouped seed/petal clusters** แทนการวาดเมล็ดทุกเมล็ด

## Fibonacci rhythm

เมื่อ `FIBONACCI_RHYTHM = ENABLED` หรือ AUTO:
- ใช้จำนวนกลุ่ม/จังหวะ เช่น 3, 5, 8, 13 เมื่อเหมาะสมกับ visual rhythm
- ใช้ในการจัด petal groups, leaf groups, radial bands, scale hierarchy หรือ repetition count
- ไม่จำเป็นต้องใช้ Fibonacci ทุกองค์ประกอบ
- ความเหมาะสมต่อจำนวนข้อและพื้นที่ระบายสีมี precedence

## Radial symmetry / petal logic

สำหรับวัตถุธรรมชาติที่มี symmetry:
- ดอกไม้สามารถใช้ 5-fold, 6-fold, 8-fold หรือรูปแบบอื่นตามความเหมาะสม
- ถ้าใช้ `PETAL_COUNT_LOGIC = NATURAL_PATTERN` ให้เลือกจำนวนกลีบ/กลุ่มที่ให้ balance และรองรับ primary-shape grammar
- question regions อาจกระจายตามกลีบ/วงแหวน แต่ต้องยังมีพื้นที่ข้อความเพียงพอ

## Natural hierarchy

`SCALE_PROGRESSION = NATURAL_HIERARCHY`:
- มี focal element หลัก 1 จุดหรือกลุ่ม
- มี secondary elements ขนาดรอง
- มี supporting micro motifs ขนาดเล็กกว่า
- การเปลี่ยนขนาดต้อง smooth และสอดคล้องกับ `TILE_SCALE_VARIATION = CONTROLLED`

## Theme examples

### สวนดอกไม้ + TRIANGLE
- focal flower วางใกล้ golden-section guide หรือ center-balanced position
- petal clusters ใช้ radial rhythm
- seed center ใช้ grouped spiral clusters ที่ได้แรงบันดาลใจจาก phyllotaxis
- ดอกข้างเคียงลดขนาดตาม natural hierarchy
- ใบไม้กระจายเป็น rhythmic clusters ไม่ต้อง mirror แข็งทุกจุด

### ทานตะวัน
- center seed field ใช้ spiral/radial cluster logic
- ห้ามวาดเมล็ดจิ๋วถี่เกินไป; ใช้ 8–13 grouped wedges/spiral bands เมื่อเหมาะสม
- petal ring ใช้ radial symmetry และ primary-shape clusters

### ใต้ทะเล / เปลือกหอย
- ใช้ spiral-inspired scale progression ได้
- ห้ามอ้าง Fibonacci spiral exact หากเป็นเพียง visual inspiration

## Interaction with primary-shape grammar

Natural proportion **ไม่แทนที่** primary-shape construction.

```text
NATURAL PROPORTION controls placement / scale / rhythm
PRIMARY SHAPE controls construction grammar
```

ตัวอย่าง:
- golden-angle guide ช่วยกำหนดตำแหน่ง petal clusters
- แต่ petal clusters ยังต้องสร้างจาก TRIANGLE / RHOMBUS / HEXAGON ตาม `PRIMARY_SHAPE`

## Interaction with Color-by-Code content

- จำนวนข้อและ mapping ถูกล็อกก่อน composition
- natural layout engine ห้ามเปลี่ยน verified question text / answer / color mapping
- ถ้า natural pattern count ไม่เท่ากับ question count ให้ group tiles หรือใช้ supporting motifs แทนการบิดจำนวนข้อ

## QA gates

PASS เมื่อ:
- composition มี focal hierarchy ชัด
- natural rhythm ช่วยให้งานดูสมดุลโดยไม่ลด usability
- ไม่มี forced golden-ratio distortion
- primary-shape grammar ยังคงชัด
- question text อ่านง่าย
- minimum colorable area ผ่าน
- tile density และ line clarity ผ่าน

FAIL เมื่อ:
- อ้าง exact golden ratio / Fibonacci / golden angle โดยไม่มีการตรวจ
- บีบข้อความหรือช่องระบายสีเพื่อบังคับสัดส่วน
- ใช้ micro-detail เล็กเกินไปเพื่อเลียนแบบธรรมชาติ
- natural pattern กลายเป็น decoration ที่ทำลาย geometric grammar

## Recommended defaults

```text
COMPOSITION_SYSTEM = AUTO
GOLDEN_RATIO_GUIDE = AUTO
PHYLLOTAXIS_MODE = AUTO
FIBONACCI_RHYTHM = AUTO
RADIAL_SYMMETRY = AUTO
PETAL_COUNT_LOGIC = AUTO
FOCAL_POINT_PLACEMENT = AUTO
SCALE_PROGRESSION = NATURAL_HIERARCHY
NATURAL_PATTERN_STRENGTH = MODERATE
```

AUTO ใช้ natural proportion เมื่อช่วยให้ theme/composition ดีขึ้น และ fallback เป็น balanced/symmetric composition เมื่อ readability หรือ mapping ต้องมาก่อน
