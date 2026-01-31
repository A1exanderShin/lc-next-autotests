import pytest
from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"phone": ""},
        {"phone": "abc"},
        {"phone": 123},
        {"phone": "7901"},
    ],
    ids=[
        "empty_payload",
        "empty_phone",
        "non_numeric_phone",
        "phone_as_int",
        "too_short_phone",
    ]
)
def test_password_recovery_send_sms_invalid_payload(payload):
    client = AuthClient()

    resp = client.post(
        "/password_recovery/send_sms",
        json=payload
    )

    assert_client_error(resp)
