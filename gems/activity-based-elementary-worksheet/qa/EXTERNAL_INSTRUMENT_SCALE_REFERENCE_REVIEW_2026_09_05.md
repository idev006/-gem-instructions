# External Instrument Scale Reference Review — 2026-09-05

Status: Reference evidence, not copied artwork
Purpose: ground the project scale/tick standard in external measurement and teaching references.

## Sources reviewed

1. NIST, SI Units — Length
   - URL: https://www.nist.gov/pml/owm/si-units-length
   - Relevant evidence: `10 millimeters (mm) = 1 centimeter (cm)`.
   - Project implication: ruler skill must treat each 1 cm span as 10 mm intervals / 11 endpoint-inclusive positions.

2. NIST, Metric Ruler / SP 376
   - URL: https://www.nist.gov/publications/nist-special-publication-376-metric-ruler
   - Relevant evidence: NIST provides metric ruler materials as educational tools for SI length measurement.
   - Project implication: ruler/measurement worksheets should follow SI unit structure and avoid decorative or approximate rulers.

3. OpenLearn, Everyday maths 2 — Reading scales
   - URL: https://www.open.edu/openlearn/mod/oucontent/view.php?id=158687&section=6.2
   - Relevant evidence: a scale numbered at every 1 kg interval with 10 steps between each numbered interval means each step is 0.1 kg.
   - Project implication: 0–5 kg dial scale at 0.1 kg resolution must use 10 intervals per 1 kg span.

4. Khan Academy, Telling time review
   - URL: https://www.khanacademy.org/math/cc-third-grade-math/time/imp-time/a/telling-time-review
   - Relevant evidence: every minute the minute hand moves one tick; the hour hand can sit between two hour numerals.
   - Project implication: analog clock skill must support minute ticks and continuous hour-hand interpretation.

5. GeeksforGeeks, Clock angle formulas
   - URL: https://www.geeksforgeeks.org/aptitude/clock-questions-aptitude/
   - Relevant evidence: analog clock is 360° divided into 12 hours and 60 minutes; hour hand moves 0.5° per minute, minute hand 6° per minute.
   - Project implication: internal deterministic clock geometry formulas are appropriate for target-to-hand mapping.

6. NIST, SI Learning Hub
   - URL: https://www.nist.gov/pml/owm/si-learning-hub
   - Relevant evidence: measurement learning depends on building familiarity and fluency with SI quantity values and units.
   - Project implication: worksheets must protect unit labels, scale consistency, and learner-readable quantity notation.

## Canonical project conclusions

- External references support treating scale structure as educational content, not decoration.
- The project must define its own canonical teaching models instead of copying a single product photo.
- Multiple real instruments may vary visually, but a primary-school worksheet must choose one internally coherent scale topology and preserve it exactly.
- For learner-read instruments, count, spacing, hierarchy, reference origin/center, and pointer/endpoint alignment are release-blocking academic evidence.

## Derived hardening actions

- Add `SCALE_TICK_STANDARD.md`.
- Add `INSTRUMENT_TICK_HIERARCHY_POLICY.md`.
- Add `INSTRUMENT_SCALE_DEFECT_TAXONOMY.md`.
- Add executable regression for scale/tick governance.
- Bind this evidence into the installer package and W09 release gate.
