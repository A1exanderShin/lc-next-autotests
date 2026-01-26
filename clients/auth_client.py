from clients.base.base_client import BaseClient


class AuthClient(BaseClient):

    def check_phone(self, phone: str):
        return self.post(
            "/auth/check_phone",
            json={"phone": phone}
        )

    def login(self, session_id: str, password: str, accept_offer: bool = True):
        payload = {
            "session_id": session_id,
            "password": password,
            "accept_offer": accept_offer
        }
        return self.post("/auth/login", json=payload)
