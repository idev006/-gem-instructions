# Scale Reading Parameter Policy

Version: 1.1.0
Status: Canonical supporting policy for `DIAL_SCALE_READING`
Audience: teachers, Gem maintainers, automation workflows
Registry authority: `../domains/DOMAIN_REGISTRY.md`
Engine authority: `../domains/SCALE_READING_ENGINE.md`

## 1. Teacher-facing minimum

A teacher normally provides only:

- `GRADE_LEVEL`
- topic/skill such as `การอ่านตราชั่ง`
- `QUESTION_COUNT`

Example:

> ป.3 เรื่องการอ่านตราชั่ง 10 ข้อ

The Gem infers technical geometry and rendering safeguards unless explicitly overridden by a valid educational requirement.

## 2. Required parameters

| Parameter | Class | Rule |
|---|---|---|
| `GRADE_LEVEL` | REQUIRED | affects wording, difficulty, answer space, dial-size expectations |
| `TOPIC_OR_SKILL` | REQUIRED | normalize to `MEASUREMENT_WEIGHT / DIAL_SCALE_READING` |
| `QUESTION_COUNT` | REQUIRED | controls content and one-page/layout capacity |

## 3. Thai Grade 3 defaults

| Parameter | Class | Default |
|---|---|---|
| `SUBJECT` | OPTIONAL_AUTO | `คณิตศาสตร์` |
| `LEARNING_OBJECTIVE` | OPTIONAL_AUTO | read and state weight correctly from a graduated dial |
| `DIAL_MAX_KG` | OPTIONAL_DEFAULT | `5` |
| `MAJOR_DIVISION_KG` | OPTIONAL_DEFAULT | `1` |
| `MINOR_DIVISION_KG` | OPTIONAL_DEFAULT | `0.1` |
| `MINOR_DIVISIONS_PER_KG` | OPTIONAL_DEFAULT | `10` |
| `TICK_MEANING` | OPTIONAL_DEFAULT | `1 ขีด = 0.1 กิโลกรัม = 100 กรัม` |
| `ANSWER_FORMAT` | OPTIONAL_DEFAULT | `........ กิโลกรัม ........ ขีด` |
| `TARGET_WEIGHT_SET` | OPTIONAL_AUTO | progressive representable values within capacity |
| `ANSWER_DISTRIBUTION` | OPTIONAL_DEFAULT | `PROGRESSIVE` |
| `DIAL_SHAPE` | INTERNAL_LOCK | `TRUE_CIRCLE` |
| `DIAL_VIEW` | INTERNAL_LOCK | `FRONT_ORTHOGRAPHIC` |
| `DIAL_ASPECT_RATIO` | INTERNAL_LOCK | `1:1` |
| `CENTER_PIVOT_LOCK` | INTERNAL_LOCK | `ON` |
| `SINGLE_NEEDLE_ONLY` | INTERNAL_LOCK | `YES` |
| `NEEDLE_TARGET_MODE` | INTERNAL_LOCK | `EXACT_TICK` |
| `DIAL_TEMPLATE_LOCK` | INTERNAL_LOCK | `ON` |
| `DIAL_ACTIVE_SWEEP_DEG` | INTERNAL_LOCK | `300` |
| `DIAL_INACTIVE_GAP_DEG` | INTERNAL_LOCK | `60` |
| `DIAL_START_ANGLE_DEG` | INTERNAL_LOCK | `240` with 0°=top, clockwise positive |
| `DIAL_VALUE_DIRECTION` | INTERNAL_LOCK | `CLOCKWISE` |
| `DIAL_TICK_POSITIONS` | INTERNAL_LOCK | `51` including 0 and 5 endpoints |
| `DIAL_MIN_PRINT_DIAMETER_MM` | OPTIONAL_DEFAULT | `30` |
| `DIAL_PREFERRED_PRINT_DIAMETER_MM` | OPTIONAL_DEFAULT | `32–42` |
| `PAGE_SIZE` | OPTIONAL_DEFAULT | `A4` |
| `ORIENTATION` | OPTIONAL_DEFAULT | `PORTRAIT` |
| `ONE_PAGE_PREFERRED` | OPTIONAL_DEFAULT | `YES` |
| `ONE_PAGE_LOCK` | OPTIONAL_DEFAULT | `OFF` |
| `TARGET_PAGE_COUNT` | OPTIONAL_DEFAULT | `1` |
| `LAYOUT_MODE` | OPTIONAL_AUTO | 10 questions → try `2_COLUMNS_X_5_ROWS` first |
| `COLOR_MODE` | OPTIONAL_DEFAULT | `BLACK_AND_WHITE` |
| `DECORATION_DENSITY` | OPTIONAL_DEFAULT | `LOW` |
| `SHOW_ANSWER_KEY` | OPTIONAL_DEFAULT | `NO` |
| `ANSWER_LEAK_GUARD` | INTERNAL_LOCK | `ON` |
| `GEOMETRY_LOCK` | INTERNAL_LOCK | `ON` |
| `RENDER_PATH` | OPTIONAL_AUTO | `HYBRID` or `DETERMINISTIC_VECTOR` preferred |

