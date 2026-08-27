# Geometric Color-by-Code — Render Pipeline Policy

Version: 1.1.0
Status: Gem-specific production policy

## Purpose

แก้ปัญหาที่ image model อาจสร้างเส้น mosaic แตก สั่น ซ้อน หรือไม่สม่ำเสมอ แม้ prompt จะระบุให้เส้นคมแล้ว โดยแยก **content/layout design** ออกจาก **final line rendering** และเลือก renderer ตามระดับความแม่นยำที่ต้องการ

## Principle

```text
ACADEMIC CONTENT = DETERMINISTIC
MAPPING = DETERMINISTIC
GEOMETRIC TOPOLOGY = DETERMINISTIC WHEN AVAILABLE
VISIBLE TEXT = DETERMINISTIC WHEN AVAILABLE
IMAGE MODEL = COMPOSITION / STYLE ASSIST, NOT SOURCE OF TRUTH
```

## Render modes

### 1. VECTOR_FIRST — preferred for production print

ใช้เมื่อ environment สามารถสร้าง SVG/PDF/vector geometry ได้

Pipeline:

```text
Verified Content Blueprint
→ Deterministic Geometry Blueprint
→ Tile/Region graph
→ SVG/vector paths
→ Deterministic Thai/text placement
→ Thai-font glyph validation
→ Color legend swatches
→ Raster preview if needed
→ Print QA
```

ข้อดี:
- เส้นคม
- จำนวน region deterministic
- shared borders ไม่ซ้อน
- text ไม่ถูก image model สะกดผิด
- export PDF/SVG ได้เมื่อ environment รองรับ

`VECTOR_FIRST` เป็น preferred mode เมื่อเป้าหมายคือใบงานที่นำไปขาย/พิมพ์จริงและความคมของเส้นเป็น critical requirement.

### 2. HYBRID — preferred when thematic composition benefits from image model

Pipeline:

```text
Image model / design reasoning
→ theme silhouette concept only
→ convert concept to deterministic tile graph
→ render geometry/text as vector
```

ห้ามนำเส้นจากภาพ generative มาใช้เป็น final printable boundaries โดยตรง หากเส้นไม่ผ่าน `PRINT_LINE_CLARITY_QA`.

### 3. IMAGE_PROMPT_ONLY — fallback

ใช้เมื่อไม่มี deterministic renderer

ต้อง:
- ใช้ strict clean-vector-like prompt
- จำกัด micro-tile density
- ห้าม sketch texture
- render → visual QA → regenerate หาก fail
- ลด geometry complexity ในรอบถัดไปก่อนเปลี่ยน style

## Default resolution

```text
RENDER_MODE = AUTO
```

AUTO resolves:

```text
if vector/deterministic renderer available:
    VECTOR_FIRST or HYBRID
else:
    IMAGE_PROMPT_ONLY_WITH_ITERATIVE_QA
```

## Canonical render parameters

```text
RENDER_MODE
VECTOR_RENDERING_PREFERRED
DETERMINISTIC_TEXT_PLACEMENT
DETERMINISTIC_REGION_TOPOLOGY
THAI_FONT_RENDER_QA
IMAGE_MODEL_ROLE
MAX_VISUAL_REGEN_ROUNDS
LINE_FAILURE_REDUCTION_FACTOR
```

Recommended defaults:

```text
RENDER_MODE = AUTO
VECTOR_RENDERING_PREFERRED = YES
DETERMINISTIC_TEXT_PLACEMENT = YES_WHEN_AVAILABLE
DETERMINISTIC_REGION_TOPOLOGY = YES_WHEN_AVAILABLE
THAI_FONT_RENDER_QA = CRITICAL
IMAGE_MODEL_ROLE = COMPOSITION_ASSIST
MAX_VISUAL_REGEN_ROUNDS = 3
LINE_FAILURE_REDUCTION_FACTOR = REDUCE_MICRO_DENSITY_20_TO_35_PERCENT
```

## Iterative line-quality loop

เมื่อใช้ IMAGE_PROMPT_ONLY:

```text
render candidate
→ audit line clarity
→ if PASS: accept
→ if FAIL:
   reduce micro-tile density 20–35%
   simplify contours
   reduce junction count
   restate vector-like line constraints
   regenerate
→ repeat up to MAX_VISUAL_REGEN_ROUNDS
```

ห้าม regenerate ด้วย prompt เดิมซ้ำ ๆ โดยไม่เปลี่ยน complexity เพราะไม่ใช่การแก้ root cause

## Failure escalation

ถ้ายัง FAIL หลังครบจำนวนรอบ:
- mark `IMAGE_RENDER_LINE_QUALITY = NOT_RELIABLE`
- switch to VECTOR_FIRST/HYBRID if available
- หรือส่ง verified blueprint/prompt พร้อมแจ้งว่าไม่ควรถือ raster generative candidate เป็น production-final

ห้ามอ้างว่า production-ready หากเส้นยังแตก

## Geometry graph rule

สำหรับ deterministic mode ให้ใช้ graph/source-of-truth ของ boundaries:
- shared edge ถูกเก็บเป็น edge เดียว
- closed region ต้องมี cycle/path ที่ปิด
- question region references tile IDs
- no orphan edge
- no duplicate edge
- no sliver cell below minimum threshold

## Text and Thai-font rule

ข้อความหัวข้อ คำสั่ง โจทย์ ตัวเลข ชื่อสี และ legend labels เป็น deterministic visible text เมื่อ renderer รองรับ

ก่อน render final ต้องตรวจว่า font stack ที่เลือกมี glyph ภาษาไทยจริงและรองรับสระ/วรรณยุกต์ครบ หาก preview แสดงเป็นกล่องสี่เหลี่ยม/tofu หรือ glyph หาย ให้ถือเป็น Critical FAIL และเปลี่ยนไปใช้ Thai-capable font ที่มีอยู่ใน environment เช่นตระกูล Noto Sans Thai/ฟอนต์ไทยที่ระบบรองรับ โดยไม่แจกจ่ายไฟล์ฟอนต์ออกไป

```text
THAI_FONT_RENDER_QA = CRITICAL
NO tofu/missing-glyph boxes
NO detached/missing Thai vowel/tone marks caused by font fallback
```

Image model ไม่ควร rewrite Thai text ใน production mode.

## Production recommendation

สำหรับใบงาน geometric Color-by-Code ที่ต้องการคุณภาพเชิงพาณิชย์:

```text
BEST = Verified content + deterministic SVG/PDF geometry/text
GOOD = Hybrid composition + deterministic vector finalization
FALLBACK = Strict image prompt + iterative visual QA
```
