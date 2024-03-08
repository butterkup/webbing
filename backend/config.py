from attr import dataclass
from pathlib import Path

@dataclass
class Config:
    templates_dir: Path
    statics_dir: Path
    public_dir: Path
    host: str = 'localhost'
    port: int = 8080
