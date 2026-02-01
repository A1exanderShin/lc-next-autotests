import pytest
from clients.payments_client import PaymentsClient
from clients.base.base_client import BaseClient
from tests.payments.assertions.common_asserts import assert_client_error


@pytest.mark.payments
@pytest.mark.kaspi
def test_payin_kaspi_unauthorized():
    """
    Попытка payin без авторизации.
    """
    client = PaymentsClient(BaseClient())

    resp = client.post(
        "/payments/payin/kaspi",
        json={"amount": 5000},
    )

    assert_client_error(resp)


@pytest.mark.payments
@pytest.mark.kaspi
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
def test_payin_kaspi_invalid_amount(authorized_user_client, payload):
    """
    Контрактные негативы по amount.
    """
    client = PaymentsClient(authorized_user_client)

    resp = client.post(
        "/payments/payin/kaspi",
        json=payload,
    )

    assert_client_error(resp)
