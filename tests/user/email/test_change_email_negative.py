import pytest
from tests.auth.assertions.common_asserts import assert_client_error


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"newEmail": "not-an-email"},
        {"newEmail": ""},
    ],
    ids=[
        "empty_payload",
        "invalid_email",
        "empty_email",
    ]
)
def test_change_email_invalid_payload(authorized_user_client, payload):
    resp = authorized_user_client.post("/user/email", json=payload)

    assert_client_error(resp)
