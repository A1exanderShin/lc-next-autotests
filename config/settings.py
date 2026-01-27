import os
from dataclasses import dataclass

TEST_PHONE = "77000000000"
TEST_PASSWORD = "00000000"

@dataclass(frozen=True)
class Settings:
    base_url: str
    timeout: int = 10


settings = Settings(
    base_url=os.getenv("BASE_URL", "http://localhost:8000")
)
