from aiohttp import web


async def hello(_: web.Request):
    return web.Response(text="Hello World")


routes: list[web.RouteDef] = [
    web.get('/', hello)
]

def setup(app: web.Application):
    app.add_routes(routes)
