import pytest
from clients.payments_client import PaymentsClient
from tests.payments.payin.assertions.payin_asserts import assert_payin_redirect


@pytest.mark.payments
@pytest.mark.qiwi
@pytest.mark.xfail(
    reason="Payin is unavailable on stage: API returns 400/500, reproduced manually",
    strict=False,
)
def test_payin_qiwi_happy(authorized_user_client):
    client = PaymentsClient(authorized_user_client)

    resp = client.payin_qiwi(amount=5000)

    assert resp.status_code == 200
    assert_payin_redirect(resp)
