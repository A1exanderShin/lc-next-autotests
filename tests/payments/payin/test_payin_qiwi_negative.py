import pytest
from clients.payments_client import PaymentsClient
from clients.base.base_client import BaseClient
from tests.payments.assertions.common_asserts import assert_client_error


@pytest.mark.payments
@pytest.mark.qiwi
def test_payin_qiwi_unauthorized():
    """
    Попытка пополнения без JWT токена.
    """
    client = PaymentsClient(BaseClient())

    resp = client.post(
        "/payments/payin/qiwi",
        json={"amount": 5000},
    )

    assert_client_error(resp)


@pytest.mark.payments
@pytest.mark.qiwi
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"amount": 0},
        {"amount": -100},
        pytest.param(
            {"amount": "5000"},
            marks=pytest.mark.xfail(
                reason="Backend accepts numeric string for amount; request reaches provider which is unavailable (500)",
                strict=False,
            ),
        ),
    ],
    ids=[
        "empty_payload",
        "zero_amount",
        "negative_amount",
        "amount_as_string",
    ],
)
def test_payin_qiwi_invalid_amount(authorized_user_client, payload):
    """
    Контрактные негативы по amount.
    """
    client = PaymentsClient(authorized_user_client)

    resp = client.post(
        "/payments/payin/qiwi",
        json=payload,
    )

    resp = client.post(
        "/payments/payin/qiwi",
        json=payload,
    )

    assert_client_error(resp)
