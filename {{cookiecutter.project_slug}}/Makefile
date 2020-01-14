SHELL := /bin/bash

all: flake8 coverage
.PHONY: all

flake8:
	flake8 {{cookiecutter.project_slug}} setup.py manage.py tests
.PHONY: flake8

test:
	pytest -xv tests
.PHONY: test

coverage:
	pytest --cov={{cookiecutter.project_slug}} --cov-report=term-missing --cov-fail-under=100 tests/
.PHONY: coverage

requirements.txt:
	python3 -m venv {{cookiecutter.virtualenv_directory}}
	source {{cookiecutter.virtualenv_directory}}/bin/activate && \
		pip3 install --upgrade pip && \
		pip3 install git+https://github.com/zuarbase/fastapi-sqlalchemy#egg=fastapi-sqlalchemy[dev,prod] && \
		pip3 install -e .[dev,prod] && \
	{{cookiecutter.virtualenv_directory}}/bin/pip3 freeze | egrep -v "{{cookiecutter.project_slug}}|pkg-resources" > $@
