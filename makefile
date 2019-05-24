.PHONY: all setup flake8 lint
# make tests >debug.log 2>&1

ifeq ($(OS),Windows_NT)
PYTHON = venv\Scripts\python.exe
GCLOUD = $(LOCALAPPDATA)\Application Data\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd
else
PYTHON = ./venv/bin/python
GCLOUD = gcloud
endif

SOURCE = source
TEST = tests
LIBDIR = $(SOURCE)/libs
COVERAGE = $(PYTHON) -m coverage
TESTS = $(TEST)/run_tests.py
VERSION = num2word

all: tests

test:
	$(PYTHON) $(TESTS) test.$(T)

flake8:
	$(PYTHON) -m flake8 --max-line-length=110 --exclude=libs $(SOURCE)
	$(PYTHON) -m flake8 --max-line-length=110 $(TEST)

lint:
	$(PYTHON) -m pylint --disable=relative-import $(SOURCE)
	$(PYTHON) -m pylint $(TEST)/test

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

deploy: tests
	$(GCLOUD) app deploy --quiet --project $(BULLS_COWS_GAE_ID) -v $(VERSION) $(SOURCE)/app.yaml $(SOURCE)/backend.yaml $(SOURCE)/cron.yaml $(SOURCE)/index.yaml $(SOURCE)/queue.yaml

setup: setup_python setup_pip

setup_pip:
	$(PYTHON) -m pip install -r $(TEST)/requirements.txt
	$(PYTHON) -m pip install -t $(LIBDIR) -r $(LIBDIR)/requirements.txt

setup_python:
	$(PYTHON_BIN) -m virtualenv ./venv
