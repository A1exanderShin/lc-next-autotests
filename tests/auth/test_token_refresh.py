from clients.auth_client import AuthClient
from config.settings import settings
from utils.phone_factory import generate_phone


def test_token_refresh_happy_path():
    client = AuthClient()

    phone = generate_phone()
    password = settings.default_password

    # register flow
    phone_resp = client.check_phone(phone)
    session_id = phone_resp.json()["data"]["session_id"]

    sms_resp = client.check_sms(session_id, 111111)
    session_id = sms_resp.json()["data"]["session_id"]

    reg_resp = client.register(session_id, password)
    reg_data = reg_resp.json()["data"]

    token = reg_data["token"]
    refresh_token = reg_data["refresh_token"]

    refresh_resp = client.token_refresh(
        token=token,
        refresh_token=refresh_token
    )

    assert refresh_resp.status_code == 200


def test_token_refresh_invalid_token():
    client = AuthClient()

    response = client.token_refresh(
        token="invalid-token",
        refresh_token="invalid-refresh-token"
    )

    assert response.status_code >= 400

