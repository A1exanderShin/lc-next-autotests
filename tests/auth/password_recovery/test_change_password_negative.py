import pytest
from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"session_id": "123"},
        {"password": "11111111"},
        {"session_id": "123", "password": ""},
        {"session_id": "", "password": "11111111"},
        {"session_id": "123", "password": "123"},
    ],
    ids=[
        "empty_payload",
        "no_password",
        "no_session_id",
        "empty_password",
        "empty_session_id",
        "too_short_password",
    ]
)
def test_password_recovery_change_password_invalid_payload(payload):
    client = AuthClient()

    resp = client.post(
        "/password_recovery/change_password",
        json=payload
    )

    assert_client_error(resp)


def test_password_recovery_change_password_wrong_state():
    client = AuthClient()

    resp = client.post(
        "/password_recovery/change_password",
        json={
            "session_id": "invalid-session",
            "password": "11111111"
        }
    )

    assert_client_error(resp)
