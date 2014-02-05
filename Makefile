init:
	pip install -r requirements.txt

test:
	py.test

publish:
	python setup.py register
	python setup.py sdist bdist_egg upload
