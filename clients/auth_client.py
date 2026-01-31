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

    def check_sms(self, session_id: str, sms_code: int):
        return self.post(
            "/auth/check_sms",
            json={
                "session_id": session_id,
                "sms_code": sms_code
            }
        )

    def register(self, session_id: str, password: str):
        return self.post(
            "/auth/register",
            json={
                "session_id": session_id,
                "password": password
            }
        )

    def token_refresh(self, token: str, refresh_token: str):
        return self.post(
            "/auth/token_refresh",
            json={
                "token": token,
                "refresh_token": refresh_token
            }
        )

    def login_with_known_credentials(self, phone: str, password: str):
        """
        Логин заранее известного пользователя.
        Используется для BT и других интеграционных сценариев.
        """
        # 1. check_phone
        resp = self.check_phone(phone)
        resp.raise_for_status()

        session_id = resp.json()["data"]["session_id"]

        # 2. login
        login_resp = self.login(
            session_id=session_id,
            password=password,
        )
        login_resp.raise_for_status()

        # 3. сохраняем token в сессию
        token = login_resp.json()["data"]["token"]
        self.set_access_token(token)

        return login_resp

