# MONEY_ENGINE — Money / Shopping Worksheets

Version: 1.0.0
Status: PRODUCTION_CANDIDATE

## Learning goals

Supports grade-appropriate tasks such as:

- identify value of coins/notes
- combine money amounts
- compare prices
- find total cost
- find change

## Core parameters

`CURRENCY`, `DENOMINATION_SET`, `QUESTION_TYPE`, `PRICE_RANGE`, `ITEM_COUNT`, `ALLOW_DECIMALS`, `TARGET_ANSWER_SET`, `ANSWER_FORMAT`

Default Thai context: `CURRENCY=THB`, use currently valid denomination concepts only when explicitly needed; avoid implying real-world availability if uncertain. For abstract arithmetic, use price labels rather than relying on exact banknote artwork.

## Deterministic arithmetic

- total = sum(item prices)
- change = amount_paid - total
- require amount_paid >= total
- all values use exact decimal arithmetic in the smallest currency unit when decimals are active

## Visual integrity

- price label must belong unambiguously to its item
- no duplicated/conflicting prices
- money icons are decorative unless exact denomination recognition is the learning objective
- if denomination recognition is taught, each coin/note value is academic data and requires explicit verification

## Answer integrity

Verified totals/change remain internal when answer key is off.

## QA

`PRICE_QA, SUM_QA, CHANGE_QA, CURRENCY_UNIT_QA, LABEL_ASSOCIATION_QA, ANSWER_LEAK_QA`

Incorrect arithmetic or ambiguous price association blocks release.

## Failure diagnosis and repair protocol

If price association, denomination validity, sum/change arithmetic, currency formatting, or answer-leak checks fail:

1. return to canonical monetary values in the smallest active currency unit;
2. recompute totals/change independently;
3. repair item-to-price or denomination associations at the data layer;
4. regenerate learner-visible labels/questions from the repaired data;
5. recheck uniqueness, affordability rule, formatting and answer leakage.

`MONEY_REPAIR_REQUIRES_DATA_RECOMPUTE=YES`

Never patch only a displayed total/change while retaining inconsistent prices or hidden state. Unresolved monetary inconsistency blocks release.
