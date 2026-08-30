# TABLE_GRAPH_READING_ENGINE — Tables, Pictographs, Bar Graphs

Version: 1.0.0
Status: PRODUCTION_CANDIDATE

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

## Pictograph invariants

- key explicitly states one icon's value
- partial icons only if grade/objective supports them
- icon counts exactly map to canonical data
- decorative icons outside the plot cannot be mistaken for data marks

## Preferred rendering

Use deterministic SVG/vector graph generation when possible.

## QA

`DATASET_QA, TABLE_ALIGNMENT_QA, AXIS_SCALE_QA, BAR_HEIGHT_QA, PICTOGRAPH_KEY_QA, ICON_COUNT_QA, LABEL_QA, VISUAL_AMBIGUITY_QA`

Any mismatch between data and visualization blocks release.