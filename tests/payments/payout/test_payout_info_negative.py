import pytest
from clients.payments_client import PaymentsClient
from clients.base.base_client import BaseClient
from tests.payments.assertions.common_asserts import assert_client_error


@pytest.mark.payments
def test_payout_info_unauthorized():
    """
    Запрос payout info без авторизации.
    """
    client = PaymentsClient(BaseClient())

    resp = client.get("/payments/payout/info")

    assert_client_error(resp)
