default:
	python setup.py sdist
	python2 setup.py bdist_wheel
	rm build/lib/raise_.py
	python3 setup.py bdist_wheel

clean:
	rm -rf raise_/__pycache__ build raise.egg-info dist
	rm -f raise_/*.py[oc] raise_.py
