import pytest
from tests.auth.assertions.common_asserts import assert_client_error


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"oldPassword": "123"},
        {"newPassword": "12345678"},
        {"oldPassword": "", "newPassword": "12345678"},
    ],
    ids=[
        "empty_payload",
        "no_new_password",
        "no_old_password",
        "empty_old_password",
    ]
)
def test_change_password_invalid_payload(authorized_user_client, payload):
    resp = authorized_user_client.post("/user/password", json=payload)

    assert_client_error(resp)


def test_change_password_invalid_old_password(authorized_user_client):
    resp = authorized_user_client.post(
        "/user/password",
        json={
            "oldPassword": "WRONG_PASSWORD",
            "newPassword": "12345678",
        }
    )

    assert_client_error(resp)
