from dataclasses import dataclass

@dataclass
class UserContext:
    token: str
    session_id: str | None = None
