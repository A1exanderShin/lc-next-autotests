from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_client_error, assert_success
from utils.phone_factory import generate_phone


def test_check_sms_happy_path():
    client = AuthClient()

    phone = generate_phone()
    session_id = client.check_phone(phone).json()["data"]["session_id"]

    resp = client.check_sms(session_id, 111111)

    assert_success(resp)

    assert resp.json()["data"]["state"] == "REGISTER"


def test_check_sms_invalid_code():
    client = AuthClient()

    phone = generate_phone()
    session_id = client.check_phone(phone).json()["data"]["session_id"]

    resp = client.check_sms(session_id, 999999)

    assert_client_error(resp)