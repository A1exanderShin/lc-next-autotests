from clients.base.base_client import BaseClient


class PaymentsClient:
    def __init__(self, client: BaseClient):
        self.client = client

    def payin_bt(self, amount: int):
        return self.client.post(
            "/payments/payin/bt",
            json={"amount": amount},
        )

    def payin_kaspi(self, amount: int):
        return self.client.post(
            "/payments/payin/kaspi",
            json={"amount": amount},
        )

    def payin_qiwi(self, amount: int):
        return self.client.post(
            "/payments/payin/qiwi",
            json={"amount": amount},
        )

    def payin_native(self, amount: int, payer_type: str = "card", payer_id: str | None = None):
        payload = {
            "amount": amount,
            "payer_type": payer_type,
        }

        if payer_id is not None:
            payload["payer_id"] = payer_id

        return self.client.post(
            "/payments/payin/native",
            json=payload,
        )

    def payin(self, amount: int, service_id: int):
        return self.client.post(
            "/payments/payin",
            json={
                "amount": amount,
                "service_id": service_id,
            },
        )

    def payout_info(self):
        return self.get("/payments/payout/info")

    def payout_native(self, amount: int, payer_type: str = "card", payer_id: str | None = None):
        payload = {
            "amount": amount,
            "payer_type": payer_type,
        }
        if payer_id:
            payload["payer_id"] = payer_id

        return self.post("/payments/payout/native", json=payload)

    def post(self, url: str, json: dict):
        return self.client.post(url, json=json)

    def get(self, url: str, params: dict | None = None):
        return self.client.get(url, params=params)


