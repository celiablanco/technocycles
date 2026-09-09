TEXDIR = tex

.PHONY: all pdf si clean

all: pdf si

pdf:
	cd $(TEXDIR) && pdflatex -interaction=nonstopmode main && \
	bibtex main && \
	pdflatex -interaction=nonstopmode main && \
	pdflatex -interaction=nonstopmode main

si:
	cd $(TEXDIR) && pdflatex -interaction=nonstopmode supplementary && \
	pdflatex -interaction=nonstopmode supplementary

clean:
	cd $(TEXDIR) && latexmk -C
