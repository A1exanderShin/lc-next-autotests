import pytest
from clients.auth_client import AuthClient
from utils.phone_factory import generate_phone


def test_check_sms_happy_path():
    client = AuthClient()

    phone = generate_phone()
    resp = client.check_phone(phone)
    assert resp.status_code == 200

    data = resp.json()["data"]
    assert data["state"] == "CHECK_SMS"

    session_id = data["session_id"]

    sms_resp = client.check_sms(
        session_id=session_id,
        sms_code=111111
    )

    assert sms_resp.status_code == 200

    sms_data = sms_resp.json()["data"]
    assert sms_data["state"] == "REGISTER"


def test_check_sms_invalid_code():
    client = AuthClient()

    phone = generate_phone()
    resp = client.check_phone(phone)
    session_id = resp.json()["data"]["session_id"]

    sms_resp = client.check_sms(
        session_id=session_id,
        sms_code="000000"
    )

    assert 400 <= sms_resp.status_code < 500
