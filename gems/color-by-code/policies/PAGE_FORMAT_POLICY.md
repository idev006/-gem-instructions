# Color-by-Code Page Format Policy

Version: 1.0.0
Status: Active SSOT Policy

## Default

```text
PAGE_SIZE = A4
ORIENTATION = PORTRAIT
```

Default output is **A4 แนวตั้ง**.

## User-configurable page size

The user may explicitly choose the paper size. Support at least:

- A4
- A3
- A5
- Letter
- Legal

If the user does not specify a paper size, use A4.

## User-configurable orientation

The user may explicitly choose:

- `PORTRAIT` = แนวตั้ง
- `LANDSCAPE` = แนวนอน

If the user does not specify orientation, use Portrait.

## Natural-language examples

- `A4 แนวตั้ง`
- `A4 แนวนอน`
- `A3 แนวนอน`
- `Letter แนวตั้ง`

## Layout rule

When page size or orientation changes, recalculate the complete layout rather than stretching an existing page. Recalculate:

- usable page area
- safe margins
- coloring-region sizes
- question placement
- legend placement
- font sizes where needed
- pagination

Do not distort illustrations or shrink text/regions below usable classroom size simply to fit the requested page.

## Priority

User-specified page size and orientation override defaults, provided the requested format can be rendered safely. If not explicitly specified, always use **A4 Portrait**.
