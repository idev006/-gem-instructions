# Primary-School Worksheet Pedagogy & Usability Profile

Version: 1.0.0
Status: Mandatory cross-cutting runtime contract
Compatible Gem baseline: 2.6.x
Applies to: Orchestrator + W01–W10 + every student worksheet prompt
Primary owners: W01 academic appropriateness + W08 learner-facing layout/readability
Release arbiter: W09

## 1. Mission

A worksheet can be mathematically correct and still be unsuitable for a primary-school learner. This profile makes learner usability, cognitive clarity, writing space, age-appropriate language and classroom print quality explicit release criteria.

`ACADEMIC_CORRECTNESS > LEARNER_COMPREHENSION > READABILITY > WRITABILITY > DECORATION > DENSITY`

The default learner is a child in Primary 1–6, not an adult technical reader.

## 2. Default page contract

When the user does not explicitly request another page size or orientation:

`PAGE_SIZE=A4`
`ORIENTATION=PORTRAIT`
`PAGE_SIZE_PROVENANCE=SYSTEM_DEFAULT`
`ORIENTATION_PROVENANCE=SYSTEM_DEFAULT`

Multiple pages are permitted when needed because `ONE_PAGE_LOCK=OFF` by default. Pagination must preserve A4 Portrait on every page unless the user explicitly overrides the page format.

Gate: `PROMPT_DEFAULT_A4_PORTRAIT_QA`.

## 3. Grade-appropriate cognitive load

Every worksheet must resolve one explicit primary learning objective. Each item should normally require one primary cognitive action unless the teacher explicitly requests multi-step work.

Default rules:
- P1–P2: direct recognition/comparison/whole-unit or one-step tasks; avoid dense scales and unnecessary mixed representations.
- P3–P4: controlled minor graduations, one- or two-step relations, explicit visual references and familiar language.
- P5–P6: broader mixed-unit/multi-step work only when aligned with the stated objective.
- Higher grade never automatically means denser or more complicated graphics.
- Do not add a secondary skill merely to make an item look harder.

Gate: `SYSTEM_PRIMARY_GRADE_APPROPRIATENESS_QA`.

## 4. Instruction clarity

Student directions must describe the action the learner actually performs, using concise grade-appropriate Thai when the worksheet is Thai.

Default target: one concise action sentence; at most two short sentences unless the learning task genuinely requires more.

Directions must not contain renderer metadata, QA language, formulas intended only for the renderer, or ambiguous pronouns/references.

Gate: `PROMPT_LEARNER_INSTRUCTION_CLARITY_QA`.

## 5. Item clarity and ambiguity control

Each item must have:
- one clear item boundary;
- one unambiguous visual/given set;
- one clearly associated response area;
- unit labels that cannot be mistaken for part of the answer;
- no competing decorative cue that looks instructional;
- no hidden assumption needed to infer the requested answer.

If two reasonable readings produce different answers, the item is invalid.

Gate: `PROMPT_LEARNER_AMBIGUITY_QA`.

## 6. Typography defaults for print

These are production readability defaults, not claims about a universal curriculum standard.

At intended A4 print size:
- P1–P3 student body text: target >=14 pt;
- P4–P6 student body text: target >=12 pt;
- primary title: target >=18 pt;
- instrument/graph numerals read by the learner: target >=12 pt unless a stronger domain minimum applies;
- Thai vowel/tone marks must remain visually distinct;
- do not reduce text below these defaults merely to force one page when pagination is unlocked.

Gate: `PROMPT_LEARNER_TYPOGRAPHY_QA`.

## 7. Writable response space

Response areas must match the expected motor/writing demand.

Default minimum clear writing height:
- P1–P3: 8 mm per handwritten response line;
- P4–P6: 6 mm per handwritten response line.

Longer numeric/unit responses receive sufficient horizontal length. A dotted answer line may not collide with a unit label or card border.

Gate: `PROMPT_LEARNER_WRITING_SPACE_QA`.

## 8. Visual load and white space

Do not maximize item density at the expense of comprehension. Preserve separation among title, directions, question numbers, instructional graphics and response zones.

Decorative art is secondary and may not:
- touch or overlap instructional geometry;
- create tick/ray/grid/pointer-like marks;
- reduce answer space;
- force smaller educational graphics;
- dominate the item visually.

When space is insufficient: reduce decoration first, then nonessential padding, then paginate. Never degrade instructional geometry or learner text.

Gates:
`PROMPT_LEARNER_VISUAL_LOAD_QA`
`PROMPT_LEARNER_DECORATION_ISOLATION_QA`.

## 9. Consistent visual grammar

