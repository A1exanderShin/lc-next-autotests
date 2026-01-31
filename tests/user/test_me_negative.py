from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error


def test_get_user_me_unauthorized():
    client = AuthClient()

    resp = client.get("/user/me")

    assert_client_error(resp)
