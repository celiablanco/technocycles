TEXDIR = tex
MAIN = main.tex

.PHONY: all pdf clean

all: pdf

pdf:
	cd $(TEXDIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN)

clean:
	cd $(TEXDIR) && latexmk -C
