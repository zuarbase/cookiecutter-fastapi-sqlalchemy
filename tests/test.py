import os
import shutil
import subprocess
from cookiecutter.main import cookiecutter

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__name__), ".."))
OUTPUT_DIR = "/tmp/fastapi_sqlalchemy_helloworld"
BIN_DIR = os.path.join(OUTPUT_DIR, "venv/bin")


def test():
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    cookiecutter(ROOT_DIR, no_input=True, output_dir="/tmp")

    env = os.environ.copy()
    env["PATH"] = BIN_DIR + ":" + env["PATH"]
    subprocess.run(
        "make flake8 test",
        cwd=OUTPUT_DIR, shell=True, env=env, check=True
    )

    subprocess.run(
        "./manage.py createuser --username=admin --password=test321",
        cwd=OUTPUT_DIR, shell=True, env=env, check=True
    )

    subprocess.run(
        "./manage.py setpassword --username=admin --password=test123",
        cwd=OUTPUT_DIR, shell=True, env=env, check=True
    )
