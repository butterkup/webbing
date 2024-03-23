from pathlib import Path
from aiohttp import web
from .config import Config
import aiohttp_mako as amako
from .utility import serve_page


async def hello(_: web.Request):
    return web.Response(text="Hello World")


checking = serve_page("checking.html")


def setup_routes(statics_dir: Path, public_dir: Path) -> list[web.AbstractRouteDef]:
    return [
        web.get("/", hello),
        web.static("/static", statics_dir),
        web.static("/public", public_dir),
        web.get("/check", checking),
    ]


def setup(app: web.Application, cfg: Config):
    routes = setup_routes(cfg.statics_dir, cfg.public_dir)
    amako.setup(app, cfg.templates_dir)
    app.add_routes(routes)
