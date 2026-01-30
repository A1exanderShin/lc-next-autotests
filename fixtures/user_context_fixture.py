import pytest
from clients.auth_client import AuthClient
from config.settings import settings
from models.user_context import UserContext
from utils.phone_factory import generate_phone


@pytest.fixture(scope="session")
def user_context():
    client = AuthClient()

    phone = generate_phone()
    password = settings.default_password

    resp = client.check_phone(phone)
    assert resp.status_code == 200

    data = resp.json()["data"]
    assert data["state"] == "CHECK_SMS"
    session_id = data["session_id"]

    sms_resp = client.check_sms(session_id, 111111)
    assert sms_resp.status_code == 200

    session_id = sms_resp.json()["data"]["session_id"]

    reg_resp = client.register(session_id, password)
    assert reg_resp.status_code == 200

    token = reg_resp.json()["data"]["token"]

    return UserContext(token=token, session_id=session_id)
