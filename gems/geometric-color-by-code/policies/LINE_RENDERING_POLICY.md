# Geometric Color-by-Code — Line Rendering Policy

Version: 1.0.0
Status: Gem-specific production policy

## Purpose

กำหนดมาตรฐานเส้นสำหรับใบงาน geometric mosaic ให้คม ชัด สะอาด และเหมาะกับการพิมพ์ A4/ถ่ายเอกสาร/ระบายสีจริง โดยลดปัญหาเส้นแตก เส้นสั่น เส้นซ้อน และ micro-geometry ที่ละเอียดเกินความสามารถของ image renderer

## Core priority

```text
CRISP_LINES > MICRO_TILE_DENSITY
READABILITY > GEOMETRIC_DETAIL
PRINT_USABILITY > DECORATIVE_COMPLEXITY
```

## Default rendering contract

```text
LINE_RENDER_STYLE = CLEAN_VECTOR_LIKE
LINE_QUALITY = CRISP
STROKE_WIDTH = UNIFORM_MEDIUM
STROKE_VARIATION = MINIMAL
SKETCH_TEXTURE = PROHIBITED
ROUGH_PENCIL_EFFECT = PROHIBITED
BROKEN_LINES = PROHIBITED
DOUBLE_STROKES = PROHIBITED
HAIRLINE_SEGMENTS = PROHIBITED
ACCIDENTAL_INTERSECTIONS = PROHIBITED
CELL_EDGE_SIMPLIFICATION = YES
MICRO_TILE_MIN_SIZE = PRINT_READABLE
TILE_DENSITY = CONTROLLED
MIN_SEGMENT_LENGTH = ENFORCED
PRINT_LINE_CLARITY_QA = CRITICAL
```

## Vector-like appearance

คำว่า `CLEAN_VECTOR_LIKE` หมายถึงภาพ raster สามารถใช้ได้ แต่เส้นควรมีลักษณะเหมือนเส้น vector ที่ถูก stroke เพียงครั้งเดียว:
- ขอบแต่ละ cell เป็นเส้นเดียวต่อเนื่อง
- ความหนาสม่ำเสมอ
- ไม่มีเส้นขน/เส้นร่าง/เส้นซ้ำ
- มุมและจุดเชื่อมสะอาด
- ไม่มี anti-sketch texture โดยตั้งใจ
- พื้นหลังขาวสะอาด

ห้ามใช้คำสั่งเชิงสไตล์ เช่น sketchy, hand-drawn rough, pencil texture, scratchy ink หากงานมี `PRINT_LINE_CLARITY_QA = CRITICAL`.

## Stroke hierarchy

แนะนำให้ใช้เพียง 2 ระดับหลัก:
1. `OUTER/MAJOR BOUNDARY` — หนากว่าเล็กน้อย
2. `INTERNAL TILE BOUNDARY` — medium และสม่ำเสมอ

ห้ามมีหลายระดับความหนาจนเกิด visual noise และห้ามใช้เส้นบางระดับ hairline สำหรับ micro tiles.

## Micro-tile density rule

จำนวน micro tiles ไม่ใช่เป้าหมายด้านคุณภาพ หากเพิ่ม tile แล้วเส้นเริ่มแตก/ซ้อน/สั่น ให้ลดจำนวน tile ทันที

สำหรับ A4:
- ใช้ tile ใหญ่พอที่จะพิมพ์และระบายสีได้
- หลีกเลี่ยง cluster ที่มีปลายสามเหลี่ยมสั้นมากหรือจุดตัดหลายเส้นในพื้นที่เล็ก
- หลีกเลี่ยง starburst/intersection ที่มีหลายเส้นมาบรรจบกันโดยไม่จำเป็น
- prefer fewer, larger, clean modules over dense ornamental micro-geometry

## Minimum segment policy

เส้นสั้นมากมีโอกาสแตกหรือกลายเป็น noise สูง จึงต้อง:
- merge/simplify geometry เมื่อ segment สั้นเกินใช้งาน
- ลด contour fidelity ก่อนเพิ่มเส้นย่อย
- ไม่สร้าง sliver triangle เพื่อไล่ contour ของวัตถุ

## Junction policy

จุดตัดของเส้นควรเรียบง่าย:
- 2–3 edges ต่อ junction เป็นค่าที่ต้องการ
- หลีกเลี่ยง 5–8 เส้นบรรจบที่จุดเดียวแบบ starburst หากไม่จำเป็น
- shared borders ต้องเป็นเส้นเดียว
- ห้ามมีเส้นปลายลอยหรือเส้นเกินทะลุ junction

## Render prompt requirements

Final worksheet prompt ต้องระบุชัด:

```text
Use crisp, clean, vector-like black line art.
Use smooth single-pass strokes with uniform medium-weight internal borders.
No sketch texture, no rough pencil effect, no fuzzy lines, no broken strokes, no double strokes.
Simplify micro-geometry whenever a segment would become too short or crowded.
Use fewer, larger geometric modules rather than dense tiny tiles.
Keep every coloring region closed, clearly bounded, and practical to color on A4.
Main activity remains pure black-and-white; color appears only in legend previews unless explicitly requested otherwise.
```

## Monochrome integrity

เมื่อ `MAIN_ART_COLOR_MODE = MONOCHROME`:
- main activity area ต้องเป็น black line + white fill เท่านั้น
- ห้ามมี beige/gray/yellow tint, watercolor wash, shadow fill หรือ accidental color leakage
- colored swatches จำกัดที่ legend ตาม policy

## Post-render visual audit

Critical FAIL หากพบอย่างใดอย่างหนึ่ง:
- เส้นแตก/เป็นช่วง
- เส้นดูสั่นหรือขรุขระอย่างชัดเจน
- duplicate stroke ตามขอบเดียวกัน
- fuzzy/gray edge ที่รบกวนการพิมพ์
- micro starburst ที่อ่าน region ไม่ออก
- tile เล็กจนระบายสีไม่ได้
- เส้นหลายเส้นชนข้อความ
- main artwork มีสี/โทนแทรกโดยไม่ได้สั่ง

## Resolution order

เมื่อ line quality ไม่ผ่าน ให้แก้ตามลำดับ:
1. ลด micro-tile density
2. simplify contours
3. ลด junction complexity
4. เพิ่ม minimum tile/segment size
5. ลด decoration
6. ใช้ label anchors/grouped regions
7. paginate หากจำเป็น

ห้ามแก้ด้วยการทำเส้นบางลงจนดูเหมือนคมขึ้น เพราะจะทำให้การพิมพ์จริงแย่ลง
