# Geometric Color-by-Code — Render Pipeline Policy

Version: 2.0.0
Status: Gem-specific production policy

## Purpose

กำหนด renderer ที่เหมาะสมสำหรับใบงาน geometric Color-by-Code โดยเฉพาะงานที่ต้องการเส้นคมสำหรับพิมพ์จริง หลังการทดสอบพบว่า image model สามารถสร้าง composition ที่ดีมากได้ แต่ **ไม่สามารถรับประกันเส้น mosaic ที่คม สม่ำเสมอ และ topology ที่ deterministic ได้ทุกครั้ง** แม้ prompt จะกำหนด clean-vector-like อย่างเข้มงวด

## Root-cause decision

```text
PROMPT QUALITY != LINE RENDER GUARANTEE
```

ดังนั้น production pipeline ต้องแยก creative composition ออกจาก final printable boundaries.

```text
ACADEMIC CONTENT = DETERMINISTIC
MAPPING = DETERMINISTIC
GEOMETRIC TOPOLOGY = DETERMINISTIC
VISIBLE ACADEMIC TEXT = DETERMINISTIC
FINAL PRINTABLE BOUNDARIES = DETERMINISTIC / VECTOR-FIRST
IMAGE MODEL = CONCEPT / COMPOSITION ASSIST ONLY
```

## Production render rule

### VECTOR_FIRST_REQUIRED

สำหรับ final worksheet ที่มี geometric coloring boundaries:

```text
PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED
```

ถ้า environment รองรับ SVG/PDF/vector/deterministic drawing ให้ใช้ deterministic renderer เป็น final source เสมอ

Pipeline:

```text
Verified Content Blueprint
→ Deterministic Geometry Blueprint
→ Tile/Region Graph
→ Shared-edge Graph
→ SVG / vector paths
→ Deterministic Thai/text placement
→ Thai-font glyph validation
→ Legend swatches
→ Vector QA
→ Raster preview (optional)
→ Print QA
```

ข้อดี:
- เส้นคมสม่ำเสมอ
- shared border เป็น edge เดียว
- ไม่มี generative fuzzy/broken strokes
- region count และ topology ตรวจสอบได้
- ข้อความไทยและโจทย์ไม่ถูก image model rewrite
- สามารถ export high-resolution raster preview จาก vector master ได้

## HYBRID_CONCEPT_ONLY

Image model ใช้ช่วยออกแบบ:
- composition
- theme silhouette idea
- visual hierarchy
- motif exploration

แต่ผลลัพธ์จาก image model ต้องถูกแปลงเป็น deterministic tile graph/vector geometry ใหม่ก่อนถือเป็น production final.

```text
IMAGE MODEL
→ concept reference only
→ deterministic reconstruction
→ vector final
```

ห้าม trace เส้นแตก/fuzzy จาก raster candidate มาเป็น final boundaries โดยตรง

## IMAGE_PROMPT_ONLY

`IMAGE_PROMPT_ONLY` ใช้ได้เพียง:
- concept preview
- exploration
- low-stakes mockup
- environment ที่ไม่มี deterministic renderer

สถานะของ output ต้องเป็น:

```text
PREVIEW_ONLY / NOT_PRODUCTION_FINAL
```

ถ้าเกิดเส้นแตก สั่น ซ้อน หรือไม่สม่ำเสมอ **ห้าม regenerate ซ้ำแล้วเรียก production-ready** เพราะ failure เป็นข้อจำกัดของ renderer ไม่ใช่ prompt เพียงอย่างเดียว

## Render-mode resolution

```text
RENDER_MODE = AUTO
```

AUTO resolves:

```text
if final output requires printable geometric boundaries:
    VECTOR_FIRST_REQUIRED
elif only concept/mockup is requested:
    IMAGE_CONCEPT_PREVIEW
else:
    choose safest deterministic path available
```

## Canonical render parameters

```text
RENDER_MODE
PRODUCTION_FINAL_RENDER_MODE
VECTOR_RENDERING_REQUIRED
DETERMINISTIC_TEXT_PLACEMENT
DETERMINISTIC_REGION_TOPOLOGY
DETERMINISTIC_SHARED_EDGES
THAI_FONT_RENDER_QA
IMAGE_MODEL_ROLE
RASTER_PREVIEW_SOURCE
```

Defaults:

```text
RENDER_MODE = AUTO
PRODUCTION_FINAL_RENDER_MODE = VECTOR_FIRST_REQUIRED
VECTOR_RENDERING_REQUIRED = YES_FOR_FINAL_PRINT
DETERMINISTIC_TEXT_PLACEMENT = YES_FOR_FINAL_PRINT
DETERMINISTIC_REGION_TOPOLOGY = YES
DETERMINISTIC_SHARED_EDGES = YES
THAI_FONT_RENDER_QA = CRITICAL
IMAGE_MODEL_ROLE = CONCEPT_AND_COMPOSITION_ASSIST
RASTER_PREVIEW_SOURCE = VECTOR_MASTER
```

## Shared-edge graph rule

Final geometry must use one source-of-truth graph:
- shared edge stored/rendered once
- every coloring region is a closed cycle/path
- no duplicate edge
- no orphan edge
- no ambiguous overlapping boundary
- no sliver cell below minimum colorable threshold
- every question region references valid tile/region IDs

## Thai text rule

หัวข้อ คำชี้แจง โจทย์ เลขข้อ ชื่อสี และ legend labels ต้องใช้ deterministic text placement ใน final print mode

Font stack ต้องผ่าน:

```text
THAI_FONT_RENDER_QA = CRITICAL
NO tofu / missing glyph
NO missing vowel/tone marks
NO broken Thai shaping
NO mixed-font baseline mismatch that harms readability
```

ไม่แจกจ่ายไฟล์ฟอนต์ให้ผู้ใช้; ใช้ฟอนต์ที่ระบบ/renderer รองรับในการสร้าง artifact เท่านั้น

## Raster preview rule

ถ้าต้องส่ง PNG/JPG preview:
- rasterize จาก vector master ที่ความละเอียดเหมาะสม
- ห้ามใช้ generative raster เป็น final print source
- anti-aliasing ต้องสม่ำเสมอ
- internal line ต้องยังต่อเนื่องเมื่อดูที่ 100%

## Production acceptance statement

```text
BEST = Verified content + deterministic vector geometry/text
ACCEPTABLE = Hybrid concept + deterministic vector reconstruction
PREVIEW ONLY = image-model raster
```

ห้ามอ้างว่า image-model raster เป็น production-final สำหรับ geometric Color-by-Code เมื่อความคมและความต่อเนื่องของเส้นเป็น requirement.
