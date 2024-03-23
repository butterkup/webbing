from aiohttp import web
from .main import application
from . import config as cfg
from pathlib import Path
import click

directory_path = click.Path(dir_okay=True, exists=True, file_okay=False, path_type=Path)


@click.command("serve_site")
@click.option(
    "--host",
    "-h",
    type=click.STRING,
    default=cfg.default_host,
    help="Host to expose site on",
)
@click.option(
    "--port",
    "-p",
    type=click.INT,
    default=cfg.default_port,
    help="Port on host to expose site on",
)
@click.option(
    "--templates-dir",
    "-T",
    type=directory_path,
    default=cfg.default_templates_dir,
    help="Mako templates to be rendered by the site",
)
@click.option(
    "--statics-dir",
    "-S",
    type=directory_path,
    default=cfg.default_statics_dir,
    help="css/js/other static files to be served for the site",
)
@click.option(
    "--public-dir",
    "-P",
    type=directory_path,
    default=cfg.default_public_dir,
    help="Source of public data like favicon.ico",
)
def serve(
    host: str, port: int, templates_dir: Path, statics_dir: Path, public_dir: Path
):
    "Serve site using the provided configuration values."
    config = cfg.Config(
        templates_dir=templates_dir,
        statics_dir=statics_dir,
        public_dir=public_dir,
        host=host,
        port=port,
    )
    web.run_app(
        application(config),
        host=host,
        port=port,
    )


if __name__ == "__main__":
    serve()
