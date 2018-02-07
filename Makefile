define exportdoc
import sys
from importlib import import_module
import pydoc
pydoc.isdata = lambda _: False
class MarkdownDoc(pydoc._PlainTextDoc):
    def getdocloc(self, _):
        return None
    def docmodule(self, m):
        m.__name__ += '\n\n'
        return '\n'.join(super().docmodule(m).split('\n')[:-4])

renderer = MarkdownDoc()
for m in sys.argv[1:]:
	print(renderer.docmodule(import_module(m)),
				file=open(m + '.txt', 'w'))
endef
export exportdoc

doc:
	@-mkdir docs
	@path=$$(pwd); \
	cd docs; \
	PYTHONPATH=$$path:$$PYTHONPATH python3 -c "$$exportdoc" algnuth algnuth.polynom algnuth.quadratic algnuth.jacobi algnuth.ideals

pypi: dist
	twine upload dist/*
	
dist: flake8
	-rm dist/*
	./setup.py bdist_wheel

clean:
	rm -rf algnuth.egg-info build dist

flake8:
	flake8 . --count --select=E901,E999,F821,F822,F823 --show-source --statistics

.PHONY: doc dist