import pytest
from clients.payments_client import PaymentsClient
from clients.base.base_client import BaseClient
from tests.payments.assertions.common_asserts import assert_client_error


@pytest.mark.bt
def test_payin_bt_unauthorized():
    """
    Попытка BT payin без авторизации.
    Используем клиент без x-access-token.
    """
    unauthorized_client = PaymentsClient(BaseClient())

    resp = unauthorized_client.post(
        "/payments/payin/bt",
        json={"amount": 5000},
    )

    assert_client_error(resp)


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
def test_payin_bt_invalid_amount(bt_authorized_client, payload):
    """
    Контрактные негативы по amount.
    Проверяем только гарантированную валидацию.
    """
    client = PaymentsClient(bt_authorized_client)

    resp = client.post(
        "/payments/payin/bt",
        json=payload,
    )

    assert_client_error(resp)
