# Classroom Artifact Qualification UAT — Measurement Instruments

Version: 1.0.0
Applies to: Activity-Based Elementary Worksheet Generator 2.6.3-LTS
Purpose: qualify rendered worksheet artifacts before declaring classroom release

## 1. Why this UAT exists

Prompt QA proves that the worksheet-generation specification, formulas, routing, scale topology, metrology checks, and renderer instructions are internally consistent. It does **not** prove that a downstream image renderer drew every visible graduation correctly.

For learner-read instruments, the rendered scale is instructional content. A child may learn an incorrect measurement concept from one missing, extra, merged, shifted, reversed, or ambiguous graduation.

Therefore:

`ONE WRONG INSTRUCTIONAL SCALE = ARTIFACT_QA FAIL = CLASSROOM_RELEASE BLOCKED`

Do not approve an artifact because it looks attractive. Count and verify the visible construction.

## 2. Qualification target

Render **24 worksheets total**:

- 8 instrument families
- 3 independently generated worksheets per family
- 10 questions per worksheet unless the test case below says otherwise

Required families:

1. Analog clock
2. Weight dial scale
3. Ruler / linear scale
4. Protractor
5. Thermometer
6. Speedometer
7. Graduated container / meniscus
8. Graph numeric axis

A family passes qualification only when all 3 samples pass all applicable artifact checks.

## 3. How to run the test

For each test case:

1. Start a fresh generation request using the exact or semantically equivalent prompt below.
2. Save the generated worksheet image/PDF without editing the academic instrument.
3. Inspect every learner-read instrument on every page.
4. Record PASS/FAIL using the evidence form in Section 6.
5. If any one item fails, stop classroom approval for that artifact and capture the defect.
6. Send the failed artifact back for root-cause analysis and permanent regression creation.

Do not repair a failed worksheet manually and then call the original generation a PASS.

## 4. The 24 required rendered UAT cases

### A. Analog clock — 3 samples

**CLK-01**
`ป.3 อ่านนาฬิกาเข็ม 10 ข้อ เน้นเวลาครึ่งชั่วโมง ไม่มีเฉลย ขาวดำ A4`

Inspect:
- exactly 60 distinct minute positions on a full minute face;
- 12 hour positions coincide with every fifth minute position and do not add positions;
- no duplicate wrap tick;
- minute hand at exact target mark;
- hour hand continuously displaced for nonzero minutes;
- 10:30, if present, must have minute hand at 180° and hour hand midway between 10 and 11 (315°).

**CLK-02**
`ป.4 อ่านนาฬิกาเข็มละเอียดระดับ 5 นาที 10 ข้อ ไม่มีเฉลย ขาวดำ A4`

Inspect the same topology plus exact 5-minute target alignment.

**CLK-03**
`ป.4 อ่านนาฬิกาเข็มละเอียดระดับ 1 นาที 10 ข้อ ไม่มีเฉลย ขาวดำ A4`

Inspect all 60 minute positions, target-hand alignment, label preservation, and no local tick crowding/merging.

---

### B. Weight dial scale — 3 samples

**WGT-01**
`ป.3 อ่านตราชั่งหน้าปัด 0–5 กก. ขีดละ 0.1 กก. 10 ข้อ ไม่มีเฉลย ขาวดำ A4`

Canonical check:
- 0–5 kg;
- 50 active intervals / 51 active positions;
- canonical active sweep/gap preserved;
- no value ticks in inactive gap;
- needle intersects the intended reading ring at the correct target.

**WGT-02**
`ป.3 อ่านตราชั่ง 0–5 กก. ตอบเป็นกิโลกรัมและขีด 10 ข้อ ไม่มีเฉลย`

Also verify `1 ขีด = 0.1 kg = 100 g` is visually represented consistently.

**WGT-03**
`ป.4 อ่านตราชั่งหน้าปัดหลายค่าที่ไม่ตรงเลขหลัก 10 ข้อ ไม่มีเฉลย`

Ensure minor ticks remain complete and uniform and targets do not drift to adjacent ticks.

---

### C. Ruler / linear scale — 3 samples

**RUL-01**
`ป.3 อ่านไม้บรรทัด เซนติเมตรและมิลลิเมตร 10 ข้อ ไม่มีเฉลย ขาวดำ A4`

For **every complete 1 cm span** at 1 mm resolution verify independently:
- exactly 10 equal intervals;
- exactly 11 endpoint-inclusive positions;
- exactly 9 interior positions;
- physical ruler border is not an extra graduation;
- 5 mm mark, if emphasized, reuses an existing position and does not add a tick.

**RUL-02**
`ป.4 วัดความยาวจากไม้บรรทัดโดยวัตถุไม่ได้เริ่มที่ 0 จำนวน 10 ข้อ ไม่มีเฉลย`

Verify scale topology plus object start/end alignment and `length = end - start` geometry.

**RUL-03**
`ป.4 อ่านไม้บรรทัด 0–15 ซม. ขีดละ 1 มม. 10 ข้อ ไม่มีเฉลย`

