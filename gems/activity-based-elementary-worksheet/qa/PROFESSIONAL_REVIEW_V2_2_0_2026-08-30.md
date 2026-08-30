# Professional Review — Activity-Based Elementary Worksheet Generator v2.2.0

Date: 2026-08-30
Result: REPAIRED → v2.2.1
Review type: architecture, instructional design, metrology, render engineering, QA/governance, teacher UX

## Executive result

v2.2.0 had a strong content-first architecture, deterministic domain routing, answer separation, instrument geometry rules, day/night clock support, and global one-page intent. The review found several cross-file consistency and release-governance defects that could cause the Gem to behave differently depending on which instruction file it followed.

All identified instruction-level critical blockers in this review were repaired in v2.2.1.

## Review perspectives

The review was conducted as if by a cross-functional production team:

- primary curriculum / instructional design
- mathematics and time pedagogy
- metrology / instrument reading
- Thai-language editing
- worksheet graphic/layout design
- print production
- software architecture
- process / QA engineering
- prompt architecture
- teacher UX / product management

## Findings and repairs

### R-01 — Global one-page policy conflict — CRITICAL

Problem:
Core v2.2.0 introduced `ONE_PAGE_PREFERRED` and `ONE_PAGE_LOCK`, but `INSTRUMENT_READING_ENGINE` and `OUTPUT_CONTRACT` still contained unconditional pagination wording. A locked one-page request could therefore be silently paginated by a subtype rule.

Repair:
- global policy is authoritative;
- optimize layout/decorations/spacing first;
- when lock OFF, paginate only after optimization;
- when lock ON, page 2 is prohibited and unsafe fit returns `ONE_PAGE_FEASIBILITY_QA=FAIL` + `LAYOUT_QA=FAIL`;
- instrument engines now explicitly obey the global page policy.

### R-02 — SCALE maturity contradiction — CRITICAL

Problem:
`SCALE_READING_ENGINE.md` claimed `PRODUCTION_HARDENED` while `DOMAIN_REGISTRY.md` (SSOT) correctly listed `PRODUCTION_CANDIDATE`.

Repair:
- scale engine changed to candidate;
- registry explicitly declared authoritative;
- new `DOMAIN_MATURITY_QA` rejects future mismatches;
- deterministic-overlay evidence may be reported separately from overall maturity.

### R-03 — TIME maturity evidence mismatch — GOVERNANCE CRITICAL

Problem:
TIME was labeled hardened while `DOMAIN_RELEASE_MATRIX.md` did not document the required ≥10 actual rendered worksheet audits under the current release rule.

Repair:
- TIME overall status conservatively changed to `PRODUCTION_CANDIDATE`;
- `ACADEMIC_RULES=DETERMINISTIC_MATURE` may still be reported;
- promotion back to hardened requires documented actual-render evidence.

### R-04 — Version/status drift — HIGH

Problem:
Core, registry, output contract, engines, and policies carried different version/status assumptions.

Repair:
- canonical core → 2.2.1;
- parameter policy → 2.2.1;
- output contract → 2.2.1;
- domain registry → 2.2.1;
- instrument/clock/scale/time engines patched to aligned semantics.

### R-05 — Image-centric output contract for text-heavy worksheets — HIGH

Problem:
The contract always framed the final stage as an image-generation prompt. This could encourage Thai text/table-heavy worksheets such as elapsed time to use a nondeterministic image model for content that should be typeset deterministically.

Repair:
Added:

`RENDER_PATH=AUTO|DOCUMENT_FIRST|HYBRID|DETERMINISTIC_VECTOR|IMAGE_ONLY`

AUTO rules:
- text/table/numeric heavy → DOCUMENT_FIRST or HYBRID;
- exact instrument/graph + theme art → HYBRID;
- mostly deterministic diagram → DETERMINISTIC_VECTOR;
- IMAGE_ONLY only when academic fidelity is not threatened or explicitly requested.

The legacy section name `FINAL_IMAGE_GENERATION_PROMPT` remains for backward compatibility, but its contents follow the resolved render path.

### R-06 — Missing one-page/render-path regression coverage — HIGH

Repair:
Acceptance suite expanded from 91 to 100 tests, adding:
- default one-page preference;
- optimization-before-pagination;
- explicit one-page lock;
- safe locked infeasibility;
- instrument page-lock compliance;
- text-heavy render-path routing;
- exact-instrument render-path routing;
- registry maturity authority;
- academic maturity vs overall maturity distinction.

### R-07 — Answer leakage in visible QA prose — PREVIOUSLY FOUND / VERIFIED FIX

The visible-output sanitizer remains mandatory. When answer key is OFF, active answers may not appear anywhere in visible output, including internal notes or QA prose.

### R-08 — Clock day/night one-face/two-answer behavior — VERIFIED

`CLOCK_READING_MODE=DAY_NIGHT_PAIR` remains valid:
- one instructional clock per question;
- two answer fields;
- deterministic Thai day/night mapping;
- hour-hand interpolation preserved;
- answer pair hidden when key is OFF;
- one-page policy now applies consistently.

## v2.2.1 release behavior

Canonical pipeline:

`REQUEST → NORMALIZE → DOMAIN ROUTE → CONTENT PLAN → DETERMINISTIC VALIDATION → INTERNAL VERIFIED BLUEPRINT → STUDENT SANITIZATION → RENDER-PATH RESOLUTION → ONE-PAGE FEASIBILITY → LAYOUT CAPACITY → RENDER PLAN → PROMPT COMPILE → VISIBLE-OUTPUT SANITIZER → QA → RELEASE`

Global defaults:

- A4 portrait
- target one page
- one-page preferred YES
- one-page lock OFF unless explicitly requested
- answer key OFF
- render objective STUDENT_WORKSHEET
- render path AUTO

## Remaining evidence backlog

Instruction architecture is repaired, but overall domains should not be promoted to HARDENED without evidence.

Priority:

1. TIME — ≥10 actual DOCUMENT_FIRST/HYBRID render audits;
2. CLOCK — actual render audit including DAY_NIGHT_PAIR and 1-page layouts;
3. SCALE — full hybrid composite audit;
4. LENGTH — 1 mm printed tick-spacing audit;
5. TEMPERATURE/CAPACITY — actual level/scale render audits;
6. DATA_READING — deterministic visualization audit.

## Review verdict

Instruction architecture after repair: **PASS for v2.2.1 baseline**.

Overall domain production maturity: governed by `domains/DOMAIN_REGISTRY.md`; no domain should be called hardened unless `qa/DOMAIN_RELEASE_MATRIX.md` evidence is satisfied.
