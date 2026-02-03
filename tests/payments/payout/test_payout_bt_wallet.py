import pytest
from clients.payments_client import PaymentsClient
from tests.payments.payout.assertions.payout_bt_wallet_asserts import (
    assert_payout_bt_wallet_redirect,
)


@pytest.mark.payments
@pytest.mark.bt
def test_payout_bt_wallet_happy(bt_authorized_client):
    client = PaymentsClient(bt_authorized_client)

    resp = client.payout_bt_wallet(amount=1000)

    assert resp.status_code == 200
    assert_payout_bt_wallet_redirect(resp)

