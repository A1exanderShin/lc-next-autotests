import pytest
from clients.auth_client import AuthClient


@pytest.fixture(scope="session")
def bt_authorized_client():
    """
    BT payin доступен только для одной тестовой учётки.
    Ограничение платёжного провайдера.
    """
    client = AuthClient()

    client.login_with_known_credentials(
        phone="77001110005",
        password="11111111"
    )

    return client
