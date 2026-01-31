from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_success
from utils.phone_factory import generate_phone
from config.settings import settings


def test_register_happy_path():
    client = AuthClient()

    phone = generate_phone()
    password = settings.default_password

    session_id = client.check_phone(phone).json()["data"]["session_id"]
    session_id = client.check_sms(session_id, 111111).json()["data"]["session_id"]

    resp = client.register(session_id, password)

    assert_success(resp)

    assert "token" in resp.json()["data"]
