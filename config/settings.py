import os
from dataclasses import dataclass

DEFAULT_PASSWORD = "11111111"

@dataclass(frozen=True)
class Settings:
    base_url: str
    timeout: int = 10
    default_password: str = DEFAULT_PASSWORD


settings = Settings(
    base_url=os.getenv("BASE_URL", "http://localhost:8000")
)
