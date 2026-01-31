from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_success
from utils.phone_factory import generate_phone
from config.settings import settings


def test_token_refresh_happy_path():
    client = AuthClient()

    phone = generate_phone()
    password = settings.default_password

    session_id = client.check_phone(phone).json()["data"]["session_id"]
    session_id = client.check_sms(session_id, 111111).json()["data"]["session_id"]

    reg_data = client.register(session_id, password).json()["data"]

    resp = client.token_refresh(
        token=reg_data["token"],
        refresh_token=reg_data["refresh_token"]
    )

    assert_success(resp)