# CLOCK_READING_ENGINE — Analog Clock Reading

Version: 1.3.0
Status: PRODUCTION_CANDIDATE
Requires: `INSTRUMENT_READING_ENGINE.md`
Registry authority: `domains/DOMAIN_REGISTRY.md`

## Learning goal
Student reads hour and minute from an analog clock accurately and, when requested, connects one analog geometry to valid day/night 24-hour readings.

## Core parameters
`CLOCK_FORMAT=12_HOUR`, `MINUTE_GRANULARITY`, `SHOW_MINUTE_MARKS`, `SHOW_NUMBERS`, `HOUR_HAND_MODE`, `ANSWER_FORMAT`, `TARGET_TIMES`, `CLOCK_READING_MODE=SINGLE|DAY_NIGHT_PAIR`, `ANSWER_TIME_FORMAT=12_HOUR|24_HOUR`.

Suggested progression: EASY whole/half hours; MEDIUM 5-minute intervals; HARD 1-minute intervals when grade-appropriate.

## Geometry invariants
- perfect circular face in square reserved box
- exact center pivot
- exactly two instructional hands unless seconds requested
- minute hand visibly longer than hour hand
- 12 hour positions evenly spaced
- standard clockwise grammar: 12 top, 3 right, 6 bottom, 9 left
- no decorative pointer/hand

## Deterministic minute-mark topology
A clock is cyclic. For a full minute-mark face:
- exactly 60 equal minute intervals around 360°
- exactly 60 distinct minute positions
- 6° spacing
- 12 hour positions every fifth minute mark = 30°
- minute 0/60 is one shared position at 12; never duplicate the tick
- major hour marks may be stronger but do not add positions
- no missing/duplicated/merged/extra minute positions

## Continuous hand placement — CRITICAL
For analog time `h:m`:
- `minute_hand_angle_deg = 6*m` clockwise from 12
- `hour_hand_angle_deg = 30*(h mod 12) + 0.5*m` clockwise from 12

The hour hand moves continuously. It is permitted to point exactly at an hour numeral only when `m=00`.

Mandatory relational interpretation:
- `m=15` → hour hand is 25% of the way from h to h+1
- `m=30` → hour hand is exactly halfway from h to h+1
- `m=45` → hour hand is 75% of the way from h to h+1

Example: `10:30` MUST place the hour hand exactly halfway between 10 and 11; it MUST NOT point directly at 10.

Any rendered nonzero-minute clock whose hour hand remains on the original hour numeral is `CRITICAL_ACADEMIC`.

## Deterministic vector hand construction — MANDATORY
Angle text alone is not sufficient for a learner-read clock. Every hand MUST be constructed from the canonical center using an explicit radial endpoint.

Let the clock center be `C=(cx,cy)`, with 0° at 12 o'clock and positive angles clockwise. For any hand angle `θ` in degrees:

`dx = sin(radians(θ))`
`dy = -cos(radians(θ))`

For normalized clock radius `R`:

`MINUTE_HAND_LENGTH = 0.78*R`
`HOUR_HAND_LENGTH = 0.55*R`

Then:

`minute_endpoint = (cx + 0.78*R*sin(radians(minute_hand_angle_deg)), cy - 0.78*R*cos(radians(minute_hand_angle_deg)))`

`hour_endpoint = (cx + 0.55*R*sin(radians(hour_hand_angle_deg)), cy - 0.55*R*cos(radians(hour_hand_angle_deg)))`

Both hands MUST be rendered as straight radial segments from exactly `C` to their computed endpoints. The renderer MUST NOT independently reposition, rotate, snap, aesthetically adjust, or approximate either endpoint.

Equivalent deterministic transform is allowed only when mathematically identical:

`HAND = rotate(canonical_vertical_hand, θ, around=C)`

where `θ` is the exact formula-derived angle and `C` is the exact shared pivot.

### Collinearity oracle
For each hand, the vector `endpoint-C` MUST be collinear with the unit direction `(sin θ, -cos θ)`. A hand that visually reaches a plausible numeral but is not on the exact computed ray is wrong.

### Anti-snap oracle
For every `m != 0`:

`abs(hour_hand_angle_deg - 30*(h mod 12)) = 0.5*m`

modulo 360 where needed. Therefore:
- :15 requires 7.5° displacement;
- :30 requires 15° displacement;
- :45 requires 22.5° displacement.

No typography, layout pressure, or visual balancing may reduce that displacement.

## Prompt serialization redundancy
For every item, the final image prompt MUST serialize geometry and human-readable relation. Required renderer-only fields:

