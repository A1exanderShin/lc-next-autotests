import pytest

from clients.auth_client import AuthClient
from utils.phone_factory import generate_phone


@pytest.fixture
def fresh_user():
    """
    Создаёт нового тестового пользователя для каждого теста.
    Пользователь disposable, rollback не требуется.
    """
    auth = AuthClient()

    phone = generate_phone()
    password = "Test12345!"

    # 1. check_phone
    resp = auth.check_phone(phone)
    assert resp.status_code == 200
    session_id = resp.json()["data"]["session_id"]

    # 2. check_sms (код зашит)
    resp = auth.check_sms(session_id, 111111)
    assert resp.status_code == 200
    session_id = resp.json()["data"]["session_id"]

    # 3. register
    resp = auth.register(
        session_id=session_id,
        password=password,
    )
    assert resp.status_code == 200

    data = resp.json()["data"]

    return {
        "phone": phone,
        "password": password,
        "token": data["token"],
        "refresh_token": data["refresh_token"],
        "gambler_id": data["gambler_id"],
    }
