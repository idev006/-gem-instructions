# Gem Production Standard

Version: 1.0.0
Status: Repository-wide policy

## Purpose

ทุก Gem ใน repository นี้ต้องถูกออกแบบจากประโยชน์ในการใช้งานจริง ความถูกต้องของเนื้อหา และความสามารถในการใช้งานโดยผู้ใช้ทั่วไป ไม่ใช่เพียงสร้าง prompt ที่ดูดี

## Mandatory design pillars

### 1. Practical usefulness

ก่อนสร้าง Gem ต้องตอบให้ได้ว่า:
- ใครคือผู้ใช้หลัก
- ใช้แก้ปัญหาอะไร
- ผลลัพธ์ถูกนำไปใช้จริงอย่างไร
- ค่า default ใดช่วยลดภาระผู้ใช้
- ข้อจำกัดใดทำให้ผลลัพธ์ไม่เหมาะกับงานจริง

ทุก Gem ต้องมี `USE_CASES` และ `NON_GOALS` ชัดเจนใน canonical instruction หรือ README ของ Gem

### 2. Correctness first

ความถูกต้องมีลำดับสูงกว่าความสวยงาม

ต้องมี validation/QA ที่เหมาะกับ domain เช่น:
- ความถูกต้องทางวิชาการ
- ความถูกต้องของภาษา
- ความเหมาะสมกับระดับชั้น/กลุ่มผู้ใช้
- ความสอดคล้องระหว่าง input → normalized data → output
- การตรวจจำนวน ขนาด รูปแบบ และข้อกำหนดที่ผู้ใช้สั่ง

หากมีข้อมูลสำคัญที่ image model ไม่ควรเดา ให้กำหนดข้อมูลนั้นแบบ deterministic หรือระบุข้อความที่ผ่านการตรวจแล้วใน prompt

### 3. User manual is mandatory

ทุก production Gem ต้องมี:

`gems/<gem-id>/USER_GUIDE.md`

คู่มือต้องประกอบด้วยอย่างน้อย:
- Gem นี้ใช้ทำอะไร
- เหมาะกับใคร
- วิธีสั่งงานแบบสั้น
- วิธีสั่งงานแบบละเอียด
- ค่า default สำคัญ
- parameters ที่ผู้ใช้ควรรู้
- ตัวอย่างหลาย use cases
- วิธีแก้/ปรับงานด้วยคำสั่ง follow-up
- ข้อจำกัดและกรณีที่ไม่เหมาะ
- วิธีตรวจผลลัพธ์ก่อนนำไปใช้จริง

### 4. Examples are mandatory

ทุก production Gem ต้องมีอย่างน้อย:

`examples/USAGE_EXAMPLES.md`

ตัวอย่างต้องครอบคลุม:
- happy path
- minimal prompt
- detailed prompt
- revision prompt
- edge case ที่พบบ่อย

### 5. QA is mandatory

ทุก production Gem ต้องมีอย่างน้อย:

`qa/ACCEPTANCE_TESTS.md`

Critical QA ต้องครอบคลุม:
- user intent
- domain correctness
- required parameters/defaults
- output usability
- language correctnessเมื่อเกี่ยวข้อง
- layout/format correctnessเมื่อเกี่ยวข้อง
- unsupported-claim prevention

## Recommended Gem folder

```text
gems/<gem-id>/
├── GEM_INSTRUCTIONS_PRODUCTION.md
├── USER_GUIDE.md
├── OUTPUT_CONTRACT.md           # when needed
├── CONVERSATION_STARTERS.md     # when needed
├── policies/
├── examples/
│   └── USAGE_EXAMPLES.md
├── qa/
│   └── ACCEPTANCE_TESTS.md
├── schemas/                     # optional
└── assets/                      # optional
```

## Release gate

Gem ไม่ถือว่า production-ready จนกว่าจะผ่านทั้งหมด:

```text
PASS — practical use case defined
PASS — canonical instruction exists
PASS — defaults are documented
PASS — correctness/validation policy exists
PASS — USER_GUIDE.md exists
PASS — usage examples exist
PASS — acceptance tests exist
PASS — limitations/non-goals documented
```

## Priority order

เมื่อข้อกำหนดขัดกัน ให้ใช้หลักทั่วไป:

1. Safety / factual correctness
2. Domain and instructional correctness
3. Explicit user request
4. Practical usability
5. Accessibility/readability
6. Output consistency
7. Aesthetics/decorations

## Continuous improvement

เมื่อพบข้อผิดพลาดจากการใช้งานจริง ให้ปรับอย่างน้อยหนึ่งรายการตามความเหมาะสม:
- canonical instruction
- user guide
- acceptance/regression test
- example
- changelog

เป้าหมายคือให้ความผิดพลาดที่เคยพบกลายเป็น regression test เพื่อป้องกันการเกิดซ้ำ
