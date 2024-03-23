from aiohttp import web
from .views import setup as views_setup
from .config import Config


async def application(config: Config | None = None) -> web.Application:
    config = Config() if config is None else config
    app = web.Application()
    views_setup(app, config)
    return app
