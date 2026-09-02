# Default Page + Weight Dial Render Profile — Compatibility Note

Version: 1.1.0
Status: DEPRECATED AS NORMATIVE AUTHORITY
Compatible Gem baseline: 2.6.x

This file is retained only so older references do not break. It MUST NOT be used as an independent source of truth.

## Canonical ownership

Default page size/orientation is owned by:

`policies/PARAMETER_POLICY.md`

Current hard default when the user gives no explicit page override:

`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`
`PAGE_SIZE_PROVENANCE=SYSTEM_DEFAULT`
`ORIENTATION_PROVENANCE=SYSTEM_DEFAULT`

Primary-school learner-facing page/readability behavior is additionally governed by:

`policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md`

Canonical 0–5 kg @0.1 kg visible tick grammar is owned by:

`workers/W03_WEIGHT_SCALE.md`
`domains/SCALE_READING_ENGINE.md`
`policies/WEIGHT_DIAL_VISIBLE_TICK_SET_PROFILE.md`

The mandatory weight-dial facts remain:

`1 kg = 10 ขีด`
`1 ขีด = 0.1 kg = 100 g`
`5 ขีด = 0.5 kg`
`INTERVALS_PER_KG=10`
`POSITIONS_PER_KG_ENDPOINT_INCLUSIVE=11`
`INTERIOR_TICK_COUNT_PER_KG=9`
`HALF_KG_INTERMEDIATE_INDEX=5`

The +0.5 kg graduation is an existing intermediate position that is longer than ordinary minor ticks and shorter/weaker than whole-kilogram major ticks.

## Precedence

If any historical wording in this compatibility file conflicts with a canonical owner above, the canonical owner wins.

No future feature or defect fix should be added here. Update the owning SSOT and permanent regression instead.