- `SEMANTIC_TARGET`
- `CLOCK_CENTER`
- `CLOCK_RADIUS`
- `MINUTE_HAND_ANGLE_DEG`
- `HOUR_HAND_ANGLE_DEG`
- `MINUTE_HAND_LENGTH_RATIO=0.78`
- `HOUR_HAND_LENGTH_RATIO=0.55`
- `MINUTE_ENDPOINT_NORMALIZED`
- `HOUR_ENDPOINT_NORMALIZED`
- `RELATIONAL_VERIFICATION`
- `ITEM_SPECIFIC_HARD_NEGATIVE`

Normalized endpoint coordinates may use center `(0,0)` and `R=1`; downstream layout scales/translates the whole clock uniformly without changing direction.

Example for 3:30:
- minute angle = 180°
- hour angle = 105°
- normalized minute endpoint ≈ `(0.000000, 0.780000)`
- normalized hour endpoint ≈ `(0.531259, 0.142350)`
- relation = `hour hand exactly halfway between 3 and 4`
- hard negative = `NEVER place the hour hand directly on 3 or 4`

Do not rely on only a semantic phrase such as “3:30”. Do not rely on only angles. Do not rely on a renderer to infer where the endpoint should be. Use angle + explicit endpoint + relational wording.

For all nonzero-minute items add an item-specific negative such as:
`WRONG: hour hand directly on the starting hour numeral.`

## DAY_NIGHT_PAIR
One question = one clock + two blank response fields. Do not create two clocks unless explicitly requested.

Thai mapping:
- h12 1–5: DAY=h+12, NIGHT=h
- h12 6–11: DAY=h, NIGHT=h+12
- h12=12: DAY=12, NIGHT=0
Minutes remain identical.

Verified day/night values remain internal when key is off. Renderer geometry may be serialized but must not be printed as answers.

## Layout
Preferred printed diameter >=30 mm for 5-minute reading; larger for 1-minute reading. For 10 items A4 portrait, first attempt 2×5 only if hand positions and minute marks remain distinguishable. Readability outranks one-page density.

## Mandatory final-prompt block
```text
CLOCK GEOMETRY — CRITICAL — DETERMINISTIC VECTOR
- use one canonical circular clock template for all items
- exactly 12 hour positions; full minute face = exactly 60 distinct minute marks at 6° spacing
- exactly two hands; minute hand longer
- both hands start at the exact same clock center C
- minute angle = 6*m
- hour angle = 30*(h mod 12)+0.5*m
- minute endpoint = C + 0.78R*(sin(minute_angle), -cos(minute_angle))
- hour endpoint = C + 0.55R*(sin(hour_angle), -cos(hour_angle))
- draw each hand as the straight segment from C to its exact computed endpoint
- DO NOT snap/approximate/reposition an endpoint to a numeral or tick
- if m != 00, hour hand must NOT stay on the hour numeral
- at :30 hour hand is exactly halfway between adjacent hour numerals
- serialize per-item exact angles + normalized endpoints + visual relation + hard negative
- no decorative extra hands, no ellipse, no perspective, no missing/extra minute marks
```

## Post-render QA
Inspect every clock individually:
- 60 distinct minute positions when full marks shown
- exact hand count/length hierarchy
- exact shared center
- minute hand on target minute
- hour hand on computed continuous angle
- endpoint-to-center vector collinear with formula direction
- for every `m!=00`, verify hour hand is displaced from the hour numeral by exactly `0.5*m` degrees
- for `:30`, verify midpoint visually and geometrically
- for `:15/:45`, verify 25%/75% sector position
- no answer leakage

## QA
`CLOCK_CIRCLE_QA, CLOCK_PIVOT_QA, HAND_COUNT_QA, HAND_LENGTH_QA, MINUTE_INTERVAL_COUNT_QA, MINUTE_POSITION_COUNT_QA, MINUTE_MARK_SPACING_QA, HOUR_POSITION_QA, HOUR_HAND_INTERPOLATION_QA, NONZERO_MINUTE_HOUR_DISPLACEMENT_QA, HALF_HOUR_MIDPOINT_QA, CLOCK_HAND_VECTOR_ENDPOINT_QA, CLOCK_HAND_RADIAL_COLLINEARITY_QA, CLOCK_HAND_ANTI_SNAP_QA, TARGET_TIME_QA, NO_MISSING_TICK_QA, NO_EXTRA_TICK_QA, MINIMUM_SIZE_QA, ONE_CLOCK_TWO_ANSWERS_QA, DAY_NIGHT_MAPPING_QA, DAY_NIGHT_ANSWER_LEAK_QA`.

Any wrong hand position, especially an hour hand pinned to the hour numeral when minutes are nonzero or an endpoint that does not match its formula-derived radial vector, blocks release.
