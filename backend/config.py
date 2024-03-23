from attr import dataclass
from pathlib import Path

working_dir = Path(__file__).parent.resolve()
default_templates_dir: Path = working_dir.parent / "templates"
default_statics_dir: Path = working_dir.parent / "statics"
default_public_dir: Path = working_dir.parent / "public"
default_host: str = "localhost"
default_port: int = 5052


@dataclass(kw_only=True)
class Config:
    templates_dir: Path = default_templates_dir
    statics_dir: Path = default_statics_dir
    public_dir: Path = default_public_dir
    host: str = default_host
    port: int = default_port
