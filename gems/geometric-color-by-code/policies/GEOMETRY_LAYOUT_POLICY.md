# Geometry Layout Policy

Version: 1.2.0

## Objective

รักษาความสวยงามแบบปูกระเบื้อง/โมเสก โดยไม่ลดความอ่านง่ายและความถูกต้องของใบงาน และต้องทำให้รูปทรงที่ผู้ใช้กำหนดเป็น **โครงสร้างที่สร้างภาพจริง** ไม่ใช่ pattern overlay บนภาพ freeform

## Primary-shape dominance

เมื่อผู้ใช้กำหนดรูปทรงหลัก:
- `SHAPE_DOMINANCE = HIGH` ตั้งเป้าให้ประมาณ 85% หรือมากกว่าของ structural cell boundaries / visible tiling rhythm ใน main activity area derive จาก geometry ของรูปทรงหลัก
- ห้ามใช้ freeform illustration เป็นโครงสร้างหลัก
- รายละเอียดเสริมที่ไม่ใช่รูปทรงหลักใช้ได้เฉพาะเพื่อช่วย recognizability/readability
- ถ้ามองภาพรวมจากระยะไกล ต้องเห็นได้ทันทีว่าภาพถูกประกอบจากรูปทรงหลัก

### Construction test

PASS:

```text
primary shape
→ repeated/varied tiles
→ grouped clusters
→ object silhouette
→ complete themed composition
```

FAIL:

```text
freeform animal/object drawing
→ geometric lines/pattern added on top
```

## Freeform-area limit

เมื่อ `SHAPE_DOMINANCE = HIGH`:
- `FREEFORM_MAJOR_OBJECTS = PROHIBITED_WHEN_HIGH`
- ห้ามมี freeform object ขนาดใหญ่ครอง silhouette หลัก
- freeform detail ใช้สำหรับตา ปาก label anchor ข้อต่อ หรือ contour correction เล็กน้อยได้
- target freeform structural area ควรต่ำประมาณ 15% และไม่ควรเกินราว 20% ของ main composition
- หากต้องใช้ freeform มากกว่านี้เพื่อให้ธีมอ่านออก ให้ redesign geometry หรือ downgrade `SHAPE_DOMINANCE` อย่างซื่อสัตย์

## Tiling validity

- TRIANGLE, SQUARE, RECTANGLE, RHOMBUS, HEXAGON: สามารถใช้ tessellation โดยตรงเมื่อ layout เหมาะสม
- CIRCLE_CELL: ใช้ cell packing / repeated circular cells ไม่ควรเรียกว่า exact tessellation หากมีช่องว่าง
- CUSTOM shape: ต้องระบุว่า exact tessellation, approximate tessellation หรือ decorative cell pattern

## Controlled tile scale

Default:

```text
TILE_SCALE_VARIATION = CONTROLLED
```

อนุญาตให้ tile มีหลายขนาดได้เพื่อสร้าง silhouette และพื้นที่โจทย์ แต่ทั้งหน้าต้องยังดูเป็น visual language เดียวกัน

FAIL เช่น:
- ครึ่งบนใช้สามเหลี่ยมใหญ่มากและโปร่งมาก
- ครึ่งล่างใช้ micro-triangle เล็กและแน่นมาก
- ไม่มี transition หรือ scale hierarchy ที่ตั้งใจ

PASS เมื่อ:
- มี base tile scale ที่มองเห็นได้
- tile ใหญ่เกิดจากการรวม module เดียวกันหรือมีสัดส่วนสัมพันธ์กัน
- density เปลี่ยนอย่างค่อยเป็นค่อยไปและมีเหตุผลเชิง composition

## Question-region grammar

Default:

```text
QUESTION_REGION_SHAPE_GRAMMAR = PRIMARY_SHAPE_GROUP
```

กฎ:
- จำนวน micro tiles อาจมากกว่าจำนวนข้อ
- default `QUESTION_REGION_MODE = GROUPED_TILES`
- question region ควรเกิดจากการรวม tile ตาม grid/tiling grammar
- หลีกเลี่ยงวงกลม ใบไม้ freeform กล่องโค้ง หรือ polygon ใหญ่ที่ตัดขาดจาก primary-shape grammar
- หากข้อความอ่านยาก ให้ใช้ LABEL_ANCHOR ก่อนกลับไปสร้าง freeform region ใหญ่
- คำถามต้องอยู่ในพื้นที่ contrast ดีและไม่ทับเส้นหลายเส้น

