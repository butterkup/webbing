from aiohttp import web
from .main import application


def serve(host: str, port: int):
    web.run_app(
        application(),
        host=host,
        port=port,
    )


if __name__ == "__main__":
    serve()
