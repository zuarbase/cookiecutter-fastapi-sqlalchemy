from {{cookiecutter.project_slug}}.main import app


@app.get('/api/config')
async def get_config() -> dict:
    return {}
