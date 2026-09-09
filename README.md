# Projections of Earth's Technosphere: Civilization Collapse-Recovery Dynamics and Detectability

Code and manuscript for a paper submitted to Acta Astronautica, modeling collapse-recovery dynamics across ten plausible futures for Earth-originating civilization and their implications for technosignature detectability.

## Layout

- `tex/` LaTeX sources
- `bibliography/` BibTeX references
- `notebooks/` Jupyter notebooks (simulations, figures, analyses)
- `figures/` generated figures

## Reproduce

Requires Python 3.9+ (NumPy, Pandas, SciPy, Matplotlib, Jupyter) and TeX Live.

```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/figures.ipynb
jupyter nbconvert --to notebook --execute --inplace notebooks/si_analysis.ipynb
```

The scenarios follow [Haqq-Misra et al. (2025)](https://doi.org/10.1016/j.techfore.2025.124194).
