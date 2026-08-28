# Geometric Color-by-Code — Answer-First Generation Policy

Version: 1.0.0
Status: Production policy

## Purpose

ป้องกันปัญหาโจทย์มีคำตอบที่ไม่มีรหัสสีรองรับ โดยกำหนดให้ Color-by-Code ใช้ **Answer/Code-First Generation** เป็นค่าเริ่มต้น: วางแผนสีและคำตอบเป้าหมายก่อน แล้วจึงสร้างโจทย์ให้ได้คำตอบนั้นอย่างถูกต้องตามเงื่อนไขวิชา

## Root cause addressed

Anti-pattern เดิม:

```text
Generate Question
→ Compute Answer
→ Try to map answer to a color
```

วิธีนี้อาจสร้างคำตอบนอก active legend ทำให้ region ไม่มีสีที่นักเรียนต้องใช้

Production pattern ใหม่:

```text
Resolve Color Count
→ Choose Active Answer/Code Set
→ Assign one Color ID per Active Answer/Code
→ Plan usage count per color
→ Assign target answer/code to every question region
→ Generate a valid question from the target answer/code
→ Validate academic constraints
→ Freeze Question/Answer/Color/Region mapping
→ Validate 100% legend coverage
→ Render
```

## Hard rule

```text
NO QUESTION MAY PRODUCE AN ANSWER/CODE OUTSIDE THE ACTIVE LEGEND.
```

ถ้าพบแม้ 1 ข้อที่ `normalized_answer_code` ไม่มี `color_id` ใน active legend = Critical FAIL และห้าม render final worksheet.

## Canonical generation direction

Default:

```text
CONTENT_GENERATION_MODE = ANSWER_FIRST
ACTIVE_CODE_SET = RESOLVED_BEFORE_QUESTION_GENERATION
COLOR_USAGE_PLAN = FROZEN_BEFORE_QUESTION_GENERATION
QUESTION_GENERATION_SOURCE = TARGET_ANSWER_OR_CODE
```

อนุญาต `QUESTION_FIRST` เฉพาะกรณีที่ source questions ถูกผู้ใช้กำหนดไว้แล้วหรือเป็น fixed external content และระบบสามารถพิสูจน์ได้ว่า active legend ครอบคลุมคำตอบทั้งหมด 100% ก่อน render.

## Numeric / Mathematics generation

สำหรับโจทย์คณิตศาสตร์:

1. เลือก target answer จาก active legend
2. สร้าง operands/operator ที่ให้ target answer
3. ตรวจ grade/topic constraints
4. ตรวจ domain constraints เช่นจำนวนหลัก, ไม่มีเศษ, ไม่ติดลบ, denominator policy ฯลฯ
5. ตรวจซ้ำด้วย independent calculation

ตัวอย่าง: ป.3 การหารลงตัว ตัวตั้ง 2 หลัก ÷ ตัวหาร 1 หลัก

ถ้า active legend คือคำตอบ `{2,3,4,5,6,7}` และ region ต้องเป็นสีเขียวที่ map กับ `5`:

```text
20 ÷ 4 = 5
25 ÷ 5 = 5
30 ÷ 6 = 5
35 ÷ 7 = 5
40 ÷ 8 = 5
45 ÷ 9 = 5
```

ต้องเลือกเฉพาะโจทย์ที่ผ่านเงื่อนไขผู้ใช้ทั้งหมด.

## Non-math generation

ใช้หลักเดียวกันกับคำศัพท์/หมวดหมู่:

```text
Target category/code
→ generate/select prompt whose verified answer belongs to that category/code
→ validate
→ freeze mapping
```

ห้ามสร้างคำถามก่อนแล้วค่อยเพิ่ม category/color แบบเดาเพื่อให้ครบสี.

## Distribution planning

ก่อนสร้างคำถามต้องกำหนด:

```text
question_count
color_count
active_answer_or_code_set
usage_target_per_color
```

ตัวอย่าง 48 ข้อ / 6 สี:

```text
8 regions per color target
```

ถ้าหารไม่ลงตัว ให้กระจายต่างกันได้ไม่เกินที่จำเป็น โดยผลรวมต้องเท่ากับ `QUESTION_COUNT` และทุกสีที่แสดงต้องมี usage >= 1.

## Required mapping record

ทุกข้อ/region ต้องมี record ก่อน render:

```text
question_id
region_id
target_answer_or_code
prompt_text
verified_correct_answer
normalized_answer_code
color_id
legend_entry_id
validation_status
```

ต้องเป็นจริงว่า:

```text
target_answer_or_code == normalized_answer_code
verified_correct_answer normalizes to normalized_answer_code
color_id == active_legend[normalized_answer_code]
validation_status == PASS
```

## Pre-render completeness gate

ก่อน render ต้อง PASS ทั้งหมด:

```text
question_count == requested_question_count
region_count == question_count
all questions validated
all normalized answers/codes ∈ active legend
all regions have color_id
all displayed legend entries have usage >= 1
sum(color usage counts) == question_count
no answer/code maps to multiple colors
no orphan question
no orphan region
no orphan legend entry
```

## Revision behavior

- เปลี่ยนจำนวนสี → rebuild active code set + distribution + affected questions before render
- เปลี่ยน topic constraints → regenerate invalid questions from the same target codes when possible
- เปลี่ยน palette colors only → preserve target answers/codes and questions; remap color values/labels deterministically
- เปลี่ยน question count → recompute usage distribution first, then add/remove questions from target codes

## Critical FAIL cases

FAIL เมื่อ:
- question generated before active answer/code set is resolved in a normal generative worksheet
- any answer has no legend color
- any legend color cannot be reached by at least one question when displayed
- image model invents arithmetic/questions after mapping freeze
- visual generation changes question text so the answer changes
- a division question violates the requested exact-division constraint
- a numeric target cannot be generated within the requested grade/topic constraints and the system silently substitutes an out-of-legend answer

## Priority

```text
ACADEMIC CORRECTNESS
> COMPLETE ANSWER/CODE COVERAGE
> MAPPING INTEGRITY
> COLOR DISTRIBUTION
> VISUAL BALANCE
> DECORATION
```
