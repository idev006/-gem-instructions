# TABLE_GRAPH_READING_ENGINE — Tables, Pictographs, Bar Graphs

Version: 1.1.0
Status: PRODUCTION_CANDIDATE
Requires: `policies/SCALE_LINE_INTEGRITY_PROFILE.md` whenever a learner reads a numeric axis/scale

## Learning goals

Supports:

- read values from a simple table
- compare categories
- find greatest/least
- total selected categories
- read pictographs
- read simple bar graphs

## Core parameters

`DATASET`, `QUESTION_TYPE`, `GRAPH_TYPE=TABLE|PICTOGRAPH|BAR`, `AXIS_MIN`, `AXIS_MAX`, `AXIS_INTERVAL`, `PICTOGRAPH_KEY`, `CATEGORY_ORDER`, `ANSWER_FORMAT`

## Deterministic data-first rule

Create/validate the dataset before rendering. The graph/table is a visualization of canonical data, not a source the image model may invent.

## Table invariants

- headers aligned with data columns
- exactly one value per intended cell
- no merged-cell ambiguity unless required
- row/category labels unambiguous

## Bar graph invariants

- common zero baseline unless explicitly teaching truncated axes
- equal category spacing
- consistent scale intervals
- bar height exactly maps to canonical value
- axis labels and units visible
- no 3D/perspective bars that distort magnitude

When the learner reads a numeric graph axis, compile a canonical `SCALE_LINE_SPEC` from `SCALE_LINE_INTEGRITY_PROFILE.md`:

- axis ticks intersect the authoritative axis at exact data positions;
- equal numeric intervals use equal geometric spacing;
- major/minor hierarchy is consistent when minor ticks exist;
- labels align to their ticks without covering them;
- configured direction is monotonic;
- required tick centers remain at least the profile minimum printed separation;
- grid lines, if used, correspond exactly to axis ticks and remain visually subordinate to bars/data;
- decoration must not resemble extra ticks, bars, data points, or grid lines.

Add W07 for exact learner-read graph/axis geometry.

## Pictograph invariants

- key explicitly states one icon's value
- partial icons only if grade/objective supports them
- icon counts exactly map to canonical data
- decorative icons outside the plot cannot be mistaken for data marks

## Preferred rendering

Use deterministic SVG/vector graph generation when possible.

## QA

`DATASET_QA, TABLE_ALIGNMENT_QA, AXIS_SCALE_QA, BAR_HEIGHT_QA, PICTOGRAPH_KEY_QA, ICON_COUNT_QA, LABEL_QA, VISUAL_AMBIGUITY_QA`.

For learner-read numeric axes also require the applicable `PROMPT_SCALE_*` gates from `SCALE_LINE_INTEGRITY_PROFILE.md`, including `PROMPT_SCALE_LINE_SPEC_QA`, `PROMPT_SCALE_TICK_ANCHOR_QA`, `PROMPT_SCALE_PRINT_SEPARATION_QA`, `PROMPT_SCALE_LABEL_ALIGNMENT_QA`, `PROMPT_SCALE_TARGET_ALIGNMENT_QA`, and `PROMPT_SCALE_LINE_SERIALIZATION_QA`.

Any mismatch between data and visualization, ambiguous scale line, missing/extra axis graduation, or incorrect bar-to-axis mapping blocks release.