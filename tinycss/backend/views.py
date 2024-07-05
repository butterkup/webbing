from aiohttp import web
from pathlib import Path


script_dir = Path(__file__).parent  # backend
working_dir = script_dir.parent  # tinycss
projects_dir = working_dir / "projects"
fonts_dir = working_dir / "fonts"


async def project(req: web.Request) -> web.StreamResponse:
    project_id = req.match_info.get("project_id")
    project_path = f"/projects/chapter_{project_id}/index.html"
    return web.HTTPMovedPermanently(project_path)


routes = (
    web.get(r"/project/{project_id:\d+}", project),
    web.static("/projects", projects_dir, follow_symlinks=True),
    web.static("/fonts", fonts_dir, follow_symlinks=True),
)


def setup(app: web.Application):
    app.add_routes(routes)
