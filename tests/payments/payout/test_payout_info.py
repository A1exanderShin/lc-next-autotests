import pytest
from clients.payments_client import PaymentsClient
from tests.payments.payout.assertions.payout_asserts import assert_payout_info


@pytest.mark.payments
def test_payout_info_happy(authorized_user_client):
    """
    Happy-path:
    Получение информации по налогам и удержаниям для payout.
    """
    client = PaymentsClient(authorized_user_client)

    resp = client.get("/payments/payout/info")

    assert resp.status_code == 200