Repeated items of the same lesson use consistent:
- instrument/template geometry;
- item numbering placement;
- answer format;
- unit notation;
- label style;
- hand/pointer/level conventions;
- spacing hierarchy.

Only the intended academic state changes between repeated items.

Gate: `PROMPT_LEARNER_TEMPLATE_CONSISTENCY_QA`.

## 10. Skill-focused progression

Unless the user explicitly requests random ordering, default item order should avoid abrupt difficulty spikes.

A preferred practice sequence is:
1. accessible anchor items that demonstrate the intended reading relation;
2. representative middle items;
3. a small number of more demanding but still on-objective items.

Do not make all items trivial and do not hide the target skill behind unrelated complexity.

Gate: `PROMPT_LEARNER_ITEM_PROGRESSION_QA`.

## 11. Teaching-instrument simplification

For learner-read measurement instruments, use a canonical teaching representation rather than unnecessary real-world complexity.

Examples:
- protractor: one active numeric scale by default unless dual-scale selection is the lesson;
- ruler: clear zero/reference and endpoint projection guides where the object is offset from the scale;
- weight dial: explicit 0.1 kg graduations and midpoint hierarchy;
- clock: continuous hour hand and two clearly distinguishable hand lengths;
- graph: 2D bars, exact axis, no perspective;
- thermometer/container: one unambiguous reading line/level.

Simplification may remove irrelevant decoration or competing scales, but may never remove required academic graduations.

Gate: `PROMPT_TEACHING_INSTRUMENT_SIMPLICITY_QA`.

## 12. Academic geometry render ownership

When geometry is academic data, free-form generative art must not own that geometry.

Required semantics:

`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES`
`CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES`
`POST_LAYOUT_GEOMETRY_TRANSFORM=UNIFORM_SCALE_AND_TRANSLATE_ONLY`

The final prompt must contain deterministic construction formulas or an explicit primitive/position manifest sufficient to reconstruct the academic geometry. Natural-language-only descriptions such as `draw a standard scale` are insufficient for high-risk instruments.

A decoration/image layer may surround the instrument but must not redraw ticks, labels, pointers, rays, axes or reading levels.

Gates:
`PROMPT_ACADEMIC_VECTOR_PRIMITIVE_LOCK_QA`
`PROMPT_ACADEMIC_GEOMETRY_TRANSFORM_QA`.

## 13. Print and accessibility defaults

- black/white instructional content must remain legible in ordinary photocopying;
- do not encode essential meaning by color alone;
- required lines use sufficient contrast and stroke thickness;
- avoid gray-only critical marks;
- no decorative background texture behind text or scales;
- labels must not sit on busy art.

Gate: `PROMPT_LEARNER_PRINT_CONTRAST_QA`.

## 14. Thai learner-facing language

For Thai worksheets:
- use standard Thai spelling and age-appropriate vocabulary;
- preserve vowels/tone marks;
- prefer familiar classroom terms;
- avoid mixing Thai and English units/labels inconsistently inside one response pattern unless the lesson requires it;
- keep instructions grammatically complete and concise.

Gate: `PROMPT_LEARNER_THAI_LANGUAGE_QA`.

## 15. Answer-format integrity

The response format must directly match the taught representation.

Examples:
- kg/ขีด lesson → separate kg and ขีด blanks if requested;
- day/night clock → two clearly labeled response fields for one clock;
- protractor → one degree answer blank with degree symbol/unit placed outside the writable blank;
- capacity → numeric blank plus mL/L unit;
- ruler mixed cm/mm → response fields consistent with the requested unit representation.

Do not create an answer format that requires an untaught conversion.

Gate: `PROMPT_LEARNER_ANSWER_FORMAT_QA`.

## 16. Artifact learner-simulation audit

Artifact QA must include a learner-view simulation in addition to metrology inspection:
1. Can the target item be understood without reading hidden metadata?
2. Can the learner identify where to look and where to write?
3. Is the required scale/reference visually unambiguous?
4. Is any decoration plausibly mistaken for academic data?
5. Is the text readable at intended A4 print size?
6. Does the expected answer follow from only visible information?

Any academic ambiguity or unreadable required information blocks classroom release.

Gate: `ARTIFACT_LEARNER_SIMULATION_QA`.

## 17. Release rule

For every production worksheet, applicable gates from this profile are conjunctive with academic/domain/metrology/page gates.

Any applicable FAIL or NOT_RUN means:

`PROMPT_RELEASE=BLOCKED`

Before actual artifact inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`

A prompt can be release-ready while the downstream artifact still requires visual/classroom qualification.