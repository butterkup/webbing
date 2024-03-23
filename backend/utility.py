import aiohttp_mako as amako
from aiohttp import web, typedefs
import typing as ty


def serve_page(page: str, **kwargs) -> typedefs.Handler:
    @amako.template(page)
    async def handler(request: web.Request):
        kwargs.setdefault("request", request)
        return kwargs

    return ty.cast(typedefs.Handler, handler)
