# Reference Version Policy

Version: 1.0.0
Status: Approved visual-reference policy

## Purpose

เก็บคุณลักษณะของภาพอ้างอิงที่ผู้ใช้ยอมรับไว้เป็น baseline โดยไม่บังคับให้ Gem ลอก composition เดิมทุกครั้ง

## Reference A — `REFERENCE_WOW`

สถานะ: User-approved visual reference

คุณลักษณะที่ต้องรักษา:
- มีความมีชีวิตชีวาและความรู้สึก “ว้าว” เมื่อมองครั้งแรก
- geometric garden มีรายละเอียดมากพอให้สนุก แต่โจทย์ยังอ่านได้
- primary shape มีบทบาทสูงและสร้าง theme ได้ชัด
- ภาพมี focal hierarchy และองค์ประกอบหลายระดับ
- Color-by-Code legend ชัดเจน

ใช้เป็น benchmark สำหรับ:
- visual impact
- thematic richness
- child engagement
- geometric identity

## Reference B — `REFERENCE_BEAUTIFUL`

สถานะ: User-approved visual reference

คุณลักษณะที่ต้องรักษา:
- สวย สะอาด ดูเป็นระเบียบ
- negative space ดี
- composition อ่านง่าย
- symmetry/balance ชัด
- รายละเอียดไม่แน่นเกินไป
- visual hierarchy เหมาะกับ A4

ใช้เป็น benchmark สำหรับ:
- cleanliness
- balance
- readability
- compositional restraint

## Reference C — `REFERENCE_NATURAL_HARMONY_V3`

สถานะ: Development target

เป้าหมายคือรวมข้อดีของ A และ B แล้วเพิ่ม Natural Proportion Engine:

```text
V1 visual impact
+ V2 cleanliness / balance
+ golden-section-inspired focal hierarchy
+ Fibonacci-inspired rhythm
+ phyllotaxis / golden-angle-inspired radial composition
+ natural scale progression
= V3 Natural Harmony
```

V3 ไม่จำเป็นต้องสมมาตรแบบ mirror 100% เสมอไป แต่ต้องมี **dynamic balance** แบบธรรมชาติ

## Evaluation matrix

ทุก candidate สำหรับ V3 ให้ประเมินอย่างน้อย:

| Dimension | Source target |
|---|---|
| First-glance wow | Reference A |
| Cleanliness | Reference B |
| Readability | Reference B |
| Theme richness | Reference A |
| Geometric grammar | A + B |
| Natural rhythm | V3 policy |
| Line clarity | Production QA |
| Coloring usability | Production QA |
| Academic/mapping integrity | Canonical SSOT |

## Promotion rule

Candidate จะ promote เป็น `REFERENCE_NATURAL_HARMONY_V3` ได้เมื่อ:
- ไม่ด้อยกว่า A ใน visual impact อย่างมีนัยสำคัญ
- ไม่ด้อยกว่า B ใน cleanliness/readability
- natural-proportion cues มองเห็นเป็น rhythm/hierarchy โดยไม่ฝืน
- ผ่าน academic, mapping, line, topology, Thai, print และ colorability gates ทั้งหมด

## Important

Reference policy บันทึก **คุณลักษณะและเกณฑ์** ไม่ถือว่าภาพ raster ที่สร้างด้วย generative image model เป็น production vector master โดยอัตโนมัติ

หากต้องใช้ reference เป็น production output ต้อง reconstruct/finalize ตาม `RENDER_PIPELINE_POLICY.md`.