Inspect multiple separate 1 cm spans across the ruler, including near labels and endpoints, for extra/missing ticks.

---

### D. Protractor — 3 samples

**PRO-01**
`ป.4 อ่านมุมจากโพรแทรกเตอร์ 0–180° ขีดละ 1° 10 ข้อ ไม่มีเฉลย A4`

Canonical check:
- exactly 180 intervals / 181 endpoint-inclusive positions;
- one exact common origin;
- baseline exactly at selected 0°;
- target ray intersects the intended graduation;
- no perspective/skew;
- one clearly active reading direction unless dual-scale reading is explicitly being taught;
- printed reading-ring geometry remains large enough that adjacent 1° tick centers are at least 0.60 mm apart;
- production minimum width for the canonical 1° profile is 70 mm.

**PRO-02**
`ป.4 อ่านมุมจากโพรแทรกเตอร์ 0–180° มีขีด 1° และเน้นขีด 5° 10 ข้อ ไม่มีเฉลย`

Verify 5° marks are hierarchy changes on existing 1° positions, never extra positions.

**PRO-03**
`ป.5 อ่านมุมจากโพรแทรกเตอร์ 0–180° ทั้งมุมแหลม มุมฉาก มุมป้าน 10 ข้อ ไม่มีเฉลย`

Verify active-scale direction, 90° vertical geometry, and no complementary 40°/140° ambiguity.

---

### E. Thermometer — 3 samples

**TMP-01**
`ป.3 อ่านเทอร์โมมิเตอร์ 0–50°C ขีดละ 1°C 10 ข้อ ไม่มีเฉลย`

Canonical check:
- 50 intervals / 51 positions;
- uniform graduation spacing;
- major/minor hierarchy consistent;
- liquid endpoint exactly on target graduation centerline;
- no between-tick endpoint in discrete-reading mode.

**TMP-02**
`ป.4 อ่านเทอร์โมมิเตอร์ 0–100°C ขีดละ 5°C 10 ข้อ ไม่มีเฉลย`

Canonical check: 20 intervals / 21 positions plus exact endpoint/labels.

**TMP-03**
`ป.5 อ่านเทอร์โมมิเตอร์ -10 ถึง 40°C ขีดละ 1°C 10 ข้อ ไม่มีเฉลย`

Verify negative signs, zero position, direction, 50 intervals / 51 positions, and exact liquid endpoint.

---

### F. Speedometer — 3 samples

**SPD-01**
`ป.4 อ่านหน้าปัดความเร็วรถ 0–120 km/h ขีดละ 10 km/h 10 ข้อ ไม่มีเฉลย`

Canonical default check:
- 0–120 km/h;
- 240° active sweep;
- 12 intervals / 13 active positions;
- 120° inactive gap;
- no value ticks in inactive gap;
- one instructional needle;
- needle endpoint intersects exact target tick.

**SPD-02**
`ป.4 อ่านหน้าปัดความเร็วรถ 0–120 km/h มีเลขหลักทุก 20 km/h และขีดย่อยทุก 10 km/h 10 ข้อ ไม่มีเฉลย`

Verify 20 km/h marks are hierarchy/labels over the same 10 km/h topology and do not add positions.

**SPD-03**
`ป.5 เปรียบเทียบค่าความเร็วจากหน้าปัดความเร็วรถ 10 ข้อ ไม่มีเฉลย`

Verify each dial uses the identical canonical template and only the needle target changes.

---

### G. Graduated container / meniscus — 3 samples

**CAP-01**
`ป.3 อ่านปริมาตรของเหลวจากภาชนะมีสเกลหน่วย mL 10 ข้อ ไม่มีเฉลย`

Inspect:
- exact interval and position count for the configured scale;
- all graduations parallel and uniformly spaced;
- labels align to intended major marks;
- liquid level aligns with intended graduation;
- decoration does not create a second apparent scale.

**CAP-02**
`ป.4 อ่านกระบอกตวง mL โดยอ่านก้นเมนิสคัส 10 ข้อ ไม่มีเฉลย`

Also verify the configured meniscus read point is visually unambiguous and on the target level.

**CAP-03**
`ป.4 อ่านภาชนะตวงที่มีขีดย่อยหลายระดับ 10 ข้อ ไม่มีเฉลย`

Verify major/intermediate/minor hierarchy does not create extra positions.

---

### H. Graph numeric axis — 3 samples

**GRF-01**
`ป.3 อ่านกราฟแท่ง แกนค่า 0–50 เพิ่มทีละ 5 จำนวน 10 ข้อ ไม่มีเฉลย`

Inspect:
- equal numeric intervals have equal geometric spacing;
- every tick intersects the same axis baseline;
- labels align to correct ticks;
- bar endpoints align exactly to represented values.

**GRF-02**
`ป.4 อ่านกราฟแท่ง แกนค่า 0–100 เพิ่มทีละ 10 จำนวน 10 ข้อ ไม่มีเฉลย`

