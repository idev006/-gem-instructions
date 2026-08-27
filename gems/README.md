# Gems Index

Each production Gem lives in its own folder under this directory.

Repository-wide production standard:

`docs/GEM_PRODUCTION_STANDARD.md`

## Folder convention

`gems/<gem-id>/`

Each Gem must keep its canonical instruction at:

`gems/<gem-id>/GEM_INSTRUCTIONS_PRODUCTION.md`

Every production Gem must also include:

- `USER_GUIDE.md` — คู่มือสำหรับผู้ใช้
- `examples/USAGE_EXAMPLES.md` — ตัวอย่างการสั่งงาน
- `qa/ACCEPTANCE_TESTS.md` — critical acceptance tests

Optional supporting directories:

- `policies/` — Gem-specific policies
- `schemas/` — machine-readable schemas
- `assets/` — Gem-specific supporting assets

Optional supporting files:

- `CONVERSATION_STARTERS.md`
- `OUTPUT_CONTRACT.md`
- `README.md`

## Production design principles

Gem ใหม่ทุกตัวต้องออกแบบโดยให้ความสำคัญกับ:

1. ประโยชน์ในการนำไปใช้จริง
2. ความถูกต้องของเนื้อหา/ตรรกะ/ภาษา
3. ความเหมาะสมกับผู้ใช้และบริบท
4. ความอ่านง่ายและใช้งานได้จริง
5. ความสวยงามและการตกแต่ง

A Gem is not considered production-ready if it has only a prompt/instruction but lacks a user guide, examples, validation rules, and acceptance tests.

## Current Gem IDs

- `worksheet-generator`
- `color-by-code`
- `themed-hub-worksheet`
- `geometric-color-by-code`

When adding a new Gem, create a new sibling folder. Do not place its canonical files directly at repository root or mix them with another Gem.
