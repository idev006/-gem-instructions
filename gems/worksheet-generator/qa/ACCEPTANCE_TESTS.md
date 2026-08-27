# Acceptance Tests

These tests validate the canonical Gem instruction before a production release.

## AT-01 — Quick teacher command

Input:

`ป.3 3 หลัก × 1 หลัก ง่าย 10 ข้อ ธีมรถแข่ง`

Expected:

- no unnecessary clarification
- grade = ป.3
- multiplicand = exactly 3 digits
- multiplier = exactly 1 digit
- difficulty = EASY
- question count = 10
- theme = racing
- A4 portrait default
- answer key included by default

## AT-02 — Exact digit enforcement

Input:

`ป.4 4 หลัก × 2 หลัก ปานกลาง 10 ข้อ`

Failure examples:

- any 3-digit multiplicand
- any 1-digit multiplier

Expected: reject/regenerate invalid candidates.

## AT-03 — Mathematics

For every accepted item:

- direct multiplication must equal decomposition/partial-product check
- answer key must use the validated answer

Any mismatch = FAIL.

## AT-04 — Multi-digit layout

Input:

`ป.4 4 หลัก × 2 หลัก ปานกลาง`

Expected:

- place-value right alignment
- room for 2 partial products
- no reuse of a 1-digit multiplier grid

## AT-05 — Large layout

Input:

`ป.5 5 หลัก × 3 หลัก ยาก 10 ข้อ`

Expected:

- room for 3 partial products
- automatic pagination when needed
- handwriting space not compressed merely to keep all 10 items on one page

## AT-06 — Revision continuity

First input:

`ป.3 3 หลัก × 1 หลัก ปานกลาง 10 ข้อ รถแข่ง`

Follow-up:

`ขออีกชุด ยากขึ้นนิดนึง`

Expected:

- preserve grade, digit sizes, count, and theme
- generate new questions
- move difficulty slightly upward within scope
- avoid prior questions when possible

## AT-07 — Photocopy mode

Input:

`ทำสำหรับถ่ายเอกสาร`

Expected:

- monochrome/high contrast
- white background
- low ink
- no information conveyed only by color

## AT-08 — Honest file claim

If the environment cannot create an actual PDF:

Expected:

- do not say `PDF พร้อมดาวน์โหลด`
- do not fabricate a link

If a file was actually created and validated, it may be described as created.

## AT-09 — Answer-key consistency

Expected for every worksheet:

- same number of items
- same numbering
- same operands
- mathematically correct answer for every item

Any mismatch = FAIL.

## AT-10 — A4 print safety

Expected:

- A4 210 × 297 mm when A4 output is available
- safe margins
- no clipped text
- no grid/footer collisions
- adequate writing space

## Release criterion

A production instruction revision must pass all critical acceptance tests before being marked stable.