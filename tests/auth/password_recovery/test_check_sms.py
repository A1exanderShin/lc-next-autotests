from clients.auth_client import AuthClient
from utils.phone_factory import generate_phone
from tests.auth.assertions.common_asserts import assert_success, assert_client_error


def test_password_recovery_check_sms_happy_path():
    client = AuthClient()

    phone = generate_phone()
    session_id = client.post(
        "/password_recovery/send_sms",
        json={"phone": phone}
    ).json()["data"]["session_id"]

    resp = client.post(
        "/password_recovery/check_sms",
        json={
            "session_id": session_id,
            "sms_code": 111111
        }
    )

    assert_success(resp)


def test_password_recovery_check_sms_invalid_code():
    client = AuthClient()

    phone = generate_phone()
    session_id = client.post(
        "/password_recovery/send_sms",
        json={"phone": phone}
    ).json()["data"]["session_id"]

    resp = client.post(
        "/password_recovery/check_sms",
        json={
            "session_id": session_id,
            "sms_code": 999999
        }
    )

    assert_client_error(resp)
