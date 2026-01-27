import pytest
from clients.auth_client import AuthClient
from fixtures.user_context import UserContext


@pytest.fixture(scope="session")
def user_context():
    client = AuthClient()

    phone = "77000000000"
    password = "00000000"

    # 1. check_phone
    check_phone_resp = client.check_phone(phone)
    assert check_phone_resp.status_code == 200, check_phone_resp.text

    check_data = check_phone_resp.json()["data"]
    assert check_data["state"] == "LOGIN"

    session_id = check_data["session_id"]

    # 2. login
    login_resp = client.login(
        session_id=session_id,
        password=password,
        accept_offer=True
    )
    assert login_resp.status_code == 200, login_resp.text

    login_data = login_resp.json()["data"]

    return UserContext(
        token=login_data["token"],
        session_id=session_id
    )
