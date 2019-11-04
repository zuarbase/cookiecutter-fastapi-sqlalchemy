#!/bin/bash

make requirements.txt
make

. {{cookiecutter.virtualenv_directory}}/bin/activate

# .env
echo DEBUG=true > .env

python3 -c 'import random; print("SECRET=" + "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))' >> .env
echo DATABASE_URL=sqlite:///$PWD/{{cookiecutter.project_slug}}.db?check_same_thread=False >> .env

# Alembic setup
cd {{cookiecutter.project_slug}}
alembic init alembic
cd ..
sed -i "s|script_location = alembic|script_location = $PWD/{{cookiecutter.project_slug}}/alembic|" {{cookiecutter.project_slug}}/alembic.ini
sed -i "s|sqlalchemy.url = driver://user:pass@localhost/dbname|sqlalchemy.url = sqlite:///$PWD/{{cookiecutter.project_slug}}.db|" {{cookiecutter.project_slug}}/alembic.ini

# Create database
touch $PWD/{{cookiecutter.project_slug}}.db
./manage.py initdb