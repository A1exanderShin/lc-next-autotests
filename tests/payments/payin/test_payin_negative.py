import pytest
from clients.payments_client import PaymentsClient
from clients.base.base_client import BaseClient
from tests.payments.assertions.common_asserts import assert_client_error


@pytest.mark.payments
def test_payin_unauthorized():
    """
    Попытка payin без JWT.
    """
    client = PaymentsClient(BaseClient())

    resp = client.post(
        "/payments/payin",
        json={
            "amount": 100,
            "service_id": 1,
        },
    )

    assert_client_error(resp)


@pytest.mark.payments
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"amount": 0, "service_id": 1},
        {"amount": -100, "service_id": 1},
        {"amount": 100},
        {"service_id": 1},
        {"amount": "100", "service_id": 1},
        {"amount": 100, "service_id": "1"},
    ],
    ids=[
        "empty_payload",
        "zero_amount",
        "negative_amount",
        "missing_service_id",
        "missing_amount",
        "amount_as_string",
        "service_id_as_string",
    ],
)
def test_payin_invalid_payload(authorized_user_client, payload):
    """
    Контрактные негативы базового payin.
    """
    client = PaymentsClient(authorized_user_client)

    resp = client.post(
        "/payments/payin",
        json=payload,
    )

    assert_client_error(resp)
