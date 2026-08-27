# Reference Version Policy

Version: 1.1.0
Status: Approved visual-reference policy

## Purpose
เก็บคุณลักษณะของภาพอ้างอิงที่ผู้ใช้ยอมรับไว้เป็น baseline โดยไม่บังคับให้ Gem ลอก composition เดิมทุกครั้ง

## REFERENCE_WOW
User-approved visual reference

Benchmark:
- first-glance wow
- thematic richness
- child engagement
- strong geometric identity
- lively composition

## REFERENCE_BEAUTIFUL
User-approved visual reference

Benchmark:
- cleanliness
- balance
- negative space
- readability
- controlled detail
- A4 visual hierarchy

## REFERENCE_NATURAL_HARMONY_V3
Status: Approved design target / promotion candidate class

Definition:
```text
REFERENCE_WOW visual impact
+ REFERENCE_BEAUTIFUL cleanliness/readability
+ Natural Harmony focal hierarchy
+ golden-section-inspired placement when useful
+ Fibonacci/phyllotaxis-inspired rhythm when useful
+ dynamic natural balance
= REFERENCE_NATURAL_HARMONY_V3
```

V3 ไม่จำเป็นต้อง mirror symmetry 100%; dynamic balance ใช้ได้และควรเลือกตามธีม

## Evaluation matrix
| Dimension | Target |
|---|---|
| First-glance wow | REFERENCE_WOW |
| Cleanliness | REFERENCE_BEAUTIFUL |
| Readability | REFERENCE_BEAUTIFUL |
| Theme richness | REFERENCE_WOW |
| Geometric grammar | Canonical v1.6.0 |
| Natural hierarchy/rhythm | Natural Proportion Policy |
| Question flow | Canonical v1.6.0 |
| Line clarity | Production QA |
| Coloring usability | Production QA |
| Academic/mapping integrity | Canonical SSOT |

## Promotion rule
Candidate จะ promote เป็น `REFERENCE_NATURAL_HARMONY_V3` ได้เมื่อ:
- ไม่ด้อยกว่า WOW อย่างมีนัยสำคัญด้าน visual impact
- ไม่ด้อยกว่า BEAUTIFUL ด้าน cleanliness/readability
- natural cues ช่วย hierarchy/rhythm โดยไม่ฝืน
- question flow กลมกลืนกับ composition
- ผ่าน academic, mapping, line, topology, Thai, print, colorability gates
- final production geometry เป็น deterministic/vector

## Reference truthfulness
Reference policy บันทึก **คุณลักษณะและเกณฑ์** ไม่ใช่การรับรองว่า raster generative image เป็น production master

Image-model candidate ที่ผู้ใช้ชอบสามารถเป็น visual reference ได้ แต่ production Golden Reference ต้อง reconstruct/finalize ตาม `RENDER_PIPELINE_POLICY.md`

## Non-copy rule
Reference เป็น benchmark ไม่ใช่ template:
- ห้ามลอกตำแหน่งวัตถุเดิมทุกครั้ง
- ห้าม reuse composition แบบ mechanical
- ธีมใหม่ควรมี composition ที่เหมาะกับธีมแต่ผ่าน quality gates เดียวกัน