Verify 10 equal intervals / 11 endpoint-inclusive axis positions and exact bar mapping.

**GRF-03**
`ป.4 อ่านกราฟแท่งที่มีเส้นกริดตามขีดของแกนค่า 10 ข้อ ไม่มีเฉลย`

Verify every grid line corresponds to a real configured axis tick and no decorative line creates a false scale position.

## 5. Universal artifact inspection checklist

For **every learner-read instrument on every rendered worksheet**, mark each item PASS/FAIL:

1. Correct topology family and active range.
2. Exact interval count.
3. Exact physical tick/position count.
4. No missing tick.
5. No extra tick.
6. No duplicated tick except legitimate cyclic wrap semantics.
7. No merged/floating/detached graduation.
8. Uniform spacing for equal-value intervals.
9. Correct scale direction.
10. Common authoritative baseline/ring/arc anchoring.
11. Correct major/intermediate/minor hierarchy without adding positions.
12. Numeric labels aligned unambiguously to intended marks.
13. Pointer/hand/ray/liquid level/bar endpoint aligned exactly to target.
14. Inactive/non-scale region contains no false value ticks.
15. Physical border/edge is not mistaken for a graduation.
16. Decoration does not create scale-like marks.
17. Repeated instruments use identical canonical scale geometry.
18. No crop/perspective/skew changes academic geometry.
19. Smallest tick spacing remains distinguishable at intended print size.
20. Black-and-white photocopy remains readable.

**Any one FAIL = entire artifact FAIL.**

## 6. Evidence form — complete for each worksheet

Copy this block once per rendered worksheet:

```text
UAT_ID:
DATE:
GEM_VERSION: 2.6.3-LTS
SOURCE_PROMPT:
RENDERER/PLATFORM:
ARTIFACT_FILENAME:
PAGE_COUNT:
ITEM_COUNT:

TOPOLOGY_CHECK: PASS / FAIL
INTERVAL_COUNT_CHECK: PASS / FAIL
POSITION_COUNT_CHECK: PASS / FAIL
UNIFORM_SPACING_CHECK: PASS / FAIL
MAJOR_MINOR_HIERARCHY_CHECK: PASS / FAIL
LABEL_ALIGNMENT_CHECK: PASS / FAIL
TARGET_ALIGNMENT_CHECK: PASS / FAIL
INACTIVE_REGION_CHECK: PASS / FAIL / N/A
DECORATION_ISOLATION_CHECK: PASS / FAIL
PRINT_READABILITY_CHECK: PASS / FAIL
W07_GEOMETRY_REVIEW: PASS / FAIL
W10_METROLOGY_REVIEW: PASS / FAIL

ARTIFACT_QA: PASS / FAIL
CLASSROOM_RELEASE: APPROVED / BLOCKED
DEFECT_ITEM_IDS:
DEFECT_DESCRIPTION:
EXPECTED_GEOMETRY:
OBSERVED_GEOMETRY:
SCREENSHOT_OR_FILE_REFERENCE:
NOTES:
```

## 7. Defect severity

### P0 — Classroom blocker
Any wrong instructional scale, target mapping, graduation count, pointer/level alignment, reversed direction, or value representation.

Action: `ARTIFACT_QA=FAIL`, `CLASSROOM_RELEASE=BLOCKED`, create permanent regression before accepting a later release.

### P1 — Readability blocker
Academic geometry is technically correct but too small, merged, crowded, ambiguous, clipped, or not photocopy-safe.

Action: block classroom release until corrected.

### P2 — Non-academic cosmetic defect
Theme/decorative issue that cannot reasonably change the learner's reading of the instrument.

Action: may be corrected without changing academic state, but must never be allowed to overlap or mimic scale geometry.

## 8. Family qualification rule

For each instrument family:

`FAMILY_ARTIFACT_QUALIFICATION=PASS` only when all 3 samples PASS.

Overall classroom qualification requires:

`24/24 rendered worksheets PASS`

and zero open P0/P1 defects.

Until then:

`PROMPT_QA=PASS` may remain true,
`ARTIFACT_QA=IN_PROGRESS`,
`CLASSROOM_RELEASE=WAITING_FOR_ARTIFACT_QA`.

After all 24 pass:

`ARTIFACT_QUALIFICATION=24/24 PASS`
`CLASSROOM_RELEASE=APPROVED`

## 9. What to send back when a test fails

Please return:

1. the rendered worksheet image/PDF;
2. UAT_ID;
3. item number(s) that look wrong;
4. if possible, a crop highlighting the scale;
5. what you expected the scale to show.

The engineering workflow will then be:

`OBSERVED ARTIFACT DEFECT → ROOT CAUSE → OWNING SSOT FIX → PERMANENT REGRESSION → FULL CI → NEW INSTALLATION ARTIFACT → RE-RENDER UAT CASE`

Do not close a scale defect with prompt wording alone if the owning rule, renderer state, metrology contract, or release gate is the real cause.
