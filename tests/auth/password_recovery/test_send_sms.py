from clients.auth_client import AuthClient
from utils.phone_factory import generate_phone
from tests.auth.assertions.common_asserts import assert_success
from tests.auth.assertions.auth_asserts import assert_has_session_id


def test_password_recovery_send_sms_happy_path():
    client = AuthClient()

    phone = generate_phone()
    resp = client.post(
        "/password_recovery/send_sms",
        json={"phone": phone}
    )

    assert_success(resp)
    assert_has_session_id(resp)
