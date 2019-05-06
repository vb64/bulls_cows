.PHONY: all setup flake8 lint
# make tests >debug.log 2>&1

ifeq ($(OS),Windows_NT)
PYTHON = venv\Scripts\python.exe
else
PYTHON = ./venv/bin/python
endif

SOURCE = source
TEST = tests
COVERAGE = $(PYTHON) -m coverage
TESTS = $(TEST)/run_tests.py

all: tests

test:
	$(PYTHON) $(TESTS) test.$(T)

flake8:
	$(PYTHON) -m flake8 --max-line-length=110 --exclude=libs,sound.py $(SOURCE)
	$(PYTHON) -m flake8 --max-line-length=110 $(TEST)

lint:
	$(PYTHON) -m pylint --disable=relative-import $(SOURCE)

verbose:
	$(PYTHON) $(TESTS) verbose

coverage:
	$(COVERAGE) run $(TESTS)

html:
	$(COVERAGE) html --skip-covered

increment: clean flake8 lint
	$(PYTHON) $(TESTS) increment
	$(PYTHON) $(TESTS) combine
	$(COVERAGE) html --skip-covered
	$(COVERAGE) report --skip-covered

report:
	$(PYTHON) $(TESTS) combine
	$(COVERAGE) html --skip-covered
	$(COVERAGE) report --skip-covered

tests: flake8 lint coverage html
	$(COVERAGE) report --skip-covered

setup: setup_python setup_pip

setup_pip:
	$(PYTHON) -m pip install -r $(TEST)/requirements.txt

setup_python:
	$(PYTHON_BIN) -m virtualenv ./venv
