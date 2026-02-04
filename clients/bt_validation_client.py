from clients.base.base_client import BaseClient


class BtValidationClient(BaseClient):
    """
    Клиент BT validation.
    Идентификация пользователя — через x-access-token.
    Тело запросов пустое (по контракту).
    """

    def start(self, access_token: str):
        return self.post(
            "/bt_validation/start",
            json={},
            headers={
                "x-access-token": access_token,
            },
        )

    def check_sms(self, access_token: str, pin: str = "000000"):
        return self.post(
            "/bt_validation/check_sms",
            json={"pin": pin},
            headers={"x-access-token": access_token},
        )

