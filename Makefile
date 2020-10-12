default:
	python setup.py sdist
	python setup.py bdist_wheel --python-tag py2
	rm build/lib/raise_.py
	python setup.py bdist_wheel --python-tag py3

clean:
	rm -rf __pycache__ build *.egg-info dist
	rm -f *.py[oc] raise_.py MANIFEST
