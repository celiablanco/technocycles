
#Branch for TF&SC submission

# Technological Civilization Collapse–Recovery Dynamics and Detectability

Code and manuscript for a paper modeling collapse–recovery dynamics across ten plausible futures for Earth-originating civilization, computing duty cycles and their implications for technosignature detectability and the Drake Equation.

## Repository layout

```
tex/                LaTeX sources (main.tex, supplementary.tex, sections/)
bibliography/       BibTeX references
notebooks/          Jupyter notebook for simulations and figures
figures/            Generated figures (PNG, 300 dpi)
Makefile            Build targets for manuscript PDFs
```

## Requirements

- Python 3.9+
- NumPy, Pandas, Matplotlib
- Jupyter (for notebook execution)
- TeX Live (pdflatex, bibtex, latexmk)

## Reproduce the figures

All simulations and figures are generated from a single notebook:

```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/figures.ipynb
```

This runs 200 Monte Carlo replicates per scenario and writes all figure PNGs to `figures/`.

## Build the manuscript

```bash
make pdf    # main paper
make si     # supplementary information
make all    # both
make clean  # remove build artifacts
```

Or manually:

```bash
cd tex
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

## Scenarios

The simulations are based on ten 1000-year future scenarios from [Haqq-Misra et al. (2025)](https://doi.org/10.1016/j.techfore.2025.124194), parameterized with growth rate, resource stock, depletion rate, collapse depth, recovery delay, recovery fraction, and existential hazard rate. See Table 4 in the manuscript for full parameter values.
