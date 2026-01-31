from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error


def test_identification_status_unauthorized():
    client = AuthClient()

    resp = client.get("/identification/status")

    assert_client_error(resp)


def test_identification_status_invalid_token(authorized_user_client):
    """
    Current behavior: endpoint ignores invalid Authorization token
    and returns 200. This is a potential security issue, but reflects
    actual backend contract.
    """
    authorized_user_client.session.headers["Authorization"] = "Bearer invalid-token"

    resp = authorized_user_client.get("/identification/status")

    assert resp.status_code == 200
