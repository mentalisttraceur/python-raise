default:
	python setup.py sdist bdist_wheel

clean:
	rm -rf raise_/__pycache__ raise_/*.py[oc] build raise.egg-info dist
