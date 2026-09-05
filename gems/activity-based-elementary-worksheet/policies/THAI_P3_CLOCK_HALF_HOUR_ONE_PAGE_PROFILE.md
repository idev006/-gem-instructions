# Thai P3 Analog Clock Half-Hour One-Page Profile

Version: 1.0.0
Status: Mandatory derived layout profile
Applies when all are true:
- Grade = Thai Primary 3 / ป.3
- skill = ANALOG_CLOCK
- CLOCK_READING_MODE=DAY_NIGHT_PAIR
- QUESTION_COUNT=10
- TARGET_MINUTE_MODE=EXACT_MINUTE_SET
- TARGET_MINUTE_SET={30}
- page size/orientation are not explicitly overridden by user
- no unusually large accessibility typography or other explicit layout override is requested

## Page truth

Default page remains:
`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`
`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

This profile does NOT fabricate explicit user provenance for `ONE_PAGE_LOCK=ON`.

Instead it provides a canonical numerically proved one-page candidate. When its dimensions are preserved and the physical packing inequalities pass, one-page output becomes mandatory for this exact profile:

`FEASIBILITY_CONFIRMED_ONE_PAGE_LAYOUT_REQUIRED=YES`

The renderer must not paginate merely for visual spaciousness after the one-page proof has passed.

## Canonical 2×5 packing candidate

A4 portrait:
- PAGE_WIDTH_MM=210
- PAGE_HEIGHT_MM=297
- MARGIN_LEFT_MM=8
- MARGIN_RIGHT_MM=8
- MARGIN_TOP_MM=8
- MARGIN_BOTTOM_MM=8
- HEADER_TITLE_DIRECTIONS_HEIGHT_MM=38
- FOOTER_RESERVED_HEIGHT_MM=0

Therefore:
- USABLE_WIDTH_MM=194
- USABLE_HEIGHT_MM=243

Grid:
- GRID_COLUMNS=2
- GRID_ROWS=5
- ITEM_MIN_WIDTH_MM=91
- ITEM_MIN_HEIGHT_MM=43
- COLUMN_GAP_MM=4
- ROW_GAP_MM=4

Required:
- REQUIRED_GRID_WIDTH_MM=2×91+4=186 <=194
- REQUIRED_GRID_HEIGHT_MM=5×43+4×4=231 <=243

Hence:
`WIDTH_FEASIBLE=YES`
`HEIGHT_FEASIBLE=YES`
`PAGE_FEASIBILITY_VERDICT=PASS`

## Item composition

Each item uses a horizontal composition inside the 91×43 mm box:
- circular clock zone: nominal diameter 34–36 mm;
- question number near the upper-left of the item, outside the clock face;
- two compact response fields placed to the right of the clock, one for กลางวัน and one for กลางคืน;
- response fields are not stacked below the clock in a way that increases item height beyond 43 mm;
- no decorative art may consume the clock or response budget.

The clock must remain large enough for 60 minute positions, 12 numerals and two clearly distinguishable hands.

## Geometry coupling

The one-page layout may uniformly scale/translate the complete clock object only.
It MUST NOT:
- rotate a hand independently;
- snap the hour hand toward a numeral;
- distort the circular face;
- merge/remove minute ticks;
- shorten answer fields below pedagogy minimum merely to fit.

## Page decision

If the canonical candidate passes exactly as above:
`PROMPT_CLOCK_P3_HALF_HOUR_10_ITEM_ONE_PAGE_QA=PASS`
`PROMPT_CLOCK_P3_HALF_HOUR_2X5_QA=PASS`

Pagination is allowed only when a documented explicit override or a changed audited minimum makes one of the packing inequalities fail. In that case W08/W10 must serialize the changed dimensions and the failed inequality.

## Artifact defect

A rendered page that shows only five of the ten requested items while this canonical state remains feasible is:
`ARTIFACT_PAGE_COUNT_QA=FAIL`
`ARTIFACT_LAYOUT_COMPLETENESS_QA=FAIL`

This is separate from clock-hand geometry QA.
