import pytest
from clients.payments_client import PaymentsClient
from tests.payments.assertions.common_asserts import assert_client_error


@pytest.mark.payments
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"amount": 0},
        {"amount": -100},
        {"amount": "100"},
    ],
    ids=[
        "empty_payload",
        "zero_amount",
        "negative_amount",
        "amount_as_string",
    ],
)
def test_payout_native_invalid_amount(bt_authorized_client, payload):
    client = PaymentsClient(bt_authorized_client)

    resp = client.post("/payments/payout/native", json=payload)

    assert_client_error(resp)
