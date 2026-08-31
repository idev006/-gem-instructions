# Runtime UAT Clock Regression — 2.6.x

Status: Critical installed-Gem prompt-generation regression
Owner: `W02_TIME_CLOCK`
Integration owner: Orchestrator + `W09_QA_RELEASE`
Executable gate: `tools/runtime_uat_regression_suite.py`

## Origin

A real installed-Gem UAT using:

`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ไม่มีเฉลย`

produced structurally plausible output but violated canonical runtime behavior. Observed failures included:

- one generic answer line instead of two day/night fields;
- implicit `ONE_PAGE_LOCK=ON` without teacher provenance;
- relational clock wording without exact numeric angles;
- allowance to reduce canonical clock graduations merely to fit layout.

The defect showed that static worker rules alone were insufficient; the runtime-critical profile must be explicit at Orchestrator instruction level and permanently regression-tested.

## Canonical runtime source

`policies/THAI_P3_CLOCK_RUNTIME_PROFILE.md`

The package builder must embed this profile into the main Orchestrator Instructions and the relevant W02/W09 Knowledge bundles.

## UAT-01 — Thai P3 AUTO mode

Generic Thai P3 analog-clock reading resolves to:

`CLOCK_READING_MODE=DAY_NIGHT_PAIR`

unless explicit SINGLE/AM-only/PM-only intent exists.

## UAT-02 — one clock, two interpretations

Each question contains exactly one analog clock face and one shared hand state.

## UAT-03 — exactly two student answer fields

Required default student response format:

`กลางวัน ........ น. | กลางคืน ........ น.`

A single generic answer line is FAIL.

## UAT-04 — strict half-hour target set

Wording such as `เน้นเวลาครึ่งชั่วโมง` resolves to:

`TARGET_MINUTE_MODE=EXACT_MINUTE_SET`
`TARGET_MINUTE_SET={30}`

No `:00` target is allowed unless the teacher explicitly asks for mixed whole-hour items.

## UAT-05 — page-lock provenance

Default remains:

`TARGET_PAGE_COUNT=1`
`ONE_PAGE_PREFERRED=YES`
`ONE_PAGE_LOCK=OFF`

`ONE_PAGE_LOCK=ON` without explicit one-page teacher wording is FAIL.

## UAT-06 — exact numeric minute angle

For every `h:30` item:

`minute_angle=180°`

must be serialized in renderer-only state.

## UAT-07 — exact numeric hour angle

For every `h:30` item:

`hour_angle=(30*(h mod 12)+15) mod 360`

must be serialized in renderer-only state.

Relational wording alone is insufficient.

## UAT-08 — relational wording retained

Numeric angles do not replace semantic/relational wording. Each item still states the intended hand relation, such as exact midpoint between adjacent hour numerals.

## UAT-09 — item-specific hard negative

Every high-risk clock state includes an item-specific negative constraint preventing the known wrong placement.

Example for 10:30: hour hand must not point directly at 10.

## UAT-10 — canonical topology preservation

Do not reduce the configured canonical full-minute clock face to only 5-minute ticks merely because page space is tight.

Reduce decoration or paginate when unlocked before degrading instructional topology.

## UAT-11 — profile embedded at runtime

The install package must embed the mandatory Thai P3 clock runtime profile in:

- Main Orchestrator Instructions;
- W02 runtime Knowledge bundle;
- W09 runtime Knowledge bundle.

## UAT-12 — W02/W09 consistency

W02 ownership rules and W09 release gates must agree on Thai P3 AUTO day/night behavior, strict half-hour semantics, numeric-angle requirements, Student Blueprint isolation and page-lock provenance.

## Release rule

Any applicable failure above blocks prompt release and package release.

The executable regression suite must report:

`12/12 PASS`

before the combined release gate can reach:

`449 + 360 + 12 = 821/821 PASS`

## Artifact boundary

These checks protect installed-Gem prompt behavior. They do not prove downstream pixels.

Before actual rendered worksheet inspection:

`ARTIFACT_QA=NOT_YET_TESTED`
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`
