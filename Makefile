.PHONY: init test test-all build publish ctest

BUILD27 = python setup.py sdist bdist_egg
BUILD33 = python3.3 setup.py bdist_egg

init:
	pip install -r requirements.txt

test:
	py.test && flake8 *.py

ctest:
	watchmedo shell-command --recursive --wait --command="make test"

test-all:
	tox

build:
	$(BUILD27)
	$(BUILD33)

publish:
	python setup.py register
	$(BUILD27) upload
	$(BUILD33) upload
