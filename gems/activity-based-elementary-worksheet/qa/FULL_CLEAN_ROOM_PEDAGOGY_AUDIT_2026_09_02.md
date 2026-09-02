# Full Clean-Room Pedagogy & Artifact Root-Cause Audit — 2026-09-02

Status: Production hardening audit
Scope: every UTF-8 text/code line under `gems/activity-based-elementary-worksheet` plus its GitHub Actions workflow, with focused semantic review of architecture, policies, workers, domain engines, QA evidence, regression tools, examples and installation packaging.

## Executive conclusion

The project has become strong at deterministic academic formulas, metrology, scale topology and page packing, but repeated artifact failures show that prompt correctness alone is not enough. The central remaining risks are integration, child usability, duplicated authority and downstream renderer freedom.

The target is not merely `correct answer values`; it is a worksheet that a primary-school learner can read, understand, write on and learn from without being taught a false visual rule.

## Root cause R1 — metrology was stronger than pedagogy

Existing SSOT has detailed formulas for clocks, rulers, dials, protractors, thermometers, containers and graphs. However there was no single mandatory cross-cutting contract for:
- learner cognitive load;
- age-appropriate instruction length/language;
- minimum student typography;
- writable response space;
- visual clutter/white-space control;
- item progression;
- ambiguity from a child's point of view;
- learner-simulation artifact QA.

Effect: a prompt could pass mathematical/metrology checks yet still produce a cramped, confusing or developmentally inappropriate worksheet.

Repair: `policies/PRIMARY_SCHOOL_WORKSHEET_PEDAGOGY_PROFILE.md` becomes mandatory runtime knowledge in the production package.

## Root cause R2 — prose-to-render freedom remained too large

Several actual defects occurred even when formulas were correct in SSOT:
- nonzero-minute clock hour hand snapped to the whole-hour numeral;
- weight dial omitted visible 0.1 kg graduations;
- speedometer pointer pivot drifted from the dial center;
- protractor geometry warped;
- graduated container used the wrong number of local subdivisions.

Cause: a downstream image renderer could interpret phrases such as `10 divisions`, `show 3:30`, or `standard scale` visually rather than reconstructing exact academic geometry.

Repair: for learner-read academic geometry require:

`ACADEMIC_GEOMETRY_RENDER_MODE=VECTOR_PRIMITIVE_LOCKED`
`GENERATIVE_ART_MAY_NOT_REDRAW_ACADEMIC_GEOMETRY=YES`
`CANONICAL_COORDINATE_SYSTEM_REQUIRED=YES`
`POST_LAYOUT_GEOMETRY_TRANSFORM=UNIFORM_SCALE_AND_TRANSLATE_ONLY`

High-risk instruments require explicit formulas/primitive position manifests, not prose-only geometry.

## Root cause R3 — duplicated authority and policy fragmentation

The same rules have accumulated in owner workers, domain engines, W07, W10, W08, W09, QA documents and later patch profiles. Duplication is sometimes necessary for independent audit, but duplicated normative wording can drift.

A concrete smell is `DEFAULT_PAGE_WEIGHT_DIAL_RENDER_PROFILE.md`, which combines two unrelated concerns (global page default and one specific weight-dial grammar) while both concerns already have canonical sources in `PARAMETER_POLICY.md` and `WEIGHT_DIAL_VISIBLE_TICK_SET_PROFILE.md`.

Repair:
- canonical page default remains in `PARAMETER_POLICY.md`;
- canonical visible weight-dial grammar remains in `WEIGHT_DIAL_VISIBLE_TICK_SET_PROFILE.md` + W03;
- compatibility/summary files must not become competing SSOT;
- full-line audit checks stale/current release truths and canonical ownership.

## Root cause R4 — token-presence regression is weaker than behavior

Many static suites correctly catch missing contracts but some assertions only check that required phrases/tokens exist. That prevents accidental deletion but cannot prove that a downstream render actually follows the formulas.

Repair:
- retain static token checks for compatibility;
- add independent numeric/oracle cases;
- require primitive manifests/coordinate relations for academic geometry;
- actual rendered worksheets remain subject to Artifact QA and learner-simulation QA.

## Root cause R5 — current-release metadata drift

The repository historically preserved an established 1366-case baseline while later additive suites raised the effective gate to 1430. Some validators/checklists still referred to the earlier number. This is not an academic formula error, but inconsistent release truth increases maintenance risk and can hide a missing suite from packaging.

Repair:
- define one current effective gate after every additive suite;
- keep historical counts only when explicitly labeled historical/established;
- validator, workflow, builder, release checklist and full-line audit must agree on current effective gate.

## Root cause R6 — one-page optimization can conflict with child usability

Physical packing logic prevents impossible geometry, but physical fit alone does not prove child-friendly density. A page can technically fit while text is too small, response zones are cramped or visual load is excessive.

Repair:
- page feasibility is conjunctive with pedagogy/readability/writability gates;
- if unlocked, paginate before reducing learner-facing text or writing space below profile defaults;
- default page remains A4 Portrait on every page unless explicitly overridden.

## Root cause R7 — real-world instruments can be unnecessarily complex for the lesson

Photorealistic or commercial instruments may contain dual scales, dense markings or visual details that are correct in real life but inappropriate for an introductory reading task.

Repair: use canonical teaching instruments. Examples:
- protractor single active scale unless dual-scale selection is the lesson;
- clean 2D bar graph, no 3D perspective;
- ruler with explicit endpoint projections when needed;
- one unambiguous thermometer/container reading convention;
- scale decorations never compete with graduations.

## Root cause R8 — Artifact QA must test the child's visible evidence

Metrology QA asks whether geometry is correct. Classroom usability also asks whether the learner can infer the intended answer from the visible page without hidden assumptions.

Repair: add `ARTIFACT_LEARNER_SIMULATION_QA` with visible-only checks for task comprehension, reading target, writing location, ambiguity, print readability and visible sufficiency.

## Mandatory child-centered production defaults

Unless explicitly overridden by a valid teacher request:
- page: A4 Portrait;
- pagination allowed if needed (`ONE_PAGE_LOCK=OFF`);
- P1–P3 body text target >=14 pt;
- P4–P6 body text target >=12 pt;
- title target >=18 pt;
- learner-read instrument/graph numerals target >=12 pt unless stronger domain minimum applies;
- handwritten answer clear height: P1–P3 >=8 mm, P4–P6 >=6 mm;
- concise student instruction;
- no essential meaning through color alone;
- no decoration behind text or instructional geometry;
- no unrelated complexity added to increase difficulty;
- item order avoids accidental difficulty spikes.

These are production design defaults. Explicit teacher requirements can override them only when academic/readability safety remains valid.

## Release taxonomy

`PROMPT_QA` verifies academic state, pedagogy contract, deterministic geometry specification, page plan and serialization.

`ARTIFACT_QA` verifies actual pixels/printed geometry and learner-visible usability.

`CLASSROOM_RELEASE` requires actual artifact acceptance.

Therefore:

`PROMPT_RELEASE=APPROVED` does not imply `CLASSROOM_RELEASE=READY`.

## Acceptance goal

The release is considered production-ready only when:
1. all prior regression suites still pass;
2. primary-school pedagogy regression passes;
3. repository full-line audit passes;
4. builder/ZIP verification passes;
5. exact GitHub Actions artifact is produced;
6. representative rendered UAT artifacts pass metrology + learner-simulation QA.

The system must never claim literal perfection or 100% pixel correctness without inspecting the actual rendered worksheet. The production objective is evidence-backed correctness with release blockers for any known educational defect.