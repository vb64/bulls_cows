.PHONY: all setup run
# make tests >debug.log 2>&1
ifeq ($(OS),Windows_NT)
GCLOUD = $(LOCALAPPDATA)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd
PYTHON = venv/Scripts/python.exe
else
GCLOUD = gcloud
PYTHON = ./venv/bin/python
endif

SOURCE = source
TESTS = tests
DFLT = $(SOURCE)/default
PIP = $(PYTHON) -m pip install
DEPLOY = $(GCLOUD) app deploy --project
FLAKE8 = $(PYTHON) -m flake8
LINT = $(PYTHON) -m pylint
PEP257 = $(PYTHON) -m pep257

PRJ = bulls-cows-240515
VERSION = py3

all: run

tests: flake8 pep257 lint

flake8:
	$(FLAKE8) $(DFLT)

pep257:
	$(PEP257) $(DFLT)

lint:
	$(LINT) $(DFLT)

run:
	$(PYTHON) $(DFLT)/bull_cows.py imcheater

deploy:
	$(DEPLOY) $(PRJ) --version $(VERSION) $(DFLT)/app.yaml

cron:
	$(DEPLOY) $(PRJ) $(SOURCE)/cron.yaml

setup: setup_python setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r $(DFLT)/requirements.txt
	$(PIP) -r $(TESTS)/requirements.txt

setup_python:
	$(PYTHON_BIN) -m venv ./venv
