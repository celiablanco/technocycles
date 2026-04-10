TEXDIR = tex
MAIN = main.tex
SI = supplementary.tex

.PHONY: all pdf si clean

all: pdf si

pdf:
	cd $(TEXDIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN)

si:
	cd $(TEXDIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(SI)

clean:
	cd $(TEXDIR) && latexmk -C
