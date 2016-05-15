# Shortcuts for various tasks

# You can set these variables from the command line.
PYTHON    = python
TSCRIPT   = tests/runner.py
CMDSEP    = ";"

.PHONY: all
all: test

test:
	$(foreach testfile,$(TSCRIPT),$(PYTHON) -m unittest $(testfile) $(CMDSEP))

clean:
	rm -f `find . -type f -name \*.py[co]`
	rm -f `find . -type f -name \*.so`
	rm -f `find . -type f -name \*.~`
	rm -f `find . -type f -name \*.orig`
	rm -f `find . -type f -name \*.bak`
	rm -f `find . -type f -name \*.rej`
	rm -rf `find . -type d -name __pycache__`
	rm -rf *.core
	rm -rf *.egg-info
	rm -rf *\$testfile*
	rm -rf .coverage
	rm -rf .tox
	rm -rf build
	rm -rf dist
	rm -rf docs/_build
	rm -rf htmlcov

#TODO install:

#TODO uninstall:

coverage: install
	# Note: coverage options are controlled by .coveragerc file
	rm -rf .coverage htmlcov
	$(PYTHON) -m coverage run $(TSCRIPT)
	$(PYTHON) -m coverage report
	@echo "writing results to htmlcov/index.html"
	$(PYTHON) -m coverage html
	$(PYTHON) -m webbrowser -t htmlcov/index.html

pep8:
	@git ls-files | grep \\.py$ | xargs $(PYTHON) -m pep8

# Upload source tarball on https://pypi.python.org/pypi/psutil.
upload-src: clean
	$(PYTHON) setup.py sdist upload

# git-tag a new release
git-tag-release:
	git tag -a release-`python -c "import setup; print(setup.get_version())"` -m `git rev-list HEAD --count`:`git rev-parse --short HEAD`
	git push --follow-tags

# vim: set ts=4 sw=4 note nu list