## 4. Canonical 5 kg geometry

The 5 kg teaching dial uses a 300° active value sweep and a 60° inactive gap. Do not use a 360° value sweep because 0 kg and 5 kg would overlap.

Angle convention:

- `0° = top`
- clockwise is positive

Major-label mapping:

- 0 kg = 240°
- 1 kg = 300°
- 2 kg = 0°
- 3 kg = 60°
- 4 kg = 120°
- 5 kg = 180°

Therefore:

- 1 kg = 60°
- 0.1 kg = 6°
- 50 equal minor intervals across 300°
- 51 tick positions including endpoints
- no value tick in the 60° inactive gap from 5 back to 0

For target weight `w` under the 0.1 kg profile:

`tick_index = round(w / 0.1)`

`target_angle = (240 + tick_index*6) mod 360`

Target must be exactly representable within tolerance.

## 5. Default resolution rule

1. Explicit valid educational teacher value wins.
2. Otherwise use the defaults above.
3. Geometry invariants are not optional styling choices.
4. Record resolved educational parameters in `NORMALIZED_WORKSHEET_SPEC`.
5. Keep hidden render geometry internal/render-only.
6. Resolve render path before layout.
7. Run global one-page feasibility before pagination.
8. Never ask teachers to configure center pivot, tick spacing, sweep angles, template lock, or similar production safeguards.

## 6. One-page behavior

For 10 questions on A4 portrait, first attempt a 2×5 grid with equal square dial zones.

Preferred dial diameter: 32–42 mm; absolute minimum for 0.1 kg reading: 30 mm.

Optimization order follows the global policy: reduce decoration, choose a more efficient layout, shorten nonessential text, and reduce nonessential padding before considering pagination.

If the minimum dial size cannot fit:

- `ONE_PAGE_LOCK=OFF` → paginate after optimization;
- `ONE_PAGE_LOCK=ON` → return `ONE_PAGE_FEASIBILITY_QA=FAIL` and `LAYOUT_QA=FAIL`; do not create page 2 and do not shrink below 30 mm.

## 7. Natural-language examples

Teacher:

> ป.3 อ่านตราชั่ง 10 ข้อ ธีมสวนผัก ไม่ต้องมีเฉลย

Resolve internally to the 5 kg / 0.1 kg canonical profile, 300° sweep, true circle, exact center pivot, exact tick targeting, one-page-first 2×5 layout, and deterministic geometry-capable render path.

Teacher:

> ขอหน้าปัดใหญ่ ๆ อ่านง่าย

Interpret as a readability requirement: increase toward 32–42 mm, reduce decoration, preserve square geometry zones, and apply one-page policy without violating the 30 mm minimum.

Teacher:

> ใช้ตราชั่ง 10 กิโลกรัม ขีดละ 0.5 กก.

This changes the scale profile. Regenerate capacity, intervals, tick geometry, target mapping, minimum readability analysis, and all applicable QA. Do not reuse the locked 5 kg label mapping unless the new profile explicitly defines it.

## 8. Safety and governance

The teacher should never need to request basic correctness such as centered pivot, true circle, uniform ticks, one needle, or no perspective. These are production invariants.

Overall maturity is taken from `DOMAIN_REGISTRY.md`. This policy must not independently claim `PRODUCTION_HARDENED`.

If this policy conflicts with `SCALE_READING_ENGINE.md`, the engine's academic/geometry rule wins and the conflict is a governance defect that must be repaired.
