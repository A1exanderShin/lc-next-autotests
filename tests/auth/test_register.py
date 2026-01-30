from clients.auth_client import AuthClient
from config.settings import settings
from utils.phone_factory import generate_phone


def test_register_happy_path():
    client = AuthClient()

    phone = generate_phone()
    password = settings.default_password

    phone_resp = client.check_phone(phone)
    assert phone_resp.status_code == 200

    phone_data = phone_resp.json()["data"]
    assert phone_data["state"] == "CHECK_SMS"

    session_id = phone_data["session_id"]

    sms_resp = client.check_sms(
        session_id=session_id,
        sms_code=111111
    )
    assert sms_resp.status_code == 200

    session_id = sms_resp.json()["data"]["session_id"]

    register_resp = client.register(
        session_id=session_id,
        password=password
    )
    assert register_resp.status_code == 200

    data = register_resp.json()["data"]
    assert "token" in data
    assert "refresh_token" in data
    assert "gambler_id" in data
