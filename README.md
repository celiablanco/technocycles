# Reproducible LaTeX Paper Workspace

This project bundles manuscript sources, bibliography, figure generation, and automation so the paper can be rebuilt end-to-end with minimal effort.

## Layout
- `tex/`: LaTeX sources (`main.tex`, `preamble.tex`, `macros.tex`, section files).
- `bibliography/`: References in BibTeX format.
- `figures/`: Auto-generated PDFs consumed by the manuscript.
- `notebooks/`: Jupyter notebook for exploratory figure generation.
- `scripts/`: Python script for figure generation.
- `data/processed/`: Placeholder for cleaned datasets.
- `.vscode/`: Editor settings for consistent LaTeX builds.
- `Makefile`: Convenience targets for building and cleaning.

## Build the manuscript
```bash
cd project
make       # runs latexmk -pdf in tex/
make clean # removes aux files in tex/
```

## Regenerate figures
- Notebook: open `notebooks/figures.ipynb`, run all cells, and verify `figures/fig1.pdf` appears.
- Script: run `python scripts/make_figures.py` from the `project/` directory.

## Notes
- The LaTeX build uses `natbib`, `hyperref`, and `cleveref` for citations and cross-references.
- Figures are expected as PDF and referenced via `\includegraphics` with labels for `\cref`.
