import pytest
from clients.payments_client import PaymentsClient
from tests.payments.payin.assertions.payin_asserts import (
    assert_payin_redirect,
    assert_payin_sms_step,
)


@pytest.mark.bt
def test_payin_bt_happy_with_existing_token(bt_authorized_client):
    """
    Happy-path BT payin для учётки с уже существующим BT токеном.
    Ожидаем немедленный redirect.
    """
    client = PaymentsClient(bt_authorized_client)

    resp = client.payin_bt(amount=5000)

    assert resp.status_code == 200
    assert_payin_redirect(resp)


@pytest.mark.bt
@pytest.mark.xfail(
    reason="BT test account already has active token; SMS_CODE step is unreachable",
    strict=True,
)
def test_payin_bt_without_token_returns_sms_step(bt_authorized_client):
    """
    Теоретический сценарий: отсутствие BT токена.
    На тестовой учётке шаг SMS_CODE недостижим из-за активного токена.
    """
    client = PaymentsClient(bt_authorized_client)

    resp = client.payin_bt(amount=5000)

    assert resp.status_code == 200
    assert_payin_sms_step(resp)
