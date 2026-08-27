# Themed Hub Worksheet — Acceptance Tests

## Critical

1. Default page is A4 Portrait when not specified.
2. Default slot count is 8 when not specified.
3. Subject and topic must remain academically correct after theme/object adaptation.
4. Main worksheet artwork is monochrome by default.
5. All Thai visible text must pass spelling, vowel/tone-mark, spacing, terminology, and age-appropriateness checks.
6. Slot count must equal requested `SLOT_COUNT`.
7. Center content must not overlap answer slots.
8. Slots must be large enough for real student writing.
9. Decorations must not overlap academic text or answer areas.
10. The selected object/theme must not distort the intended activity.
11. Open-ended topics must be converted into short-answer-compatible activities before prompt generation.
12. Generated prompt must explicitly state page size, orientation, subject, grade, topic, activity, slot count, object/theme, layout family, monochrome rules, safe margins, and no-overlap constraints.

## Multi-subject regression set

- Thai: ป.1 สระอา, 8 slots, pizza
- Thai: ป.3 มาตราตัวสะกด, 10 slots, flower
- Math: ป.2 แม่ 4, 12 slots, wheel
- English: Animals vocabulary, 10 slots, zoo
- Science: plant parts, 6 slots, flower
- Science: solar system, 8 slots, orbit
- Social studies: continents, 7 slots, world-map theme

## Visual regression

PASS when:
- simple line art
- white background
- clean outline
- low ink
- child-friendly
- coloring-friendly
- no dense shading
- no clutter
- no text collisions
- no tiny unusable slots
