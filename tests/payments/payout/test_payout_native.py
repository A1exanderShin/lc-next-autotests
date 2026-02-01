import pytest
from clients.payments_client import PaymentsClient
from tests.payments.payout.assertions.payout_asserts import assert_payout_redirect


@pytest.mark.payments
def test_payout_native_happy(bt_authorized_client):
    client = PaymentsClient(bt_authorized_client)

    resp = client.payout_native(amount=1000)

    assert resp.status_code == 200
    assert_payout_redirect(resp)
