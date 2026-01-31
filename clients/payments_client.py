from clients.base.base_client import BaseClient


class PaymentsClient:
    def __init__(self, client: BaseClient):
        self.client = client

    def payin_bt(self, amount: int):
        return self.client.post(
            "/payments/payin/bt",
            json={"amount": amount},
        )

    def post(self, url: str, json: dict):
        return self.client.post(url, json=json)
