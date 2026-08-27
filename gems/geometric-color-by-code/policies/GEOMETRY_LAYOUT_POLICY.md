# Geometry Layout Policy

Version: 1.4.0

## Objective

รักษาความสวยงามแบบ mosaic/tessellation โดยให้ **ความคมของเส้น ความสามารถในการระบายสีจริง และ visual hierarchy** เป็น production requirements ไม่ใช่รายละเอียดเสริม

อ่านร่วมกับ:
- `LINE_RENDERING_POLICY.md`
- `RENDER_PIPELINE_POLICY.md`
- `GOLDEN_REFERENCE_STANDARD.md`

## Primary-shape dominance

เมื่อ `SHAPE_DOMINANCE = HIGH`:
- target ประมาณ >=85% ของ structural tiling rhythm derive จาก primary shape
- freeform major objects prohibited
- theme silhouette ต้องเกิดจาก tile clusters
- question regions ต้องยังสัมพันธ์กับ primary-shape grammar

## Controlled tile scale

```text
TILE_SCALE_VARIATION = CONTROLLED
```

- มี base tile module หรือสัดส่วนที่สัมพันธ์กัน
- ห้ามแบ่งหน้าเป็นหลาย visual systems ที่ไม่สัมพันธ์กัน
- transition ของ density ต้องมีเหตุผลเชิง composition

## Minimum colorable area

```text
MIN_COLORABLE_CELL_SIZE = AGE_APPROPRIATE_PRINT_USABLE
MIN_SEGMENT_LENGTH = ENFORCED
MICRO_TILE_DENSITY_POLICY = QUALITY_FIRST
```

FAIL เมื่อ:
- มี sliver cell แคบ/แหลมจนดินสอสีลงยาก
- มี cell เล็กมากเพียงเพื่อรักษารายละเอียด silhouette
- มี segment สั้นจำนวนมากจนเกิด visual noise

Resolution order:
1. merge neighboring compatible cells
2. simplify contour
3. reduce junction count
4. reduce micro-tile density
5. preserve mapping SSOT

## Question-region grammar

Default:

```text
QUESTION_REGION_MODE = GROUPED_TILES
QUESTION_REGION_SHAPE_GRAMMAR = PRIMARY_SHAPE_GROUP
```

- region ต้อง derive จาก tile grouping
- label anchor ใช้ได้เมื่อจำเป็น แต่ต้องเล็กและไม่กลายเป็น visual grammar หลัก
- หลีกเลี่ยง large circle / leaf / cloud / rounded box answer containers

## Freeform detail budget

```text
FREEFORM_DETAIL_BUDGET = SMALL_RECOGNIZABILITY_DETAILS_ONLY
```

อนุญาตเฉพาะรายละเอียดเล็ก เช่น antenna, eye, stem joint หรือ short contour correction

ไม่อนุญาตให้ใช้ freeform เป็น major cloud, petal, leaf, wing หรือ animal body เมื่อ HIGH dominance

## Stroke hierarchy

ใช้ 3 ระดับ:

```text
OUTER FRAME / main activity boundary = HEAVY
OBJECT / THEME SILHOUETTE = MEDIUM
INTERNAL TILE BOUNDARY = LIGHT_TO_MEDIUM
```

เป้าหมาย:
- outer boundary อ่านออกทันที
- silhouette ชัดแต่ไม่หนักเท่า frame
- internal grid บางกว่าเล็กน้อยแต่ยังคมและพิมพ์ชัด

ห้าม:
- hairline
- fuzzy/sketch stroke
- accidental double stroke
- broken join
- charcoal/pencil texture

## Triangle-mosaic reference rule

สำหรับ `PRIMARY_SHAPE = TRIANGLE`:
- flower petals = triangle clusters
- leaves = tapered triangle clusters
- butterfly wings = mirrored triangle groups
- clouds = stepped/faceted triangle clusters
- mountains = triangular bands
- ground = triangle strips / faceted fields

freeform antenna/body detail ใช้ได้ในสัดส่วนเล็กเพื่อ recognizability

## Topology quality

`LINE_TOPOLOGY_QA = CRITICAL`

PASS เมื่อ:
- shared border = เส้นเดียว
- closed regions ปิดสนิท
- ไม่มี micro gaps
- ไม่มี accidental intersections
- ไม่มี starburst junction ที่เกิดจากเส้นจำนวนมากมาชนกันโดยไม่จำเป็น
- border ไม่ชน text-safe area

## Starburst avoidance

เมื่อหลาย tile edges จะมาชนที่จุดเดียว:
- ลดจำนวน edges ที่ converge
- stagger junctions
- merge local cells
- simplify motif geometry

ห้ามสร้างจุดดาวเส้นถี่ที่ทำให้ดูเป็นเส้นแตกหรือระบายสีไม่ได้

## Print rule

Default A4 Portrait, white background, black clean outlines, low ink. Main activity monochrome; colored preview จำกัดอยู่ใน legend เว้นแต่ผู้ใช้สั่งต่างออกไป

## Priority

```text
CRISP LINES
> COLORABILITY
> TOPOLOGY
> MICRO DETAIL
```
