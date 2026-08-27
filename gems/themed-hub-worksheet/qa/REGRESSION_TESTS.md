# Themed Hub Worksheet — Regression Tests

Version: 1.0.0

## Purpose

ป้องกันข้อผิดพลาดที่เคยพบหรือมีความเสี่ยงสูงในการสร้าง prompt สำหรับใบงาน Themed Hub

## R-01 Default preservation

Input:
```text
ป.1 ภาษาไทย สระอา 8 ช่อง
```
Expected:
- A4 Portrait
- 8 slots
- Thai-first
- monochrome main art
- object/theme/layout resolved automatically

## R-02 Exact slot count

Input:
```text
ป.3 ภาษาไทย มาตราตัวสะกด 10 ช่อง ดอกไม้
```
Expected: exactly 10 instructional slots in blueprint.

## R-03 Pagination over compression

Input:
```text
ป.3 ภาษาไทย คำควบกล้ำ 24 ช่อง A4 แนวตั้ง
```
Expected: multiple pages or equivalent usable page plan; never 24 tiny unusable slots on one page.

## R-04 Revision preservation

Base:
```text
ป.2 คณิตศาสตร์ แม่ 4 8 ช่อง พิซซ่า A4 แนวตั้ง
```
Revision:
```text
เปลี่ยนเป็นดอกไม้
```
Expected: only object/layout adaptations change. Academic content, grade, topic, count, page size and orientation remain.

## R-05 No theme contamination

Input:
```text
ป.5 วิทยาศาสตร์ ระบบสุริยะ 8 ช่อง ธีมอาหาร
```
Expected: theme affects decoration/container only; scientific names/facts remain correct.

## R-06 Thai exact-text protection

When final prompt contains important Thai title/instruction text, it must be supplied as exact text and must not instruct the visual model to paraphrase it.

## R-07 Long response safety

Input requests long explanations in radial slots.
Expected: activity is shortened appropriately or layout/pagination changes. FAIL on tiny text.

## R-08 Open-ended conversion

Input:
```text
ป.5 สังคมศึกษา ให้แสดงความคิดเห็นเรื่องพลเมืองดี 8 ช่อง
```
Expected: convert to a short-response activity only when the learning intent can be preserved; otherwise state that this worksheet format is not ideal.

## R-09 Answer-key SSOT

When `ANSWER_KEY=YES`, worksheet prompts and answer key must derive from one Verified Content Blueprint.

## R-10 Honest output

If only a prompt is produced, response must not say that a PDF/image file has already been generated or checked.

## R-11 AUTO without unnecessary questions

When subject, topic, and intended activity are inferable, missing object/theme/layout should resolve with AUTO rather than triggering clarification.

## R-12 Academic uncertainty

If required content cannot be verified confidently, do not invent it. Ask only for genuinely missing critical information or keep the prompt at a structure-only level until content is verified.
