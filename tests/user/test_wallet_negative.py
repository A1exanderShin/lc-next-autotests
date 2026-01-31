from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error


def test_get_user_wallet_unauthorized():
    client = AuthClient()

    resp = client.get("/user/wallet")

    assert_client_error(resp)
