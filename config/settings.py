import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    base_url: str
    timeout: int = 10


settings = Settings(
    base_url=os.getenv("BASE_URL", "http://localhost:8000")
)
