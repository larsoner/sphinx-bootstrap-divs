all: clean build check-manifest check-readme

build:
	sphinx-build . build/html
clean:
	rm -Rf build
	rm -Rf sphinx_boostrap_theme_collapse/__pycache__
view:
	@python -c "import webbrowser; webbrowser.open_new_tab('file://$(PWD)/build/html/index.html')"

show: view

check-manifest:
	check-manifest --ignore .circleci*,build,conf.py

check-readme:
	python setup.py check --restructuredtext --strict
