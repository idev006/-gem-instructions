# Gem Installation Guide — activity-based-elementary-worksheet

Version: 1.0.0
Target Gem baseline: 2.3.2

## 1. Main Instructions

Use the complete contents of:

`GEM_INSTRUCTIONS_PRODUCTION.md`

as the Gem's primary Instructions.

Do not replace it with a shortened summary. Baseline 2.3.2 deliberately restores the full production core and protects against accidental instruction truncation.

## 2. Knowledge Base upload

Upload supporting files according to `KB_MANIFEST.md`.

Recommended full supported-domain installation:

```text
OUTPUT_CONTRACT.md
ARCHITECTURE.md
KB_ROUTER.md
KB_MANIFEST.md
policies/PARAMETER_POLICY.md
domains/DOMAIN_REGISTRY.md
domains/INSTRUMENT_READING_ENGINE.md
domains/TIME_ENGINE.md
domains/CLOCK_READING_ENGINE.md
domains/SCALE_READING_ENGINE.md
domains/LENGTH_READING_ENGINE.md
domains/TEMPERATURE_READING_ENGINE.md
domains/CAPACITY_READING_ENGINE.md
domains/MONEY_ENGINE.md
domains/CALENDAR_ENGINE.md
domains/TABLE_GRAPH_READING_ENGINE.md
qa/ACCEPTANCE_TESTS.md
qa/PROMPT_GENERATOR_ACCEPTANCE_TESTS.md
qa/ACTUAL_RENDER_FAILURE_REGRESSION_V2_3_1.md
qa/BASELINE_2_3_2_RELEASE_CHECKLIST.md
qa/DOMAIN_RELEASE_MATRIX.md
USER_GUIDE.md
```

If the platform has a low KB-file limit, prioritize required core files, the domain engines you actually use, `INSTRUMENT_READING_ENGINE.md` for visual instruments, and the critical QA suites.

## 3. Routing behavior

The Gem must apply `KB_ROUTER.md` rather than blending every uploaded file indiscriminately.

Examples:

- elapsed time → `TIME_ENGINE.md`
- analog clock → `CLOCK_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md`
- dial scale → `SCALE_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md`
- ruler → `LENGTH_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md`
- thermometer → `TEMPERATURE_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md`
- capacity/meniscus → `CAPACITY_READING_ENGINE.md` + `INSTRUMENT_READING_ENGINE.md`

`DOMAIN_REGISTRY.md` remains SSOT for domain maturity.

## 4. Expected output behavior

A normal request should produce a Prompt Package whose primary deliverable is:

`FINAL_IMAGE_GENERATION_PROMPT`

The user should be able to copy that final prompt alone into another AI/image-generation system.

The final prompt must not stop at `[ภาพ...]`, Markdown worksheet text, `TBD`, `same as above`, or missing per-item visual states.

## 5. Installation smoke tests

Run these after installation.

### Test A — elapsed time

`ป.3 หาระยะเวลาจากเวลาเริ่มต้นและเวลาสิ้นสุด 10 ข้อ ชั่วโมงเต็ม ไม่มีเฉลย`

Expected: deterministic time content + copy-ready final image prompt; no solved answers.

### Test B — clock 10:30 regression

`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลา 10:30 และเวลาครึ่งชั่วโมง ไม่มีเฉลย`

Expected final prompt must state for 10:30:
- minute hand = 180° / at 6
- hour hand = 315°
- exactly halfway between 10 and 11
- never directly on 10

### Test C — canonical scale

`ป.3 อ่านตราชั่ง 0–5 กก. ขีดละ 0.1 กก. 10 ข้อ ไม่มีเฉลย`

Expected:
- 300° active sweep
- visible 60° inactive gap
- 50 intervals / 51 active positions
- zero value ticks inside gap
- explicit no-360° substitution

### Test D — thermometer

Use a discrete minor interval. Expected target levels are exactly representable and liquid endpoints align exactly to valid ticks.

### Test E — meniscus

Use top or bottom meniscus explicitly. Expected final prompt defines the designated read point and prohibits target-value labels/arrow annotations.

## 6. Pass criteria

Installation is considered structurally correct only if:

`KB_ROUTE_QA=PASS`
`KB_COMPATIBILITY_QA=PASS`
`PROMPT_COMPLETENESS_QA=PASS`
`PROMPT_COPY_READY_QA=PASS`
`PLACEHOLDER_VISUAL_QA=PASS`
`ANSWER_LEAK_QA=PASS`
`TARGET_VALUE_LEAK_QA=PASS` when applicable
`PER_ITEM_RENDER_STATE_QA=PASS` for visual tasks

plus all selected domain-specific gates.

## 7. Important boundary

The Gem validates and releases the prompt. It does not guarantee third-party rendered pixels.

After another AI creates the worksheet image, inspect the actual artifact before classroom use. Prompt QA and artifact QA are separate stages.

## 8. Upgrade procedure

When upgrading the Gem:

1. replace the primary Instructions with the new full `GEM_INSTRUCTIONS_PRODUCTION.md`;
2. read the new `KB_MANIFEST.md`;
3. update changed required KB files;
4. keep compatible independent domain engines unless manifest/regression says otherwise;
5. run smoke tests;
6. update any external command catalog that names the old Gem baseline.

Do not mix a new core baseline with an old Output Contract/Parameter Policy/Registry unless the manifest explicitly declares that combination compatible.