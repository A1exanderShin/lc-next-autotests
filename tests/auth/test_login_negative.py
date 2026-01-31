import pytest
from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"password": "11111111"},
        {"session_id": "123"},
        {"session_id": "123", "password": ""},
    ],
    ids=[
        "empty_payload",
        "no_session_id",
        "no_password",
        "empty_password",
    ]
)
def test_login_invalid_payload(payload):
    client = AuthClient()

    resp = client.post("/auth/login", json=payload)
    assert resp.status_code in (400, 403)


def test_login_invalid_credentials():
    client = AuthClient()

    resp = client.post(
        "/auth/login",
        json={
            "session_id": "invalid-session",
            "password": "wrong-password",
        }
    )

    assert_client_error(resp)