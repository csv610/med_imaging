# Medical Imaging: What Medical Imaging Reveals About Disease

**Author:** Chaman Singh Verma  
**Format:** LaTeX book; compiled with pdfTeX (`pdflatex`)

This book explains how medical imaging modalities reveal anatomical, physiological, and pathological features of disease. It covers imaging principles, modality-specific findings, interpretation, organ-system diagnosis, emergencies, interventions, and medical-imaging applications of artificial intelligence.

## Build

Install a LaTeX distribution that provides `pdflatex`, then run these commands from the repository root:

```sh
pdflatex -interaction=nonstopmode -halt-on-error med_imaging.tex
pdflatex -interaction=nonstopmode -halt-on-error med_imaging.tex
```

The second pass updates the table of contents and cross-references. The output is `med_imaging.pdf`. The build uses the included PNG illustrations and standard LaTeX packages loaded by `med_imaging.tex`.

## Repository layout

- `med_imaging.tex` — book entry point, front matter, and chapter assembly
- `foundations/` — imaging physics, acquisition, safety, workflow, and AI foundations
- `modalities/` — modality chapters and required infographic assets
- `interpretation/` — image-reading and reporting concepts
- `organ_systems/`, `disease_imaging/`, `emergency/` — clinical applications
- `interventional/` — image-guided procedures
- `artificial_intelligence/` — AI methods and applications
- `practical/` — reading guides, cases, and reporting practice
- `chapters/` — appendices and supplementary chapters
- `scripts/` — source-maintenance utilities

## Medical and editorial notice

This is an educational reference, not a substitute for professional medical judgment or current institutional protocols. Clinical indications and recommendations should be checked against current professional guidance before use in patient care.

## Copyright and reuse

Copyright © 2026 Chaman Singh Verma. All rights reserved. No open-source license is currently granted for the book text or artwork. Contact the author for permission to reuse or redistribute material. Third-party references and resources remain subject to their respective terms.