## Theme construction

Theme silhouette ต้องเกิดจาก tile grouping เช่น:
- flower = symmetric clusters
- leaf = tapered clusters
- butterfly = mirrored clusters
- cloud = stepped/clustered cells
- mountain = triangular or stepped bands
- waves = stepped/angled bands
- elephant = grouped rhombus/triangle cells forming head, body, ears, trunk and legs
- bird = mirrored/stacked polygon cells forming body, head, wing and tail

กฎ: theme recognizability ต้องไม่มาก่อน readability แต่ recognizability ห้ามถูกแก้ด้วยการกลับไปวาด freeform major object

## Triangle-mosaic reference rule

เมื่อ `PRIMARY_SHAPE = TRIANGLE` และธีมสวน/ธรรมชาติ:
- flower petals ต้องสร้างจาก triangle clusters หรือ modules ที่ derive จาก triangular grid
- leaves ต้องเป็น tapered triangle clusters
- butterfly wings ต้องเป็น mirrored triangle groups
- clouds ควรเป็น stepped triangle clusters ไม่ใช่ freeform cloud outline ขนาดใหญ่
- hills/mountains/ground bands ต้องรักษา triangular rhythm
- question regions ยังต้องสัมพันธ์กับ triangular grouping

## Line / Topology Quality

`LINE_TOPOLOGY_QA = CRITICAL`

PASS เมื่อ:
- shared border ระหว่างสอง region อ่านเป็นเส้นเดียวชัดเจน
- join ต่อกันสนิท
- ไม่มีเส้นซ้อนโดยไม่ตั้งใจ
- ไม่มีช่องเปิดที่ทำให้ region ไม่ปิด
- ไม่มี tiny sliver cell ที่เด็กระบายสีจริงไม่ได้
- ไม่มี border collision กับข้อความ

FAIL เมื่อพบ:
- accidental double lines
- broken joins
- ambiguous shared borders
- micro gaps ระหว่าง tile ที่ควรติดกัน
- เส้นตัดกันแบบไม่ตั้งใจ
- sliver cell เล็กมากจาก contour correction

### Sliver-cell resolution

ถ้า cell เล็กเกินใช้งาน:
1. merge กับ adjacent region ที่ mapping เข้ากันได้
2. simplify local topology
3. reduce contour detail
4. preserve question/color mapping SSOT

ห้ามปล่อย sliver cell ไว้เพียงเพื่อรักษาความเหมือนภาพต้นฉบับ

## Density resolution

เมื่อโจทย์/ข้อความแน่นเกินไป:
1. ลด decoration
2. รวม tiles เป็น question regions ใหญ่ขึ้น
3. ย้ายคำถามไป anchor zone
4. ปรับ orientation
5. paginate
6. ห้ามย่อตัวอักษรจนอ่านยาก

## Visual-language consistency audit

ก่อน PASS ให้ตรวจ:
1. base tile rhythm ต่อเนื่องทั้งหน้าไหม
2. scale variation ถูกควบคุมไหม
3. question regions ยังดูเป็นสมาชิกของ mosaic เดียวกันไหม
4. มีส่วนใดดูเหมือน conventional illustration แทรกอยู่หรือไม่
5. density transition มีเหตุผลหรือไม่

## Shape audit checklist

ก่อน PASS ให้ถาม:
1. ถ้าลบเส้น freeform ออก ภาพยังคงอ่านเป็น mosaic จาก primary shape หรือไม่
2. silhouette หลักเกิดจาก tile clusters จริงหรือไม่
3. มีวัตถุหลักใดที่เป็น conventional drawing แล้วเพียงเติม pattern ภายหลังหรือไม่
4. primary-shape rhythm ต่อเนื่องพอหรือไม่
5. question regions ยังสัมพันธ์กับ grid/tiling หรือถูกตัดเป็น freeform ขนาดใหญ่เกินไปหรือไม่
6. line topology สะอาดและระบายสีได้จริงหรือไม่

ถ้าข้อ 2 = ไม่ หรือข้อ 3 = ใช่ → Critical FAIL สำหรับ `SHAPE_DOMINANCE = HIGH`

## Print rule

Default A4 Portrait, print-safe margin, white background, black outlines, low ink. Colored preview จำกัดไว้ที่ legend เว้นแต่ผู้ใช้สั่งเป็นอย่างอื่น
