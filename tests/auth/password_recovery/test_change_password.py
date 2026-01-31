from clients.auth_client import AuthClient
from utils.phone_factory import generate_phone
from tests.auth.assertions.common_asserts import assert_success, assert_client_error
from config.settings import settings


def test_password_recovery_change_password_happy_path():
    client = AuthClient()

    phone = generate_phone()
    session_id = client.post(
        "/password_recovery/send_sms",
        json={"phone": phone}
    ).json()["data"]["session_id"]

    client.post(
        "/password_recovery/check_sms",
        json={
            "session_id": session_id,
            "sms_code": 111111
        }
    )

    resp = client.post(
        "/password_recovery/change_password",
        json={
            "session_id": session_id,
            "password": settings.default_password
        }
    )

    assert_success(resp)


def test_password_recovery_change_password_invalid_password():
    client = AuthClient()

    resp = client.post(
        "/password_recovery/change_password",
        json={
            "session_id": "invalid",
            "password": "123"
        }
    )

    assert_client_error(resp)
