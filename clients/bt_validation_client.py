from clients.base.base_client import BaseClient


class BtValidationClient(BaseClient):
    """
    BT validation client.
    All endpoints are POST.
    Auth via x-access-token.
    """

    def start(self, access_token: str):
        return self.post(
            "/bt_validation/start",
            json={},
            headers={"x-access-token": access_token},
        )

    def check_sms(self, access_token: str, pin: str):
        return self.post(
            "/bt_validation/check_sms",
            json={"pin": pin},
            headers={"x-access-token": access_token},
        )

    def status(self, access_token: str):
        return self.post(
            "/bt_validation/status",
            json={},
            headers={"x-access-token": access_token},
        )
