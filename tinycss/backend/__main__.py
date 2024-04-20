from .main import application
from aiohttp import web
import click

HOST = "localhost"
PORT = 3000


@click.command
@click.option("--host", "-H", default=HOST)
@click.option("--port", "-P", type=int, default=PORT)
def main(host: str, port: int):
    web.run_app(application(), host=host, port=port)


if __name__ == "__main__":
    main()
