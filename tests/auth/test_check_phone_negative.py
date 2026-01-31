import pytest
from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error
from utils.phone_factory import generate_phone


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
        "no_phone",
        "empty_phone",
        "non_numeric",
        "int_phone",
        "too_short",
    ]
)
def test_check_phone_invalid_payload(payload):
    client = AuthClient()

    resp = client.post("/auth/check_phone", json=payload)

    assert_client_error(resp)

def test_check_phone_rate_limit():
    client = AuthClient()
    phone = generate_phone()

    client.check_phone(phone)
    resp = client.check_phone(phone)

    assert_client_error(resp)