import pytest
from clients.payments_client import PaymentsClient
from clients.base.base_client import BaseClient
from tests.payments.assertions.common_asserts import assert_client_error


@pytest.mark.payments
@pytest.mark.native
def test_payin_native_unauthorized():
    """
    Попытка payin без JWT.
    """
    client = PaymentsClient(BaseClient())

    resp = client.post(
        "/payments/payin/native",
        json={
            "amount": 5000,
            "payer_type": "card",
        },
    )

    assert_client_error(resp)


@pytest.mark.payments
@pytest.mark.native
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"amount": 0, "payer_type": "card"},
        {"amount": -100, "payer_type": "card"},
        {"amount": "5000", "payer_type": "card"},
        {"amount": 5000},  # нет payer_type
    ],
    ids=[
        "empty_payload",
        "zero_amount",
        "negative_amount",
        "amount_as_string",
        "missing_payer_type",
    ],
)
def test_payin_native_invalid_payload(authorized_user_client, payload):
    """
    Контрактные негативы native payin.
    """
    client = PaymentsClient(authorized_user_client)

    resp = client.post(
        "/payments/payin/native",
        json=payload,
    )

    assert_client_error(resp)
