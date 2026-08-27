# Output Contract

Version: 1.1.0
Status: Active

## Default deliverables

When the execution environment supports actual file creation, a completed worksheet request targets:

1. Student worksheet
   - A4
   - Portrait unless requested otherwise
   - Thai as the primary visible language
   - black-and-white / monochrome by default
   - no answers visible
   - safe print margins
   - adequate handwriting space

2. Answer key
   - generated from the same problem data
   - question order identical to the student worksheet
   - answers mathematically validated
   - Thai labels/instructions checked for correctness

3. Optional preview
   - PNG/JPG for inspection only
   - not the source of truth

4. Optional QA metadata
   - worksheet ID
   - generator/instruction version
   - validation status

## Truthfulness

Never claim a PDF, DOCX, preview, or download exists unless it was actually created in the current environment.

## A4 baseline

```text
Page size: 210 × 297 mm
Orientation: Portrait
Preferred safe margin: 10–12 mm
Background: white
Print mode: monochrome / low-ink / photocopy-safe
```

## Thai-first rule

Thai is the default visible language for worksheet titles, instructions, labels, example text, self-assessment, teacher areas, and answer-key labels unless the user explicitly requests otherwise.

Thai-language correctness is a critical QA gate. Before final delivery, check spelling, vowel and tone marks, spacing, clarity, terminology consistency, and age appropriateness.

## Monochrome rule

The default worksheet must be usable in pure black-and-white printing.

- no required color fill
- no colored backgrounds by default
- no meaning communicated by color alone
- high-contrast text and lines
- low ink usage
- photocopy-safe

## Illustration rule

If illustrations or characters are included, they must default to:

- simple black-and-white line art
- clear, bold outlines
- minimal detail
- child-friendly forms
- coloring-friendly open areas
- no dense shading, realistic rendering, or visually busy textures

Illustrations must not collide with instructional text, calculation grids, numbers, or handwriting areas.

## Student-page rules

- no hidden or visible final answers
- correct place-value alignment
- grid sized to the operation
- no illustration collision with instructional content
- numbering continuous and complete
- Thai instructional text correct
- black-and-white readability acceptable

## Answer-key rules

- derive from the same source problem objects
- never regenerate answers from rendered artwork
- question count and numbering must match exactly
- Thai labels and explanatory text must be checked before delivery

## Completion rule

`READY TO PRINT` may be used only after critical math, Thai-language, layout, monochrome, and illustration QA pass.