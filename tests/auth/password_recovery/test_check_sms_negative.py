import pytest
from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"sms_code": 111111},
        {"session_id": "123"},
        {"session_id": "123", "sms_code": "111111"},
        {"session_id": "", "sms_code": 111111},
    ],
    ids=[
        "empty_payload",
        "no_session_id",
        "no_sms_code",
        "sms_code_as_string",
        "empty_session_id",
    ]
)
def test_password_recovery_check_sms_invalid_payload(payload):
    client = AuthClient()

    resp = client.post(
        "/password_recovery/check_sms",
        json=payload
    )

    assert_client_error(resp)


def test_password_recovery_check_sms_invalid_code():
    client = AuthClient()

    resp = client.post(
        "/password_recovery/check_sms",
        json={
            "session_id": "invalid-session",
            "sms_code": 999999
        }
    )

    assert_client_error(resp)
