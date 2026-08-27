# Output Contract

## Default deliverables

When the execution environment supports actual file creation, a completed worksheet request targets:

1. Student worksheet
   - A4
   - Portrait unless requested otherwise
   - no answers visible
   - safe print margins
   - adequate handwriting space

2. Answer key
   - generated from the same problem data
   - question order identical to the student worksheet
   - answers mathematically validated

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
Background: predominantly white
Print mode: grayscale-safe / low-ink compatible
```

## Student-page rules

- no hidden or visible final answers
- correct place-value alignment
- grid sized to the operation
- no illustration collision with instructional content
- numbering continuous and complete

## Answer-key rules

- derive from the same source problem objects
- never regenerate answers from rendered artwork
- question count and numbering must match exactly

## Completion rule

`READY TO PRINT` may be used only after critical math and layout QA pass.