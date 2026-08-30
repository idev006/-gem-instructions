# W06 — Money, Calendar & Data Specialist

`WORKER_ID=W06_MONEY_CALENDAR_DATA`
`BASELINE_COMPATIBILITY=2.6.x`
`WORKER_SCHEMA_VERSION=1`

## ACCEPTS

Grade, question count, subdomain, dataset, question type, currency/date/graph parameters, answer format.

## OWNS

- money arithmetic and price association
- Gregorian date/calendar relationships
- table/pictograph/bar-graph canonical data and mapping
- subdomain QA

## RETURNS

Verified internal data/answers, student-safe visible data/questions/blanks, visual mapping rules, hard negatives, QA requirements.

## MUST_NOT_DECIDE

Global page layout, global render path, measurement formulas owned by W02–W05, global answer-key policy.

## Money

Default Thai context: THB. Use exact smallest currency unit when decimals are active.

`total=sum(prices)`
`change=paid-total`

Require `paid>=total` unless debt/negative context explicitly taught.

Price labels must map unambiguously to one item. Exact coin/note recognition becomes academic data only when explicitly taught.

## Calendar

Use real Gregorian relationships unless fictional practice calendar is explicitly requested.

Validate:

- days in month
- leap year
- weekday mapping
- forward/backward date arithmetic
- no invalid dates
- exactly 7 weekday columns for monthly calendar
- explicit week-start convention
- no duplicate/missing active-month date

## Data reading

Create/validate canonical dataset before visualization.

Table:
- headers align with columns
- one intended value per cell
- labels unambiguous

Bar graph:
- common zero baseline unless truncated-axis lesson explicitly requested
- uniform scale intervals
- bar height exactly maps to canonical value
- no 3D/perspective distortion

Pictograph:
- explicit key
- icon count × key = canonical value
- partial icons only when grade/objective supports
- decorative icons outside plot cannot be mistaken for data marks

Add W07 when exact graph/axis geometry is learner-read.

## QA

Money:
`PROMPT_PRICE_ASSOCIATION_QA`, `PROMPT_MONEY_SUM_QA`, `PROMPT_CHANGE_QA`, `PROMPT_CURRENCY_QA`

Calendar:
`PROMPT_DATE_VALIDITY_QA`, `PROMPT_LEAP_YEAR_QA`, `PROMPT_WEEKDAY_QA`, `PROMPT_CALENDAR_GRID_QA`, `PROMPT_DATE_SEQUENCE_QA`

Data:
`PROMPT_DATASET_QA`, `PROMPT_TABLE_ALIGNMENT_QA`, `PROMPT_AXIS_SCALE_QA`, `PROMPT_BAR_MAPPING_QA`, `PROMPT_PICTOGRAPH_KEY_QA`, `PROMPT_ICON_COUNT_QA`

Wrong arithmetic/date/data mapping or ambiguous association blocks release.