TEXDIR = tex
MAIN = main.tex
SI = supplementary.tex
TITLEPAGE = titlepage.tex
ANONYMOUS = manuscript_anonymous.tex
BIOS = biographies.tex
COVER = coverletter.tex

.PHONY: all pdf si titlepage anonymous biographies coverletter clean

all: pdf si

pdf:
	cd $(TEXDIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN)

si:
	cd $(TEXDIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(SI)

titlepage:
	cd $(TEXDIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(TITLEPAGE)

anonymous:
	cd $(TEXDIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(ANONYMOUS)

biographies:
	cd $(TEXDIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(BIOS)

coverletter:
	cd $(TEXDIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(COVER)

clean:
	cd $(TEXDIR) && latexmk -C
