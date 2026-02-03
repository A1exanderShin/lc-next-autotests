import pytest
from clients.payments_client import PaymentsClient
from tests.payments.payout.assertions.payout_asserts import assert_payout_created


@pytest.mark.payments
@pytest.mark.xfail(reason="Payout method temporarily unavailable on stage")
def test_payout_happy(bt_authorized_client):
    client = PaymentsClient(bt_authorized_client)

    resp = client.payout(
        amount=30000,      # выше минимального
        service_id=2,      # BT / test service
    )

    print(resp.status_code)
    print(resp.text)

    assert resp.status_code == 200
    assert_payout_created(resp)
