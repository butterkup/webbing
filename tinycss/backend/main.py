from aiohttp import web
from .views import setup as views_setup


async def application():
    app = web.Application()
    views_setup(app)
    return app
