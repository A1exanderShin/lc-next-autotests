from clients.base.base_client import BaseClient


class AuthClient(BaseClient):

    def check_phone(self, phone: str):
        return self.post(
            "/auth/check_phone",
            json={"phone": phone}
        )

    def login(self, session_id: str | None, password: str, accept_offer: bool = True):
        payload = {
            "password": password,
            "accept_offer": accept_offer
        }

        if session_id is not None:
            payload["session_id"] = session_id

        return self.post("/auth/login", json=payload)

