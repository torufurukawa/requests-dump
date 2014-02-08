.PHONY: init test test-all build publish

init:
	pip install -r requirements.txt

test:
	py.test

test-all:
	tox

publish:
	python setup.py register
	python setup.py sdist bdist_egg upload
	python3.3 setup.py bdist_egg upload
