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
	virtualenv -p python3 {{cookiecutter.virtualenv_directory}}
	{{cookiecutter.virtualenv_directory}}/bin/pip3 install git+https://github.com/zuarbase/fastapi-sqlalchemy#egg=fastapi-sqlalchemy[dev,prod]
	{{cookiecutter.virtualenv_directory}}/bin/pip3 install -e .[dev,prod]
	{{cookiecutter.virtualenv_directory}}/bin/pip3 freeze | egrep -v "{{cookiecutter.project_slug}}|pkg-resources" > $@
