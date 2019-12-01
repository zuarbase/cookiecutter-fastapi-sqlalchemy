from setuptools import setup, find_packages

PACKAGE = '{{cookiecutter.project_slug}}'
VERSION = '0.0.0'

setup(
    name=PACKAGE,
    version=VERSION,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'fastapi_sqlalchemy',
        'click',
    ],
    extras_require={
        'dev': [
            'sphinx',
            'aiofiles',  # only needed for starlette.staticfiles.StaticFiles
            'pytest-cov',
            'pytest-env'
        ],
        'prod': [
            'uvicorn',
            'gunicorn',
            'alembic'
        ]
    }
)