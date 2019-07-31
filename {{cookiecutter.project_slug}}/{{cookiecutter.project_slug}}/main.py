""" application main """
import logging


from fastapi_sqlalchemy import FastAPI_SQLAlchemy, middleware
from starlette.staticfiles import StaticFiles

from . import settings


logger = logging.getLogger(__name__)


def make_app() -> FastAPI_SQLAlchemy:
    """ Create an ASGI Application
    """
    logging.basicConfig()
    logging.getLogger('fastapi_sqlalchemy').setLevel(logging.INFO)

    return FastAPI_SQLAlchemy(
        str(settings.DATABASE_URL),
        title='{{cookiecutter.project_name}}',
        version='0.0.0'
    )


app = make_app()
app.add_middleware(middleware.SessionMiddleware)
app.router.default = StaticFiles(directory='static', html=True)
