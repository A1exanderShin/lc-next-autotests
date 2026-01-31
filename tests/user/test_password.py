from clients.auth_client import AuthClient
from tests.auth.assertions.common_asserts import assert_success, assert_client_error


def test_change_password_happy_path(authorized_fresh_user_client, fresh_user):
    new_password = "NewPass12345!"
    auth = AuthClient()

    # 1. Меняем пароль
    resp = authorized_fresh_user_client.post(
        "/user/password",
        json={
            "oldPassword": fresh_user["password"],
            "newPassword": new_password,
        }
    )
    assert_success(resp)

    # 2. Старый пароль НЕ работает (даже после check_phone)
    resp = auth.check_phone(fresh_user["phone"])
    session_id = resp.json()["data"]["session_id"]

    resp = auth.login(session_id, fresh_user["password"])
    assert_client_error(resp)

    # 3. Новый пароль работает (после check_phone)
    resp = auth.check_phone(fresh_user["phone"])
    session_id = resp.json()["data"]["session_id"]

    resp = auth.login(session_id, new_password)
    assert_success(resp)
