from clients.auth_client import AuthClient
from utils.phone_factory import generate_phone


def test_check_sms_happy_path():
    client = AuthClient()

    phone = generate_phone()
    session_id = client.check_phone(phone).json()["data"]["session_id"]

    resp = client.check_sms(session_id, 111111)

    assert resp.status_code == 200
    assert resp.json()["data"]["state"] == "REGISTER"


def test_check_sms_invalid_code():
    client = AuthClient()

    phone = generate_phone()
    session_id = client.check_phone(phone).json()["data"]["session_id"]

    resp = client.check_sms(session_id, 999999)

    assert resp.status_code == 400
