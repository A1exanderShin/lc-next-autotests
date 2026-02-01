import pytest
from clients.payments_client import PaymentsClient
from tests.payments.payin.assertions.payin_asserts import assert_payin_redirect


@pytest.mark.payments
@pytest.mark.native
@pytest.mark.xfail(
    reason="Payin is unavailable on stage: API returns 400/500, reproduced manually",
    strict=False,
)
def test_payin_native_happy_without_saved_card(authorized_user_client):
    """
    Payin без сохранённой карты.
    """
    client = PaymentsClient(authorized_user_client)

    resp = client.payin_native(amount=5000, payer_type="card")

    assert resp.status_code == 200
    assert_payin_redirect(resp)


@pytest.mark.payments
@pytest.mark.native
@pytest.mark.xfail(
    reason="Payin is unavailable on stage: API returns 400/500, reproduced manually",
    strict=False,
)
def test_payin_native_happy_with_saved_card(authorized_user_client):
    """
    Payin с сохранённой картой.
    payer_id берётся из фикстуры/предусловий, если есть.
    """
    client = PaymentsClient(authorized_user_client)

    resp = client.payin_native(
        amount=5000,
        payer_type="card",
        payer_id="1",
    )

    assert resp.status_code == 200
    assert_payin_redirect(resp)
