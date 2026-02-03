import pytest
from clients.payments_client import PaymentsClient
from clients.base.base_client import BaseClient
from tests.payments.assertions.common_asserts import assert_client_error


@pytest.mark.payments
@pytest.mark.bt
def test_payout_bt_wallet_unauthorized():
    client = PaymentsClient(BaseClient())

    resp = client.post(
        "/payments/payout/bt_wallet",
        json={"amount": 30000},
    )

    assert_client_error(resp)


@pytest.mark.payments
@pytest.mark.bt
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"amount": 0},
        {"amount": -100},
    ],
    ids=[
        "empty_payload",
        "zero_amount",
        "negative_amount",
    ],
)
def test_payout_bt_wallet_invalid_amount(bt_authorized_client, payload):
    client = PaymentsClient(bt_authorized_client)

    resp = client.post(
        "/payments/payout/bt_wallet",
        json=payload,
    )

    assert_client_error(resp)
