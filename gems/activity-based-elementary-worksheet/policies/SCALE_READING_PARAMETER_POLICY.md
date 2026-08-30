# Scale Reading Parameter Policy

Version: 1.0.0
Status: Canonical supporting policy for `DIAL_SCALE_READING`
Audience: teachers, Gem maintainers, automation workflows

## 1. Teacher-facing minimum

A teacher should normally need to provide only:

- `GRADE_LEVEL`
- topic/skill such as `การอ่านตราชั่ง`
- `QUESTION_COUNT`

Example:

> ป.3 เรื่องการอ่านตราชั่ง 10 ข้อ

The Gem should infer the rest unless the teacher explicitly overrides it.

## 2. Required parameters

| Parameter | Class | Rule |
|---|---|---|
| `GRADE_LEVEL` | REQUIRED | affects wording, difficulty, dial size expectations |
| `TOPIC_OR_SKILL` | REQUIRED | normalize to `MEASUREMENT_WEIGHT / DIAL_SCALE_READING` |
| `QUESTION_COUNT` | REQUIRED | controls content and layout capacity |

## 3. Optional defaults for Thai Grade 3 scale reading

| Parameter | Class | Default |
|---|---|---|
| `SUBJECT` | OPTIONAL_AUTO | `คณิตศาสตร์` |
| `LEARNING_OBJECTIVE` | OPTIONAL_AUTO | read and state weight correctly from a dial |
| `DIAL_MAX_KG` | OPTIONAL_DEFAULT | `5` |
| `MAJOR_DIVISION_KG` | OPTIONAL_DEFAULT | `1` |
| `MINOR_DIVISION_KG` | OPTIONAL_DEFAULT | `0.1` |
| `MINOR_DIVISIONS_PER_KG` | OPTIONAL_DEFAULT | `10` |
| `TICK_MEANING` | OPTIONAL_DEFAULT | `1 ขีด = 0.1 กิโลกรัม = 100 กรัม` |
| `ANSWER_FORMAT` | OPTIONAL_DEFAULT | `........ กิโลกรัม ........ ขีด` |
| `TARGET_WEIGHT_SET` | OPTIONAL_AUTO | progressive valid values within capacity |
| `ANSWER_DISTRIBUTION` | OPTIONAL_DEFAULT | `PROGRESSIVE` |
| `DIAL_SHAPE` | INTERNAL_LOCK | `TRUE_CIRCLE` |
| `DIAL_VIEW` | INTERNAL_LOCK | `FRONT_ORTHOGRAPHIC` |
| `DIAL_ASPECT_RATIO` | INTERNAL_LOCK | `1:1` |
| `CENTER_PIVOT_LOCK` | INTERNAL_LOCK | `ON` |
| `SINGLE_NEEDLE_ONLY` | INTERNAL_LOCK | `YES` |
| `NEEDLE_TARGET_MODE` | INTERNAL_LOCK | `EXACT_TICK` |
| `DIAL_TEMPLATE_LOCK` | INTERNAL_LOCK | `ON` |
| `DIAL_MIN_PRINT_DIAMETER_MM` | OPTIONAL_DEFAULT | `30` |
| `DIAL_PREFERRED_PRINT_DIAMETER_MM` | OPTIONAL_DEFAULT | `32–42` |
| `PAGE_SIZE` | OPTIONAL_DEFAULT | `A4` |
| `ORIENTATION` | OPTIONAL_DEFAULT | `PORTRAIT` |
| `LAYOUT_MODE` | OPTIONAL_AUTO | 10 questions → `2_COLUMNS_X_5_ROWS` |
| `COLOR_MODE` | OPTIONAL_DEFAULT | `BLACK_AND_WHITE` |
| `DECORATION_DENSITY` | OPTIONAL_DEFAULT | `LOW` for scale reading |
| `SHOW_ANSWER_KEY` | OPTIONAL_DEFAULT | `NO` |
| `ANSWER_LEAK_GUARD` | INTERNAL_LOCK | `ON` |
| `GEOMETRY_LOCK` | INTERNAL_LOCK | `ON` |
| `DETERMINISTIC_DIAL_OVERLAY` | OPTIONAL_AUTO | prefer when execution environment supports vector/SVG overlay |

## 4. Default resolution rule

1. Explicit valid teacher value wins.
2. Otherwise use the scale-reading defaults above.
3. Record every resolved value in `NORMALIZED_WORKSHEET_SPEC`.
4. Do not ask teachers to configure geometry locks.
5. If a requested question density would force dial diameter below 30 mm, change layout/paginate instead of silently shrinking.

## 5. Natural language examples

Teacher:

> ป.3 อ่านตราชั่ง 10 ข้อ ธีมสวนผัก ไม่ต้องมีเฉลย

Resolve internally to:

```text
DOMAIN = MEASUREMENT_WEIGHT
QUESTION_TYPE = DIAL_SCALE_READING
DIAL_MAX_KG = 5
MINOR_DIVISION_KG = 0.1
MINOR_DIVISIONS_PER_KG = 10
ANSWER_FORMAT = ........ กิโลกรัม ........ ขีด
CENTER_PIVOT_LOCK = ON
DIAL_TEMPLATE_LOCK = ON
LAYOUT_MODE = 2_COLUMNS_X_5_ROWS
DECORATION_DENSITY = LOW
SHOW_ANSWER_KEY = NO
```

Teacher:

> ขอหน้าปัดใหญ่ ๆ อ่านง่าย

Interpret as a readability requirement, not merely a visual preference:

- increase dial diameter toward preferred 32–42 mm;
- reduce decoration;
- preserve square dial zones;
- paginate if necessary.

Teacher:

> ใช้ตราชั่ง 10 กิโลกรัม ขีดละ 0.5 กก.

Override capacity/division parameters and regenerate tick geometry. Do not keep the 5 kg/0.1 kg defaults.

## 6. Safety rule

The teacher should never be required to say:

- center the pivot;
- make the dial circular;
- keep ticks evenly spaced;
- lock aspect ratio;
- use exactly one needle.

Those are internal production invariants and must be enforced automatically.